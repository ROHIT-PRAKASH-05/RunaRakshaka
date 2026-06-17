# ==============================================================================
#  RunaRakshaka  —  Shared CSS  (design tokens + global styles)
#  Import and call inject_shared_css() on every page, before rendering content.
# ==============================================================================

import streamlit as st
from components.design_system import RISK_TIERS, get_risk_tier  # noqa: F401

SHARED_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

/* ==========================================================================
   DESIGN TOKENS
   ========================================================================== */
:root {
    --font-display: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif;
    --font-body:    'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

    --primary:       #00B4D8;
    --primary-dark:  #0096B7;
    --primary-light: #E0F7FB;
    --primary-glow:  rgba(0, 180, 216, .16);

    --accent:      var(--primary);
    --accent-dark: var(--primary-dark);

    --ink:         #0F172A;
    --ink-soft:    #1E293B;
    --muted:       #64748B;
    --muted-light: #94A3B8;
    --border:      #E6E9F0;
    --border-soft: #EEF1F6;
    --bg:          #FAFBFD;
    --bg-soft:     #F4F6FA;
    --card:        #FFFFFF;

    --green:        #16A34A;  --green-bg:     #F0FDF4;  --green-border:  #BBF7D0;  --green-pill:  #DCFCE7;
    --amber:        #D97706;  --amber-bg:     #FFFBEB;  --amber-border:  #FDE68A;  --amber-pill:  #FEF3C7;
    --red:          #E11D48;  --red-bg:       #FFF1F3;  --red-border:    #FECDD3;  --red-pill:    #FFE4E9;
    --violet:       #7C3AED;  --violet-bg:    #F5F3FF;  --violet-border: #DDD6FE;  --violet-pill: #EDE9FE;

    --shadow-xs: 0 1px 2px rgba(15,23,42,.04);
    --shadow-sm: 0 2px 10px rgba(15,23,42,.06);
    --shadow-md: 0 10px 28px rgba(15,23,42,.08);
    --shadow-lg: 0 24px 48px rgba(15,23,42,.12);

    --radius-sm: 10px;
    --radius-md: 16px;
    --radius-lg: 20px;
    --radius-xl: 26px;
    --ease: cubic-bezier(.22,1,.36,1);
}

/* ==========================================================================
   GLOBAL SHELL
   ========================================================================== */
.stApp { background: var(--bg); }
html, body, [class*="css"] { font-family: var(--font-body); }
h1,h2,h3,h4,h5 { font-family: var(--font-display); color: var(--ink); letter-spacing: -.01em; }

[data-testid="stSidebarNav"] { display: none !important; }
#MainMenu  { visibility: hidden; }
footer     { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

.block-container { padding-top: 1.6rem; max-width: 1180px; }

::-webkit-scrollbar       { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted-light); }

/* ==========================================================================
   SIDEBAR NAV LINK TEXT — force dark colour everywhere (fixes mobile invisible text)
   ========================================================================== */
[data-testid="stPageLink"] > a {
    color:         var(--ink)       !important;
    font-size:     .87rem           !important;
    padding:       8px 10px         !important;
    border-radius: var(--radius-sm) !important;
    font-weight:   600              !important;
    transition:    background .15s var(--ease) !important;
}
[data-testid="stPageLink"] > a:hover {
    background: var(--bg-soft)      !important;
    color:      var(--primary-dark) !important;
}

/* ==========================================================================
   MOBILE SIDEBAR — toggle button always visible + sidebar overlay
   ========================================================================== */
[data-testid="collapsedControl"] {
    display:       flex      !important;
    visibility:    visible   !important;
    opacity:       1         !important;
    position:      fixed     !important;
    top:           .6rem     !important;
    left:          .6rem     !important;
    z-index:       9999      !important;
    background:    #fff      !important;
    border-radius: 8px       !important;
    box-shadow:    0 2px 8px rgba(0,0,0,.15) !important;
    padding:       .3rem     !important;
}

