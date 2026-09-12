# Real Router Ablation & Routing Mechanism Analysis

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 162  
**Evidence Artifact:** [`docs/evidence/real_router_ablation.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_router_ablation.json)  
**Evaluated Population:** Out-of-Sample Chronological Test Stream ($N=118,108$, Total Frauds = 4,064)  

---

## 1. Routing Strategy Comparative Ablation

To determine the empirical mechanism driving routing enrichment, we evaluated four distinct escalation policies across all operational budgets:

| Budget (%) | Escalated Count ($K$) | Random Policy (Fraud N / Density) | Amount-Only Policy (Fraud N / Density) | Uncertainty-Only Policy (Fraud N / Density) | Amount + Uncertainty Policy (Fraud N / Density) | Primary Strategy Advantage |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.5%** | **591** | 21 frauds (3.55%) | 9 frauds (1.52%) | **253 frauds (42.81%)** | 15 frauds (2.54%) | **28.1x more frauds** than Amount-Only |
| **1.0%** | **1,181** | 42 frauds (3.56%) | 34 frauds (2.88%) | **440 frauds (37.26%)** | 47 frauds (3.98%) | **12.9x more frauds** than Amount-Only |
| **2.0%** | **2,362** | 81 frauds (3.43%) | 152 frauds (6.44%) | **720 frauds (30.48%)** | 114 frauds (4.83%) | **4.7x more frauds** than Amount-Only |
| **5.0%** | **5,905** | 202 frauds (3.42%) | 312 frauds (5.28%) | **1,559 frauds (26.40%)** | 277 frauds (4.69%) | **5.0x more frauds** than Amount-Only |
| **10.0%** | **11,811** | 385 frauds (3.26%) | 570 frauds (4.83%) | **2,343 frauds (19.84%)** | 632 frauds (5.35%) | **4.1x more frauds** than Amount-Only |

---

## 2. Scientific Findings

1. **Uncertainty is the Dominant Factor:**  
   Model uncertainty $|p - 0.5|$ overwhelmingly drives escalation benefit. At the 0.5% budget, uncertainty captures **253 frauds**, compared to only **9 frauds** captured by sorting purely by transaction dollar value.
2. **Amount-Only Policy Fails at Ultra-Low Budgets:**  
   Sorting strictly by transaction amount performs worse than uniform random sampling at small budgets (1.52% vs 3.55% at 0.5% budget). Real fraudsters in IEEE-CIS frequently execute card-testing or micro-transactions ($1–$50) rather than high-value purchases.
3. **No Redundancy with Transaction Amount:**  
   The router is genuinely exploiting calibrated probability uncertainty rather than rediscovering transaction magnitude.
4. **Epistemic vs Causal Statement:**  
   This routing benefit reflects empirical correlation between model boundary ambiguity and fraud prevalence; no causal claims regarding transaction amount or fraud generation are made.
