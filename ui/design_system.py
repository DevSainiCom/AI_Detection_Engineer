"""
Enterprise Design System — v2
==============================
Premium styling for AI Detection Engineering Platform.
Designed to feel like Microsoft Defender / Datadog dashboard.
"""

import streamlit as st

# ──────────────────────────────────────────────────────────────
# Platform Constants
# ──────────────────────────────────────────────────────────────

PLATFORM_NAME = "AI Detection Engineering Platform"
PLATFORM_VERSION = "v0.3"
PLATFORM_TARGET = "Microsoft Sentinel"
PLATFORM_CLASSIFICATION = "Proof of Concept"
PREPARED_FOR = "PMI"
COMPANY = "EPAM"

# ──────────────────────────────────────────────────────────────
# Color Palette
# ──────────────────────────────────────────────────────────────
# Navy:    #0f1628
# Deep:    #161d33
# Accent:  #4f6ef7  (electric blue)
# Success: #10b981
# Warning: #f59e0b
# Danger:  #ef4444
# Surface: #f8f9fc
# Border:  #e2e5f1

ENTERPRISE_CSS = """
<style>
    /* ═══════════════════════════════════════════════════════════
       GLOBAL RESET & TYPOGRAPHY
       ═══════════════════════════════════════════════════════════ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .main {
        background: #f8f9fc;
    }

    /* ═══════════════════════════════════════════════════════════
       TOP BANNER — Gradient hero strip
       ═══════════════════════════════════════════════════════════ */
    .enterprise-banner {
        background: linear-gradient(135deg, #0f1628 0%, #1a2342 40%, #243056 70%, #1a2342 100%);
        color: white;
        padding: 1.1rem 1.8rem;
        border-radius: 14px;
        margin-bottom: 1.6rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 8px 32px rgba(15, 22, 40, 0.25);
        position: relative;
        overflow: hidden;
    }

    .enterprise-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(79,110,247,0.15) 0%, transparent 70%);
        pointer-events: none;
    }

    .enterprise-banner .banner-left {
        position: relative;
        z-index: 1;
    }

    .enterprise-banner .banner-left h2 {
        margin: 0;
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: #ffffff;
    }

    .enterprise-banner .banner-tags {
        display: flex;
        gap: 0.5rem;
        margin-top: 0.5rem;
        flex-wrap: wrap;
    }

    .enterprise-banner .tag {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 0.2rem 0.65rem;
        border-radius: 6px;
        font-size: 0.68rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: rgba(255,255,255,0.7);
        backdrop-filter: blur(4px);
    }

    .enterprise-banner .tag.tag-accent {
        background: rgba(79,110,247,0.2);
        border-color: rgba(79,110,247,0.3);
        color: #93b0ff;
    }

    .enterprise-banner .banner-right {
        text-align: right;
        position: relative;
        z-index: 1;
    }

    .enterprise-banner .banner-right .prepared-for {
        font-size: 0.7rem;
        color: rgba(255,255,255,0.45);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
    }

    .enterprise-banner .banner-right .client-name {
        font-size: 1.3rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.01em;
        margin-top: 0.1rem;
    }

    /* ═══════════════════════════════════════════════════════════
       PAGE HEADER
       ═══════════════════════════════════════════════════════════ */
    .page-header-wrap {
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #e2e5f1;
    }

    .page-header-wrap .page-eyebrow {
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #4f6ef7;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .page-header-wrap h1 {
        font-size: 1.65rem;
        font-weight: 800;
        color: #0f1628;
        margin: 0;
        letter-spacing: -0.03em;
        line-height: 1.2;
    }

    .page-header-wrap .page-subtitle {
        font-size: 0.92rem;
        color: #6b7494;
        margin-top: 0.35rem;
        line-height: 1.5;
        font-weight: 400;
    }

    /* ═══════════════════════════════════════════════════════════
       ENTERPRISE CARDS
       ═══════════════════════════════════════════════════════════ */
    .e-card {
        background: #ffffff;
        border: 1px solid #e2e5f1;
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 1px 4px rgba(15, 22, 40, 0.04);
        transition: box-shadow 0.2s ease;
    }

    .e-card:hover {
        box-shadow: 0 4px 16px rgba(15, 22, 40, 0.08);
    }

    .e-card .e-card-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #8b92a8;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .e-card .e-card-body {
        font-size: 0.93rem;
        color: #1f2640;
        line-height: 1.65;
    }

    /* Card with left accent border */
    .e-card.accent-left {
        border-left: 4px solid #4f6ef7;
    }

    .e-card.accent-success {
        border-left: 4px solid #10b981;
    }

    .e-card.accent-warning {
        border-left: 4px solid #f59e0b;
    }

    .e-card.accent-danger {
        border-left: 4px solid #ef4444;
    }

    /* ═══════════════════════════════════════════════════════════
       METRIC CARDS
       ═══════════════════════════════════════════════════════════ */
    .m-card {
        background: #ffffff;
        border: 1px solid #e2e5f1;
        border-radius: 12px;
        padding: 1.3rem 1.2rem;
        text-align: center;
        box-shadow: 0 1px 4px rgba(15, 22, 40, 0.04);
        position: relative;
        overflow: hidden;
    }

    .m-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
    }

    .m-card.m-blue::after { background: #4f6ef7; }
    .m-card.m-green::after { background: #10b981; }
    .m-card.m-amber::after { background: #f59e0b; }
    .m-card.m-red::after { background: #ef4444; }
    .m-card.m-purple::after { background: #8b5cf6; }

    .m-card .m-value {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1;
    }

    .m-card.m-blue .m-value { color: #4f6ef7; }
    .m-card.m-green .m-value { color: #10b981; }
    .m-card.m-amber .m-value { color: #f59e0b; }
    .m-card.m-red .m-value { color: #ef4444; }
    .m-card.m-purple .m-value { color: #8b5cf6; }

    .m-card .m-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #8b92a8;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    /* ═══════════════════════════════════════════════════════════
       INFO BANNERS
       ═══════════════════════════════════════════════════════════ */
    .i-banner {
        border-radius: 10px;
        padding: 1rem 1.3rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        line-height: 1.6;
        display: flex;
        gap: 0.8rem;
        align-items: flex-start;
    }

    .i-banner .i-icon {
        font-size: 1.1rem;
        flex-shrink: 0;
        margin-top: 0.1rem;
    }

    .i-banner.i-info {
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        color: #3730a3;
    }

    .i-banner.i-success {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
    }

    .i-banner.i-warning {
        background: #fffbeb;
        border: 1px solid #fde68a;
        color: #92400e;
    }

    .i-banner.i-context {
        background: #f8f9fc;
        border: 1px solid #e2e5f1;
        color: #4b5563;
        font-size: 0.85rem;
    }

    /* ═══════════════════════════════════════════════════════════
       STEP INDICATOR (horizontal)
       ═══════════════════════════════════════════════════════════ */
    .step-indicator {
        display: flex;
        align-items: center;
        gap: 0;
        margin-bottom: 1.5rem;
        padding: 0.8rem 1rem;
        background: white;
        border-radius: 12px;
        border: 1px solid #e2e5f1;
        overflow-x: auto;
    }

    .step-dot {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.7rem;
        font-weight: 700;
        flex-shrink: 0;
    }

    .step-dot.done { background: #10b981; color: white; }
    .step-dot.active { background: #4f6ef7; color: white; box-shadow: 0 0 0 3px rgba(79,110,247,0.25); }
    .step-dot.pending { background: #e2e5f1; color: #8b92a8; }

    .step-line {
        flex: 1;
        height: 2px;
        min-width: 12px;
        margin: 0 2px;
    }

    .step-line.done { background: #10b981; }
    .step-line.pending { background: #e2e5f1; }

    /* ═══════════════════════════════════════════════════════════
       SIDEBAR — Premium dark sidebar
       ═══════════════════════════════════════════════════════════ */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1628 0%, #131b30 100%);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        padding-top: 1rem;
    }

    section[data-testid="stSidebar"] .stMarkdown p {
        color: rgba(255,255,255,0.65) !important;
        font-size: 0.82rem;
    }

    section[data-testid="stSidebar"] .stMarkdown strong {
        color: rgba(255,255,255,0.9) !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.06) !important;
    }

    section[data-testid="stSidebar"] .stCaption p {
        color: rgba(255,255,255,0.35) !important;
        font-size: 0.72rem !important;
    }

    /* Sidebar progress bars */
    section[data-testid="stSidebar"] .stProgress > div > div {
        background-color: rgba(255,255,255,0.08) !important;
        border-radius: 4px;
    }

    section[data-testid="stSidebar"] .stProgress > div > div > div {
        background: linear-gradient(90deg, #4f6ef7, #6d8cff) !important;
        border-radius: 4px;
    }

    /* ═══════════════════════════════════════════════════════════
       BUTTON OVERRIDES
       ═══════════════════════════════════════════════════════════ */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4f6ef7, #3d5bd9) !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        letter-spacing: 0.01em !important;
        padding: 0.6rem 1.5rem !important;
        box-shadow: 0 4px 14px rgba(79,110,247,0.3) !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(79,110,247,0.4) !important;
        transform: translateY(-1px);
    }

    .stButton > button[kind="secondary"],
    .stButton > button:not([kind="primary"]) {
        border-radius: 10px !important;
        font-weight: 500 !important;
        border: 1px solid #e2e5f1 !important;
    }

    /* ═══════════════════════════════════════════════════════════
       FORM INPUTS
       ═══════════════════════════════════════════════════════════ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        border-radius: 10px !important;
        border-color: #e2e5f1 !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #4f6ef7 !important;
        box-shadow: 0 0 0 3px rgba(79,110,247,0.1) !important;
    }

    /* ═══════════════════════════════════════════════════════════
       EXPANDER
       ═══════════════════════════════════════════════════════════ */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        color: #4b5563 !important;
    }

    /* ═══════════════════════════════════════════════════════════
       DIVIDER
       ═══════════════════════════════════════════════════════════ */
    .section-divider {
        border: none;
        border-top: 1px solid #e2e5f1;
        margin: 1.8rem 0;
    }

    /* ═══════════════════════════════════════════════════════════
       AGENT ARCHITECTURE CONTEXT BOX
       ═══════════════════════════════════════════════════════════ */
    .arch-context {
        background: linear-gradient(135deg, #f8f9fc, #eef2ff);
        border: 1px solid #e2e5f1;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
    }

    .arch-context .arch-title {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #4f6ef7;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .arch-context .arch-body {
        font-size: 0.88rem;
        color: #4b5563;
        line-height: 1.6;
    }

    /* ═══════════════════════════════════════════════════════════
       TABLE STYLING
       ═══════════════════════════════════════════════════════════ */
    .stTable table {
        border-radius: 10px;
        overflow: hidden;
    }

    /* ═══════════════════════════════════════════════════════════
       CHECKLIST ITEMS
       ═══════════════════════════════════════════════════════════ */
    .checklist-item {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.45rem 0;
        font-size: 0.9rem;
        color: #1f2640;
    }

    .checklist-item .check-icon {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.65rem;
        flex-shrink: 0;
    }

    .checklist-item .check-icon.done {
        background: #ecfdf5;
        color: #10b981;
    }

    .checklist-item .check-icon.pending {
        background: #fef3c7;
        color: #f59e0b;
    }
</style>
"""


