# 08 Multi-Budget Full System Evaluation

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-BUDGET-SWEEP-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Full-system decision stream metrics across operational escalation budgets. |

---

## Real Data Escalation Budget Synthesis
- At 0.5% budget: 591 reviews isolate 253 fraudulent transactions (12.44x lift).
- At 1.0% budget: 1,181 reviews isolate 440 fraudulent transactions (10.83x lift).
- At 5.0% budget: 5,905 reviews isolate 1,559 fraudulent transactions (38.36% of all test fraud).
The selective architecture allows an institution to tune secondary review strictly to available analyst staffing without degrading frontline throughput.