@media (max-width: 768px) {

    /* Sidebar: fixed full-height overlay */
    section[data-testid="stSidebar"] {
        position:   fixed    !important;
        top:        0        !important;
        left:       0        !important;
        height:     100vh    !important;
        width:      82vw     !important;
        min-width:  260px    !important;
        max-width:  320px    !important;
        z-index:    1000     !important;
        box-shadow: 4px 0 24px rgba(0,0,0,.18) !important;
        overflow-y: auto     !important;
    }

    /* Ensure sidebar background is solid white — no bleed-through */
    section[data-testid="stSidebar"] > div {
        background: #fff !important;
        height:     100% !important;
    }

    /* Nav link text explicitly dark on mobile */
    [data-testid="stPageLink"] > a {
        color:       #0F172A   !important;
        font-size:   .9rem     !important;
        padding:     10px 12px !important;
        font-weight: 600       !important;
        display:     block     !important;
    }

    /* Main content padding */
    .block-container {
        padding-top:   1rem  !important;
        padding-left:  .8rem !important;
        padding-right: .8rem !important;
    }

    /* Stack all columns vertically */
    [data-testid="column"] {
        width:     100% !important;
        flex:      1 1 100% !important;
        min-width: 100% !important;
    }

    /* Hero text */
    .hero-title      { font-size: 1.55rem !important; }
    .hero-sub        { font-size: .88rem  !important; }
    .page-hero-title { font-size: 1.25rem !important; }
    .page-hero-sub   { font-size: .84rem  !important; }

    /* Buttons full width */
    .stButton > button { width: 100% !important; }

    /* Cap chart height */
    .js-plotly-plot { max-height: 220px !important; }

    /* Card spacing */
    .mod-card, .stat-card, .content-card, .res-card {
        margin-bottom: .7rem !important;
    }

    /* Risk banner */
    .risk-banner {
        font-size:     .85rem !important;
        padding:       .7rem .9rem !important;
        letter-spacing:.02em !important;
    }

    /* Pills */
    .pill { font-size: .68rem !important; padding: 4px 10px !important; }

    /* Derived chips */
    .derived-chip-val { font-size: 1rem !important; }
}

/* ==========================================================================
   TABLET  (769px – 1024px)
   ========================================================================== */
@media (min-width: 769px) and (max-width: 1024px) {
    .block-container {
        padding-left:  1.5rem !important;
        padding-right: 1.5rem !important;
    }
}

/* ==========================================================================
   NATIVE WIDGET POLISH
   ========================================================================== */
.stButton > button {
    border-radius: var(--radius-sm) !important;
    font-weight:   700              !important;
    font-family:   var(--font-body) !important;
    border:        1px solid var(--border) !important;
    color:         var(--ink)       !important;
    transition:    all .18s var(--ease);
}
.stButton > button:hover {
    border-color: var(--primary)      !important;
    color:        var(--primary-dark) !important;
    box-shadow:   var(--shadow-sm);
    transform:    translateY(-1px);
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    border:     none !important;
    color:      #fff !important;
    box-shadow: var(--shadow-sm);
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 14px 30px var(--primary-glow);
    transform:  translateY(-2px);
}

.stTextInput input, .stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div,
.stDateInput input {
    border-radius: var(--radius-sm) !important;
    border-color:  var(--border)    !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: var(--primary)                !important;
    box-shadow:   0 0 0 3px var(--primary-glow) !important;
}
.stSlider [data-baseweb="slider"] [role="slider"] {
    background-color: var(--primary)                !important;
    box-shadow:       0 0 0 4px var(--primary-glow) !important;
}
.stTabs [data-baseweb="tab-list"] { gap: 6px; }
.stTabs [data-baseweb="tab"]      { border-radius: var(--radius-sm) var(--radius-sm) 0 0; font-weight: 700; }
[data-testid="stMetric"] {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-md);
    padding:       .9rem 1rem;
    box-shadow:    var(--shadow-xs);
}

/* ==========================================================================
   SECTION LABEL
   ========================================================================== */
