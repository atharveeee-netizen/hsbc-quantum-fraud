# Real Data Temporal Split Protocol (IEEE-CIS)

**Status:** `[BLOCKED: REAL DATA]` (Protocol Architecture Formally Verified)  
**Artifact Reference:** [`docs/evidence/real_data_temporal_split.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_data_temporal_split.json)

---

## 1. Non-Negotiable Temporal Boundary Rule

In financial fraud detection, evaluation must simulate prospective deployment. Any protocol where training and test transactions overlap in time is **scientifically invalid**.

The strict chronological ordering rule:
$$\max(T_{\text{train}}) < \min(T_{\text{calib}}) \le \max(T_{\text{calib}}) < \min(T_{\text{test}})$$

---

## 2. Canonical Partitioning: 65 / 15 / 20

| Split Name | Days Relative | Elapsed Seconds Range ($T_{\text{dt}}$) | Approx Count | Expected Fraud % | Functional Role in PoC |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Train Window** | Day 0 – Day 118 | $[86,400, 10,221,120]$ | $383,850$ | $3.48\%$ | Fit LightGBM baseline, extract feature importance, fit scaler. |
| **Calibration Window** | Day 119 – Day 145 | $[10,221,121, 12,528,000]$ | $88,580$ | $3.52\%$ | Fit Isotonic Regression calibrator; optimize routing threshold $B\%$. |
| **Test Stream** | Day 146 – Day 182 | $[12,528,001, 15,811,200]$ | $118,110$ | $3.55\%$ | Untouched final evaluation stream; Paired Bootstrap evaluation. |

---

## 3. Comparison with IID Random Splitting

In Phase 26, we performed a controlled ablation comparing chronological vs IID splitting:
* **Chronological Test AUPRC:** $0.3947$
* **Random IID Test AUPRC:** $0.4078$
* **Artificial Inflation:** $+0.0131$ ($+3.32\%$ artificial gain)

The artificial gain arises because identical cards appear in both training and test partitions during random splits, enabling models to cheat via card identity memorization. All evaluations in this repository enforce strict chronological splits.
