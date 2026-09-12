import numpy as np
from sklearn.neural_network import MLPClassifier
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClassicalMLPExpert:
    """
    [IMPLEMENTED] Strong Neural Network Classical Expert Control (Multi-Layer Perceptron).
    Architecture: 2 hidden layers (32, 16) with ReLU, L2 regularization, and early stopping.
    Trained strictly on escalated training traffic.
    """
    def __init__(self, hidden_layer_sizes=(32, 16), alpha=1e-3, max_iter=200, random_state=42):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.alpha = alpha
        self.max_iter = max_iter
        self.random_state = random_state
        self.model_ = None

    def fit(self, X_train, y_train):
        X_arr = np.asarray(X_train)
        y_arr = np.asarray(y_train)
        
        self.model_ = MLPClassifier(
            hidden_layer_sizes=self.hidden_layer_sizes,
            activation='relu',
            alpha=self.alpha,
            max_iter=self.max_iter,
            early_stopping=True,
            n_iter_no_change=10,
            random_state=self.random_state
        )
        self.model_.fit(X_arr, y_arr)
        return self

    def predict_proba(self, X_test):
        if self.model_ is None:
            raise RuntimeError("ClassicalMLPExpert must be fitted before predict_proba.")
        X_arr = np.asarray(X_test)
        if len(X_arr) == 0:
            return np.empty((0, 2))
        return self.model_.predict_proba(X_arr)

    def predict(self, X_test):
        probs = self.predict_proba(X_test)
        if len(probs) == 0:
            return np.empty(0, dtype=int)
        return (probs[:, 1] >= 0.5).astype(int)

    def get_hyperparameters(self):
        return {
            "model_type": "ClassicalMLPExpert",
            "hidden_layer_sizes": self.hidden_layer_sizes,
            "alpha": self.alpha,
            "max_iter": self.max_iter,
            "random_state": self.random_state
        }
