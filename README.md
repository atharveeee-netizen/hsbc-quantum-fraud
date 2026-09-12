# HSBC Quantum-Enhanced Credit Card Fraud Detection

**Project Codename:** `hsbc-quantum-fraud`

## 1. What is this?
A technically serious, reproducible, evidence-driven hybrid classical/quantum fraud detection PoC for the HSBC Global Quantum + AI Challenge 2026.

## 2. What problem does it solve?
Credit card fraud is highly asymmetric in cost ($4.41 per $1 of fraud). Current classical models suffer in the uncertain band near decision boundaries. This project tests if escalating that specific, highly-uncertain traffic to a quantum expert improves the Precision-Recall tradeoff within a realistic authorization latency envelope (100-300ms).

## 3. Why quantum?
Near-term quantum algorithms (like projected quantum kernels) are conjectured to have superior generalization from sparse labelled examples, which is exactly the profile of fraud detection near the decision boundary. Rather than replacing the classical stack, we route a subset of traffic (budget $B$) to the quantum expert.

## 4. What is actually implemented?
*(To be updated dynamically by the agent loop)*
- [ ] Data Pipeline & Temporal Validation
- [ ] Classical Incumbent (LightGBM)
- [ ] Escalation Router
- [ ] Quantum Expert (Projected Kernel / Fidelity QAE)
- [ ] Classical Controls (Tuned RBF, Classical Expert, Random Router)

## 5. How is it evaluated?
- Primary metrics: AUPRC, Precision at fixed Recall.
- Evaluation split: Strict temporal split to emulate real-world distribution shift.
- Hardware: Simulator execution first, Braket hardware for final verification.
- Statistical: Bootstrapped confidence intervals against classical controls under the exact same escalation budget.

## 6. How do I reproduce it?
*(To be updated once execution framework is initialized)*

## 7. What results have actually been obtained?
*(To be populated during Phase 8)*

## 8. What remains planned/blocked?
*(To be populated continuously by the Claim Auditor)*