# ──────────────────────────────────────────────────────────────
# Inject CSS (call once per page)
# ──────────────────────────────────────────────────────────────

def inject_css():
    st.markdown(ENTERPRISE_CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Enterprise Banner
# ──────────────────────────────────────────────────────────────

def enterprise_banner():
    st.markdown(f"""
    <div class="enterprise-banner">
        <div class="banner-left">
            <h2>🛡️ {PLATFORM_NAME}</h2>
            <div class="banner-tags">
                <span class="tag">{COMPANY}</span>
                <span class="tag tag-accent">{PLATFORM_TARGET}</span>
                <span class="tag">Azure OpenAI</span>
                <span class="tag">{PLATFORM_VERSION}</span>
            </div>
        </div>
        <div class="banner-right">
            <div class="prepared-for">Prepared for</div>
            <div class="client-name">{PREPARED_FOR}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Page Header
# ──────────────────────────────────────────────────────────────

def page_header(title, subtitle="", eyebrow=""):
    eyebrow_html = f'<div class="page-eyebrow">{eyebrow}</div>' if eyebrow else ""
    sub_html = f'<div class="page-subtitle">{subtitle}</div>' if subtitle else ""
    st.markdown(f"""
    <div class="page-header-wrap">
        {eyebrow_html}
        <h1>{title}</h1>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Architecture Context Box
# ──────────────────────────────────────────────────────────────

def arch_context(agent_name, description):
    """Show which agent powers this page and what it does."""
    st.markdown(f"""
    <div class="arch-context">
        <div class="arch-title">🤖 {agent_name}</div>
        <div class="arch-body">{description}</div>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Cards
# ──────────────────────────────────────────────────────────────

def enterprise_card(title, content, accent=""):
    """accent: '', 'accent-left', 'accent-success', 'accent-warning', 'accent-danger'"""
    st.markdown(f"""
    <div class="e-card {accent}">
        <div class="e-card-label">{title}</div>
        <div class="e-card-body">{content}</div>
    </div>
    """, unsafe_allow_html=True)


def metric_card(value, label, color="blue"):
    """color: blue, green, amber, red, purple"""
    st.markdown(f"""
    <div class="m-card m-{color}">
        <div class="m-value">{value}</div>
        <div class="m-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def metric_row(metrics):
    """metrics: list of dicts {value, label, color}"""
    cols = st.columns(len(metrics))
    for col, m in zip(cols, metrics):
        with col:
            metric_card(m["value"], m["label"], m.get("color", "blue"))


# ──────────────────────────────────────────────────────────────
# Info Banners
# ──────────────────────────────────────────────────────────────

_BANNER_ICONS = {
    "info": "💡",
    "success": "✅",
    "warning": "⚠️",
    "context": "📋",
}

def info_banner(text, variant="info"):
    icon = _BANNER_ICONS.get(variant, "💡")
    st.markdown(f"""
    <div class="i-banner i-{variant}">
        <span class="i-icon">{icon}</span>
        <div>{text}</div>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Checklist
# ──────────────────────────────────────────────────────────────

def checklist(items, done=True):
    """Render a styled checklist. items: list of strings."""
    icon_class = "done" if done else "pending"
    icon = "✓" if done else "○"
    for item in items:
        st.markdown(f"""
        <div class="checklist-item">
            <span class="check-icon {icon_class}">{icon}</span>
            <span>{item}</span>
        </div>
        """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# Section Divider
# ──────────────────────────────────────────────────────────────

def section_divider():
    st.markdown('<hr class="section-divider"/>', unsafe_allow_html=True)
