# 15 Scientific Limitations & Threats to Validity

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-LIMITATIONS-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c0968b6` |
| **Metric Definition** | Identified threats to internal and external validity. |

---

## Disclosed Research Limitations
1. **Real Data Access:** `[BLOCKED: REAL DATA]`. Experiments conducted on a deterministic synthetic benchmark mirroring IEEE-CIS features. Full validation on raw IEEE-CIS data remains pending legitimate credentials.
2. **Qubit Dimensionality:** Quantum feature maps evaluated at 2 qubits due to $O(N^2)$ circuit complexity in pairwise kernel matrices. Higher qubit dimensions may exhibit different expressivity but will suffer from severe barren plateau and simulation scaling limits.
3. **Associative Routing:** Selective routing enrichment reflects the underlying distribution of transaction amounts and uncertainty margins; it does not constitute a causal intervention on fraud behavior.
