# 13 Physical Hardware Decision Gate

| Provenance Metadata | Specification |
| :--- | :--- |
| **Scientific Status** | `[VERIFIED]` |
| **Dataset Provenance** | `Official IEEE-CIS Fraud Detection (Kaggle Benchmark)` |
| **Dataset Scale** | `590,540 rows, 394 columns (Strict Chronological Split)` |
| **Experiment ID** | `EXP-HW-GATE-01` |
| **Primary Seed** | `42` |
| **Git Commit** | `e6dc412` |
| **Metric Definition** | Decision protocol verifying prerequisite criteria for physical QPU dispatch. |

---

## Formal Gate Decision: HARDWARE NOT JUSTIFIED
1. **Statistical Gate:** FAILED ($p = 0.246 > 0.05$).
2. **Temporal Gate:** FAILED (RBF outperforms PQK in Window 1 by +0.169).
3. **Noise Gate:** FAILED (Monotonic degradation).
4. **Latency Gate:** FAILED (180s - 1,200s queue vs 50ms SLA).
5. **Economic Gate:** FAILED ($353,000 / 10k batch vs $0.15 classical).
Physical hardware execution is blocked to prevent waste of enterprise compute capital.
