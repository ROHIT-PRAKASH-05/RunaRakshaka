# ==============================================================================
#  RunaRakshaka  —  Financial Stability Analyzer
#  Dataset 5
# ==============================================================================

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from components.sidebar import render_sidebar
from components.shared_css import inject_shared_css

# ==============================================================================
#  PAGE CONFIG
# ==============================================================================

st.set_page_config(
    page_title="Financial Stability — RunaRakshaka",
    page_icon="📈",
    layout="wide",
)

# ==============================================================================
#  DESIGN SYSTEM
# ==============================================================================

inject_shared_css()

st.markdown("""
<style>

.sec-label {
    font-size: .72rem; font-weight: 800; color: #D97706;
    text-transform: uppercase; letter-spacing: .12em; margin: .2rem 0 .8rem;
}

.page-hero {
    background: linear-gradient(135deg, #FFFBEB 0%, #FEF3E2 100%);
    border: 1px solid #FDE68A; border-radius: 20px;
    padding: 1.8rem 2rem 1.6rem; margin-bottom: 1.6rem;
    border-left: 4px solid #D97706;
}
.page-hero-icon  { font-size: 2rem; margin-bottom: .4rem; }
.page-hero-title { font-size: 1.7rem; font-weight: 800; color: #1A1F36; margin-bottom: .2rem; }
.page-hero-sub   { font-size: .92rem; color: #6B7280; margin-bottom: .8rem; line-height: 1.6; }

.input-section-label {
    font-size: .68rem; font-weight: 800; color: #D97706;
    text-transform: uppercase; letter-spacing: .12em;
    margin-bottom: .5rem; display: block;
}

.derived-chip {
    background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 10px;
    padding: .7rem 1rem; text-align: center;
}
.derived-chip-val { font-size: 1.25rem; font-weight: 800; color: #D97706; }
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
    mdl = joblib.load(os.path.join(BASE_DIR, "models", "dataset5", "best_model_v2.pkl"))
    scl = joblib.load(os.path.join(BASE_DIR, "models", "dataset5", "scaler_v2.pkl"))
    return mdl, scl

model, scaler = load_model()

# ==============================================================================
#  PAGE HERO
# ==============================================================================

st.markdown("""
<div class="page-hero">
  <div class="page-hero-icon">📈</div>
  <div class="page-hero-title">Financial Stability Analyzer</div>
  <div class="page-hero-sub">
    Predict loan repayment probability and overall financial health across 29 engineered features
    including credit score, debt ratio, income, and employment status.
  </div>
  <span class="pill pill-amber">Dataset 5</span>
  <span class="pill pill-blue">XGBoost</span>
  <span class="pill pill-violet">AUPRC 0.9744</span>
  <span class="pill pill-green">Best Minority-Class Model</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  INPUTS
# ==============================================================================

st.markdown('<div class="sec-label">Applicant Financial Profile</div>', unsafe_allow_html=True)

# Grade letter → numeric score (A=1 safest, G=7 riskiest)
GRADE_LETTER_MAP = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">💰 Income &amp; Loan Details</span>
    </div>
    """, unsafe_allow_html=True)
    annual_income = st.number_input(
        "Annual Income ($)",
        min_value=1_000, value=60_000, step=1_000,
        help="Gross annual income of the applicant",
    )
    loan_amount = st.number_input(
        "Loan Amount ($)",
        min_value=500, value=12_000, step=500,
        help="Total loan amount requested",
    )
    interest_rate = st.number_input(
        "Interest Rate (%)",
        min_value=1.0, max_value=40.0, value=13.0,
        help="Annual interest rate on the loan",
    )

with col2:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">📊 Credit &amp; Debt Profile</span>
    </div>
    """, unsafe_allow_html=True)
    credit_score = st.number_input(
        "Credit Score",
        min_value=300, max_value=850, value=650,
        help="FICO or equivalent credit score (300–850)",
    )
    debt_to_income_ratio = st.number_input(
        "Debt-to-Income Ratio",
        min_value=0.0, max_value=2.0, value=0.18, format="%.2f",
        help="Total monthly debt obligations divided by gross monthly income",
    )
    # Full subgrade selectbox — note: only the letter maps to the model feature
    # (grade_number was not in final_features after SelectKBest); the digit
    # is shown for UX completeness and future model versions.
    grade_subgrade = st.selectbox(
        "Loan Grade",
        options=[
            "A1","A2","A3","A4","A5",
            "B1","B2","B3","B4","B5",
            "C1","C2","C3","C4","C5",
            "D1","D2","D3","D4","D5",
            "E1","E2","E3","E4","E5",
            "F1","F2","F3","F4","F5",
            "G1","G2","G3","G4","G5",
        ],
        index=12,   # default = C3
        help=(
            "Loan sub-grade (letter A–G = risk tier, digit 1–5 = sub-tier). "
            "A = lowest risk, G = highest risk. "
            "The deployed model was trained using only the letter tier; "
            "the digit is displayed for reference."
        ),
    )

