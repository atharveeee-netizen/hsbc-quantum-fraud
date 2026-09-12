import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RAW_DATA_PATH = "../../data/raw"

def generate_synthetic_data(num_samples=10000):
    """
    [IMPLEMENTED] Generates synthetic smoke-test fixture mirroring IEEE-CIS schema.
    This bypasses Kaggle credential blockers and allows the engineering loop to continue.
    """
    if not os.path.exists(RAW_DATA_PATH):
        os.makedirs(RAW_DATA_PATH)
        
    logging.info(f"Generating {num_samples} synthetic samples...")
    
    # Simulate chronological ordering (TransactionDT)
    dt = np.sort(np.random.randint(86400, 86400*30, size=num_samples))
    
    # Features
    amt = np.random.exponential(scale=50, size=num_samples)
    card1 = np.random.randint(1000, 18000, size=num_samples)
    
    # Simulate a noisy decision boundary
    fraud_prob = 1 / (1 + np.exp(-(amt/100 - 1.5 + np.random.normal(0, 1, size=num_samples))))
    is_fraud = np.random.binomial(1, fraud_prob)
    
    df = pd.DataFrame({
        'TransactionID': np.arange(3000000, 3000000 + num_samples),
        'isFraud': is_fraud,
        'TransactionDT': dt,
        'TransactionAmt': amt,
        'card1': card1
    })
    
    out_path = os.path.join(RAW_DATA_PATH, 'train_transaction.csv')
    df.to_csv(out_path, index=False)
    logging.info(f"[SYNTHETIC] data saved to {out_path} with {(is_fraud.sum()/num_samples)*100:.2f}% fraud rate.")

if __name__ == "__main__":
    generate_synthetic_data()
