# 02 Hybrid Selective Escalation Architecture

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[REAL DATA] [MEASURED] [VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-ARCH-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | System throughput, operational latency, and selective escalation enrichment. |

---

## Dual-Stage Selective Pipeline
```text
Digital Payment Stream (IEEE-CIS, N=590,540)
        │
        ▼
Decision-Time Feature Scaling (Fitted strictly on Train Split)
        │
        ▼
Stage 1: Frontline Calibrated LightGBM (Clears ≥99% traffic, <5ms)
        │
        ▼
Selective Uncertainty Router (|p - 0.5| ≤ τ)
        │
        ├── High Confidence Clear (99%) ──► Instant Approval / Decline
        │
        ▼ Escalated Budget B ∈ {0.5%, 1.0%, 2.0%, 5.0%, 10.0%}
Stage 2: Ambiguity Specialist Queue
        ├── Candidate A: Classical Tuned RBF Expert (Fair Control)
        ├── Candidate B: Classical Gradient Boosted Expert (Control)
        ├── Candidate C: Classical Multi-Layer Perceptron (Control)
        └── Candidate D: Quantum Projected / Fidelity Kernel (Experimental)
        │
        ▼
Final Operational Score & Risk Band Resolution
```
