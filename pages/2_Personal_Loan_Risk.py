# ==============================================================================
#  RunaRakshaka  —  Personal Loan Risk Analyzer
#  Dataset 3
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
    page_title="Personal Loan Risk — RunaRakshaka",
    page_icon="🏦",
    layout="wide",
)

# ==============================================================================
#  DESIGN SYSTEM
# ==============================================================================

inject_shared_css()

st.markdown("""
<style>

.sec-label {
    font-size: .72rem; font-weight: 800; color: #16A34A;
    text-transform: uppercase; letter-spacing: .12em; margin: .2rem 0 .8rem;
}

.page-hero {
    background: linear-gradient(135deg, #F0FDF4 0%, #E9F8EF 100%);
    border: 1px solid #BBF7D0; border-radius: 20px;
    padding: 1.8rem 2rem 1.6rem; margin-bottom: 1.6rem;
    border-left: 4px solid #16A34A;
}
.page-hero-icon  { font-size: 2rem; margin-bottom: .4rem; }
.page-hero-title { font-size: 1.7rem; font-weight: 800; color: #1A1F36; margin-bottom: .2rem; }
.page-hero-sub   { font-size: .92rem; color: #6B7280; margin-bottom: .8rem; line-height: 1.6; }

.input-section-label {
    font-size: .68rem; font-weight: 800; color: #16A34A;
    text-transform: uppercase; letter-spacing: .12em;
    margin-bottom: .5rem; display: block;
}

.derived-chip {
    background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 10px;
    padding: .7rem 1rem; text-align: center;
}
.derived-chip-val { font-size: 1.25rem; font-weight: 800; color: #16A34A; }
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
    mdl = joblib.load(os.path.join(BASE_DIR, "models", "dataset3", "best_model_dataset3.pkl"))
    scl = joblib.load(os.path.join(BASE_DIR, "models", "dataset3", "scaler_dataset3.pkl"))
    enc = joblib.load(os.path.join(BASE_DIR, "models", "dataset3", "label_encoders_dataset3.pkl"))
    return mdl, scl, enc

model, scaler, label_encoders = load_model()

# ==============================================================================
#  PAGE HERO
# ==============================================================================

st.markdown("""
<div class="page-hero">
  <div class="page-hero-icon">🏦</div>
  <div class="page-hero-title">Personal Loan Risk Analyzer</div>
  <div class="page-hero-sub">
    Assess the probability that a personal loan applicant may default using income,
    loan grade, interest rate, and loan intent as risk signals.
  </div>
  <span class="pill pill-green">Dataset 3</span>
  <span class="pill pill-blue">Random Forest</span>
  <span class="pill pill-violet">ROC-AUC 0.9377</span>
  <span class="pill pill-amber">Accuracy 89%</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  INPUTS
# ==============================================================================

st.markdown('<div class="sec-label">Applicant Profile</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">💰 Financial Details</span>
    </div>
    """, unsafe_allow_html=True)
    person_income = st.number_input(
        "Annual Income ($)",
        min_value=1_000, value=50_000, step=1_000,
        help="Gross annual income of the applicant",
    )
    loan_amnt = st.number_input(
        "Loan Amount ($)",
        min_value=500, value=10_000, step=500,
        help="Total loan amount requested",
    )

with col2:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">📋 Loan Parameters</span>
    </div>
    """, unsafe_allow_html=True)
    loan_int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=1.0, max_value=40.0, value=12.0,
        help="Annual interest rate assigned to the loan",
    )
    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"],
        help="Credit grade assigned to the loan (A = best, G = riskiest)",
    )

with col3:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">🏠 Applicant Background</span>
    </div>
    """, unsafe_allow_html=True)
    loan_intent = st.selectbox(
        "Loan Purpose",
        ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"],
        help="The stated purpose of the loan",
    )
    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["MORTGAGE", "OTHER", "OWN", "RENT"],
        help="Current housing status of the applicant",
    )

# ==============================================================================
#  DERIVED FEATURES (live preview)
# ==============================================================================

loan_percent_income = loan_amnt / person_income
risk_score          = loan_percent_income * loan_int_rate

st.markdown('<div class="sec-label">Derived Risk Indicators</div>', unsafe_allow_html=True)

d1, d2 = st.columns(2, gap="medium")
with d1:
    st.markdown(f"""
    <div class="derived-chip">
      <div class="derived-chip-val">{loan_percent_income:.4f}</div>
      <div class="derived-chip-lbl">Loan-to-Income Ratio</div>
    </div>
    """, unsafe_allow_html=True)
with d2:
    st.markdown(f"""
    <div class="derived-chip">
      <div class="derived-chip-val">{risk_score:.4f}</div>
      <div class="derived-chip-lbl">Composite Risk Score</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  PREDICT
# ==============================================================================

if st.button("🔍  Analyze Personal Loan Default Risk", use_container_width=True, type="primary"):

    grade_encoded  = label_encoders["loan_grade"].transform([loan_grade])[0]
    intent_encoded = label_encoders["loan_intent"].transform([loan_intent])[0]
    home_encoded   = label_encoders["person_home_ownership"].transform([person_home_ownership])[0]

    X = pd.DataFrame([{
        "loan_amnt":             loan_amnt,
        "loan_grade":            grade_encoded,
        "loan_int_rate":         loan_int_rate,
        "loan_intent":           intent_encoded,
        "loan_percent_income":   loan_percent_income,
        "person_home_ownership": home_encoded,
        "person_income":         person_income,
        "risk_score":            risk_score,
    }])

    X_scaled = scaler.transform(X)
    prob_default          = model.predict_proba(X_scaled)[0][1]
    default_probability   = prob_default * 100
    repayment_probability = 100 - default_probability

    # Store for Unified Dashboard
    st.session_state["dataset3_risk"] = default_probability

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
        title={"text": "Personal Loan Default Risk", "font": {"size": 16}},
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
        rec_title = "✅ Eligible for Loan Approval"
        rec_body  = ("Strong repayment capability confirmed. Income-to-loan ratio and credit grade "
                     "indicate low default risk. Recommended for standard approval.")
    elif default_probability < 50:
        rec_title = "⚠️ Moderate Risk — Proceed with Verification"
        rec_body  = ("Moderate default risk detected. Income stability, employment history, and "
                     "existing debt obligations should be verified before approval. "
                     "Consider a reduced loan amount or higher collateral requirement.")
    else:
        rec_title = "❌ High Default Risk — Approval Not Recommended"
        rec_body  = ("Elevated default risk across income, grade, and loan purpose indicators. "
                     "Approval is not recommended without a guarantor, secured collateral, "
                     "or significant improvement in the applicant's financial standing.")

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
  <b>Dataset 3</b> &nbsp;·&nbsp; Personal Loan Default Prediction &nbsp;·&nbsp;
  RunaRakshaka &nbsp;·&nbsp; PES University MCA 2025–26
</div>
""", unsafe_allow_html=True)