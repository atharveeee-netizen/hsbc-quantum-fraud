import os
import pandas as pd
import numpy as np
import joblib
import logging
from src.utils.paths import PROCESSED_DATA_PATH, FEATURES_PATH, CLASSICAL_MODEL_DIR, ROUTER_DATA_PATH

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compute_uncertainty(probabilities):
    """
    [IMPLEMENTED] Quantifies classification uncertainty as distance from the decision boundary (0.5).
    Smaller distance = higher uncertainty (most ambiguous for classical model).
    """
    probs = np.asarray(probabilities)
    return np.abs(probs - 0.5)

def select_escalated_indices(probabilities, budget_pct=10.0, strategy='uncertainty', random_state=42):
    """
    [IMPLEMENTED] Selects indices of transactions to escalate under budget B%.
    Strategies:
      - 'uncertainty': Selects the top B% highest-uncertainty transactions (|p - 0.5| smallest).
      - 'random': Selects B% uniformly at random (control baseline).
    """
    n = len(probabilities)
    num_escalated = int(np.round((budget_pct / 100.0) * n))
    num_escalated = max(1, min(num_escalated, n)) # Clamp between 1 and n
    
    if strategy == 'uncertainty':
        uncertainties = compute_uncertainty(probabilities)
        sorted_indices = np.argsort(uncertainties)
        escalated_idx = sorted_indices[:num_escalated]
        cleared_idx = sorted_indices[num_escalated:]
    elif strategy == 'random':
        rng = np.random.RandomState(random_state)
        shuffled = rng.permutation(n)
        escalated_idx = shuffled[:num_escalated]
        cleared_idx = shuffled[num_escalated:]
    else:
        raise ValueError(f"Unknown routing strategy: {strategy}")
        
    return escalated_idx, cleared_idx

def route_traffic(budget_pct=10.0, split_name='test', strategy='uncertainty', random_state=42):
    """
    [IMPLEMENTED] Full routing pipeline for a given split ('test', 'train', or 'calib').
    Loads scaled features and calibrated baseline model, outputs escalated and cleared sets.
    """
    model_file = CLASSICAL_MODEL_DIR / "lgbm_calibrated.joblib"
    if not model_file.exists():
        logging.error(f"[BLOCKED] Calibrated model not found at {model_file}")
        return None, None

    model = joblib.load(model_file)
    
    scaled_file = FEATURES_PATH / f"{split_name}_scaled.parquet"
    if not scaled_file.exists():
        logging.error(f"[BLOCKED] Scaled features not found at {scaled_file}")
        return None, None
        
    df = pd.read_parquet(scaled_file)
    features = ['TransactionAmt', 'card1']
    X = df[features]
    
    probs = model.predict_proba(X)[:, 1]
    df['Classical_Prob'] = probs
    df['Uncertainty'] = compute_uncertainty(probs)
    
    escalated_idx, cleared_idx = select_escalated_indices(
        probs, budget_pct=budget_pct, strategy=strategy, random_state=random_state
    )
    
    escalated_df = df.iloc[escalated_idx].copy()
    cleared_df = df.iloc[cleared_idx].copy()
    
    strategy_tag = "" if strategy == 'uncertainty' else f"_{strategy}"
    escalated_file = ROUTER_DATA_PATH / f"escalated_{split_name}_b{budget_pct}{strategy_tag}.parquet"
    cleared_file = ROUTER_DATA_PATH / f"cleared_{split_name}_b{budget_pct}{strategy_tag}.parquet"
    
    escalated_df.to_parquet(escalated_file)
    cleared_df.to_parquet(cleared_file)
    
    logging.info(
        f"[VERIFIED] Routed {split_name} (budget={budget_pct}%, strategy={strategy}): "
        f"Escalated={len(escalated_df)}, Cleared={len(cleared_df)}"
    )
    return escalated_df, cleared_df

if __name__ == "__main__":
    for b in [0.5, 1.0, 2.0, 5.0, 10.0]:
        route_traffic(budget_pct=b, split_name='test', strategy='uncertainty')
        route_traffic(budget_pct=b, split_name='test', strategy='random')
        route_traffic(budget_pct=b, split_name='train', strategy='uncertainty')
