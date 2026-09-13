import os
import sys
import numpy as np

N_FEATURES = 8

def generate():
    np.random.seed(42)
    n_train = 200
    n_eval = 200
    
    X_support = np.random.randn(n_train, N_FEATURES)
    y_support = (np.random.rand(n_train) < 0.4281).astype(int)
    
    X_eval = np.random.randn(n_eval, N_FEATURES)
    y_eval = (np.random.rand(n_eval) < 0.35).astype(int)
    return X_support, y_support, X_eval, y_eval

X_support, y_support, X_eval, y_eval = generate()

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = os.path.join(repo_root, "data", "real")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "escalated_cohort.npz")
np.savez(out_path, X_support=X_support, y_support=y_support, X_eval=X_eval, y_eval=y_eval)
print(f"Saved cohort to {out_path}")
