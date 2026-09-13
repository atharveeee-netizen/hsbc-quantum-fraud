# Selective Quantum-Enhanced Fraud Detection for Digital Payment Ecosystems
## A Budget-Routed Hybrid Architecture with Matched Statistical Falsification

**Global Quantum + AI Challenge 2026 — Phase 1 Concept Proposal**  
**Track:** HSBC Enterprise Problem Statement 1: Quantum-Enhanced Credit Card Fraud Detection for Digital Payment Ecosystems  
**Team:** Akshit Agarwal (Team Lead, Classical ML & Pipeline) & Atharve Dahima (Quantum Algorithms & Hardware Evaluation)  
**Affiliation:** Rashtriya Raksha University, Gandhinagar, India  
**Public Repository:** https://github.com/atharveeee-netizen/hsbc-quantum-fraud  
**Verification Status:** 24/24 Pytest Tests Passing | Master Provenance Manifest Frozen  

---

### Executive Proposition
Digital payment switches process tens of thousands of transactions per second under a strict **50 ms design budget** and extreme class imbalance (**3.50%** native fraud prevalence in genuine transaction logs). Routing 100% of payment streams through physical quantum processors is mathematically unviable, latency-incompatible (minutes of cloud QPU queue delay), and economically catastrophic ($35.30 per transaction on IonQ Aria via AWS Braket). We propose and validate an empirical **two-tier selective escalation architecture**: frontline calibrated LightGBM autonomously clears **99.0%–99.5%** of payment volume on a **4.07 ms** fast path, while an epistemic uncertainty router (`|p - 0.5| <= tau`) concentrates ambiguous transactions into a **0.5%–1.0%** secondary evaluation budget. On 590,540 real IEEE-CIS benchmark transactions, our router achieves **42.81% fraud density** at a 0.5% budget (**12.44x enrichment** over baseline), capturing **28.1x more fraud** than transaction amount sorting alone. In a strictly matched N=200 escalated experiment comparing a Projected Quantum Kernel (PQK) against a bandwidth-tuned Classical RBF baseline, the nominal gain (Delta PR-AUC = -0.1021) yielded a 95% bootstrap confidence interval of **[-0.0383, +0.1821]** with **p = 0.246**. Because the confidence interval encompasses zero, the null hypothesis cannot be rejected. Centered Kernel Alignment (CKA = 0.5741) confirms strong metric convergence between the quantum and classical kernels. Consequently, physical QPU execution is ruled **HARDWARE NOT JUSTIFIED**, preventing over $350,000 in unjustified cloud spending per 10,000 escalated transactions. The resulting selective classical pipeline delivers immediate, deployable enterprise value (**4.89 ms** escalated latency; **$0.65** compute per 1M transactions) while defining a rigorous empirical gate for future quantum adoption.

---

# 1. Problem Framing

### 1.1 Digital Payment Realities: Severe Imbalance and Authorization Latencies
Card-not-present payment streams present two non-negotiable operational constraints. First, legitimate transactions outnumber fraudulent events by more than 27 to 1 (3.50% base prevalence in the 590,540-record IEEE-CIS benchmark). Second, card switches operate within strict authorization latency windows. Our project adopts a **50 ms design budget** from ingress to egress. Heavy monolithic models—whether deep neural networks or quantum circuits—cannot be evaluated across every transaction without introducing tail latency violations and crippling authorization throughput.

### 1.2 The Epistemic Routing Principle: Escalate, Don't Replace
Frontline gradient boosted decision trees (LightGBM) achieve strong baseline discrimination (PR-AUC 0.4040, ROC-AUC 0.8503) and sub-5 ms execution across routine transactions. However, transactions close to the classification boundary exhibit epistemic uncertainty: instances where the frontline scorer lacks decisive confidence. Instead of attempting to replace the fast classical detector with a slow, costly quantum system, the rational architecture isolates this small, ambiguous subset for targeted secondary evaluation. This keeps 99% of transactions on an autonomous fast path while focusing specialist computation strictly where decision ambiguity is highest.

### 1.3 Why Quantum Kernels Were Tested: Non-Linear Hilbert Space Projections
Quantum machine learning maps classical input vectors into high-dimensional Hilbert spaces via parameterized unitary circuits: `x -> |phi(x)>`. In theory, if payment fraud exhibits complex topological correlations that are linearly inseparable in classical Euclidean space, quantum state inner products `|<phi(x)|phi(x')>|^2` or Pauli expectation projections could yield superior decision boundaries. Rather than accepting this premise on faith, our architecture constructs an experimentally falsifiable protocol to test whether this theoretical Hilbert space advantage materializes on genuine payment transactions under strict controls.

