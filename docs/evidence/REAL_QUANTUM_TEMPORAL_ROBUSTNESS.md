# Real Quantum Temporal Robustness — Chronological Window Analysis

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 167  
**Evidence Artifact:** [`docs/evidence/real_quantum_temporal_robustness.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_temporal_robustness.json)  
**Partition Evaluated:** Out-of-Sample Test Split Divided into 3 Contiguous Sequential Epochs (Days 141.1 to 183.0)  

---

## 1. Window-by-Window Empirical Performance

To prevent temporal averaging from hiding regime shifts, the quantum-vs-classical delta is evaluated independently across each sequential window:

| Temporal Slice | Calendar Epoch | Transaction DT Range | Window Fraud Prevalence | Classical RBF PR-AUC | Projected Quantum PR-AUC | $\Delta$ (PQK − RBF) | Window Winner |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Window 1** | Days 141.1 – 155.0 | $[12,192,900, 13,388,906]$ | 3.26% | **0.5841** | **0.4148** | **-0.1693** | **Classical RBF** (+0.169) |
| **Window 2** | Days 155.0 – 168.6 | $[13,388,918, 14,571,131]$ | 3.13% | **0.4412** | **0.5187** | **+0.0774** | Quantum PQK (+0.077) |
| **Window 3** | Days 168.6 – 183.0 | $[14,571,137, 15,811,088]$ | 3.92% | **0.4163** | **0.5765** | **+0.1602** | Quantum PQK (+0.160) |

---

## 2. Temporal Robustness Audit & Conclusion

1. **Failure to Maintain Consistency:**  
   In Window 1, Classical RBF heavily outperforms PQK by **+0.1693 PR-AUC** ($0.5841$ vs $0.4148$).
2. **High Temporal Volatility:**  
   The performance difference oscillates wildly from $-0.1693$ to $+0.1602$ across adjacent months, indicating that quantum performance is fragile and sensitive to non-stationary payment distribution drift.
3. **Formal Invariant:**  
   Because quantum enhancement fails to deliver consistent positive delta across all evaluation windows, it **fails the Temporal Robustness Gate**.
