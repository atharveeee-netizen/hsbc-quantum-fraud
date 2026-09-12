"""
IEEE-CIS & Synthetic Schema Validator Module
Enforces strict schema validation contracts across raw and processed datasets.
Prevents accidental confusion between synthetic benchmarks and real IEEE-CIS data.
"""

import pandas as pd
from typing import Dict, Any, List

class SchemaValidationError(Exception):
    """Raised when a dataset fails schema validation."""
    pass

SYNTHETIC_REQUIRED_COLUMNS = [
    "TransactionID",
    "isFraud",
    "TransactionDT",
    "TransactionAmt",
    "card1"
]

# Core IEEE-CIS transaction identity columns
IEEE_CIS_MINIMAL_COLUMNS = [
    "TransactionID",
    "isFraud",
    "TransactionDT",
    "TransactionAmt",
    "ProductCD",
    "card1",
    "card2",
    "card3",
    "card4",
    "card5",
    "card6"
]

def detect_dataset_provenance_type(df: pd.DataFrame) -> str:
    """
    Identifies whether a DataFrame conforms to the synthetic benchmark or full IEEE-CIS.
    """
    cols = set(df.columns)
    if "ProductCD" in cols and len(cols) > 20:
        return "REAL_IEEE_CIS"
    elif all(c in cols for c in SYNTHETIC_REQUIRED_COLUMNS):
        return "SYNTHETIC_BENCHMARK"
    else:
        return "UNKNOWN_SCHEMA"

def validate_synthetic_dataset(df: pd.DataFrame) -> bool:
    """
    Validates synthetic benchmark schema and monotonicity.
    """
    missing = [c for c in SYNTHETIC_REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise SchemaValidationError(f"Synthetic dataset missing required columns: {missing}")

    if not df["TransactionDT"].is_monotonic_increasing:
        raise SchemaValidationError("Synthetic dataset TransactionDT must be monotonically increasing.")

    if not set(df["isFraud"].unique()).issubset({0, 1}):
        raise SchemaValidationError("isFraud column must contain only binary {0, 1} values.")

    return True

def validate_real_ieee_cis_dataset(df: pd.DataFrame) -> bool:
    """
    Validates real IEEE-CIS dataset schema requirements.
    """
    missing = [c for c in IEEE_CIS_MINIMAL_COLUMNS if c not in df.columns]
    if missing:
        raise SchemaValidationError(
            f"[BLOCKED: REAL DATA] Real IEEE-CIS validation failed. Missing expected columns: {missing}"
        )

    if not df["TransactionDT"].is_monotonic_increasing:
        raise SchemaValidationError("IEEE-CIS TransactionDT must be sorted chronologically.")

    return True