.sec-label {
    font-size:      .72rem;
    font-weight:    800;
    color:          var(--primary);
    text-transform: uppercase;
    letter-spacing: .14em;
    margin:         .2rem 0 .9rem;
    display:        flex;
    align-items:    center;
    gap:            .6rem;
    font-family:    var(--font-display);
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

/* ==========================================================================
   HOME HERO
   ========================================================================== */
.hero {
    text-align: center;
    padding:    2.4rem 1rem 1.8rem;
    position:   relative;
}
.hero::before {
    content:        '';
    position:       absolute;
    top:            -40px;
    left:           50%;
    width:          520px;
    height:         320px;
    transform:      translateX(-50%);
    border-radius:  50%;
    background:     radial-gradient(closest-side, var(--primary-glow), transparent 70%);
    z-index:        0;
    pointer-events: none;
}
.hero-title {
    font-family:    var(--font-display);
    font-size:      2.6rem;
    font-weight:    800;
    color:          var(--ink);
    margin:         .3rem 0;
    letter-spacing: -.02em;
    position:       relative;
    z-index:        1;
}
.hero-sub {
    font-size:     1.04rem;
    color:         var(--muted);
    margin-bottom: 1.1rem;
    position:      relative;
    z-index:       1;
}

/* ==========================================================================
   SUB-PAGE HERO
   ========================================================================== */
.page-hero {
    background:    linear-gradient(135deg, #FFFFFF 0%, var(--bg-soft) 100%);
    border:        1px solid var(--border);
    border-radius: var(--radius-xl);
    padding:       1.9rem 2.1rem 1.7rem;
    margin-bottom: 1.7rem;
    border-left:   4px solid var(--hero-accent, var(--primary));
    box-shadow:    var(--shadow-xs);
}
.page-hero-icon  { font-size: 2.1rem; margin-bottom: .45rem; }
.page-hero-title { font-family: var(--font-display); font-size: 1.75rem; font-weight: 800; color: var(--ink); margin-bottom: .25rem; }
.page-hero-sub   { font-size: .93rem; color: var(--muted); margin-bottom: .8rem; line-height: 1.65; max-width: 72ch; }

/* ==========================================================================
   PILLS
   ========================================================================== */
.pill {
    display:        inline-block;
    padding:        5px 14px;
    border-radius:  999px;
    font-size:      .72rem;
    font-weight:    700;
    margin:         2px;
    letter-spacing: .02em;
    border:         1px solid transparent;
}
.pill-blue   { color: var(--primary-dark); background: var(--primary-light); }
.pill-green  { color: #15803D;             background: var(--green-pill); }
.pill-amber  { color: #B45309;             background: var(--amber-pill); }
.pill-violet { color: #6D28D9;             background: var(--violet-pill); }
.pill-red    { color: #BE123C;             background: var(--red-pill); }

/* ==========================================================================
   CARDS
   ========================================================================== */
.content-card {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-lg);
    padding:       1.5rem 1.6rem;
    box-shadow:    var(--shadow-xs);
    margin-bottom: 1rem;
    overflow-x:    auto;
}
.input-card {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-lg);
    padding:       1.35rem 1.45rem;
    box-shadow:    var(--shadow-sm);
    margin-bottom: 1.2rem;
}
.input-card-label {
    font-size:      .68rem;
    font-weight:    800;
    color:          var(--primary);
    text-transform: uppercase;
    letter-spacing: .12em;
    margin-bottom:  .6rem;
    font-family:    var(--font-display);
}

.res-card, .stat-card {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-lg);
    padding:       1.15rem .95rem;
    text-align:    center;
    box-shadow:    var(--shadow-xs);
    transition:    box-shadow .18s var(--ease), transform .18s var(--ease);
}
.res-card:hover, .stat-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
.res-val, .stat-val { font-family: var(--font-display); font-size: 1.7rem; font-weight: 800; line-height: 1; }
.res-lbl, .stat-lbl { font-size: .78rem; color: var(--muted); margin-top: 5px; font-weight: 600; }

.model-card {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-lg);
    padding:       1.15rem 1rem 1.05rem;
    text-align:    center;
    box-shadow:    var(--shadow-xs);
    border-top:    3px solid var(--mc-color, var(--primary));
    height:        100%;
    transition:    box-shadow .2s var(--ease), transform .2s var(--ease);
}
.model-card:hover   { box-shadow: var(--shadow-md); transform: translateY(-2px); }
.model-card-icon    { font-size: 1.4rem; margin-bottom: .35rem; }
.model-card-title   { font-size: .76rem; font-weight: 800; color: var(--ink); margin-bottom: .5rem; text-transform: uppercase; letter-spacing: .05em; font-family: var(--font-display); }
.model-card-risk    { font-family: var(--font-display); font-size: 1.85rem; font-weight: 800; color: var(--mc-color, var(--primary)); line-height: 1; }
.model-card-weight  { font-size: .7rem; color: var(--muted-light); font-weight: 600; margin-top: 2px; }
.model-card-contrib { font-size: .78rem; font-weight: 700; color: var(--ink); margin-top: 5px; background: var(--bg-soft); border-radius: 7px; padding: .22rem .55rem; display: inline-block; }

.overall-card {
    background:    linear-gradient(135deg, var(--violet-bg) 0%, #EEEAFD 100%);
    border:        1px solid var(--violet-border);
    border-radius: var(--radius-lg);
    padding:       1.35rem 1.2rem 1.25rem;
    text-align:    center;
    box-shadow:    0 8px 26px rgba(124,58,237,.12);
    height:        100%;
}
.overall-eyebrow { font-size: .65rem; font-weight: 800; color: var(--violet); text-transform: uppercase; letter-spacing: .12em; margin-bottom: .5rem; font-family: var(--font-display); }
.overall-val     { font-family: var(--font-display); font-size: 2.5rem; font-weight: 800; line-height: 1; }
.overall-lbl     { font-size: .8rem; color: var(--muted); font-weight: 600; margin-top: 5px; }
.overall-level   { margin-top: .75rem; font-size: .82rem; font-weight: 800; padding: .32rem .85rem; border-radius: 99px; display: inline-block; }

.mod-card {
    background:    var(--card);
    border:        1px solid var(--border);
    border-radius: var(--radius-xl);
    padding:       1.55rem 1.45rem;
    height:        100%;
    box-shadow:    var(--shadow-xs);
    border-top:    3px solid var(--mod-accent, var(--primary));
    transition:    box-shadow .2s var(--ease), transform .2s var(--ease);
}
.mod-icon  { width: 48px; height: 48px; border-radius: 13px; display: flex; align-items: center; justify-content: center; font-size: 1.45rem; margin-bottom: .85rem; background: var(--mod-accent-soft, var(--primary-light)); }
.mod-title { font-family: var(--font-display); font-size: 1.1rem; font-weight: 800; color: var(--ink); margin-bottom: .3rem; }
.mod-desc  { font-size: .86rem; color: var(--muted); line-height: 1.6; margin-bottom: .85rem; }
.chip-row  { display: flex; flex-wrap: wrap; gap: 6px; }
.chip      { font-size: .72rem; font-weight: 600; color: var(--ink-soft); background: var(--bg-soft); border: 1px solid var(--border-soft); border-radius: 8px; padding: 3px 9px; }
.mod-cta   { display: flex; align-items: center; gap: 4px; font-size: .82rem; font-weight: 700; color: var(--primary-dark); margin-top: .95rem; padding-top: .75rem; border-top: 1px solid var(--border-soft); }

/* whole-card click target */
div[data-testid="stColumn"]:has(div[data-testid="stButton"]) { position: relative; }
div[data-testid="stColumn"]:has(div[data-testid="stButton"]):hover .mod-card { box-shadow: var(--shadow-lg); transform: translateY(-4px); border-color: var(--mod-accent, var(--primary)); }
div[data-testid="stColumn"]:has(div[data-testid="stButton"]) div[data-testid="stElementContainer"]:has(div[data-testid="stButton"]) { position: static; }
div[data-testid="stColumn"]:has(div[data-testid="stButton"]) div[data-testid="stButton"] { position: absolute; inset: 0; margin: 0; z-index: 5; }
div[data-testid="stColumn"]:has(div[data-testid="stButton"]) div[data-testid="stButton"] button { width: 100%; height: 100%; padding: 0; background: transparent !important; border: none !important; color: transparent !important; box-shadow: none !important; cursor: pointer; }
div[data-testid="stColumn"]:has(div[data-testid="stButton"]) div[data-testid="stButton"] button:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: var(--radius-xl); }

/* ==========================================================================
   RISK / WARN / REC / DERIVED
   ========================================================================== */
.risk-banner { border-radius: var(--radius-lg); padding: 1.05rem 2rem; text-align: center; color: #fff; font-size: 1.15rem; font-weight: 800; letter-spacing: .04em; margin: 1rem 0; box-shadow: var(--shadow-md); }

.warn-card  { background: var(--amber-bg); border: 1px solid var(--amber-border); border-left: 4px solid var(--amber); border-radius: var(--radius-lg); padding: 1.2rem 1.5rem; margin-bottom: 1rem; }
.warn-title { font-weight: 800; color: var(--amber); font-size: .95rem; margin-bottom: .5rem; font-family: var(--font-display); }
.warn-body  { font-size: .86rem; color: var(--ink); line-height: 1.7; }

.rec-card  { border-radius: var(--radius-lg); padding: 1.15rem 1.4rem; border-left: 4px solid var(--rc-color, var(--primary)); background: var(--rc-bg, var(--bg-soft)); font-size: .88rem; color: var(--ink); line-height: 1.7; }
.rec-title { font-weight: 800; font-size: .92rem; margin-bottom: .4rem; color: var(--rc-color, var(--primary)); font-family: var(--font-display); }

.derived-chip     { background: var(--primary-light); border: 1px solid #BAE6FD; border-radius: var(--radius-sm); padding: .75rem 1rem; text-align: center; }
.derived-chip-val { font-family: var(--font-display); font-size: 1.25rem; font-weight: 800; color: var(--primary-dark); }
.derived-chip-lbl { font-size: .74rem; color: var(--muted); font-weight: 600; }

.info-row         { display: flex; justify-content: space-between; align-items: center; padding: 7px 0; border-bottom: 1px solid var(--border); font-size: .85rem; }
.info-row:last-child { border-bottom: none; }
.info-key         { color: var(--muted); font-weight: 600; }
.info-value       { color: var(--ink);   font-weight: 700; }

.perf-metric     { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.05rem .9rem; text-align: center; box-shadow: var(--shadow-xs); border-top: 3px solid var(--pm-color, var(--primary)); }
.perf-metric-val { font-family: var(--font-display); font-size: 1.5rem; font-weight: 800; color: var(--pm-color, var(--primary)); }
.perf-metric-lbl { font-size: .76rem; color: var(--muted); margin-top: 3px; font-weight: 600; }

/* ==========================================================================
   TECH BADGE / PIPELINE
   ========================================================================== */
.tech-badge       { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 9px 6px; text-align: center; font-size: .78rem; font-weight: 700; transition: box-shadow .15s var(--ease), transform .15s var(--ease); }
.tech-badge:hover { box-shadow: var(--shadow-sm); transform: translateY(-1px); }

.step-row  { display: flex; align-items: flex-start; gap: 12px; padding: 7px 0; }
.step-num  { width: 24px; height: 24px; border-radius: 50%; background: var(--primary); color: #fff; font-size: .68rem; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.step-text { font-size: .85rem; color: var(--ink); padding-top: 2px; font-weight: 500; }

/* ==========================================================================
   SIDEBAR
   ========================================================================== */
section[data-testid="stSidebar"] { background: var(--card); border-right: 1px solid var(--border); }
section[data-testid="stSidebar"] .block-container { padding-top: 1rem; }

.sidebar-brand       { text-align: center; padding: 1.1rem 0 1.3rem; border-bottom: 1px solid var(--border); margin-bottom: .6rem; }
.sidebar-brand-icon  { width: 52px; height: 52px; margin: 0 auto .55rem; border-radius: 14px; background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 8px 20px var(--primary-glow); }
.sidebar-brand-title { font-family: var(--font-display); font-size: 1.15rem; font-weight: 800; color: var(--ink); letter-spacing: -.01em; }
.sidebar-brand-sub   { font-size: .73rem; color: var(--muted); margin-top: .2rem; letter-spacing: .03em; }

.sidebar-section-label { font-size: .68rem; font-weight: 800; color: var(--muted); text-transform: uppercase; letter-spacing: .1em; margin: .8rem 0 .6rem; font-family: var(--font-display); }

.status-row   { display: flex; align-items: center; gap: .55rem; margin-bottom: .4rem; }
.status-dot   { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; }
.status-label { font-size: .82rem; font-weight: 600; }
.status-track { height: 6px; border-radius: 99px; background: var(--bg-soft); overflow: hidden; margin: .5rem 0 .7rem; }
.status-fill  { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--primary), var(--primary-dark)); transition: width .3s var(--ease); }

.dev-card { background: var(--bg-soft); border: 1px solid var(--border); border-radius: var(--radius-md); padding: .85rem 1rem; }
.dev-name { font-size: .88rem; font-weight: 800; color: var(--ink); }
.dev-usn  { font-size: .76rem; color: var(--primary-dark); font-weight: 700; font-family: monospace; }
.dev-prog { font-size: .72rem; color: var(--muted); margin-top: .2rem; }

/* ==========================================================================
   FOOTERS
   ========================================================================== */
.footer      { text-align: center; color: var(--muted); font-size: .82rem; padding: 1.7rem 0 .6rem; }
.footer b    { color: var(--ink); }
.page-footer { text-align: center; color: var(--muted); font-size: .8rem; padding: 1.5rem 0 .4rem; border-top: 1px solid var(--border); margin-top: 2rem; }
.page-footer b { color: var(--ink); }

/* ==========================================================================
   UTILITY SPACERS
   ========================================================================== */
.vspace-sm { height: .4rem; }
.vspace-md { height: .8rem; }
.vspace-lg { height: 1.4rem; }

</style>
"""


def inject_shared_css():
    st.markdown(SHARED_CSS, unsafe_allow_html=True)