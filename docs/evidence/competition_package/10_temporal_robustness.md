# 10 Temporal Robustness & Non-Stationarity

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-TEMPORAL-ROBUST-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c58c174` |
| **Metric Definition** | AUPRC across 3 non-overlapping sequential chronological test windows. |

---

## Sequential Temporal Evaluation
- **Window 1:** Baseline = $0.2913$, Quantum = $0.2907$, RBF = $0.2968$ ($\Delta = -0.0061$).
- **Window 2:** Baseline = $0.3127$, Quantum = $0.3086$, RBF = $0.3106$ ($\Delta = -0.0020$).
- **Window 3:** Baseline = $0.3093$, Quantum = $0.3087$, RBF = $0.3103$ ($\Delta = -0.0016$).

**Finding:** Temporal non-stationarity causes natural baseline shifts, but in no temporal window does quantum demonstrate an advantage over classical controls.
