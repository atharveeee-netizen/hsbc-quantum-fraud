import time
import json
import logging
import numpy as np
import pandas as pd
from src.utils.paths import FEATURES_PATH, EVIDENCE_DIR
from src.models.quantum.projected_kernel import compute_kernel_matrix, compute_projected_kernel_matrix

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_sample_size_robustness(sample_sizes=(50, 100, 200, 400)):
    """
    [IMPLEMENTED] Phase 37: Sample-Size and Resource Scaling Robustness.
    Empirically profiles kernel evaluation runtime, condition number, memory, and scaling.
    """
    logging.info("Starting Phase 37 Sample-Size Robustness & Scaling Analysis...")
    train_df = pd.read_parquet(FEATURES_PATH / "train_scaled.parquet")
    features = ['TransactionAmt', 'card1']
    
    scaling_records = []
    
    for n in sample_sizes:
        if n > len(train_df):
            continue
            
        X_sub = train_df[features].head(n).values
        
        # 1. Fast Fidelity Kernel (Simulated Statevectors)
        t0 = time.time()
        K_fid = compute_kernel_matrix(X_sub, method='fast_fidelity')
        t_fid = time.time() - t0
        
        # 2. Projected Quantum Kernel
        t0 = time.time()
        K_pqk = compute_projected_kernel_matrix(X_sub, gamma=1.0)
        t_pqk = time.time() - t0
        
        # Metrics
        mem_bytes = K_fid.nbytes
        eigs_fid = np.linalg.eigvalsh(K_fid)
        cond_fid = float(np.max(eigs_fid) / (max(np.min(eigs_fid), 1e-12)))
        
        # Theoretical QPU shot/circuit evaluations for pairwise swap test
        # Pairwise inversion tests require N*(N-1)/2 quantum executions
        qpu_pairwise_circuits = int(n * (n - 1) / 2)
        
        scaling_records.append({
            "sample_size_N": n,
            "kernel_matrix_shape": [n, n],
            "memory_kb": float(mem_bytes / 1024.0),
            "runtime_fidelity_sec": float(t_fid),
            "runtime_projected_sec": float(t_pqk),
            "condition_number_fidelity": cond_fid,
            "qpu_pairwise_inversion_circuits": qpu_pairwise_circuits,
            "simulator_statevector_calls": n
        })
        
        logging.info(
            f"N={n}: Fidelity={t_fid:.3f}s, Projected={t_pqk:.3f}s, "
            f"Memory={mem_bytes/1024:.1f}KB, QPU Pairwise Circuits={qpu_pairwise_circuits}"
        )
        
    df_scaling = pd.DataFrame(scaling_records)
    
    report = {
        "metadata": {
            "dataset_type": "SYNTHETIC",
            "device": "PennyLane default.qubit (Simulated)",
            "n_qubits": 2
        },
        "scaling_summary": scaling_records,
        "complexity_analysis": {
            "simulator_statevector_complexity": "O(N) quantum executions + O(N^2) classical BLAS multiplication",
            "physical_qpu_pairwise_complexity": "O(N^2) quantum swap-test circuit executions",
            "hardware_scalability_verdict": (
                "Full-population quantum kernel matrices scale quadratically O(N^2) in circuit evaluations on physical QPUs. "
                "For N=10,000 transactions, physical execution requires ~50,000,000 quantum circuits. "
                "The escalation router is computationally essential to limit quantum execution strictly to small budget subsets (B <= 2%)."
            )
        }
    }
    
    out_file = EVIDENCE_DIR / "sample_size_robustness.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    df_scaling.to_csv(EVIDENCE_DIR / "sample_size_robustness.csv", index=False)
    
    logging.info(f"[VERIFIED] Sample size scaling analysis saved to {out_file}")
    return report, df_scaling

if __name__ == "__main__":
    run_sample_size_robustness()
