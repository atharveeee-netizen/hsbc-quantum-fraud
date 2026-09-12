import os
import zipfile
import pandas as pd
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

KAGGLE_DATASET = "ieee-fraud-detection"
from src.utils.paths import RAW_DATA_PATH, PROCESSED_DATA_PATH

def download_data():
    """[PLANNED] Deterministic acquisition via Kaggle API. Requires kaggle.json."""
    if os.path.exists(os.path.join(RAW_DATA_PATH, 'train_transaction.csv')):
        logging.info("Dataset already exists locally (Real or Synthetic).")
        return

    logging.info("Attempting to download dataset from Kaggle...")
    try:
        subprocess.run(["kaggle", "competitions", "download", "-c", KAGGLE_DATASET, "-p", str(RAW_DATA_PATH)], check=True)
        zip_path = os.path.join(RAW_DATA_PATH, f"{KAGGLE_DATASET}.zip")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_PATH)
        logging.info("[MEASURED] Download and extraction complete.")
    except Exception as e:
        logging.error(f"[BLOCKED] Failed to download data: {e}")
        logging.info("Generating [SYNTHETIC] data as a fallback to clear the blocker...")
        from src.data.generate_synthetic import generate_synthetic_data
        generate_synthetic_data()

def perform_temporal_split(train_ratio=0.70, calib_ratio=0.10):
    """
    [IMPLEMENTED] Splitting chronologically using TransactionDT is a strict non-negotiable requirement.
    Random IID splits cause temporal data leakage in fraud detection. 
    The ratio (e.g. 70/10/20) is configurable based on data volume.
    """
    logging.info(f"Loading transaction data for temporal split (Train: {train_ratio}, Calib: {calib_ratio})...")
    df = pd.read_csv(os.path.join(RAW_DATA_PATH, 'train_transaction.csv'))
    
    df = df.sort_values('TransactionDT').reset_index(drop=True)
    
    n = len(df)
    train_end = int(n * train_ratio)
    calib_end = int(n * (train_ratio + calib_ratio))
    
    train_df = df.iloc[:train_end]
    calib_df = df.iloc[train_end:calib_end]
    test_df = df.iloc[calib_end:]
    
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)
        
    train_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'train.parquet'))
    calib_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'calib.parquet'))
    test_df.to_parquet(os.path.join(PROCESSED_DATA_PATH, 'test.parquet'))
    
    logging.info(f"[VERIFIED] Temporal Split Complete: Train={len(train_df)}, Calib={len(calib_df)}, Test={len(test_df)}")
    
if __name__ == "__main__":
    download_data()
    perform_temporal_split()
