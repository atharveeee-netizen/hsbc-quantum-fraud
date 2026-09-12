import pytest
import numpy as np
from src.models.router.escalation_router import compute_uncertainty, select_escalated_indices

def test_uncertainty_calculation():
    probs = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    unc = compute_uncertainty(probs)
    assert np.allclose(unc, np.array([0.5, 0.25, 0.0, 0.25, 0.5]))

def test_select_escalated_budget_counts():
    probs = np.linspace(0.1, 0.9, 1000)
    for b in [0.5, 1.0, 2.0, 5.0, 10.0]:
        esc_idx, clr_idx = select_escalated_indices(probs, budget_pct=b, strategy='uncertainty')
        expected_count = int(np.round((b / 100.0) * len(probs)))
        assert len(esc_idx) == expected_count
        assert len(clr_idx) == len(probs) - expected_count
        # Ensure no overlap
        assert len(set(esc_idx).intersection(set(clr_idx))) == 0

def test_random_routing_reproducibility():
    probs = np.linspace(0.1, 0.9, 500)
    esc1, _ = select_escalated_indices(probs, budget_pct=5.0, strategy='random', random_state=42)
    esc2, _ = select_escalated_indices(probs, budget_pct=5.0, strategy='random', random_state=42)
    assert np.array_equal(esc1, esc2)
    
    esc3, _ = select_escalated_indices(probs, budget_pct=5.0, strategy='random', random_state=99)
    assert not np.array_equal(esc1, esc3)
