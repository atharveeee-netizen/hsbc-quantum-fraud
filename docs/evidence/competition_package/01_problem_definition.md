# 01 Problem Definition & Scientific Scope

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-PROBLEM-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `9857a2a` |
| **Metric Definition** | Classification accuracy under class imbalance (AUPRC, AUROC, Precision, Recall). |

---

## Core Research Question
> **At what escalation budget, if any, does a quantum expert improve the precision–recall tradeoff by more than a tuned classical expert occupying the same slot on temporally split card-not-present transaction data?**

## Scientific Constraints & Firewalls
1. **Severe Imbalance:** Fraud rates in card-not-present (CNP) transactions range between 1% and 4% (tested benchmark: 3.5%).
2. **Strict Chronological Splitting:** Random train/test splits cause severe temporal leakage. All splits are strictly monotonic in `TransactionDT`.
3. **Selective Escalation Budget:** Real-time authorization SLAs (100–300ms) prevent escalating 100% of traffic. Hard escalation budgets ($B \in [0.5\%, 10\%]$) are enforced.
4. **Honest Null-Result Stance:** The goal is honest scientific falsification; no quantum advantage was demonstrated or claimed.
