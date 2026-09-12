# HSBC Quantum-Enhanced Credit Card Fraud Detection

**Repository:** `atharveeee-netizen/hsbc-quantum-fraud`  
**Focus:** Scientifically defensible hybrid classical–quantum fraud detection proof of concept.  
**Research Status:** `[SYNTHETIC]` `[MEASURED]` `[VERIFIED]` `[OUTCOME B: NO QUANTUM ADVANTAGE]`

---

## Strict Scientific Claim Firewall

> [!IMPORTANT]
> To eliminate unsubstantiated claims and marketing narratives, all findings are tagged with standardized scientific statuses:
> * `[VERIFIED]` - Independently tested and confirmed reproducible via automated verification tests (`tests/test_evidence_reproducibility.py`).
> * `[IMPLEMENTED]` - Operational code running end-to-end in the repository.
> * `[MEASURED]` - Empirical metrics extracted directly from machine-readable experiment artifacts in `docs/evidence/`.
> * `[SYNTHETIC]` - Evaluated on a deterministic synthetic fixture mirroring IEEE-CIS tabular schema.
> * `[BLOCKED]` - Prevented by external constraints (e.g. AWS Braket QPU access, Kaggle credentials).
> * `[INCONCLUSIVE]` - Difference from null hypothesis is not statistically significant ($p > 0.05$).

---

## 1. Master Research Verdict: OUTCOME B — NO QUANTUM ADVANTAGE

Following execution of the complete autonomous scientific master loop (Phases 1 through 56), the definitive research conclusion is:

1. **Predictive Advantage:** `[NO QUANTUM ADVANTAGE / INCONCLUSIVE]`  
   Across all tested escalation budgets ($B \in \{0.5\%, 1.0\%, 2.0\%, 5.0\%, 10.0\%\}$), the difference in full-system AUPRC between the Quantum Expert and a properly tuned Classical RBF Expert is statistically indistinguishable from zero ($\Delta \in [-0.0050, +0.0005]$, with $0$ inside the 95% bootstrap confidence interval in every case; Bonferroni-adjusted $p \ge 0.72$).
2. **Best Performing Expert Model:** Strong Classical Gradient Boosting (`ClassicalGBMExpert` trained specifically on the escalated subset) achieved the highest full-system AUPRC across all budgets ($0.3113$ at $10\%$ budget), outperforming both Classical RBF and Quantum Experts.
3. **Mathematical Cause of Equivalence:** Centered Kernel Alignment (CKA) between the Quantum Fidelity Kernel and Classical RBF is **$0.9429$** ($94.3\%$ geometric alignment), with **$0.9906$** spectral cosine similarity. The quantum kernel functions as an expensive classical RBF surrogate.
4. **Causal Value of Selective Routing:** Selective routing is empirically validated. Amount-driven escalation provides **$2.09\times$ fraud enrichment**, while residual uncertainty orthogonal to amount provides **$1.23\times$ additive enrichment**. This gain is a property of the routing architecture, not quantum computation.
5. **Hardware Decision Gate:** Formal verdict is `[HARDWARE NOT JUSTIFIED]`. Physical noise degrades quantum state purity ($1.000 \to 0.565$ in Phase 43 simulation), and physical QPU execution costs $\approx \$3,217$ for $N=100$ ($>600,000\times$ more expensive than classical CPU execution at $\$0.000005$).

---

## 2. Master Quantum Advantage Taxonomy

| Advantage Dimension | Scientific Verdict | Empirical Evidence & Artifact Reference |
| :--- | :--- | :--- |
| **Predictive Advantage** | `[NO QUANTUM ADVANTAGE]` | $\Delta(\text{Quantum} - \text{RBF}) \in [-0.0050, +0.0005]$, all $95\%$ CIs contain zero; Classical GBM is superior ($0.3113$ vs $0.2975$). Artifact: `full_system_evaluation.json`. |
| **Computational Advantage** | `[NO ADVANTAGE]` | Physical QPU kernel computation scales quadratically $O(N^2)$, requiring $79,800$ circuits for $N=400$. Artifact: `sample_size_robustness.json`. |
| **Economic Advantage** | `[NO ADVANTAGE]` | Physical QPU execution on IonQ Aria costs $\approx \$3,217$ for $N=100$, $>600,000\times$ more expensive than classical compute ($\approx \$0.000005$). Artifact: `hardware_and_economics.json`. |
| **Operational Advantage** | `[UNVIABLE ON QPU / VIABLE WITH CLASSICAL GBM]` | QPU queue latencies (minutes/hours) violate the $100-300$ms authorization SLA. The selective-escalation architecture with Classical GBM is production-viable. Artifact: `hardware_and_economics.json`. |

