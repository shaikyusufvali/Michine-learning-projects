import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "demand"
    / "passenger_demand.pkl"
)

def show_passenger_demand():

    st.title("👥 Passenger Demand Prediction")

    st.write(
        "Predict the expected number of passengers "
        "using the trained machine learning model."
    )

    st.markdown("---")

    if not MODEL_PATH.exists():

        st.error(
            f"Passenger demand model not found:\n{MODEL_PATH}"
        )

        return

    try:

        model = joblib.load(MODEL_PATH)

    except Exception as e:

        st.error(
            f"Unable to load passenger demand model: {e}"
        )

        return

    st.success(
        "Passenger demand model loaded successfully ✅"
    )

    st.markdown("---")

    st.header("📝 Passenger Information")

    col1, col2 = st.columns(2)

    with col1:

        station = st.selectbox(
            "🚉 Station",
            [
                "Hyderabad",
                "Secunderabad",
                "Vijayawada",
                "Guntur",
                "Warangal",
                "Visakhapatnam",
                "Tirupati",
                "Nellore",
                "Kurnool",
                "Nizamabad"
            ]
        )

        hour = st.slider(
            "🕐 Hour",
            min_value=0,
            max_value=23,
            value=12
        )

        day_of_week = st.selectbox(
            "📅 Day of Week",
            options=[0, 1, 2, 3, 4, 5, 6],
            format_func=lambda x: [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ][x]
        )

    with col2:

        holiday = st.selectbox(
            "🎉 Holiday",
            [0, 1],
            format_func=lambda x:
                "Yes" if x == 1 else "No"
        )

        weather = st.selectbox(
            "🌦️ Weather",
            [
                "Clear",
                "Cloudy",
                "Rain",
                "Heavy Rain",
                "Fog"
            ]
        )

        special_event = st.selectbox(
            "🎪 Special Event",
            [0, 1],
            format_func=lambda x:
                "Yes" if x == 1 else "No"
        )

    is_weekend = int(
        day_of_week >= 5
    )

    is_peak_hour = int(
        (7 <= hour <= 10)
        or
        (17 <= hour <= 21)
    )

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

    station_encoded = station_mapping[station]

    train_type_encoded = 0

    input_data = pd.DataFrame({

        "hour": [
            hour
        ],

        "day_of_week": [
            day_of_week
        ],

        "is_weekend": [
            is_weekend
        ],

        "is_peak_hour": [
            is_peak_hour
        ],

        "station_encoded": [
            station_encoded
        ],

        "train_type_encoded": [
            train_type_encoded
        ],

        "holiday": [
            holiday
        ],

        "special_event": [
            special_event
        ]
    })

    if hasattr(model, "feature_names_in_"):

        model_features = list(
            model.feature_names_in_
        )

        missing_features = [
            feature
            for feature in model_features
            if feature not in input_data.columns
        ]

        if missing_features:

            st.error(
                f"Missing model features: {missing_features}"
            )

            return

        input_data = input_data[
            model_features
        ]

    st.markdown("---")

    st.header("📊 Input Summary")

    st.dataframe(
        input_data,
        use_container_width=True
    )

    if st.button(
        "👥 Predict Passenger Demand",
        use_container_width=True
    ):

        try:

            prediction = model.predict(
                input_data
            )

            predicted_passengers = float(
                prediction[0]
            )

            predicted_passengers = max(
                0,
                predicted_passengers
            )

            st.markdown("---")

            st.header(
                "🎯 Prediction Result"
            )

            st.metric(
                "Expected Passenger Demand",
                f"{predicted_passengers:.0f} passengers"
            )

            if predicted_passengers < 400:

                st.success(
                    "🟢 Low Demand — Normal passenger activity."
                )

            elif predicted_passengers < 700:

                st.warning(
                    "🟡 Medium Demand — Increased passenger activity."
                )

            else:

                st.error(
                    "🔴 High Demand — Heavy passenger activity expected."
                )

        except Exception as e:

            st.error(
                f"Passenger demand prediction failed: {e}"
            )

if __name__ == "__main__":

    show_passenger_demand()