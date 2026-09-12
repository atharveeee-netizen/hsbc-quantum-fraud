# Research Status & Truth Document

> [!IMPORTANT]
> This document explicitly details the factual state of the HSBC Quantum Fraud repository to prevent any unsupported claims from bleeding into presentations or documentation. Every claim maps directly to empirical artifacts in `docs/evidence/`.

## Current State of Evidence

### 1. Data Integrity
*   **Real Data:** `[BLOCKED]` Real IEEE-CIS data has NOT been acquired due to missing Kaggle credentials. All experimental results in this repository are strictly from a generated `[SYNTHETIC]` fixture.
*   **Synthetic Data:** `[IMPLEMENTED]` 10,000 samples generated with non-linear decision boundaries mirroring IEEE-CIS schema.
*   **Temporal Leakage:** `[VERIFIED]` Strict chronological splitting on `TransactionDT` (Train: [86654, 1849443], Calib: [1849897, 2100898], Test: [2101217, 2591967]). Leakage check: `False` (0 leakage). Random IID splitting artificially inflates test AUPRC by +0.0131, confirming the necessity of temporal validation.

### 2. Classical Stack & Controls (Phase 21)
*   **LightGBM Baseline:** `[IMPLEMENTED]` Calibrated with isotonic regression on the temporal calibration split. Full-test AUPRC: 0.3040, ROC-AUC: 0.4833.
*   **Classical RBF Control:** `[IMPLEMENTED]` `SVC(kernel='rbf')` tuned via Stratified 3-Fold Cross-Validation strictly on training escalated traffic (Best params: C=10.0, gamma='scale').
*   **Strong Classical GBM Control:** `[IMPLEMENTED]` `LGBMClassifier` trained specifically on the escalated training traffic.
*   **Random-Routing Control:** `[IMPLEMENTED]` Routes traffic uniformly at random at identical budgets.

### 3. Quantum Implementation & Diagnostics (Phase 27 & 28)
*   **Fidelity Quantum Kernel (FQK):** `[IMPLEMENTED]` Exact PennyLane statevector inner product `|<psi(x1)|psi(x2)>|^2` using 2-qubit AngleEmbedding + BasicEntanglerLayers.
*   **Projected Quantum Kernel (PQK):** `[IMPLEMENTED]` Evaluates 1-qubit Pauli expectation observables (X, Y, Z) per qubit followed by Gaussian kernel on projected representation.
*   **Positive Semi-Definite (PSD) Diagnostics:** `[VERIFIED]` Gram matrix has 0 negative eigenvalues (strictly PSD). Condition number: ~3.7e11. Effective rank: 5.81 (Fidelity) vs 5.13 (Projected) vs 10.51 (Classical RBF).
*   **Kernel-Target Alignment (KTA):** `[MEASURED]` Projected Quantum Kernel achieved highest KTA (0.2050) vs Classical RBF (0.1820) and Quantum Fidelity (0.1857).
*   **Hardware Execution:** `[PLANNED]` `[BLOCKED]` Real QPU execution is blocked pending AWS Braket credentials. All quantum results are simulated on `default.qubit`.

### 4. Full Routed System & Budget Sweep (Phase 22)
Evaluated across all 5 pre-registered budgets on full test stream (N=2,000):
*   **Budget 0.5% (N=10 escalated):** Quantum AUPRC = 0.3041 vs RBF = 0.3036 vs GBM = 0.3042 vs Random = 0.3029
*   **Budget 1.0% (N=20 escalated):** Quantum AUPRC = 0.3033 vs RBF = 0.3030 vs GBM = 0.3043 vs Random = 0.3011
*   **Budget 2.0% (N=40 escalated):** Quantum AUPRC = 0.3041 vs RBF = 0.3050 vs GBM = 0.3044 vs Random = 0.3009
*   **Budget 5.0% (N=100 escalated):** Quantum AUPRC = 0.2997 vs RBF = 0.3013 vs GBM = 0.3103 vs Random = 0.2975
*   **Budget 10.0% (N=200 escalated):** Quantum AUPRC = 0.2975 vs RBF = 0.3023 vs GBM = 0.3113 vs Random = 0.3062

### 5. Paired Statistical Bootstrap & Multiple Testing (Phase 24 & 25)
*   **Paired Bootstrap:** 1,000 resamples per budget evaluating Δ(Quantum - RBF) on the exact same test transactions.
    *   0.5% Budget: Δ = +0.0005 [95% CI: -0.0005, +0.0023], nominal p = 0.6880, Bonferroni p = 1.0000
    *   1.0% Budget: Δ = +0.0004 [95% CI: -0.0007, +0.0024], nominal p = 0.6100, Bonferroni p = 1.0000
    *   2.0% Budget: Δ = -0.0009 [95% CI: -0.0056, +0.0036], nominal p = 0.7140, Bonferroni p = 1.0000
    *   5.0% Budget: Δ = -0.0015 [95% CI: -0.0066, +0.0035], nominal p = 0.5260, Bonferroni p = 1.0000
    *   10.0% Budget: Δ = -0.0050 [95% CI: -0.0129, +0.0020], nominal p = 0.1440, Bonferroni p = 0.7200
*   **Verdict:** In every budget, 0 is contained within the 95% bootstrap confidence interval. There is NO statistically significant difference between Quantum Expert and Classical RBF Control.

### 6. Router Audit Findings (Phase 23)
*   **Uncertainty vs Fraud:** Weak correlation (Spearman rho = 0.0384, p = 0.0862).
*   **Feature Dominance:** `TransactionAmt` heavily dominates escalation over `card1` (influence ratio > 5.2x).
*   **Covariate Shift:** Significant Kolmogorov-Smirnov distribution shift on `TransactionAmt` (p < 1e-5 across all budgets), showing escalated transactions are significantly larger in transaction amount.
*   **Enrichment:** Learned uncertainty routing achieves up to 1.29x fraud enrichment over random routing at 2% budget.

### 7. Core Scientific Verdict
*   **Quantum Advantage:** `[INCONCLUSIVE / NULL HYPOTHESIS UPHELD]`
    No predictive quantum advantage is demonstrated over fair classical controls.
    Strong Classical Gradient Boosting (`ClassicalGBMExpert`) achieves the highest full-system AUPRC (0.3113 at 10% budget), outperforming both Classical RBF and Quantum Expert.