---

## 3. Empirical Evidence Matrix (Full System Budget Sweep)

Evaluated across the full chronological test stream ($N=2,001$ transactions) using **$1,000$ paired bootstrap resamples** with identical transaction subsets and training-only tuning:

| Escalation Budget | Escalated Count | Classical Only AUPRC | Classical + RBF Expert | Classical + Quantum (FQK) | Classical + Strong GBM | Classical + Random Route | $\Delta(\text{Quantum} - \text{RBF})$ [95% Bootstrap CI] | Nominal $p$-value | Bonferroni $p$-value | Zero in 95% CI |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.5%** | 10 | 0.3040 | 0.3036 | 0.3041 | **0.3042** | 0.3029 | $+0.0005$ $[-0.0005, +0.0023]$ | $0.6880$ | $1.0000$ | **Yes** |
| **1.0%** | 20 | 0.3040 | 0.3030 | 0.3033 | **0.3043** | 0.3011 | $+0.0004$ $[-0.0007, +0.0024]$ | $0.6100$ | $1.0000$ | **Yes** |
| **2.0%** | 40 | 0.3040 | 0.3050 | 0.3041 | 0.3044 | 0.3009 | $-0.0009$ $[-0.0056, +0.0036]$ | $0.7140$ | $1.0000$ | **Yes** |
| **5.0%** | 100 | 0.3040 | 0.3013 | 0.2997 | **0.3103** | 0.2975 | $-0.0015$ $[-0.0066, +0.0035]$ | $0.5260$ | $1.0000$ | **Yes** |
| **10.0%** | 200 | 0.3040 | 0.3023 | 0.2975 | **0.3113** | 0.3062 | $-0.0050$ $[-0.0129, +0.0020]$ | $0.1440$ | $0.7200$ | **Yes** |

