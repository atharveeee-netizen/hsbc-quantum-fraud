import pytest
import numpy as np
from src.evaluation.noisy_simulation import run_noisy_simulation

def test_noisy_simulation_execution():
    """
    [IMPLEMENTED] Unit test to verify depolarizing noise model execution and output integrity.
    """
    report, df_noise = run_noisy_simulation(noise_rates=(0.0, 0.05), n_samples=20, seed=42)
    assert len(df_noise) == 2
    assert df_noise.iloc[0]['mean_state_purity'] >= df_noise.iloc[1]['mean_state_purity']
    assert 0.0 <= df_noise.iloc[0]['test_auprc'] <= 1.0