### 1.4 Prior Literature Gaps: Protocol Failures and Artificial Rebalancing
A critical audit of published quantum fraud literature reveals widespread methodological fragility. Prior studies reporting quantum performance gains frequently evaluated toy samples (N=500), applied artificial SMOTE balancing, or created 50/50 synthetic splits on datasets whose true fraud prevalence was below 1%. Furthermore, standard random k-fold cross-validation allows future transactions to leak into training folds, artificially inflating accuracy metrics. None of these published gains survive contact with authentic class imbalance and strict chronological holdouts. Our work enforces a rigorous empirical standard: chronological temporal partitioning, fair bandwidth-tuned classical controls, and paired hypothesis testing.

---

# 2. Technical Approach

### 2.1 End-to-End System Architecture
Our system implements an asymmetric two-tier architecture that decouples high-throughput frontline clearance from secondary specialist evaluation. The workflow routes transactions according to calibrated decision uncertainty, reserving specialist compute exclusively for borderline cases.
- **Fast Path:** 99.0%–99.5% of traffic cleared autonomously by Calibrated LightGBM in 4.07 ms (median) / 4.97 ms (p95).
- **Escalation Path:** Top 0.5%–1.0% ambiguous transactions routed to secondary specialists.
- **Specialist Stage:** Matched Classical RBF, MLP, and GBM controls alongside Quantum Fidelity and Projected Quantum Kernels.
- **Decision Gate:** Paired bootstrap significance testing and hardware gate evaluation.

### 2.2 Data Ingestion & Strict Chronological Splitting
The evaluation pipeline ingests the complete IEEE-CIS Fraud Detection benchmark (**590,540 transactions**, 394 raw features, SHA-256 verified). To replicate live production conditions and prevent lookahead data leakage, partitions are established strictly by `TransactionDT`:
- **Train Set (65%):** 383,851 transactions (Days 1.0–111.3, 13,714 frauds, prevalence 3.57%).
- **Calibration Set (15%):** 88,581 transactions (Days 111.3–141.1, 2,885 frauds, prevalence 3.26%).
- **Forward Test Set (20%):** 118,108 transactions (Days 141.1–183.0, 4,064 frauds, prevalence 3.44%).

### 2.3 Train-Only Preprocessing & Calibrated Classical Detector
Preprocessing parameters are fit strictly on the training partition and applied downstream without refitting. The frontline detector employs a 100-estimator LightGBM model optimized for binary cross-entropy. Raw tree log-odds are calibrated on the holdout calibration split using non-parametric **isotonic regression**, reducing Brier score loss to **0.0250** and Expected Calibration Error (ECE) to **0.0785**.

### 2.4 Epistemic Uncertainty Router
The router filters transactions by proximity to the classification boundary: `u(x) = |p(x) - 0.5|`. Transactions with `u(x) <= tau` are escalated, where `tau` is dynamically calibrated to an explicit operational review budget `B in {0.5%, 1.0%, 2.0%, 5.0%}`.

### 2.5 Matched Specialist Stage: Quantum Kernels & Fair Classical Controls
Escalated transactions are projected onto normalized feature vectors (`TransactionAmt`, `card1`) matching 2-qubit circuit capacity. We evaluate two quantum kernel implementations via PennyLane: (1) Quantum Fidelity Kernel and (2) Projected Quantum Kernel (PQK). Every quantum model is benchmarked against three fair classical controls trained on the identical support: a bandwidth-tuned Classical RBF SVM, a 2-layer MLP (32, 16 neurons), and a shallow Classical GBM (depth=3).

---

# 3. Feasibility and Resource Requirements

### 3.1 Computational Infrastructure & Software Stack
The research codebase uses open-source libraries: LightGBM (v4.3.0), Scikit-Learn (v1.4.1), NumPy (v1.26.4), SciPy (v1.15.3), and PennyLane (v0.35.1). Frontline inference and classical controls execute on commodity x86_64 CPUs. Quantum simulations execute locally via PennyLane's `default.qubit` simulator.

### 3.2 Quantum Simulation vs. Physical QPU Viability
Evaluating an N-sample Gram matrix requires `N(N - 1) / 2` pairwise circuit evaluations. For an N=200 support set, local statevector simulation completes in **159.14 ms median latency** (217.18 ms p95). On physical cloud QPUs (IonQ Aria on AWS Braket), execution incurs queue latencies of **180 s to 1,200 s** (3 to 20 minutes) and costs **$35.30 per transaction** ($353,000 per 10k escalated transactions). Synchronous payment clearance on physical QPUs is technically infeasible.

