import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score, average_precision_score
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ROUTER_DATA_PATH = "../../../data/router"

def train_classical_control(budget_pct=10.0):
    """
    [IMPLEMENTED] The strongest classical baseline for the exact same escalation slot.
    This is an RBF Kernel SVM, evaluating against the same B% escalated subset.
    """
    logging.info(f"Loading escalated transactions for Budget={budget_pct}%...")
    try:
        escalated_df = pd.read_parquet(os.path.join(ROUTER_DATA_PATH, f"escalated_b{int(budget_pct)}.parquet"))
    except FileNotFoundError:
        logging.error(f"[BLOCKED] Escalated data for budget {budget_pct}% not found.")
        return

    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    X = escalated_df[features]
    y = escalated_df[target]
    
    # 50/50 Train/Test split of the escalated traffic
    n = len(escalated_df)
    train_end = int(n * 0.5)
    
    X_train, y_train = X.iloc[:train_end], y.iloc[:train_end]
    X_test, y_test = X.iloc[train_end:], y.iloc[train_end:]
    
    logging.info("[IMPLEMENTED] Training Classical RBF Control...")
    
    # RBF Kernel Control
    c_model = SVC(kernel='rbf', probability=True, random_state=42)
    c_model.fit(X_train, y_train)
    
    preds = c_model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    auprc = average_precision_score(y_test, preds)
    
    logging.info(f"[SYNTHETIC] [MEASURED] Classical RBF Control ROC-AUC: {auc:.4f}")
    logging.info(f"[SYNTHETIC] [MEASURED] Classical RBF Control AUPRC: {auprc:.4f}")

if __name__ == "__main__":
    train_classical_control(budget_pct=10.0)
