import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "maintenance" / "maintenance_model.pkl"


@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        return None

    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None


def show_maintenance():

    st.title("🔧 Predictive Maintenance")

    st.write(
        "Predict railway equipment failure risk using machine learning."
    )

    st.markdown("---")

    model = load_model()

    if model is None:

        st.error("Maintenance model could not be loaded.")

        st.info(
            "Please make sure maintenance_model.pkl exists in "
            "models/maintenance/"
        )

        return

    st.success("Maintenance model loaded successfully ✅")

    st.markdown("---")

    st.header("🔧 Train Equipment Information")

    col1, col2 = st.columns(2)

    with col1:

        engine_temperature = st.number_input(
            "🌡️ Engine Temperature (°C)",
            min_value=40.0,
            max_value=150.0,
            value=85.0,
            step=1.0
        )

        brake_pressure = st.number_input(
            "🛑 Brake Pressure",
            min_value=40.0,
            max_value=130.0,
            value=95.0,
            step=1.0
        )

        vibration = st.number_input(
            "📳 Vibration",
            min_value=0.0,
            max_value=15.0,
            value=4.0,
            step=0.1
        )

        wheel_condition = st.slider(
            "⚙️ Wheel Condition",
            min_value=0,
            max_value=100,
            value=80
        )

    with col2:

        engine_hours = st.number_input(
            "⏱️ Engine Hours",
            min_value=0,
            max_value=30000,
            value=5000,
            step=500
        )

        last_service_days = st.number_input(
            "📅 Days Since Last Service",
            min_value=1,
            max_value=500,
            value=100,
            step=10
        )

        maintenance_count = st.number_input(
            "🔧 Previous Maintenance Count",
            min_value=0,
            max_value=30,
            value=5,
            step=1
        )

    input_data = pd.DataFrame({

        "engine_temperature": [
            engine_temperature
        ],

        "brake_pressure": [
            brake_pressure
        ],

        "vibration": [
            vibration
        ],

        "wheel_condition": [
            wheel_condition
        ],

        "engine_hours": [
            engine_hours
        ],

        "last_service_days": [
            last_service_days
        ],

        "maintenance_count": [
            maintenance_count
        ]

    })

    st.markdown("---")

    st.header("📊 Equipment Status")

    st.dataframe(
        input_data,
        use_container_width=True
    )

    st.markdown("---")

    if st.button(
        "🔧 Predict Maintenance Risk",
        use_container_width=True
    ):

        try:

            prediction = model.predict(input_data)

            prediction_value = int(prediction[0])

            st.markdown("---")

            st.header("🎯 Maintenance Prediction")

            if prediction_value == 1:

                st.error(
                    "🔴 FAILURE RISK DETECTED"
                )

                st.warning(
                    "Immediate maintenance inspection is recommended."
                )

                st.metric(
                    "Failure Prediction",
                    "FAILURE"
                )

            else:

                st.success(
                    "🟢 NO IMMEDIATE FAILURE RISK"
                )

                st.info(
                    "Equipment condition appears normal."
                )

                st.metric(
                    "Failure Prediction",
                    "NORMAL"
                )

        except Exception as e:

            st.error(
                "Prediction failed."
            )

            st.exception(e)


if __name__ == "__main__":

    show_maintenance()