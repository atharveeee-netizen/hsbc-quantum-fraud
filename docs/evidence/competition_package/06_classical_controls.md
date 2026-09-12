# 06 Classical Control Strengthening

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-CTRL-STRENGTH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e9bd296` |
| **Metric Definition** | AUPRC of specialized experts on identical escalated subset (N=200). |

---

## Expert Tournament on Identical Escalated Traffic
All models evaluated on the identical top 10% escalated partition:
1. **Classical Gradient Boosting (`ClassicalGBM`):** Mean system AUPRC = **$0.3069$** (Tournament Winner).
2. **Quantum Projected Kernel:** Mean system AUPRC = **$0.3044$**.
3. **Classical RBF Tuned (C=10.0, gamma='scale'):** Mean system AUPRC = **$0.3030$**.
4. **Quantum Fidelity Kernel:** Mean system AUPRC = **$0.3017$**.
5. **Classical Polynomial Kernel (d=3):** Mean system AUPRC = **$0.3016$**.
6. **Classical MLP Neural Network:** Mean system AUPRC = **$0.3014$**.

**Scientific Finding:** Strong classical gradient boosting outperforms both classical RBF and all tested quantum kernels on escalated fraud traffic.
