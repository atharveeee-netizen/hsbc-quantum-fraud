# Real Data Feature Leakage Audit Report

**Status:** `[REAL DATA]` `[MEASURED]` `[VERIFIED]`  
**Execution Phase:** Phase 127  
**Scope:** Evaluation of Candidate Features for Real-Time Decision-Time Ingestion  

---

## 1. Decision-Time Feature Classification

Every feature fed to the frontline and specialist models was audited against the operational decision point (payment gateway authorization, sub-50 ms SLA):

| Feature Name | Feature Domain | Decision-Time Classification | Evidentiary Rationale |
| :--- | :--- | :--- | :--- |
| `TransactionAmt` | Transaction Value | `AVAILABLE_AT_DECISION_TIME` | Transmitted directly in ISO 8583 authorization request payload. |
| `card1` | Card Issuer Bank / IIN | `AVAILABLE_AT_DECISION_TIME` | Extracted from primary account number (PAN) IIN range at authorization. |
| `card2` | Issuer sub-category | `AVAILABLE_AT_DECISION_TIME` | Routing metadata available at switch. |
| `card3` | Country Code | `AVAILABLE_AT_DECISION_TIME` | Originating bank country code. |
| `card5` | Payment network code | `AVAILABLE_AT_DECISION_TIME` | Card scheme identification. |
| `C1` | Transaction counter | `AVAILABLE_AT_DECISION_TIME` | Cumulative count of past transactions associated with phone/email. |
| `C2` | Velocity counter | `AVAILABLE_AT_DECISION_TIME` | Historical velocity up to transaction arrival. |
| `C5` | Counter | `AVAILABLE_AT_DECISION_TIME` | Historical velocity count. |
| `C13` | Counter | `AVAILABLE_AT_DECISION_TIME` | Historical velocity count. |
| `D1` | Timedelta (Days since start) | `AVAILABLE_AT_DECISION_TIME` | Days since cardholder onboarding / first observed transaction. |

---

## 2. Excluded Features (Flagged as Potential Future / Identity Memorization Leakage)

1. **Cardholder Pseudonym Reconstruction (`card1 + addr1 + D1` UID):**
   * *Risk:* Creating artificial composite user IDs memorizes specific Kaggle cardholder identities. While this artificially inflates offline competition AUC, it fails in live production when zero-day cards appear.
   * *Action:* Explicitly excluded.
2. **Post-Authorization Chargeback Flags (`isFraud` Target Leakage):**
   * *Risk:* Target encodings computed across the full dataset leak future chargeback statuses into historical transactions.
   * *Action:* Zero target-encoding used. All categorical mappings and imputations are fit strictly on the Train partition.
3. **Future Window Aggregates (e.g. mean amount in $t \pm 7\text{ days}$):**
   * *Risk:* Requires lookahead into future transactions.
   * *Action:* Strictly banned. Only past-looking velocity counters (`C` columns) are utilized.
4. **Identity Join Profiles (`train_identity.csv`):**
   * *Risk:* Only present for $24.42\%$ of transactions (severe non-random missingness; absent on POS / chip transactions).
   * *Action:* Excluded from frontline baseline to ensure uniform availability for 100% of transaction traffic.
