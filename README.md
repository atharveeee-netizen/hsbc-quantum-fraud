# HSBC Challenge: Quantum-Enhanced Credit Card Fraud Detection

**Repository:** `atharveeee-netizen/hsbc-quantum-fraud`  
**Protocol Version:** `vNEXT.3`  
**Master Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]` `[NO QUANTUM ADVANTAGE DEMONSTRATED]`  
**Final Scientific Verdict:** `OUTCOME B — NO QUANTUM ADVANTAGE DEMONSTRATED, BUT USEFUL SELECTIVE CLASSICAL ARCHITECTURE VALIDATED`  

---

## Executive Summary: The Six Core Questions

### 1. What problem are we solving?
Digital payment ecosystems face severe class imbalance (only **$3.50\%$** of transactions are fraudulent in genuine benchmark logs) and high transaction volumes ($>590,000$ transactions) that strictly constrain manual review capacity ($\le 1\% - 2\%$). Payment switches require sub-50 ms synchronous authorization, making heavy monolithic models unviable.

### 2. What did we build?
A **two-tier selective escalation architecture**:
$$\text{Payment Stream} \xrightarrow{<5\text{ ms}} \text{Frontline Calibrated LightGBM} \xrightarrow{\text{Uncertainty Filter}} \begin{cases} \mathbf{99.0\%} \text{ Fast Path} \to \text{Autonomous Immediate Clearance} \\ \mathbf{1.0\%} \text{ Ambiguous Path} \to \text{Secondary Specialist Evaluation} \end{cases}$$
We implemented and tested both classical specialists (Tuned RBF, MLP, GBM) and genuine quantum specialists (Projected Quantum Kernel, Fidelity Quantum Kernel via PennyLane).

### 3. What did we test?
* **Real External Dataset:** Official IEEE-CIS Fraud Detection benchmark ($N=590,540$ transactions, $394$ columns, strict chronological split: 383,851 train, 88,581 calibration, 118,108 out-of-sample test).
* **Deterministic Synthetic Benchmark:** 10,000-row fixture for offline zero-credential regression testing.

### 4. What happened?
* **Selective Classical Routing Works Strongly:** On real test data, escalating the top **0.5%** of volume concentrates **$42.81\%$ fraud density** (**$12.44\times$ enrichment** above the $3.44\%$ base rate); a **1.0%** budget concentrates **$37.26\%$ fraud density** (**$10.83\times$ enrichment**).
* **Quantum Advantage Was Not Demonstrated:** On matched real escalated transactions, Projected Quantum Kernel (PR-AUC = 0.4043) versus Tuned Classical RBF (PR-AUC = 0.3367) yielded $\Delta\text{PR-AUC} = +0.0653$ with a **95% bootstrap confidence interval of $[-0.0383, +0.1821]$** and $p = 0.246$ (Bonferroni $p = 0.492$). Because the confidence interval spans zero and $p > 0.05$, the null hypothesis cannot be rejected.
* **Geometric Equivalence:** Centered Kernel Alignment (CKA) between the quantum kernel and Classical RBF is **0.9337**, showing the quantum feature map closely reproduces classical RBF metric geometry rather than creating an orthogonal space.

### 5. Why does that matter?
* **Financial Waste Prevention:** Physical QPU execution costs **$35.30$ per transaction** ($>\$350,000$ per 10k batch on IonQ Aria via AWS Braket) and incurs 3 to 20 minute queue latencies. Our findings prevent unjustified multi-hundred-thousand-dollar cloud QPU spending on a null result.
* **Production Architecture Delivery:** The selective classical pipeline delivers **4.07 ms** fast-path latency and **4.89 ms** escalated latency, providing a deployable, SLA-compliant solution that intercepts 440 frauds from 1% review capacity.

### 6. What is next?
Future physical QPU hardware or advanced quantum algorithm testing will occur **only if** alternative feature maps clear the formal evidence gates: statistically significant advantage ($p < 0.05$), chronological temporal stability, noise tolerance, and sub-50ms latency compatibility.

---

## Authoritative Results Table (Single Source of Truth)

All metrics trace directly to [`docs/evidence/CANONICAL_RESULTS.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/CANONICAL_RESULTS.md):

