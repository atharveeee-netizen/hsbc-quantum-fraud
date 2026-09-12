# 12 Physical Noise Simulation

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-NOISE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `9857a2a` |
| **Metric Definition** | Depolarizing noise probability p in [0.0, 0.10], state purity, kernel fidelity, and AUPRC. |

---

## Noisy Simulation on PennyLane `default.mixed`
- **p = 0.00 (Ideal):** Purity = $1.0000$, Kernel Fidelity = $1.0000$, AUPRC = $0.4821$.
- **p = 0.01 (NISQ Minimal):** Purity = $0.9406$, Kernel Fidelity = $0.9995$, AUPRC = $0.4821$.
- **p = 0.05 (NISQ Moderate):** Purity = $0.7418$, Kernel Fidelity = $0.9856$, AUPRC = $0.4678$.
- **p = 0.10 (NISQ Severe):** Purity = $0.5647$, Kernel Fidelity = $0.9422$, AUPRC = $0.4678$.

**Finding:** Physical noise monotonically degrades quantum state purity and downstream classification accuracy. Physical QPUs cannot exceed ideal simulator accuracy.
