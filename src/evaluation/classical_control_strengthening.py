import json
import logging
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score
from src.utils.paths import FEATURES_PATH, CLASSICAL_MODEL_DIR, EVIDENCE_DIR
from src.models.router.escalation_router import select_escalated_indices
from src.models.experts.quantum_expert import QuantumExpert
from src.models.experts.classical_rbf_expert import ClassicalRBFExpert
from src.models.experts.classical_gbm_expert import ClassicalGBMExpert
from src.models.experts.classical_mlp_expert import ClassicalMLPExpert
from src.models.experts.classical_poly_expert import ClassicalPolyExpert

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_classical_strengthening(
    budgets=(0.5, 1.0, 2.0, 5.0, 10.0),
    seed=42
):
    """
    [IMPLEMENTED] Phase 32: Classical Control Strengthening Benchmark.
    Tests a diverse suite of competitive classical architectures against the Quantum Expert.
    """
    logging.info("Starting Phase 32 Classical Control Strengthening Benchmark...")
    
    train_df = pd.read_parquet(FEATURES_PATH / "train_scaled.parquet")
    test_df = pd.read_parquet(FEATURES_PATH / "test_scaled.parquet")
    
    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    X_train = train_df[features].values
    y_train = train_df[target].values
    X_test = test_df[features].values
    y_test = test_df[target].values
    
    base_model = joblib.load(CLASSICAL_MODEL_DIR / "lgbm_calibrated.joblib")
    probs_train = base_model.predict_proba(X_train)[:, 1]
    probs_test = base_model.predict_proba(X_test)[:, 1]
    
    # Train set escalated traffic (top 200 uncertain)
    unc_train = np.abs(probs_train - 0.5)
    top_train = np.argsort(unc_train)[:200]
    X_train_exp = X_train[top_train]
    y_train_exp = y_train[top_train]
    
    # Initialize all competitive classical controls & quantum experts
    experts = {
        "Classical_RBF_Tuned": ClassicalRBFExpert(tune_cv=True, random_state=seed),
        "Classical_GBM": ClassicalGBMExpert(n_estimators=50, max_depth=3, random_state=seed),
        "Classical_MLP_NeuralNet": ClassicalMLPExpert(hidden_layer_sizes=(32, 16), max_iter=200, random_state=seed),
        "Classical_Poly_Kernel": ClassicalPolyExpert(degree=3, C=1.0, random_state=seed),
        "Quantum_Fidelity_Kernel": QuantumExpert(method='fast_fidelity', C=1.0, random_state=seed),
        "Quantum_Projected_Kernel": QuantumExpert(method='projected', C=1.0, gamma=1.0, random_state=seed)
    }
    
    # Fit all models on exact identical training escalated traffic
    logging.info(f"Fitting all {len(experts)} candidate expert models on N={len(X_train_exp)} uncertain transactions...")
    for name, exp in experts.items():
        logging.info(f"Fitting {name}...")
        exp.fit(X_train_exp, y_train_exp)
        
    records = []
    
    for b in budgets:
        esc_idx, _ = select_escalated_indices(probs_test, budget_pct=b, strategy='uncertainty', random_state=seed)
        X_esc = X_test[esc_idx]
        y_esc = y_test[esc_idx]
        
        for name, exp in experts.items():
            prob_esc = exp.predict_proba(X_esc)[:, 1]
            
            # Full system decision stream
            sys_probs = probs_test.copy()
            sys_probs[esc_idx] = prob_esc
            
            sys_auprc = float(average_precision_score(y_test, sys_probs))
            sys_auc = float(roc_auc_score(y_test, sys_probs))
            
            # Expert subset metrics
            sub_auprc = float(average_precision_score(y_esc, prob_esc)) if len(np.unique(y_esc)) > 1 else 0.0
            sub_auc = float(roc_auc_score(y_esc, prob_esc)) if len(np.unique(y_esc)) > 1 else 0.5
            
            records.append({
                "budget_pct": b,
                "model_name": name,
                "n_escalated": len(esc_idx),
                "full_system_auprc": sys_auprc,
                "full_system_roc_auc": sys_auc,
                "expert_subset_auprc": sub_auprc,
                "expert_subset_roc_auc": sub_auc
            })
            
    df_results = pd.DataFrame(records)
    
    # Save artifacts
    json_path = EVIDENCE_DIR / "classical_strengthening_benchmark.json"
    csv_path = EVIDENCE_DIR / "classical_strengthening_benchmark.csv"
    
    df_results.to_csv(csv_path, index=False)
    
    summary = {
        "metadata": {
            "dataset_type": "SYNTHETIC",
            "seed": seed,
            "budgets": list(budgets),
            "models_tested": list(experts.keys())
        },
        "mean_full_system_auprc_across_budgets": df_results.groupby('model_name')['full_system_auprc'].mean().to_dict(),
        "detailed_table": records
    }
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
        
    logging.info(f"[VERIFIED] Classical strengthening benchmark complete. Saved to {json_path}")
    return summary, df_results

if __name__ == "__main__":
    run_classical_strengthening()
