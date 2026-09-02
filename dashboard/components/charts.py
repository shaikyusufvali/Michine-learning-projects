# ============================================================
# RAILPULSE AI
# DASHBOARD CHART COMPONENTS
# ============================================================

import streamlit as st
import pandas as pd


def line_chart(data, x=None, y=None):
    """
    Display a line chart.
    """

    if isinstance(data, pd.DataFrame) and x and y:
        chart_data = data.set_index(x)[y]
        st.line_chart(chart_data)

    else:
        st.line_chart(data)


def bar_chart(data, x=None, y=None):
    """
    Display a bar chart.
    """

    if isinstance(data, pd.DataFrame) and x and y:
        chart_data = data.set_index(x)[y]
        st.bar_chart(chart_data)

    else:
        st.bar_chart(data)


def area_chart(data, x=None, y=None):
    """
    Display an area chart.
    """

    if isinstance(data, pd.DataFrame) and x and y:
        chart_data = data.set_index(x)[y]
        st.area_chart(chart_data)

    else:
        st.area_chart(data)


def display_chart(title, data, chart_type="line"):
    """
    Display a chart with a title.

    Supported chart types:
    - line
    - bar
    - area
    """

    st.subheader(title)

    if chart_type == "line":
        line_chart(data)

    elif chart_type == "bar":
        bar_chart(data)

    elif chart_type == "area":
        area_chart(data)

    else:
        st.warning(
            "Invalid chart type. "
            "Use 'line', 'bar', or 'area'."
        )