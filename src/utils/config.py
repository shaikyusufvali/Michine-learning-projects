# ============================================================
# RAILPULSE AI
# PROJECT CONFIGURATION
# ============================================================

from pathlib import Path


# ============================================================
# PROJECT ROOT
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]


# ============================================================
# MAIN DIRECTORIES
# ============================================================

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = BASE_DIR / "models"

NOTEBOOKS_DIR = BASE_DIR / "notebooks"

SRC_DIR = BASE_DIR / "src"

DASHBOARD_DIR = BASE_DIR / "dashboard"

TESTS_DIR = BASE_DIR / "tests"


# ============================================================
# RAW DATA FILES
# ============================================================

TRAIN_DATA_PATH = (
    RAW_DATA_DIR / "train_data.csv"
)

PASSENGER_DATA_PATH = (
    RAW_DATA_DIR / "passenger_data.csv"
)

MAINTENANCE_DATA_PATH = (
    RAW_DATA_DIR / "maintenance_data.csv"
)

STATION_CROWD_DATA_PATH = (
    RAW_DATA_DIR / "station_crowd.csv"
)


# ============================================================
# PROCESSED DATA FILES
# ============================================================

DELAY_PROCESSED_PATH = (
    PROCESSED_DATA_DIR / "delay_processed.csv"
)

PASSENGER_PROCESSED_PATH = (
    PROCESSED_DATA_DIR / "passenger_processed.csv"
)

MAINTENANCE_PROCESSED_PATH = (
    PROCESSED_DATA_DIR / "maintenance_processed.csv"
)

CROWD_PROCESSED_PATH = (
    PROCESSED_DATA_DIR / "crowd_processed.csv"
)


# ============================================================
# FEATURE DATA FILES
# ============================================================

DELAY_FEATURES_PATH = (
    PROCESSED_DATA_DIR / "delay_features.csv"
)

PASSENGER_FEATURES_PATH = (
    PROCESSED_DATA_DIR / "passenger_features.csv"
)

MAINTENANCE_FEATURES_PATH = (
    PROCESSED_DATA_DIR / "maintenance_features.csv"
)

CROWD_FEATURES_PATH = (
    PROCESSED_DATA_DIR / "crowd_features.csv"
)


# ============================================================
# MODEL FILES
# ============================================================

DELAY_MODEL_PATH = (
    MODELS_DIR / "delay" / "delay_model.pkl"
)

CLASSIFICATION_MODEL_PATH = (
    MODELS_DIR
    / "classification"
    / "delay_classifier.pkl"
)

DEMAND_MODEL_PATH = (
    MODELS_DIR
    / "demand"
    / "passenger_demand.pkl"
)

MAINTENANCE_MODEL_PATH = (
    MODELS_DIR
    / "maintenance"
    / "maintenance_model.pkl"
)

CROWD_MODEL_PATH = (
    MODELS_DIR
    / "crowd"
    / "crowd_model.pkl"
)


# ============================================================
# PROJECT SETTINGS
# ============================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20


# ============================================================
# MODEL SETTINGS
# ============================================================

N_ESTIMATORS = 200

MAX_DEPTH = 15


# ============================================================
# APPLICATION SETTINGS
# ============================================================

APP_TITLE = "RailPulse AI"

APP_DESCRIPTION = (
    "AI-powered Railway Intelligence and "
    "Prediction System"
)


# ============================================================
# CREATE DIRECTORIES IF NOT EXIST
# ============================================================

for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    NOTEBOOKS_DIR,
    SRC_DIR,
    DASHBOARD_DIR,
    TESTS_DIR,
]:
    directory.mkdir(
        parents=True,
        exist_ok=True
    )