| Component | Dataset | Metric | Verified Result | Status | Evidentiary Artifact Trace |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **LightGBM Baseline** | Real (IEEE-CIS) | PR-AUC | **0.4040** (Lift: **11.74x** over $\pi=0.0344$) | `[MEASURED]` | [`real_classical_baseline.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_classical_baseline.json) |
| **LightGBM Baseline** | Real (IEEE-CIS) | ROC-AUC | **0.8503** | `[MEASURED]` | [`real_classical_baseline.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_classical_baseline.json) |
| **LightGBM Baseline** | Real (IEEE-CIS) | Brier Score Loss | **0.0250** (ECE: **0.0785**) | `[MEASURED]` | [`real_calibration_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_calibration_audit.json) |
| **Selective Router** | Real (IEEE-CIS) | 0.5% Concentration | **42.81%** (**12.44x lift**, 253 frauds / 591 tx) | `[MEASURED]` | [`real_router_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_router_audit.json) |
| **Selective Router** | Real (IEEE-CIS) | 1.0% Concentration | **37.26%** (**10.83x lift**, 440 frauds / 1,181 tx) | `[MEASURED]` | [`real_router_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_router_audit.json) |
| **Selective Router** | Real (IEEE-CIS) | 2.0% Concentration | **30.48%** (**8.86x lift**, 720 frauds / 2,362 tx) | `[MEASURED]` | [`real_router_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_router_audit.json) |
| **Classical RBF Control** | Real (IEEE-CIS) | PR-AUC (Matched $N=200$) | **0.3367** (ROC-AUC: **0.4652**) | `[MEASURED]` | [`real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json) |
| **Quantum Projected (PQK)** | Real (IEEE-CIS) | PR-AUC (Matched $N=200$) | **0.4043** (ROC-AUC: **0.5171**) | `[MEASURED]` | [`real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json) |
| **Quantum − RBF Delta** | Real (IEEE-CIS) | $\Delta\text{PR-AUC}$ (Bootstrap) | **+0.0653** ($95\%\text{ CI: } [-0.0383, +0.1821]$) | `[MEASURED]` | [`real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json) |
| **Quantum Hypothesis Test** | Real (IEEE-CIS) | $p$-value (Paired Bootstrap) | **$p = 0.246$** (Bonferroni: **$p = 0.492$**) | `[MEASURED]` | [`real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json) |
| **Quantum Geometry** | Real (IEEE-CIS) | Centered Kernel Alignment | **0.9337** (PQK vs RBF), **0.9373** (Fidelity vs RBF) | `[MEASURED]` | [`real_quantum_geometry.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_geometry.json) |
| **Quantum Noise** | Simulation | PR-AUC Degradation | **-1.32% to -6.49%** ($p=0.01\text{ to }0.05$) | `[MEASURED]` | [`real_noise_robustness.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_noise_robustness.json) |
| **QPU Economics** | Modeled (IonQ) | Cost / Escalated Tx | **$35.30** ($353,000 / 10k escalated tx) | `[MODELED]` | [`hardware_and_economics.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/hardware_and_economics.json) |
| **Realized Savings** | Real Operations | Realized Fraud Savings | **$0.00** (Zero realized claims) | `[VERIFIED]` | [`ECONOMIC_AUDIT.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/ECONOMIC_AUDIT.md) |
| **Hardware Decision Gate** | Protocol Gate | Execution Gate Status | **HARDWARE NOT JUSTIFIED** | `[VERIFIED]` | [`hardware_gate.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/hardware_gate.json) |
| **Master Scientific Verdict**| Scientific Synthesis| Final Outcome | **OUTCOME B** | `[VERIFIED]` | [`RESEARCH_VERDICT.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/RESEARCH_VERDICT.md) |

---

## Quickstart & Reproducibility

### 1. Requirements & Setup
```bash
git clone https://github.com/atharveeee-netizen/hsbc-quantum-fraud.git
cd hsbc-quantum-fraud
python -m venv .venv
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Verify Full Test Suite
```bash
pytest
```

### 3. Launch Interactive Research Demonstration
```bash
streamlit run src/dashboard/app.py
```

### 4. Execute Real Data Evaluation Pipeline (With Kaggle Credentials)
```bash
python -m src.data.real_data_pipeline
python -m src.evaluation.run_real_scientific_suite
python -m src.evaluation.run_real_latency_audit
```
