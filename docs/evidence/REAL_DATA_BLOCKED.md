# Real Data Ingestion Gate: Access Blocked Declaration (Phase 100)
## Master Autonomous Scientific Loop — HSBC Quantum Fraud Detection

> **Global Scientific Status:**
> `[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]`
>
> **Gate Decision:** `[BLOCKED: REAL DATA]`  
> **Evaluation Date:** 2026-09-12  
> **Enforcement Code:** [`src/data/make_dataset.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/data/make_dataset.py) (`RealDataBlockedError`)  

---

## 1. Exact Missing Dependency
- **Missing File:** `C:\Users\noobg\.kaggle\kaggle.json`
- **Missing Environment Variables:** `KAGGLE_USERNAME`, `KAGGLE_KEY`
- **Competition Rule:** The official IEEE-CIS Fraud Detection dataset is hosted under competition terms on Kaggle (`kaggle competitions download -c ieee-fraud-detection`). Ingestion requires an authenticated user token who has accepted the competition agreement.
- **Firewall Policy:** Autonomous downloading of unauthorized mirror files or unverified external sources is strictly prohibited to avoid licensing violations and dataset contamination.

---

## 2. Exact Expected Files
When real data access is enabled, the pipeline expects the raw competition archive to yield:
1. `data/raw/train_transaction.csv`
   - **Expected Rows:** $590,540$ transactions
   - **Expected Columns:** $394$ features (`TransactionID`, `isFraud`, `TransactionDT`, `TransactionAmt`, `ProductCD`, `card1`–`card6`, `addr1`–`addr2`, `dist1`–`dist2`, `P_emaildomain`, `R_emaildomain`, `C1`–`C14`, `D1`–`D15`, `M1`–`M9`, `V1`–`V339`)
   - **Expected Target Prevalence:** $\approx 3.499\%$ fraud rate ($20,663$ positive cases)
2. `data/raw/train_identity.csv` (Optional enricher)
   - **Expected Rows:** $144,233$ records
   - **Expected Columns:** $41$ identity features (`id_01`–`id_38`, `DeviceType`, `DeviceInfo`)

---

## 3. Exact Ingestion Command
Once credentials are provided, execution will proceed deterministically via:
```bash
# Verify credentials exist
kaggle competitions download -c ieee-fraud-detection -p data/raw/

# Run verified ingestion and schema validation gate
python -c "from src.data.make_dataset import ingest_real_ieee_cis, perform_temporal_split; ingest_real_ieee_cis(); perform_temporal_split()"
```

---

## 4. Exact Schema Contract
The ingestion validator (`src/data/schema_validator.py`) enforces the following real-data contract before allowing any downstream execution:
- **Mandatory Columns:** `TransactionID`, `isFraud`, `TransactionDT`, `TransactionAmt`, `card1`.
- **Target Invariant:** `isFraud` must be strictly binary ($\{0, 1\}$) with fraud rate between $0.5\%$ and $10.0\%$.
- **Temporal Invariant:** `TransactionDT` must be strictly positive and chronologically sortable with zero negative deltas.
- **Row Invariant:** Row count must exceed $100,000$ records to confirm genuine competition scale.

---

## 5. Exact Next Action for User / Operator
To transition the repository from `[REAL DATA BLOCKED]` to `[REAL DATA]` empirical evaluation:
1. Generate an API token from Kaggle Account Settings (`kaggle.json`).
2. Place the token at `C:\Users\noobg\.kaggle\kaggle.json` or export:
   ```powershell
   $env:KAGGLE_USERNAME="your_kaggle_username"
   $env:KAGGLE_KEY="your_kaggle_api_key"
   ```
3. Re-run the ingestion pipeline:
   ```bash
   python -m pytest tests/test_real_data_gate.py
   ```

Until these credentials are provided, all ongoing pipeline hardening, router evaluation, and classical controls proceed strictly using the pre-registered synthetic benchmark fixture (`10,000` rows, seed `42`), explicitly labeled:
```
[SYNTHETIC] [MEASURED] [VERIFIED]
```
