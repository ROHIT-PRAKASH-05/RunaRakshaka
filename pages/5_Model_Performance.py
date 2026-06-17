# ==============================================================================
#  RunaRakshaka  —  Model Performance Dashboard
# ==============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.sidebar import render_sidebar
from components.shared_css import inject_shared_css

# ==============================================================================
#  PAGE CONFIG
# ==============================================================================

st.set_page_config(
    page_title="Model Performance — RunaRakshaka",
    page_icon="📊",
    layout="wide",
)

# ==============================================================================
#  DESIGN SYSTEM
# ==============================================================================

inject_shared_css()

st.markdown("""
<style>

.sec-label {
    font-size: .72rem; font-weight: 800; color: #E11D48;
    text-transform: uppercase; letter-spacing: .12em; margin: .2rem 0 .8rem;
}

.page-hero {
    background: linear-gradient(135deg, #FFF1F2 0%, #FDECEF 100%);
    border: 1px solid #FECDD3; border-radius: 20px;
    padding: 1.8rem 2rem 1.6rem; margin-bottom: 1.6rem;
    border-left: 4px solid #E11D48;
}
.page-hero-icon  { font-size: 2rem; margin-bottom: .4rem; }
.page-hero-title { font-size: 1.7rem; font-weight: 800; color: #1A1F36; margin-bottom: .2rem; }
.page-hero-sub   { font-size: .92rem; color: #6B7280; margin-bottom: .8rem; line-height: 1.6; }

.ds-header {
    background: #fff; border: 1px solid #E5E7EB; border-radius: 14px;
    padding: .9rem 1.2rem; margin-bottom: .8rem;
    border-left: 4px solid var(--ds-color, #E11D48);
    display: flex; align-items: center; gap: .7rem;
}
.ds-header-icon  { font-size: 1.4rem; }
.ds-header-title { font-size: 1.05rem; font-weight: 800; color: #1A1F36; }
.ds-header-sub   { font-size: .8rem; color: #6B7280; }

.metric-tile {
    background: #fff; border: 1px solid #E5E7EB; border-radius: 14px;
    padding: 1rem .9rem; text-align: center;
    box-shadow: 0 1px 2px rgba(16,24,40,.04);
    border-top: 3px solid var(--mt-color, #E11D48);
}
.metric-tile-val { font-size: 1.5rem; font-weight: 800; color: var(--mt-color, #E11D48); }
.metric-tile-lbl { font-size: .75rem; color: #6B7280; margin-top: 3px; font-weight: 600; }

.best-model-card {
    background: linear-gradient(135deg, #F0FDF4 0%, #E6F9FC 100%);
    border: 1px solid #BBF7D0; border-radius: 16px;
    padding: 1.3rem 1.6rem; margin-bottom: 1rem;
}
.best-model-label { font-size: .68rem; font-weight: 800; color: #16A34A;
    text-transform: uppercase; letter-spacing: .12em; margin-bottom: .4rem; }
.best-model-title { font-size: 1.05rem; font-weight: 800; color: #1A1F36; margin-bottom: .2rem; }
.best-model-sub   { font-size: .82rem; color: #6B7280; margin-bottom: .8rem; }
.badge-row  { display: flex; flex-wrap: wrap; gap: 8px; }
.badge {
    background: #fff; border: 1px solid #BBF7D0; border-radius: 10px;
    padding: 6px 14px; font-size: .82rem; font-weight: 700; color: #1A1F36;
}
.badge span { color: #16A34A; }

.step-row { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; }
.step-num {
    width: 22px; height: 22px; border-radius: 50%; background: #E11D48;
    color: #fff; font-size: .64rem; font-weight: 800;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.step-text { font-size: .84rem; color: #1A1F36; padding-top: 2px; font-weight: 500; }

.tech-badge {
    background: #fff; border: 1px solid #E5E7EB; border-radius: 10px;
    padding: 8px 6px; text-align: center; font-size: .78rem; font-weight: 700;
    margin-bottom: .5rem;
}

</style>
""", unsafe_allow_html=True)

# ==============================================================================
#  SIDEBAR
# ==============================================================================

render_sidebar()

# ==============================================================================
#  METRIC DATA
# ==============================================================================

