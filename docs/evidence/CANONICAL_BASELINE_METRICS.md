# Canonical Baseline Metrics Specification (Phase 130)
## Master Autonomous Scientific Loop — HSBC Quantum Fraud Detection

> **Status:** `[SYNTHETIC] [MEASURED] [VERIFIED]`  
> **Authority:** Phase 130 Metric Anomaly Resolution  
> **Model Artifact:** [`src/models/classical/lgbm_calibrated.joblib`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/src/models/classical/lgbm_calibrated.joblib)  
> **Evaluation Partition:** Test Split ($N=2,001$, chronologically holdout $T \in [2101217, 2591967]$)  

---

## 1. The Canonical Metric Specification

To eliminate ambiguity across reports, all baseline comparisons must cite the exact feature stream under evaluation:

| Metric Name | Canonical Primary Value | Secondary Comparison Value | Feature Representation | Model Status | Exact Meaning & Role |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Baseline PR-AUC (AUPRC)** | **0.3987** | $0.3040$ | **Raw Unscaled Features** (`TransactionAmt`, `card1`) | Calibrated LightGBM (Isotonic) | **The True Empirical Classical Hurdle.** Achieved when LightGBM evaluates features on the scale on which it was trained. |
| **Baseline ROC-AUC (AUROC)** | **0.5996** | $0.4833$ | **Raw Unscaled Features** (`TransactionAmt`, `card1`) | Calibrated LightGBM (Isotonic) | **The True Empirical Discrimination.** Demonstrates positive discrimination above random chance ($0.50$). |
| **Conservative Stream PR-AUC** | **0.3040** | $0.3987$ | **Standardized Features** ($\mu=0, \sigma=1$) | Calibrated LightGBM (Misaligned) | Baseline score within the unified standardized evaluation matrix in `full_system_evaluation.json`. Matches test base prevalence ($30.93\%$). |
| **Conservative Stream ROC-AUC** | **0.4833** | $0.5996$ | **Standardized Features** ($\mu=0, \sigma=1$) | Calibrated LightGBM (Misaligned) | Conservative reference in `budget_sweep_results.csv`. |
| **Legacy `0.8540` AUROC** | **PERMANENTLY DISCARDED** | N/A | In-sample / Uncommitted | Non-chronological Prototype | **Invalid.** Removed from all competition and ledger artifacts. |

---

## 2. Invariant Rules for Downstream Reporting
1. **Zero Cherry-Picking:** When reporting relative improvements ($\Delta$), always compare against the matched feature stream (e.g., compare standardized kernel models against standardized control baselines, or raw tree specialists against raw tree baselines).
2. **Prevalence Context:** Baseline PR-AUC ($0.3987$) provides $+0.0894$ lift over the synthetic test prevalence ($0.3093$).
3. **No Uncalibrated Comparison:** All probability scores are calibrated via isotonic regression on the dedicated calibration split ($N=999$) strictly prior to test evaluation.
