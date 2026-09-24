import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_regression(y_true, y_pred):

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "mae": mae,
        "mse": mse,
        "rmse": rmse,
        "r2_score": r2
    }


def print_regression_results(
    y_true,
    y_pred
):

    results = evaluate_regression(
        y_true,
        y_pred
    )

    print("\n========================================")
    print("REGRESSION MODEL RESULTS")
    print("========================================")

    print(
        "MAE  :",
        round(results["mae"], 4)
    )

    print(
        "MSE  :",
        round(results["mse"], 4)
    )

    print(
        "RMSE :",
        round(results["rmse"], 4)
    )

    print(
        "R²   :",
        round(results["r2_score"], 4)
    )

    return results