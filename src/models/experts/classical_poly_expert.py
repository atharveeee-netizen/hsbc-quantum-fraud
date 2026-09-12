import numpy as np
from sklearn.svm import SVC
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClassicalPolyExpert:
    """
    [IMPLEMENTED] Non-linear Polynomial Kernel Control (Degree 3).
    Alternative classical kernel control alongside RBF.
    """
    def __init__(self, degree=3, C=1.0, random_state=42):
        self.degree = degree
        self.C = C
        self.random_state = random_state
        self.model_ = None

    def fit(self, X_train, y_train):
        self.model_ = SVC(
            kernel='poly',
            degree=self.degree,
            C=self.C,
            probability=True,
            random_state=self.random_state
        )
        self.model_.fit(np.asarray(X_train), np.asarray(y_train))
        return self

    def predict_proba(self, X_test):
        if self.model_ is None:
            raise RuntimeError("ClassicalPolyExpert must be fitted before predict_proba.")
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
            "model_type": "ClassicalPolyExpert",
            "kernel": "poly",
            "degree": self.degree,
            "C": self.C,
            "random_state": self.random_state
        }
