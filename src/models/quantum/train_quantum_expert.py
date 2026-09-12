import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score, average_precision_score
import logging
from src.models.quantum.projected_kernel import compute_kernel_matrix
from src.features.build_features import FEATURES_PATH

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_quantum_expert(budget_pct=10.0):
    """
    [IMPLEMENTED] The genuine Quantum Expert using a PennyLane Projected Quantum Kernel.
    """
    logging.info(f"Loading escalated transactions for Budget={budget_pct}%...")
    
    # We must load the SCALED features to prevent test-leakage and unbounded angles
    # For now, we simulate this by loading train_scaled and just taking a small slice 
    # (since escalated_df isn't scaled in this skeleton, we'll slice train_scaled).
    # In a full pipeline, the router would route scaled features.
    
    try:
        df = pd.read_parquet(os.path.join(FEATURES_PATH, 'train_scaled.parquet'))
    except FileNotFoundError:
        logging.error("[BLOCKED] Features not found.")
        return

    # Simulate escalated traffic (N=200) from the scaled data
    escalated_df = df.head(200)

    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    X = escalated_df[features]
    y = escalated_df[target]
    
    # 50/50 Train/Test split of the escalated traffic
    n = len(escalated_df)
    train_end = int(n * 0.5)
    
    X_train, y_train = X.iloc[:train_end], y.iloc[:train_end]
    X_test, y_test = X.iloc[train_end:], y.iloc[train_end:]
    
    logging.info("Computing Quantum Kernel Matrix for Training (N=100)...")
    K_train = compute_kernel_matrix(X_train)
    
    logging.info("Training Quantum SVM on precomputed kernel...")
    q_model = SVC(kernel='precomputed', probability=True, random_state=42)
    q_model.fit(K_train, y_train)
    
    logging.info("Computing Quantum Kernel Matrix for Testing (N=100)...")
    K_test = compute_kernel_matrix(X_test, X_train)
    
    preds = q_model.predict_proba(K_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    auprc = average_precision_score(y_test, preds)
    
    logging.info(f"[SYNTHETIC] [MEASURED] Genuine Quantum Expert ROC-AUC: {auc:.4f}")
    logging.info(f"[SYNTHETIC] [MEASURED] Genuine Quantum Expert AUPRC: {auprc:.4f}")

if __name__ == "__main__":
    train_quantum_expert(budget_pct=10.0)
