# 09 Statistical Falsification & Bootstrap Discipline

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-STATS-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c0968b6` |
| **Metric Definition** | Paired bootstrap distributions (B=1,000), 95% confidence intervals, and Bonferroni corrections. |

---

## Rigorous Falsification Protocol
- **Paired Bootstrap:** 1,000 resamples of test predictions evaluated simultaneously on identical bootstrapped samples.
- **Statistical Test:** Paired difference test $\Delta = \text{AUPRC}_{\text{Quantum}} - \text{AUPRC}_{\text{RBF}}$.
- **Confidence Intervals:** 95% percentile bootstrap intervals include zero across all evaluated escalation budgets.
- **Multi-Seed Testing:** 5 random seeds (42, 43, 44, 45, 46) confirm the difference remains non-positive and centered at zero.
- **Verdict:** The null hypothesis cannot be rejected. No statistically supported quantum advantage exists.
