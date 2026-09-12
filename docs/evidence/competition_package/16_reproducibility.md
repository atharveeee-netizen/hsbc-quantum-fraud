# 16 Environment & Code Reproducibility Audit

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-REPRO-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Environment configuration, seed determinism, and independent reproduction commands. |

---

## Independent Verification Instructions
- **Virtual Environment:** Python 3.10 with pinned packages in `requirements.txt`.
- **Full Test Suite:** Run `pytest` to execute all 24 unit, provenance, and firewall tests.
- **Interactive App:** Run `streamlit run src/dashboard/app.py`.
- **Real Data Execution:** Authenticate with Kaggle and run `python -m src.evaluation.run_real_scientific_suite`.
