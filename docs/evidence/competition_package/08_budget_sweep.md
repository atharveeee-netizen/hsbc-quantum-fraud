# 08 Selective Escalation Budget Sweep

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-BUDGET-SWEEP-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `9857a2a` |
| **Metric Definition** | Full-system AUPRC across escalation budgets B in {0.5%, 1%, 2%, 5%, 10%}. |

---

## Systematic Budget Sweep Results
| Budget $B$ | Baseline AUPRC | Classical RBF AUPRC | Quantum Expert AUPRC | Delta (Q - RBF) | 95% Bootstrap CI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0.5%** | 0.3040 | 0.3060 | 0.3060 | +0.0000 | [-0.0005, +0.0005] |
| **1.0%** | 0.3040 | 0.3090 | 0.3090 | +0.0000 | [-0.0010, +0.0010] |
| **2.0%** | 0.3040 | 0.3120 | 0.3115 | -0.0005 | [-0.0020, +0.0010] |
| **5.0%** | 0.3040 | 0.3160 | 0.3130 | -0.0030 | [-0.0060, +0.0000] |
| **10.0%** | 0.3040 | 0.3180 | 0.3100 | -0.0080 | [-0.0120, -0.0040] |

**Finding:** At low budgets (0.5%–1.0%), Quantum and Tuned RBF are statistically tied. At higher budgets, Classical RBF pulls ahead while Classical GBM dominates all methods.
