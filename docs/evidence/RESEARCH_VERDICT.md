# Master Research Verdict: OUTCOME B — NO QUANTUM ADVANTAGE

**Project:** HSBC Quantum-Enhanced Credit Card Fraud Detection Proof of Concept  
**Repository:** `atharveeee-netizen/hsbc-quantum-fraud`  
**Scientific Verdict:** `[OUTCOME B: NO QUANTUM ADVANTAGE]`  
**Research Status Tags:** `[SYNTHETIC]` `[MEASURED]` `[VERIFIED]` `[OUTCOME B: NO QUANTUM ADVANTAGE]` `[HARDWARE NOT JUSTIFIED]`  
**Machine-Readable Source:** [`docs/evidence/research_verdict.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/research_verdict.json)

---

## Executive Summary

Through the execution of an autonomous scientific master loop across 80 phases, this project conducted an exhaustive, fair, and statistically disciplined benchmark of quantum kernel methods against matched classical controls for credit card fraud detection under selective escalation constraints.

The conclusion is definitive:
**Under a fair experimental design, quantum kernel methods do not provide a predictive, computational, economic, or operational advantage over matched classical controls.**

This conclusion is **not a failure of engineering**. On the contrary, it represents a high-value scientific result:
1. It validates that **selective routing** is effective ($2.09\times$ enrichment via transaction amount, $1.23\times$ additive enrichment via residual classification uncertainty).
2. It proves that **Strong Classical Gradient Boosting (`ClassicalGBMExpert`)** is the superior expert for escalated traffic ($0.3113$ full-system AUPRC vs $0.2975$ for Quantum).
3. It explains the mathematical mechanism: Centered Kernel Alignment (CKA) between the Quantum Fidelity Kernel and the Classical Gaussian RBF Kernel is **$0.9429$** ($94.3\%$ geometric alignment) with **$0.9906$** spectral cosine similarity. The quantum kernel functions as an expensive surrogate for the classical RBF kernel.
4. It enforces an honest **Hardware Decision Gate**: running on physical QPUs would cost $>600,000\times$ more than classical compute and violate banking authorization SLAs without any predictive benefit.

---

## Mandatory Research Questions & Empirical Answers

### Q1: Does selective routing improve the fraud workflow?
* **Answer:** **YES** `[VERIFIED]`
* **Empirical Evidence:** Amount-only routing provides $2.09\times$ fraud enrichment. Residual uncertainty orthogonal to amount provides $1.23\times$ additive enrichment. The combined router lifts full-system AUPRC from $0.3040$ (frontline alone) to $0.3162$ (with expert escalation).
* **Artifacts:** [`docs/evidence/router_causality_ablation.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/router_causality_ablation.json), [`docs/evidence/router_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/router_audit.json).

### Q2: Does the quantum expert beat a fair classical expert?
* **Answer:** **NO** `[NO QUANTUM ADVANTAGE]`
* **Empirical Evidence:** Against a properly tuned Classical RBF Expert, the Quantum Expert is statistically tied across all budgets ($\Delta \in [-0.0050, +0.0005]$). Against Strong Classical GBM, quantum is decisively beaten across all budgets ($0.2975$ vs $0.3113$ at $10\%$ budget).
* **Artifacts:** [`docs/evidence/budget_sweep_results.csv`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/budget_sweep_results.csv), [`docs/evidence/classical_strengthening_benchmark.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/classical_strengthening_benchmark.json).

### Q3: At what budget does quantum add value?
* **Answer:** **AT NO TESTED BUDGET** `[MEASURED]`
* **Empirical Evidence:** Evaluated across $B \in \{0.5\%, 1.0\%, 2.0\%, 5.0\%, 10.0\%\}$. $\Delta\text{AUPRC}(\text{Quantum} - \text{RBF})$:
  * Budget $0.5\%$: $+0.0005$ $[-0.0005, +0.0023]$
  * Budget $1.0\%$: $+0.0004$ $[-0.0007, +0.0024]$
  * Budget $2.0\%$: $-0.0009$ $[-0.0056, +0.0036]$
  * Budget $5.0\%$: $-0.0015$ $[-0.0066, +0.0035]$
  * Budget $10.0\%$: $-0.0050$ $[-0.0129, +0.0020]$
* **Artifacts:** [`docs/evidence/budget_sweep_results.csv`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/budget_sweep_results.csv).

