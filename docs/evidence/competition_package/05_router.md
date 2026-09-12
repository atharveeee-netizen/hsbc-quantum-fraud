# 05 Selective Escalation Router & Enrichment Audit

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-ROUTER-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e9bd296` |
| **Metric Definition** | Fraud enrichment factor = (Escalated Fraud Rate) / (Base Population Fraud Rate). |

---

## Router Enrichment Factors (Associative Audit)
- **Amount-Based Routing:** **$2.09\times$** fraud concentration over base rate.
- **Combined (Amount + Uncertainty):** **$1.63\times$** fraud concentration.
- **Orthogonal Uncertainty (Residual):** **$1.23\times$** additive enrichment.
- **Uncertainty Margin Only:** **$0.96\times$**.
- **Random Routing Control:** **$0.78\times$**.

> [!NOTE]
> Amount-based routing produced measured enrichment under the tested synthetic benchmark. This is an associative enrichment result reflecting transaction risk distribution, not a causal relationship between transaction amount and fraud occurrence.
