import pennylane as qml
import numpy as np
from src.models.quantum.feature_encoding import quantum_feature_map, scale_to_pi, n_qubits
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# [DESIGN CHOICE] We use default.qubit (exact simulator) for the base implementation (Phase 14).
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def compute_overlap(x1, x2):
    """
    [IMPLEMENTED] Evaluates the inner product |<psi(x1)|psi(x2)>|^2 using the inversion test.
    """
    quantum_feature_map(x1)
    qml.adjoint(quantum_feature_map)(x2)
    return qml.probs(wires=range(n_qubits))

def compute_kernel_matrix(X1, X2=None):
    """
    [IMPLEMENTED] Computes the full Gram matrix.
    If X2 is None, computes the symmetric K(X1, X1).
    """
    logging.info(f"Mapping classical features to angles...")
    X1_angles = scale_to_pi(X1.values if hasattr(X1, 'values') else X1)
    
    if X2 is None:
        X2_angles = X1_angles
        symmetric = True
    else:
        X2_angles = scale_to_pi(X2.values if hasattr(X2, 'values') else X2)
        symmetric = False
        
    N1 = len(X1_angles)
    N2 = len(X2_angles)
    
    K = np.zeros((N1, N2))
    
    logging.info(f"Evaluating {N1}x{N2} kernel matrix on simulator...")
    for i in range(N1):
        for j in range(N2):
            if symmetric and j < i:
                # Use symmetry
                K[i, j] = K[j, i]
            elif symmetric and i == j:
                # Identity overlap
                K[i, j] = 1.0
            else:
                # Probability of measuring |00> after U(x2)^\dagger U(x1)
                K[i, j] = compute_overlap(X1_angles[i], X2_angles[j])[0]
                
    logging.info("[VERIFIED] Kernel matrix evaluation complete.")
    return K
