# Phase 1: Research & Discovery Findings

## 1. Challenge Requirements
- **Goal:** Identify innovative, feasible, and impactful approaches to real-world problems using quantum computing, quantum-inspired methods, or quantum-AI hybrid workflows.
- **Problem Statement:** HSBC, Quantum-Enhanced Credit Card Fraud Detection for Digital Payment Ecosystems.
- **Core Constraints:** Cannot assume quantum advantage. Must test the precision-recall tradeoff of escalating traffic to a quantum expert vs a classical expert under the exact same computational budget.

## 2. Evaluation Criteria
- **Metrics:** Area Under the Precision-Recall Curve (AUPRC) as primary. Precision at fixed recall. Expected cost per 10,000 transactions.
- **Split:** Strict Temporal validation (preventing data leakage across time).
- **Control:** 
  - Tuned RBF Kernel.
  - Random router at identical budget $B$.
  - Classical expert (MLP/GBM) in the quantum slot.
- **Falsification:** Compute the geometric difference $g(K_C, K_Q)$ to verify if advantage is provably available.

## 3. Relevant Datasets
- **Primary:** IEEE-CIS Fraud Detection. Features `TransactionDT` which permits a genuine temporal split.
- **Secondary (Stress Test):** European Cardholder (ULB). Highly imbalanced (0.172%).

## 4. Current Fraud-Detection Literature (Selected)
- **Dal Pozzolo et al. (2015):** Recommends AUPRC for highly unbalanced datasets.
- **LexisNexis Risk Solutions (2024):** True Cost of Fraud Study — $4.41 of cost per $1 of fraud.
- **Kyriienko & Magnusson (2022):** Reported >10% AP over RBF, but used a rebalanced subset (500 samples, 25 frauds). *Our project challenges this standard.*
- **Chaves et al. (2026):** Routed hybrid AP 0.793 vs XGBoost 0.770 on threshold-selected subset. The most honest benchmark to date.

## 5. Temporal Validation Practices
- Random K-Fold CV is highly discouraged as it leaks future behavioral patterns into the training set, artificially inflating AUPRC.
- We must sort the IEEE-CIS dataset by `TransactionDT` and split: 70% Train, 10% Calibration, 20% Test chronologically.

## 6. Open Questions / Next Steps
- We need to formulate the specific architecture pipeline for the router in Phase 2.
- The Data Engineering agent (Phase 3) needs to implement a deterministic pipeline to download the IEEE-CIS dataset from Kaggle and execute the temporal split.
