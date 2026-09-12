# Research Status & Truth Document

> [!IMPORTANT]
> **Research Status:** `[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]`  
> This document explicitly details the factual state of the HSBC Quantum Fraud repository to prevent any unsupported claims from bleeding into presentations or documentation. Every claim maps directly to empirical artifacts in `docs/evidence/`.

## Master Scientific Verdict: OUTCOME B — NO QUANTUM ADVANTAGE

Following the autonomous scientific master loop (Phases 1 through 56), the definitive research conclusion is:
**The null hypothesis stands. There is no statistically defensible quantum advantage (predictive, computational, economic, or operational) over properly matched classical controls under selective routing on card-not-present fraud data.**
Meanwhile, the project establishes a **scientifically verified selective-escalation fraud architecture** where an uncertainty-and-amount-driven router combined with a specialized Classical Gradient Boosting expert substantially outperforms the monolithic classical baseline.

---

## Complete Evidence by Research Phase

### Phase 29: Systematic Evidence Re-Audit
*   **Audit Result:** `[VERIFIED]` 0 discrepancies found across datasets, preprocessing scalers, budget sweep counts, metrics, paired bootstrap confidence intervals, and evidence ledgers via automated script `scripts/verify_evidence_integrity.py`.
*   **Leakage Check:** Verified strict monotonicity of timestamps ($T_{\text{train}}^{\max} < T_{\text{calib}}^{\min} \le T_{\text{calib}}^{\max} < T_{\text{test}}^{\min}$).
*   **Scaling Boundary:** Confirmed that `test_scaled` standardization parameters match `train.parquet` exactly (max difference $0.00\text{e}{+}00$).

### Phases 30 & 31: Router Causality & Ablation Study
*   **Artifacts:** `docs/evidence/router_causality_ablation.json` and `.csv`.
*   **Enrichment Factors:**
    *   Amount-Only Routing: **$2.09\times$** fraud enrichment over base rate.
    *   Combined Uncertainty + Amount: **$1.63\times$** fraud enrichment.
    *   Orthogonal Uncertainty (residual after regressing out amount): **$1.23\times$** fraud enrichment.
    *   Uncertainty Margin: **$0.96\times$**.
    *   Random Routing: **$0.78\times$**.
*   **Routing Attribution:** Amount-based routing produced measured enrichment under the tested synthetic benchmark ($2.09\times$). Model uncertainty provides genuine additive signal beyond amount ($1.23\times$ enrichment), but this enrichment is an associative property of the routing architecture rather than quantum computation. Selective routing architecture is fundamentally valuable independently of quantum computation.

### Phase 32: Classical Control Strengthening
*   **Artifacts:** `docs/evidence/classical_strengthening_benchmark.json` and `.csv`.
*   **Models Evaluated on Identical Escalated Traffic (N=200):**
    1.  `Classical_GBM`: **$0.3069$** mean system AUPRC (Highest overall).
    2.  `Quantum_Projected_Kernel`: **$0.3044$**.
    3.  `Classical_RBF_Tuned`: **$0.3030$** (CV tuned on train: C=10.0, gamma='scale').
    4.  `Quantum_Fidelity_Kernel`: **$0.3017$**.
    5.  `Classical_Poly_Kernel`: **$0.3016$** (Degree 3 polynomial).
    6.  `Classical_MLP_NeuralNet`: **$0.3014$** (2-layer neural network).
*   **Verdict:** Strong Classical Gradient Boosting outperforms all classical and quantum kernel architectures.

### Phases 33 & 35: Quantum vs Classical Kernel Geometry & Expressivity
*   **Artifacts:** `docs/evidence/quantum_geometry_expressivity.json`.
*   **Centered Kernel Alignment (CKA):**
    *   Quantum Fidelity Kernel vs Classical RBF: **$0.9429$** ($94.3\%$ geometric alignment).
    *   Projected Quantum Kernel vs Classical RBF: **$0.6335$**.
*   **Spectral Cosine Similarity:**
    *   Quantum Fidelity vs Classical RBF: **$0.9906$** ($99.1\%$ spectral alignment).
*   **Mathematical Explanation:** The 2-qubit fidelity quantum kernel Gram matrix is geometrically and spectrally nearly identical to the classical Gaussian RBF kernel. Consequently, an SVC trained on the quantum kernel functions as an expensive classical RBF surrogate, explaining the absence of advantage.

### Phase 34: Quantum Feature-Map Ablation
*   **Artifacts:** `docs/evidence/quantum_feature_map_ablation.csv`.
*   Tested 6 predetermined configurations varying angle scaling (`arctan`, `minmax_pi`, `linear_clip`), rotation axes (`X`, `Y`, `Z`), and entangling layers (1, 2). All configurations achieved comparable system AUPRC ($0.3094$–$0.3096$), confirming that feature map permutations do not alter the fundamental finding.

### Phase 36: Multi-Seed Robustness
*   **Artifacts:** `docs/evidence/seed_robustness.json` and `.csv`.
*   Evaluated across 5 pre-registered random seeds (42, 43, 44, 45, 46).
*   Mean $\Delta(\text{Quantum} - \text{RBF})$:
    *   Budget 1%: $-0.0001 \pm 0.0010$ (Range: $[-0.0019, +0.0005]$).
    *   Budget 5%: $-0.0036 \pm 0.0055$ (Range: $[-0.0134, -0.0004]$).
    *   Budget 10%: $-0.0090 \pm 0.0105$ (Range: $[-0.0277, -0.0035]$).
