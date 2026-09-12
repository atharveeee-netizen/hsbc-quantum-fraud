import os
import json
import logging
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import rbf_kernel
from src.models.quantum.projected_kernel import compute_kernel_matrix, compute_projected_kernel_matrix
from src.utils.paths import FEATURES_PATH, RESULTS_PATH, EVIDENCE_DIR

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_effective_rank(eigvals):
    """
    Computes Roy & Vetterli (2007) effective rank:
    R_eff = exp( - sum p_i * ln(p_i) ) where p_i = lambda_i / sum(lambda)
    """
    pos_eigs = eigvals[eigvals > 1e-10]
    if len(pos_eigs) == 0:
        return 0.0
    p = pos_eigs / np.sum(pos_eigs)
    entropy = -np.sum(p * np.log(p + 1e-12))
    return float(np.exp(entropy))

def compute_kernel_target_alignment(K, y):
    """
    [IMPLEMENTED] Kernel-Target Alignment (Cristianini et al., 2002):
    A(K, Y) = <K, Y>_F / ( ||K||_F * ||Y||_F )
    where Y = y * y^T, with y in {-1, +1}^N.
    """
    y_signed = np.where(np.asarray(y) == 0, -1.0, 1.0)
    Y = np.outer(y_signed, y_signed)
    
    fro_K = np.linalg.norm(K, 'fro')
    fro_Y = np.linalg.norm(Y, 'fro')
    
    if fro_K == 0 or fro_Y == 0:
        return 0.0
        
    alignment = np.sum(K * Y) / (fro_K * fro_Y)
    return float(alignment)

def compute_class_separability(K, y):
    """
    Computes ratio of mean within-class kernel similarity to mean between-class kernel similarity.
    Higher ratio (> 1.0) indicates better geometric class clustering.
    """
    y_arr = np.asarray(y)
    mask_same = (y_arr[:, None] == y_arr[None, :])
    mask_diff = ~mask_same
    
    # Exclude diagonal
    np.fill_diagonal(mask_same, False)
    
    within_sim = np.mean(K[mask_same]) if np.any(mask_same) else 0.0
    between_sim = np.mean(K[mask_diff]) if np.any(mask_diff) else 0.0
    
    ratio = float(within_sim / (between_sim + 1e-8))
    return {
        "within_class_similarity": float(within_sim),
        "between_class_similarity": float(between_sim),
        "separability_ratio": ratio
    }

def diagnose_kernel(K, y=None):
    """
    Comprehensive spectral, geometric, and target alignment diagnostics.
    """
    eigvals = np.linalg.eigvalsh(K)
    neg_eigs = eigvals[eigvals < -1e-6]
    
    diag = {
        "matrix_shape": list(K.shape),
        "min_eigenvalue": float(np.min(eigvals)),
        "max_eigenvalue": float(np.max(eigvals)),
        "num_negative_eigenvalues": int(len(neg_eigs)),
        "condition_number": float(np.max(eigvals) / (max(np.min(eigvals), 1e-10))),
        "effective_rank": compute_effective_rank(eigvals),
        "mean_off_diagonal_similarity": float(np.mean(K[~np.eye(K.shape[0], dtype=bool)])),
        "variance_similarity": float(np.var(K))
    }
    
    if y is not None:
        diag["kernel_target_alignment"] = compute_kernel_target_alignment(K, y)
        diag["class_separability"] = compute_class_separability(K, y)
        
    return diag

def run_full_kernel_diagnostics(n_samples=100, seed=42):
    """
    [IMPLEMENTED] Phase 28: Full diagnostic comparison of:
      1. Classical RBF Kernel
      2. Quantum Fidelity Kernel
      3. Projected Quantum Kernel (PQK)
    """
    logging.info(f"Running Phase 28 Kernel Quality Diagnostics on N={n_samples} samples...")
    train_file = FEATURES_PATH / "train_scaled.parquet"
    if not train_file.exists():
        logging.error("[BLOCKED] Scaled features not found.")
        return
        
    df = pd.read_parquet(train_file).head(n_samples)
    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    X = df[features].values
    y = df[target].values
    
    # 1. Classical RBF Kernel
    logging.info("Evaluating Classical RBF Kernel...")
    K_rbf = rbf_kernel(X, gamma=1.0)
    diag_rbf = diagnose_kernel(K_rbf, y)
    
    # 2. Quantum Fidelity Kernel
    logging.info("Evaluating Quantum Fidelity Kernel...")
    K_q_fid = compute_kernel_matrix(X, method='fast_fidelity')
    diag_q_fid = diagnose_kernel(K_q_fid, y)
    
    # 3. Projected Quantum Kernel (PQK)
    logging.info("Evaluating Projected Quantum Kernel...")
    K_q_proj = compute_projected_kernel_matrix(X, gamma=1.0)
    diag_q_proj = diagnose_kernel(K_q_proj, y)
    
    report = {
        "metadata": {
            "dataset_type": "SYNTHETIC",
            "n_samples": n_samples,
            "features": features,
            "target": target,
            "fraud_prevalence": float(np.mean(y))
        },
        "classical_rbf_kernel": diag_rbf,
        "quantum_fidelity_kernel": diag_q_fid,
        "quantum_projected_kernel": diag_q_proj,
        "scientific_summary": {
            "all_kernels_psd": bool(
                diag_rbf["num_negative_eigenvalues"] == 0 and
                diag_q_fid["num_negative_eigenvalues"] == 0 and
                diag_q_proj["num_negative_eigenvalues"] == 0
            ),
            "highest_kernel_target_alignment": max(
                [("RBF", diag_rbf["kernel_target_alignment"]),
                 ("Quantum_Fidelity", diag_q_fid["kernel_target_alignment"]),
                 ("Quantum_Projected", diag_q_proj["kernel_target_alignment"])],
                key=lambda x: x[1]
            )[0]
        }
    }
    
    out_file = RESULTS_PATH / "kernel_diagnostics.json"
    evidence_file = EVIDENCE_DIR / "kernel_diagnostics.json"
    
    with open(out_file, "w") as f:
        json.dump(report, f, indent=2)
    with open(evidence_file, "w") as f:
        json.dump(report, f, indent=2)
        
    logging.info(f"[VERIFIED] Kernel diagnostics saved to {out_file} and {evidence_file}")
    return report

if __name__ == "__main__":
    run_full_kernel_diagnostics()
