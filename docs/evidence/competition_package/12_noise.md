# 12 Simulated Physical Noise Sensitivity

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SIMULATED NOISE] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-NOISE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Frobenius kernel distortion and PR-AUC decay under depolarizing and readout noise. |

---

## Controlled Noise Perturbation Matrix
- $p = 0.001$ ($0.1\%$ error): 0.17% distortion, PR-AUC = 0.3784.
- $p = 0.010$ ($1.0\%$ error): 1.66% distortion, PR-AUC = 0.3739 (-1.32%).
- $p = 0.020$ ($2.0\%$ error): 3.29% distortion, PR-AUC = 0.3689 (-2.64%).
- $p = 0.050$ ($5.0\%$ error): 8.12% distortion, PR-AUC = 0.3543 (-6.49%).
Physical quantum noise degrades kernel fidelity monotonically without providing any regularization benefit.
