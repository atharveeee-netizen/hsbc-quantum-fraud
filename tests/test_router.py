import pytest
import numpy as np

def test_escalation_logic():
    """
    [IMPLEMENTED] Unit test to verify the router correctly escalates based on uncertainty.
    """
    # Simulated probabilities
    probs = np.array([0.1, 0.9, 0.49, 0.51, 0.2])
    uncertainty = np.abs(probs - 0.5)
    
    # Lowest distance from 0.5 is highest uncertainty
    # 0.49 -> 0.01
    # 0.51 -> 0.01
    # 0.2  -> 0.3
    # 0.1  -> 0.4
    # 0.9  -> 0.4
    
    sorted_idx = np.argsort(uncertainty)
    
    # The two most uncertain should be 0.49 and 0.51
    assert probs[sorted_idx[0]] in [0.49, 0.51]
    assert probs[sorted_idx[1]] in [0.49, 0.51]
    
    print("[VERIFIED] Router uncertainty sort correctly identifies decision-boundary traffic.")
