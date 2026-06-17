# ==============================================================================
#  RunaRakshaka  —  Sidebar  (components/sidebar.py)
# ==============================================================================

import streamlit as st


def render_sidebar() -> None:
    """Render the full application sidebar: brand, nav, prediction status, dev card."""

    # Suppress Streamlit's auto-generated multipage nav so only our hand-built
    # nav is visible. The rule also lives in shared_css.py; both are kept so
    # the sidebar stays clean even when a page calls render_sidebar() before
    # inject_shared_css() (e.g. pages that import in a different order).
    st.markdown("""
    <style>
      [data-testid="stSidebarNav"] { display: none !important; }
      section[data-testid="stSidebar"] .block-container { padding-top: .8rem; }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        # ── Brand ─────────────────────────────────────────────────────────────
        st.markdown("""
        <div style="
            text-align: center;
            padding: 1.1rem 0 1.3rem;
            border-bottom: 1px solid var(--border, #E6E9F0);
            margin-bottom: .5rem;
        ">
          <div style="
              width: 52px; height: 52px; margin: 0 auto .55rem;
              border-radius: 14px;
              background: linear-gradient(135deg, #00B4D8 0%, #0096B7 100%);
              display: flex; align-items: center; justify-content: center;
              font-size: 1.5rem;
              box-shadow: 0 8px 20px rgba(0,180,216,.22);
          ">🛡️</div>
          <div style="
              font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
              font-size: 1.12rem; font-weight: 800;
              color: var(--ink, #0F172A);
              letter-spacing: -.01em;
          ">RunaRakshaka</div>
          <div style="font-size: .73rem; color: var(--muted, #64748B); margin-top: .2rem; letter-spacing: .03em;">
            AI Debt Risk Prediction
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Navigation ─────────────────────────────────────────────────────────
        # NOTE: paths must match the filenames in /pages exactly.
        nav_items = [
            ("app.py",                            "🏠", "Home"),
            ("pages/1_Credit_Card_Risk.py",       "💳", "Credit Card Risk"),
            ("pages/2_Personal_Loan_Risk.py",     "🏦", "Personal Loan Risk"),
            ("pages/3_Financial_Stability.py",    "📈", "Financial Stability"),
            ("pages/4_Unified_Risk_Dashboard.py", "🎯", "Unified Dashboard"),
            ("pages/5_Model_Performance.py",      "📊", "Model Performance"),
        ]

        try:
            current_path = st.context.url
        except Exception:
            current_path = ""

        for path, icon, label in nav_items:
            is_active = path.split("/")[-1].replace(".py", "") in current_path
            display_label = f"**{icon}  {label}**" if is_active else f"{icon}  {label}"
            st.page_link(path, label=display_label)

        st.markdown("<div style='height:.3rem'></div>", unsafe_allow_html=True)
        st.divider()

        # ── Prediction status ─────────────────────────────────────────────────
        d2 = st.session_state.get("dataset2_risk")
        d3 = st.session_state.get("dataset3_risk")
        d5 = st.session_state.get("dataset5_risk")

        st.markdown("""
        <div style="
            font-size: .68rem; font-weight: 800; color: var(--muted, #64748B);
            text-transform: uppercase; letter-spacing: .1em; margin-bottom: .65rem;
            font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
        ">Prediction Status</div>
        """, unsafe_allow_html=True)

        predictions = [
            (d2, "💳", "Credit Card Risk"),
            (d3, "🏦", "Personal Loan Risk"),
            (d5, "📈", "Financial Stability"),
        ]
        rows_html = ""
        done_count = sum(1 for v, _, _ in predictions if v is not None)

        for value, icon, label in predictions:
            done = value is not None
            dot_color = "#16A34A" if done else "#CBD5E1"
            text_color = "#0F172A" if done else "#94A3B8"
            check = "✓" if done else "·"
            rows_html += (
                f'<div style="display:flex; align-items:center; gap:.55rem; margin-bottom:.38rem;">'
                f'<div style="width:9px; height:9px; border-radius:50%; background:{dot_color}; flex-shrink:0;"></div>'
                f'<span style="font-size:.81rem; font-weight:600; color:{text_color};">'
                f'{icon} {label}</span>'
                f'<span style="margin-left:auto; font-size:.75rem; font-weight:700; color:{dot_color};">{check}</span>'
                f'</div>'
            )

        # Progress bar
        fill_pct = int(done_count / 3 * 100)
        rows_html += (
            f'<div style="height:5px; border-radius:99px; background:#EEF1F6; margin:.6rem 0 .8rem; overflow:hidden;">'
            f'<div style="height:100%; width:{fill_pct}%; border-radius:99px; '
            f'background:linear-gradient(90deg,#00B4D8,#0096B7); transition:width .3s;"></div>'
            f'</div>'
        )

        st.markdown(rows_html, unsafe_allow_html=True)

        if done_count == 3:
            if st.button("🔄 Reset All Predictions", use_container_width=True):
                stale_keys = [
                    k for k in st.session_state.keys()
                    if k.startswith(("dataset", "stress_", "risk_", "model_"))
                ]
                for key in stale_keys:
                    st.session_state.pop(key, None)
                st.rerun()

        st.divider()

        # ── Developer card ─────────────────────────────────────────────────────
        st.markdown("""
        <div style="
            background: var(--bg-soft, #F4F6FA);
            border: 1px solid var(--border, #E6E9F0);
            border-radius: 12px;
            padding: .85rem 1rem;
        ">
          <div style="
              font-size: .85rem; font-weight: 800;
              color: var(--ink, #0F172A);
              font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
          ">Rohit P</div>
          <div style="
              font-size: .76rem; color: #0096B7; font-weight: 700;
              margin-top: .15rem; font-family: monospace;
          ">PES1PG25CA325</div>
          <div style="font-size: .71rem; color: var(--muted, #64748B); margin-top: .2rem;">
            MCA · PES University · 2025–26
          </div>
        </div>
        """, unsafe_allow_html=True)