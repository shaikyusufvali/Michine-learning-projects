# ============================================================
# RAILPULSE AI
# CATEGORICAL ENCODING UTILITIES
# ============================================================

import pandas as pd


# ============================================================
# LABEL ENCODING
# ============================================================

def label_encode(df, columns=None):
    """
    Convert categorical columns into numeric category codes.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    columns : list, optional
        Columns to encode.
        If None, all object/category columns are encoded.

    Returns
    -------
    pandas.DataFrame
        Encoded dataframe.
    """

    df = df.copy()

    # Automatically find categorical columns
    if columns is None:

        columns = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    # Encode each column
    for column in columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .astype("category")
                .cat.codes
            )

    return df


# ============================================================
# ONE-HOT ENCODING
# ============================================================

def one_hot_encode(df, columns=None):
    """
    Convert categorical columns into one-hot encoded columns.
    """

    df = df.copy()

    if columns is None:

        columns = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    if columns:

        df = pd.get_dummies(
            df,
            columns=columns,
            drop_first=False
        )

    return df


# ============================================================
# ENCODE ALL CATEGORICAL COLUMNS
# ============================================================

def encode_categorical_columns(df):
    """
    Encode all categorical columns using label encoding.
    """

    return label_encode(df)