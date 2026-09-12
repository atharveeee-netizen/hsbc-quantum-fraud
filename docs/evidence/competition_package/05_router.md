# 05 Selective Uncertainty Router & Ablation Audit

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-ROUTER-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Fraud concentration, enrichment ratio, and routing mechanism ablation. |

---

## Router Multi-Budget Performance on Real Data
- **0.5% Budget (591 tx):** **42.81% fraud density** (**12.44x enrichment**, 253 frauds captured).
- **1.0% Budget (1,181 tx):** **37.26% fraud density** (**10.83x enrichment**, 440 frauds captured).
- **2.0% Budget (2,362 tx):** **30.48% fraud density** (**8.86x enrichment**, 720 frauds captured).
- **5.0% Budget (5,905 tx):** **26.40% fraud density** (**7.67x enrichment**, 1,559 frauds captured).

## Routing Ablation Finding
At the 0.5% budget, uncertainty routing captures **253 frauds** (42.81% density), whereas amount-only routing captures only **9 frauds** (1.52% density). The routing benefit is driven by model uncertainty, not transaction magnitude.
