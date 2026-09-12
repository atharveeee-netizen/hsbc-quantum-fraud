import os
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.calibration import CalibratedClassifierCV
import logging
import joblib

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PROCESSED_DATA_PATH = "../../../data/processed"
MODEL_PATH = "."


def train_baseline():
    """
    [IMPLEMENTED] Trains the LightGBM baseline on the temporal split.
    """
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
        
    logging.info("Loading temporal datasets (Train & Calib)...")
    try:
        train_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'train.parquet'))
        calib_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'calib.parquet'))
        test_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'test.parquet'))
    except FileNotFoundError:
        logging.error("[BLOCKED] Datasets not found. Run make_dataset.py first.")
        return

    features = ['TransactionAmt', 'card1']  # Using synthetic features for now
    target = 'isFraud'
    
    X_train, y_train = train_df[features], train_df[target]
    X_calib, y_calib = calib_df[features], calib_df[target]
    X_test, y_test = test_df[features], test_df[target]
    
    logging.info("Training Base LightGBM model...")
    base_model = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, random_state=42)
    base_model.fit(X_train, y_train)
    
    logging.info("Calibrating model using Isotonic Regression...")
    calibrated_model = CalibratedClassifierCV(base_model, method='isotonic', cv='prefit')
    calibrated_model.fit(X_calib, y_calib)
    
    logging.info("Evaluating on Temporal Test Set...")
    preds = calibrated_model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    auprc = average_precision_score(y_test, preds)
    
    logging.info(f"[SYNTHETIC] [MEASURED] Test ROC-AUC: {auc:.4f}")
    logging.info(f"[SYNTHETIC] [MEASURED] Test AUPRC: {auprc:.4f}")
    
    # Save the model
    model_file = os.path.join(MODEL_PATH, "lgbm_calibrated.joblib")
    joblib.dump(calibrated_model, model_file)
    logging.info(f"[VERIFIED] Model saved to {model_file}")

if __name__ == "__main__":
    train_baseline()
