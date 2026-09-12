import os
import json
import logging
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import (
    roc_auc_score, average_precision_score, precision_score,
    recall_score, f1_score, confusion_matrix
)
from src.utils.paths import (
    FEATURES_PATH, CLASSICAL_MODEL_DIR, RESULTS_PATH, EVIDENCE_DIR
)
from src.models.router.escalation_router import compute_uncertainty, select_escalated_indices
from src.models.experts.quantum_expert import QuantumExpert
from src.models.experts.classical_rbf_expert import ClassicalRBFExpert
from src.models.experts.classical_gbm_expert import ClassicalGBMExpert

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_binary_metrics(y_true, y_prob, threshold=0.5):
    """
    Computes standard classification metrics at a given decision threshold.
    """
    y_pred = (y_prob >= threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    
    auc = roc_auc_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 0.5
    auprc = average_precision_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 0.0
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    return {
        "roc_auc": float(auc),
        "auprc": float(auprc),
        "precision": float(prec),
        "recall": float(rec),
        "f1": float(f1),
        "confusion_matrix": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)}
    }

def run_paired_bootstrap(y_true, prob_quantum, prob_control, n_bootstrap=1000, seed=42):
    """
    [IMPLEMENTED] Paired bootstrap hypothesis test and confidence intervals.
    Resamples the exact same test transactions with replacement for both models.
    """
    rng = np.random.RandomState(seed)
    n = len(y_true)
    
    diff_auprc = []
    diff_auc = []
    diff_f1 = []
    
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        y_b = y_true[idx]
        
        # Check if both classes are present in sample
        if len(np.unique(y_b)) < 2:
            continue
            
        q_prob_b = prob_quantum[idx]
        c_prob_b = prob_control[idx]
        
        # AUPRC diff
        q_auprc = average_precision_score(y_b, q_prob_b)
        c_auprc = average_precision_score(y_b, c_prob_b)
        diff_auprc.append(q_auprc - c_auprc)
        
        # ROC-AUC diff
        q_auc = roc_auc_score(y_b, q_prob_b)
        c_auc = roc_auc_score(y_b, c_prob_b)
        diff_auc.append(q_auc - c_auc)
        
        # F1 diff
        q_f1 = f1_score(y_b, (q_prob_b >= 0.5).astype(int), zero_division=0)
        c_f1 = f1_score(y_b, (c_prob_b >= 0.5).astype(int), zero_division=0)
        diff_f1.append(q_f1 - c_f1)
        
    diff_auprc = np.array(diff_auprc)
    diff_auc = np.array(diff_auc)
    diff_f1 = np.array(diff_f1)
    
    # 95% Bootstrap Confidence Intervals (percentile method)
    ci_auprc = (float(np.percentile(diff_auprc, 2.5)), float(np.percentile(diff_auprc, 97.5)))
    ci_auc = (float(np.percentile(diff_auc, 2.5)), float(np.percentile(diff_auc, 97.5)))
    ci_f1 = (float(np.percentile(diff_f1, 2.5)), float(np.percentile(diff_f1, 97.5)))
    
    # Empirical two-sided p-value against H0: diff == 0
    p_val_auprc = 2.0 * min(np.mean(diff_auprc <= 0), np.mean(diff_auprc >= 0))
    p_val_auprc = min(1.0, max(1.0 / len(diff_auprc), p_val_auprc))
    
    p_val_auc = 2.0 * min(np.mean(diff_auc <= 0), np.mean(diff_auc >= 0))
    p_val_auc = min(1.0, max(1.0 / len(diff_auc), p_val_auc))
    
    return {
        "n_samples": len(diff_auprc),
        "seed": seed,
        "delta_auprc": {
            "mean": float(np.mean(diff_auprc)),
            "std": float(np.std(diff_auprc)),
            "ci_95": ci_auprc,
            "p_value": float(p_val_auprc),
            "zero_in_ci": bool(ci_auprc[0] <= 0.0 <= ci_auprc[1])
        },
        "delta_roc_auc": {
            "mean": float(np.mean(diff_auc)),
            "std": float(np.std(diff_auc)),
            "ci_95": ci_auc,
            "p_value": float(p_val_auc),
            "zero_in_ci": bool(ci_auc[0] <= 0.0 <= ci_auc[1])
        },
        "delta_f1": {
            "mean": float(np.mean(diff_f1)),
            "std": float(np.std(diff_f1)),
            "ci_95": ci_f1,
            "zero_in_ci": bool(ci_f1[0] <= 0.0 <= ci_f1[1])
        }
    }

