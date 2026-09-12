# 02 Hybrid System Architecture

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[SYNTHETIC] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `synthetic_ieee_cis_benchmark` (v1.0-synthetic-10k) |
| **Real Data Status** | `[BLOCKED: REAL DATA]` (Awaiting Kaggle credentials) |
| **Experiment ID** | `EXP-ARCH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `c58c174` |
| **Metric Definition** | System throughput, latency, and routing accuracy. |

---

## Dual-Stage Hybrid Pipeline
```text
Digital Payment Transaction
        │
        ▼
Classical Feature Standardization (Train-fit only)
        │
        ▼
Stage 1: Calibrated LightGBM Baseline (Clears ≥90% traffic, <15ms)
        │
        ▼
Selective Escalation Router (Uncertainty Margin + Transaction Amount)
        │
        ├── High Confidence Clear ──► Instant Approval / Decline
        │
        ▼ Escalated Budget B ∈ {0.5%, 1%, 2%, 5%, 10%}
Stage 2: Ambiguity Expert
        ├── Candidate A: Classical Tuned RBF (Control)
        ├── Candidate B: Classical LightGBM Expert (Control)
        ├── Candidate C: Classical Poly / MLP (Control)
        └── Candidate D: Quantum Projected / Fidelity Kernel (Experimental)
        │
        ▼
Full-System Score Fusion & Final Fraud Decision
```
