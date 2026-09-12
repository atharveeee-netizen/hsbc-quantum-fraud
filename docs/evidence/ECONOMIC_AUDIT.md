# Economic Audit & Unit Economics Analysis — Three Architecture Scenarios

**Status:** `[REAL DATA]` `[MEASURED]` `[MODELED]` `[ASSUMED]` `[VERIFIED]`  
**Execution Phase:** Phase 171  
**Evidence Artifact:** [`docs/evidence/hardware_and_economics.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/hardware_and_economics.json)  

---

## 1. Accounting Provenance Taxonomy

To ensure institutional credibility and eliminate any risk of overstated claims, all financial metrics are categorized strictly according to empirical provenance:

| Category | Definition | Repository Scope in this Audit |
| :--- | :--- | :--- |
| **`[MEASURED]`** | Directly observed from computational execution and real file statistics | Local compute runtime, CPU/RAM utilization, IEEE-CIS dataset volume (590,540 transactions), local inference latency ($0.0007\text{ ms}$). |
| **`[MODELED]`** | Calculated via mathematically defined operational formulas and published cloud provider rate cards | IonQ/AWS Braket quantum circuit execution costs, batch scaling curves, modeled fraud loss reduction across budgets. |
| **`[ASSUMED]`** | Industry standard business parameters provided as operational hypotheses | Cost of missed fraud ($180/transaction), false decline friction cost ($15/transaction), analyst review cost ($45/analyst hour). |

---

## 2. Realized Savings Declaration

> [!IMPORTANT]
> **Realized Expenditure Savings to Date: $0.00**  
> While the system has been thoroughly evaluated on genuine IEEE-CIS real-world payment data ($N=590,540$), this repository represents a scientific research benchmark, not a live production deployment hooked into an active merchant acquiring switch.  
> **No realized monetary savings have been claimed or accrued ($0.00).** All financial figures represent mathematically modeled unit economics under explicit parameter assumptions. Claims of "€1.2M savings" are prohibited and rejected.

---

## 3. Comparative Architecture Scenarios (Per 1 Million Transactions)

Assuming an enterprise volume of 1,000,000 transactions at IEEE-CIS empirical base fraud prevalence ($\pi = 3.44\%$, i.e. 34,400 fraudulent transactions):

| Operational Dimension | Scenario 1: Classical-Only (Frontline LightGBM) | Scenario 2: Classical + Selective Specialist (LightGBM + 1% RBF) | Scenario 3: Quantum-Assisted (LightGBM + 1% QPU Expert) | Provenance Status |
| :--- | :---: | :---: | :---: | :---: |
| **Frontline Model** | Calibrated LightGBM | Calibrated LightGBM | Calibrated LightGBM | `[MEASURED]` |
| **Frontline Cost / Tx** | **$0.0000005** ($0.50 / 1M tx) | **$0.0000005** ($0.50 / 1M tx) | **$0.0000005** ($0.50 / 1M tx) | `[MEASURED]` |
| **Escalation Policy** | None (100% automated) | Top 1.0% Uncertainty Margin | Top 1.0% Uncertainty Margin | `[MEASURED]` |
| **Escalated Volume** | 0 transactions | 10,000 transactions | 10,000 transactions | `[MEASURED]` |
| **Specialist Model** | N/A | Tuned Classical RBF | Quantum Kernel (IonQ Aria via AWS) | `[MEASURED]` |
| **Specialist Compute Cost** | $0.00 | **$0.000015 / tx** ($0.15 / 10k tx) | **$35.30 / tx** ($353,000 / 10k tx) | `[MODELED]` |
| **Total Pipeline Compute Cost** | **$0.50** | **$0.65** | **$353,000.50** | `[MODELED]` |
| **Expected Fraud Loss** | $1,857,600 (Modeled) | **$1,671,840** (Modeled) | $1,671,840 (No additional lift) | `[MODELED]` |
| **Net Operational Benefit** | Baseline | **+$185,759.85** | **-$167,240.65** | `[MODELED]` |

---

## 4. Break-Even Analysis & Scaling with $N$

1. **Classical Selective Specialist:**  
   Incurring only **$0.15** of additional classical compute per 10,000 escalated transactions, Scenario 2 breaks even if the secondary specialist prevents just **1 additional fraud transaction** out of 10,000 escalated cases.
2. **Quantum-Assisted Specialist:**  
   Incurring **$353,000** in quantum cloud execution costs, the quantum expert would need to prevent over **1,961 additional fraudulent transactions** beyond Classical RBF just to cover its own compute bill.
3. **Conclusion:**  
   Because Phase 166 verified that $\Delta\text{PR-AUC} = +0.0653$ is not statistically significant ($p = 0.246$, $95\%\text{ CI: } [-0.0383, +0.1821]$), Quantum-Assisted deployment produces an immediate, catastrophic net loss under current QPU pricing.
