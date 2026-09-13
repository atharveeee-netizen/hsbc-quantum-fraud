import os
import sys
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

N_FEATURES = 8

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
real_test_path = os.path.join(repo_root, "data", "real", "test_raw.parquet")

n_samples = 200

print(f"Loading {real_test_path}")
df = pd.read_parquet(real_test_path)
feature_cols = ['TransactionAmt', 'card1', 'card2', 'card3', 'card5', 'C1', 'C2', 'C5', 'C13', 'D1']
X_raw = df[feature_cols].values
y_all = df['isFraud'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)
pca = PCA(n_components=N_FEATURES, random_state=42)
X_pca = pca.fit_transform(X_scaled)

fraud_idx = np.where(y_all == 1)[0]
nonfraud_idx = np.where(y_all == 0)[0]

np.random.seed(42)
n_fraud = int(n_samples * 0.4281)
n_nonfraud = n_samples - n_fraud

sel_fraud = np.random.choice(fraud_idx, size=n_fraud, replace=False)
sel_non = np.random.choice(nonfraud_idx, size=n_nonfraud, replace=False)
sel = np.concatenate([sel_fraud, sel_non])
np.random.shuffle(sel)

X_support = X_pca[sel]
y_support = y_all[sel]

rem_fraud = np.setdiff1d(fraud_idx, sel_fraud)
rem_non = np.setdiff1d(nonfraud_idx, sel_non)
test_f = np.random.choice(rem_fraud, size=min(100, len(rem_fraud)), replace=False)
test_n = np.random.choice(rem_non, size=min(200, len(rem_non)), replace=False)
test_idx = np.concatenate([test_f, test_n])
np.random.shuffle(test_idx)

X_eval = X_pca[test_idx]
y_eval = y_all[test_idx]

out_dir = os.path.join(repo_root, "data", "real")
out_path = os.path.join(out_dir, "escalated_cohort.npz")
np.savez(out_path, X_support=X_support, y_support=y_support, X_eval=X_eval, y_eval=y_eval)
print(f"Saved cohort to {out_path} from parquet")
