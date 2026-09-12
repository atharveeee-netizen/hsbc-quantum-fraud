# Master Scientific Evidence Ledger

> **Last Updated:** 2026-09-12T13:18:54.937279+00:00  
> **Claim Firewall Status:** `ENFORCED`  
> **Real Data Gate:** `BLOCKED` (Awaiting IEEE-CIS credentials; synthetic benchmark active)  
> **Hardware Decision Gate:** `HARDWARE NOT JUSTIFIED`  

---

## 1. Executive Quantum Advantage Taxonomy

| Advantage Dimension | Verdict | Empirical Evidence |
| :--- | :--- | :--- |
| **Predictive Advantage** | **NO ADVANTAGE / INCONCLUSIVE** | Statistically tied with Classical RBF ($\Delta \in [-0.0050, +0.0005]$, all 95% CIs include 0); Classical GBM is superior ($0.3113$ vs $0.2975$). |
| **Computational Advantage** | **NO ADVANTAGE** | Pairwise QPU kernel evaluation scales quadratically $O(N^2)$, requiring $79,800$ circuits for $N=400$. |
| **Economic Advantage** | **NO ADVANTAGE** | Physical QPU execution costs $pprox \$3,217$ for $N=100$, $>600,000	imes$ more expensive than classical CPU ($<\$0.00001$). |
| **Operational Advantage** | **UNVIABLE ON QPU / VIABLE WITH CLASSICAL GBM** | QPU queue latencies (minutes/hours) violate the $100-300$ms authorization SLA. Routed Classical GBM is operational. |

---

## 2. Complete Scientific Evidence Matrix (Phases 21–50)

