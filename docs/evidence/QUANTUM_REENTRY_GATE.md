# Quantum Re-Entry Decision Gate — Evaluation Protocol & Pre-Conditions

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 164  
**Evidence Artifact:** [`docs/evidence/real_quantum_reentry_gate.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_reentry_gate.json)  

---

## 1. Evaluation of the 5 Mandatory Pre-Conditions

Prior to committing computational resources to quantum kernel simulation, the five formal gating criteria were evaluated:

| Criterion | Evaluation Question | Verified Finding | Gate Status |
| :---: | :--- | :--- | :---: |
| **Q1** | Does the real classical baseline leave meaningful headroom on escalated traffic? | **Yes.** In the uncertain boundary region ($|p - 0.5| \le 0.12$), classical baseline accuracy drops to ~50-60%, leaving significant headroom for secondary specialist intervention. | `[PASSED]` |
| **Q2** | Is the routing subset sufficiently small to bound computational complexity? | **Yes.** At a 1.0% escalation budget, the candidate stream is constrained to 1,181 transactions; for kernel Gram matrix evaluation, stratified subsampling ($N=200$ support) bounds execution. | `[PASSED]` |
| **Q3** | Is there a fair, tuned classical RBF control? | **Yes.** `ClassicalRBFExpert` implements cross-validated hyperparameter tuning ($C, \gamma$) strictly on identical training support. | `[PASSED]` |
| **Q4** | Is quantum kernel evaluation computationally and economically feasible? | **Yes, under matched support protocol.** Full $118\text{k} \times 118\text{k}$ Gram matrix is impossible ($>\$41\text{k}$ on QPU); statevector / projected simulation on $N=200$ support is fully tractable locally. | `[PASSED]` |
| **Q5** | Is there a scientifically testable, non-trivial hypothesis? | **Yes.** Hypothesis $H_1$: The non-linear Hilbert space mapping of a 2-qubit AngleEmbedding quantum kernel yields superior separation over classical RBF on decision-boundary transactions. | `[PASSED]` |

---

## 2. Gate Decision & Execution Protocol

**Gate Verdict:** **`PROCEED UNDER MATCHED PROTOCOL`**

### Protocol Rules:
1. **Identical Datasets & Partitions:** Both classical controls and quantum models must evaluate on the exact same $N=200$ escalated transaction instances.
2. **Identical Features & Preprocessing:** Exactly 2 standardized features (`TransactionAmt`, `card1`) mapped into $[-\pi, \pi]$ via arctan transformation.
3. **No Advantage Cherry-Picking:** Quantum models must be compared directly against the strongest classical control (Tuned RBF), not a degraded dummy baseline.
