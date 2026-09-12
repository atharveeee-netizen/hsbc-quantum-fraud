import os
import zipfile
import pandas as pd
import hashlib
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# IEEE-CIS Fraud Detection parameters
KAGGLE_DATASET = "ieee-fraud-detection"
RAW_DATA_PATH = "../../data/raw"
PROCESSED_DATA_PATH = "../../data/processed"

def download_data():
    """Deterministic acquisition via Kaggle API."""
    if not os.path.exists(RAW_DATA_PATH):
        os.makedirs(RAW_DATA_PATH)
    
    expected_files = ['train_transaction.csv', 'train_identity.csv']
    if all(os.path.exists(os.path.join(RAW_DATA_PATH, f)) for f in expected_files):
        logging.info("Dataset already exists locally.")
        return

    logging.info("Downloading dataset from Kaggle...")
    try:
        subprocess.run(["kaggle", "competitions", "download", "-c", KAGGLE_DATASET, "-p", RAW_DATA_PATH], check=True)
        # Unzip
        zip_path = os.path.join(RAW_DATA_PATH, f"{KAGGLE_DATASET}.zip")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_PATH)
        logging.info("Download and extraction complete.")
    except Exception as e:
        logging.error(f"Failed to download data: {e}")
        logging.info("Ensure Kaggle API token (~/.kaggle/kaggle.json) is installed.")
        raise

def perform_temporal_split():
    """
    Splits the dataset 70/10/20 chronologically using TransactionDT.
    Random IID splits cause temporal data leakage in fraud detection.
    """
    logging.info("Loading transaction data for temporal split...")
    df = pd.read_csv(os.path.join(RAW_DATA_PATH, 'train_transaction.csv'))
    
    # Sort strictly by time
    df = df.sort_values('TransactionDT').reset_index(drop=True)
    
    n = len(df)
    train_end = int(n * 0.70)
    calib_end = int(n * 0.80)
    
    train_df = df.iloc[:train_end]
    calib_df = df.iloc[train_end:calib_end]
    test_df = df.iloc[calib_end:]
    
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)
        
    train_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'train.parquet'))
    calib_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'calib.parquet'))
    test_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'test.parquet'))
    
    logging.info(f"Temporal Split Complete: Train={len(train_df)}, Calib={len(calib_df)}, Test={len(test_df)}")
    
if __name__ == "__main__":
    download_data()
    # Note: Only execute the split if data download was successful.
    if os.path.exists(os.path.join(RAW_DATA_PATH, 'train_transaction.csv')):
        perform_temporal_split()
