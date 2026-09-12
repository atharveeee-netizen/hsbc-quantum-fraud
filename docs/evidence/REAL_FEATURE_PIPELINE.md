# Real-Data Feature Engineering Pipeline

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 128  
**Artifact Directory:** [`data/real/`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/data/real)  

---

## 1. Pipeline Principles & Invariants

1. **Deterministic Execution:** Seed fixed to $42$ across all sampling, partitioning, and model initializations.
2. **Train-Fitted Transformations:**
   * Missing value imputation medians are computed **strictly from the Train partition** ($N=383,851$).
   * Z-score scaling parameters ($\mu, \sigma$) are computed **strictly from the Train partition**.
   * Calibration and Test splits are transformed using stored Train parameters; zero parameters are learned from out-of-sample data.
3. **Reproducible Parquet Artifacts:**
   * `data/real/train_scaled.parquet` ($383,851\text{ rows}$)
   * `data/real/test_scaled.parquet` ($118,108\text{ rows}$)

---

## 2. Feature Definitions & Transformation Schema

| Feature | Input Type | Missing Handling | Normalization |
| :--- | :--- | :--- | :--- |
| `TransactionAmt` | Continuous Float | None ($0.0\%$ missing) | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `card1` | Numeric Categorical | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `card2` | Numeric Categorical | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `card3` | Numeric Categorical | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `card5` | Numeric Categorical | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `C1` | Count Integer | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `C2` | Count Integer | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `C5` | Count Integer | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `C13` | Count Integer | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
| `D1` | Timedelta Integer | Imputed with Train Median | Standardized ($\mu_{\text{train}}, \sigma_{\text{train}}$) |
