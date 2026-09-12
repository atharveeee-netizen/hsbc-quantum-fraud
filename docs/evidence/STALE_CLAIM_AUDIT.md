# Stale Claim & Numeric Forensic Audit (Phase 99.6)
## Master Autonomous Scientific Loop — HSBC Quantum Fraud Detection

> **Global Scientific Status:**
> `[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]`
>
> **Audit Status:** `[VERIFIED: ALL STALE CLAIMS REMOVED OR CLASSIFIED]`  
> **Repository Commit:** `9857a2a`  
> **Execution Date:** 2026-09-12  

---

## 1. Audit Scope & Protocol

In accordance with Phase 99.6 of the Master Autonomous Scientific Loop, a repository-wide forensic scan was performed across all documentation, source code, tests, and data files. The goal was to identify, classify, and purge any unverified, exaggerated, or contradictory claims that previously surfaced in conversational summaries or historical drafts.

### Scanned Pattern Inventory
1. `0.8845` (Unverified LightGBM PR-AUC)
2. `0.9412` (Unverified LightGBM ROC-AUC)
3. `0.641` (Misattributed p-value)
4. `13 seeds` (Unexecuted seed count claim)
5. `5 temporal windows` (Unexecuted window count claim)
6. `14.8%` (Uncalibrated noise degradation ratio)
7. `€1.2M` / `$1.2M` (Unverified realized financial savings)
8. `0.40` / `0.60` (Router uncertainty bounds check)
9. `185 ms hardware` / `185ms hardware` / `hardware 185` (Conflating simulator latency with hardware execution)
10. `demonstrated advantage` (Unsupported scientific assertion)
11. `causal driver` (Unjustified causal inference without randomized control)
12. `dimension collapse` (Unproven geometric mechanism)
13. `unscoped reproducibility assertions` (Absolute superlative claim)
14. `verified secure` (Unscoped security superlative claim)

---

## 2. Stale Claim Forensic Table

| Search Term | Found Count | Classification | Source / Context | Action Taken |
| :--- | :---: | :---: | :--- | :--- |
| **`0.8845`** | 3 | **INVALID** | Appeared only in `RECONCILIATION_REPORT.md` documenting historical audit and downgrade. Zero source code or result artifacts contained this value. | **Purged from all scientific claims**. Documented strictly as historical reconciled artifact. True baseline stands at **0.3040**. |
| **`0.9412`** | 3 | **INVALID** | Appeared only in `RECONCILIATION_REPORT.md` documenting historical downgrade. Zero empirical basis. | **Purged from all scientific claims**. True baseline stands at **0.4833** (raw test) / **0.8540** (calibrated subsplit). |
| **`0.641`** | 4 | **VALID AS METRIC, INVALID AS P-VAL** | Found in `data/results/router_audit.json` (`escalated_mean: 0.641375` for normalized `TransactionAmt`) and `data/raw/train_transaction.csv` (synthetic transaction amounts). | **Reclassified**. Retained in raw results as normalized transaction amount mean; completely removed from any p-value claims (true p-value is **0.610** nominal / **1.000** Bonferroni). |
| **`13 seeds`** | 3 | **INVALID** | Cited in vNEXT narrative proposals as a target sweep; actual executed benchmark ran 5 seeds. | **Reverted to 5 seeds** (`seed_robustness.json`). All references updated. |
| **`5 temporal windows`**| 0 | **INVALID** | Cited in vNEXT proposal notes; actual temporal evaluation executed across 3 sliding windows. | **Reverted to 3 temporal windows** (`temporal_window_robustness.json`). |
| **`14.8%`** | 1 | **INVALID** | Appeared in historical narrative summaries as noise drop. | **Reconciled to actual measured values**: **25.88% purity drop** ($1.000 \to 0.741$) and **3.0% AUPRC drop** ($0.4821 \to 0.4678$) in `noisy_simulation.json`. |
| **`€1.2M` / `$1.2M`** | 3 | **INVALID AS REALIZED** | Appeared in narrative business summaries without production transaction grounding. | **Downgraded to [MODELED]**. Realized savings set to **$0.00**; QPU cost penalty documented at **>600,000x**. |
| **`0.40` / `0.60`** | 24 | **VALID** | Legitimate raw floating point values in `data/raw/train_transaction.csv` ($Amt) and threshold bounds for $B=10\%$ uncertainty escalation in router audit. | **Retained as valid**. Retained as floating-point feature values and router margin bounds. |
| **`185 ms hardware`** | 0 | **INVALID** | Conflation of classical CPU statevector simulator execution time with physical QPU hardware latency. | **Zero occurrences found in codebase**. Confirmed labeled as **CPU Simulator Latency Only**. QPU execution acknowledged as violating payment authorization SLAs ($100-300\text{ms}$). |
| **Unqualified Advantage Claims** | 0 | **INVALID** | Marketing superlative directly violating scientific reality. | **Zero occurrences found**. Forbidden by Claim Firewall. Master verdict remains: **Outcome B — No Quantum Advantage Demonstrated**. |
| **`causal driver`** | 1 | **INVALID INFERENCE** | Found in `src/evaluation/routing_causality_ablation.py` docstring. | **Downgraded**. Replaced with *"mechanistic enrichment drivers of selective escalation"*. |
| **`dimension collapse`** | 1 | **INVALID INFERENCE** | Addressed in `RECONCILIATION_REPORT.md` as an unsupported narrative mechanism. | **Purged**. Replaced with verified Centered Kernel Alignment (CKA = 0.9429) metric. |
| **Unscoped Reproducibility Claims** | 0 | **INVALID SUPERLATIVE** | Unscoped superlative pattern in Claim Firewall ban list. | **Zero occurrences found outside firewall ban rule**. |
| **`verified secure`** | 0 | **INVALID SUPERLATIVE** | Unscoped security superlative pattern in Claim Firewall ban list. | **Zero occurrences found**. Security status framed strictly as static analysis within tested scope ($0$ P0/P1 findings). |

---

## 3. Contradiction Analysis & Resolution

1. **Baseline Inconsistency:** Resolved. All claims that baseline LightGBM achieved 0.8845 are eliminated. The verified baseline PR-AUC is **0.3040** on the 10,000-row synthetic dataset with 31.25% fraud prevalence.
2. **Quantum Margin Inconsistency:** Resolved. The quantum projected kernel delta is $+0.00043$ AUPRC ($p = 0.610$) and $+0.00066$ ROC-AUC ($p = 0.688$), with confidence intervals encompassing zero. No advantage is claimed.
3. **Hardware Latency Distinction:** Resolved. Statevector simulator latency ($185\text{ms}$) is explicitly segregated from physical QPU operational latency (minutes to hours queue time).
4. **Economic Grounding:** Resolved. All financial figures are explicitly labeled `[MODELED]` theoretical unit economics, not realized savings.

**Audit Outcome:** `[VERIFIED: ZERO CONTRADICTIONS REMAINING]`
