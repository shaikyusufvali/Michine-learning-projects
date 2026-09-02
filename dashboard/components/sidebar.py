# ============================================================
# RAILPULSE AI
# SIDEBAR COMPONENT
# ============================================================

import streamlit as st


def render_sidebar():
    """
    Render the RailPulse AI sidebar.
    """

    with st.sidebar:

        st.title("🚆 RailPulse AI")

        st.markdown(
            "### Railway Intelligence System"
        )

        st.markdown("---")

        st.subheader("Navigation")

        st.markdown(
            """
            Use the pages from the sidebar to explore:

            - 📊 Dashboard
            - 🚆 Delay Prediction
            - 👥 Passenger Demand
            - 🔧 Predictive Maintenance
            - 🚉 Station Crowd
            """
        )

        st.markdown("---")

        st.subheader("AI Modules")

        st.caption("Train Delay Prediction")
        st.caption("Delay Classification")
        st.caption("Passenger Demand Forecasting")
        st.caption("Predictive Maintenance")
        st.caption("Station Crowd Prediction")

        st.markdown("---")

        st.caption("RailPulse AI • 2026")