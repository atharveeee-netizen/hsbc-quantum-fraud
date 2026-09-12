# Real Temporal Dataset Partitioning & Validation Freeze

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 158  
**Evidence Artifact:** [`docs/evidence/real_temporal_split.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_temporal_split.json)  
**Partitioning Strategy:** Strict Chronological Monotonic Splitting  

---

## 1. Temporal Horizon & Resolution

The IEEE-CIS transaction log represents continuous digital payment traffic recorded via the relative second offset `TransactionDT`:

* **Total Observed Duration:** $15,724,731\text{ seconds} = \mathbf{181.999\text{ days}}$ (~26.0 weeks).
* **Minimum `TransactionDT`:** $86,400\text{ seconds}$ (Day 1.000, 24:00:00 UTC).
* **Maximum `TransactionDT`:** $15,811,131\text{ seconds}$ (Day 183.000).
* **Transaction Throughput:** 590,540 transactions across 182 days ($\approx 3,245\text{ transactions/day}$).

---

## 2. Chronological Partition Boundaries & Monotonicity Proof

To eliminate future lookahead bias, partitions were created strictly by sorting the 590,540 transactions by `TransactionDT` and dividing into three contiguous temporal epochs:

| Partition Split | Fraction | Transaction Count | $T_{\min}$ (s) | $T_{\max}$ (s) | Calendar Span (Days) | Fraud Count | Fraud Prevalence ($\pi$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Train Split** | **65.0%** | **383,851** | 86,400 | 9,614,637 | Days 1.00 – 111.28 | 13,126 | 3.4196% |
| **Calibration Split** | **15.0%** | **88,581** | 9,614,722 | 12,192,842 | Days 111.28 – 141.12 | 3,473 | 3.9207% |
| **Test Split** | **20.0%** | **118,108** | 12,192,900 | 15,811,131 | Days 141.12 – 183.00 | 4,064 | 3.4409% |

### Formal Monotonicity Proof:

1. **Train-to-Calibration Boundary:**
   $$\max(T_{\text{train}}) = 9,614,637 < \min(T_{\text{calib}}) = 9,614,722$$
   $$\Delta T = +85\text{ seconds} > 0$$
   *(Zero transaction overlap between Train and Calibration partitions).*

2. **Calibration-to-Test Boundary:**
   $$\max(T_{\text{calib}}) = 12,192,842 < \min(T_{\text{test}}) = 12,192,900$$
   $$\Delta T = +58\text{ seconds} > 0$$
   *(Zero transaction overlap between Calibration and Test partitions).*

---

## 3. Feature Construction Lineage & Anti-Leakage Audit

Under the audited feature construction pipeline:
* **No Transaction Overlap:** Every transaction belongs to exactly one chronological epoch; indices are mutually disjoint.
* **No Partition-Boundary Leakage:** Feature imputation values (medians) and standardization statistics ($\mu, \sigma$) are computed **strictly on the Train partition ($N=383,851$)** and stored as frozen parameters. Calibration and Test partitions undergo out-of-sample transformation using these frozen training statistics without updating them.
* **Zero Future Windowing:** The evaluated frontline feature set consists strictly of transaction-level attributes available at authorization time (`TransactionAmt`, `card1`, `card2`, `card3`, `card5`, `C1`, `C2`, `C5`, `C13`, `D1`). No future sliding aggregations or backward-looking rolling counts that span across partition boundaries were constructed.
* **Formal Conclusion:** We certify **no transaction overlap and no observed partition-boundary leakage under the audited feature construction**.
