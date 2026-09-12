# Real Data Schema & Feature Availability Audit (IEEE-CIS)

**Dataset:** IEEE-CIS Fraud Detection (Vesta Corporation / Kaggle)  
**Status:** `[BLOCKED: REAL DATA]` (Specification & Schema Pre-Flight Verified)  
**Artifact Reference:** [`docs/evidence/real_data_schema.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_data_schema.json)

---

## 1. Schema Overview

The IEEE-CIS dataset comprises two relational tables joined by `TransactionID`:
1. `train_transaction.csv` ($590,540$ rows, $394$ columns): Core transactional payload, payment cards, amounts, timing, counting, and Vesta engineered features.
2. `train_identity.csv` ($144,233$ rows, $41$ columns): Device identity, browser versions, operating systems, and network parameters.

---

## 2. TransactionDT Semantics & Temporal Boundaries

* **Definition:** An integer timedelta representing elapsed seconds from an undisclosed reference epoch ($T_0$).
* **Minimum Value:** $86,400$ (representing Day 1, 24:00:00).
* **Span:** $182$ days across training transactions.
* **Non-resettable Monotonicity:** In credit card fraud, user behavior, fraud attack vectors, and cardholder spending habits drift over time. Cross-validation MUST strictly respect chronological ordering ($T_{\text{train}} < T_{\text{calib}} < T_{\text{test}}$).
* **Leakage Danger:** Random IID sampling mixes cardholder identities across time, enabling models to memorize specific compromised cards rather than learning generalizable fraud patterns. In Phase 26, this artificial inflation was empirically measured at $+0.0131$ AUPRC.

---

## 3. Target Variable & Class Imbalance

* **Target Column:** `isFraud` (Binary: 0 for legitimate, 1 for fraudulent).
* **Class Imbalance:** Fraud rate is $\approx 3.499\%$ ($20,663$ positive cases out of $590,540$).
* **Evaluation Metric:** Precision-Recall AUC (AUPRC / PR-AUC) is the mandatory primary metric. ROC-AUC is misleadingly high due to the overwhelming volume of true negatives.

---

## 4. Missingness Structure & Sparsity Blocks

1. **Low Missingness (<10%):** `TransactionAmt`, `ProductCD`, `card1`, `C1-C14`.
2. **Medium Missingness (10%–50%):** `card2-card6`, `addr1-addr2`, `P_emaildomain`.
3. **High Missingness (>50%):** `dist1`, `dist2`, `R_emaildomain`, `D6-D9`, `id_01-id_38`.
4. **Vesta V-Features (V1–V339):** Co-missingness clusters correspond to merchant checkout systems. Global median imputation distorts these sparsity signatures; LightGBM handles native NaN branching, which is preserved in our baseline.

---

## 5. Authorization-Time Availability & Exclusions

In a production banking authorization flow (e.g. HSBC Card-Not-Present authorization), decisions must occur within **$100-300$ ms**. Features must be rigorously audited for temporal availability:

| Feature / Signal | Authorization Availability | Decision & Rationale |
| :--- | :---: | :--- |
| `TransactionAmt` | **Immediate** | Included. Primary risk factor. |
| `card1-card6`, `addr1-addr2` | **Immediate** | Included. Core card metadata. |
| `P_emaildomain`, `R_emaildomain` | **Immediate** | Included with frequency encoding fit on training set only. |
| `C1-C14`, `D1-D15` | **Immediate** | Included. Historical transaction counts and days since previous event. |
| Chargeback Settlement Flags | **Unavailable (+30 to +90 days)** | **EXCLUDED.** Chargebacks take weeks to resolve; using them at inference is impossible. |
| Global Out-of-Fold Target Encoding | **Post-hoc Leakage** | **EXCLUDED.** Target encodings computed across test windows cause catastrophic future leakage. |
| Future Rolling Velocities | **Future Leakage** | **EXCLUDED.** Rolling aggregations must only look backward ($t \le \text{TransactionDT}$). |

---

## 6. Quantum Dimension Constraints

Physical QPUs and simulators cannot ingest $394$ continuous/categorical features due to qubit count and circuit depth limits ($n_{\text{qubits}} \le 8$ in current NISQ regimes).
* **Downsampling:** Top $4-8$ mutual-information features derived strictly from training data (`TransactionAmt`, `card1`, `C1`, `C13`, `D1`, `D15`, `V258`, `V307`).
* **Preprocessing:** MinMax/StandardScaler fit strictly on training escalated partitions.