with col3:
    st.markdown("""
    <div class="content-card">
      <span class="input-section-label">🙋 Personal Background</span>
    </div>
    """, unsafe_allow_html=True)
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
    )
    employment = st.selectbox(
        "Employment Status",
        ["Employed", "Self-employed", "Student", "Retired", "Unemployed"],
    )
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Business", "Education", "Home", "Medical"],
    )
    education = st.selectbox(
        "Education Level",
        ["High School", "Bachelor's", "Master's", "PhD", "Other"],
        index=1,
        help="Highest completed education level",
    )

# ==============================================================================
#  PREDICT
# ==============================================================================

if st.button("🔍  Analyze Financial Stability", use_container_width=True, type="primary"):

    try:
        # ── Grade parsing ──────────────────────────────────────────────────────
        # grade_subgrade is always a valid string from the selectbox (e.g. "C3")
        # Extract letter and number exactly as the training pipeline does.
        grade_letter_char = grade_subgrade[0].upper()               # "C"
        grade_letter      = GRADE_LETTER_MAP.get(grade_letter_char, 4)  # 1-7, default D
        grade_number      = int(grade_subgrade[1]) if grade_subgrade[1].isdigit() else 3
        # grade_score matches training: letter*5 + number  (range 6-40)
        grade_score       = grade_letter * 5 + grade_number

        # ── Education ordinal (matches training encoding exactly) ──────────────
        edu_map = {
            "High School": 1,
            "Bachelor's":  2,
            "Master's":    3,
            "PhD":         4,
            "Other":       2,
        }
        education_ordinal = edu_map.get(education, 2)

        # ── Feature engineering — mirrors training pipeline exactly ────────────
        # debt_burden_ratio: annual interest cost as fraction of income
        debt_burden_ratio   = (loan_amount * (interest_rate / 100)) / (annual_income + 1)

        # monthly_emi: rough EMI assuming 36-month loan
        monthly_emi         = loan_amount / 36

        # emi_to_income_ratio: EMI as fraction of monthly income
        emi_to_income_ratio = monthly_emi / ((annual_income / 12) + 1)

        # financial_stress: higher DTI × higher rate = more stressed borrower
        financial_stress    = debt_to_income_ratio * interest_rate

        # income_per_credit: income earned per credit score point
        income_per_credit   = annual_income / (credit_score + 1)

        # loan_to_income: loan size relative to annual income
        loan_to_income      = loan_amount / (annual_income + 1)

        # rate_x_dti: combined rate + leverage risk
        rate_x_dti          = interest_rate * debt_to_income_ratio

        # credit_income_index: credit quality × log income
        credit_income_index = credit_score * np.log1p(annual_income)

        # grade_x_rate: grade risk amplified by interest rate
        grade_x_rate        = grade_score * interest_rate

        # Binary risk flags (thresholds match training exactly)
        high_risk_flag   = int((interest_rate > 15) and (debt_to_income_ratio > 0.12))
        subprime_flag    = int(credit_score < 620)
        severe_risk_flag = int((credit_score < 620) and (grade_letter >= 5))

        # ── Build feature DataFrame in the same column order as final_features ─
        # (alphabetical, as produced by sorted(final_features) in training)
        X = pd.DataFrame([{
    "annual_income":                   annual_income,
    "credit_income_index":             credit_income_index,
    "credit_score":                    credit_score,
    "debt_burden_ratio":               debt_burden_ratio,
    "debt_to_income_ratio":            debt_to_income_ratio,
    "emi_to_income_ratio":             emi_to_income_ratio,
    "employment_status_Employed":      int(employment == "Employed"),
    "employment_status_Retired":       int(employment == "Retired"),
    "employment_status_Self-employed": int(employment == "Self-employed"),
    "employment_status_Student":       int(employment == "Student"),
    "employment_status_Unemployed":    int(employment == "Unemployed"),
    "financial_stress":                financial_stress,
    "gender_Female":                   int(gender == "Female"),
    "grade_letter":                    grade_letter,
    "grade_score":                     grade_score,
    "grade_x_rate":                    grade_x_rate,
    "high_risk_flag":                  high_risk_flag,
    "income_per_credit":               income_per_credit,
    "interest_rate":                   interest_rate,
    "loan_amount":                     loan_amount,
    "loan_purpose_Business":           int(loan_purpose == "Business"),
    "loan_purpose_Education":          int(loan_purpose == "Education"),
    "loan_purpose_Home":               int(loan_purpose == "Home"),
    "loan_purpose_Medical":            int(loan_purpose == "Medical"),
    "loan_to_income":                  loan_to_income,
    "monthly_emi":                     monthly_emi,
    "rate_x_dti":                      rate_x_dti,
    "severe_risk_flag":                severe_risk_flag,
    "subprime_flag":                   subprime_flag,
}])

        X_scaled = scaler.transform(X)

        # ── Probability interpretation ─────────────────────────────────────────
        # Training target: loan_paid_back  (class 0 = Not Paid, class 1 = Paid Back)
        # predict_proba(X)[0][1] = P(loan_paid_back == 1) = P(repayment)
        # risk_probability = complement = P(default)
        prob_repayment        = float(model.predict_proba(X_scaled)[0][1])
        repayment_probability = prob_repayment * 100
        risk_probability      = 100 - repayment_probability

        # Store for Unified Dashboard
        st.session_state["dataset5_risk"] = risk_probability
        st.session_state["stress_index"]  = financial_stress

        # ── Risk classification (20 / 50 thresholds — matches other pages) ─────
        if risk_probability < 20:
            risk, color, rc_color, rc_bg = "LOW RISK",    "#16A34A", "#16A34A", "#F0FDF4"
        elif risk_probability < 50:
            risk, color, rc_color, rc_bg = "MEDIUM RISK", "#D97706", "#D97706", "#FFFBEB"
        else:
            risk, color, rc_color, rc_bg = "HIGH RISK",   "#DC2626", "#DC2626", "#FEF2F2"

        # ── Derived indicators preview ─────────────────────────────────────────
        st.markdown(
            '<div class="sec-label">Engineered Feature Summary</div>',
            unsafe_allow_html=True,
        )

        f1, f2, f3, f4 = st.columns(4, gap="medium")
        chips = [
            (f"{loan_to_income:.4f}",    "Loan-to-Income Ratio",  f1),
            (f"{monthly_emi:.2f}",       "Monthly EMI ($)",        f2),
            (f"{financial_stress:.2f}",  "Financial Stress Index", f3),
            (f"{debt_burden_ratio:.4f}", "Debt Burden Ratio",      f4),
        ]
        for val, lbl, col in chips:
            with col:
                st.markdown(f"""
                <div class="derived-chip">
                  <div class="derived-chip-val">{val}</div>
                  <div class="derived-chip-lbl">{lbl}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

        # ── Result metrics ─────────────────────────────────────────────────────
        st.markdown(
            '<div class="sec-label">Prediction Results</div>',
            unsafe_allow_html=True,
        )

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
              <div class="res-val" style="color:{color};">{risk_probability:.2f}%</div>
              <div class="res-lbl">Default Risk Probability</div>
            </div>
            """, unsafe_allow_html=True)
        with r3:
            st.markdown(f"""
            <div class="res-card">
              <div class="res-val" style="color:#D97706;">{financial_stress:.2f}</div>
              <div class="res-lbl">Financial Stress Index</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

        # ── Gauges (side by side) ──────────────────────────────────────────────
        st.markdown(
            '<div class="sec-label">Risk &amp; Stress Gauges</div>',
            unsafe_allow_html=True,
        )

        g1, g2 = st.columns(2, gap="medium")

        with g1:
            fig_risk = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk_probability,
                number={"suffix": "%", "font": {"size": 28}},
                title={"text": "Financial Default Risk", "font": {"size": 15}},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar":  {"color": color, "thickness": 0.25},
                    "bgcolor": "white",
                    "steps": [
                        {"range": [0,  20], "color": "#DCFCE7"},
                        {"range": [20, 50], "color": "#FEF9C3"},
                        {"range": [50, 100], "color": "#FEE2E2"},
                    ],
                },
            ))
            fig_risk.update_layout(
                height=280, margin=dict(t=40, b=10, l=20, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig_risk, use_container_width=True)

        with g2:
            stress_val   = min(100, financial_stress)
            stress_color = (
                "#16A34A" if stress_val < 30
                else ("#D97706" if stress_val < 60 else "#DC2626")
            )
            fig_stress = go.Figure(go.Indicator(
                mode="gauge+number",
                value=stress_val,
                number={"suffix": " /100", "font": {"size": 28}},
                title={"text": "Financial Stress Index", "font": {"size": 15}},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar":  {"color": stress_color, "thickness": 0.25},
                    "bgcolor": "white",
                    "steps": [
                        {"range": [0,  30], "color": "#DCFCE7"},
                        {"range": [30, 60], "color": "#FEF9C3"},
                        {"range": [60, 100], "color": "#FEE2E2"},
                    ],
                },
            ))
            fig_stress.update_layout(
                height=280, margin=dict(t=40, b=10, l=20, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig_stress, use_container_width=True)

        # ── Risk banner ────────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="risk-banner" style="background:{color};">
          {risk}
        </div>
        """, unsafe_allow_html=True)

        # ── Recommendation ─────────────────────────────────────────────────────
        st.markdown(
            '<div class="sec-label">AI Recommendation</div>',
            unsafe_allow_html=True,
        )

        if risk_probability < 20:
            rec_title = "✅ Financially Stable — Eligible for Approval"
            rec_body  = (
                "The applicant demonstrates strong financial stability with a low stress index "
                "and healthy repayment capacity. Credit score, debt burden, and income ratios "
                "all indicate minimal default risk. Recommended for full approval."
            )
        elif risk_probability < 50:
            rec_title = "⚠️ Moderate Instability — Conditional Approval"
            rec_body  = (
                "Moderate risk detected. Financial stress indicators show some vulnerability. "
                "Review employment stability and existing debt obligations. "
                "Conditional approval with reduced loan amount or additional collateral is advised."
            )
        else:
            rec_title = "❌ Financially Unstable — High Default Risk"
            rec_body  = (
                "High financial stress and elevated default probability indicators. "
                "The applicant's credit profile, debt burden, and income-to-loan ratios "
                "present significant repayment concerns. Loan approval is not recommended "
                "at this time without substantial financial restructuring."
            )

        st.markdown(f"""
        <div class="rec-card" style="--rc-color:{rc_color}; --rc-bg:{rc_bg};">
          <div class="rec-title" style="color:{rc_color};">{rec_title}</div>
          {rec_body}
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(
            f"⚠️ Prediction failed: {e}\n\n"
            "This may be due to a mismatch between the input features and the saved model. "
            "Please verify that `best_model_v2.pkl` and `scaler_v2.pkl` were produced by "
            "the v2 training pipeline and that the feature list matches `final_features.txt`."
        )

# ==============================================================================
#  FOOTER
# ==============================================================================

st.markdown("""
<div class="page-footer">
  <b>Dataset 5</b> &nbsp;·&nbsp; Financial Stability Prediction (XGBoost · AUPRC 0.9744) &nbsp;·&nbsp;
  RunaRakshaka &nbsp;·&nbsp; PES University MCA 2025–26
</div>
""", unsafe_allow_html=True)