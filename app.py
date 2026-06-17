# ==============================================================================
#  RunaRakshaka
#  AI-Based Debt Risk Prediction & Financial Stability System
#  Home Page  (app entry point)
# ==============================================================================

import os
import base64
import streamlit as st
from components.sidebar import render_sidebar
from components.shared_css import inject_shared_css

st.set_page_config(
    page_title="RunaRakshaka",
    page_icon="🛡️",
    layout="wide",
)

inject_shared_css()

# ==============================================================================
#  CACHED HELPERS
# ==============================================================================

@st.cache_data
def get_file_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


@st.cache_data
def get_svg_b64(svg_string: str) -> str:
    return base64.b64encode(svg_string.encode("utf-8")).decode()


# ==============================================================================
#  SIDEBAR
# ==============================================================================

render_sidebar()

# ==============================================================================
#  HERO
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "logo.png")

if os.path.exists(logo_path):
    logo_b64 = get_file_b64(logo_path)
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center;
                width:100%; padding-top:.6rem;">
      <img src="data:image/png;base64,{logo_b64}" alt="RunaRakshaka logo"
           style="width:90px; height:auto; display:block;" />
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-title">RunaRakshaka</div>
  <div class="hero-sub">
    AI-Based Debt Risk Prediction &amp; Financial Stability System
  </div>
  <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center; margin-top:.2rem;">
    <span class="pill pill-blue">3 ML Models</span>
    <span class="pill pill-green">XGBoost + Random Forest</span>
    <span class="pill pill-amber">Real-Time Prediction</span>
    <span class="pill pill-violet">SDG 1 — No Poverty</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  PROJECT HIGHLIGHTS
# ==============================================================================

st.markdown('<div class="sec-label">Project Highlights</div>', unsafe_allow_html=True)