def run_full_routed_evaluation(
    budgets=(0.5, 1.0, 2.0, 5.0, 10.0),
    n_train_expert=200,
    n_bootstrap=1000,
    seed=42
):
    """
    [IMPLEMENTED] Complete Phase 21 & Phase 22 & Phase 24 Scientific Evaluation.
    Evaluates:
      A. Classical-only
      B. Classical + RBF Expert
      C. Classical + Quantum Expert (Fidelity)
      D. Classical + Quantum Expert (Projected)
      E. Classical + Strong Classical Expert (LightGBM)
      F. Classical + Random-Routing Control (RBF on random traffic)
    Under budgets 0.5%, 1%, 2%, 5%, 10%.
    """
    logging.info("Starting Full Routed-System Scientific Evaluation...")
    
    # 1. Load Data
    train_df = pd.read_parquet(FEATURES_PATH / "train_scaled.parquet")
    test_df = pd.read_parquet(FEATURES_PATH / "test_scaled.parquet")
    
    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    X_train_full = train_df[features].values
    y_train_full = train_df[target].values
    X_test_full = test_df[features].values
    y_test_full = test_df[target].values
    
    # 2. Load Base Model
    base_model = joblib.load(CLASSICAL_MODEL_DIR / "lgbm_calibrated.joblib")
    
    # Base predictions
    prob_base_train = base_model.predict_proba(X_train_full)[:, 1]
    prob_base_test = base_model.predict_proba(X_test_full)[:, 1]
    
    # Classical-only metrics on full test stream
    classical_only_metrics = compute_binary_metrics(y_test_full, prob_base_test)
    logging.info(f"Classical-Only Test AUPRC: {classical_only_metrics['auprc']:.4f}, ROC-AUC: {classical_only_metrics['roc_auc']:.4f}")
    
    # 3. Identify Training Escalated Traffic for Expert Fitting (Leakage-free!)
    train_uncertainties = compute_uncertainty(prob_base_train)
    # Select top n_train_expert most uncertain training transactions
    top_train_idx = np.argsort(train_uncertainties)[:n_train_expert]
    
    X_train_exp = X_train_full[top_train_idx]
    y_train_exp = y_train_full[top_train_idx]
    
    logging.info(f"Fitting experts on N={len(X_train_exp)} uncertain training samples (Fraud={np.sum(y_train_exp)})...")
    
    # Fit Experts
    # 1. Quantum Expert (Fidelity Kernel)
    q_expert_fidelity = QuantumExpert(method='fast_fidelity', C=1.0, random_state=seed)
    q_expert_fidelity.fit(X_train_exp, y_train_exp)
    
    # 2. Quantum Expert (Projected Kernel)
    q_expert_projected = QuantumExpert(method='projected', C=1.0, gamma=1.0, random_state=seed)
    q_expert_projected.fit(X_train_exp, y_train_exp)
    
    # 3. Classical RBF Expert (with CV tuning on X_train_exp)
    rbf_expert = ClassicalRBFExpert(tune_cv=True, random_state=seed)
    rbf_expert.fit(X_train_exp, y_train_exp)
    
    # 4. Classical GBM Expert
    gbm_expert = ClassicalGBMExpert(n_estimators=50, max_depth=3, random_state=seed)
    gbm_expert.fit(X_train_exp, y_train_exp)
    
    results = {
        "metadata": {
            "dataset_type": "SYNTHETIC",
            "n_train_full": len(train_df),
            "n_test_full": len(test_df),
            "n_train_expert": n_train_expert,
            "train_expert_fraud_count": int(np.sum(y_train_exp)),
            "budgets_pct": list(budgets),
            "features": features,
            "n_bootstrap": n_bootstrap,
            "seed": seed
        },
        "classical_only_baseline": classical_only_metrics,
        "sweeps": []
    }
    
    flat_rows = []
    
    test_uncertainties = compute_uncertainty(prob_base_test)
    
    for b in budgets:
        logging.info(f"\n--- Evaluating Escalation Budget B = {b}% ---")
        
        # A. Route Test Traffic via Uncertainty
        esc_idx, clr_idx = select_escalated_indices(prob_base_test, budget_pct=b, strategy='uncertainty', random_state=seed)
        # B. Route Test Traffic via Random (Control)
        rnd_esc_idx, rnd_clr_idx = select_escalated_indices(prob_base_test, budget_pct=b, strategy='random', random_state=seed)
        
        n_esc = len(esc_idx)
        fraud_in_esc = int(np.sum(y_test_full[esc_idx]))
        fraud_in_clr = int(np.sum(y_test_full[clr_idx]))
        fraud_in_rnd = int(np.sum(y_test_full[rnd_esc_idx]))
        
        X_esc = X_test_full[esc_idx]
        y_esc = y_test_full[esc_idx]
        
        X_rnd = X_test_full[rnd_esc_idx]
        y_rnd = y_test_full[rnd_esc_idx]
        
        # Expert predictions on escalated subset
        q_fid_prob_esc = q_expert_fidelity.predict_proba(X_esc)[:, 1]
        q_proj_prob_esc = q_expert_projected.predict_proba(X_esc)[:, 1]
        rbf_prob_esc = rbf_expert.predict_proba(X_esc)[:, 1]
        gbm_prob_esc = gbm_expert.predict_proba(X_esc)[:, 1]
        
        # Random router expert prediction (using RBF expert on random traffic)
        rnd_rbf_prob_esc = rbf_expert.predict_proba(X_rnd)[:, 1]
        
        # Assemble Full-System Decisions:
        # P_system = P_base for cleared, P_expert for escalated
        sys_prob_q_fid = prob_base_test.copy()
        sys_prob_q_fid[esc_idx] = q_fid_prob_esc
        
        sys_prob_q_proj = prob_base_test.copy()
        sys_prob_q_proj[esc_idx] = q_proj_prob_esc
        
        sys_prob_rbf = prob_base_test.copy()
        sys_prob_rbf[esc_idx] = rbf_prob_esc
        
        sys_prob_gbm = prob_base_test.copy()
        sys_prob_gbm[esc_idx] = gbm_prob_esc
        
        sys_prob_rnd = prob_base_test.copy()
        sys_prob_rnd[rnd_esc_idx] = rnd_rbf_prob_esc
        
        # Calculate Full System Metrics
        m_q_fid = compute_binary_metrics(y_test_full, sys_prob_q_fid)
        m_q_proj = compute_binary_metrics(y_test_full, sys_prob_q_proj)
        m_rbf = compute_binary_metrics(y_test_full, sys_prob_rbf)
        m_gbm = compute_binary_metrics(y_test_full, sys_prob_gbm)
        m_rnd = compute_binary_metrics(y_test_full, sys_prob_rnd)
        
        # Expert-subset metrics
        m_q_fid_subset = compute_binary_metrics(y_esc, q_fid_prob_esc)
        m_rbf_subset = compute_binary_metrics(y_esc, rbf_prob_esc)
        
        # Paired Bootstrap Comparison: Quantum (Fidelity) vs RBF Control
        bootstrap_q_vs_rbf = run_paired_bootstrap(y_test_full, sys_prob_q_fid, sys_prob_rbf, n_bootstrap=n_bootstrap, seed=seed)
        # Paired Bootstrap Comparison: Quantum (Fidelity) vs Strong GBM Control
        bootstrap_q_vs_gbm = run_paired_bootstrap(y_test_full, sys_prob_q_fid, sys_prob_gbm, n_bootstrap=n_bootstrap, seed=seed)
        # Paired Bootstrap Comparison: Quantum (Projected) vs RBF Control
        bootstrap_qproj_vs_rbf = run_paired_bootstrap(y_test_full, sys_prob_q_proj, sys_prob_rbf, n_bootstrap=n_bootstrap, seed=seed)
        
        sweep_entry = {
            "budget_pct": b,
            "n_escalated": n_esc,
            "escalated_coverage_pct": float(n_esc / len(test_df) * 100),
            "fraud_prevalence": {
                "in_escalated": float(fraud_in_esc / n_esc) if n_esc > 0 else 0.0,
                "in_cleared": float(fraud_in_clr / len(clr_idx)),
                "in_random_escalated": float(fraud_in_rnd / len(rnd_esc_idx)),
                "total_test": float(np.sum(y_test_full) / len(test_df))
            },
            "system_metrics": {
                "classical_only": classical_only_metrics,
                "classical_plus_rbf": m_rbf,
                "classical_plus_quantum_fidelity": m_q_fid,
                "classical_plus_quantum_projected": m_q_proj,
                "classical_plus_gbm": m_gbm,
                "classical_plus_random_router": m_rnd
            },
            "expert_subset_metrics": {
                "quantum_fidelity": m_q_fid_subset,
                "classical_rbf": m_rbf_subset
            },
            "paired_bootstrap": {
                "quantum_fidelity_vs_rbf": bootstrap_q_vs_rbf,
                "quantum_fidelity_vs_gbm": bootstrap_q_vs_gbm,
                "quantum_projected_vs_rbf": bootstrap_qproj_vs_rbf
            }
        }
        results["sweeps"].append(sweep_entry)
        
        logging.info(f"Budget {b}% - Full System AUPRC:")
        logging.info(f"  Classical-only:           {classical_only_metrics['auprc']:.4f}")
        logging.info(f"  Classical + RBF:          {m_rbf['auprc']:.4f}")
        logging.info(f"  Classical + Quantum (Fid):{m_q_fid['auprc']:.4f}")
        logging.info(f"  Classical + Quantum (Prj):{m_q_proj['auprc']:.4f}")
        logging.info(f"  Classical + Strong GBM:   {m_gbm['auprc']:.4f}")
        logging.info(f"  Classical + Random-Route: {m_rnd['auprc']:.4f}")
        logging.info(
            f"  Δ(Quantum_Fid - RBF) AUPRC: {bootstrap_q_vs_rbf['delta_auprc']['mean']:+.4f} "
            f"[95% CI: {bootstrap_q_vs_rbf['delta_auprc']['ci_95'][0]:+.4f}, {bootstrap_q_vs_rbf['delta_auprc']['ci_95'][1]:+.4f}], "
            f"p={bootstrap_q_vs_rbf['delta_auprc']['p_value']:.4f}"
        )
        
        # Flatten for CSV
        flat_rows.append({
            "budget_pct": b,
            "n_escalated": n_esc,
            "classical_only_auprc": classical_only_metrics['auprc'],
            "classical_only_auc": classical_only_metrics['roc_auc'],
            "rbf_auprc": m_rbf['auprc'],
            "rbf_auc": m_rbf['roc_auc'],
            "q_fid_auprc": m_q_fid['auprc'],
            "q_fid_auc": m_q_fid['roc_auc'],
            "q_proj_auprc": m_q_proj['auprc'],
            "q_proj_auc": m_q_proj['roc_auc'],
            "gbm_auprc": m_gbm['auprc'],
            "gbm_auc": m_gbm['roc_auc'],
            "rnd_auprc": m_rnd['auprc'],
            "rnd_auc": m_rnd['roc_auc'],
            "delta_auprc_q_vs_rbf": bootstrap_q_vs_rbf['delta_auprc']['mean'],
            "delta_auprc_ci_low": bootstrap_q_vs_rbf['delta_auprc']['ci_95'][0],
            "delta_auprc_ci_high": bootstrap_q_vs_rbf['delta_auprc']['ci_95'][1],
            "p_val_auprc": bootstrap_q_vs_rbf['delta_auprc']['p_value'],
            "zero_in_ci": bootstrap_q_vs_rbf['delta_auprc']['zero_in_ci']
        })
        
    # Apply Multiple-Testing Corrections across budgets (Phase 25)
    p_vals = [r["p_val_auprc"] for r in flat_rows]
    m_tests = len(p_vals)
    # Bonferroni
    bonf_p = [min(1.0, p * m_tests) for p in p_vals]
    
    # Benjamini-Hochberg FDR
    sorted_order = np.argsort(p_vals)
    ranks = np.empty_like(sorted_order)
    ranks[sorted_order] = np.arange(1, m_tests + 1)
    fdr_q = [min(1.0, (p * m_tests) / r) for p, r in zip(p_vals, ranks)]
    
    for i, r in enumerate(flat_rows):
        r["bonferroni_p"] = bonf_p[i]
        r["bh_fdr_q"] = fdr_q[i]
        results["sweeps"][i]["multiple_testing_correction"] = {
            "bonferroni_p": bonf_p[i],
            "bh_fdr_q": fdr_q[i]
        }
        
    # Save JSON and CSV results
    json_path = RESULTS_PATH / "full_system_evaluation.json"
    csv_path = RESULTS_PATH / "budget_sweep_results.csv"
    
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
        
    df_flat = pd.DataFrame(flat_rows)
    df_flat.to_csv(csv_path, index=False)
    
    logging.info(f"[VERIFIED] Saved full system evaluation JSON to {json_path}")
    logging.info(f"[VERIFIED] Saved budget sweep CSV to {csv_path}")
    
    return results, df_flat

if __name__ == "__main__":
    run_full_routed_evaluation()
