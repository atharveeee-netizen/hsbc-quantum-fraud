# HSBC Quantum-Enhanced Credit Card Fraud Detection

**Repository:** `atharveeee-netizen/hsbc-quantum-fraud`  
**Focus:** Scientifically defensible hybrid classical–quantum fraud detection proof of concept.

---

## Strict Scientific Claim Firewall

> [!IMPORTANT]
> To eliminate unsubstantiated claims and marketing narratives, all findings are tagged with standardized scientific statuses:
> * `[VERIFIED]` - Tested and confirmed reproducible via automated tests and audit pipelines.
> * `[IMPLEMENTED]` - Complete operational code running in the repository.
> * `[MEASURED]` - Empirical metric extracted directly from structured experiment artifacts.
> * `[SYNTHETIC]` - Evaluated on a deterministic synthetic fixture mirroring IEEE-CIS schema.
> * `[BLOCKED]` - Prevented by external constraints (e.g. AWS Braket QPU access, Kaggle credentials).
> * `[INCONCLUSIVE]` - Difference from null hypothesis is not statistically significant ($p > 0.05$).

---

## 1. Executive Summary & Verified Verdict

*   **Real Data:** `[BLOCKED]` Real IEEE-CIS data is blocked pending credentials. All experiments currently operate strictly on `[SYNTHETIC]` fixtures.
*   **Predictive Quantum Advantage:** `[INCONCLUSIVE / NULL HYPOTHESIS UPHELD]`
    Across all evaluated escalation budgets ($B \in \{0.5\%, 1.0\%, 2.0\%, 5.0\%, 10.0\%\}$), the difference in full-system AUPRC between the Quantum Expert and a properly tuned Classical RBF Expert is statistically indistinguishable from zero ($\Delta \in [-0.0050, +0.0005]$, with $0$ inside the 95% bootstrap confidence interval in every case).
*   **Best Overall Performing Model:** Strong Classical Gradient Boosting (`ClassicalGBMExpert` trained on the escalated subset) achieved the highest full-system AUPRC ($0.3113$ at $10\%$ budget).
*   **Routing Validation:** Learned uncertainty routing outperforms random routing by up to $1.29\times$ in fraud capture rate, proving that selective escalation identifies higher-risk traffic, but this gain is a property of the router, not quantum computation.

---

## 2. Empirical Evidence Matrix (Full System Budget Sweep)

Evaluated across the full chronological test stream ($N=2,000$ transactions) with $1,000$ paired bootstrap resamples:

| Escalation Budget | Escalated Count | Classical Only AUPRC | Classical + RBF Expert | Classical + Quantum (FQK) | Classical + Strong GBM | Classical + Random Route | $\Delta(\text{Quantum} - \text{RBF})$ [95% CI] | Nominal $p$-value | Bonferroni $p$-value | Zero in 95% CI |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0.5%** | 10 | 0.3040 | 0.3036 | 0.3041 | **0.3042** | 0.3029 | $+0.0005$ $[-0.0005, +0.0023]$ | $0.6880$ | $1.0000$ | **Yes** |
| **1.0%** | 20 | 0.3040 | 0.3030 | 0.3033 | **0.3043** | 0.3011 | $+0.0004$ $[-0.0007, +0.0024]$ | $0.6100$ | $1.0000$ | **Yes** |
| **2.0%** | 40 | 0.3040 | 0.3050 | 0.3041 | 0.3044 | 0.3009 | $-0.0009$ $[-0.0056, +0.0036]$ | $0.7140$ | $1.0000$ | **Yes** |
| **5.0%** | 100 | 0.3040 | 0.3013 | 0.2997 | **0.3103** | 0.2975 | $-0.0015$ $[-0.0066, +0.0035]$ | $0.5260$ | $1.0000$ | **Yes** |
| **10.0%** | 200 | 0.3040 | 0.3023 | 0.2975 | **0.3113** | 0.3062 | $-0.0050$ $[-0.0129, +0.0020]$ | $0.1440$ | $0.7200$ | **Yes** |

*Artifact Source:* `data/results/budget_sweep_results.csv` and `docs/evidence/evidence_ledger.json`.

---

## 3. Architecture & Routing

```text
CARD-NOT-PRESENT TRANSACTION
            ↓
     CLASSICAL BASELINE (LightGBM)
            ↓
      ISOTONIC CALIBRATED SCORE
            ↓
     ESCALATION ROUTER (|p - 0.5|)
            ↓
     ┌──────┴──────────────────────────┐
     ↓                                 ↓
 NORMAL TRAFFIC (100-B)%        BORDERLINE HARD CASE (B%)
     ↓                                 ↓
 CLASSICAL DECISION            ┌───────┴───────┬───────────────┐
                               ↓               ↓               ↓
                            QUANTUM         CLASSICAL      STRONG GBM
                            EXPERT          RBF CONTROL     CONTROL
                               ↓               ↓               ↓
                               └───────┬───────┴───────────────┘
                                       ↓
                           PAIRED BOOTSTRAP TEST (N=1000)
                                       ↓
                             EVIDENCE LEDGER AUDIT
```

---

## 4. Key Scientific Audits

### Router Audit (Phase 23)
*   **Temporal Leakage:** Verified 0 leakage. Timestamps are strictly monotone ($T_{\text{train}} < T_{\text{calib}} < T_{\text{test}}$).
*   **Feature Dominance:** Escalation is dominated by `TransactionAmt` over `card1` by $> 5.2\times$.
*   **Covariate Shift:** Two-sample Kolmogorov-Smirnov test demonstrates significant shift on `TransactionAmt` ($p < 10^{-5}$ across all budgets).

### Temporal Robustness (Phase 26)
*   Random IID train/test splitting inflates test AUPRC by $+0.0131$ ($0.4078$ vs $0.3947$ in strict chronological test).
*   Strict chronological splitting is mandatory to prevent false optimism in fraud detection benchmarks.

### Quantum Kernel Diagnostics (Phase 28)
*   All Gram matrices verified Positive Semi-Definite (0 negative eigenvalues).
*   Kernel-Target Alignment (KTA): Projected Quantum Kernel achieved $0.2050$ vs Classical RBF $0.1820$ and Quantum Fidelity $0.1857$.
*   Effective Rank: Classical RBF ($10.51$) > Quantum Fidelity ($5.81$) > Projected Quantum ($5.13$).

---

## 5. Reproducibility & Commands

Run the complete pipeline from scratch:

```bash
# 1. Run unit and integration tests
pytest

# 2. Generate deterministic synthetic data fixture
python -m src.data.generate_synthetic

# 3. Perform strict chronological temporal split (70/10/20)
python -m src.data.make_dataset

# 4. Fit feature scalers strictly on training data
python -m src.features.build_features

# 5. Train and calibrate incumbent classical LightGBM
python -m src.models.classical.train_baseline

# 6. Execute independent router audit
python -m src.evaluation.router_audit

# 7. Run full routed system evaluation across all budgets (0.5% - 10%)
python -m src.evaluation.system_evaluator

# 8. Evaluate temporal robustness vs random IID splitting
python -m src.evaluation.temporal_robustness

# 9. Compute quantum kernel quality diagnostics (PSD, KTA, Effective Rank)
python -m src.evaluation.kernel_diagnostics

# 10. Compile master evidence ledger
python -m src.evaluation.evidence_ledger
```

---

## 6. Project Evidence Ledger

All empirical findings are tracked in `docs/evidence/EVIDENCE_LEDGER.md` and machine-readable `docs/evidence/evidence_ledger.json`.
No claims are made without associated artifacts, random seeds, and statistical confidence intervals.
