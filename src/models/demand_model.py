# ============================================================
# RAILWAY AI INTELLIGENCE
# PASSENGER DEMAND PREDICTION MODEL
# ============================================================

import pandas as pd
import numpy as np
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = (
    BASE_DIR
    / "data"
    / "raw"
    / "passenger_data.csv"
)

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "demand"
    / "passenger_demand.pkl"
)

PREDICTION_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "passenger_demand_predictions.csv"
)


# ============================================================
# TRAIN MODEL
# ============================================================

def train_demand_model():

    print("\n" + "=" * 60)
    print("TRAIN PASSENGER DEMAND MODEL")
    print("=" * 60)

    # Load data
    df = pd.read_csv(DATA_PATH)

    print("Dataset Shape:", df.shape)

    # Target
    target = "passenger_count"

    # Numeric features
    X = df.select_dtypes(include=np.number).drop(
        columns=[target],
        errors="ignore"
    )

    y = df[target]

    print("Features:", list(X.columns))
    print("Target:", target)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )

    # Train
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, y_pred)

    mse = mean_squared_error(
        y_test,
        y_pred
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_test,
        y_pred
    )

    print("\nModel Results")
    print("-" * 40)
    print("MAE  :", round(mae, 4))
    print("MSE  :", round(mse, 4))
    print("RMSE :", round(rmse, 4))
    print("R2   :", round(r2, 4))

    # Predictions
    predictions = pd.DataFrame({
        "actual_passenger_count": y_test.values,
        "predicted_passenger_count": y_pred
    })

    # Create directories
    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    PREDICTION_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save model
    joblib.dump(
        model,
        MODEL_PATH
    )

    # Save predictions
    predictions.to_csv(
        PREDICTION_PATH,
        index=False
    )

    print("\nModel saved:", MODEL_PATH)
    print("Predictions saved:", PREDICTION_PATH)

    return model


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    train_demand_model()