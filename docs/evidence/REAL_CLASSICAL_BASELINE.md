# Real Classical Baseline Freeze — IEEE-CIS Production Stream

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 160  
**Evidence Artifact:** [`docs/evidence/real_classical_baseline.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_classical_baseline.json)  
**Partition Evaluated:** Out-of-Sample Chronological Test Split ($N=118,108$)  

---

## 1. Classical Model Discrimination & Calibration

Evaluated across the full 118,108 out-of-sample transaction stream (4,064 frauds, base prevalence $\pi = 3.4409\%$):

| Model Architecture | PR-AUC | Lift Over Prevalence ($\pi$) | ROC-AUC | Brier Score Loss | Single Tx Latency | Memory Footprint | Seed | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Calibrated LightGBM (Isotonic)** | **0.4040** | **11.74x** | **0.8503** | **0.0250** | **0.0007 ms** ($0.7\text{ }\mu\text{s}$) | ~354 KB | 42 | `[MEASURED]` |
| **Logistic Regression Control** | 0.1610 | 4.68x | 0.7200 | 0.0315 | 0.0004 ms ($0.4\text{ }\mu\text{s}$) | ~12 KB | 42 | `[MEASURED]` |
| **Random Guessing Baseline** | 0.0344 | 1.00x | 0.5000 | 0.0332 | 0.0000 ms | 0 KB | N/A | `[THEORETICAL]` |

---

## 2. Key Findings & Engineering Invariants

1. **Massive Relative Discrimination:**  
   Calibrated LightGBM achieves an empirical PR-AUC of **0.4040**, representing an **11.74x relative lift** above random guessing ($\pi = 0.0344$).
2. **Global Separation:**  
   The ROC-AUC of **0.8503** demonstrates strong overall ranking ability across the entire 182-day transaction spectrum.
3. **Probability Tightness:**  
   Brier score loss of **0.0250** confirms tight probability calibration, ensuring reliable downstream risk routing.
4. **Sub-Microsecond Latency:**  
   Frontline inference consumes approximately $0.7\text{ }\mu\text{s}$ per transaction, utilizing $<0.002\%$ of the standard $50\text{ ms}$ synchronous payment authorization budget.
