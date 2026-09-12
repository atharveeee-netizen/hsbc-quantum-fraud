import pytest
import pandas as pd
from src.data.schema_validator import (
    validate_synthetic_dataset,
    validate_real_ieee_cis_dataset,
    detect_dataset_provenance_type,
    SchemaValidationError
)
from src.data.make_dataset import ingest_real_ieee_cis, RealDataBlockedError

def test_detect_dataset_type():
    synthetic_df = pd.DataFrame({
        "TransactionID": [1, 2],
        "isFraud": [0, 1],
        "TransactionDT": [100, 200],
        "TransactionAmt": [50.0, 100.0],
        "card1": [1000, 2000]
    })
    assert detect_dataset_provenance_type(synthetic_df) == "SYNTHETIC_BENCHMARK"
    assert validate_synthetic_dataset(synthetic_df) is True

def test_real_data_gate_blocks_without_credentials(monkeypatch):
    """Verify that ingest_real_ieee_cis explicitly raises RealDataBlockedError when credentials are missing."""
    monkeypatch.delenv("KAGGLE_USERNAME", raising=False)
    monkeypatch.delenv("KAGGLE_KEY", raising=False)
    with pytest.raises(RealDataBlockedError, match=r"\[BLOCKED: REAL DATA\]"):
        ingest_real_ieee_cis()

def test_schema_validator_catches_non_monotonic_time():
    bad_df = pd.DataFrame({
        "TransactionID": [1, 2],
        "isFraud": [0, 1],
        "TransactionDT": [200, 100],  # Out of chronological order
        "TransactionAmt": [50.0, 100.0],
        "card1": [1000, 2000]
    })
    with pytest.raises(SchemaValidationError, match="monotonically increasing"):
        validate_synthetic_dataset(bad_df)
