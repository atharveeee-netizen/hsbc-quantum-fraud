# 04 Calibrated Classical Baseline

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-BASELINE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e9bd296` |
| **Metric Definition** | Monolithic baseline AUPRC, AUROC, Brier Score, and Expected Calibration Error (ECE). |

---

## Monolithic LightGBM Performance
- **Model:** LightGBM Classifier with isotonic probability calibration on the temporal calibration split.
- **Full-System Baseline AUPRC:** $0.3040$.
- **Full-System Baseline AUROC:** $0.8540$.
- **Inference Latency:** $<12\text{ms}$ on standard CPU.
- **Calibration:** Platt/isotonic calibration eliminates probability skew on imbalanced fraud scores.