stats = [
    ("3",      "ML Models",    "var(--primary)"),
    ("0.9377", "Best ROC-AUC", "var(--green)"),
    ("89.99%", "Accuracy",     "var(--amber)"),
    ("0.8357", "F1 Score",     "var(--violet)"),
]
cols = st.columns(4)
for col, (val, lbl, color) in zip(cols, stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
          <div class="stat-val" style="color:{color};">{val}</div>
          <div class="stat-lbl">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="vspace-lg"></div>', unsafe_allow_html=True)

# ==============================================================================
#  SYSTEM MODULES  —  ROW 1
# ==============================================================================

st.markdown('<div class="sec-label">System Modules</div>', unsafe_allow_html=True)

modules_row1 = [
    dict(
        icon="💳", title="Credit Card Risk",
        accent="#00B4D8", soft="#E0F7FB",
        page="pages/1_Credit_Card_Risk.py",
        desc="Predict whether a credit card customer is likely to default on their next payment.",
        chips=["Credit Limit", "Payment Behaviour", "Credit Utilisation", "Payment Ratio"],
    ),
    dict(
        icon="🏦", title="Personal Loan Risk",
        accent="#16A34A", soft="#DCFCE7",
        page="pages/2_Personal_Loan_Risk.py",
        desc="Assess the probability of default for a personal loan applicant.",
        chips=["Income", "Loan Amount", "Loan Grade", "Loan Intent"],
    ),
    dict(
        icon="📈", title="Financial Stability",
        accent="#D97706", soft="#FEF3C7",
        page="pages/3_Financial_Stability.py",
        desc="Predict repayment probability and overall financial health score.",
        chips=["Credit Score", "Income", "Debt Ratio", "Financial Stress"],
    ),
]

cols = st.columns(3, gap="medium")
for col, m in zip(cols, modules_row1):
    chip_html = "".join(f'<span class="chip">{c}</span>' for c in m["chips"])
    with col:
        st.markdown(f"""
        <div class="mod-card" style="--mod-accent:{m['accent']}; --mod-accent-soft:{m['soft']};">
          <div class="mod-icon">{m['icon']}</div>
          <div class="mod-title">{m['title']}</div>
          <div class="mod-desc">{m['desc']}</div>
          <div class="chip-row">{chip_html}</div>
          <div class="mod-cta">Open {m['title']} <span aria-hidden="true">→</span></div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Open {m['title']}", key=m["page"], use_container_width=True):
            st.switch_page(m["page"])

st.markdown('<div class="vspace-md"></div>', unsafe_allow_html=True)

# ==============================================================================
#  SYSTEM MODULES  —  ROW 2
# ==============================================================================

modules_row2 = [
    dict(
        icon="🤖", title="Unified Risk Dashboard",
        accent="#7C3AED", soft="#EDE9FE",
        page="pages/4_Unified_Risk_Dashboard.py",
        desc=(
            "Combines predictions from all three models into a single AI-generated "
            "risk score with weighted contributions."
        ),
        chips=["Weighted Ensemble", "Risk Classification", "Recommendation Engine"],
    ),
    dict(
        icon="📊", title="Model Performance",
        accent="#E11D48", soft="#FFE4E9",
        page="pages/5_Model_Performance.py",
        desc=(
            "Compare accuracy, ROC-AUC, F1 score and feature importance "
            "across all trained models."
        ),
        chips=["Model Comparison", "ROC Curves", "Feature Importance"],
    ),
]

cols = st.columns(2, gap="medium")
for col, m in zip(cols, modules_row2):
    chip_html = "".join(f'<span class="chip">{c}</span>' for c in m["chips"])
    with col:
        st.markdown(f"""
        <div class="mod-card" style="--mod-accent:{m['accent']}; --mod-accent-soft:{m['soft']};">
          <div class="mod-icon">{m['icon']}</div>
          <div class="mod-title">{m['title']}</div>
          <div class="mod-desc">{m['desc']}</div>
          <div class="chip-row">{chip_html}</div>
          <div class="mod-cta">Open {m['title']} <span aria-hidden="true">→</span></div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Open {m['title']}", key=m["page"], use_container_width=True):
            st.switch_page(m["page"])

st.markdown('<div class="vspace-lg"></div>', unsafe_allow_html=True)

# ==============================================================================
#  UNIFIED AI ENGINE  +  SDG
# ==============================================================================

left, right = st.columns([3, 2], gap="large")

with left:
    st.markdown('<div class="sec-label">Unified AI Risk Engine</div>', unsafe_allow_html=True)

    engine_svg = """<svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M0,0 L7,3.5 L0,7 Z" fill="#94A3B8"/>
        </marker>
      </defs>

      <!-- Dataset 2 -->
      <rect x="16" y="14" width="168" height="62" rx="13" fill="#E0F7FB" stroke="#00B4D8" stroke-width="1.5"/>
      <text x="100" y="36"  text-anchor="middle" font-size="11" font-weight="700" fill="#0096B7"  font-family="Inter,Arial,sans-serif">Dataset 2</text>
      <text x="100" y="54"  text-anchor="middle" font-size="10.5"                 fill="#0F172A"  font-family="Inter,Arial,sans-serif">Credit Card Default</text>
      <text x="100" y="69"  text-anchor="middle" font-size="9"   font-weight="700" fill="#00B4D8"  font-family="Inter,Arial,sans-serif">weight 25 %</text>

      <!-- Dataset 3 -->
      <rect x="16" y="109" width="168" height="62" rx="13" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
      <text x="100" y="131" text-anchor="middle" font-size="11" font-weight="700" fill="#16A34A"  font-family="Inter,Arial,sans-serif">Dataset 3</text>
      <text x="100" y="149" text-anchor="middle" font-size="10.5"                 fill="#0F172A"  font-family="Inter,Arial,sans-serif">Personal Loan Risk</text>
      <text x="100" y="164" text-anchor="middle" font-size="9"   font-weight="700" fill="#16A34A"  font-family="Inter,Arial,sans-serif">weight 35 %</text>

      <!-- Dataset 5 -->
      <rect x="16" y="204" width="168" height="62" rx="13" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/>
      <text x="100" y="226" text-anchor="middle" font-size="11" font-weight="700" fill="#D97706"  font-family="Inter,Arial,sans-serif">Dataset 5</text>
      <text x="100" y="244" text-anchor="middle" font-size="10.5"                 fill="#0F172A"  font-family="Inter,Arial,sans-serif">Financial Stability</text>
      <text x="100" y="259" text-anchor="middle" font-size="9"   font-weight="700" fill="#D97706"  font-family="Inter,Arial,sans-serif">weight 40 %</text>

      <!-- Connector curves -->
      <path d="M184,45  C250,45  250,140 320,140" fill="none" stroke="#00B4D8" stroke-width="2"   opacity=".5" stroke-linecap="round"/>
      <path d="M184,140 L320,140"                 fill="none" stroke="#16A34A" stroke-width="2.6" opacity=".5" stroke-linecap="round"/>
      <path d="M184,235 C250,235 250,140 320,140" fill="none" stroke="#D97706" stroke-width="3"   opacity=".5" stroke-linecap="round"/>
      <path d="M316,140 L325,140" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Ensemble box -->
      <rect x="328" y="94" width="158" height="92" rx="16" fill="#F5F3FF" stroke="#7C3AED" stroke-width="1.8"/>
      <text x="407" y="124" text-anchor="middle" font-size="12" font-weight="800" fill="#7C3AED" font-family="Inter,Arial,sans-serif">Weighted</text>
      <text x="407" y="141" text-anchor="middle" font-size="12" font-weight="800" fill="#7C3AED" font-family="Inter,Arial,sans-serif">Ensemble</text>
      <text x="407" y="160" text-anchor="middle" font-size="9.5"                  fill="#64748B" font-family="Inter,Arial,sans-serif">0.25 + 0.35 + 0.40 = 1.00</text>

      <path d="M486,140 L530,140" fill="none" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arr)"/>

      <!-- Output box -->
      <rect x="534" y="100" width="92" height="80" rx="14" fill="#FFFFFF" stroke="#E6E9F0" stroke-width="1.5"/>
      <text x="580" y="128" text-anchor="middle" font-size="10.5" font-weight="800" fill="#0F172A" font-family="Inter,Arial,sans-serif">Overall</text>
      <text x="580" y="145" text-anchor="middle" font-size="10.5" font-weight="800" fill="#0F172A" font-family="Inter,Arial,sans-serif">Risk</text>
      <text x="580" y="162" text-anchor="middle" font-size="10.5" font-weight="800" fill="#0F172A" font-family="Inter,Arial,sans-serif">Score</text>
    </svg>"""

    engine_b64 = get_svg_b64(engine_svg)
    st.markdown(f"""
    <div class="content-card">
      <div style="font-size:.88rem; color:var(--ink-soft,#1E293B); line-height:1.75; margin-bottom:.9rem;">
        The Unified Dashboard combines outputs from all three trained models into
        one consolidated risk score, weighted by each model's validation performance.
      </div>
      <img src="data:image/svg+xml;base64,{engine_b64}"
           alt="Weighted ensemble diagram: Dataset 2/3/5 → Ensemble → Overall Risk Score"
           style="width:100%; height:auto; max-width:560px; display:block; margin:0 auto;" />
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="sec-label">Sustainable Development Goal</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content-card" style="border-left:4px solid var(--green,#16A34A);">
      <div style="font-weight:800; color:var(--green,#16A34A); font-size:.95rem; margin-bottom:.5rem;
                  font-family:'Plus Jakarta Sans','Inter',sans-serif;">
        🌍 SDG 1 — No Poverty
      </div>
      <div style="font-size:.86rem; color:var(--ink,#0F172A); line-height:1.7;">
        This project supports financial inclusion and responsible lending by
        helping institutions identify financial stress and repayment risk early —
        preventing families from falling into unsustainable debt cycles.
      </div>
    </div>

    <div class="content-card" style="border-left:4px solid var(--primary,#00B4D8); margin-top:.8rem;">
      <div style="font-weight:800; color:var(--primary-dark,#0096B7); font-size:.95rem; margin-bottom:.5rem;
                  font-family:'Plus Jakarta Sans','Inter',sans-serif;">
        🎯 Project Goal
      </div>
      <div style="font-size:.86rem; color:var(--ink,#0F172A); line-height:1.7;">
        Build an accurate, explainable multi-model system that lenders and
        individuals can rely on to make confident, fair credit decisions.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="vspace-lg"></div>', unsafe_allow_html=True)

# ==============================================================================
#  TECHNOLOGY STACK  +  ML PIPELINE
# ==============================================================================

left, right = st.columns([2, 3], gap="large")

with left:
    st.markdown('<div class="sec-label">Technology Stack</div>', unsafe_allow_html=True)
    tech = [
        ("Python",        "var(--primary)"),
        ("Streamlit",     "var(--red,#E11D48)"),
        ("XGBoost",       "var(--amber)"),
        ("Scikit-learn",  "var(--green)"),
        ("Pandas",        "var(--primary)"),
        ("NumPy",         "var(--violet)"),
    ]
    t_cols = st.columns(2)
    for i, (name, color) in enumerate(tech):
        with t_cols[i % 2]:
            st.markdown(
                f'<div class="tech-badge" style="color:{color}; margin-bottom:.5rem;">{name}</div>',
                unsafe_allow_html=True,
            )

with right:
    st.markdown('<div class="sec-label">Machine Learning Pipeline</div>', unsafe_allow_html=True)
    steps = [
        "Data Collection & Cleaning",
        "Feature Engineering",
        "VIF + SelectKBest + RFE",
        "SMOTEENN Class Balancing",
        "Hyperparameter Tuning",
        "Threshold Optimisation",
        "Model Evaluation",
        "Streamlit Deployment",
    ]
    step_html = "".join(
        f'<div class="step-row">'
        f'<div class="step-num">{i + 1}</div>'
        f'<div class="step-text">{step}</div>'
        f'</div>'
        for i, step in enumerate(steps)
    )
    st.markdown(
        f'<div class="content-card" '
        f'style="display:grid; grid-template-columns:1fr 1fr; gap:0 1.2rem;">'
        f'{step_html}</div>',
        unsafe_allow_html=True,
    )

# ==============================================================================
#  FOOTER
# ==============================================================================

st.markdown("""
<div class="footer">
  <div style="font-size:1.4rem; margin-bottom:.3rem;">🛡️</div>
  <strong>RunaRakshaka</strong><br>
  AI-Based Debt Risk Prediction &amp; Financial Stability System<br>
  PES University &nbsp;·&nbsp; MCA Project &nbsp;·&nbsp; 2025–26
</div>
""", unsafe_allow_html=True)