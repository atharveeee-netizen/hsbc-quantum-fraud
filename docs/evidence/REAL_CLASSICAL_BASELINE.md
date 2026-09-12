# Real-Data Classical Baseline Performance Report

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 129  
**Evidence Artifact:** [`docs/evidence/real_classical_baseline.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_classical_baseline.json)  
**Trained Model:** Calibrated LightGBM (Isotonic Regression on Out-of-Sample Chronological Validation)  
**Evaluation Set:** $N=118,108$ transactions (Chronological Test Split)  

---

## 1. Primary & Secondary Baseline Metrics

| Metric Dimension | Measured Empirical Value | Baseline Reference | Relative Lift / Context |
| :--- | :---: | :---: | :---: |
| **Empirical Fraud Prevalence** | **3.4418%** ($4,065\text{ frauds}$) | Random baseline | $\pi = 0.0344$ |
| **Precision-Recall AUC (PR-AUC)** | **0.4040** | 0.0344 (Random) | **$11.74\times\text{ Lift Over Prevalence}$** |
| **ROC-AUC** | **0.8503** | 0.5000 (Random) | Exceptional global discrimination |
| **Brier Score Loss** | **0.0250** | — | Highly calibrated risk scoring |
| **Single-Transaction Latency** | **0.0007 ms** ($0.7\text{ }\mu\text{s}$) | $<50.0\text{ ms}$ (SLA) | Consumes $<0.002\%$ of latency SLA |

---

## 2. Selective Escalation & Enrichment on Real Traffic (Phase 131)

When the selective uncertainty router is applied to the genuine $118,108$-transaction test stream:

| Escalation Budget (%) | Escalated Volume | Fraud Count | Escalated Fraud Prevalence | Population Fraud Prevalence | Fraud Enrichment Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0.5%** | **590 tx** | 253 | **42.88%** | 3.44% | **$12.46\times$ Enrichment** |
| **1.0%** | **1,181 tx** | 440 | **37.26%** | 3.44% | **$10.83\times$ Enrichment** |
| **2.0%** | **2,362 tx** | 720 | **30.48%** | 3.44% | **$8.86\times$ Enrichment** |
| **5.0%** | **5,905 tx** | 1,559 | **26.40%** | 3.44% | **$7.67\times$ Enrichment** |
| **10.0%** | **11,810 tx** | 2,343 | **19.84%** | 3.44% | **$5.77\times$ Enrichment** |

### Key Operational Finding
At a $1.0\%$ escalation budget, the router isolates **$1,181$ transactions**, containing **$440$ actual frauds** ($37.26\%$ fraud density). This concentrates over $10.8\%$ of all fraud in the entire test set into just $1.0\%$ of operational review volume, confirming the high practical value of selective escalation on genuine financial data.
