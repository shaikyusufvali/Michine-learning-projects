# ============================================================
# RAILPULSE AI
# DASHBOARD CARD COMPONENTS
# ============================================================

import streamlit as st


def metric_card(title, value, description=None):
    """
    Display a reusable metric card.
    """

    st.metric(
        label=title,
        value=value,
        delta=description
    )


def prediction_card(title, prediction, status=None):
    """
    Display a prediction result card.
    """

    st.subheader(title)

    st.markdown(
        f"### {prediction}"
    )

    if status:
        st.caption(status)


def info_card(title, message):
    """
    Display an informational card.
    """

    st.info(
        f"**{title}**\n\n{message}"
    )


def success_card(title, message):
    """
    Display a success card.
    """

    st.success(
        f"**{title}**\n\n{message}"
    )


def warning_card(title, message):
    """
    Display a warning card.
    """

    st.warning(
        f"**{title}**\n\n{message}"
    )


def error_card(title, message):
    """
    Display an error card.
    """

    st.error(
        f"**{title}**\n\n{message}"
    )