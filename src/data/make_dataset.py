"""
Dataset Ingestion & Temporal Splitting Pipeline (Phases 81-83)
Supports explicit Real IEEE-CIS ingestion gate and deterministic synthetic benchmark.
Strictly forbids silent fallback or masquerading synthetic data as real data.
"""

import os
import sys
import json
import zipfile
import logging
import pandas as pd
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any

from src.utils.paths import RAW_DATA_PATH, PROCESSED_DATA_PATH
from src.utils.provenance import create_provenance_record
from src.data.schema_validator import (
    validate_synthetic_dataset,
    validate_real_ieee_cis_dataset,
    detect_dataset_provenance_type,
    SchemaValidationError
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

KAGGLE_DATASET = "ieee-fraud-detection"

class RealDataBlockedError(RuntimeError):
    """Raised when real IEEE-CIS data access is requested without valid credentials."""
    pass

def check_kaggle_credentials() -> bool:
    """Checks whether valid Kaggle credentials exist in environment or ~/.kaggle."""
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    has_env = ("KAGGLE_USERNAME" in os.environ and "KAGGLE_KEY" in os.environ)
    return kaggle_json.exists() or has_env

def ingest_real_ieee_cis() -> Dict[str, Any]:
    """
    [BLOCKED: REAL DATA] Attempts genuine IEEE-CIS ingestion via Kaggle API.
    Raises RealDataBlockedError if credentials or raw files are missing.
    Never silently substitutes synthetic data.
    """
    logging.info("Evaluating Real Data Ingestion Gate (Phase 83)...")
    if not check_kaggle_credentials():
        logging.warning("[BLOCKED: REAL DATA] No legitimate Kaggle credentials found in ~/.kaggle/kaggle.json or environment.")
        raise RealDataBlockedError(
            "[BLOCKED: REAL DATA] Real IEEE-CIS data ingestion is blocked. "
            "Kaggle credentials not present. To execute with real data, configure ~/.kaggle/kaggle.json."
        )

    logging.info("Attempting genuine download of IEEE-CIS competition data...")
    try:
        subprocess.run(["kaggle", "competitions", "download", "-c", KAGGLE_DATASET, "-p", str(RAW_DATA_PATH)], check=True)
        zip_path = RAW_DATA_PATH / f"{KAGGLE_DATASET}.zip"
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_PATH)
        logging.info("[MEASURED] Genuine IEEE-CIS download complete.")
    except Exception as e:
        raise RealDataBlockedError(f"[BLOCKED: REAL DATA] Kaggle download failed: {e}")

    real_csv = RAW_DATA_PATH / "train_transaction.csv"
    df = pd.read_csv(real_csv)
    validate_real_ieee_cis_dataset(df)
    return {"status": "[VERIFIED: REAL DATA INGESTED]", "rows": len(df)}

def ingest_synthetic_benchmark() -> pd.DataFrame:
    """
    [IMPLEMENTED] [SYNTHETIC] Ingests or generates the standardized synthetic benchmark.
    Explicitly labeled as synthetic in provenance records.
    """
    raw_file = RAW_DATA_PATH / "train_transaction.csv"
    if not raw_file.exists():
        logging.info("Generating deterministic synthetic benchmark dataset...")
        from src.data.generate_synthetic import generate_synthetic_data
        generate_synthetic_data()

    df = pd.read_csv(raw_file)
    validate_synthetic_dataset(df)
    logging.info(f"[SYNTHETIC] [MEASURED] Loaded synthetic benchmark dataset: {len(df)} rows.")
    return df

def perform_temporal_split(
    df: Optional[pd.DataFrame] = None,
    train_ratio: float = 0.70,
    calib_ratio: float = 0.10
) -> Dict[str, Any]:
    """
    [IMPLEMENTED] Chronological split along monotonic TransactionDT.
    Prevents temporal data leakage. Ratios: 70% Train, 10% Calib, 20% Test.
    """
    if df is None:
        df = ingest_synthetic_benchmark()

    dtype = detect_dataset_provenance_type(df)
    dataset_status = "[REAL DATA] [MEASURED]" if dtype == "REAL_IEEE_CIS" else "[SYNTHETIC] [MEASURED] [VERIFIED]"
    dataset_source = "ieee_cis_real" if dtype == "REAL_IEEE_CIS" else "synthetic_ieee_cis_benchmark"

    logging.info(f"Performing temporal split ({train_ratio:.0%}/{calib_ratio:.0%}/{1-train_ratio-calib_ratio:.0%}) on {dtype}...")
    df = df.sort_values('TransactionDT').reset_index(drop=True)

    n = len(df)
    train_end = int(n * train_ratio)
    calib_end = int(n * (train_ratio + calib_ratio))

    train_df = df.iloc[:train_end]
    calib_df = df.iloc[train_end:calib_end]
    test_df = df.iloc[calib_end:]

    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    train_df.to_parquet(PROCESSED_DATA_PATH / 'train.parquet')
    calib_df.to_parquet(PROCESSED_DATA_PATH / 'calib.parquet')
    test_df.to_parquet(PROCESSED_DATA_PATH / 'test.parquet')

    provenance = create_provenance_record(
        dataset_source=dataset_source,
        dataset_status=dataset_status,
        dataset_version=f"v1.0-{dtype.lower()}",
        train_range={
            "dt_min": float(train_df["TransactionDT"].min()),
            "dt_max": float(train_df["TransactionDT"].max()),
            "n_samples": len(train_df),
            "fraud_rate": float(train_df["isFraud"].mean())
        },
        calibration_range={
            "dt_min": float(calib_df["TransactionDT"].min()),
            "dt_max": float(calib_df["TransactionDT"].max()),
            "n_samples": len(calib_df),
            "fraud_rate": float(calib_df["isFraud"].mean())
        },
        test_range={
            "dt_min": float(test_df["TransactionDT"].min()),
            "dt_max": float(test_df["TransactionDT"].max()),
            "n_samples": len(test_df),
            "fraud_rate": float(test_df["isFraud"].mean())
        },
        sample_count=n
    )

    with open(PROCESSED_DATA_PATH / 'provenance.json', 'w', encoding='utf-8') as f:
        json.dump(provenance, f, indent=2)

    logging.info(
        f"[VERIFIED] Temporal Split Complete: Train={len(train_df)}, Calib={len(calib_df)}, Test={len(test_df)}. "
        f"Provenance saved to {PROCESSED_DATA_PATH / 'provenance.json'}"
    )

    return {
        "status": "[VERIFIED]",
        "dataset_type": dtype,
        "train_len": len(train_df),
        "calib_len": len(calib_df),
        "test_len": len(test_df),
        "provenance": provenance
    }

if __name__ == "__main__":
    perform_temporal_split()
