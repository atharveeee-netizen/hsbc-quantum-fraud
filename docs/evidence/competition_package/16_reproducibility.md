# 16 Reproducibility Audit & Execution Instructions

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-REPRO-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c58c174` |
| **Metric Definition** | Deterministic reproduction across Python 3.10+, pinned requirements, and fixed seeds. |

---

## Reproduction Instructions
The current synthetic evidence pipeline passed reproducibility checks under the documented environment.

```bash
# 1. Environment Setup
pip install -r requirements.txt

# 2. Pipeline Execution
python -m src.data.generate_synthetic
python -m src.data.make_dataset
python -m src.features.build_features
python -m src.models.classical.train_baseline

# 3. Evidence Compilation & Audits
python -m src.evaluation.budget_sweep
python -m src.evaluation.evidence_ledger
python scripts/verify_evidence_integrity.py
python scripts/audit_claim_firewall.py
python scripts/security_audit.py
python scripts/reproducibility_audit.py

# 4. Verification Tests
pytest
```
