import os
import pandas as pd
import numpy as np
import joblib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PROCESSED_DATA_PATH = "../../../data/processed"
MODEL_PATH = "../classical"
ROUTER_DATA_PATH = "../../../data/router"

def route_traffic(budget_pct=10.0):
    """
    [IMPLEMENTED] Routes the top B% most uncertain transactions to the Quantum/Classical Expert queue.
    The remaining (1-B)% are cleared classically.
    """
    if not os.path.exists(ROUTER_DATA_PATH):
        os.makedirs(ROUTER_DATA_PATH)

    logging.info("Loading Test Set and Classical Baseline Model...")
    try:
        test_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'test.parquet'))
        model = joblib.load(os.path.join(MODEL_PATH, "lgbm_calibrated.joblib"))
    except FileNotFoundError:
        logging.error("[BLOCKED] Test data or baseline model not found.")
        return

    features = ['TransactionAmt', 'card1']
    X_test = test_df[features]
    
    # 1. Classical Prediction
    logging.info("Computing Classical Probabilities...")
    probs = model.predict_proba(X_test)[:, 1]
    test_df['Classical_Prob'] = probs
    
    # 2. Uncertainty Scoring (Distance from decision boundary 0.5)
    # The closer to 0.5, the higher the uncertainty (closer to 0)
    test_df['Uncertainty'] = np.abs(probs - 0.5)
    
    # 3. Escalation Routing
    num_escalated = int((budget_pct / 100.0) * len(test_df))
    logging.info(f"Escalation Budget: {budget_pct}% -> Escalating {num_escalated} out of {len(test_df)} transactions.")
    
    # Sort by uncertainty (lowest distance from 0.5 is highest uncertainty)
    routed_df = test_df.sort_values(by='Uncertainty', ascending=True).reset_index(drop=True)
    
    escalated_df = routed_df.iloc[:num_escalated]
    cleared_df = routed_df.iloc[num_escalated:]
    
    # Save the routed subsets
    escalated_file = os.path.join(ROUTER_DATA_PATH, f"escalated_b{int(budget_pct)}.parquet")
    cleared_file = os.path.join(ROUTER_DATA_PATH, f"cleared_b{int(budget_pct)}.parquet")
    
    escalated_df.to_parquet(escalated_file)
    cleared_df.to_parquet(cleared_file)
    
    logging.info(f"[VERIFIED] Routing complete. Saved to {ROUTER_DATA_PATH}")

if __name__ == "__main__":
    route_traffic(budget_pct=10.0)
