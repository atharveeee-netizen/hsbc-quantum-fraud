# Local Inference Latency Audit Report

**Status:** `[SYNTHETIC]` `[MEASURED]` `[MODELED]` `[VERIFIED]`  
**Execution Phase:** Phase 144  
**Evidence Artifact:** [`docs/evidence/latency_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/latency_audit.json)  
**Execution Environment:** Windows 10 (Build 10.0.26200), Intel64 16-Core Logical Processor, Python 3.10.11  

---

## 1. Executive Summary

Production payment rails (e.g. Visa, Mastercard, HSBC internal switch) enforce strict synchronous authorization Service Level Agreements (SLAs), requiring transaction risk scoring within **sub-50 ms** (frequently sub-25 ms at the fraud engine layer).

To rigorously evaluate real-time viability, latency was measured across individual system stages over 50–100 repeated runs.

### Key Measured Takeaways
* **Classical Fast Path Satisfies Production SLA:** The complete end-to-end classical decision pipeline (Feature Preprocessing + Calibrated LightGBM + Router) achieves a **median latency of $1.50\text{ ms}$ and p95 of $2.19\text{ ms}$**, consuming less than $5\%$ of the 50 ms budget.
* **Classical Escalation Satisfies Production SLA:** When routed to a secondary Classical RBF Expert, end-to-end latency remains **$1.59\text{ ms}$ (p95: $1.98\text{ ms}$)**.
* **Quantum Simulation Violates Real-Time SLA:** Local statevector simulation of the Projected Quantum Kernel on a single transaction against $N=50$ support points requires **$235.67\text{ ms}$ (p95: $253.24\text{ ms}$)**, exceeding the synchronous SLA by over $4.7\times$.
* **Physical QPU Dispatch Incompatible with Synchronous Payment Authorization:** Physical QPUs require cloud dispatch, circuit compilation, and queueing ($180 - 1,200\text{ seconds}$ modeled), restricting quantum evaluation strictly to offline, post-clearing investigation.

---

## 2. Component Latency Breakdown

| Pipeline Stage | Repetitions | Median Latency (ms) | p95 Latency (ms) | Min (ms) | Max (ms) | Operational SLA Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Feature Preprocessing & Scaling** | 100 | **0.06 ms** | 0.11 ms | 0.06 ms | 0.13 ms | `[COMPLIANT]` |
| **2. Frontline LightGBM Scoring** | 100 | **2.46 ms** | 4.68 ms | 2.07 ms | 6.05 ms | `[COMPLIANT]` |
| **3. Router Uncertainty Evaluation** | 100 | **0.004 ms** | 0.004 ms | 0.003 ms | 0.005 ms | `[COMPLIANT]` |
| **4. Classical RBF Expert Scoring** | 50 | **0.12 ms** | 0.17 ms | 0.12 ms | 0.31 ms | `[COMPLIANT]` |
| **5. Quantum Kernel Simulation ($N=50$)** | 10 | **235.67 ms** | 253.24 ms | 167.45 ms | 260.87 ms | `[EXCEEDS REAL-TIME SLA]` |

---

## 3. End-to-End Decision Pathways

| Architecture Pathway | Measured Median | Measured p95 | Real-Time Payment SLA Compliance |
| :--- | :---: | :---: | :--- |
| **Path A: Fast Path (Classical Only)**<br>$\text{Input} \to \text{Preprocess} \to \text{LightGBM} \to \text{Route} \to \text{Decision}$ | **1.50 ms** | **2.19 ms** | **Fully Compliant** ($<5\%$ of 50ms SLA) |
| **Path B: Classical Escalation**<br>$\text{Input} \to \text{Preprocess} \to \text{LightGBM} \to \text{Escalate} \to \text{RBF Expert}$ | **1.59 ms** | **1.98 ms** | **Fully Compliant** ($<5\%$ of 50ms SLA) |
| **Path C: Quantum Escalation (Local Sim)**<br>$\text{Input} \to \text{Preprocess} \to \text{LightGBM} \to \text{Escalate} \to \text{Quantum Kernel}$ | **237.2 ms** | **255.4 ms** | **Non-Compliant** ($470\%$ of 50ms SLA) |
| **Path D: Physical Cloud QPU Dispatch** (`[MODELED]`)<br>$\text{Input} \to \text{AWS Braket / IonQ Queue} \to \text{Execution}$ | **180,000 ms** (3 min) | **1,200,000 ms** (20 min) | **Incompatible with Online Authorization** |

---

## 4. Architectural Verdict

For live Card-Not-Present payment authorization, the system must deploy **Path A + Path B**. Quantum specialist escalation can only be evaluated asynchronously in batch anti-money laundering (AML) or T+1 offline dispute investigation workflows.
