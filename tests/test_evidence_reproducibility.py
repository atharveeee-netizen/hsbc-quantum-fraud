import pytest
from scripts.verify_evidence_integrity import verify_all_evidence

def test_evidence_integrity_audit():
    """
    [IMPLEMENTED] Regression test that asserts 0 discrepancies across all generated evidence.
    """
    failures = verify_all_evidence()
    assert len(failures) == 0, f"Evidence audit failed with: {failures}"
