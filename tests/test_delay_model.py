# ============================================================
# RAILPULSE AI
# DELAY MODEL TESTS
# ============================================================

from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "delay" / "delay_model.pkl"
DATA_PATH = BASE_DIR / "data" / "raw" / "train_data.csv"


def test_delay_model_file_exists():
    """
    Check whether the trained delay model exists.
    """

    assert MODEL_PATH.exists(), (
        f"Delay model not found: {MODEL_PATH}"
    )


def test_delay_dataset_exists():
    """
    Check whether the delay training dataset exists.
    """

    assert DATA_PATH.exists(), (
        f"Training dataset not found: {DATA_PATH}"
    )


def test_delay_model_can_be_loaded():
    """
    Check whether the saved delay model can be loaded.
    """

    assert MODEL_PATH.exists()

    model = joblib.load(MODEL_PATH)

    assert model is not None


def test_delay_dataset_can_be_loaded():
    """
    Check whether the training dataset can be loaded.
    """

    assert DATA_PATH.exists()

    df = pd.read_csv(DATA_PATH)

    assert not df.empty
    assert len(df.columns) > 0


def test_delay_model_has_features():
    """
    Check whether the trained model contains feature information.
    """

    assert MODEL_PATH.exists()

    model = joblib.load(MODEL_PATH)

    assert hasattr(model, "feature_names_in_")
    assert len(model.feature_names_in_) > 0


def test_delay_model_can_predict():
    """
    Check whether the delay model can make predictions
    using its trained features.
    """

    assert MODEL_PATH.exists()

    model = joblib.load(MODEL_PATH)

    feature_names = list(model.feature_names_in_)

    data = pd.read_csv(DATA_PATH)

    available_features = [
        column
        for column in feature_names
        if column in data.columns
    ]

    assert len(available_features) == len(feature_names), (
        "Dataset does not contain all model features."
    )

    X = data[feature_names].head(5)

    predictions = model.predict(X)

    assert len(predictions) == len(X)
    assert len(predictions) > 0