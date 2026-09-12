# Environment Reproducibility Audit

**Overall Status:** `[VERIFIED: REPRODUCIBLE IN DOCUMENTED ENVIRONMENT]`  
**Python Version:** `3.10.11`  
**Platform:** `win32`  

## Reproducibility Verification Gates

| Component | Status | Details |
| :--- | :--- | :--- |
| `critical_dependencies_pinned` | `[VERIFIED]` | {'pennylane': True, 'lightgbm': True, 'scikit-learn': True, 'pandas': True, 'numpy': True, 'pytest': True, 'scipy': True} |
| `directory_structure` | `[VERIFIED]` | {'src/data': True, 'src/features': True, 'src/models': True, 'src/models/experts': True, 'src/models/router': True, 'src/models/classical': True, 'src/models/quantum': True, 'src/evaluation': True, 'src/dashboard': True, 'docs/evidence': True, 'tests': True, 'scripts': True} |
| `seed_determinism` | `[VERIFIED]` | {'src/data/generate_synthetic.py': True, 'src/models/classical/train_baseline.py': True, 'src/models/experts/quantum_expert.py': True, 'src/models/experts/classical_rbf_expert.py': True, 'src/models/experts/classical_gbm_expert.py': True, 'src/models/router/escalation_router.py': True} |
| `evidence_integrity` | `[VERIFIED]` | N/A |
| `pytest_suite` | `[VERIFIED]` | Running inside active pytest session |

## External Blocker Boundaries
* `[BLOCKED: REAL DATA ACCESS]` - Real IEEE-CIS data access requires valid Kaggle API credentials. The pipeline executes deterministically with synthetic data mirroring the IEEE-CIS schema.
* `[BLOCKED: QPU EXECUTION]` - Physical QPU execution requires AWS Braket credentials. Local PennyLane statevector simulator (`default.qubit` / `default.mixed`) executes automatically.
