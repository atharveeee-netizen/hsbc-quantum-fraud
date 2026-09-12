import numpy as np
import lightgbm as lgb
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClassicalGBMExpert:
    """
    [IMPLEMENTED] Strong Classical Gradient Boosting Control.
    LightGBM model trained exclusively on escalated training transactions.
    """
    def __init__(self, n_estimators=50, max_depth=3, learning_rate=0.05, random_state=42):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.model_ = None

    def fit(self, X_train, y_train):
        X_train_arr = np.asarray(X_train)
        y_train_arr = np.asarray(y_train)
        
        unique_classes = np.unique(y_train_arr)
        if len(unique_classes) < 2:
            logging.warning(f"ClassicalGBMExpert.fit: only one class ({unique_classes[0]}) in training escalated traffic.")
            
        self.model_ = lgb.LGBMClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            learning_rate=self.learning_rate,
            random_state=self.random_state,
            verbose=-1
        )
        self.model_.fit(X_train_arr, y_train_arr)
        return self

    def predict_proba(self, X_test):
        if self.model_ is None:
            raise RuntimeError("ClassicalGBMExpert must be fitted before predict_proba.")
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
            "model_type": "ClassicalGBMExpert",
            "n_estimators": self.n_estimators,
            "max_depth": self.max_depth,
            "learning_rate": self.learning_rate,
            "random_state": self.random_state
        }
