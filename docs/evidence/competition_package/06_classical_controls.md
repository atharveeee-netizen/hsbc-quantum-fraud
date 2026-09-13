# 06 Classical Control Strengthening

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-CTRL-STRENGTH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Performance of specialized classical models on matched escalated traffic. |

---

## Classical Controls on Matched Escalated Support ($N=200$)
- **Classical RBF Control (Tuned):** PR-AUC = **0.6561**, ROC-AUC = **0.7546**, Latency = 0.78 ms.
- **Classical MLP Neural Network:** PR-AUC = **0.3516**, ROC-AUC = **0.4867**, Latency = 0.01 ms.
- **Classical Gradient Boosted (GBM):** PR-AUC = **0.3529**, ROC-AUC = **0.4369**, Latency = 0.02 ms.
All classical models evaluate within sub-millisecond budgets and require zero specialized quantum coprocessors.
