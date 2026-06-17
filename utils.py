# ==============================================================================
# utils.py
# Shared Components for RunaRakshaka
# ==============================================================================

import streamlit as st
import plotly.graph_objects as go

# ==============================================================================
# GLOBAL CSS
# ==============================================================================

GLOBAL_CSS = """
<style>

/* ============================================================================
MAIN APP
============================================================================ */

.stApp {
    background-color: #0E1117;
    color: #E6EDF3;
}

/* ============================================================================
SIDEBAR
============================================================================ */

section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
}

/* ============================================================================
HEADINGS
============================================================================ */

h1,h2,h3,h4 {
    color: #E6EDF3;
}

/* ============================================================================
CARDS
============================================================================ */

.rr-card {

    background: #161B22;

    border: 1px solid #30363D;

    border-radius: 16px;

    padding: 20px;

    margin-bottom: 15px;
}

/* ============================================================================
SECTION TITLES
============================================================================ */

.rr-section {

    font-size: 1.1rem;

    font-weight: 700;

    color: #00B4D8;

    margin-bottom: 12px;
}

/* ============================================================================
METRIC BOXES
============================================================================ */

.rr-metric {

    background: #161B22;

    border: 1px solid #30363D;

    border-radius: 14px;

    padding: 15px;

    text-align: center;
}

.rr-metric-value {

    font-size: 1.8rem;

    font-weight: 800;
}

.rr-metric-label {

    color: #8B949E;

    font-size: 0.8rem;
}

/* ============================================================================
STREAMLIT METRICS
============================================================================ */

[data-testid="metric-container"] {

    background: #161B22;

    border: 1px solid #30363D;

    border-radius: 12px;

    padding: 12px;
}

/* ============================================================================
BUTTONS
============================================================================ */

.stButton > button {

    width: 100%;

    border-radius: 10px;

    border: none;

    color: white;

    font-weight: 600;

    background: linear-gradient(
        135deg,
        #00B4D8,
        #0077B6
    );
}

.stButton > button:hover {

    background: linear-gradient(
        135deg,
        #0096C7,
        #023E8A
    );
}

/* ============================================================================
DATAFRAME
============================================================================ */

[data-testid="stDataFrame"] {

    border-radius: 12px;

    overflow: hidden;
}

/* ============================================================================
PROGRESS BAR
============================================================================ */

.stProgress > div > div > div {

    background-color: #00B4D8;
}

/* ============================================================================
FOOTER
============================================================================ */

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

</style>
"""

# ==============================================================================
# SECTION HEADER
# ==============================================================================

def section_header(title):

    st.markdown(
        f"""
        <div style="
        background:#161B22;
        border-left:4px solid #00B4D8;
        padding:12px;
        border-radius:10px;
        margin-top:10px;
        margin-bottom:15px;
        ">
            <h3 style="margin:0;">
                {title}
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# RISK CARD
# ==============================================================================

def risk_card(
    title,
    value,
    color
):

    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            font-weight:bold;
            font-size:24px;
        ">
            {title}<br>
            {value}
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# GAUGE CHART
# ==============================================================================

def gauge_chart(
    value,
    title,
    color="#00B4D8"
):

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=value,

            title={
                "text": title
            },

            gauge={

                "axis": {
                    "range": [0,100]
                },

                "bar": {
                    "color": color
                },

                "steps": [

                    {
                        "range":[0,30],
                        "color":"#D5F5E3"
                    },

                    {
                        "range":[30,60],
                        "color":"#FCF3CF"
                    },

                    {
                        "range":[60,100],
                        "color":"#FADBD8"
                    }

                ]
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==============================================================================
# RECOMMENDATION ENGINE
# ==============================================================================

def recommendation_box(
    risk_score
):

    st.subheader(
        "💡 AI Recommendation"
    )

    if risk_score < 30:

        st.success("""
        Eligible for approval.

        Good repayment capacity.

        Financial profile appears stable.
        """)

    elif risk_score < 60:

        st.warning("""
        Moderate risk detected.

        Additional verification recommended.

        Review repayment history carefully.
        """)

    else:

        st.error("""
        High probability of default.

        Elevated financial stress indicators.

        Loan approval not recommended.
        """)

# ==============================================================================
# FOOTER
# ==============================================================================

def footer():

    st.markdown("---")

    st.markdown(
        """
        <center>

        <b>RunaRakshaka</b><br>

        AI-Based Debt Risk Prediction &
        Financial Stability System<br><br>

        PES College of Engineering<br>

        Rohit P • PES1PG25CA325

        </center>
        """,
        unsafe_allow_html=True
    )