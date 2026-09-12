# Master Scientific Evidence Ledger

> **Last Updated:** 2026-09-12T09:12:33.913933+00:00  
> **Claim Firewall Status:** `ENFORCED`  
> **Quantum Advantage Verdict:** `INCONCLUSIVE` (Null hypothesis stands)  
> **Real IEEE-CIS Benchmark:** `BLOCKED` (Synthetic benchmark active)  

---

## 1. Evidence Matrix: Claim -> Experiment -> Artifact -> Result -> Status

| Claim ID | Category | Status | Primary Metric | Result Summary | 95% CI / p-value | Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-BASE-01` | Classical ML | `MEASURED` | AUPRC / KTA | Established baseline on temporal synthetic split: AUPRC=0.3040, ROC-AUC=0.4833.... | N/A | Measured exclusively on synthetic smoke fixture du... |
| `CLM-ROUTED-B0.5` | Full System Evaluation | `MEASURED` | AUPRC / KTA | At 0.5% budget, Quantum Expert AUPRC=0.3041 vs Classical RBF=0.3036 (Δ=+0.0005, ... | [-0.0005, +0.0023], p=0.6880 | Tested on 2-qubit simulation on synthetic benchmar... |
| `CLM-ROUTED-B1.0` | Full System Evaluation | `MEASURED` | AUPRC / KTA | At 1.0% budget, Quantum Expert AUPRC=0.3033 vs Classical RBF=0.3030 (Δ=+0.0004, ... | [-0.0007, +0.0024], p=0.6100 | Tested on 2-qubit simulation on synthetic benchmar... |
| `CLM-ROUTED-B2.0` | Full System Evaluation | `MEASURED` | AUPRC / KTA | At 2.0% budget, Quantum Expert AUPRC=0.3041 vs Classical RBF=0.3050 (Δ=-0.0009, ... | [-0.0056, +0.0036], p=0.7140 | Tested on 2-qubit simulation on synthetic benchmar... |
| `CLM-ROUTED-B5.0` | Full System Evaluation | `MEASURED` | AUPRC / KTA | At 5.0% budget, Quantum Expert AUPRC=0.2997 vs Classical RBF=0.3013 (Δ=-0.0015, ... | [-0.0066, +0.0035], p=0.5260 | Tested on 2-qubit simulation on synthetic benchmar... |
| `CLM-ROUTED-B10.0` | Full System Evaluation | `MEASURED` | AUPRC / KTA | At 10.0% budget, Quantum Expert AUPRC=0.2975 vs Classical RBF=0.3023 (Δ=-0.0050,... | [-0.0129, +0.0020], p=0.1440 | Tested on 2-qubit simulation on synthetic benchmar... |
| `CLM-ROUTER-AUDIT-01` | Router Audit | `VERIFIED` | AUPRC / KTA | Router temporal leakage: NONE (Verified). Uncertainty correlates with borderline... | N/A | Routing effectiveness is bounded by classical base... |
| `CLM-TEMPORAL-01` | Temporal Validation | `VERIFIED` | AUPRC / KTA | Random IID splitting artificially inflates test AUPRC by +0.0131 relative to str... | N/A | Evaluated on synthetic chronological fixture.... |
| `CLM-KERNEL-PSD-01` | Quantum Diagnostics | `VERIFIED` | AUPRC / KTA | Quantum Gram matrix is strictly Positive Semi-Definite (0 negative eigenvalues).... | N/A | Computed on N=100 samples with 2-qubit AngleEmbedd... |

---

## 2. Strict Scientific Principles Enforced

1. **No Cherry-Picking:** All 5 escalation budgets (0.5%, 1%, 2%, 5%, 10%) are reported irrespective of outcome.
2. **Paired Bootstrap:** Every quantum vs classical delta is computed on the exact same resampled test transactions.
3. **Multiple Testing Correction:** Bonferroni and Benjamini-Hochberg FDR adjustments applied across budget sweeps.
4. **Fair Tuning:** Classical RBF control tuned via cross-validation strictly on the training fold.
5. **No Leakage:** Preprocessing scalers fit exclusively on the chronological training window.
