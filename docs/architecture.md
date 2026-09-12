# System Architecture

The project strictly separates the pipeline into deterministic stages to guarantee reproducibility, prevent temporal data leakage, and ensure a rigorous, fair apples-to-apples comparison between Classical Experts and Quantum Experts under identical selective routing budgets.

## 1. End-to-End Scientific Architecture

```mermaid
graph TD
    classDef data fill:#f0f4f8,stroke:#091e42,stroke-width:2px,color:#091e42
    classDef classical fill:#fff0b3,stroke:#ff8b00,stroke-width:2px,color:#091e42
    classDef router fill:#e1cceb,stroke:#5243aa,stroke-width:2px,color:#5243aa
    classDef quantum fill:#e3fcef,stroke:#006644,stroke-width:2px,color:#006644
    classDef evaluation fill:#deebff,stroke:#0052cc,stroke-width:2px,color:#091e42

    D1["Raw Transaction Stream"]:::data --> D2["Temporal Split\nStrict Chronological (TransactionDT)"]:::data
    D2 --> D3["Feature Engineering\nScaler fitted strictly on Train"]:::data
    
    D3 --> C1["Classical Incumbent\nLightGBM"]:::classical
    C1 --> C2["Isotonic Calibration\nDedicated Calib Window"]:::classical
    
    C2 --> R1{"Escalation Router\nUncertainty |p - 0.5|"}:::router
    
    R1 -- "Cleared (100 - B)%" --> S_CLR["Calibrated Base Score"]:::classical
    
    R1 -- "Escalated B% Traffic" --> EXP_FORK{"Identical Escalated Traffic"}:::router
    EXP_FORK --> Q1["Quantum Expert\nFQK / Projected Kernel + SVC"]:::quantum
    EXP_FORK --> C3["Classical Control 1\nRBF SVC (CV-Tuned on Train)"]:::classical
    EXP_FORK --> C4["Classical Control 2\nStrong GBM Expert"]:::classical
    
    R1 -- "Uniform Random Sample B%" --> RND["Random Router Control\nRBF on Random Traffic"]:::classical
    
    S_CLR --> S1["Full-System Combined Prediction Stream"]:::evaluation
    Q1 --> S1
    C3 --> S1
    C4 --> S1
    RND --> S1
    
    S1 --> V1["Full-System Evaluation\nAUPRC / ROC-AUC / Confusion Matrix"]:::evaluation
    V1 --> V2["Paired Bootstrap (N=1000)\nΔ Metric, 95% CI, p-value"]:::evaluation
    V2 --> V3["Multiple Comparison Discipline\nBonferroni & Benjamini-Hochberg FDR"]:::evaluation
    V3 --> V4["Master Evidence Ledger\ndocs/evidence/evidence_ledger.json"]:::evaluation
```

## 2. Directory and Module Organization

1.  **Data Ingestion & Splitting (`src/data/`):**
    *   `generate_synthetic.py`: Deterministic synthetic generator matching IEEE-CIS tabular schema.
    *   `make_dataset.py`: Kaggle API acquisition interface and strict chronological temporal splitter.
2.  **Feature Pipeline (`src/features/`):**
    *   `build_features.py`: `StandardScaler` fitted exclusively on historical training data to eliminate test set contamination.
3.  **Base Classical Model (`src/models/classical/`):**
    *   `train_baseline.py`: LightGBM base classifier with Isotonic probability calibration.
4.  **Escalation Router (`src/models/router/`):**
    *   `escalation_router.py`: Quantifies boundary uncertainty $|p - 0.5|$, routes top $B\%$ ambiguous traffic, implements random-routing control baseline.
5.  **Specialist Experts (`src/models/experts/`):**
    *   `quantum_expert.py`: Quantum Expert using PennyLane exact fidelity kernel or 1-qubit Pauli expectation projected kernel (PQK) + scikit-learn `SVC(kernel='precomputed')`.
    *   `classical_rbf_expert.py`: Classical `SVC(kernel='rbf')` with automated 3-fold cross-validation tuning strictly on training escalated traffic.
    *   `classical_gbm_expert.py`: Strong non-linear `LGBMClassifier` trained specifically on ambiguous boundary transactions.
6.  **Quantum Kernel Mechanics (`src/models/quantum/`):**
    *   `feature_encoding.py`: Arctan angle scaling into $[-\pi, \pi]$ and $N$-qubit entangling circuits.
    *   `projected_kernel.py`: Statevector overlap computation and 1-qubit reduced Pauli expectation extraction.
7.  **Scientific Evaluation & Statistical Audit (`src/evaluation/`):**
    *   `system_evaluator.py`: Complete full-system evaluation across budgets $B \in \{0.5, 1, 2, 5, 10\}\%$, 1,000 paired bootstrap iterations, and FDR / Bonferroni multiple testing corrections.
    *   `router_audit.py`: Independent router audit (covariate shift KS-tests, feature dominance, uncertainty vs fraud correlation, future information checks).
    *   `temporal_robustness.py`: Compares chronological evaluation vs random IID evaluation to quantify temporal leakage inflation.
    *   `kernel_diagnostics.py`: Computes PSD eigenvalues, condition number, effective rank, and Kernel-Target Alignment (KTA).
    *   `evidence_ledger.py`: Master ledger compiler enforcing claim-to-artifact mapping.

## 3. Strict Scientific Controls Enforced

*   **Identical Escalation Slices:** Every expert evaluates the exact same transaction IDs under each budget.
*   **Leakage Firewall:** Feature scalers, baseline models, and expert hyperparameters are fitted strictly inside chronological training boundaries.
*   **Paired Bootstrap:** Bootstrap iterations draw identical sample index permutations for all competing models.
*   **No Cherry-Picking:** All 5 budgets are evaluated and reported in tabular evidence ledgers.
