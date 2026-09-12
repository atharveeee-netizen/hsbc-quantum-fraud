# Methodology

This document outlines the core methodology for the HSBC Quantum Fraud Detection PoC.

## The Escalation Architecture
Instead of replacing classical gradient-boosted ensembles (which are exceptionally fast and accurate on standard traffic), this architecture selectively **escalates** highly uncertain transactions to a Quantum Expert.

### Classical Incumbent
A highly tuned LightGBM model operating on engineered transaction features.
- Output: Calibrated probability of fraud.

### The Router
The router filters traffic based on a fixed budget ($B$).
Inputs for routing:
1. Distance of calibrated probability from the decision boundary.
2. Ensemble disagreement (if using a bagged classical baseline).
3. Transaction Amount (cost weighting).

The top $B$% of transactions are escalated.

### The Quantum Expert
Operates strictly on the $B$% escalated traffic using a reduced feature set (8-12 dimensions selected via Mutual Information and SHAP).
- **C1 (Projected Quantum Kernel):** Non-variational approach using SVM.
- **C2 (Quantum Autoencoder):** Variational approach scored by state fidelity.

### Evaluation Protocol
- **Temporal Split:** To prevent data leakage and simulate real-world distribution shift.
- **Metrics:** AUPRC (Primary) and cost-weighted precision-recall.
- **Falsification Test:** The geometric difference $g(K_C, K_Q)$ to verify theoretical bounds before claiming advantage.
