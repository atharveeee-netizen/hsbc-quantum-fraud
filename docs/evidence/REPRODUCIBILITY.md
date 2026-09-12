# Reproducibility Audit & Execution Manifest (Phase 75)

**Overall Status:** `[VERIFIED: 100% REPRODUCIBLE]`  
**Runtime Environment:** Python 3.10.11 on `win32`  

---

## Reproducibility Checklist

* **critical_dependencies_pinned:** `[VERIFIED]`
* **directory_structure:** `[VERIFIED]`
* **seed_determinism:** `[VERIFIED]`
* **evidence_integrity:** `[VERIFIED]`
* **pytest_suite:** `[VERIFIED]`

---

## Canonical Reproduction Workflow

A new researcher can clone a clean checkout and run the full pipeline deterministically:

```bash
pip install -r requirements.txt
python -m src.data.generate_synthetic
python -m src.data.make_dataset
python -m src.features.build_features
python -m src.models.classical.train_baseline
python -m src.evaluation.budget_sweep
python scripts/verify_evidence_integrity.py
pytest
```

---

## Blocker Disclosure

* `[BLOCKED: REAL DATA]` - Real IEEE-CIS data access requires `kaggle.json` or local `train_transaction.csv`. Synthetic pipeline executes automatically as fallback.
* `[BLOCKED: QPU EXECUTION]` - Physical QPU execution requires AWS Braket credentials. Local PennyLane statevector simulator (`default.qubit` / `default.mixed`) executes automatically.
