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
    """Raised when real IEEE-CIS data access is requested without valid credentials or accepted rules."""
    pass

def check_kaggle_credentials() -> bool:
    """Checks whether valid Kaggle credentials exist in environment or ~/.kaggle."""
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    access_token = Path.home() / ".kaggle" / "access_token"
    has_legacy_env = ("KAGGLE_USERNAME" in os.environ and "KAGGLE_KEY" in os.environ)
    has_token_env = ("KAGGLE_API_TOKEN" in os.environ)
    return kaggle_json.exists() or access_token.exists() or has_legacy_env or has_token_env

def _get_kaggle_auth_headers() -> Dict[str, str]:
    """Resolves authentication headers for Kaggle API requests."""
    # 1. Bearer Token (Kaggle API Token format)
    if "KAGGLE_API_TOKEN" in os.environ and os.environ["KAGGLE_API_TOKEN"].strip():
        return {"Authorization": f"Bearer {os.environ['KAGGLE_API_TOKEN'].strip()}"}
    access_token_file = Path.home() / ".kaggle" / "access_token"
    if access_token_file.exists():
        try:
            tok = access_token_file.read_text(encoding='utf-8').strip()
            if tok:
                return {"Authorization": f"Bearer {tok}"}
        except Exception:
            pass

    # 2. Basic Auth (Legacy Username / Key)
    import base64
    if "KAGGLE_USERNAME" in os.environ and "KAGGLE_KEY" in os.environ:
        raw_creds = f"{os.environ['KAGGLE_USERNAME']}:{os.environ['KAGGLE_KEY']}".encode('utf-8')
        return {"Authorization": f"Basic {base64.b64encode(raw_creds).decode()}"}
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if kaggle_json.exists():
        try:
            data = json.loads(kaggle_json.read_text(encoding='utf-8'))
            raw_creds = f"{data['username']}:{data['key']}".encode('utf-8')
            return {"Authorization": f"Basic {base64.b64encode(raw_creds).decode()}"}
        except Exception:
            pass

    return {}

def download_competition_file_api(dataset_name: str, file_name: str, dest_path: Path):
    """Downloads a competition file using the Kaggle REST API."""
    import urllib.request
    import urllib.error
    
    headers = _get_kaggle_auth_headers()
    if not headers:
        raise RealDataBlockedError("[BLOCKED: REAL DATA] No Kaggle credentials found.")

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://www.kaggle.com/api/v1/competitions/data/download/{dataset_name}/{file_name}"
    req = urllib.request.Request(url, headers=headers)
    
    try:
        logging.info(f"Connecting to Kaggle API to stream {file_name}...")
        with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as f_out:
            while True:
                chunk = resp.read(1024 * 1024) # 1 MB chunks
                if not chunk:
                    break
                f_out.write(chunk)
        logging.info(f"Successfully downloaded {file_name} to {dest_path}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        if e.code == 403:
            raise RealDataBlockedError(
                f"[BLOCKED: REAL DATA] Kaggle HTTP 403 Forbidden: {err_msg} "
                f"Please visit https://www.kaggle.com/competitions/{dataset_name}/rules in your browser "
                f"while logged in and click 'I Understand and Accept' to grant download permissions to your API token."
            )
        raise RealDataBlockedError(f"[BLOCKED: REAL DATA] Kaggle download failed with HTTP {e.code}: {err_msg}")
    except Exception as e:
        raise RealDataBlockedError(f"[BLOCKED: REAL DATA] Network download error: {e}")

def ingest_real_ieee_cis() -> Dict[str, Any]:
    """
    [BLOCKED: REAL DATA] Attempts genuine IEEE-CIS ingestion via Kaggle API.
    Raises RealDataBlockedError if credentials, rules acceptance, or raw files are missing.
    Never silently substitutes synthetic data.
    """
    logging.info("Evaluating Real Data Ingestion Gate (Phase 83 / Phase 123)...")
    if not check_kaggle_credentials():
        logging.warning("[BLOCKED: REAL DATA] No legitimate Kaggle credentials found in ~/.kaggle/kaggle.json, access_token, or environment.")
        raise RealDataBlockedError(
            "[BLOCKED: REAL DATA] Real IEEE-CIS data ingestion is blocked. "
            "Kaggle credentials not present. To execute with real data, configure ~/.kaggle/kaggle.json or ~/.kaggle/access_token."
        )

    real_csv = RAW_DATA_PATH / "train_transaction.csv"
    is_real_cached = False
    if real_csv.exists():
        try:
            sample_df = pd.read_csv(real_csv, nrows=10)
            if detect_dataset_provenance_type(sample_df) == "REAL_IEEE_CIS":
                is_real_cached = True
        except Exception:
            is_real_cached = False

    if not is_real_cached:
        logging.info("Attempting genuine download of IEEE-CIS competition data...")
        # Check if kaggle CLI is installed
        cli_available = False
        try:
            subprocess.run(["kaggle", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            cli_available = True
        except Exception:
            cli_available = False

        if cli_available:
            try:
                subprocess.run(["kaggle", "competitions", "download", "-c", KAGGLE_DATASET, "-p", str(RAW_DATA_PATH)], check=True)
                zip_path = RAW_DATA_PATH / f"{KAGGLE_DATASET}.zip"
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(RAW_DATA_PATH)
                logging.info("[MEASURED] Genuine IEEE-CIS download complete via CLI.")
            except Exception as e:
                raise RealDataBlockedError(f"[BLOCKED: REAL DATA] Kaggle CLI download failed: {e}")
        else:
            # Native REST API download using authenticated token
            download_competition_file_api(KAGGLE_DATASET, "train_transaction.csv", real_csv)
            id_csv = RAW_DATA_PATH / "train_identity.csv"
            try:
                download_competition_file_api(KAGGLE_DATASET, "train_identity.csv", id_csv)
            except Exception as e:
                logging.warning(f"Could not download train_identity.csv: {e}")

    try:
        df = pd.read_csv(real_csv)
        validate_real_ieee_cis_dataset(df)
        return {"status": "[VERIFIED: REAL DATA INGESTED]", "rows": len(df)}
    except SchemaValidationError as e:
        raise RealDataBlockedError(f"[BLOCKED: REAL DATA] File in data/raw is not valid real IEEE-CIS data: {e}")

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
