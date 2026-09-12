# 03 Real Dataset Provenance & Ingestion Freeze

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-DATA-PROV-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Cryptographic hashes, row counts, monotonic temporal boundaries, and zero target leakage. |

---

## Verified Raw Data Provenance (IEEE-CIS)
- **Raw Transaction File:** `train_transaction.csv` (SHA-256: `3a5c83ab6b3cc13dcabe5ffa9f522307fd5f7f7b6e6f6a60c32284ca6283d642`, 590,540 rows, 394 cols).
- **Raw Identity File:** `train_identity.csv` (SHA-256: `b63c725d8377be90a995268d97f347c17d456b95db45807adcf9f59cd603c37c`, 144,233 rows, 41 cols).
- **Identity Join Rate:** 24.42% (excluded from frontline 100% SLA authorization to prevent massive missingness imputation).
- **Chronological Partitions:**
  - **Train (65%):** $N=383,851$, Days 1.0 – 111.3 ($T \in [86400, 9614637]$), $\pi = 3.42\%$.
  - **Calibration (15%):** $N=88,581$, Days 111.3 – 141.1 ($T \in [9614722, 12192842]$), $\pi = 3.92\%$.
  - **Test (20%):** $N=118,108$, Days 141.1 – 183.0 ($T \in [12192900, 15811131]$), $\pi = 3.44\%$.
- **Monotonicity Proof:** $\max(T_{\text{train}}) < \min(T_{\text{calib}}) < \min(T_{\text{test}})$ (Zero boundary leakage).
