# Real Quantum Statistical Validation — Paired Bootstrap Hypothesis Testing

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 166  
**Evidence Artifact:** [`docs/evidence/real_quantum_matched_experiment.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_quantum_matched_experiment.json)  
**Hypothesis Test:** $H_0: \Delta\text{PR-AUC} \le 0$ vs $H_1: \Delta\text{PR-AUC} > 0$  
**Resampling Protocol:** 1,000 Paired Bootstrap Iterations on Matched Escalated Test Stream  

---

## 1. Statistical Summary Table

Comparing the strongest quantum candidate (**Projected Quantum Kernel**) against the fair tuned classical baseline (**Classical RBF Expert**):

| Evaluation Metric | Point Estimate Delta | 1,000-Iteration Bootstrap Mean Delta | 95% Empirical Confidence Interval | Empirical $p$-Value | Bonferroni Adjusted $p$-Value | Statistically Significant at $\alpha=0.05$? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **$\Delta$ PR-AUC (PQK − RBF)** | **+0.0676** | **+0.0653** | **$[-0.0383, +0.1821]$** | **$p = 0.246$** | **$p = 0.492$** | **NO (Fails Gate)** |
| **$\Delta$ ROC-AUC (PQK − RBF)** | **+0.0519** | **+0.0501** | **$[-0.1044, +0.2052]$** | **$p = 0.312$** | **$p = 0.624$** | **NO (Fails Gate)** |

---

## 2. Definitive Scientific Interpretation

> [!CAUTION]
> **Definitive Null Finding:**  
> While the point estimate for PQK showed a nominal $+0.0676$ PR-AUC on this subsample, **the 95% confidence interval spans zero ($[-0.0383, +0.1821]$)** and the empirical $p$-value is **$0.246$** (Bonferroni adjusted $p = 0.492$).  
> Under standard scientific thresholds ($\alpha = 0.05$), the null hypothesis $H_0$ **CANNOT be rejected**.

### Critical Scientific Invariants Enforced:
1. **No Cherry-Picking:** We report the full confidence interval including the negative lower bound ($-0.0383$).
2. **Multiple-Testing Correction:** Bonferroni adjustment confirms that testing both PR-AUC and ROC-AUC inflates false-positive risk ($p = 0.492$).
3. **Formal Scientific Conclusion:**  
   **No statistically significant quantum advantage is demonstrated over fair classical RBF controls on real IEEE-CIS payment transaction data.**
