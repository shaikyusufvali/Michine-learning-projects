# ============================================================
# RAILPULSE AI
# PREDICTION TESTS
# ============================================================

from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data" / "raw"


def load_model(model_path):
    """
    Load a saved machine learning model.
    """

    assert model_path.exists(), (
        f"Model not found: {model_path}"
    )

    return joblib.load(model_path)


def test_classification_prediction():
    """
    Test delay classification model prediction.
    """

    model_path = (
        MODELS_DIR
        / "classification"
        / "delay_classifier.pkl"
    )

    data_path = DATA_DIR / "train_data.csv"

    model = load_model(model_path)

    assert data_path.exists()

    df = pd.read_csv(data_path)

    feature_names = list(model.feature_names_in_)

    assert all(
        feature in df.columns
        for feature in feature_names
    )

    X = df[feature_names].head(5)

    predictions = model.predict(X)

    assert len(predictions) == len(X)


def test_passenger_demand_prediction():
    """
    Test passenger demand regression model prediction.
    """

    model_path = (
        MODELS_DIR
        / "demand"
        / "passenger_demand.pkl"
    )

    data_path = DATA_DIR / "passenger_data.csv"

    model = load_model(model_path)

    assert data_path.exists()

    df = pd.read_csv(data_path)

    feature_names = list(model.feature_names_in_)

    assert all(
        feature in df.columns
        for feature in feature_names
    )

    X = df[feature_names].head(5)

    predictions = model.predict(X)

    assert len(predictions) == len(X)


def test_maintenance_prediction():
    """
    Test predictive maintenance model prediction.
    """

    model_path = (
        MODELS_DIR
        / "maintenance"
        / "maintenance_model.pkl"
    )

    data_path = DATA_DIR / "maintenance_data.csv"

    model = load_model(model_path)

    assert data_path.exists()

    df = pd.read_csv(data_path)

    feature_names = list(model.feature_names_in_)

    assert all(
        feature in df.columns
        for feature in feature_names
    )

    X = df[feature_names].head(5)

    predictions = model.predict(X)

    assert len(predictions) == len(X)


def test_crowd_prediction():
    """
    Test station crowd prediction model prediction.
    """

    model_path = (
        MODELS_DIR
        / "crowd"
        / "crowd_model.pkl"
    )

    data_path = DATA_DIR / "station_crowd.csv"

    model = load_model(model_path)

    assert data_path.exists()

    df = pd.read_csv(data_path)

    if "station" in df.columns and "station_encoded" in model.feature_names_in_:
        station_mapping = {
            "Hyderabad": 0,
            "Secunderabad": 1,
            "Vijayawada": 2,
            "Guntur": 3,
            "Warangal": 4,
            "Visakhapatnam": 5,
            "Tirupati": 6,
            "Nellore": 7,
            "Kurnool": 8,
            "Nizamabad": 9
        }

        df["station_encoded"] = (
            df["station"]
            .map(station_mapping)
            .fillna(0)
        )

    feature_names = list(model.feature_names_in_)

    assert all(
        feature in df.columns
        for feature in feature_names
    )

    X = df[feature_names].head(5)

    predictions = model.predict(X)

    assert len(predictions) == len(X)