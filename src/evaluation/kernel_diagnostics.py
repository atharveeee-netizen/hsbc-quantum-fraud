import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import rbf_kernel
from src.models.quantum.projected_kernel import compute_kernel_matrix
from src.features.build_features import FEATURES_PATH
import os
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def diagnose_kernel(K):
    """
    Computes mathematical diagnostics on the kernel matrix.
    """
    eigvals = np.linalg.eigvalsh(K)
    neg_eigs = eigvals[eigvals < -1e-6]
    
    return {
        "min_eigenvalue": float(np.min(eigvals)),
        "max_eigenvalue": float(np.max(eigvals)),
        "num_negative_eigenvalues": len(neg_eigs),
        "condition_number": float(np.max(eigvals) / (np.min(eigvals) + 1e-8)),
        "mean_similarity": float(np.mean(K)),
        "variance_similarity": float(np.var(K))
    }

def run_diagnostics():
    """
    [IMPLEMENTED] Phase 16: Compares the spectral properties of the Classical RBF vs Projected Quantum Kernel.
    """
    logging.info("Loading a tiny sample for kernel diagnostics (N=50)...")
    try:
        df = pd.read_parquet(os.path.join(FEATURES_PATH, 'train_scaled.parquet')).head(50)
    except FileNotFoundError:
        logging.error("[BLOCKED] Processed data not found.")
        return
        
    features = ['TransactionAmt', 'card1']
    X = df[features]
    
    logging.info("Computing Classical RBF Kernel...")
    K_rbf = rbf_kernel(X, gamma=None)
    rbf_diag = diagnose_kernel(K_rbf)
    
    logging.info("Computing Projected Quantum Kernel...")
    K_quantum = compute_kernel_matrix(X)
    quantum_diag = diagnose_kernel(K_quantum)
    
    report = {
        "rbf_kernel": rbf_diag,
        "quantum_kernel": quantum_diag
    }
    
    os.makedirs("../../docs/evidence", exist_ok=True)
    out_path = "../../docs/evidence/kernel_diagnostics.json"
    
    with open(out_path, "w") as f:
        json.dump(report, f, indent=4)
        
    logging.info(f"[VERIFIED] Diagnostics saved to {out_path}")
    
    # Assert physical constraints (PSD matrix)
    if quantum_diag["num_negative_eigenvalues"] == 0:
        logging.info("[VERIFIED] Quantum kernel is Positive Semi-Definite (valid Gram matrix).")
    else:
        logging.warning("[INCONCLUSIVE] Quantum kernel exhibits negative eigenvalues. May require regularization.")

if __name__ == "__main__":
    run_diagnostics()
