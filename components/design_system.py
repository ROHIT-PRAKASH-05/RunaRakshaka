# ==============================================================================
#  RunaRakshaka  —  Design System  (components/design_system.py)
#  Single source of truth for risk tiers, colour tokens, and component helpers.
#
#  shared_css.py re-exports RISK_TIERS and get_risk_tier from here so that
#  any existing page importing from shared_css keeps working without changes.
# ==============================================================================

# ---------------------------------------------------------------------------
#  RISK TIERS
#  Centralised thresholds and colour tokens for every risk classification
#  rendered anywhere in the app (banners, cards, pills, recommendations).
# ---------------------------------------------------------------------------

RISK_TIERS: dict[str, dict] = {
    "low": {
        "color":      "#16A34A",
        "bg":         "#F0FDF4",
        "border":     "#BBF7D0",
        "pill_bg":    "#DCFCE7",
        "label":      "LOW RISK",
        "emoji":      "✅",
        "gradient":   "linear-gradient(135deg, #16A34A 0%, #15803D 100%)",
    },
    "medium": {
        "color":      "#D97706",
        "bg":         "#FFFBEB",
        "border":     "#FDE68A",
        "pill_bg":    "#FEF9C3",
        "label":      "MEDIUM RISK",
        "emoji":      "⚠️",
        "gradient":   "linear-gradient(135deg, #D97706 0%, #B45309 100%)",
    },
    "high": {
        "color":      "#E11D48",
        "bg":         "#FFF1F3",
        "border":     "#FECDD3",
        "pill_bg":    "#FFE4E9",
        "label":      "HIGH RISK",
        "emoji":      "🚨",
        "gradient":   "linear-gradient(135deg, #E11D48 0%, #BE123C 100%)",
    },
}


def get_risk_tier(
    score: float,
    low_max: float = 30,
    medium_max: float = 60,
) -> dict:
    """Return the RISK_TIERS entry that matches a 0-100 risk score.

    Args:
        score:       Risk percentage, 0–100.
        low_max:     Upper bound (exclusive) for the LOW tier.
        medium_max:  Upper bound (exclusive) for the MEDIUM tier.

    Using a single function here means Credit Card, Personal Loan,
    Financial Stability, and Unified Dashboard all classify risk
    identically instead of each page re-implementing its own if/elif
    chain that could quietly diverge over time.
    """
    if score < low_max:
        return RISK_TIERS["low"]
    if score < medium_max:
        return RISK_TIERS["medium"]
    return RISK_TIERS["high"]


# ---------------------------------------------------------------------------
#  COLOUR PALETTE  (mirrors :root tokens in shared_css.py)
#  Import these in Python code that needs hex values directly —
#  e.g. Plotly/Altair charts, dynamic inline-style strings.
# ---------------------------------------------------------------------------

COLORS = {
    # brand
    "primary":        "#00B4D8",
    "primary_dark":   "#0096B7",
    "primary_light":  "#E0F7FB",
    "primary_glow":   "rgba(0,180,216,.16)",
    # neutrals
    "ink":            "#0F172A",
    "ink_soft":       "#1E293B",
    "muted":          "#64748B",
    "muted_light":    "#94A3B8",
    "border":         "#E6E9F0",
    "border_soft":    "#EEF1F6",
    "bg":             "#FAFBFD",
    "bg_soft":        "#F4F6FA",
    "card":           "#FFFFFF",
    # status
    "green":          "#16A34A",
    "amber":          "#D97706",
    "red":            "#E11D48",
    "violet":         "#7C3AED",
}


# ---------------------------------------------------------------------------
#  COMPONENT HELPERS
#  Thin Python functions that return HTML strings so page files stay clean.
# ---------------------------------------------------------------------------

def risk_banner_html(label: str, color: str, gradient: str) -> str:
    """Full-width coloured banner for a risk verdict."""
    return (
        f'<div class="risk-banner" style="background:{gradient};">'
        f'{label}</div>'
    )


def rec_card_html(title: str, body: str, color: str, bg: str) -> str:
    """Recommendation card with left accent bar."""
    return (
        f'<div class="rec-card" style="--rc-color:{color}; --rc-bg:{bg};">'
        f'<div class="rec-title">{title}</div>'
        f'{body}</div>'
    )


def model_card_html(
    icon: str,
    title: str,
    risk_pct: float,
    weight_label: str,
    contrib: str,
    color: str,
) -> str:
    """Per-model risk card used on the Unified Dashboard."""
    return (
        f'<div class="model-card" style="--mc-color:{color};">'
        f'<div class="model-card-icon">{icon}</div>'
        f'<div class="model-card-title">{title}</div>'
        f'<div class="model-card-risk">{risk_pct:.1f}%</div>'
        f'<div class="model-card-weight">{weight_label}</div>'
        f'<div class="model-card-contrib">{contrib}</div>'
        f'</div>'
    )


def perf_metric_html(value: str, label: str, color: str) -> str:
    """Small performance-metric card (Model Performance page)."""
    return (
        f'<div class="perf-metric" style="--pm-color:{color};">'
        f'<div class="perf-metric-val">{value}</div>'
        f'<div class="perf-metric-lbl">{label}</div>'
        f'</div>'
    )


def info_row_html(key: str, value: str) -> str:
    """Single key/value row for a stat table."""
    return (
        f'<div class="info-row">'
        f'<span class="info-key">{key}</span>'
        f'<span class="info-value">{value}</span>'
        f'</div>'
    )


def derived_chip_html(value: str, label: str) -> str:
    """Blue derived-metric chip."""
    return (
        f'<div class="derived-chip">'
        f'<div class="derived-chip-val">{value}</div>'
        f'<div class="derived-chip-lbl">{label}</div>'
        f'</div>'
    )


def sec_label_html(text: str) -> str:
    """Section heading label with trailing rule."""
    return f'<div class="sec-label">{text}</div>'


def warn_card_html(title: str, body: str) -> str:
    """Amber warning / 'predictions required' card."""
    return (
        f'<div class="warn-card">'
        f'<div class="warn-title">{title}</div>'
        f'<div class="warn-body">{body}</div>'
        f'</div>'
    )