# Real IEEE-CIS Data Ingestion Report

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 124  
**Evidence Artifact:** [`docs/evidence/real_data_ingestion.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_data_ingestion.json)  
**Dataset Source:** Official IEEE Computational Intelligence Society (IEEE-CIS) Fraud Detection Competition via Kaggle API  

---

## 1. Provenance & Cryptographic Verification

| File Name | File Size (Bytes) | SHA-256 Checksum | Ingestion Status |
| :--- | :---: | :--- | :---: |
| `train_transaction.csv` | 683,351,067 | `3a5c83ab6b3cc13dcabe5ffa9f522307fd5f7f7b6e6f6a60c32284ca6283d642` | `[VERIFIED]` |
| `train_identity.csv` | 26,529,680 | `b63c725d8377be90a995268d97f347c17d456b95db45807adcf9f59cd603c37c` | `[VERIFIED]` |

* **Ingestion Method:** Direct REST API streaming via authenticated Kaggle API token (`KGAT_...`).
* **Raw Files Stored:** `data/raw/train_transaction.csv` and `data/raw/train_identity.csv` (strictly excluded from Git tracking via `.gitignore`).

---

## 2. Table Schemas & Record Properties

### 2.1 `train_transaction.csv`
* **Total Transactions (Rows):** **590,540**
* **Total Columns:** **394**
* **Primary Key:** `TransactionID` (Zero duplicate records detected; strictly unique).
* **Target Variable:** `isFraud` (Binary: 0 = Legitimate, 1 = Fraudulent).
* **Fraud Count:** **20,663** fraudulent transactions.
* **Legitimate Count:** **569,877** legitimate transactions.
* **Empirical Fraud Prevalence:** **$3.4990\%$** (1 fraud per 27.5 legitimate transactions).
* **Temporal Coordinate:** `TransactionDT` (Integer seconds since reference timestamp).
  * Minimum `TransactionDT`: **86,400** (Day 1).
  * Maximum `TransactionDT`: **15,811,131** (Day 182.99).
  * Total Observed Duration: **182.0 days** (~6 months).

### 2.2 `train_identity.csv`
* **Total Identity Records:** **144,233**
* **Total Columns:** **41** (Device information, IP networks, browser user-agents, OS types).
* **Transaction Match Rate:** **$24.42\%$** (Only 144,233 out of 590,540 transactions possess an accompanying identity profile).
* **Design Decision:** The frontline classical model must operate on transaction features available for 100% of volume; identity features are reserved for specialist escalation queues.
