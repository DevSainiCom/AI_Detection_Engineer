"""
Shared UI Components — v2
==========================
"""

import streamlit as st
from ui.design_system import (
    inject_css,
    enterprise_banner,
    page_header as _page_header,
    arch_context,
    enterprise_card,
    metric_card,
    metric_row,
    info_banner,
    checklist,
    section_divider,
)


def page_setup(title, subtitle="", eyebrow="", agent_name="", agent_desc=""):
    """
    Full page initialization:
    1. Inject CSS  2. Banner  3. Header  4. Optional agent context
    """
    inject_css()
    enterprise_banner()
    _page_header(title, subtitle, eyebrow)
    if agent_name:
        arch_context(agent_name, agent_desc)


def page_header(title, subtitle=""):
    """Backward-compatible — auto-injects CSS + banner."""
    inject_css()
    enterprise_banner()
    _page_header(title, subtitle)


# ── Navigation ──

def next_button():
    return st.button("Continue ▶", use_container_width=True, type="primary")


def previous_button():
    return st.button("◀ Previous", use_container_width=True)


def nav_buttons():
    section_divider()
    c1, c2 = st.columns(2)
    with c1:
        if previous_button():
            if st.session_state.step > 0:
                st.session_state.step -= 1
                st.rerun()
    with c2:
        if next_button():
            st.session_state.step += 1
            st.rerun()


# ── Convenience ──

def section(title):
    section_divider()
    st.subheader(title)


def success(text):
    st.success(text)


def warning(text):
    st.warning(text)


def developer_view(data, label="Developer View"):
    with st.expander(f"🔧 {label}"):
        st.json(data)
