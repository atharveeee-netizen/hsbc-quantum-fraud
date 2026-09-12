# Research Status & Truth Document

> [!IMPORTANT]
> This document explicitly details the factual state of the HSBC Quantum Fraud repository to prevent any unsupported claims from bleeding into presentations or documentation.

## Current State of Evidence

### 1. Data Integrity
*   **Real Data:** `[BLOCKED]` Real IEEE-CIS data has NOT been acquired due to missing Kaggle credentials.
*   **Synthetic Data:** `[IMPLEMENTED]` The pipeline currently operates *exclusively* on a generated `[SYNTHETIC]` smoke-test fixture.
*   **Temporal Leakage:** `[VERIFIED]` The pipeline guarantees strict chronological splitting (`TransactionDT`), successfully avoiding the random CV leakage common in fraud benchmarks.

### 2. Classical Stack
*   **LightGBM Baseline:** `[IMPLEMENTED]` The incumbent pipeline exists and correctly implements Isotonic Calibration on a dedicated calibration window.
*   **Classical RBF Control:** `[IMPLEMENTED]` An RBF Kernel Support Vector Machine is implemented as the classical analogue to the projected quantum kernel.

### 3. Quantum Implementations
*   **Projected Quantum Kernel:** `[PLANNED]` Feature selection, quantum feature map (e.g., `ZZFeatureMap`), and kernel compilation are pending implementation.
*   **Quantum Autoencoder (QAE):** `[PLANNED]` Only to be implemented if analytically justified.
*   **Simulator Execution:** `[PLANNED]` Not yet executed.
*   **Hardware Execution:** `[PLANNED]` `[BLOCKED]` AWS Braket QPU credentials required.

### 4. Routing & Architecture
*   **Escalation Router:** `[VERIFIED]` The router successfully routes traffic based on calibration uncertainty. Budget sweep methodology is conceptually `[PLANNED]`.

### 5. Claims
*   **Quantum Advantage:** `[INCONCLUSIVE]` No quantum advantage of any type (predictive, computational, economic, operational) has been demonstrated. The null hypothesis stands.
