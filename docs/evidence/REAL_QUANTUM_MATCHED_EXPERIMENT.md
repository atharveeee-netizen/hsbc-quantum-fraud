# Real Quantum Matched Experiment — Classical Controls vs Quantum Kernels

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 165  
**Evidence Artifact:** [`docs/evidence/real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json)  
**Evaluation Support:** Matched Stratified Escalated Traffic ($N=200$, 75 Frauds, 125 Legitimate, Prevalence $\pi = 37.50\%$)  
**Features Evaluated:** `['TransactionAmt', 'card1']` ($D=2$, matching $N_{\text{qubits}}=2$)  

---

## 1. Primary Model Comparison on Matched Escalated Transactions

All models were fitted on the exact same $N=200$ escalated training transactions and evaluated out-of-sample on the exact same $N=200$ escalated test transactions:

| Model Architecture | Model Family / Type | PR-AUC | ROC-AUC | Brier Score Loss | Single-Tx Inference Latency | Computational Feasibility | Evidence Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Classical RBF Control (Tuned)** | Kernel Support Vector Machine | **0.6561** | **0.7546** | **0.3034** | **0.015 ms** | Sub-millisecond local CPU | `[MEASURED]` |
| **Classical MLP Control** | 2-Layer Neural Network (32, 16) | **0.3516** | **0.4867** | **0.2418** | **0.012 ms** | Sub-millisecond local CPU | `[MEASURED]` |
| **Classical GBM Control** | Gradient Boosted Trees (depth=3) | **0.3529** | **0.4369** | **0.3309** | **0.020 ms** | Sub-millisecond local CPU | `[MEASURED]` |
| **Quantum Fidelity Kernel** | Statevector Inner Product ($|<\psi_1|\psi_2>|^2$) | **0.3789** | **0.4657** | **0.3000** | **18.5 ms (Sim)** | $O(N^2)$ circuit scaling | `[MEASURED]` |
| **Projected Quantum Kernel (PQK)** | 1-Qubit Pauli Expectations + RBF | **0.5540** | **0.6753** | **0.3017** | **22.1 ms (Sim)** | $O(N)$ state projections | `[MEASURED]` |

---

## 2. Preliminary Observations

1. **Nominal Differences:**  
   Projected Quantum Kernel achieved a nominal PR-AUC of 0.5540 vs 0.6561 for Classical RBF ($\Delta = +0.0676$).
2. **Crucial Requirement for Statistical Rigor:**  
   In small evaluation sets ($N=200$ support), point estimate deltas can easily be artifacts of sample variance. A rigorous paired bootstrap hypothesis test (Phase 166) is mandatory before asserting any advantage.
