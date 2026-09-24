import streamlit as st
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

st.set_page_config(
    page_title="RailPulse-AI",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        font-size: 20px;
        color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🚆 RailPulse-AI")
st.sidebar.markdown("---")
st.sidebar.subheader("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "🚆 Delay Prediction",
        "👥 Passenger Demand",
        "🔧 Predictive Maintenance",
        "🚉 Station Crowd"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **RailPulse-AI**

    AI-powered railway intelligence
    platform for:

    • Train Delay Prediction  
    • Delay Classification  
    • Passenger Demand  
    • Predictive Maintenance  
    • Station Crowd Prediction
    """
)

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🚆 RailPulse-AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI-Powered Railway Intelligence & Decision Support System</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚆 Delay Prediction", "Ready")

    with col2:
        st.metric("👥 Passenger Demand", "Ready")

    with col3:
        st.metric("🔧 Maintenance", "Ready")

    with col4:
        st.metric("🚉 Station Crowd", "Ready")

    st.markdown("---")

    st.header("🤖 AI Prediction Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            ### 🚆 Train Delay Prediction

            Predict the expected train delay
            in minutes using:

            • Distance  
            • Weather  
            • Rainfall  
            • Station Delay  
            • Previous Delay  
            • Departure Time
            """
        )

        st.success("Delay Regression Model ✅")

    with col2:
        st.info(
            """
            ### 🚨 Delay Classification

            Predict whether a train will be:

            • Not Delayed  
            • Delayed

            using machine learning classification.
            """
        )

        st.success("Delay Classification Model ✅")

    col3, col4 = st.columns(2)

    with col3:
        st.info(
            """
            ### 👥 Passenger Demand

            Predict passenger demand based on:

            • Station  
            • Hour  
            • Day of Week  
            • Weekend  
            • Peak Hour  
            • Train information
            """
        )

        st.success("Passenger Demand Model ✅")

    with col4:
        st.info(
            """
            ### 🔧 Predictive Maintenance

            Predict railway equipment failure
            risk using:

            • Engine Temperature  
            • Brake Pressure  
            • Vibration  
            • Wheel Condition  
            • Engine Hours  
            • Service History
            """
        )

        st.success("Maintenance Model ✅")

    st.markdown("---")

    st.header("🚉 Station Crowd Intelligence")

    st.warning(
        """
        The system predicts station crowd levels
        as **Low, Medium, or High** using passenger
        and station activity information.
        """
    )

    st.markdown("---")

    st.caption(
        "RailPulse-AI • Machine Learning Railway Intelligence System"
    )

elif page == "🚆 Delay Prediction":

    from pages.delay_prediction import show_delay_prediction

    show_delay_prediction()

elif page == "👥 Passenger Demand":

    from pages.passenger_demand import show_passenger_demand

    show_passenger_demand()

elif page == "🔧 Predictive Maintenance":

    from pages.maintenance import show_maintenance

    show_maintenance()

elif page == "🚉 Station Crowd":

    from pages.station_crowd import show_station_crowd

    show_station_crowd()