import pytest
import numpy as np
from src.models.quantum.projected_kernel import compute_kernel_matrix
from src.models.quantum.feature_encoding import scale_to_pi

def test_scale_to_pi():
    """
    [IMPLEMENTED] Verifies the arctan mapping bounds the features correctly.
    """
    X = np.array([-1000.0, 0.0, 1000.0])
    X_scaled = scale_to_pi(X)
    
    # Should be strictly bounded between -pi and pi
    assert np.all(X_scaled > -np.pi)
    assert np.all(X_scaled < np.pi)
    assert X_scaled[1] == 0.0

def test_kernel_matrix_properties():
    """
    [IMPLEMENTED] Validates the quantum kernel behaves like a valid Gram matrix.
    """
    # 3 random samples, 2 features
    X = np.random.randn(3, 2)
    
    K = compute_kernel_matrix(X)
    
    # 1. Dimensions
    assert K.shape == (3, 3)
    
    # 2. Symmetry
    assert np.allclose(K, K.T, atol=1e-6)
    
    # 3. Diagonal is 1.0 (overlap with self)
    assert np.allclose(np.diag(K), np.ones(3), atol=1e-6)
    
    # 4. Values bound between 0 and 1 (probabilities)
    assert np.all(K >= 0.0)
    assert np.all(K <= 1.0)
