import pennylane as qml
import numpy as np
from src.models.quantum.feature_encoding import quantum_feature_map, scale_to_pi, n_qubits
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# [DESIGN CHOICE] Exact state simulator for ideal circuit evaluation
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def compute_overlap(x1, x2):
    """
    [IMPLEMENTED] Evaluates the inner product |<psi(x1)|psi(x2)>|^2 using the inversion test.
    Native QPU / shot-based execution interface.
    """
    quantum_feature_map(x1)
    qml.adjoint(quantum_feature_map)(x2)
    return qml.probs(wires=range(n_qubits))

@qml.qnode(dev)
def get_quantum_state(x):
    """
    [IMPLEMENTED] Evaluates the full statevector |psi(x)> = U(x)|0>.
    """
    quantum_feature_map(x)
    return qml.state()

@qml.qnode(dev)
def get_pauli_projections(x):
    """
    [IMPLEMENTED] Projected Quantum Representation (Huang et al., 2021).
    Extracts 1-qubit reduced Pauli expectations (X, Y, Z) on each wire.
    For n qubits, produces a 3*n real feature vector in [-1, 1]^(3n).
    """
    quantum_feature_map(x)
    return (
        [qml.expval(qml.PauliX(w)) for w in range(n_qubits)] +
        [qml.expval(qml.PauliY(w)) for w in range(n_qubits)] +
        [qml.expval(qml.PauliZ(w)) for w in range(n_qubits)]
    )

def compute_kernel_matrix(X1, X2=None, method='fast_fidelity'):
    """
    [IMPLEMENTED] Computes the Gram matrix.
    If X2 is None, computes the symmetric K(X1, X1).
    Methods:
      - 'fast_fidelity': Computes statevectors and inner products (|Psi1 @ Psi2.T|^2).
                         Mathematically identical to inversion test, O(N) instead of O(N^2) simulations.
      - 'inversion_test': Explicit pairwise circuit evaluations via compute_overlap (hardware baseline).
      - 'projected': True projected quantum kernel using Pauli expectation features.
    """
    X1_angles = scale_to_pi(X1.values if hasattr(X1, 'values') else np.asarray(X1))
    
    if X2 is None:
        X2_angles = X1_angles
        symmetric = True
    else:
        X2_angles = scale_to_pi(X2.values if hasattr(X2, 'values') else np.asarray(X2))
        symmetric = False
        
    N1 = len(X1_angles)
    N2 = len(X2_angles)
    
    if method == 'fast_fidelity':
        states1 = np.array([get_quantum_state(x) for x in X1_angles])
        if symmetric:
            states2 = states1
        else:
            states2 = np.array([get_quantum_state(x) for x in X2_angles])
        
        # Inner product: |<psi_i | psi_j>|^2
        K = np.abs(states1 @ states2.conj().T) ** 2
        
        if symmetric:
            # Enforce numerical symmetry and exact unit diagonal
            K = 0.5 * (K + K.T)
            np.fill_diagonal(K, 1.0)
            
        K = np.clip(K, 0.0, 1.0)
        return K
        
    elif method == 'projected':
        return compute_projected_kernel_matrix(X1, X2)
        
    elif method == 'inversion_test':
        K = np.zeros((N1, N2))
        for i in range(N1):
            for j in range(N2):
                if symmetric and j < i:
                    K[i, j] = K[j, i]
                elif symmetric and i == j:
                    K[i, j] = 1.0
                else:
                    K[i, j] = compute_overlap(X1_angles[i], X2_angles[j])[0]
        K = np.clip(K, 0.0, 1.0)
        return K
    else:
        raise ValueError(f"Unknown kernel method: {method}")

def compute_projected_kernel_matrix(X1, X2=None, gamma=1.0):
    """
    [IMPLEMENTED] Projected Quantum Kernel (PQK) via 1-qubit Pauli projections.
    k_PQK(x, x') = exp(-gamma * ||phi_Q(x) - phi_Q(x')||^2)
    where phi_Q(x) in R^(3*n_qubits).
    """
    X1_angles = scale_to_pi(X1.values if hasattr(X1, 'values') else np.asarray(X1))
    symmetric = (X2 is None)
    
    phi1 = np.array([get_pauli_projections(x) for x in X1_angles])
    if symmetric:
        phi2 = phi1
    else:
        X2_angles = scale_to_pi(X2.values if hasattr(X2, 'values') else np.asarray(X2))
        phi2 = np.array([get_pauli_projections(x) for x in X2_angles])
        
    # Classical RBF kernel over projected quantum representations
    # Squared Euclidean distance ||phi1_i - phi2_j||^2
    dist_sq = np.sum(phi1**2, axis=1, keepdims=True) + np.sum(phi2**2, axis=1, keepdims=True).T - 2.0 * (phi1 @ phi2.T)
    dist_sq = np.maximum(dist_sq, 0.0) # avoid negative numerical artifacts
    K = np.exp(-gamma * dist_sq)
    
    if symmetric:
        K = 0.5 * (K + K.T)
        np.fill_diagonal(K, 1.0)
        
    return np.clip(K, 0.0, 1.0)
