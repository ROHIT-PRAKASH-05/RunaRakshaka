# ==============================================================================
#  RunaRakshaka  —  Unified AI Risk Dashboard
# ==============================================================================

import streamlit as st
import plotly.graph_objects as go

from components.sidebar import render_sidebar

# ==============================================================================
#  PAGE CONFIG
# ==============================================================================

st.set_page_config(
    page_title="Unified Dashboard — RunaRakshaka",
    page_icon="🤖",
    layout="wide",
)

# ==============================================================================
#  DESIGN SYSTEM  (self-contained — no dependency on shared_css for these classes)
# ==============================================================================

st.markdown("""
<style>
/* ── Google Font ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; }

/* Remove Streamlit's default top padding */
.block-container { padding-top: 1.4rem !important; }

/* ── Tokens ──────────────────────────────────────────────────────────────── */
:root {
  --purple-50:  #F5F3FF;
  --purple-100: #EDE9FE;
  --purple-200: #DDD6FE;
  --purple-600: #7C3AED;
  --purple-700: #6D28D9;

  --blue-400:   #38BDF8;
  --blue-500:   #00B4D8;
  --green-600:  #16A34A;
  --amber-600:  #D97706;
  --red-600:    #DC2626;

  --gray-50:    #F8F9FB;
  --gray-100:   #F1F5F9;
  --gray-200:   #E5E7EB;
  --gray-400:   #9CA3AF;
  --gray-500:   #6B7280;
  --gray-900:   #1A1F36;

  --radius-sm:  10px;
  --radius-md:  16px;
  --radius-lg:  20px;
  --shadow-sm:  0 1px 3px rgba(16,24,40,.06), 0 1px 2px rgba(16,24,40,.04);
  --shadow-md:  0 4px 16px rgba(16,24,40,.08);
}

/* ── Section label ───────────────────────────────────────────────────────── */
.sec-label {
  font-family: 'Inter', sans-serif;
  font-size: .68rem;
  font-weight: 800;
  color: var(--purple-600);
  text-transform: uppercase;
  letter-spacing: .14em;
  margin: .2rem 0 .9rem;
  display: flex;
  align-items: center;
  gap: .5rem;
}
.sec-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--purple-200);
}

/* ── Pills ───────────────────────────────────────────────────────────────── */
.pill {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  padding: .25rem .75rem;
  border-radius: 99px;
  font-family: 'Inter', sans-serif;
  font-size: .72rem;
  font-weight: 700;
  margin: .25rem .2rem .25rem 0;
}
.pill-violet { background: var(--purple-100); color: var(--purple-700); border: 1px solid var(--purple-200); }
.pill-blue   { background: #E0F7FF; color: #0077A8; border: 1px solid #BAE6FD; }
.pill-green  { background: #F0FDF4; color: var(--green-600); border: 1px solid #BBF7D0; }
.pill-amber  { background: #FFFBEB; color: var(--amber-600); border: 1px solid #FDE68A; }

/* ── Page Hero ───────────────────────────────────────────────────────────── */
.page-hero {
  background: linear-gradient(135deg, var(--purple-50) 0%, var(--purple-100) 100%);
  border: 1px solid var(--purple-200);
  border-left: 4px solid var(--purple-600);
  border-radius: var(--radius-lg);
  padding: 1.8rem 2.2rem 1.6rem;
  margin-bottom: 1.8rem;
}
.page-hero-icon  { font-size: 2rem; margin-bottom: .35rem; }
.page-hero-title {
  font-family: 'Inter', sans-serif;
  font-size: 1.8rem;
  font-weight: 900;
  color: var(--gray-900);
  margin-bottom: .3rem;
  letter-spacing: -.02em;
}
.page-hero-sub {
  font-family: 'Inter', sans-serif;
  font-size: .9rem;
  color: var(--gray-500);
  margin-bottom: 1rem;
  line-height: 1.7;
  max-width: 72ch;
}

/* ── Model cards ─────────────────────────────────────────────────────────── */
.model-card {
  background: #fff;
  border: 1px solid var(--gray-200);
  border-top: 3px solid var(--mc-color, var(--purple-600));
  border-radius: var(--radius-md);
  padding: 1.1rem 1rem 1rem;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: box-shadow .2s ease, transform .2s ease;
  height: 100%;
}
.model-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
.model-card-icon   { font-size: 1.4rem; margin-bottom: .35rem; }
.model-card-title  {
  font-family: 'Inter', sans-serif;
  font-size: .76rem;
  font-weight: 800;
  color: var(--gray-900);
  margin-bottom: .5rem;
  text-transform: uppercase;
  letter-spacing: .04em;
}
.model-card-risk   {
  font-family: 'Inter', sans-serif;
  font-size: 1.8rem;
  font-weight: 900;
  color: var(--mc-color, var(--purple-600));
  line-height: 1;
  margin-bottom: .2rem;
}
.model-card-weight {
  font-family: 'Inter', sans-serif;
  font-size: .7rem;
  color: var(--gray-400);
  font-weight: 600;
  margin-top: .25rem;
}
.model-card-contrib {
  font-family: 'Inter', sans-serif;
  font-size: .78rem;
  font-weight: 800;
  color: var(--gray-900);
  margin-top: .3rem;
  background: var(--gray-50);
  border-radius: 6px;
  padding: .2rem .5rem;
  display: inline-block;
}

/* ── Overall card ────────────────────────────────────────────────────────── */
.overall-card {
  background: linear-gradient(135deg, var(--purple-50) 0%, var(--purple-100) 100%);
  border: 1px solid var(--purple-200);
  border-radius: var(--radius-md);
  padding: 1.3rem 1.2rem 1.2rem;
  text-align: center;
  box-shadow: 0 4px 20px rgba(124,58,237,.12);
  height: 100%;
}
.overall-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: .65rem;
  font-weight: 800;
  color: var(--purple-600);
  text-transform: uppercase;
  letter-spacing: .12em;
  margin-bottom: .5rem;
}
.overall-val {
  font-family: 'Inter', sans-serif;
  font-size: 2.6rem;
  font-weight: 900;
  line-height: 1;
  letter-spacing: -.02em;
}
.overall-lbl {
  font-family: 'Inter', sans-serif;
  font-size: .78rem;
  color: var(--gray-500);
  font-weight: 600;
  margin-top: .4rem;
}
.overall-level {
  font-family: 'Inter', sans-serif;
  margin-top: .7rem;
  font-size: .82rem;
  font-weight: 800;
  padding: .3rem .8rem;
  border-radius: 99px;
  display: inline-block;
}

/* ── Risk banner ─────────────────────────────────────────────────────────── */
.risk-banner {
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #fff;
  text-align: center;
  padding: .85rem 1.5rem;
  border-radius: var(--radius-md);
  margin: 1rem 0;
  box-shadow: var(--shadow-sm);
}

/* ── Warn card ───────────────────────────────────────────────────────────── */
.warn-card {
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  border-left: 4px solid var(--amber-600);
  border-radius: var(--radius-md);
  padding: 1.2rem 1.5rem;
  margin-bottom: 1rem;
}
.warn-title {
  font-family: 'Inter', sans-serif;
  font-weight: 800;
  color: var(--amber-600);
  font-size: .95rem;
  margin-bottom: .5rem;
}
.warn-body {
  font-family: 'Inter', sans-serif;
  font-size: .86rem;
  color: var(--gray-900);
  line-height: 1.7;
}

/* ── Content card ────────────────────────────────────────────────────────── */
.content-card {
  background: #fff;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius-md);
  padding: 1.2rem 1.4rem;
  box-shadow: var(--shadow-sm);
}

/* ── Recommendation card ─────────────────────────────────────────────────── */
.rec-card {
  background: var(--rc-bg, #F5F3FF);
  border: 1px solid var(--rc-border, var(--purple-200));
  border-left: 4px solid var(--rc-color, var(--purple-600));
  border-radius: var(--radius-md);
  padding: 1.4rem 1.8rem;
  box-shadow: var(--shadow-sm);
  font-family: 'Inter', sans-serif;
  font-size: .9rem;
  color: var(--gray-900);
  line-height: 1.75;
}
.rec-title {
  font-family: 'Inter', sans-serif;
  font-size: 1.05rem;
  font-weight: 800;
  margin-bottom: .65rem;
  color: var(--rc-color, var(--purple-600));
}

/* ── Page footer ─────────────────────────────────────────────────────────── */
.page-footer {
  font-family: 'Inter', sans-serif;
  font-size: .76rem;
  color: var(--gray-400);
  text-align: center;
  padding: 1.4rem 0 .6rem;
  border-top: 1px solid var(--gray-200);
  margin-top: 2rem;
}
.page-footer b { color: var(--purple-600); }

/* ── Divider ─────────────────────────────────────────────────────────────── */
.vdivider { height: .8rem; }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
#  SIDEBAR
# ==============================================================================

render_sidebar()

# ==============================================================================
#  PAGE HERO
# ==============================================================================

st.markdown("""
<div class="page-hero">
  <div class="page-hero-icon">🤖</div>
  <div class="page-hero-title">Unified AI Risk Dashboard</div>
  <div class="page-hero-sub">
    Consolidated financial risk assessment generated from all three trained models.
    Individual predictions are weighted by model validation performance and
    combined into a single interpretable risk score with an AI recommendation.
  </div>
  <span class="pill pill-violet">⚖️ Weighted Ensemble</span>
  <span class="pill pill-blue">📊 3 Models Combined</span>
  <span class="pill pill-green">🎯 Risk Classification</span>
  <span class="pill pill-amber">💡 Recommendation Engine</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#  FETCH SESSION STATE
# ==============================================================================

dataset2_risk   = st.session_state.get("dataset2_risk", None)
dataset3_risk   = st.session_state.get("dataset3_risk", None)
dataset5_risk   = st.session_state.get("dataset5_risk", None)
dataset5_stress = st.session_state.get("stress_index",  0.0)

# ==============================================================================
#  VALIDATION — prompt user to run missing predictions
# ==============================================================================

missing = []
if dataset2_risk is None:
    missing.append(("💳", "Credit Card Risk",    "pages/1_Credit_Card_Risk.py",    "open_cc_dash"))
if dataset3_risk is None:
    missing.append(("🏦", "Personal Loan Risk",  "pages/2_Personal_Loan_Risk.py",  "open_pl_dash"))
if dataset5_risk is None:
    missing.append(("📈", "Financial Stability", "pages/3_Financial_Stability.py", "open_fs_dash"))

if missing:
    st.markdown("""
    <div class="warn-card">
      <div class="warn-title">⚠️ Predictions Required Before Dashboard Can Load</div>
      <div class="warn-body">
        Please run predictions on the following modules first. The Unified Dashboard
        aggregates risk scores from all three models into a consolidated assessment.
      </div>
    </div>
    """, unsafe_allow_html=True)

    for icon, label, page, key in missing:
        col_a, col_b = st.columns([4, 1], gap="medium")
        with col_a:
            st.markdown(f"""
            <div style="padding:10px 0; font-size:.92rem; color:#1A1F36; font-family:'Inter',sans-serif;">
              {icon} &nbsp; <strong>{label}</strong>
              <span style="color:#9CA3AF;"> — prediction not yet run</span>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            if st.button(f"Go →", key=key, use_container_width=True):
                st.switch_page(page)

    st.stop()

# ==============================================================================
#  WEIGHTED ENSEMBLE SCORE
# ==============================================================================

WEIGHTS = {"dataset2": 0.25, "dataset3": 0.35, "dataset5": 0.40}

contrib2 = WEIGHTS["dataset2"] * dataset2_risk
contrib3 = WEIGHTS["dataset3"] * dataset3_risk
contrib5 = WEIGHTS["dataset5"] * dataset5_risk

overall_risk = contrib2 + contrib3 + contrib5

# Persist for use elsewhere in the app (e.g. future export/report pages)
st.session_state["overall_risk"] = overall_risk

# Risk classification
if overall_risk < 30:
    risk_level  = "LOW RISK"
    color       = "#16A34A"
    rc_color    = "#16A34A"
    rc_bg       = "#F0FDF4"
    rc_border   = "#BBF7D0"
    level_style = "background:#DCFCE7; color:#16A34A;"
elif overall_risk < 60:
    risk_level  = "MEDIUM RISK"
    color       = "#D97706"
    rc_color    = "#D97706"
    rc_bg       = "#FFFBEB"
    rc_border   = "#FDE68A"
    level_style = "background:#FEF9C3; color:#D97706;"
else:
    risk_level  = "HIGH RISK"
    color       = "#DC2626"
    rc_color    = "#DC2626"
    rc_bg       = "#FEF2F2"
    rc_border   = "#FECACA"
    level_style = "background:#FEE2E2; color:#DC2626;"

# ==============================================================================
#  COMBINED STRESS INDEX
#  Blends the overall ensemble risk with Dataset 5's raw financial_stress
#  signal, instead of showing Dataset 5's stress in isolation. Clamped to
#  [0, 100] since the raw stress term can exceed 100 on its own for very
#  high DTI / interest-rate combinations.
# ==============================================================================

stress_index = min(100, max(0, overall_risk * 0.7 + dataset5_stress * 3))

# ==============================================================================
#  MODEL CONTRIBUTION CARDS
# ==============================================================================

st.markdown('<div class="sec-label">Individual Model Risk Scores</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4, gap="medium")

model_cards = [
    ("💳", "Credit Card Risk",         dataset2_risk, 25, contrib2, "#00B4D8", m1),
    ("🏦", "Personal Loan Risk",       dataset3_risk, 35, contrib3, "#16A34A", m2),
    ("📈", "Financial Stability Risk",  dataset5_risk, 40, contrib5, "#D97706", m3),
]

for icon, title, risk_val, weight, contrib, mc_color, col in model_cards:
    r_color = "#16A34A" if risk_val < 20 else ("#D97706" if risk_val < 50 else "#DC2626")
    with col:
        st.markdown(f"""
        <div class="model-card" style="--mc-color:{mc_color};">
          <div class="model-card-icon">{icon}</div>
          <div class="model-card-title">{title}</div>
          <div class="model-card-risk" style="color:{r_color};">{risk_val:.2f}%</div>
          <div class="model-card-weight">Weight: {weight}%</div>
          <div class="model-card-contrib">Contribution: {contrib:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="overall-card">
      <div class="overall-eyebrow">Overall Risk</div>
      <div class="overall-val" style="color:{color};">{overall_risk:.2f}%</div>
      <div class="overall-lbl">Weighted Ensemble Score</div>
      <div class="overall-level" style="{level_style}">{risk_level}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  GAUGES
# ==============================================================================

st.markdown('<div class="sec-label">Risk &amp; Stress Gauges</div>', unsafe_allow_html=True)

g1, g2 = st.columns(2, gap="medium")

gauge_layout = dict(
    height=300,
    margin=dict(t=50, b=10, l=20, r=20),
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif"),
)

gauge_steps = [
    {"range": [0,  30], "color": "#DCFCE7"},
    {"range": [30, 60], "color": "#FEF9C3"},
    {"range": [60, 100], "color": "#FEE2E2"},
]

with g1:
    fig_overall = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=overall_risk,
        number={"suffix": "%", "font": {"size": 34, "color": color}},
        title={"text": "<b>Unified Risk Score</b>", "font": {"size": 15, "color": "#1A1F36"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#9CA3AF"},
            "bar":  {"color": color, "thickness": 0.28},
            "bgcolor": "white",
            "bordercolor": "#E5E7EB",
            "steps": gauge_steps,
            "threshold": {
                "line": {"color": color, "width": 3},
                "thickness": 0.75,
                "value": overall_risk,
            },
        },
    ))
    fig_overall.update_layout(**gauge_layout)
    st.plotly_chart(fig_overall, use_container_width=True)

with g2:
    stress_color = "#16A34A" if stress_index < 30 else ("#D97706" if stress_index < 60 else "#DC2626")
    fig_stress = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stress_index,
        number={"suffix": " /100", "font": {"size": 34, "color": stress_color}},
        title={"text": "<b>Combined Stress Index</b><br><span style='font-size:.82em;color:#6B7280'>Ensemble risk + Dataset 5 stress</span>",
               "font": {"size": 15, "color": "#1A1F36"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#9CA3AF"},
            "bar":  {"color": stress_color, "thickness": 0.28},
            "bgcolor": "white",
            "bordercolor": "#E5E7EB",
            "steps": gauge_steps,
        },
    ))
    fig_stress.update_layout(**gauge_layout)
    st.plotly_chart(fig_stress, use_container_width=True)

# Risk banner
st.markdown(f"""
<div class="risk-banner" style="background:{color};">
  {risk_level}
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  CONTRIBUTION BREAKDOWN CHART  +  SUMMARY TABLE
# ==============================================================================

left, right = st.columns([3, 2], gap="large")

with left:
    st.markdown('<div class="sec-label">Risk Contribution Breakdown</div>', unsafe_allow_html=True)

    bar_colors  = ["#00B4D8", "#16A34A", "#D97706"]
    labels      = ["Dataset 2<br>(Credit Card)", "Dataset 3<br>(Personal Loan)", "Dataset 5<br>(Financial Stability)"]
    contribs    = [contrib2, contrib3, contrib5]
    raw_risks   = [dataset2_risk, dataset3_risk, dataset5_risk]

    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        x=labels,
        y=contribs,
        marker_color=bar_colors,
        marker_line_width=0,
        text=[f"{c:.2f}%<br><span style='font-size:.8em;'>(raw {r:.1f}%)</span>"
              for c, r in zip(contribs, raw_risks)],
        textposition="outside",
        width=0.45,
        hovertemplate="<b>%{x}</b><br>Contribution: %{y:.2f}%<extra></extra>",
    ))
    bar_fig.update_layout(
        height=350,
        title=dict(
            text="Weighted Contribution to Overall Risk Score",
            font=dict(size=14, color="#1A1F36", family="Inter, sans-serif"),
        ),
        yaxis_title="Contribution (%)",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=55, b=20, l=10, r=10),
        showlegend=False,
        yaxis=dict(
            range=[0, max(contribs) * 1.35],
            gridcolor="#F1F5F9",
            zerolinecolor="#E5E7EB",
        ),
        xaxis=dict(tickfont=dict(size=12, family="Inter, sans-serif")),
        font=dict(family="Inter, sans-serif"),
    )
    st.plotly_chart(bar_fig, use_container_width=True)

with right:
    st.markdown('<div class="sec-label">Risk Summary Table</div>', unsafe_allow_html=True)

    rows = [
        ("Dataset 2", "💳 Credit Card Risk",    f"{dataset2_risk:.2f}%", "25%", f"{contrib2:.2f}%"),
        ("Dataset 3", "🏦 Personal Loan Risk",  f"{dataset3_risk:.2f}%", "35%", f"{contrib3:.2f}%"),
        ("Dataset 5", "📈 Financial Stability", f"{dataset5_risk:.2f}%", "40%", f"{contrib5:.2f}%"),
        ("—",         "⚖️ Overall Risk",         f"{overall_risk:.2f}%",  "100%", f"{overall_risk:.2f}%"),
    ]

    row_htmls = []
    for i, (ds, mod, risk_v, wt, contrib_v) in enumerate(rows):
        is_total = (i == 3)
        bg  = "#F5F3FF" if is_total else ("white" if i % 2 == 0 else "#F8F9FB")
        fw  = "800"     if is_total else "500"
        sep = "border-top:2px solid #DDD6FE;" if is_total else "border-bottom:1px solid #F1F5F9;"
        row_htmls.append(f"""<tr style="background:{bg}; {sep}">
          <td style="padding:9px 6px; font-weight:700; color:#00B4D8;">{ds}</td>
          <td style="padding:9px 6px; color:#1A1F36; font-weight:{fw};">{mod}</td>
          <td style="padding:9px 6px; text-align:right; font-weight:{fw}; color:#1A1F36;">{risk_v}</td>
          <td style="padding:9px 6px; text-align:right; color:#9CA3AF;">{wt}</td>
          <td style="padding:9px 6px; text-align:right; font-weight:{fw}; color:#7C3AED;">{contrib_v}</td>
        </tr>""")

    # IMPORTANT: the wrapping div, the table, and the closing div must all be
    # passed to ONE st.markdown() call. Streamlit sanitizes/parses each
    # markdown call independently, so splitting an open tag and its closing
    # tag across separate calls breaks HTML rendering and the raw markup is
    # shown as text instead of rendering.
    table_html = f"""<div class="content-card"><table style="width:100%; border-collapse:collapse; font-size:.82rem; font-family:'Inter',sans-serif;">
      <thead>
        <tr style="border-bottom:2px solid #E5E7EB;">
          <th style="text-align:left; padding:8px 6px; color:#6B7280; font-weight:700; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;">Dataset</th>
          <th style="text-align:left; padding:8px 6px; color:#6B7280; font-weight:700; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;">Module</th>
          <th style="text-align:right; padding:8px 6px; color:#6B7280; font-weight:700; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;">Risk</th>
          <th style="text-align:right; padding:8px 6px; color:#6B7280; font-weight:700; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;">Wt.</th>
          <th style="text-align:right; padding:8px 6px; color:#6B7280; font-weight:700; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em;">Contrib.</th>
        </tr>
      </thead>
      <tbody>{"".join(row_htmls)}</tbody>
    </table></div>"""

    st.markdown(table_html, unsafe_allow_html=True)

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  RISK DISTRIBUTION PIE CHART
# ==============================================================================

st.markdown('<div class="sec-label">Risk Distribution</div>', unsafe_allow_html=True)

pie_fig = go.Figure(
    data=[
        go.Pie(
            labels=["Credit Card", "Personal Loan", "Financial Stability"],
            values=[contrib2, contrib3, contrib5],
            hole=0.5,
            marker=dict(colors=["#00B4D8", "#16A34A", "#D97706"], line=dict(color="#FFFFFF", width=2)),
            textinfo="label+percent",
            textfont=dict(family="Inter, sans-serif", size=12),
        )
    ]
)
pie_fig.update_layout(
    title=dict(
        text="Share of Overall Risk by Model",
        font=dict(size=14, color="#1A1F36", family="Inter, sans-serif"),
    ),
    height=380,
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=55, b=20, l=10, r=10),
    font=dict(family="Inter, sans-serif"),
    legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
    annotations=[dict(
        text=f"{overall_risk:.1f}%<br><span style='font-size:.7em;color:#6B7280'>Overall</span>",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=20, family="Inter, sans-serif", color=color),
    )],
)
st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  AI RECOMMENDATION
# ==============================================================================

st.markdown('<div class="sec-label">AI Recommendation</div>', unsafe_allow_html=True)

if overall_risk < 30:
    rec_title = "✅ Eligible for Approval — Low Consolidated Risk"
    rec_body  = ("All three models report low-to-moderate risk. The applicant demonstrates "
                 "good repayment capability across credit card behaviour, personal loan profile, "
                 "and overall financial stability. The weighted ensemble score supports loan approval.")
elif overall_risk < 60:
    rec_title = "⚠️ Moderate Consolidated Risk — Proceed with Caution"
    rec_body  = ("Moderate risk detected across the ensemble. One or more models have flagged "
                 "elevated default indicators. Additional verification of income stability, "
                 "existing liabilities, and repayment history is strongly recommended before approval.")
else:
    rec_title = "❌ High Consolidated Risk — Approval Not Recommended"
    rec_body  = ("The weighted ensemble of all three models indicates high default probability. "
                 "Financial stress, poor credit signals, and elevated loan-to-income ratios across "
                 "multiple datasets suggest significant repayment risk. Loan approval is not "
                 "recommended without a comprehensive financial review and restructuring plan.")

st.markdown(f"""
<div class="rec-card" style="--rc-color:{rc_color}; --rc-bg:{rc_bg}; --rc-border:{rc_border};">
  <div class="rec-title">{rec_title}</div>
  {rec_body}
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  FINAL RISK SCORE CARD
# ==============================================================================

st.markdown('<div class="sec-label">Final Risk Score</div>', unsafe_allow_html=True)

mcol1, mcol2, mcol3 = st.columns([1, 1, 1], gap="medium")
with mcol2:
    st.metric(
        "Unified Risk Score",
        f"{overall_risk:.2f}%",
        delta=risk_level,
        delta_color="off",
    )

st.markdown("<div class='vdivider'></div>", unsafe_allow_html=True)

# ==============================================================================
#  DOWNLOAD REPORT
# ==============================================================================

st.markdown('<div class="sec-label">Export</div>', unsafe_allow_html=True)

report = f"""RunaRakshaka — Unified AI Risk Report
=======================================

Individual Model Scores
------------------------
Dataset 2 (Credit Card Risk)     : {dataset2_risk:.2f}%   | Weight 25% | Contribution {contrib2:.2f}%
Dataset 3 (Personal Loan Risk)   : {dataset3_risk:.2f}%   | Weight 35% | Contribution {contrib3:.2f}%
Dataset 5 (Financial Stability)  : {dataset5_risk:.2f}%   | Weight 40% | Contribution {contrib5:.2f}%

Combined Stress Index            : {stress_index:.2f} / 100

Overall Weighted Risk Score
----------------------------
{overall_risk:.2f}%

Risk Level
----------
{risk_level}

Recommendation
---------------
{rec_title}
{rec_body}

-----------------------------------------------------
Generated by RunaRakshaka Unified AI Risk Engine
Weighted Ensemble of 3 ML Models
PES University MCA 2025-26
"""

st.download_button(
    "📄 Download Report",
    report,
    file_name="runarakshaka_risk_report.txt",
    mime="text/plain",
    use_container_width=False,
)

# ==============================================================================
#  FOOTER
# ==============================================================================

st.markdown("""
<div class="page-footer">
  <b>RunaRakshaka</b> &nbsp;·&nbsp; Unified AI Risk Engine &nbsp;·&nbsp;
  Weighted Ensemble of 3 ML Models &nbsp;·&nbsp; PES University MCA 2025–26
</div>
""", unsafe_allow_html=True)