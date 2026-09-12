import json
import logging
import pandas as pd
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.utils.paths import (
    PROCESSED_DATA_PATH, FEATURES_PATH, EVIDENCE_DIR, RESULTS_PATH
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def verify_all_evidence():
    """
    [IMPLEMENTED] Phase 29: Systematic mathematical and architectural re-audit of all existing evidence.
    """
    logging.info("Starting Phase 29 Systematic Evidence Re-Audit...")
    audit_failures = []
    
    # 1. Dataset & Temporal Integrity
    train_raw = pd.read_parquet(PROCESSED_DATA_PATH / "train.parquet")
    calib_raw = pd.read_parquet(PROCESSED_DATA_PATH / "calib.parquet")
    test_raw = pd.read_parquet(PROCESSED_DATA_PATH / "test.parquet")
    
    t_train_max = train_raw['TransactionDT'].max()
    t_calib_min = calib_raw['TransactionDT'].min()
    t_calib_max = calib_raw['TransactionDT'].max()
    t_test_min = test_raw['TransactionDT'].min()
    
    if t_train_max >= t_calib_min:
        audit_failures.append(f"Temporal Leakage: Train max DT ({t_train_max}) >= Calib min DT ({t_calib_min})")
    if t_calib_max >= t_test_min:
        audit_failures.append(f"Temporal Leakage: Calib max DT ({t_calib_max}) >= Test min DT ({t_test_min})")
        
    logging.info(f"Dataset counts: Train={len(train_raw)}, Calib={len(calib_raw)}, Test={len(test_raw)}")
    
    # 2. Scaling Boundary Audit
    # Verify that test_scaled was standardized with train parameters
    train_amt_mean = train_raw['TransactionAmt'].mean()
    train_amt_std = train_raw['TransactionAmt'].std(ddof=0)
    
    train_scaled = pd.read_parquet(FEATURES_PATH / "train_scaled.parquet")
    test_scaled = pd.read_parquet(FEATURES_PATH / "test_scaled.parquet")
    
    expected_test_amt_scaled = (test_raw['TransactionAmt'].values - train_amt_mean) / train_amt_std
    actual_test_amt_scaled = test_scaled['TransactionAmt'].values
    
    max_scale_diff = np.max(np.abs(expected_test_amt_scaled - actual_test_amt_scaled))
    if max_scale_diff > 1e-4:
        audit_failures.append(f"Scaling Contamination: Test features not scaled by train parameters (diff={max_scale_diff})")
    else:
        logging.info(f"Feature scaling strictly training-only: max numerical diff = {max_scale_diff:.2e}")
        
    # 3. CSV vs JSON Evidence Concordance
    csv_file = EVIDENCE_DIR / "budget_sweep_results.csv"
    json_file = EVIDENCE_DIR / "full_system_evaluation.json"
    
    if not csv_file.exists() or not json_file.exists():
        audit_failures.append("Evidence artifacts missing in docs/evidence/")
        return audit_failures
        
    df_csv = pd.read_csv(csv_file)
    with open(json_file) as f:
        data_json = json.load(f)
        
    # Verify budget counts and values
    expected_budgets = [0.5, 1.0, 2.0, 5.0, 10.0]
    for b in expected_budgets:
        csv_row = df_csv[df_csv['budget_pct'] == b]
        if len(csv_row) != 1:
            audit_failures.append(f"Budget {b}% missing or duplicated in CSV")
            continue
            
        json_sweep = [s for s in data_json['sweeps'] if s['budget_pct'] == b]
        if len(json_sweep) != 1:
            audit_failures.append(f"Budget {b}% missing or duplicated in JSON")
            continue
            
        json_entry = json_sweep[0]
        n_esc_expected = int(np.round((b / 100.0) * len(test_raw)))
        
        # Check escalated count
        if json_entry['n_escalated'] != n_esc_expected:
            audit_failures.append(f"Budget {b}%: expected {n_esc_expected} escalated, found {json_entry['n_escalated']}")
            
        # Check AUPRC match between CSV and JSON
        json_q_auprc = json_entry['system_metrics']['classical_plus_quantum_fidelity']['auprc']
        csv_q_auprc = csv_row['q_fid_auprc'].values[0]
        if not np.isclose(json_q_auprc, csv_q_auprc, atol=1e-6):
            audit_failures.append(f"Budget {b}%: CSV q_fid_auprc ({csv_q_auprc}) != JSON ({json_q_auprc})")
            
        # Verify 0 in 95% CI
        ci = json_entry['paired_bootstrap']['quantum_fidelity_vs_rbf']['delta_auprc']['ci_95']
        zero_in_ci = (ci[0] <= 0.0 <= ci[1])
        if not zero_in_ci:
            audit_failures.append(f"Budget {b}%: Zero not in CI [{ci[0]}, {ci[1]}] unexpectedly")
            
    # 4. Master Ledger Consistency
    ledger_file = EVIDENCE_DIR / "evidence_ledger.json"
    with open(ledger_file) as f:
        ledger = json.load(f)
        
    if ledger['metadata']['quantum_advantage_status'] != "NOT YET ESTABLISHED / INCONCLUSIVE":
        audit_failures.append("Evidence ledger metadata has unsupported quantum advantage claim")
        
    if len(audit_failures) == 0:
        logging.info("[VERIFIED] Phase 29 Re-Audit Passed: 0 discrepancies found across datasets, scaling, metrics, and ledgers.")
    else:
        logging.error(f"[FAILED] Phase 29 Re-Audit found {len(audit_failures)} discrepancies: {audit_failures}")
        
    return audit_failures

if __name__ == "__main__":
    fails = verify_all_evidence()
    if fails:
        exit(1)
    exit(0)
