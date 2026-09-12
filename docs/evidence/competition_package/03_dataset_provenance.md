# 03 Dataset Provenance & Data Firewall

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-DATA-PROV-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e9bd296` |
| **Metric Definition** | Data monotonicity, temporal boundaries, and absence of target leakage. |

---

## Provenance Boundary & Real Data Gate
- **Current Data Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`.
- **Real Data Status:** `[BLOCKED: REAL DATA]` (Awaiting IEEE-CIS / Kaggle API credentials).
- **Synthetic Fixture:** 10,000 transactions mirroring IEEE-CIS columns (`TransactionDT`, `TransactionAmt`, `card1`, `isFraud`).
- **Temporal Windows:**
  - **Train (70%):** $T \in [86400, 691200]$, $N=7,000$, Fraud Rate $= 3.49\%$.
  - **Calibration (10%):** $T \in [691200, 777600]$, $N=1,000$, Fraud Rate $= 3.50\%$.
  - **Test (20%):** $T \in [777600, 950400]$, $N=2,000$, Fraud Rate $= 3.50\%$.
- **Leakage Firewall:** Strict inequality $T_{\text{train}}^{\max} < T_{\text{calib}}^{\min} \le T_{\text{calib}}^{\max} < T_{\text{test}}^{\min}$. Preprocessing scalers fit strictly on training set.
