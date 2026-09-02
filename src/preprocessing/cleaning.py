# ============================================================
# RAILPULSE AI
# DATA CLEANING UTILITIES
# ============================================================

import pandas as pd
import numpy as np


def remove_duplicates(df):
    """Remove duplicate rows from dataframe."""

    df = df.copy()

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Duplicates removed: {before - after}")

    return df


def clean_column_names(df):
    """Standardize dataframe column names."""

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df


def handle_missing_values(df):
    """Fill missing values using median or mode."""

    df = df.copy()

    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):

            median_value = df[column].median()

            if pd.isna(median_value):
                median_value = 0

            df[column] = df[column].fillna(median_value)

        else:

            mode = df[column].mode()

            if not mode.empty:
                fill_value = mode.iloc[0]
            else:
                fill_value = "Unknown"

            df[column] = df[column].fillna(fill_value)

    return df


def handle_infinite_values(df):
    """Replace infinite values and handle missing values."""

    df = df.copy()

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    return handle_missing_values(df)


def clean_data(df):
    """Run the complete data cleaning pipeline."""

    df = df.copy()

    df = clean_column_names(df)

    df = remove_duplicates(df)

    df = handle_infinite_values(df)

    return df
