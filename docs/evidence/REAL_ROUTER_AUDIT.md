# Real Selective Router Audit — IEEE-CIS Production Stream

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 161  
**Evidence Artifact:** [`docs/evidence/real_router_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_router_audit.json)  
**Evaluated Population:** Out-of-Sample Chronological Test Stream ($N=118,108$, Total Frauds = 4,064, $\pi = 3.44\%$)  

---

## 1. Multi-Budget Router Performance Matrix

Transactions are routed to specialist secondary escalation based on decision margin uncertainty $|p - 0.5| \le \tau$:

| Escalation Budget (%) | Escalated Count ($K$) | Fraud Count Intercepted | Escalated Fraud Density | Base Fraud Prevalence | Fraud Enrichment / Lift | Fraud Population Recall | Decision Threshold ($\tau$) | Routing Latency | Operational Burden Assessment |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **0.5%** | **591** | **253** | **42.81%** | 3.44% | **12.44x** | **6.23%** | 0.0818 | 0.0007 ms | Ultra-selective tier; 253 frauds in 591 reviews |
| **1.0%** | **1,181** | **440** | **37.26%** | 3.44% | **10.83x** | **10.83%** | 0.1242 | 0.0007 ms | Primary recommended operating point |
| **2.0%** | **2,362** | **720** | **30.48%** | 3.44% | **8.86x** | **17.72%** | 0.1782 | 0.0007 ms | Balanced secondary review capacity |
| **5.0%** | **5,905** | **1,559** | **26.40%** | 3.44% | **7.67x** | **38.36%** | 0.2685 | 0.0007 ms | Captures over 38% of all fraud in 5% volume |
| **10.0%** | **11,811** | **2,343** | **19.84%** | 3.44% | **5.77x** | **57.65%** | 0.3541 | 0.0007 ms | High-coverage tier; intercepts 57.6% of fraud |

> [!NOTE]
> All reported associations describe empirical correlation between model epistemic/aleatoric uncertainty and ground-truth fraud outcomes. No causal claims are asserted.

---

## 2. Operational Takeaway

The uncertainty escalation router concentrates fraud density from an unmanageable 1 in 28 base rate up to **1 in 2.3 transactions** (42.81%) at the 0.5% budget, and **1 in 2.7 transactions** (37.26%) at the 1.0% budget. This proves the selective routing architecture operates with high efficiency on genuine payment streams.