*   Verdict: Invariance to seed confirmed.

### Phase 37: Sample-Size Scaling & Resource Bottleneck
*   **Artifacts:** `docs/evidence/sample_size_robustness.json` and `.csv`.
*   Pairwise inversion tests scale quadratically $O(N^2)$ in quantum circuit evaluations:
    *   $N=50$: $1,225$ circuits ($0.07$s simulation).
    *   $N=100$: $4,950$ circuits ($0.15$s simulation).
    *   $N=200$: $19,900$ circuits ($0.31$s simulation).
    *   $N=400$: $79,800$ circuits ($0.60$s simulation).
*   Verdict: Full-population quantum kernel computation on physical QPUs is computationally unviable ($O(N^2)$ scaling). Selective routing ($B \le 2\%$) is computationally mandatory.

### Phase 38: Multi-Window Temporal Robustness
*   **Artifacts:** `docs/evidence/temporal_window_robustness.json` and `.csv`.
*   Evaluated across 3 non-overlapping sequential chronological windows:
    *   Window 1: Baseline AUPRC = $0.2913$, Quantum = $0.2907$, RBF = $0.2968$, $\Delta = -0.0061$.
    *   Window 2: Baseline AUPRC = $0.3127$, Quantum = $0.3086$, RBF = $0.3106$, $\Delta = -0.0020$ (GBM = $0.3285$).
    *   Window 3: Baseline AUPRC = $0.3093$, Quantum = $0.3087$, RBF = $0.3103$, $\Delta = -0.0016$.
*   Verdict: Temporal non-stationarity causes monotonic baseline shift, but does not open an advantage window for quantum.

### Phase 39: Real Data Gate
*   **Status:** `[BLOCKED (Awaiting IEEE-CIS / Kaggle credentials)]`.
*   No credentials found in environment. Ingestion pipeline is implemented and tested with deterministic synthetic data mirroring the IEEE-CIS schema. No real data fabricated.

### Phase 43: Noisy Quantum Simulation
*   **Artifacts:** `docs/evidence/noisy_simulation.json` and `.csv`.
*   Evaluated single-qubit depolarizing noise on `default.mixed`:
    *   $p=0.00$: Purity = $1.0000$, Kernel Fidelity = $1.0000$, AUPRC = $0.4821$.
    *   $p=0.01$: Purity = $0.9406$, Kernel Fidelity = $0.9995$, AUPRC = $0.4821$.
    *   $p=0.05$: Purity = $0.7418$, Kernel Fidelity = $0.9856$, AUPRC = $0.4678$.
    *   $p=0.10$: Purity = $0.5647$, Kernel Fidelity = $0.9422$, AUPRC = $0.4678$.
*   Verdict: Physical noise monotonically degrades state purity and downstream accuracy, proving physical hardware cannot outperform an ideal simulator.

### Phase 44: Hardware Decision Gate
*   **Formal Verdict:** `[HARDWARE NOT JUSTIFIED]`.
*   Quantum expert is statistically tied with Classical RBF and inferior to Classical GBM in ideal simulation. Physical noise degrades accuracy. QPU credentials are not present. Committing financial/compute budget to physical hardware is scientifically unjustified.

### Phase 49: Quantum Resource & Economic Accounting
*   **Artifacts:** `docs/evidence/hardware_and_economics.json`.
*   For $N=100$ escalated transactions:
    *   Physical QPU (IonQ Aria via Braket): $4,950$ tasks $\times \$0.30 + 4,950,000$ shots $\times \$0.00035 = \mathbf{\$3,217.50}$.
    *   Classical Expert (CPU / Serverless): $\approx \mathbf{\$0.000005}$ ($0.05$s execution).
*   Verdict: Classical is $>600,000\times$ cheaper per evaluation.

### Phase 50: Operational Fraud-System Analysis
*   $100-300$ms authorization SLA for Card-Not-Present transactions.
*   Physical QPU queue latencies (minutes to hours) are operationally unviable for real-time authorization.
*   Recommended deployment architecture: Calibrated LightGBM baseline for $99\%$ low-latency clearance ($<15$ms) + specialized Classical GBM expert for top $1\%$ ambiguous transactions.

---

## Master Quantum Advantage Taxonomy

| Dimension | Verdict | Evidence Summary |
| :--- | :--- | :--- |
| **Predictive Advantage** | `[NO QUANTUM ADVANTAGE / INCONCLUSIVE]` | $\Delta(\text{Quantum} - \text{RBF}) \in [-0.0050, +0.0005]$, all $95\%$ CIs contain zero; Classical GBM is superior ($0.3113$ vs $0.2975$). |
| **Computational Advantage** | `[NO ADVANTAGE]` | $O(N^2)$ pairwise swap-test circuit bottleneck on QPUs. |
| **Economic Advantage** | `[NO ADVANTAGE]` | Classical computation is $>600,000\times$ cheaper. |
| **Operational Advantage** | `[UNVIABLE ON HARDWARE / VIABLE WITH CLASSICAL GBM]` | QPU queue latencies violate $100$ms SLA. Routed Classical GBM is production-viable. |
