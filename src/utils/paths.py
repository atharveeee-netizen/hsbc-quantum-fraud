import os
from pathlib import Path

# Base project root (absolute)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Data subdirectories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "raw"
PROCESSED_DATA_PATH = DATA_DIR / "processed"
FEATURES_PATH = DATA_DIR / "features"
ROUTER_DATA_PATH = DATA_DIR / "router"
RESULTS_PATH = DATA_DIR / "results"

# Models and Artifacts
MODELS_DIR = PROJECT_ROOT / "src" / "models"
CLASSICAL_MODEL_DIR = MODELS_DIR / "classical"
EVIDENCE_DIR = PROJECT_ROOT / "docs" / "evidence"

# Ensure essential directories exist
for p in [RAW_DATA_PATH, PROCESSED_DATA_PATH, FEATURES_PATH, ROUTER_DATA_PATH, RESULTS_PATH, CLASSICAL_MODEL_DIR, EVIDENCE_DIR]:
    p.mkdir(parents=True, exist_ok=True)
