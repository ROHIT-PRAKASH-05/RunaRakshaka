# ==============================================================================
#  RunaRakshaka  —  Credit Card Default Risk Analyzer
#  Dataset 2
# ==============================================================================

import os
import joblib
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from components.sidebar import render_sidebar
from components.shared_css import inject_shared_css

# ==============================================================================
#  PAGE CONFIG
# ==============================================================================

st.set_page_config(
    page_title="Credit Card Risk — RunaRakshaka",
    page_icon="💳",
    layout="wide",
)

# ==============================================================================
#  DESIGN SYSTEM
# ==============================================================================

inject_shared_css()

st.markdown("""
<style>

.sec-label {
    font-size: .72rem; font-weight: 800; color: #00B4D8;
    text-transform: uppercase; letter-spacing: .12em; margin: .2rem 0 .8rem;
}

.page-hero {
    background: linear-gradient(135deg, #EFF8FF 0%, #E6F9FC 100%);
    border: 1px solid #BAE6FD; border-radius: 20px;
    padding: 1.8rem 2rem 1.6rem; margin-bottom: 1.6rem;
    border-left: 4px solid #00B4D8;
}
.page-hero-icon  { font-size: 2rem; margin-bottom: .4rem; }
.page-hero-title { font-size: 1.7rem; font-weight: 800; color: #1A1F36; margin-bottom: .2rem; }
.page-hero-sub   { font-size: .92rem; color: #6B7280; margin-bottom: .8rem; line-height: 1.6; }

.input-section-label {
    font-size: .68rem; font-weight: 800; color: #00B4D8;
    text-transform: uppercase; letter-spacing: .12em;
    margin-bottom: .5rem; display: block;
}

.derived-chip {
    background: #EFF8FF; border: 1px solid #BAE6FD; border-radius: 10px;
    padding: .7rem 1rem; text-align: center;
}
.derived-chip-val { font-size: 1.25rem; font-weight: 800; color: #00B4D8; }
.derived-chip-lbl { font-size: .74rem; color: #6B7280; font-weight: 600; margin-top: 2px; }

</style>
""", unsafe_allow_html=True)

# ==============================================================================
#  SIDEBAR
# ==============================================================================

render_sidebar()

# ==============================================================================
#  LOAD MODEL
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache_resource
def load_model():
    mdl = joblib.load(os.path.join(BASE_DIR, "models", "dataset2", "best_model_dataset2.pkl"))
    scl = joblib.load(os.path.join(BASE_DIR, "models", "dataset2", "scaler_dataset2.pkl"))
    return mdl, scl

model, scaler = load_model()

# ==============================================================================
#  PAGE HERO
# ==============================================================================

st.markdown("""
<div class="page-hero">
  <div class="page-hero-icon">💳</div>
  <div class="page-hero-title">Credit Card Default Risk Analyzer</div>
  <div class="page-hero-sub">
    Predict whether a credit card customer is likely to default on their next payment
    cycle based on credit limit, payment behaviour, and utilisation patterns.
    <br><em style="color:#D97706;">Note: This model has a ROC-AUC of 0.74 — predictions should be reviewed alongside other signals.</em>
  </div>
  <span class="pill pill-blue">Dataset 2</span>
  <span class="pill pill-green">XGBoost</span>
  <span class="pill pill-amber">ROC-AUC 0.7400</span>
  <span class="pill pill-blue">Accuracy 82%</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  INPUT SECTION
# ==============================================================================

st.markdown('<div class="sec-label">Customer Profile</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">📋 Account Details</span>
    </div>
    """, unsafe_allow_html=True)
    limit_bal = st.number_input(
        "Credit Limit ($)",
        min_value=1_000, max_value=1_000_000, value=100_000, step=5_000,
        help="Total credit limit on the card",
    )
    age = st.number_input(
        "Customer Age",
        min_value=18, max_value=100, value=30,
        help="Age of the credit card holder",
    )

with col2:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">📅 Payment Status History</span>
    </div>
    """, unsafe_allow_html=True)
    payment_status_sep = st.selectbox(
        "September Payment Status",
        options=[0, 1, 2, 3, 4, 5, 6],
        help="0 = paid on time, higher = months delayed",
    )
    payment_status_aug = st.selectbox(
        "August Payment Status",
        options=[0, 1, 2, 3, 4, 5, 6],
    )
    payment_status_jul = st.selectbox(
        "July Payment Status",
        options=[0, 1, 2, 3, 4, 5, 6],
    )

with col3:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">📊 Utilisation Ratios</span>
    </div>
    """, unsafe_allow_html=True)
    credit_utilization = st.slider(
        "Credit Utilization",
        min_value=0.0, max_value=1.5, value=0.20, step=0.01,
        help="Ratio of outstanding balance to credit limit",
    )
    payment_ratio = st.slider(
        "Payment Ratio",
        min_value=0.0, max_value=2.0, value=1.10, step=0.01,
        help="Ratio of amount paid to minimum due",
    )

# ==============================================================================
#  DERIVED FEATURES (live preview)
# ==============================================================================

avg_payment_delay = (payment_status_sep + payment_status_aug + payment_status_jul) / 3
max_payment_delay = max(payment_status_sep, payment_status_aug, payment_status_jul)

