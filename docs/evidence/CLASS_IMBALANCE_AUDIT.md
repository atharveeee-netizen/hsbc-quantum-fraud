# Real-Data Class Imbalance & Prevalence Audit

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 157  
**Evidence Artifact:** [`docs/evidence/real_class_imbalance_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_class_imbalance_audit.json)  

---

## 1. Canonical Real Test Data Imbalance Profile

On the chronological out-of-sample test partition ($N=118,108$ transactions spanning Days 141.1 to 183.0):

| Dimension | Real Test Partition Value | Evidentiary Definition | Status |
| :--- | :---: | :--- | :---: |
| **Total Test Transactions ($N$)** | **118,108** | Full out-of-sample chronological test stream | `[MEASURED]` |
| **Fraudulent Transactions ($N_{\text{fraud}}$)** | **4,064** | Ground-truth positive chargeback labels (`isFraud == 1`) | `[MEASURED]` |
| **Legitimate Transactions ($N_{\text{legit}}$)** | **114,044** | Ground-truth negative labels (`isFraud == 0`) | `[MEASURED]` |
| **Empirical Test Fraud Prevalence ($\pi_{\text{test}}$)** | **3.4409%** | Base rate $N_{\text{fraud}} / N$ (1 fraud per 28.1 legit tx) | `[MEASURED]` |
| **Random Guessing PR-AUC Baseline** | **0.0344** | Theoretical uninformative baseline ($\text{PR-AUC} = \pi$) | `[MEASURED]` |
| **Calibrated LightGBM PR-AUC** | **0.4040** | Empirical out-of-sample PR-AUC | `[MEASURED]` |
| **Baseline PR-AUC Lift Factor** | **11.74x** | Model PR-AUC divided by base prevalence ($\text{PR-AUC} / \pi$) | `[MEASURED]` |
| **Calibrated LightGBM ROC-AUC** | **0.8503** | Pairwise ranking discrimination across entire spectrum | `[MEASURED]` |
| **Brier Score Loss** | **0.0250** | Mean squared probability calibration error | `[MEASURED]` |

---

## 2. Rigorous Distinction: PR-AUC vs Concentration vs Recall

To avoid conflation across evaluation domains, the three primary metrics are strictly distinguished:

1. **Precision-Recall AUC (PR-AUC):**  
   Measures the area under the continuous precision-recall curve across all possible decision thresholds $[0, 1]$. In highly imbalanced contexts ($\pi = 3.44\%$), an uninformative model scores $0.0344$. A score of $0.4040$ represents an **$11.74\times$ lift**, confirming high ranking power.
2. **Fraud Concentration (Precision at Operational Budget $K$):**  
   The empirical proportion of escalated transactions that are fraudulent ($\text{Escalated Frauds} / \text{Escalated Volume}$). At a $0.5\%$ budget (590 transactions), the router achieves **$42.88\%$ fraud concentration** (**$12.46\times$ enrichment** above the $3.44\%$ base rate).
3. **Fraud Capture (Recall at Operational Budget $K$):**  
   The cumulative percentage of total population fraud captured within the escalated budget ($\text{Escalated Frauds} / 4,064$). At a $0.5\%$ budget, 253 of 4,064 frauds are captured (**$6.23\%$ recall**); at a $5.0\%$ budget, 1,559 frauds are captured (**$38.36\%$ recall**).

---

## 3. Disparity Between Synthetic Benchmark and Genuine IEEE-CIS

| Evaluation Vector | Synthetic Benchmark Fixture | Genuine IEEE-CIS Production Stream | Implication |
| :--- | :---: | :---: | :--- |
| **Evaluation Set Size** | 2,001 | **118,108** | $59\times$ larger sample size on real data |
| **Fraud Prevalence ($\pi$)** | 30.93% | **3.44%** | Real data is $9.0\times$ more severely imbalanced |
| **Random Baseline PR-AUC** | 0.3093 | **0.0344** | Random baseline drops by $89\%$ on real data |
| **Calibrated LightGBM PR-AUC** | 0.3987 | **0.4040** | Nominal scores are similar, but relative lift differs |
| **Prevalence-Normalized Lift** | $1.29\times$ | **$11.74\times$** | **Real data demonstrates $9.1\times$ greater relative discrimination lift** |
| **Calibrated LightGBM ROC-AUC** | 0.5996 | **0.8503** | Real data demonstrates far stronger global separation |
| **Calibrated Brier Score** | 0.2065 | **0.0250** | Real data achieves order-of-magnitude tighter calibration |

> [!WARNING]
> Synthetic metrics and real-data metrics must never be mixed or averaged together.
