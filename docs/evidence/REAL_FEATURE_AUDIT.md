# Real Feature Pipeline Audit — Lineage, Classification & Leakage Analysis

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 159  
**Audit Protocol:** `vNEXT.3`  
**Processed Artifacts:**  
* `data/real/train_scaled.parquet` ($N=383,851$)  
* `data/real/test_scaled.parquet` ($N=118,108$)  

---

## 1. Production Feature Taxonomy & Lineage Classification

The frontline classical and specialist pipeline utilizes 10 decision-time features available at payment authorization. Every feature is audited and classified below:

| Feature Name | Feature Type | Classification | Source & Semantics | Missingness (Train) | Imputation Strategy | Scaler Fit Partition | Leakage Risk Level |
| :--- | :---: | :---: | :--- | :---: | :--- | :---: | :---: |
| `TransactionAmt` | Continuous | **Raw** | Transaction value in USD | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `card1` | Discrete | **Categorical** | Card issuer identification code | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `card2` | Discrete | **Categorical** | Card identity verification number | 1.52% | Train median (361.0) | Train only ($\mu, \sigma$) | **Zero** |
| `card3` | Discrete | **Categorical** | Card issuing country/region code | 0.27% | Train median (150.0) | Train only ($\mu, \sigma$) | **Zero** |
| `card5` | Discrete | **Categorical** | Card product category / tier code | 0.73% | Train median (226.0) | Train only ($\mu, \sigma$) | **Zero** |
| `C1` | Discrete | **Aggregate** | Transaction count / frequency metric | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `C2` | Discrete | **Aggregate** | Address match / velocity counter | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `C5` | Discrete | **Aggregate** | Card velocity / counter attribute | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `C13` | Discrete | **Aggregate** | Cumulative activity count attribute | 0.00% | None | Train only ($\mu, \sigma$) | **Zero** |
| `D1` | Continuous | **Temporal** | Timedelta (days since card activation/previous event) | 0.21% | Train median (3.0) | Train only ($\mu, \sigma$) | **Zero** |

---

## 2. Invariant Checklist: Zero Boundary Leakage

1. **Target-Derived Features:**  
   **None.** Zero target encoding, out-of-fold target statistics, or target-mean aggregations were constructed. Features are purely operational transaction descriptors.
2. **Scaler & Imputer Fitting:**  
   `StandardScaler` and `SimpleImputer` (median) were fitted strictly on `X_train` ($N=383,851$). Parameter values ($\mu, \sigma, \text{median}$) were locked prior to transforming calibration ($N=88,581$) and test ($N=118,108$) splits.
3. **Temporal Directionality:**  
   No future windowing (such as future rolling means, future transaction counts, or backward-looking aggregates calculated across partition splits) was employed. All aggregates (`C1`–`C13`) were provided directly by IEEE-CIS as point-in-time features computed by the payment processor.
4. **Conclusion:**  
   All 10 features strictly satisfy the decision-time operational constraint and exhibit **zero partition-boundary leakage**.
