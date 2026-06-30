import os

# Base Directories
ARTIFACTS_DIR = "artifacts"
DATA_DIR = os.path.join("notebook", "data")

# Dataset
DATASET_PATH = os.path.join(DATA_DIR, "students.csv")

# Saved Objects
MODEL_PATH = os.path.join(ARTIFACTS_DIR, "model.pkl")
PREPROCESSOR_PATH = os.path.join(ARTIFACTS_DIR, "preprocessor.pkl")