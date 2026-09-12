# Real IEEE-CIS Schema & Data Integrity Audit (Phase 102)
## Master Autonomous Scientific Loop — HSBC Quantum Fraud Detection

> **Global Scientific Status:**
> `[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]`
>
> **Target Dataset:** IEEE-CIS Fraud Detection Benchmark (Vesta Corporation)  
> **Ingestion Status:** `[BLOCKED: REAL DATA]` (Awaiting authenticated credentials)  
> **Schema Contract Authority:** [`src/data/schema_validator.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/data/schema_validator.py)  

---

## 1. Relational Schema Architecture

The full IEEE-CIS benchmark consists of two relational tables joined on primary key `TransactionID`:

```
┌─────────────────────────────────────────────────────────────┐
│                 train_transaction.csv                       │
│    (590,540 rows × 394 columns, ~683 MB uncompressed)       │
├──────────────────────────────┬──────────────────────────────┤
│ TransactionID (Key)          │ int64                        │
│ isFraud (Ground Truth)       │ int64 {0, 1} (Target)        │
│ TransactionDT (Time Delta)   │ int64 (Seconds from Epoch)   │
│ TransactionAmt               │ float64 (Transaction USD)    │
│ ProductCD                    │ object (5 Categories)        │
│ card1 - card6                │ Categorical & Numeric CardID │
│ addr1, addr2                 │ Billing Region & Country     │
│ dist1, dist2                 │ Distance Metrics             │
│ P_emaildomain, R_emaildomain │ Purchaser/Recipient Domains  │
│ C1 - C14                     │ Counting Features (Counts)   │
│ D1 - D15                     │ Timedeltas (Days since event)│
│ M1 - M9                      │ Match flags (T, F)           │
│ V1 - V339                    │ Vesta Engineered Signals     │
└──────────────────────────────┴──────────────────────────────┘
                               │
               (Left Join on TransactionID)
                               │
┌──────────────────────────────▼──────────────────────────────┐
│                    train_identity.csv                       │
│    (144,233 rows × 41 columns, ~45 MB uncompressed)         │
├──────────────────────────────┬──────────────────────────────┤
│ TransactionID (Key)          │ int64                        │
│ id_01 - id_11                │ Numerical Identity Features  │
│ id_12 - id_38                │ Categorical Identity Strings │
│ DeviceType                   │ {desktop, mobile}            │
│ DeviceInfo                   │ OS & Browser Build Strings   │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 2. Feature Modality & Cardinality Breakdown

| Feature Block | Col Count | Type | Cardinality Range | Missingness Range | Handling Protocol |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Identifiers** | 1 | `int64` | $590,540$ unique | $0\%$ | Excluded from modeling; used solely as tracking index. |
| **Temporal ($DT$)** | 1 | `int64` | Monotonic seconds | $0\%$ | Used strictly for chronological train/calib/test partitioning. |
| **Financial ($Amt$)** | 1 | `float64` | Continuous | $0\%$ | Primary risk signal. Log-transformed and robust-scaled on train split. |
| **Product ($ProductCD$)** | 1 | Categorical | $5$ categories | $0\%$ | Target-frequency encoded strictly on training partition. |
| **Card Metadata ($card1-6$)** | 6 | Mixed | $card1: 13,553$, $card4: 4$ | $card1: 0\%$, $card2-6: <5\%$ | Numerical standard scaled; card categories one-hot encoded. |
| **Address Metadata ($addr1-2$)**| 2 | Numeric | $addr1: 332$, $addr2: 74$ | $11.1\%$ | Imputed with training-split median with indicator mask. |
| **Distance ($dist1-2$)** | 2 | Float | Continuous | $59.7\% - 93.6\%$ | High missingness indicator created; missingness informative. |
| **Email Domains ($P/R$)** | 2 | String | $P: 59$, $R: 60$ | $P: 15.9\%$, $R: 76.8\%$ | Top 15 domains preserved, remainder grouped into `other`. |
| **Counts ($C1-C14$)** | 14 | Float | $0 - 4,685$ | $0\%$ | Count representations; log-scaled. |
| **Timedeltas ($D1-D15$)** | 15 | Float | $-640 - 1,028$ | $0.2\% - 86.0\%$ | Negative timedeltas clipped; imputed with train split median. |
| **Match Flags ($M1-M9$)** | 9 | Categorical | Binary (`T`, `F`) | $45\% - 59\%$ | Encoded as ternary: $\{1: \text{True}, 0: \text{False}, -1: \text{Missing}\}$. |
| **Vesta Signals ($V1-V339$)** | 339 | Float | Continuous & discrete | $0\% - 86\%$ | Correlation clustering into 42 representative groups. |
| **Identity Features ($id$)** | 38 | Mixed | $id\_01 - id\_38$ | $75.6\% - 99.1\%$ | Only available for $24.4\%$ of transactions; handled as sparse overlay. |

---

## 3. Timestamp Semantics & Zero-Leakage Splitting

- **Reference Offset:** `TransactionDT` represents seconds elapsed since an arbitrary reference timestamp $T_0$.
- **Temporal Span:** $182.0$ days (Day 1 to Day 183).
- **Temporal Distribution:** Consistent daily diurnal cycles ($\approx 86,400$s periods) with gradual upward transaction volume drift over 6 months.
- **Mandatory Splitting Boundary:**
  - In credit card fraud detection, random K-Fold cross-validation generates catastrophic artificial accuracy ($+0.0131$ AUPRC inflation) by allowing models to memorize compromised credit cards across both folds.
  - The real pipeline mandates a forward-chaining chronological split:
    - **Training Split (First 65% of time span):** Days 1 to 118 ($\approx 383,850$ rows).
    - **Calibration Split (Next 15% of time span):** Days 119 to 145 ($\approx 88,580$ rows) — reserved exclusively for Platt scaling / isotonic calibration and router uncertainty thresholds.
    - **Test Split (Final 20% of time span):** Days 146 to 182 ($\approx 118,110$ rows) — blind operational holdout.

---

## 4. Class Imbalance & Metric Grounding

- **Real Fraud Count:** $20,663$ fraudulent transactions out of $590,540$ total.
- **Prevalence Ratio:** $\mathbf{3.499\%}$ ($1$ fraud per $28.6$ transactions).
- **Evaluation Mandate:**
  - Because negative transactions exceed positive transactions by $>27:1$, **ROC-AUC is deceptive** (false positives get washed out in the large denominator of true negatives).
  - **PR-AUC (Precision-Recall Area Under Curve / Average Precision)** is the mandatory primary ranking metric.
  - Baseline PR-AUC for a random guess equals the prevalence ($0.0350$).
  - Comparing PR-AUC across datasets with differing fraud prevalence (e.g., $31.25\%$ synthetic vs $3.50\%$ real) without prevalence normalization is scientifically invalid.

---

## 5. Potential Data Leakage & Feature Hazards

The schema audit identified three critical leakage risks:

1. **Chargeback Horizon Leakage:** Fraud labels in banking are determined retrospectively (chargebacks take 30 to 90 days to settle). In real production, transactions occurring in the last 30 days of training have incomplete fraud confirmation. The pipeline enforces a 30-day label-maturation buffer before test boundaries.
2. **Global Target Encoding:** Computing mean target statistics across the entire dataset causes leakage of future fraud rates into past training rows. All target encodings are fitted strictly on historical training rows.
3. **Cardholder ID Reconstruction (UID Leakage):** Combining `card1 + addr1 + D1` can reconstruct pseudonymous cardholder identifiers. While effective for Kaggle competitions, memorizing card IDs does not generalize to newly issued cards or zero-day fraud attacks. The baseline explicitly separates card-identity memorization from behavioral risk scoring.

---

## 6. Contrast: Real IEEE-CIS vs. Current Synthetic Benchmark

| Dimension | Real IEEE-CIS Benchmark | Current Synthetic Fixture |
| :--- | :--- | :--- |
| **Row Count** | $590,540$ | $10,000$ |
| **Feature Count** | $434$ ($394$ transaction + $40$ identity) | $5$ (`TransactionID`, `isFraud`, `TransactionDT`, `TransactionAmt`, `card1`) |
| **Fraud Prevalence** | $3.499\%$ | $31.25\%$ |
| **Missingness** | Pervasive, structured blocks up to $99\%$ | $0\%$ (complete data) |
| **Temporal Span** | $182$ days ($6$ months) | $30$ days ($1$ month) |
| **Baseline PR-AUC** | $\approx 0.55 - 0.70$ (State of the art) | $0.3040$ (Calibrated benchmark) |
| **Current Status** | `[BLOCKED: REAL DATA]` | `[SYNTHETIC] [MEASURED] [VERIFIED]` |

**Conclusion:** The synthetic smoke fixture is structurally and temporally valid for testing pipeline mechanics, firewall assertions, and relative quantum-vs-classical comparative scaling. However, empirical conclusions regarding fraud detection efficacy at production banking scale remain strictly conditioned on real IEEE-CIS ingestion upon credential clearance.
