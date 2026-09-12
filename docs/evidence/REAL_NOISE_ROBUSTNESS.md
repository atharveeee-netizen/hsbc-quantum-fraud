# Simulated Noise Robustness — Depolarizing & Readout Sensitivity

**Status:** `[SIMULATED NOISE]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 169  
**Evidence Artifact:** [`docs/evidence/real_noise_robustness.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_noise_robustness.json)  
**Noise Model:** Simulated Depolarizing Channel + Readout Perturbation on Quantum Kernel Gram Matrix  

---

## 1. Controlled Noise Degradation Matrix

Evaluated under increasing physical error rates modeled on superconducting / trapped-ion hardware characteristics:

| Depolarizing Error Rate ($p$) | Frobenius Kernel Distortion | Degraded Quantum PR-AUC | Relative Performance Drop | Modeled Hardware Regime |
| :---: | :---: | :---: | :---: | :--- |
| **$p = 0.000$** (Ideal) | **0.00%** | **0.3789** | 0.00% | Ideal statevector simulator baseline |
| **$p = 0.001$** ($0.1\%$) | **0.17%** | **0.3784** | -0.13% | High-fidelity trapped-ion gate regime (e.g. Quantinuum) |
| **$p = 0.010$** ($1.0\%$) | **1.66%** | **0.3739** | -1.32% | Standard NISQ superconducting gate error (e.g. IBM Eagle) |
| **$p = 0.020$** ($2.0\%$) | **3.29%** | **0.3689** | -2.64% | Typical unmitigated NISQ two-qubit error rate |
| **$p = 0.050$** ($5.0\%$) | **8.12%** | **0.3543** | -6.49% | Noisy intermediate-scale edge environment |

---

## 2. Distinction Between Simulated and Hardware Noise

> [!CAUTION]
> **Provenance Classification Invariant:**  
> All noise evaluations in this report are classified strictly as `[SIMULATED NOISE]`. No physical quantum processor execution was conducted. Numerical values represent synthetic depolarizing channels applied to simulated Gram matrices and must not be cited as measured hardware telemetry.

### Engineering Finding:
Physical quantum noise degrades kernel matrix fidelity monotonically. In no scenario did stochastic quantum noise provide beneficial regularization or elevate performance above classical controls.
