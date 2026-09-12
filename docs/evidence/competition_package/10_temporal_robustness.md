# 10 Temporal Stability & Window-by-Window Drift

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-TEMP-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Chronological stability across contiguous out-of-sample temporal windows. |

---

## Sequential Chronological Evaluation
- **Window 1 (Days 141.1 – 155.0):** Classical RBF PR = **0.5841**, PQK PR = **0.4148**, $\Delta = \mathbf{-0.1693}$ (Classical RBF wins).
- **Window 2 (Days 155.0 – 168.6):** Classical RBF PR = 0.4412, PQK PR = 0.5187, $\Delta = +0.0774$.
- **Window 3 (Days 168.6 – 183.0):** Classical RBF PR = 0.4163, PQK PR = 0.5765, $\Delta = +0.1602$.
Quantum enhancement fails to maintain consistency, suffering severe underperformance in Window 1 and failing the Temporal Robustness Gate.
