# Real Local Latency Audit — Inference Timing & SLA Compliance

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 172  
**Evidence Artifact:** [`docs/evidence/real_latency_audit.json`](file:///C:/Users/noobg/.gemini/antigravity-ide/scratch/hsbc-quantum-fraud/docs/evidence/real_latency_audit.json)  
**Target Payment SLA:** $< 50.0\text{ ms}$ Synchronous Card-Not-Present Authorization  
**Test Environment:** Windows x64, 16 Cores, Python 3.10  

---

## 1. Component Latency Profile (Single Transaction)

Evaluated across repeated execution runs with warmup cycles:

| Pipeline Component | Measurement Count | Mean Latency | Median Latency | 95th Percentile (p95) | 99th Percentile (p99) | SLA Compliance ($<50\text{ ms}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Feature Extraction & Scaling** | 200 runs | 0.0035 ms | **0.0031 ms** | 0.0048 ms | 0.0089 ms | **PASS** ($<0.01\%\text{ SLA}$) |
| **Frontline Calibrated LightGBM** | 200 runs | 3.8421 ms | **3.7850 ms** | 4.6210 ms | 5.1240 ms | **PASS** ($7.6\%\text{ SLA}$) |
| **Selective Uncertainty Router** | 500 runs | 0.0009 ms | **0.0008 ms** | 0.0014 ms | 0.0022 ms | **PASS** ($<0.01\%\text{ SLA}$) |
| **Classical RBF Expert ($N=200$)** | 100 runs | 0.8120 ms | **0.7850 ms** | 1.0420 ms | 1.4510 ms | **PASS** ($1.6\%\text{ SLA}$) |
| **PennyLane Quantum Simulator** | 20 runs | 164.2150 ms | **159.1423 ms** | 217.1762 ms | 235.4010 ms | **FAIL** ($3.2\times - 4.3\times\text{ violation}$) |
| **Cloud QPU Hardware Dispatch** | N/A | `NOT MEASURED` | **180,000 ms** (180 s) | **1,200,000 ms** (20 min) | `NOT MEASURED` | **FAIL** ($3,600\times\text{ violation}$) |

---

## 2. End-to-End Operational Pipeline Latencies

| Execution Path | Description | End-to-End Median Latency | End-to-End p95 Latency | SLA Margin Remaining | Production Readiness |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Fast Path (99.0% of Volume)** | Preprocessing → LightGBM → Router → Instant Decline / Approve | **4.07 ms** | **4.97 ms** | **+45.03 ms (90% headroom)** | **PRODUCTION READY** |
| **Escalated Path (1.0% Volume - Classical)** | Preprocessing → LightGBM → Router → Tuned Classical RBF Expert | **4.89 ms** | **5.45 ms** | **+44.55 ms (89% headroom)** | **PRODUCTION READY** |
| **Escalated Path (1.0% Volume - Quantum)** | Preprocessing → LightGBM → Router → Quantum Kernel Simulator | **163.22 ms** | **222.15 ms** | **-172.15 ms (Violation)** | **UNVIABLE SYNCHRONOUSLY** |

> [!CAUTION]
> Cloud QPU hardware latency is designated strictly as `NOT MEASURED` for physical execution because hardware gates prevented dispatch. Modeled queue latency (180s to 1,200s) confirms physical QPUs are unviable for synchronous frontline payment clearance.
