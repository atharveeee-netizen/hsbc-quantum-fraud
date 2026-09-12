import pennylane as qml
import numpy as np

# [DESIGN CHOICE] We use a 2-qubit system because we are currently using 2 features.
n_qubits = 2

def scale_to_pi(X):
    """
    [IMPLEMENTED] Maps standardized features deterministically into [-pi, pi].
    Using an arctan mapping to handle outliers smoothly without truncating.
    """
    return np.arctan(X) * 2

def quantum_feature_map(x):
    """
    [IMPLEMENTED] A 2-layer AngleEmbedding + BasicEntanglerLayers.
    x is a single data point of shape (2,)
    """
    # Layer 1: Angle Embedding (Rotation around X axis)
    qml.AngleEmbedding(x, wires=range(n_qubits), rotation='X')
    
    # Layer 2: Entanglement
    weights = np.zeros((1, n_qubits)) # Fixed dummy weights for structural entanglement
    qml.BasicEntanglerLayers(weights, wires=range(n_qubits))