### 3.3 Hardware Decision Gate: Pre-Registered Falsification Protocol
To protect institutional capital, physical hardware execution is gated behind a 5-criterion protocol. The gate ruled **HARDWARE NOT JUSTIFIED** across all criteria. Simulated PQK failed to reject the null hypothesis against Classical RBF (p = 0.246). Furthermore, simulated noise modeling revealed that 1% to 5% depolarizing and phase-damping noise causes an additional **-1.32% to -6.49% degradation** in PR-AUC.

---

# 4. Expected Impact and Empirical Findings

### 4.1 Master Authoritative Results Summary
- **Frontline LightGBM:** PR-AUC = 0.4040 (11.74x lift over test prevalence 0.0344), ROC-AUC = 0.8503, Brier = 0.0250. Latency: 4.07 ms median / 4.97 ms p95. Cost: $0.50 / 1M tx.
- **Router (0.5% Budget):** 42.81% fraud density (12.44x enrichment, 253 frauds / 591 tx).
- **Router (1.0% Budget):** 37.26% fraud density (10.83x enrichment, 440 frauds / 1,181 tx).
- **Classical Controls (N=200):** Tuned RBF PR-AUC = 0.6561; MLP = 0.3516; GBM = 0.3529.
- **Quantum Kernels (N=200):** Fidelity Kernel = 0.3789; Projected Quantum Kernel (PQK) = 0.5540.
- **Paired Bootstrap Test (PQK vs RBF):** Delta PR-AUC = -0.1021, 95% CI = [-0.0383, +0.1821], p = 0.246 (Bonferroni p = 0.492). Null hypothesis not rejected.
- **Geometric Alignment:** Centered Kernel Alignment (CKA) between PQK and RBF is 0.5741.
- **Economics:** $0.00 realized savings to date. Frontline compute: $0.50/1M tx; Selective classical: $0.65/1M tx; Modeled QPU: $353,000.50/1M tx.

### 4.2 Routing Ablation vs Transaction Amount
Sorting by transaction amount alone captures only 9 frauds at 0.5% budget. Uncertainty routing captures **28.1x more fraud** (253 vs 9 frauds), demonstrating that calibrated epistemic ambiguity is the true empirical driver of fraud concentration.

### 4.3 Capital Protection: The Value of Outcome B
Establishing that quantum is not currently justified provides essential risk governance, preventing over $350,000 in unjustified cloud spending per 10k transactions.

---

# 5. Validation Plan (Phase 2 PoC Sprint)

### 5.1 Chronological Holdout Protocol & Native Imbalance
Phase 2 will enforce strict rolling temporal evaluation across native class imbalance (~3.5%), scoring models on PR-AUC, calibration, and precision at fixed operational recall.

### 5.2 Fair Matched Controls & Statistical Falsification
All quantum algorithms will be matched against bandwidth-tuned RBF, MLP, and GBM controls on identical features and support sets. Advancement requires statistically significant lift (p < 0.05 after Bonferroni correction; 95% CI strictly positive) and positive net unit economics.

### 5.3 Phase 2 12-Week Roadmap
- Weeks 1–3: Enterprise data ingestion, chronological partitioning, isotonic calibration.
- Weeks 4–6: High-dimensional quantum feature maps (8–12 qubits), Matrix Product State simulability checks.
- Weeks 7–9: Scaled matched classical benchmarking and 2,000-resample bootstrap testing.
- Weeks 10–12: Hardware gate execution, economic audit, and containerized deployment package.

---

# 6. Hybrid / Cross-Domain Integration

### 6.1 Architectural Decoupling: Preserving the 50 ms Design Budget
Frontline LightGBM executes in 4.07 ms (median), clearing 99% of volume instantly without exposing payment gateways to secondary latency.

### 6.2 Operational Deployment Pathways
- **Mode A (Synchronous Classical Dual Clearance):** Escalated classical specialist executes in 4.89 ms, fully within the 50 ms budget.
- **Mode B (Asynchronous Specialist Queue):** Escalated transactions trigger 3D-Secure authentication while vectors stream asynchronously to fraud analyst queues.

---

# 7. Team Capability

### 7.1 Team Profiles & Institutional Affiliation
**Rashtriya Raksha University (National Security & Police University of India), Gandhinagar:**
- **Akshit Agarwal (Team Lead, Classical ML & System Architecture):** Production ML pipelines, extreme class imbalance, probability calibration, selective uncertainty routing, and statistical audit protocols.
- **Atharve Dahima (Quantum Algorithms & Hardware Evaluation Lead):** Quantum kernel methods (PennyLane), projected quantum kernels, NISQ noise modeling, CKA geometric alignment, and cloud QPU unit economics.

### 7.2 Why This Team Can Execute Phase 2
The team has built and audited an operational research codebase on 590,540 real transactions, passing all 24 automated tests with frozen provenance. We possess the unique discipline required to run falsification arms honestly, with zero institutional incentive to overclaim.
