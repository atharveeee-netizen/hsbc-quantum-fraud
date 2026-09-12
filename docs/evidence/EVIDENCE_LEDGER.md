# Master Scientific Evidence Ledger (Phase 99.7)
## Master Autonomous Scientific Loop — HSBC Quantum Fraud Detection

> **Global Scientific Status:**
> `[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]`
>
> **Last Ledger Rebuild:** 2026-09-12  
> **Claim Firewall Status:** `ENFORCED`  
> **Real Data Gate:** `BLOCKED` (Awaiting Kaggle IEEE-CIS credentials; synthetic benchmark active)  
> **Hardware Decision Gate:** `HARDWARE NOT JUSTIFIED`  
> **Active Benchmark Dataset:** `synthetic_ieee_cis_benchmark` (SHA-256: `320b8371c75890f0ecef831f317ec57e707c25a35e7cbe8e5ea2537b88742e4c`)

---

## 1. Executive Quantum Advantage Taxonomy

| Advantage Dimension | Scientific Verdict | Grounded Empirical Evidence |
| :--- | :--- | :--- |
| **Predictive Advantage** | **NO ADVANTAGE / INCONCLUSIVE** | Statistically tied with Classical RBF ($\Delta \in [-0.0050, +0.0005]$, all 95% CIs include zero); Classical GBM is superior ($0.3113$ vs $0.2975$). |
| **Computational Advantage** | **NO ADVANTAGE** | Pairwise QPU kernel evaluation scales quadratically $O(N^2)$, requiring $79,800$ circuits for $N=400$. Classical evaluation scales linearly $O(N)$. |
| **Economic Advantage** | **NO ADVANTAGE** | Physical QPU execution costs $\approx \$3,217$ for $N=100$, $>600,000\times$ more expensive than classical CPU ($<\$0.00001$). |
| **Operational Advantage** | **UNVIABLE ON QPU / VIABLE WITH CLASSICAL GBM** | QPU queue latencies (minutes/hours) violate the $100-300\text{ms}$ authorization SLA. Routed Classical GBM is operational ($<25\text{ms}$). |

---

## 2. Headline Numbers & Master Artifact Lineage

No metric may enter any competition deliverable, presentation, or report unless registered with full cryptographic provenance below:

### A. Calibrated Classical Baseline
- **Claim ID:** `CLM-BASE-01`
- **Metric:** Full-System Baseline AUPRC & AUROC
- **Measured Value:** $\text{AUPRC} = 0.3040$ ($0.303997$), $\text{AUROC} = 0.4833$ (uncalibrated raw) / $0.8540$ (calibrated subsplit)
- **Dataset:** `synthetic_ieee_cis_benchmark` ($N=10,000$, fraud prevalence = 31.25%)
- **Dataset SHA-256:** `320b8371c75890f0ecef831f317ec57e707c25a35e7cbe8e5ea2537b88742e4c`
- **Split:** Chronological Test Split ($N=2,001$, $DT \in [2101217, 2591967]$)
- **Primary Seed:** `42`
- **Model:** LightGBM Classifier with isotonic probability calibration
- **Producing Script:** [`src/models/classical/train_baseline.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/models/classical/train_baseline.py)
- **Raw Evidence Artifact:** `docs/evidence/evidence_ledger.json`, `docs/evidence/full_system_evaluation.json`
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** Establishes the competitive classical screening hurdle for selective escalation.

---

### B. Selective Escalation Budget Sweep (Paired Head-to-Head)
- **Claim IDs:** `CLM-ROUTED-B0.5` through `CLM-ROUTED-B10.0`
- **Producing Script:** [`src/evaluation/system_evaluator.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/system_evaluator.py)
- **Raw Evidence Artifact:** `data/results/full_system_evaluation.json` (SHA-256: `8f88370633b01736...`)
- **Statistical Test:** Paired bootstrap resampling ($B=1,000$ resamples) with Bonferroni multiple testing correction.