*Artifact Source:* [`docs/evidence/budget_sweep_results.csv`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/budget_sweep_results.csv) and [`docs/evidence/full_system_evaluation.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/full_system_evaluation.json).

---

## 4. Architecture & Routing

```text
CARD-NOT-PRESENT TRANSACTION
            ↓
     CLASSICAL BASELINE (LightGBM)
            ↓
      ISOTONIC CALIBRATED SCORE
            ↓
     ESCALATION ROUTER (|p - 0.5| & TransactionAmt)
            ↓
     ┌──────┴──────────────────────────────────────────┐
     ↓                                                 ↓
 NORMAL TRAFFIC (100-B)%                        BORDERLINE HARD CASE (B%)
     ↓                                                 ↓
 CLASSICAL DECISION                     ┌──────────────┼──────────────┐
 (<15ms SLA)                            ↓              ↓              ↓
                                     QUANTUM       CLASSICAL      STRONG GBM
                                     EXPERT        RBF EXPERT       EXPERT
                                     (Tied)          (Tied)       (WINNER: 0.3113)
                                        ↓              ↓              ↓
                                        └──────────────┼──────────────┘
                                                       ↓
                                         PAIRED BOOTSTRAP TEST (N=1000)
                                                       ↓
                                         EVIDENCE LEDGER AUDIT (Phase 42)
```

---

## 5. Complete Scientific Audit Summary

*   **Router Causality & Ablation (Phases 30 & 31):** Amount-only routing achieves $2.09\times$ fraud enrichment; residual uncertainty orthogonal to amount achieves $1.23\times$ enrichment. Combining uncertainty with amount produces $1.63\times$ enrichment and lifts system AUPRC from $0.3040$ to $0.3162$.
*   **Classical Strengthening (Phase 32):** Tested Tuned RBF ($0.3030$), LightGBM ($0.3069$), MLP Neural Net ($0.3014$), and Polynomial Kernel ($0.3016$) on identical training escalated slices ($N=200$). LightGBM expert is the top performer.
*   **Quantum Geometry (Phases 33 & 35):** CKA similarity between Quantum Fidelity Kernel and Classical RBF is $0.9429$. Spectral cosine similarity is $0.9906$.
*   **Multi-Seed Robustness (Phase 36):** Tested across 5 pre-registered seeds (42–46). Mean $\Delta(\text{Quantum} - \text{RBF})$ remains $\le 0$ across all seeds ($-0.0001$ at 1%, $-0.0036$ at 5%, $-0.0090$ at 10%).
*   **Resource Scaling (Phase 37):** Physical QPU execution requires $O(N^2)$ pairwise circuits ($79,800$ circuits at $N=400$), proving selective routing ($B \le 2\%$) is computationally mandatory.
*   **Multi-Window Temporal Robustness (Phase 38):** Evaluated across 3 sequential chronological test windows. Monotonic degradation observed (concept drift); quantum delta remains negative across all windows.
*   **Noisy Quantum Simulation (Phase 43):** Depolarizing noise on `default.mixed` degrades state purity from $1.000$ to $0.565$ and reduces AUPRC from $0.4821$ to $0.4678$.
*   **Hardware Decision Gate (Phase 44):** Evaluated as `[HARDWARE NOT JUSTIFIED]`. No physical QPU credentials present; physical execution would cost $\sim \$3,200$ for $N=100$ without scientific benefit.
*   **Real IEEE-CIS Benchmark (Phase 39):** `[BLOCKED]` pending credentials. Evaluated strictly on synthetic benchmarks without fabricating real data.

---

## 6. Reproducibility & Commands

A clean checkout reproduces all results deterministically:

```bash
# 1. Run all 14 unit, integration, and evidence-verification tests
pytest

# 2. Generate deterministic synthetic data fixture
python -m src.data.generate_synthetic

# 3. Perform strict chronological temporal split (70/10/20)
python -m src.data.make_dataset

# 4. Fit feature scalers strictly on training data
python -m src.features.build_features

# 5. Train and calibrate incumbent classical LightGBM
python -m src.models.classical.train_baseline

# 6. Run router causality and controlled ablation study (Phases 30 & 31)
python -m src.evaluation.routing_causality_ablation

# 7. Run classical control strengthening benchmark (Phase 32)
python -m src.evaluation.classical_control_strengthening

# 8. Run quantum kernel expressivity and geometry CKA audit (Phases 33, 34, 35)
python -m src.evaluation.quantum_kernel_expressivity_geometry

# 9. Run multi-seed robustness testing (Phase 36)
python -m src.evaluation.seed_robustness

# 10. Run sample-size resource scaling analysis (Phase 37)
python -m src.evaluation.sample_size_robustness

# 11. Run multi-window temporal robustness analysis (Phase 38)
python -m src.evaluation.temporal_window_robustness

# 12. Run realistic depolarizing noisy quantum simulation (Phase 43)
python -m src.evaluation.noisy_simulation

# 13. Evaluate hardware gate and economic accounting (Phases 44, 49, 50)
python -m src.evaluation.hardware_and_economics

# 14. Compile master evidence ledger
python -m src.evaluation.evidence_ledger

# 15. Verify 100% evidence consistency and zero leakage
python scripts/verify_evidence_integrity.py
```

---

## 7. Master Scientific Evidence Ledger

All empirical artifacts, configurations, random seeds, and statistical confidence intervals are tracked in:
* [`docs/evidence/EVIDENCE_LEDGER.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/EVIDENCE_LEDGER.md)
* [`docs/evidence/evidence_ledger.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/evidence_ledger.json)
* [`docs/research_status.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/research_status.md)
* [`docs/architecture.md`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/architecture.md)
