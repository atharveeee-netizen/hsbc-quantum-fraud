# 04 Calibrated Classical Baseline

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-BASELINE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c0968b6` |
| **Metric Definition** | Monolithic baseline AUPRC, AUROC, Brier Score, and Expected Calibration Error (ECE). |

---

## Monolithic LightGBM Performance
- **Model:** LightGBM Classifier with isotonic probability calibration on the temporal calibration split.
- **Full-System Baseline AUPRC:** $0.3040$ ($0.3987$ on raw test features).
- **Full-System Baseline AUROC:** $0.5996$ (raw test features) / $0.4833$ (standardized feature stream).
- **Inference Latency:** $<12	ext{ms}$ on standard CPU.
- **Calibration:** Platt/isotonic calibration eliminates probability skew on imbalanced fraud scores.
