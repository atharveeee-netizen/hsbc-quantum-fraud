# Adversarial Synthetic Stress Testing Report

**Status:** `[SYNTHETIC STRESS TEST]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 141  
**Evidence Artifact:** [`docs/evidence/adversarial_stress_test.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/adversarial_stress_test.json)  
**Evaluated Sample Size:** $N=2,001$ test transactions  

> [!WARNING]
> **Scientific Integrity Notice:**  
> These experiments simulate controlled distributional shifts on the synthetic pipeline. They do **NOT** represent real-world external validation on IEEE-CIS production data (which remains legitimately blocked pending Kaggle credentials). All metrics below are strictly designated as **`[SYNTHETIC STRESS TEST]`**.

---

## 1. Executive Summary

To systematically evaluate pipeline robustness prior to real-data unblocking, the system was subjected to eight severe adversarial distribution shifts:
1. **Class Prevalence Decay:** $31.0\%$ down to $1.0\%$ (simulating extreme real-world fraud imbalance).
2. **Transaction Amount Scale Shift:** Multipliers from $0.5\times$ to $5.0\times$ (simulating inflationary shocks / high-value spikes).
3. **Feature Gaussian Noise:** Perturbation standard deviation $\sigma \in [0.0, 0.30]$.
4. **Missingness Injection:** Zero-imputation masking on `card1` from $0\%$ to $30\%$.
5. **Temporal Sliding Block Drift:** 3 sequential chronological evaluation windows.
6. **Categorical Cardinality Shifts:** Out-of-vocabulary card numbers from $0\%$ to $50\%$.
7. **Calibration Stability & Brier Score Drift:** Probabilistic calibration under stress.
8. **Router Budget Enrichment Stability:** Uncertainty-driven escalation across budgets from $0.5\%$ to $10.0\%$.

### Canonical Stress Test Findings
* **No Quantum Advantage Under Stress:** Across all 8 perturbation axes, the Projected Quantum Kernel (PQK) failed to demonstrate a statistically significant or consistent performance advantage over the Classical RBF or Classical GBM controls ($\Delta \text{PR-AUC}_{\text{PQK} - \text{RBF}} \in [-0.056, +0.017]$).
* **Prevalence-Normalized Metrics:** At $1.0\%$ fraud prevalence, raw PR-AUC collapses from $0.335$ to $0.008$, illustrating why synthetic AUPRC cannot be compared directly to real-world imbalanced datasets.
* **Router Robustness:** The selective router achieves consistent enrichment across all budgets ($1.94\times$ enrichment at $0.5\%$ budget; $1.62\times$ at $1.0\%$), verifying selective concentration.

---

## 2. Quantitative Results by Stress Dimension

### 2.1 Shift 1: Class Prevalence Shift (31.0% to 1.0%)

| Target Prev | Actual Prev | Baseline PR-AUC | Classical RBF | Classical GBM | Quantum PQK | $\Delta(\text{PQK} - \text{RBF})$ | Baseline Lift |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **31.0%** | 30.93% | 0.3349 | 0.2797 | 0.2552 | 0.2457 | -0.0340 | 1.08x |
| **15.0%** | 14.95% | 0.1503 | 0.1291 | 0.1137 | 0.0918 | -0.0373 | 1.01x |
| **5.0%** | 4.95% | 0.0667 | 0.0406 | 0.0453 | 0.0556 | +0.0150 | 1.35x |
| **3.5%** | 3.49% | 0.0388 | 0.0459 | 0.0313 | 0.0553 | +0.0094 | 1.11x |
| **1.0%** | 0.93% | 0.0080 | 0.0108 | 0.0091 | 0.0187 | +0.0079 | 0.86x |

### 2.2 Shift 2: Transaction Amount Multiplier (0.5x to 5.0x)

| Multiplier | Mean Amount ($) | Baseline PR-AUC | Classical RBF | Classical GBM | Quantum PQK | $\Delta(\text{PQK} - \text{RBF})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.5x** | $25.22 | 0.3126 | 0.3252 | 0.2915 | 0.2935 | -0.0317 |
| **1.0x** | $50.44 | 0.3349 | 0.2797 | 0.2552 | 0.2457 | -0.0340 |
| **2.0x** | $100.88 | 0.3172 | 0.2960 | 0.2475 | 0.3097 | +0.0137 |
| **5.0x** | $252.21 | 0.3021 | 0.2336 | 0.2365 | 0.2506 | +0.0169 |

