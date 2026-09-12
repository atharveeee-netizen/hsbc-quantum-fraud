# System Architecture

The project explicitly separates the pipeline into deterministic stages to guarantee reproducibility, prevent temporal data leakage, and ensure an apples-to-apples comparison between the Classical Expert and the Quantum Expert.

## Architecture Flow

```mermaid
graph TD
    classDef data fill:#f0f4f8,stroke:#091e42,stroke-width:2px,color:#091e42
    classDef classical fill:#fff0b3,stroke:#ff8b00,stroke-width:2px,color:#091e42
    classDef router fill:#e1cceb,stroke:#5243aa,stroke-width:2px,color:#5243aa
    classDef quantum fill:#e3fcef,stroke:#006644,stroke-width:2px,color:#006644
    classDef evaluation fill:#deebff,stroke:#0052cc,stroke-width:2px,color:#091e42
    classDef ui fill:#eae6ff,stroke:#403294,stroke-width:2px,color:#091e42

    D1[Raw Transaction Data]:::data --> D2[Data Validation]:::data
    D2 --> D3[Temporal Split\n70/10/20]:::data
    D3 --> D4[Feature Engineering]:::data
    
    D4 --> C1(Classical Incumbent\nLightGBM):::classical
    C1 --> C2(Calibration\nIsotonic):::classical
    
    C2 --> R1{Escalation Router\nBudget Sweep B%}:::router
    
    R1 -- Cleared\n(1-B)% --> E1[Normal Traffic\nCleared Classically]:::classical
    R1 -- Escalated\nB% --> C3[Classical Expert\nMLP / Tuned GBM]:::classical
    R1 -- Escalated\nB% --> Q1[Quantum Expert\nKernel / QAE]:::quantum
    
    E1 --> S1[Decision / Score]:::evaluation
    C3 --> S1
    Q1 --> S1
    
    S1 --> V1[Evaluation / Metrics]:::evaluation
    V1 --> V2[Statistical Analysis\nBootstrap/C.I.]:::evaluation
    
    V2 --> U1[Evidence Dashboard\nVisualization]:::ui
    V2 --> U2[Experiment Provenance\nLogging]:::ui
```

## Module Separation

1.  **Data:** `src/data/` (Acquisition, temporal splitting, validation)
2.  **Preprocessing:** `src/features/` (Engineering, scaling, reduction)
3.  **Classical ML:** `src/models/classical/` (LightGBM, Calibration, Baseline)
4.  **Routing:** `src/models/router/` (Uncertainty thresholding, budget sweeps)
5.  **Quantum ML:** `src/models/quantum/` (Kernels, QAE, PennyLane/Qiskit)
6.  **Controls:** (Implemented alongside Quantum ML for identical evaluation)
7.  **Evaluation:** `src/evaluation/` (AUPRC, C.I., Geometric difference)
8.  **Statistics:** `src/stats/` (Bootstrapping, significance)
9.  **Visualization & UI:** `src/dashboard/` (Streamlit/React for frontend)
10. **Experiment Provenance:** `src/tracking/` (MLflow or custom JSON schema for seeds, versions, config)