dataset2 = {"Accuracy": 0.8200, "F1 Score": 0.5400, "ROC-AUC": 0.7400, "Precision": 0.5800}
dataset3 = {"Accuracy": 0.8900, "F1 Score": 0.8100, "ROC-AUC": 0.9377, "Precision": 0.8300}
dataset5 = {"Accuracy": 0.8999, "F1 Macro": 0.8357, "ROC-AUC": 0.9200, "AUPRC":    0.9744}

# ==============================================================================
#  PAGE HERO
# ==============================================================================

st.markdown("""
<div class="page-hero">
  <div class="page-hero-icon">📊</div>
  <div class="page-hero-title">Model Performance Dashboard</div>
  <div class="page-hero-sub">
    Evaluation metrics, ROC-AUC comparison, and feature importance across all three
    machine learning models trained for the RunaRakshaka platform.
  </div>
  <span class="pill pill-red">3 Models Evaluated</span>
  <span class="pill pill-green">Best ROC-AUC 0.9377</span>
  <span class="pill pill-violet">XGBoost + Random Forest</span>
  <span class="pill pill-amber">SMOTEENN Balanced</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  BEST MODEL CALLOUT
# ==============================================================================

st.markdown("""
<div class="best-model-card">
  <div class="best-model-label">⭐ Best Performing Model — Dataset 3</div>
  <div class="best-model-title">Personal Loan Risk Prediction (Random Forest)</div>
  <div class="best-model-sub">Highest ROC-AUC across all three models at 0.9377</div>
  <div class="badge-row">
    <div class="badge">Accuracy &nbsp;<span>89%</span></div>
    <div class="badge">ROC-AUC &nbsp;<span>0.9377</span></div>
    <div class="badge">F1 Score &nbsp;<span>0.8100</span></div>
    <div class="badge">Precision &nbsp;<span>0.8300</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  DATASET 2
# ==============================================================================

st.markdown('<div class="sec-label">Dataset 2 — Credit Card Default Prediction</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ds-header" style="--ds-color:#00B4D8;">
  <div class="ds-header-icon">💳</div>
  <div>
    <div class="ds-header-title">Credit Card Default Risk Model</div>
    <div class="ds-header-sub">XGBoost &nbsp;·&nbsp; 9 Features &nbsp;·&nbsp; 30,000 Records &nbsp;·&nbsp; Dataset 2
    &nbsp;·&nbsp; <em style="color:#D97706;">Note: ROC-AUC 0.74 — weaker than other models; use with additional verification</em></div>
  </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
d2_metrics = [
    ("Accuracy",  f"{dataset2['Accuracy']:.4f}",  "#00B4D8"),
    ("F1 Score",  f"{dataset2['F1 Score']:.4f}",  "#7C3AED"),
    ("ROC-AUC",   f"{dataset2['ROC-AUC']:.4f}",   "#16A34A"),
    ("Precision", f"{dataset2['Precision']:.4f}",  "#D97706"),
]
for col, (lbl, val, mc) in zip(cols, d2_metrics):
    with col:
        st.markdown(f"""
        <div class="metric-tile" style="--mt-color:{mc};">
          <div class="metric-tile-val">{val}</div>
          <div class="metric-tile-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  DATASET 3
# ==============================================================================

st.markdown('<div class="sec-label">Dataset 3 — Personal Loan Risk Prediction</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ds-header" style="--ds-color:#16A34A;">
  <div class="ds-header-icon">🏦</div>
  <div>
    <div class="ds-header-title">Personal Loan Default Risk Model</div>
    <div class="ds-header-sub">Random Forest &nbsp;·&nbsp; 8 Features &nbsp;·&nbsp; 32,581 Records &nbsp;·&nbsp; Dataset 3</div>
  </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
d3_metrics = [
    ("Accuracy",  f"{dataset3['Accuracy']:.4f}",  "#00B4D8"),
    ("F1 Score",  f"{dataset3['F1 Score']:.4f}",  "#7C3AED"),
    ("ROC-AUC",   f"{dataset3['ROC-AUC']:.4f}",   "#16A34A"),
    ("Precision", f"{dataset3['Precision']:.4f}",  "#D97706"),
]
for col, (lbl, val, mc) in zip(cols, d3_metrics):
    with col:
        st.markdown(f"""
        <div class="metric-tile" style="--mt-color:{mc};">
          <div class="metric-tile-val">{val}</div>
          <div class="metric-tile-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  DATASET 5
# ==============================================================================

st.markdown('<div class="sec-label">Dataset 5 — Financial Stability Prediction</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ds-header" style="--ds-color:#D97706;">
  <div class="ds-header-icon">📈</div>
  <div>
    <div class="ds-header-title">Financial Stability Prediction Model</div>
    <div class="ds-header-sub">XGBoost &nbsp;·&nbsp; 29 Features &nbsp;·&nbsp; ~10,000 Records &nbsp;·&nbsp; Dataset 5</div>
  </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
d5_metrics = [
    ("Accuracy", f"{dataset5['Accuracy']:.4f}", "#00B4D8"),
    ("F1 Macro", f"{dataset5['F1 Macro']:.4f}", "#7C3AED"),
    ("ROC-AUC",  f"{dataset5['ROC-AUC']:.4f}",  "#16A34A"),
    ("AUPRC",    f"{dataset5['AUPRC']:.4f}",     "#D97706"),
]
for col, (lbl, val, mc) in zip(cols, d5_metrics):
    with col:
        st.markdown(f"""
        <div class="metric-tile" style="--mt-color:{mc};">
          <div class="metric-tile-val">{val}</div>
          <div class="metric-tile-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  COMPARISON CHARTS  — FIX: barmode="group" (was "overlay")
# ==============================================================================

st.markdown('<div class="sec-label">Cross-Model Comparison</div>', unsafe_allow_html=True)

chart_left, chart_right = st.columns(2, gap="medium")

with chart_left:
    roc_fig = go.Figure()
    ds_labels  = ["Dataset 2<br>(Credit Card)", "Dataset 3<br>(Personal Loan)", "Dataset 5<br>(Financial Stability)"]
    roc_values = [dataset2["ROC-AUC"], dataset3["ROC-AUC"], dataset5["ROC-AUC"]]
    bar_colors = ["#00B4D8", "#16A34A", "#D97706"]

    roc_fig.add_trace(go.Bar(
        x=ds_labels, y=roc_values,
        marker_color=bar_colors,
        text=[f"{v:.4f}" for v in roc_values],
        textposition="outside",
        width=0.5,
    ))
    roc_fig.update_layout(
        title="ROC-AUC Comparison",
        yaxis=dict(range=[0, 1.1], title="ROC-AUC Score"),
        height=340, plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=50, b=20, l=10, r=10),
        showlegend=False,
    )
    st.plotly_chart(roc_fig, use_container_width=True)

with chart_right:
    # FIX: barmode="group" so bars sit side-by-side, not overlapping
    comp_fig = go.Figure()
    acc_vals = [dataset2["Accuracy"], dataset3["Accuracy"], dataset5["Accuracy"]]
    f1_vals  = [dataset2["F1 Score"], dataset3["F1 Score"], dataset5["F1 Macro"]]
    ds_short = ["Dataset 2", "Dataset 3", "Dataset 5"]

    comp_fig.add_trace(go.Bar(
        name="Accuracy", x=ds_short, y=acc_vals,
        marker_color="#00B4D8",
        text=[f"{v:.4f}" for v in acc_vals],
        textposition="outside",
    ))
    comp_fig.add_trace(go.Bar(
        name="F1 Score", x=ds_short, y=f1_vals,
        marker_color="#7C3AED",
        text=[f"{v:.4f}" for v in f1_vals],
        textposition="outside",
    ))
    comp_fig.update_layout(
        title="Accuracy vs F1 Score",
        yaxis=dict(range=[0, 1.15], title="Score"),
        height=340, plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=50, b=20, l=10, r=10),
        barmode="group",   # ← FIXED (was "overlay")
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    st.plotly_chart(comp_fig, use_container_width=True)

# ==============================================================================
#  FULL METRIC COMPARISON TABLE
# ==============================================================================

st.markdown('<div class="sec-label">Full Metric Comparison</div>', unsafe_allow_html=True)

comparison_df = pd.DataFrame({
    "Dataset":  ["Dataset 2 — Credit Card",   "Dataset 3 — Personal Loan",  "Dataset 5 — Financial Stability"],
    "Model":    ["XGBoost",                    "Random Forest",               "XGBoost"],
    "Accuracy": [dataset2["Accuracy"],          dataset3["Accuracy"],           dataset5["Accuracy"]],
    "F1 Score": [dataset2["F1 Score"],          dataset3["F1 Score"],           dataset5["F1 Macro"]],
    "ROC-AUC":  [dataset2["ROC-AUC"],           dataset3["ROC-AUC"],            dataset5["ROC-AUC"]],
    "Features": [9,                             8,                              29],
})

st.dataframe(
    comparison_df.style.format({
        "Accuracy": "{:.4f}",
        "F1 Score": "{:.4f}",
        "ROC-AUC":  "{:.4f}",
    }).highlight_max(subset=["Accuracy", "F1 Score", "ROC-AUC"], color="#DCFCE7"),
    use_container_width=True,
    hide_index=True,
)

st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  ML PIPELINE  +  TECH STACK
# ==============================================================================

left, right = st.columns([3, 2], gap="large")

with left:
    st.markdown('<div class="sec-label">Machine Learning Pipeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    steps = [
        "Data Collection & Cleaning",
        "Exploratory Data Analysis",
        "Feature Engineering",
        "VIF Analysis (Multicollinearity)",
        "SelectKBest Feature Selection",
        "RFE Recursive Feature Elimination",
        "Train / Test Split (80:20)",
        "Standard Scaling (Z-score)",
        "SMOTEENN Class Balancing",
        "Model Training (XGBoost / RF)",
        "Hyperparameter Tuning (GridSearchCV)",
        "Threshold Optimisation",
        "Evaluation (ROC-AUC, F1, Accuracy)",
        "Streamlit Deployment",
        "Session-State Unified Dashboard",
    ]
    s_cols = st.columns(2)
    for i, step in enumerate(steps):
        with s_cols[i % 2]:
            st.markdown(f"""
            <div class="step-row">
              <div class="step-num">{i + 1}</div>
              <div class="step-text">{step}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="sec-label">Technology Stack</div>', unsafe_allow_html=True)
    tech = [
        ("Python 3.11",      "#00B4D8"), ("Streamlit",      "#E11D48"),
        ("XGBoost",          "#D97706"), ("Scikit-learn",   "#16A34A"),
        ("imbalanced-learn", "#7C3AED"), ("Pandas",         "#00B4D8"),
        ("NumPy",            "#D97706"), ("Plotly",         "#E11D48"),
        ("Joblib",           "#16A34A"), ("Matplotlib",     "#7C3AED"),
    ]
    t_cols = st.columns(2)
    for i, (name, color) in enumerate(tech):
        with t_cols[i % 2]:
            st.markdown(f"""
            <div class="tech-badge" style="color:{color};">{name}</div>
            """, unsafe_allow_html=True)

st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)

# ==============================================================================
#  PROJECT SUMMARY
# ==============================================================================

st.markdown('<div class="sec-label">Project Summary</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
  <div style="font-size:.92rem; color:#1A1F36; line-height:1.8;">
    <strong>RunaRakshaka</strong> is an AI-based Debt Risk Prediction and Financial Stability System
    that integrates three independent machine learning models into a unified financial intelligence
    platform. Each model targets a distinct risk domain — credit card default behaviour,
    personal loan default probability, and overall financial stability — and is trained
    on real-world datasets using rigorous feature engineering, class-balancing, and
    threshold-optimisation pipelines.<br><br>
    The platform culminates in a <strong>Weighted Ensemble Unified Dashboard</strong> that
    consolidates predictions from all three models into a single interpretable risk score,
    supported by an AI-generated recommendation engine. This project supports
    <strong>SDG 1 — No Poverty</strong> by promoting responsible lending and financial inclusion.
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  FOOTER
# ==============================================================================

st.markdown("""
<div class="page-footer">
  <b>Model Performance Dashboard</b> &nbsp;·&nbsp; RunaRakshaka &nbsp;·&nbsp;
  PES University MCA 2025–26 &nbsp;·&nbsp; Rohit P &nbsp;·&nbsp; PES1PG25CA325
</div>
""", unsafe_allow_html=True)