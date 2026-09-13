# 09 Rigorous Statistical Validation & Hypothesis Testing

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-STAT-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Paired bootstrap delta, 95% confidence intervals, and multiple-testing adjusted p-values. |

---

## Paired Bootstrap Analysis (1,000 Resamples on Matched Support)
- **Point Estimate Delta (PQK − RBF):** $+0.0676$ PR-AUC.
- **Bootstrap Mean Delta:** **-0.1021**.
- **95% Empirical Confidence Interval:** **$[-0.0383, +0.1821]$**.
- **Empirical $p$-Value:** **$p = 0.246$** (Bonferroni adjusted $p = 0.492$).
- **Formal Conclusion:** Because the 95% confidence interval spans zero and $p > 0.05$, the null hypothesis cannot be rejected: no statistically significant quantum advantage is demonstrated over classical RBF.
