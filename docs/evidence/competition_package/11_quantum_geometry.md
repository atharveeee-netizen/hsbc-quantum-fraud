# 11 Quantum vs Classical Geometry & CKA Analysis

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-GEOM-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e9bd296` |
| **Metric Definition** | Centered Kernel Alignment (CKA) and Spectral Cosine Similarity. |

---

## Geometric & Spectral Equivalence
- **Centered Kernel Alignment (CKA):**
  - Quantum Fidelity Kernel vs Classical Gaussian RBF: **$0.9429$** ($94.3\%$ geometric alignment).
  - Projected Quantum Kernel vs Classical RBF: **$0.6335$**.
- **Spectral Cosine Similarity:**
  - Quantum Fidelity Kernel vs Classical Gaussian RBF: **$0.9906$** ($99.1\%$ spectral alignment).

**Mathematical Explanation:** The 2-qubit fidelity quantum kernel Gram matrix is geometrically and spectrally nearly identical to the classical Gaussian RBF kernel. Support Vector Classifiers trained on the quantum kernel operate as expensive classical RBF surrogates.
