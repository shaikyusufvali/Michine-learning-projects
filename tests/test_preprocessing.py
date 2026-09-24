# ============================================================
# RAILPULSE AI
# PREPROCESSING TESTS
# ============================================================

import pandas as pd
import numpy as np

from src.preprocessing.cleaning import (
    clean_column_names,
    remove_duplicates,
    handle_missing_values,
    handle_infinite_values,
    clean_data
)

from src.preprocessing.encoding import (
    label_encode,
    one_hot_encode,
    encode_categorical_columns
)

from src.preprocessing.scaling import (
    standard_scale,
    minmax_scale,
    scale_features
)


# ============================================================
# CLEANING TESTS
# ============================================================

def test_clean_column_names():

    df = pd.DataFrame({
        "Train Name": ["Express"],
        "Delay-Minutes": [10]
    })

    result = clean_column_names(df)

    assert "train_name" in result.columns
    assert "delay_minutes" in result.columns


def test_remove_duplicates():

    df = pd.DataFrame({
        "train": ["A", "A", "B"],
        "delay": [10, 10, 20]
    })

    result = remove_duplicates(df)

    assert len(result) == 2


def test_handle_missing_values():

    df = pd.DataFrame({
        "delay": [10, np.nan, 20],
        "station": ["Hyderabad", None, "Guntur"]
    })

    result = handle_missing_values(df)

    assert result["delay"].isna().sum() == 0
    assert result["station"].isna().sum() == 0


def test_handle_infinite_values():

    df = pd.DataFrame({
        "delay": [10, np.inf, 20, -np.inf]
    })

    result = handle_infinite_values(df)

    assert np.isfinite(result["delay"]).all()


def test_clean_data():

    df = pd.DataFrame({
        "Train Name": ["Express", "Express", "Superfast"],
        "Delay-Minutes": [10, 10, np.nan]
    })

    result = clean_data(df)

    assert "train_name" in result.columns
    assert "delay_minutes" in result.columns
    assert len(result) == 2
    assert result.isna().sum().sum() == 0


# ============================================================
# ENCODING TESTS
# ============================================================

def test_label_encode():

    df = pd.DataFrame({
        "station": ["Hyderabad", "Guntur", "Hyderabad"]
    })

    result = label_encode(df)

    assert result["station"].dtype.kind in "iu"


def test_one_hot_encode():

    df = pd.DataFrame({
        "station": ["Hyderabad", "Guntur"]
    })

    result = one_hot_encode(df)

    assert "station_Hyderabad" in result.columns
    assert "station_Guntur" in result.columns


def test_encode_categorical_columns():

    df = pd.DataFrame({
        "station": ["Hyderabad", "Guntur"]
    })

    result = encode_categorical_columns(df)

    assert result["station"].dtype.kind in "iu"


# ============================================================
# SCALING TESTS
# ============================================================

def test_standard_scale():

    df = pd.DataFrame({
        "delay": [10, 20, 30]
    })

    result, scaler = standard_scale(df)

    assert result.shape == df.shape
    assert scaler is not None


def test_minmax_scale():

    df = pd.DataFrame({
        "delay": [10, 20, 30]
    })

    result, scaler = minmax_scale(df)

    assert result.shape == df.shape
    assert scaler is not None


def test_scale_features():

    df = pd.DataFrame({
        "delay": [10, 20, 30]
    })

    result, scaler = scale_features(
        df,
        method="standard"
    )

    assert result.shape == df.shape
    assert scaler is not None