### 2.3 Shift 3: Feature Gaussian Noise Injection

| Noise Scale ($\sigma$) | Classical RBF PR-AUC | Classical GBM PR-AUC | Quantum PQK PR-AUC | $\Delta(\text{PQK} - \text{RBF})$ |
| :---: | :---: | :---: | :---: | :---: |
| **$\sigma = 0.00$** | 0.2797 | 0.2552 | 0.2457 | -0.0340 |
| **$\sigma = 0.05$** | 0.2782 | 0.2533 | 0.2490 | -0.0293 |
| **$\sigma = 0.15$** | 0.2807 | 0.2525 | 0.2693 | -0.0113 |
| **$\sigma = 0.30$** | 0.2741 | 0.2722 | 0.2467 | -0.0273 |

### 2.4 Shift 4: Feature Missingness (Card1 Zero-Imputation)

| Missing Rate | Classical RBF PR-AUC | Classical GBM PR-AUC | Quantum PQK PR-AUC | $\Delta(\text{PQK} - \text{RBF})$ |
| :---: | :---: | :---: | :---: | :---: |
| **0%** | 0.2797 | 0.2552 | 0.2457 | -0.0340 |
| **5%** | 0.2794 | 0.2545 | 0.2466 | -0.0328 |
| **15%** | 0.2718 | 0.2463 | 0.2803 | +0.0085 |
| **30%** | 0.2891 | 0.2663 | 0.2704 | -0.0187 |

### 2.5 Shift 5: Temporal Sliding Block Drift

| Chronological Block | Sample Count | Observed Prevalence | Baseline PR-AUC | Classical RBF | Quantum PQK | $\Delta(\text{PQK} - \text{RBF})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Block 1** | 250 | 28.0% | 0.3284 | 0.2891 | 0.2329 | -0.0562 |
| **Block 2** | 250 | 34.0% | 0.4898 | 0.4108 | 0.3638 | -0.0470 |
| **Block 3** | 250 | 32.8% | 0.4459 | 0.3193 | 0.3252 | +0.0059 |

### 2.6 Shift 6: Card1 Out-of-Vocabulary Cardinality Shift

| OOV Rate | Classical RBF PR-AUC | Classical GBM PR-AUC | Quantum PQK PR-AUC | $\Delta(\text{PQK} - \text{RBF})$ |
| :---: | :---: | :---: | :---: | :---: |
| **0%** | 0.2797 | 0.2552 | 0.2457 | -0.0340 |
| **10%** | 0.2768 | 0.2534 | 0.2671 | -0.0096 |
| **25%** | 0.2813 | 0.2628 | 0.2704 | -0.0109 |
| **50%** | 0.2844 | 0.2604 | 0.2832 | -0.0012 |

### 2.7 Shift 7: Calibration & Brier Score Under Stress

* **Frontline Calibrated LightGBM Brier Score:** **0.2065** (Strongest overall calibration).
* **Classical RBF Expert Brier Score:** 0.3898.
* **Quantum PQK Expert Brier Score:** 0.3582.

### 2.8 Shift 8: Router Budget Enrichment Stability

| Budget (%) | Escalated Volume | Escalated Fraud Rate | Baseline Fraud Rate | Enrichment Ratio |
| :---: | :---: | :---: | :---: | :---: |
| **0.5%** | 10 | 60.0% | 30.93% | **1.94x** |
| **1.0%** | 20 | 50.0% | 30.93% | **1.62x** |
| **2.0%** | 40 | 47.5% | 30.93% | **1.54x** |
| **5.0%** | 100 | 44.0% | 30.93% | **1.42x** |
| **10.0%** | 200 | 44.0% | 30.93% | **1.42x** |

---

## 3. Scientific Conclusion

1. **Robustness of Classical Components:** Frontline LightGBM and Classical RBF exhibit strong resilience to extreme feature noise, missingness, and cardinality shifts.
2. **Selective Enrichment Validated:** The router concentrates high-risk, ambiguous traffic into specialist queues reliably ($1.42\times - 1.94\times$ fraud concentration) without requiring causal assumptions.
3. **Firm Quantum Invariance:** Stressing the synthetic distributions across 8 dimensions confirms the core scientific verdict: **no quantum advantage demonstrated**.
