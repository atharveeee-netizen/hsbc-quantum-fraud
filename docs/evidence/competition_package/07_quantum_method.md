# 07 Quantum Kernel Formulation

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-QUANTUM-METH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `9857a2a` |
| **Metric Definition** | Gram matrix symmetry, positive semi-definiteness, and expressivity. |

---

## Quantum Feature Encoding & Kernels
- **Qubit Register:** 2-qubit circuit with angle encoding ($\{R_x, R_y, R_z\}$ rotations).
- **Entanglement:** Parameterized CNOT / CZ entangling layers.
- **Kernel Types Evaluated:**
  1. **Fidelity Kernel:** $K(x, x') = |\langle \psi(x) | \psi(x') \rangle|^2$ via transition probability / Swap test.
  2. **Projected Quantum Kernel:** Projects quantum states onto 1-particle reduced density matrices (1-RDM) followed by classical RBF evaluation in Hilbert space.
- **Simulator Backend:** PennyLane statevector simulator (`default.qubit`).
