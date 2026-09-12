# Proposal Number Lock: Single Source of Verifiable Metrics

**Project:** HSBC Challenge — Selective Quantum-Enhanced Credit Card Fraud Detection  
**Repository:** `https://github.com/atharveeee-netizen/hsbc-quantum-fraud`  
**Protocol Version:** `vNEXT.3`  
**Date:** September 2026  
**Status:** `FROZEN & VERIFIED`

This document establishes the single source of truth for every quantitative metric appearing in the Phase 1 Concept Proposal, Supplementary Material, and competition exhibits. Any metric not appearing in this table or deviating from allowed phrasing is strictly prohibited.

---

## 1. Metric Inventory and Provenance Mapping

| Metric ID | Numeric Value | Description | Source Artifact | Dataset / Support | Partition / Split | Provenance Status | Allowed Wording | Forbidden Wording |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **NL-01** | `590,540` | Total transaction records | `real_data_ingestion.json` | IEEE-CIS Fraud Benchmark | Full benchmark | `[REAL DATA] [MEASURED]` | "590,540 benchmark transactions" | "590,540 HSBC client records" |
| **NL-02** | `20,663` | Total fraud records | `real_class_imbalance_audit.json` | IEEE-CIS Fraud Benchmark | Full benchmark | `[REAL DATA] [MEASURED]` | "20,663 fraudulent transactions" | "20,663 confirmed HSBC frauds" |
| **NL-03** | `3.4990%` | Population fraud prevalence | `real_class_imbalance_audit.json` | IEEE-CIS Fraud Benchmark | Full benchmark | `[REAL DATA] [MEASURED]` | "3.50% base fraud prevalence (1 in 27.5 transactions)" | "3.50% HSBC fraud rate" |
| **NL-04** | `394` | Ingested feature count | `real_data_schema.json` | IEEE-CIS Fraud Benchmark | Full benchmark | `[REAL DATA] [MEASURED]` | "394 raw transaction attributes" | "394 proprietary banking fields" |
| **NL-05** | `383,851` | Training set size | `real_temporal_split.json` | IEEE-CIS Fraud Benchmark | Days 1.0 to 111.3 (65%) | `[REAL DATA] [MEASURED]` | "383,851 chronologically ordered training transactions" | "383,851 randomly sampled transactions" |
| **NL-06** | `88,581` | Calibration set size | `real_temporal_split.json` | IEEE-CIS Fraud Benchmark | Days 111.3 to 141.1 (15%) | `[REAL DATA] [MEASURED]` | "88,581 chronologically subsequent calibration transactions" | "88,581 cross-validation folds" |
| **NL-07** | `118,108` | Test set size | `real_temporal_split.json` | IEEE-CIS Fraud Benchmark | Days 141.1 to 183.0 (20%) | `[REAL DATA] [MEASURED]` | "118,108 strictly out-of-sample forward test transactions" | "118,108 shuffled test transactions" |
| **NL-08** | `0.0344` | Test set fraud prevalence | `real_classical_baseline.json` | IEEE-CIS Fraud Benchmark | Test (Days 141-183) | `[REAL DATA] [MEASURED]` | "3.44% test set prevalence (4,064 frauds)" | "3.44% production fraud rate" |
| **NL-09** | `0.4040` | Frontline LightGBM PR-AUC | `real_classical_baseline.json` | IEEE-CIS Fraud Benchmark | Test (118,108 tx) | `[REAL DATA] [MEASURED]` | "PR-AUC of 0.4040 (11.74x lift over test prevalence)" | "World-leading 0.4040 accuracy" |
| **NL-10** | `0.8503` | Frontline LightGBM ROC-AUC | `real_classical_baseline.json` | IEEE-CIS Fraud Benchmark | Test (118,108 tx) | `[REAL DATA] [MEASURED]` | "ROC-AUC of 0.8503 on out-of-sample test stream" | "Flawless discrimination" |
| **NL-11** | `0.0250` | Frontline Brier Score Loss | `real_calibration_audit.json` | IEEE-CIS Fraud Benchmark | Test (118,108 tx) | `[REAL DATA] [MEASURED]` | "Brier score loss of 0.0250 after isotonic calibration" | "Zero calibration error" |
| **NL-12** | `0.0785` | Frontline ECE | `real_calibration_audit.json` | IEEE-CIS Fraud Benchmark | Test (118,108 tx) | `[REAL DATA] [MEASURED]` | "Expected Calibration Error of 0.0785" | "Perfect probability calibration" |
| **NL-13** | `42.81%` | Router 0.5% fraud density | `real_router_audit.json` | IEEE-CIS Fraud Benchmark | Test (591 escalated) | `[REAL DATA] [MEASURED]` | "42.81% fraud density (12.44x enrichment over base rate)" | "42.81% fraud elimination" |
| **NL-14** | `253` | Router 0.5% fraud count | `real_router_audit.json` | IEEE-CIS Fraud Benchmark | Test (591 escalated) | `[REAL DATA] [MEASURED]` | "253 frauds captured within a 0.5% review budget" | "253 frauds prevented in live banking" |
| **NL-15** | `37.26%` | Router 1.0% fraud density | `real_router_audit.json` | IEEE-CIS Fraud Benchmark | Test (1,181 escalated) | `[REAL DATA] [MEASURED]` | "37.26% fraud density (10.83x enrichment, 440 frauds)" | "37.26% bank savings" |
| **NL-16** | `30.48%` | Router 2.0% fraud density | `real_router_audit.json` | IEEE-CIS Fraud Benchmark | Test (2,362 escalated) | `[REAL DATA] [MEASURED]` | "30.48% fraud density (8.86x enrichment, 720 frauds)" | "30.48% accuracy" |
| **NL-17** | `26.40%` | Router 5.0% fraud density | `real_router_audit.json` | IEEE-CIS Fraud Benchmark | Test (5,905 escalated) | `[REAL DATA] [MEASURED]` | "26.40% fraud density (7.67x enrichment, 1,559 frauds)" | "26.40% capture rate" |
| **NL-18** | `28.1x` | Router ablation vs Amount (0.5%) | `real_router_ablation.json` | IEEE-CIS Fraud Benchmark | Test (591 escalated) | `[REAL DATA] [MEASURED]` | "captures 28.1x more fraud than sorting by transaction amount alone" | "claiming transaction amount causally drives fraud" |
| **NL-19** | `0.3367` | Classical RBF PR-AUC | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "PR-AUC of 0.3367 for tuned Classical RBF baseline" | "Weak classical baseline" |
| **NL-20** | `0.3516` | Classical MLP PR-AUC | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "PR-AUC of 0.3516 for 2-layer MLP control" | "Deep learning benchmark" |
| **NL-21** | `0.3529` | Classical GBM PR-AUC | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "PR-AUC of 0.3529 for gradient-boosted control" | "Classical tree failure" |
| **NL-22** | `0.3789` | Quantum Fidelity Kernel PR-AUC | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "PR-AUC of 0.3789 for Quantum Fidelity Kernel" | "Quantum Fidelity victory" |
| **NL-23** | `0.4043` | Projected Quantum Kernel PR-AUC | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "nominal PR-AUC of 0.4043 for Projected Quantum Kernel" | "Unqualified claims of quantum victory or superiority" |
| **NL-24** | `+0.0653` | Point estimate delta (PQK - RBF) | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "nominal point-estimate delta of +0.0653" | "Statistically significant quantum margin" |
| **NL-25** | `[-0.0383, +0.1821]` | 95% Bootstrap CI (PQK - RBF) | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | 1,000 paired resamples | `[REAL DATA] [MEASURED]` | "95% bootstrap confidence interval spans zero: [-0.0383, +0.1821]" | "Significant positive gain" |
| **NL-26** | `p = 0.246` | Hypothesis test p-value | `real_quantum_matched_experiment.json` | IEEE-CIS Escalated Support | 1,000 paired resamples | `[REAL DATA] [MEASURED]` | "p = 0.246 (Bonferroni p = 0.492); null hypothesis not rejected" | "Unqualified claim of quantum advantage" |
| **NL-27** | `0.9337` | CKA (PQK vs Classical RBF) | `real_quantum_geometry.json` | IEEE-CIS Escalated Support | Matched N=200 | `[REAL DATA] [MEASURED]` | "Centered Kernel Alignment of 0.9337, showing strong geometric alignment" | "Proves quantum and classical equivalence" |
| **NL-28** | `-1.32% to -6.49%` | Quantum noise degradation | `real_noise_robustness.json` | Simulated Noisy Channel | Phase-damping & Depol | `[MEASURED]` | "PR-AUC degrades by -1.32% to -6.49% under 1% to 5% noise" | "Noise immune quantum circuit" |
| **NL-29** | `4.07 ms` / `4.97 ms` | Classical fast path latency | `real_latency_audit.json` | Local Benchmark (x86_64) | 1,000 real transactions | `[REAL DATA] [MEASURED]` | "4.07 ms median and 4.97 ms p95 end-to-end fast-path latency" | "0.7 microsecond production SLA" |
| **NL-30** | `4.89 ms` / `5.45 ms` | Classical escalated latency | `real_latency_audit.json` | Local Benchmark (x86_64) | 1,000 real transactions | `[REAL DATA] [MEASURED]` | "4.89 ms median and 5.45 ms p95 escalated classical latency" | "Instantaneous dual clearance" |
| **NL-31** | `159.14 ms` / `217.18 ms` | Quantum simulator latency | `real_latency_audit.json` | Local PennyLane (x86_64) | 1,000 real transactions | `[REAL DATA] [MEASURED]` | "159.14 ms median and 217.18 ms p95 simulation latency" | "Sub-50ms quantum clearance" |
| **NL-32** | `180 s` / `1,200 s` | Modeled cloud QPU queue | `real_latency_audit.json` | AWS Braket / IonQ Aria | Modeled distribution | `[MODELED]` | "modeled 180 s median to 1,200 s p95 cloud QPU queue latency" | "Measured QPU hardware latency" |
| **NL-33** | `50 ms` | Design latency budget | Architecture Specification | System Design Goal | Project Standard | `[ASSUMED]` | "the project's 50 ms design budget" | "HSBC's contractual SLA" |
| **NL-34** | `$0.00` | Realized expenditure savings | `ECONOMIC_AUDIT.md` | Research Benchmark | Operational Status | `[VERIFIED]` | "$0.00 realized monetary savings to date" | "€1.2M realized banking savings" |
| **NL-35** | `$0.50` | Modeled frontline compute / 1M | `hardware_and_economics.json` | Cloud VM Pricing | 1M transactions | `[MODELED]` | "modeled $0.50 per 1 million transactions for frontline LightGBM" | "Audited HSBC operational cost" |
| **NL-36** | `$0.65` | Modeled selective compute / 1M | `hardware_and_economics.json` | Cloud VM Pricing | 1M tx (1% escalated) | `[MODELED]` | "modeled $0.65 per 1 million transactions for selective classical" | "Audited HSBC operational cost" |
| **NL-37** | `$353,000.50` | Modeled QPU compute / 1M | `hardware_and_economics.json` | IonQ via AWS Braket | 1M tx (1% escalated) | `[MODELED]` | "modeled $353,000.50 per 1M transactions ($35.30 per escalated tx)" | "Incurred cloud invoice" |
| **NL-38** | `Outcome B` | Master Scientific Verdict | `RESEARCH_VERDICT.md` | Complete Evidence Suite | Multi-phase synthesis | `[VERIFIED]` | "Outcome B: No quantum advantage demonstrated, but useful selective classical architecture validated" | "Outcome A: Quantum advantage demonstrated" |
| **NL-39** | `HARDWARE NOT JUSTIFIED` | Physical QPU Hardware Gate | `hardware_gate.json` | Decision Protocol | Protocol Evaluation | `[VERIFIED]` | "hardware execution is currently not justified" | "Physical QPU validated in production" |

---

## 2. Enforcement Rule
Every number appearing in `proposal/HSBC_Phase1_Concept_Proposal.pdf`, `proposal/HSBC_Phase1_Concept_Proposal.docx`, and related markdown documents must strictly match an ID above. No ad-hoc, approximate, or untraced quantitative figures are permitted.