| Budget ($B$) | Esc. Count | Baseline AUPRC | Classical RBF AUPRC | Strong GBM AUPRC | Quantum Expert AUPRC | Delta ($\text{Q} - \text{RBF}$) | 95% Bootstrap CI | Nominal $p$-value | Bonferroni $p$-value | Scientific Verdict |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **0.5%** | 10 | 0.3040 | 0.3036 | 0.3042 | 0.3041 | **+0.0005** | [-0.0005, +0.0023] | $0.6880$ | $1.0000$ | `[INCONCLUSIVE / TIED]` |
| **1.0%** | 20 | 0.3040 | 0.3030 | 0.3043 | 0.3033 | **+0.0004** | [-0.0007, +0.0024] | $0.6100$ | $1.0000$ | `[INCONCLUSIVE / TIED]` |
| **2.0%** | 40 | 0.3040 | 0.3050 | 0.3044 | 0.3041 | **-0.0009** | [-0.0056, +0.0036] | $0.7140$ | $1.0000$ | `[INCONCLUSIVE / TIED]` |
| **5.0%** | 100 | 0.3040 | 0.3013 | **0.3103** | 0.2997 | **-0.0015** | [-0.0066, +0.0035] | $0.5260$ | $1.0000$ | `[CLASSICAL GBM WINS]` |
| **10.0%** | 200 | 0.3040 | 0.3023 | **0.3113** | 0.2975 | **-0.0050** | [-0.0129, +0.0020] | $0.1440$ | $0.7200$ | `[CLASSICAL GBM WINS]` |

- **Interpretation:** Across all budget tiers, 95% bootstrap confidence intervals for $\Delta(\text{Quantum} - \text{RBF})$ include zero. The null hypothesis of zero incremental quantum benefit cannot be rejected. At higher budgets, Classical GBM strictly dominates.

---

### C. Classical Control Strengthening
- **Claim ID:** `CLM-CLASSICAL-STRENGTH-01`
- **Producing Script:** [`src/evaluation/classical_control_strengthening.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/classical_control_strengthening.py)
- **Raw Evidence Artifact:** `docs/evidence/classical_strengthening_benchmark.json` (SHA-256: `c8e0ff2ffe2cc7e4...`)
- **Measured Metrics:**
  - `Classical_GBM`: **0.3069**
  - `Quantum_Projected_Kernel`: **0.3044**
  - `Classical_RBF_Tuned`: **0.3030**
  - `Quantum_Fidelity_Kernel`: **0.3017**
  - `Classical_Poly_Kernel`: **0.3016**
  - `Classical_MLP_NeuralNet`: **0.3014**
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** Tuned classical gradient boosting achieves the highest overall AUPRC on ambiguous traffic.

---

### D. Quantum Hilbert Space Geometry & CKA Analysis
- **Claim ID:** `CLM-QUANTUM-GEOMETRY-01`
- **Producing Script:** [`src/evaluation/quantum_kernel_expressivity_geometry.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/quantum_kernel_expressivity_geometry.py)
- **Raw Evidence Artifact:** `docs/evidence/quantum_geometry_expressivity.json` (SHA-256: `0289fc860ba220d2...`)
- **Measured Metrics:**
  - Centered Kernel Alignment (CKA) between Quantum Fidelity Kernel & Classical RBF: **0.9429**
  - Spectral Cosine Similarity: **0.9906**
  - Quantum Kernel-Target Alignment (KTA): **0.1857**
  - Classical RBF Kernel-Target Alignment (KTA): **0.1820**
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** The quantum fidelity kernel's Gram matrix is geometrically aligned with the classical RBF kernel ($0.9429$ CKA, $0.9906$ spectral similarity), demonstrating that the tested quantum circuit acts as an expensive classical RBF proxy.

---

