import numpy as np
from sklearn.svm import SVC
import logging
from src.models.quantum.projected_kernel import compute_kernel_matrix, compute_projected_kernel_matrix
from src.models.quantum.feature_encoding import n_qubits

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumExpert:
    """
    [IMPLEMENTED] Genuine Quantum Expert using PennyLane Quantum Kernel + SVC.
    Supports:
      - 'fast_fidelity': Exact statevector fidelity quantum kernel |<psi(x1)|psi(x2)>|^2
      - 'projected': True projected quantum kernel (PQK) via 1-qubit Pauli expectation observables
      - 'inversion_test': Pairwise circuit simulation (hardware-equivalent)
    """
    def __init__(self, method='fast_fidelity', C=1.0, gamma=1.0, random_state=42):
        self.method = method
        self.C = C
        self.gamma = gamma
        self.random_state = random_state
        self.model_ = None
        self.X_train_ = None
        self.y_train_ = None
        self.n_qubits = n_qubits

    def fit(self, X_train, y_train):
        """
        Fits the Quantum Expert on escalated training transactions.
        Precomputes the training Gram matrix and fits scikit-learn SVC.
        """
        self.X_train_ = np.asarray(X_train)
        self.y_train_ = np.asarray(y_train)
        
        # Check if single class present (edge case in small budgets)
        unique_classes = np.unique(self.y_train_)
        if len(unique_classes) < 2:
            logging.warning(f"QuantumExpert.fit: only one class ({unique_classes[0]}) in training escalated traffic.")
            
        if self.method == 'projected':
            K_train = compute_projected_kernel_matrix(self.X_train_, gamma=self.gamma)
        else:
            K_train = compute_kernel_matrix(self.X_train_, method=self.method)
            
        # Regularization / stabilization for PSD
        # In case of small numerical noise, project eigenvalues to >= 0
        w, v = np.linalg.eigh(K_train)
        w_clipped = np.maximum(w, 1e-10)
        K_train = v @ np.diag(w_clipped) @ v.T
        K_train = 0.5 * (K_train + K_train.T)
        np.fill_diagonal(K_train, 1.0)
        
        self.model_ = SVC(
            kernel='precomputed',
            C=self.C,
            probability=True,
            random_state=self.random_state
        )
        self.model_.fit(K_train, self.y_train_)
        return self

    def predict_proba(self, X_test):
        """
        Computes rectangular kernel matrix K(X_test, X_train) and evaluates probabilities.
        Returns: array of shape (N_test, 2)
        """
        if self.model_ is None or self.X_train_ is None:
            raise RuntimeError("QuantumExpert must be fitted before predict_proba.")
            
        X_test_arr = np.asarray(X_test)
        
        if len(X_test_arr) == 0:
            return np.empty((0, 2))
            
        if self.method == 'projected':
            K_test = compute_projected_kernel_matrix(X_test_arr, self.X_train_, gamma=self.gamma)
        else:
            K_test = compute_kernel_matrix(X_test_arr, self.X_train_, method=self.method)
            
        return self.model_.predict_proba(K_test)

    def predict(self, X_test):
        probs = self.predict_proba(X_test)
        if len(probs) == 0:
            return np.empty(0, dtype=int)
        return (probs[:, 1] >= 0.5).astype(int)

    def get_hyperparameters(self):
        return {
            "model_type": "QuantumExpert",
            "kernel_method": self.method,
            "n_qubits": self.n_qubits,
            "C": self.C,
            "gamma": self.gamma,
            "random_state": self.random_state
        }
