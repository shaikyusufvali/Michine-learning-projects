# ============================================================
# RAILWAY AI INTELLIGENCE
# FEATURE ENGINEERING
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================================
# FEATURE ENGINEERING FUNCTION
# ============================================================

def create_features(df):
    df = df.copy()

    # --------------------------------------------------------
    # Datetime Features
    # --------------------------------------------------------

    datetime_columns = []

    for column in df.columns:
        if "date" in column.lower() or "time" in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], errors="coerce")

                if df[column].notna().any():
                    datetime_columns.append(column)

                    df[f"{column}_year"] = df[column].dt.year
                    df[f"{column}_month"] = df[column].dt.month
                    df[f"{column}_day"] = df[column].dt.day
                    df[f"{column}_dayofweek"] = df[column].dt.dayofweek
                    df[f"{column}_hour"] = df[column].dt.hour

                    # Original datetime column remove
                    df.drop(columns=[column], inplace=True)

            except Exception:
                pass

    # --------------------------------------------------------
    # Categorical Encoding
    # --------------------------------------------------------

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:
        df[column] = df[column].astype("category").cat.codes

    # --------------------------------------------------------
    # Replace Infinite Values
    # --------------------------------------------------------

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # --------------------------------------------------------
    # Fill Missing Values
    # --------------------------------------------------------

    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):

            median_value = df[column].median()

            if pd.isna(median_value):
                median_value = 0

            df[column] = df[column].fillna(median_value)

        else:

            df[column] = df[column].fillna("Unknown")

    return df


# ============================================================
# PROCESS ONE FILE
# ============================================================

def process_file(input_file, output_file):

    print("\n" + "=" * 60)
    print(f"Processing: {input_file.name}")
    print("=" * 60)

    df = pd.read_csv(input_file)

    print("Original Shape:", df.shape)

    df = create_features(df)

    print("Feature Engineered Shape:", df.shape)

    df.to_csv(output_file, index=False)

    print("Saved:", output_file)


# ============================================================
# MAIN
# ============================================================

def main():

    files = {
        "delay_processed.csv": "delay_features.csv",
        "passenger_processed.csv": "passenger_features.csv",
        "maintenance_processed.csv": "maintenance_features.csv",
        "crowd_processed.csv": "crowd_features.csv"
    }

    for input_name, output_name in files.items():

        input_file = PROCESSED_DIR / input_name
        output_file = PROCESSED_DIR / output_name

        if input_file.exists():

            process_file(
                input_file,
                output_file
            )

        else:

            print(f"\nFile not found: {input_file}")


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()