import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "crowd"
    / "crowd_model.pkl"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        return None

    try:
        return joblib.load(MODEL_PATH)

    except Exception:
        return None


# ============================================================
# STATION ENCODING
# ============================================================

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


# ============================================================
# MAIN FUNCTION
# ============================================================

def show_station_crowd():

    st.title("🚉 Station Crowd Prediction")

    st.write(
        "Predict station crowd level using machine learning."
    )

    st.markdown("---")


    # ========================================================
    # LOAD MODEL
    # ========================================================

    model = load_model()

    if model is None:

        st.error(
            "❌ Crowd model could not be loaded."
        )

        st.info(
            "Please make sure crowd_model.pkl exists inside "
            "models/crowd/"
        )

        return


    st.success(
        "✅ Crowd model loaded successfully"
    )

    st.markdown("---")


    # ========================================================
    # STATION INFORMATION
    # ========================================================

    st.header("🚉 Station Information")

    col1, col2 = st.columns(2)


    # ========================================================
    # LEFT COLUMN
    # ========================================================

    with col1:

        station = st.selectbox(
            "🚉 Select Station",
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
            value=9
        )


        day_of_week = st.slider(
            "📅 Day of Week",
            min_value=0,
            max_value=6,
            value=1
        )


        holiday = st.selectbox(
            "🎉 Holiday",
            [0, 1]
        )


    # ========================================================
    # RIGHT COLUMN
    # ========================================================

    with col2:

        train_frequency = st.number_input(
            "🚆 Train Frequency",
            min_value=1,
            max_value=30,
            value=8
        )


        passenger_count = st.number_input(
            "👥 Passenger Count",
            min_value=50,
            max_value=3000,
            value=800
        )


        entry_count = st.number_input(
            "➡️ Entry Count",
            min_value=0,
            max_value=3000,
            value=500
        )


        exit_count = st.number_input(
            "⬅️ Exit Count",
            min_value=0,
            max_value=3000,
            value=300
        )


    st.markdown("---")


    # ========================================================
    # CREATE INPUT DATA
    # ========================================================

    station_encoded = station_mapping[station]


    input_data = pd.DataFrame({

        "station_encoded": [station_encoded],

        "hour": [hour],

        "day_of_week": [day_of_week],

        "holiday": [holiday],

        "train_frequency": [train_frequency],

        "passenger_count": [passenger_count],

        "entry_count": [entry_count],

        "exit_count": [exit_count]

    })


    # ========================================================
    # DISPLAY INPUT
    # ========================================================

    st.header("📊 Station Status")

    st.dataframe(
        input_data,
        use_container_width=True
    )


    st.markdown("---")


    # ========================================================
    # PREDICTION
    # ========================================================

    if st.button(
        "🚉 Predict Crowd Level",
        use_container_width=True
    ):

        try:

            # -----------------------------------------------
            # Make Prediction
            # -----------------------------------------------

            prediction = model.predict(
                input_data
            )


            result = prediction[0]

            result = str(result)


            # -----------------------------------------------
            # Display Result
            # -----------------------------------------------

            st.markdown("---")

            st.header("🎯 Crowd Prediction")


            if result.lower() == "high":

                st.error(
                    "🔴 HIGH CROWD"
                )

                st.warning(
                    "Heavy crowd expected. "
                    "Additional monitoring is recommended."
                )


            elif result.lower() == "medium":

                st.warning(
                    "🟡 MEDIUM CROWD"
                )

                st.info(
                    "Moderate crowd expected at the station."
                )


            elif result.lower() == "low":

                st.success(
                    "🟢 LOW CROWD"
                )

                st.info(
                    "Station crowd is expected to be low."
                )


            else:

                st.info(
                    f"Predicted Crowd: {result}"
                )


            # -----------------------------------------------
            # Metric
            # -----------------------------------------------

            st.metric(
                "Predicted Crowd Level",
                result.upper()
            )


        except Exception as e:

            st.error(
                "❌ Crowd prediction failed."
            )

            st.exception(e)


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    show_station_crowd()