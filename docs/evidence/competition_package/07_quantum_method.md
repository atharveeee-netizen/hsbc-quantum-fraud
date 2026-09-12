# 07 Quantum Kernel Formulation

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-QUANTUM-METH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Statevector fidelity and projected quantum kernel mathematical specifications. |

---

## Quantum Specialist Implementations
1. **Fidelity Quantum Kernel:** Evaluates exact statevector inner products $K(x_1, x_2) = |\langle \psi(x_1) | \psi(x_2) \rangle|^2$ using PennyLane `AngleEmbedding` and `BasicEntanglerLayers`.
2. **Projected Quantum Kernel (Huang et al., 2021):** Extracts 1-qubit Pauli expectation observables $\langle X_i \rangle, \langle Y_i \rangle, \langle Z_i \rangle$ to construct physical projections in $[-1, 1]^{3n}$, followed by classical Gaussian kernel classification.
