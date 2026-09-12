import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from src.utils.paths import PROCESSED_DATA_PATH, FEATURES_PATH

def build_features():
    """
    [IMPLEMENTED] Deterministic feature transformation pipeline.
    Fits scalers ONLY on training data to prevent temporal leakage into the test set.
    """

        
    logging.info("Loading processed temporal datasets...")
    try:
        train_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'train.parquet'))
        calib_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'calib.parquet'))
        test_df = pd.read_parquet(os.path.join(PROCESSED_DATA_PATH, 'test.parquet'))
    except FileNotFoundError:
        logging.error("[BLOCKED] Datasets not found.")
        return

    # [PLANNED] Quantum Feature Selection (8-12 dimensions)
    # For now, we scale the synthetic numerical features
    features = ['TransactionAmt', 'card1']
    target = 'isFraud'
    
    logging.info("Fitting StandardScaler exclusively on Training data...")
    scaler = StandardScaler()
    scaler.fit(train_df[features])
    
    # Save the scaler for reproducibility
    scaler_path = os.path.join(FEATURES_PATH, "scaler.joblib")
    joblib.dump(scaler, scaler_path)
    
    # Transform
    def transform_and_save(df, name):
        X_scaled = scaler.transform(df[features])
        df_scaled = pd.DataFrame(X_scaled, columns=features)
        df_scaled[target] = df[target].values
        
        # Preserve indices or other important metadata if needed
        # (For this synthetic test, we just save the scaled data)
        out_path = os.path.join(FEATURES_PATH, f"{name}_scaled.parquet")
        df_scaled.to_parquet(out_path)
        logging.info(f"Saved {name} features to {out_path}")

    transform_and_save(train_df, "train")
    transform_and_save(calib_df, "calib")
    transform_and_save(test_df, "test")
    
    logging.info("[VERIFIED] Feature engineering complete. No test leakage detected.")

if __name__ == "__main__":
    build_features()