| Claim ID | Category | Status | Primary Result | 95% CI / p-value / Metric | Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-BASE-01` | Classical Baseline | `MEASURED` | Established baseline on chronological synthetic split: AUPRC=0.3040, ROC-AU... | N/A | Evaluated on synthetic benchmark due to IEEE-... |
| `CLM-ROUTED-B0.5` | Routed System Evaluation | `MEASURED` | At 0.5% budget, Quantum AUPRC=0.3041 vs Classical RBF=0.3036 vs Classical G... | [-0.0005, +0.0023], p=0.6880 | Evaluated on 2-qubit simulator; classical RBF... |
| `CLM-ROUTED-B1.0` | Routed System Evaluation | `MEASURED` | At 1.0% budget, Quantum AUPRC=0.3033 vs Classical RBF=0.3030 vs Classical G... | [-0.0007, +0.0024], p=0.6100 | Evaluated on 2-qubit simulator; classical RBF... |
| `CLM-ROUTED-B2.0` | Routed System Evaluation | `MEASURED` | At 2.0% budget, Quantum AUPRC=0.3041 vs Classical RBF=0.3050 vs Classical G... | [-0.0056, +0.0036], p=0.7140 | Evaluated on 2-qubit simulator; classical RBF... |
| `CLM-ROUTED-B5.0` | Routed System Evaluation | `MEASURED` | At 5.0% budget, Quantum AUPRC=0.2997 vs Classical RBF=0.3013 vs Classical G... | [-0.0066, +0.0035], p=0.5260 | Evaluated on 2-qubit simulator; classical RBF... |
| `CLM-ROUTED-B10.0` | Routed System Evaluation | `MEASURED` | At 10.0% budget, Quantum AUPRC=0.2975 vs Classical RBF=0.3023 vs Classical ... | [-0.0129, +0.0020], p=0.1440 | Evaluated on 2-qubit simulator; classical RBF... |
| `CLM-ROUTER-CAUSALITY-01` | Router Causality | `VERIFIED` | Transaction amount drives 2.09x fraud enrichment alone; residual uncertaint... | Enrichment=2.09x | Tested on synthetic features mirroring IEEE-C... |
| `CLM-CLASSICAL-STRENGTH-01` | Classical Strengthening | `MEASURED` | Strong Classical GBM achieves the highest mean system AUPRC (0.3069), outpe... | N/A | All models fitted strictly on training escala... |
| `CLM-QUANTUM-GEOMETRY-01` | Quantum Geometry | `VERIFIED` | Quantum Fidelity Kernel has 0.9429 CKA geometric alignment and 0.9906 spect... | CKA=0.9429 | Evaluated on matched N=100 samples with 2-qub... |
| `CLM-SEED-ROBUSTNESS-01` | Seed Robustness | `VERIFIED` | Across 5 pre-registered random seeds (42-46), Δ(Quantum - RBF) is consisten... | N/A | Evaluated across budgets 1%, 5%, 10%.... |
| `CLM-SCALING-01` | Resource Scaling | `VERIFIED` | Full-population quantum kernel matrices scale quadratically O(N^2) in circu... | N/A | Measured on PennyLane default.qubit simulator... |
| `CLM-TEMPORAL-WINDOWS-01` | Temporal Robustness | `VERIFIED` | Monotonic degradation observed across time windows (concept drift). Δ(Quant... | N/A | Evaluated on 3 non-overlapping sequential win... |
| `CLM-NOISY-SIM-01` | Noise Sensitivity | `VERIFIED` | State purity drops from 1.000 to 0.9406 at p=0.01 and 0.5647 at p=0.10. Cla... | N/A | Single-qubit depolarizing channel on default.... |
| `CLM-HARDWARE-GATE-01` | Hardware Gate | `VERIFIED` | Hardware Decision Gate Verdict: HARDWARE NOT JUSTIFIED. Physical QPU execut... | HARDWARE NOT JUSTIFIED | Based on AWS Braket standard QPU pricing mode... |
| `CLM-REAL-DATA-GATE` | Real Data Ingestion | `BLOCKED` | Real IEEE-CIS evaluation is formally blocked by lack of Kaggle credentials;... | N/A | Real data results cannot be reported without ... |
| `CLM-SEC-AUDIT-01` | Security & Hygiene | `VERIFIED` | Security audit verified clean: [VERIFIED: NO P0/P1 FINDINGS WITHIN TESTED S... | [VERIFIED: NO P0/P1 FINDINGS WITHIN TESTED SCOPE] | Static regex and ast analysis.... |
| `CLM-REPRO-AUDIT-01` | Reproducibility | `VERIFIED` | Reproducibility verified in documented environment: core modules enforce de... | [VERIFIED: REPRODUCIBLE IN DOCUMENTED ENVIRONMENT] | Requires Python 3.10+.... |
| `CLM-FIREWALL-01` | Claim Firewall | `VERIFIED` | Claim firewall audit verified: 0 unsubstantiated marketing phrases across d... | [VERIFIED: FIREWALL CLEAN] | Automated pattern matching.... |
| `CLM-RESEARCH-VERDICT` | Research Verdict | `VERIFIED` | OUTCOME B — NO QUANTUM ADVANTAGE. Null hypothesis upheld under fair control... | N/A | Evaluated on synthetic benchmark; physical ha... |

---

## 3. Strict Scientific Controls Enforced

1. **No Cherry-Picking:** All 5 escalation budgets reported across all runs.
2. **Paired Bootstrap:** Every quantum vs classical delta is computed on identical resampled test transactions ($N=1000$ resamples).
3. **Multiple Testing Correction:** Bonferroni and Benjamini-Hochberg FDR adjustments applied across all tested budgets.
4. **Fair Tuning:** Classical RBF and GBM controls tuned via cross-validation strictly on the training fold.
5. **Leakage Firewall:** Scalers fitted exclusively on historical training data; timestamps strictly monotone ($T_{\text{train}} < T_{\text{calib}} < T_{\text{test}}$).
6. **Noisy Simulation:** Purity degradation ($1.000 \to 0.565$) confirms physical noise cannot improve performance.
7. **Hardware Gate:** Hardware expenditure rejected as scientifically unjustified.
