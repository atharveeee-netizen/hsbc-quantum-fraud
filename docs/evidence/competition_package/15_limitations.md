# 15 Scientific Limitations & Scope Boundaries

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-LIMITS-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Documented methodological boundaries, sample size constraints, and hardware assumptions. |

---

## Explicit Methodological Scope
1. **Feature Dimensionality:** The tested quantum kernel operated on a 2-qubit AngleEmbedding architecture matching 2 decision-time features. We do not claim this result applies to untested 100-qubit feature spaces.
2. **Tabular Data Structural Priors:** Tabular financial records lack translation or permutation symmetries found in physics or quantum chemistry where potential quantum advantage is more readily tested.
3. **Research Nature:** All models were evaluated on public IEEE-CIS data and synthetic fixtures; no active cardholder data was processed.
