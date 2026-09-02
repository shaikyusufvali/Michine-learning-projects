# ============================================================
# RAILPULSE AI
# FEATURE SCALING UTILITIES
# ============================================================

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def standard_scale(df, columns=None):
    """Apply StandardScaler to selected numeric columns."""

    df = df.copy()

    if columns is None:
        columns = df.select_dtypes(
            include=["number"]
        ).columns.tolist()

    scaler = StandardScaler()

    if columns:
        df[columns] = scaler.fit_transform(
            df[columns]
        )

    return df, scaler


def minmax_scale(df, columns=None):
    """Apply MinMaxScaler to selected numeric columns."""

    df = df.copy()

    if columns is None:
        columns = df.select_dtypes(
            include=["number"]
        ).columns.tolist()

    scaler = MinMaxScaler()

    if columns:
        df[columns] = scaler.fit_transform(
            df[columns]
        )

    return df, scaler


def scale_features(df, method="standard", columns=None):
    """Scale dataframe features using the selected method."""

    if method == "standard":

        return standard_scale(
            df,
            columns
        )

    elif method == "minmax":

        return minmax_scale(
            df,
            columns
        )

    else:

        raise ValueError(
            "Invalid scaling method. "
            "Use 'standard' or 'minmax'."
        )
