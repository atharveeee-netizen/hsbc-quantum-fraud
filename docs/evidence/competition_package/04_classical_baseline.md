# 04 Calibrated Classical Baseline Freeze

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-BASELINE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Out-of-sample PR-AUC, ROC-AUC, Brier Score, and Inference Latency. |

---

## Real-Data LightGBM Baseline Performance
Evaluated out-of-sample across the 118,108 test transactions:
- **PR-AUC:** **0.4040** (**11.74x lift** over random guessing $\pi = 0.0344$).
- **ROC-AUC:** **0.8503** (Strong global discrimination across 182-day span).
- **Brier Score Loss:** **0.0250** (ECE = 0.0785).
- **Inference Latency:** **0.0007 ms** ($0.7	ext{ }\mu	ext{s/tx}$).
- **Logistic Regression Control:** PR-AUC = 0.1610 (Lift: 4.68x), ROC-AUC = 0.7200, Brier = 0.0315.
