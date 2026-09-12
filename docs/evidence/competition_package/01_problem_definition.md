# 01 Problem Definition & Scientific Scope

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-PROBLEM-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Classification accuracy under class imbalance (AUPRC, AUROC, Brier Score, Latency). |

---

## Core Research Question
> **At what escalation budget, if any, does a quantum kernel expert improve the precision–recall tradeoff by more than a tuned classical expert occupying the same slot on temporally split real-world card-not-present transaction data?**

## Scientific Constraints & Firewalls
1. **Severe Imbalance:** Fraud rates in card-not-present (CNP) transactions range between 1% and 4% (tested benchmark: 3.5%).
2. **Strict Chronological Splitting:** Random train/test splits cause severe temporal leakage. All splits are strictly monotonic in `TransactionDT`.
3. **Selective Escalation Budget:** Real-time authorization SLAs (100–300ms) prevent escalating 100% of traffic. Hard escalation budgets ($B \in [0.5\%, 10\%]$) are enforced.
4. **Honest Null-Result Stance:** The primary objective is rigorous empirical evaluation; no quantum advantage was demonstrated or claimed.