st.markdown('<div class="sec-label">Derived Risk Indicators</div>', unsafe_allow_html=True)

d1, d2 = st.columns(2, gap="medium")
with d1:
    st.markdown(f"""
    <div class="derived-chip">
      <div class="derived-chip-val">{avg_payment_delay:.2f}</div>
      <div class="derived-chip-lbl">Average Payment Delay (months)</div>
    </div>
    """, unsafe_allow_html=True)
with d2:
    st.markdown(f"""
    <div class="derived-chip">
      <div class="derived-chip-val">{max_payment_delay}</div>
      <div class="derived-chip-lbl">Maximum Payment Delay (months)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  PREDICT
# ==============================================================================

if st.button("🔍  Analyze Credit Card Default Risk", use_container_width=True, type="primary"):

    X = pd.DataFrame([{
        "limit_bal":           limit_bal,
        "age":                 age,
        "payment_status_sep":  payment_status_sep,
        "payment_status_aug":  payment_status_aug,
        "payment_status_jul":  payment_status_jul,
        "avg_payment_delay":   avg_payment_delay,
        "max_payment_delay":   max_payment_delay,
        "credit_utilization":  credit_utilization,
        "payment_ratio":       payment_ratio,
    }])

    X_scaled = scaler.transform(X)
    prob_default          = model.predict_proba(X_scaled)[0][1]
    default_probability   = prob_default * 100
    repayment_probability = 100 - default_probability

    # Store for Unified Dashboard
    st.session_state["dataset2_risk"] = default_probability

    # Risk classification
    if default_probability < 20:
        risk, color, rc_color, rc_bg = "LOW RISK",    "#16A34A", "#16A34A", "#F0FDF4"
    elif default_probability < 50:
        risk, color, rc_color, rc_bg = "MEDIUM RISK", "#D97706", "#D97706", "#FFFBEB"
    else:
        risk, color, rc_color, rc_bg = "HIGH RISK",   "#DC2626", "#DC2626", "#FEF2F2"

    # ---------- Result metrics ----------
    st.markdown('<div class="sec-label">Prediction Results</div>', unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3, gap="medium")
    with r1:
        st.markdown(f"""
        <div class="res-card">
          <div class="res-val" style="color:#16A34A;">{repayment_probability:.2f}%</div>
          <div class="res-lbl">Repayment Probability</div>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.markdown(f"""
        <div class="res-card">
          <div class="res-val" style="color:{color};">{default_probability:.2f}%</div>
          <div class="res-lbl">Default Probability</div>
        </div>
        """, unsafe_allow_html=True)
    with r3:
        st.markdown(f"""
        <div class="res-card">
          <div class="res-val" style="color:{color};">{risk}</div>
          <div class="res-lbl">Risk Classification</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

    # ---------- Gauge ----------
    st.markdown('<div class="sec-label">Default Risk Gauge</div>', unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=default_probability,
        number={"suffix": "%", "font": {"size": 32}},
        title={"text": "Credit Card Default Risk", "font": {"size": 16}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar":  {"color": color, "thickness": 0.25},
            "bgcolor": "white",
            "steps": [
                {"range": [0,  20], "color": "#DCFCE7"},
                {"range": [20, 50], "color": "#FEF9C3"},
                {"range": [50, 100], "color": "#FEE2E2"},
            ],
            "threshold": {
                "line": {"color": color, "width": 3},
                "thickness": 0.75,
                "value": default_probability,
            },
        },
    ))
    fig.update_layout(
        height=320, margin=dict(t=40, b=10, l=20, r=20),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)

    # ---------- Risk banner ----------
    st.markdown(f"""
    <div class="risk-banner" style="background:{color};">
      {risk}
    </div>
    """, unsafe_allow_html=True)

    # ---------- Recommendation ----------
    st.markdown('<div class="sec-label">AI Recommendation</div>', unsafe_allow_html=True)

    if default_probability < 20:
        rec_title = "✅ Eligible for Credit Approval"
        rec_body  = ("Strong payment history and low utilisation indicate excellent repayment "
                     "capability. Customer profile is financially stable with minimal default risk.")
    elif default_probability < 50:
        rec_title = "⚠️ Proceed with Caution"
        rec_body  = ("Moderate default risk detected. Additional credit history verification "
                     "is recommended. Consider reducing the credit limit or requesting a co-applicant.")
    else:
        rec_title = "❌ High Default Risk — Review Required"
        rec_body  = ("Elevated default indicators across payment history and utilisation ratio. "
                     "Credit approval is not recommended without significant collateral or guarantor support.")

    st.markdown(f"""
    <div class="rec-card" style="--rc-color:{rc_color}; --rc-bg:{rc_bg};">
      <div class="rec-title" style="color:{rc_color};">{rec_title}</div>
      {rec_body}
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
#  FOOTER
# ==============================================================================

st.markdown("""
<div class="page-footer">
  <b>Dataset 2</b> &nbsp;·&nbsp; Credit Card Default Prediction &nbsp;·&nbsp;
  RunaRakshaka &nbsp;·&nbsp; PES University MCA 2025–26
</div>
""", unsafe_allow_html=True)