### Q4: Is the difference statistically meaningful?
* **Answer:** **NO** `[INCONCLUSIVE / NULL HYPOTHESIS UPHELD]`
* **Empirical Evidence:** Across $1,000$ paired bootstrap resamples per budget, every $95\%$ confidence interval contains zero. Bonferroni-adjusted $p$-values range from $0.7200$ to $1.0000$ (nominal $p \in [0.1440, 0.7140]$).
* **Artifacts:** [`docs/evidence/full_system_evaluation.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/full_system_evaluation.json).

### Q5: Does it survive temporal validation?
* **Answer:** **YES (NEGATIVE CONCLUSION CONFIRMED)** `[VERIFIED]`
* **Empirical Evidence:** Evaluated across $3$ sequential temporal windows on chronological streams. Concept drift degrades overall AUPRC monotonically, and $\Delta(\text{Quantum} - \text{RBF})$ remains non-positive across all windows ($-0.0042$, $-0.0051$, $-0.0048$).
* **Artifacts:** [`docs/evidence/temporal_window_robustness.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/temporal_window_robustness.json).

### Q6: Does it survive noise?
* **Answer:** **NO** `[NOISE-FRAGILE]`
* **Empirical Evidence:** Depolarizing noise simulation on `default.mixed` collapses state purity from $1.000$ to $0.565$ at noise probability $p=0.10$, reducing classification AUPRC from $0.4821$ to $0.4678$.
* **Artifacts:** [`docs/evidence/noisy_simulation.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/noisy_simulation.json).

### Q7: Does it survive real hardware, if hardware is executed?
* **Answer:** **HARDWARE NOT EXECUTED / NOT JUSTIFIED** `[HARDWARE NOT JUSTIFIED]`
* **Empirical Evidence:** Physical QPU execution was formally gated and rejected under Phase 44/69 criteria. Because quantum is uncompetitive in ideal simulation and degraded by noise, expending physical hardware credits would be scientifically unjustified.
* **Artifacts:** [`docs/evidence/hardware_and_economics.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/hardware_and_economics.json).

### Q8: Is there any measurable operational/economic benefit?
* **Answer:** **NO** `[UNVIABLE ON QPU / VIABLE WITH CLASSICAL GBM]`
* **Empirical Evidence:** Physical QPU execution costs $\approx \$3,217$ for $N=100$ ($>600,000\times$ more than classical CPU compute at $\$0.000005$). QPU queue times (minutes/hours) violate the $100-300$ms authorization SLA.
* **Artifacts:** [`docs/evidence/hardware_and_economics.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/hardware_and_economics.json).

### Q9: What evidence supports every claim?
* **Answer:** **MACHINE-READABLE EVIDENCE LEDGER AND REPRODUCIBLE SCRIPTS** `[VERIFIED]`
* **Empirical Evidence:** 22 machine-readable JSON and CSV artifacts in `docs/evidence/` verified by automated CI checks with 0 discrepancies and 100% test pass rate.
* **Artifacts:** [`docs/evidence/evidence_ledger.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/evidence_ledger.json), [`docs/evidence/EVIDENCE_LEDGER.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/EVIDENCE_LEDGER.md).

### Q10: What remains unknown?
* **Answer:** **REAL IEEE-CIS RAW EVALUATION AND FAULT-TOLERANT REGIMES** `[BLOCKED: REAL DATA]`
* **Empirical Evidence:** Full IEEE-CIS raw tabular dataset access is blocked pending Kaggle credentials. Whether future fault-tolerant quantum algorithms (e.g. quantum linear systems solvers) could yield advantages on non-kernel fraud embeddings remains an open theoretical question.
* **Artifacts:** [`docs/evidence/real_data_ingestion_manifest.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_data_ingestion_manifest.json).

---

## Production Recommendations for Financial Institutions

1. **Deploy the Selective Escalation Architecture:** The combination of frontline LightGBM scoring with amount-and-uncertainty routing is immediately viable and yields significant fraud capture enrichment.
2. **Deploy Classical GBM as the Escalation Specialist:** `ClassicalGBMExpert` trained on the escalated partition is fast (<5ms), cheap, highly accurate, and beats all kernel variants.
3. **Retain Quantum Kernel Methods as Research Diagnostics Only:** Current NISQ quantum kernels reproduce classical RBF geometry with extreme cost and latency penalties.
