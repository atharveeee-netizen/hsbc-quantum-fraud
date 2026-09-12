import pytest
from src.utils.provenance import (
    create_provenance_record,
    validate_provenance_record,
    build_master_provenance_manifest,
    REQUIRED_PROVENANCE_FIELDS
)

def test_provenance_record_completeness():
    """Verify that a generated provenance record contains all 18 required fields."""
    rec = create_provenance_record()
    for field in REQUIRED_PROVENANCE_FIELDS:
        assert field in rec, f"Missing required provenance field: {field}"
    assert rec["dataset_status"] == "[SYNTHETIC] [MEASURED] [VERIFIED]"

def test_provenance_firewall_blocks_synthetic_masquerading_as_real():
    """Verify that attempting to label synthetic data as real data raises ValueError."""
    with pytest.raises(ValueError, match="Provenance integrity violation"):
        create_provenance_record(
            dataset_source="synthetic_ieee_cis_benchmark",
            dataset_status="[REAL DATA] [VERIFIED]"
        )

def test_master_provenance_manifest():
    """Verify that master provenance manifest builds and records real data status as BLOCKED."""
    manifest = build_master_provenance_manifest()
    assert manifest["real_data_status"] == "[BLOCKED: REAL DATA]"
    assert manifest["global_provenance_verdict"] == "[SYNTHETIC] [MEASURED] [VERIFIED] [REAL DATA BLOCKED] [QUANTUM ADVANTAGE NOT DEMONSTRATED]"
    assert manifest["total_indexed_artifacts"] >= 15
