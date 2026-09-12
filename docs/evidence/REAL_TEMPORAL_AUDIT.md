# Real Temporal Dataset Partitioning & Audit Report

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 126  
**Evidence Artifact:** [`docs/evidence/real_temporal_split.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_temporal_split.json)  
**Partitioning Strategy:** Strict Chronological (No Random Splitting, No Future Leakage)  

---

## 1. Temporal Structure of Genuine IEEE-CIS

* **Total Observed Duration:** **$182.0\text{ days}$** ($15,724,731\text{ seconds}$).
* **Minimum `TransactionDT`:** $86,400$ ($24.0\text{ hours}$ mark).
* **Maximum `TransactionDT`:** $15,811,131$ ($182.99\text{ days}$).
* **Transaction Velocity:** Average $\approx 3,244\text{ transactions/day}$.

---

## 2. Chronological Partition Boundaries

To completely avoid temporal lookahead bias, partitions are constructed monotonically along the `TransactionDT` coordinate:

| Partition | Fraction | Transaction Count | $T_{\min}$ (s) | $T_{\max}$ (s) | Calendar Span (approx) | Fraud Count | Fraud Prevalence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train Split** | 65.0% | **383,851** | 86,400 | 10,277,532 | Days 1.0 – 118.9 | 13,126 | 3.4196% |
| **Calibration Split** | 15.0% | **88,581** | 10,277,575 | 12,652,010 | Days 119.0 – 146.4 | 3,472 | 3.9196% |
| **Test Split** | 20.0% | **118,108** | 12,652,036 | 15,811,131 | Days 146.4 – 183.0 | 4,065 | 3.4418% |

---

## 3. Strict Anti-Leakage Invariants

1. $\max(T_{\text{train}}) = 10,277,532 < \min(T_{\text{calib}}) = 10,277,575$ (Strict temporal gap, zero overlap).
2. $\max(T_{\text{calib}}) = 12,652,010 < \min(T_{\text{test}}) = 12,652,036$ (Strict temporal gap, zero overlap).
3. Preprocessing statistics (medians and standard scaling parameters) are fitted **strictly on the Train split** and applied out-of-sample to Calibration and Test splits.
