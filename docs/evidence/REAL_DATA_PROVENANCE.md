# Real Data Provenance Freeze — IEEE-CIS Fraud Detection

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Dataset Origin:** Official IEEE-CIS Fraud Detection Benchmark (Kaggle Competition)  
**Ingestion Timestamp:** 2026-09-12  
**Audit Protocol:** `vNEXT.3` Phase 156  

---

## 1. Raw Data Integrity & Cryptographic Hashes

Every raw file utilized in this investigation was streamed directly via authenticated Kaggle API from the official competition repository. Hashes were computed using chunked SHA-256 (64 KB buffers):

| File Name | SHA-256 Checksum | File Size (Bytes) | Exact Row Count | Exact Column Count |
| :--- | :--- | :---: | :---: | :---: |
| `train_transaction.csv` | `3a5c83ab6b3cc13dcabe5ffa9f522307fd5f7f7b6e6f6a60c32284ca6283d642` | 683,351,067 | **590,540** | **394** |
| `train_identity.csv` | `b63c725d8377be90a995268d97f347c17d456b95db45807adcf9f59cd603c37c` | 26,529,680 | **144,233** | **41** |

> [!IMPORTANT]
> **Data Privacy & Storage Policy:**  
> Raw data files (`data/raw/*.csv`) and processed parquet files (`data/real/*.parquet`) are strictly gitignored and reside solely on local authenticated research drives. No proprietary raw transaction data is committed to the remote git repository.

---

## 2. Table Join & Identity Coverage Audit

- **Primary Entity Key:** `TransactionID` (32-bit integer).
- **Primary Transaction Count:** 590,540 distinct transactions.
- **Identity Profile Records:** 144,233 distinct records.
- **Join Cardinality:** Left Outer Join on `TransactionID` ($1 : \le 1$).
- **Identity Match Rate:** **24.4239%** (144,233 / 590,540).
- **Engineering SLA Decision:** Because 75.58% of transactions lack identity attributes (e.g., DeviceType, DeviceInfo, id_01 to id_38), identity features cannot be mandated for a 100% SLA frontline payment authorization detector without massive imputation artifacts. Frontline decision-time inference operates strictly on transaction-level payload features (`TransactionAmt`, card attributes, temporal deltas).

---

## 3. Target Distribution & Severe Class Imbalance

- **Target Column:** `isFraud` (binary integer: `0` = legitimate, `1` = fraudulent).
- **Total Transactions ($N$):** 590,540
- **Total Fraudulent Transactions ($N_{\text{fraud}}$):** **20,663**
- **Total Legitimate Transactions ($N_{\text{legit}}$):** **569,877**
- **Empirical Fraud Prevalence ($\pi$):** **3.4990%** ($0.034990009$)
- **Imbalance Ratio:** 1 fraudulent transaction per **27.58** legitimate transactions.

---

## 4. Temporal Ordering & Time Horizon

- **Time Vector:** `TransactionDT` represents elapsed seconds from an unrevealed initial reference epoch ($t_0 = 0$).
- **Minimum TransactionDT:** `86,400` seconds (Day 1.000).
- **Maximum TransactionDT:** `15,811,131` seconds (Day 183.000).
- **Total Observation Horizon:** 15,724,731 seconds = **181.999 days** (~6 months).
- **Chronological Sorting:** All transaction records are strictly ordered by `TransactionDT` prior to partitioning to preserve temporal causality.

---

## 5. Data Hygiene & Missingness Profile

- **Total Matrix Cells:** $590,540 \times 394 = 232,672,760$ cells.
- **Total Missing Cells:** 95,557,211 cells (**41.07%** overall missingness rate).
- **Duplicate Keys:** Exactly **0 duplicate `TransactionID` entries** detected in `train_transaction.csv`.
- **Handling Strategy:** Missing numerical feature entries are imputed using training-split median values strictly computed on the training partition ($N=383,851$) without future lookahead.
