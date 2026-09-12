import pytest
import numpy as np
from src.models.experts.quantum_expert import QuantumExpert
from src.models.experts.classical_rbf_expert import ClassicalRBFExpert
from src.models.experts.classical_gbm_expert import ClassicalGBMExpert

@pytest.fixture
def dummy_traffic():
    np.random.seed(42)
    X_train = np.random.randn(30, 2)
    y_train = np.random.binomial(1, 0.4, size=30)
    X_test = np.random.randn(10, 2)
    y_test = np.random.binomial(1, 0.4, size=10)
    return X_train, y_train, X_test, y_test

def test_quantum_expert_interface(dummy_traffic):
    X_train, y_train, X_test, y_test = dummy_traffic
    q_exp = QuantumExpert(method='fast_fidelity', random_state=42)
    q_exp.fit(X_train, y_train)
    
    probs = q_exp.predict_proba(X_test)
    assert probs.shape == (10, 2)
    assert np.all(probs >= 0.0)
    assert np.all(probs <= 1.0)
    assert np.allclose(np.sum(probs, axis=1), 1.0)
    
    preds = q_exp.predict(X_test)
    assert preds.shape == (10,)
    assert set(np.unique(preds)).issubset({0, 1})

def test_classical_rbf_expert_interface(dummy_traffic):
    X_train, y_train, X_test, y_test = dummy_traffic
    rbf_exp = ClassicalRBFExpert(tune_cv=True, random_state=42)
    rbf_exp.fit(X_train, y_train)
    
    probs = rbf_exp.predict_proba(X_test)
    assert probs.shape == (10, 2)
    assert np.all(probs >= 0.0)
    assert np.all(probs <= 1.0)
    assert np.allclose(np.sum(probs, axis=1), 1.0)

def test_classical_gbm_expert_interface(dummy_traffic):
    X_train, y_train, X_test, y_test = dummy_traffic
    gbm_exp = ClassicalGBMExpert(n_estimators=10, random_state=42)
    gbm_exp.fit(X_train, y_train)
    
    probs = gbm_exp.predict_proba(X_test)
    assert probs.shape == (10, 2)
    assert np.all(probs >= 0.0)
    assert np.all(probs <= 1.0)
    assert np.allclose(np.sum(probs, axis=1), 1.0)

def test_classical_mlp_expert_interface(dummy_traffic):
    from src.models.experts.classical_mlp_expert import ClassicalMLPExpert
    X_train, y_train, X_test, y_test = dummy_traffic
    mlp_exp = ClassicalMLPExpert(hidden_layer_sizes=(8, 4), max_iter=50, random_state=42)
    mlp_exp.fit(X_train, y_train)
    
    probs = mlp_exp.predict_proba(X_test)
    assert probs.shape == (10, 2)
    assert np.all(probs >= 0.0)
    assert np.all(probs <= 1.0)
    assert np.allclose(np.sum(probs, axis=1), 1.0)

def test_classical_poly_expert_interface(dummy_traffic):
    from src.models.experts.classical_poly_expert import ClassicalPolyExpert
    X_train, y_train, X_test, y_test = dummy_traffic
    poly_exp = ClassicalPolyExpert(degree=2, C=1.0, random_state=42)
    poly_exp.fit(X_train, y_train)
    
    probs = poly_exp.predict_proba(X_test)
    assert probs.shape == (10, 2)
    assert np.all(probs >= 0.0)
    assert np.all(probs <= 1.0)
    assert np.allclose(np.sum(probs, axis=1), 1.0)

