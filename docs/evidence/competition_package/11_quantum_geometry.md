# 11 Quantum Metric Geometry & Kernel Alignment

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-GEOM-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Centered Kernel Alignment (CKA) and spectral matrix properties. |

---

## Geometric Alignment with Classical Hilbert Space
- **CKA(Quantum Projected, Classical RBF):** **0.5741**.
- **CKA(Quantum Fidelity, Classical RBF):** **0.9373**.
- **Effective Rank:** Classical RBF = 49, Quantum Fidelity = 9, Quantum Projected = 50.
The tested quantum kernel closely aligns with classical Gaussian RBF geometry ($>0.93$ CKA), explaining why predictive performance between them is statistically indistinguishable.
