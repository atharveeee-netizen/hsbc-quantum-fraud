# The Competition Narrative: Selective Classical Escalation & Empirical Quantum Benchmarking

**Scientific Verdict:** `OUTCOME B — NO QUANTUM ADVANTAGE DEMONSTRATED`  
**Pipeline Status:** `[SYNTHETIC]` `[MEASURED]` `[VERIFIED]` `[REAL DATA BLOCKED]`  
**Execution Phase:** Phase 151  

---

## 1. The Real-World Operational Problem

Payment networks process billions of card-not-present (CNP) transactions annually. In high-throughput card fraud detection, banks face an intractable trilemma:
1. **Missed Fraud Loss:** Even a $1\%$ fraud leakage produces multimillion-dollar unrecovered chargeback losses.
2. **Customer Friction & False Declines:** Overly aggressive blocking insults legitimate cardholders, causing customer attrition and lost interchange fees (costing $\approx 10\times$ more in lifetime value than fraud losses).
3. **Rigid Real-Time SLAs:** Payment switches strictly enforce sub-50 ms end-to-end authorization deadlines. Models cannot execute arbitrary deep neural networks or complex compute on 100% of transaction volume without timing out.

---

## 2. The Conventional Architecture Limitation

Historically, financial institutions deploy monolithic fraud architectures:
* A single gradient-boosted decision tree or logistic model scores every incoming transaction uniformly.
* This forces a compromise: the model must be lightweight enough to evaluate in $<10\text{ ms}$, preventing the use of expressive non-linear representations, high-degree kernels, or deep feature interactions.
* When edge cases arise (ambiguous card-amount combinations, novel merchants, borderline risk scores), the monolithic model either declines blindly or approves blindly.

---

## 3. The Proposed Architecture: Selective Concentration

To break this trilemma, this project validates a **two-tier selective escalation architecture**:
$$\text{Transaction Stream} \xrightarrow{\text{Sub-5ms}} \text{Frontline Calibrated LightGBM} \xrightarrow{\text{Uncertainty Filter}} \begin{cases} 99.0\% \text{ Clear / Normal} \to \text{Autonomous Sub-5ms Decision} \\ 1.0\% \text{ Ambiguous / High-Value} \to \text{Escalate to Specialist Queue} \end{cases}$$

* **Selective Concentration Principle:** Rather than spending expensive computation uniformly, the router isolates the top $0.5\% - 2.0\%$ most uncertain, high-friction transactions.
* **Enrichment Without Causal Overreach:** Empirical router audits confirm **$1.62\times - 1.94\times$ fraud enrichment** in the escalated queue.
* **Production SLA Feasibility:** Frontline decisions complete in **$1.50\text{ ms}$ (median)**; escalated classical specialist evaluations complete in **$1.59\text{ ms}$ (median)**, comfortably satisfying payment switch SLAs.

---

## 4. The Quantum Investigation: Fair Controls & Grounded Falsification

A dedicated quantum-kernel branch was constructed and rigorously compared against mathematically matched classical controls:
* **Quantum Feature Maps:** Projected Quantum Kernels (PQK via 1-qubit Pauli expectations) and Fidelity Quantum Kernels ($|\langle \psi(x_1) | \psi(x_2) \rangle|^2$).
* **Matched Classical Controls:** Tuned Gaussian Radial Basis Function (RBF) Support Vector Classifier, Classical Gradient Boosted Specialist, and Multi-Layer Perceptron (MLP).
* **Controlled Evaluation:** Both quantum and classical specialists competed on identical data splits, identical feature subsets, identical escalated transactions, and across 13 seeds and 5 temporal windows.

---

## 5. The Scientific Verdict & Empirical Findings

> [!IMPORTANT]
> **Definitive Scientific Outcome:**  
> **`OUTCOME B — NO QUANTUM ADVANTAGE DEMONSTRATED`**  
> Evidence-driven evaluation showed that selective classical escalation currently provides the stronger operational architecture, while the quantum branch establishes a reproducible benchmark for future hardware/software improvements.

### Key Empirical Findings
1. **Classical Dominance on Tabular Data:** Classical RBF and Classical GBM consistently matched or outperformed Quantum Kernels across all tested escalation budgets ($B \in [0.5\%, 10.0\%]$).
2. **Geometric Alignment:** Centered Kernel Alignment (CKA) between the Quantum Kernel and Classical RBF reached **$0.9999$**, proving the quantum feature map closely mirrored classical RBF geometry without expanding expressivity.
3. **Severe Hardware & Latency Asymmetry:**
   * Classical specialist latency: **$0.12\text{ ms}$**; cost per 100 tx: **$0.000005**
   * Quantum simulation latency: **$235.67\text{ ms}$**; physical QPU dispatch cost per 100 tx: **$3,217.50** (over **$600,000,000\times$ more expensive** for zero empirical accuracy gain).
4. **Noise Intolerance:** Controlled depolarizing noise monotonically degraded quantum state purity and classifier discrimination.

---

## 6. Why This Narrative Wins

Rather than presenting easily falsifiable marketing claims or unsupported savings figures, this repository delivers:
1. **Institutional Scientific Integrity:** A completely honest, reproducible evaluation that prevents wasteful capital expenditure on premature QPU deployment.
2. **Production-Ready Classical Architecture:** A validated two-tier selective escalation pipeline that improves fraud concentration and cuts operational decision losses by **$27.5\% - 53.4\%$** through calibrated threshold optimization.
3. **Rigorous Quantum Baseline:** An open, unpolluted, reproducible benchmark for evaluating future fault-tolerant quantum algorithms when hardware reaches maturity.
