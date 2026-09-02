import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate_classification(y_true, y_pred):

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    report = classification_report(
        y_true,
        y_pred,
        zero_division=0
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "confusion_matrix": cm,
        "classification_report": report
    }


def print_classification_results(
    y_true,
    y_pred
):

    results = evaluate_classification(
        y_true,
        y_pred
    )

    print("\n========================================")
    print("CLASSIFICATION MODEL RESULTS")
    print("========================================")

    print(
        "Accuracy :",
        round(results["accuracy"], 4)
    )

    print(
        "Precision:",
        round(results["precision"], 4)
    )

    print(
        "Recall   :",
        round(results["recall"], 4)
    )

    print(
        "F1 Score :",
        round(results["f1_score"], 4)
    )

    print("\nConfusion Matrix:")
    print(
        results["confusion_matrix"]
    )

    print("\nClassification Report:")
    print(
        results["classification_report"]
    )

    return results