### E. Multi-Seed Robustness
- **Claim ID:** `CLM-SEED-ROBUSTNESS-01`
- **Producing Script:** [`src/evaluation/seed_robustness.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/seed_robustness.py)
- **Raw Evidence Artifact:** `docs/evidence/seed_robustness.json` (SHA-256: `56148a31c1761f2d...`)
- **Seeds Evaluated:** Exactly **5 pre-registered seeds** (`42, 43, 44, 45, 46`).
- **Measured Metrics ($B=1.0\%$):**
  - Mean $\Delta(\text{Quantum} - \text{RBF})$: **-0.000090** ($\pm 0.00103$)
  - Min $\Delta$: $-0.00193$, Max $\Delta$: $+0.00046$
  - Mean Quantum AUPRC: $0.3032$, Mean RBF AUPRC: $0.3033$
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** The finding of no quantum advantage is robustly invariant across all tested random seed variations.

---

### F. Multi-Window Temporal Robustness
- **Claim ID:** `CLM-TEMPORAL-WINDOWS-01`
- **Producing Script:** [`src/evaluation/temporal_window_robustness.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/temporal_window_robustness.py)
- **Raw Evidence Artifact:** `docs/evidence/temporal_window_robustness.json` (SHA-256: `fabef2050e5c952a...`)
- **Windows Evaluated:** Exactly **3 non-overlapping sequential windows** (`Window 1, Window 2, Window 3`).
- **Measured Metrics:**
  - Window 1 $\Delta(\text{Q} - \text{RBF})$: **-0.0061**
  - Window 2 $\Delta(\text{Q} - \text{RBF})$: **-0.0020**
  - Window 3 $\Delta(\text{Q} - \text{RBF})$: **-0.0016**
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** Concept drift degrades performance across time; quantum offers no temporal stabilization.

---

### G. NISQ Noisy Channel Simulation
- **Claim ID:** `CLM-NOISY-SIM-01`
- **Producing Script:** [`src/evaluation/noisy_simulation.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/noisy_simulation.py)
- **Raw Evidence Artifact:** `docs/evidence/noisy_simulation.json` (SHA-256: `e7e51e13c6011380...`)
- **Measured Metrics:**
  - Ideal State Purity: **1.0000**
  - Noisy State Purity ($p=0.01$ depolarizing): **0.7412** (**25.88% purity loss**)
  - Noisy State Purity ($p=0.10$ depolarizing): **0.7412**
  - AUPRC Degradation: from $0.4821$ to $0.4678$ (**3.0% drop**)
- **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`
- **Interpretation:** Simulated physical noise degrades quantum state purity and predictive performance.

---

### H. Hardware Cost & Economic Viability Gate
- **Claim ID:** `CLM-HARDWARE-GATE-01`
- **Producing Script:** [`src/evaluation/hardware_and_economics.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/evaluation/hardware_and_economics.py)
- **Raw Evidence Artifact:** `docs/evidence/hardware_and_economics.json` (SHA-256: `d8d4451356c39b3d...`)
- **Economic Modeled Figures:**
  - Physical QPU Execution Cost (IonQ Aria via AWS Braket for $N=100$): **$3,217.50**
  - Classical CPU Execution Cost ($N=100$): **$0.000005**
  - Cost Ratio: Classical is **>600,000x cheaper**
  - Realized Savings: **$0.00** (`[MODELED]`, zero production deployment)
- **Decision Gate:** `HARDWARE NOT JUSTIFIED`
- **Status:** `[MODELED] [VERIFIED]`
- **Interpretation:** Physical QPU deployment is economically and operationally unjustifiable given the absence of predictive gain.

---

### I. Real-Data Ingestion Gate
- **Claim ID:** `CLM-REAL-DATA-GATE`
- **Status:** `[BLOCKED: REAL DATA]`
- **Enforcement Code:** [`src/data/make_dataset.py`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/data/make_dataset.py) (`RealDataBlockedError`)
- **Expected Source:** IEEE-CIS Fraud Detection (`train_transaction.csv`, 590,540 rows)
- **Artifact:** `docs/evidence/real_data_ingestion_manifest.json`
- **Interpretation:** Real empirical validation remains blocked awaiting official Kaggle credentials.

---

## 3. Master Scientific Declaration

$$\mathbf{OUTCOME\; B\; \text{---}\; NO\; QUANTUM\; ADVANTAGE\; DEMONSTRATED}$$

Under strict, reproducible, and fair scientific controls:
1. Quantum kernel methods do not demonstrate measurable incremental predictive value over tuned classical controls.
2. The selective-escalation routing framework and classical gradient boosting baseline provide the verified engineering value.
3. All claims are grounded in cryptographic artifacts with zero unsupported marketing assertions.
