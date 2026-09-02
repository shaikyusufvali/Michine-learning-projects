import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "delay"
    / "delay_model.pkl"
)

def show_delay_prediction():

    st.title("🚆 Train Delay Prediction")

    st.write(
        "Predict the expected train delay in minutes "
        "using machine learning."
    )

    st.markdown("---")

    if not MODEL_PATH.exists():

        st.error(
            f"Delay model not found:\n{MODEL_PATH}"
        )

        return

    try:

        model = joblib.load(
            MODEL_PATH
        )

    except Exception as e:

        st.error(
            f"Unable to load model: {e}"
        )

        return

    st.success(
        "Delay prediction model loaded successfully ✅"
    )

    st.markdown("---")

    st.header("📝 Train Information")

    col1, col2 = st.columns(2)

    with col1:

        distance_km = st.number_input(
            "Distance (km)",
            min_value=10.0,
            max_value=1000.0,
            value=300.0,
            step=10.0
        )

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            max_value=50.0,
            value=30.0,
            step=1.0
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            step=1.0
        )

    with col2:

        station_delay = st.number_input(
            "Station Delay (minutes)",
            min_value=0.0,
            max_value=60.0,
            value=5.0,
            step=1.0
        )

        previous_delay = st.number_input(
            "Previous Delay (minutes)",
            min_value=0.0,
            max_value=60.0,
            value=5.0,
            step=1.0
        )

    st.markdown("---")

    st.header("📊 Input Summary")

    input_data = pd.DataFrame({

        "distance_km": [
            distance_km
        ],

        "temperature": [
            temperature
        ],

        "rainfall": [
            rainfall
        ],

        "station_delay": [
            station_delay
        ],

        "previous_delay": [
            previous_delay
        ]

    })

    st.dataframe(
        input_data,
        use_container_width=True
    )

    if st.button(
        "🚆 Predict Train Delay",
        use_container_width=True
    ):

        try:

            if hasattr(model, "feature_names_in_"):

                input_data = input_data[
                    model.feature_names_in_
                ]

            prediction = model.predict(
                input_data
            )

            predicted_delay = float(
                prediction[0]
            )

            predicted_delay = max(
                0,
                predicted_delay
            )

            st.markdown("---")

            st.header(
                "🎯 Prediction Result"
            )

            st.metric(
                "Predicted Train Delay",
                f"{predicted_delay:.2f} minutes"
            )

            if predicted_delay < 5:

                st.success(
                    "🟢 Low Delay — Train is expected "
                    "to operate close to schedule."
                )

            elif predicted_delay < 15:

                st.warning(
                    "🟡 Moderate Delay — Some delay "
                    "is expected."
                )

            else:

                st.error(
                    "🔴 High Delay — Significant train "
                    "delay is expected."
                )

        except Exception as e:

            st.error(
                f"Prediction failed: {e}"
            )

if __name__ == "__main__":

    show_delay_prediction()