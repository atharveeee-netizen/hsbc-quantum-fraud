import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClassicalRBFExpert:
    """
    [IMPLEMENTED] Fair Classical RBF Support Vector Classifier Control.
    Evaluated on the exact same escalated transactions and features as QuantumExpert.
    Supports internal cross-validation tuning strictly on training data.
    """
    def __init__(self, C=1.0, gamma='scale', tune_cv=True, random_state=42):
        self.C = C
        self.gamma = gamma
        self.tune_cv = tune_cv
        self.random_state = random_state
        self.model_ = None
        self.best_params_ = {"C": C, "gamma": gamma}

    def fit(self, X_train, y_train):
        """
        Fits the RBF SVC on escalated training transactions.
        If tune_cv=True, conducts 3-fold stratified cross-validation on X_train.
        """
        X_train_arr = np.asarray(X_train)
        y_train_arr = np.asarray(y_train)
        
        unique_classes, counts = np.unique(y_train_arr, return_counts=True)
        if len(unique_classes) < 2:
            logging.warning(f"ClassicalRBFExpert.fit: only one class ({unique_classes[0]}) in training escalated traffic.")
            
        min_class_count = np.min(counts) if len(counts) > 0 else 0
        
        if self.tune_cv and min_class_count >= 3:
            param_grid = {
                'C': [0.1, 1.0, 10.0],
                'gamma': ['scale', 0.1, 1.0]
            }
            cv = StratifiedKFold(n_splits=min(3, min_class_count), shuffle=True, random_state=self.random_state)
            base_svc = SVC(kernel='rbf', probability=True, random_state=self.random_state)
            grid = GridSearchCV(base_svc, param_grid, cv=cv, scoring='roc_auc', n_jobs=1)
            grid.fit(X_train_arr, y_train_arr)
            self.model_ = grid.best_estimator_
            self.best_params_ = grid.best_params_
            logging.info(f"ClassicalRBFExpert tuned best params: {self.best_params_}")
        else:
            self.model_ = SVC(
                kernel='rbf',
                C=self.C,
                gamma=self.gamma,
                probability=True,
                random_state=self.random_state
            )
            self.model_.fit(X_train_arr, y_train_arr)
            self.best_params_ = {"C": self.C, "gamma": self.gamma}
            
        return self

    def predict_proba(self, X_test):
        if self.model_ is None:
            raise RuntimeError("ClassicalRBFExpert must be fitted before predict_proba.")
        X_test_arr = np.asarray(X_test)
        if len(X_test_arr) == 0:
            return np.empty((0, 2))
        return self.model_.predict_proba(X_test_arr)

    def predict(self, X_test):
        probs = self.predict_proba(X_test)
        if len(probs) == 0:
            return np.empty(0, dtype=int)
        return (probs[:, 1] >= 0.5).astype(int)

    def get_hyperparameters(self):
        return {
            "model_type": "ClassicalRBFExpert",
            "kernel": "rbf",
            "tuned": self.tune_cv,
            "best_params": self.best_params_,
            "random_state": self.random_state
        }
