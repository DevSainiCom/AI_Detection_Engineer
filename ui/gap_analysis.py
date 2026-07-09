"""
Gap Analysis (Coverage Analysis) — Enterprise Redesign
"""

import streamlit as st

from ui.components import *
from ui.design_system import (
    enterprise_card, metric_row, info_banner, checklist, section_divider,
)
from backend.services.gap_analysis_service import gap_analysis_service


def render():

    page_setup(
        title="Coverage Analysis",
        subtitle="Assess current detection coverage and identify monitoring gaps against the application threat profile.",
        eyebrow="Customer Onboarding · Step 3 of 12",
        agent_name="Gap Analysis Agent",
        agent_desc=(
            "Compares the application threat model and architecture against existing detection "
            "coverage to identify monitoring blind spots and prioritise remediation. "
            "<strong>Current POC:</strong> Rule-based analysis against the Application Analysis output. "
            "<strong>Future:</strong> AI-powered comparison against live Sentinel analytics rules, "
            "MITRE ATT&CK Navigator, and the customer detection library."
        ),
    )

    if st.session_state.application is None:
        info_banner(
            "Complete <strong>Application Analysis</strong> before running coverage analysis.",
            variant="warning",
        )
        nav_buttons()
        return

    # Auto-generate once
    if st.session_state.gap_analysis is None:
        with st.spinner("Analysing detection coverage..."):
            st.session_state.gap_analysis = gap_analysis_service.analyze(
                st.session_state.application
            )

    result = st.session_state.gap_analysis

    info_banner(
        "Coverage analysis completed. Gaps identified and detection roadmap generated.",
        variant="success",
    )

    # ── Metrics ──
    maturity_color = {
        "Advanced": "green", "Intermediate": "blue",
        "Basic": "amber", "Minimal": "red",
    }.get(result.security_maturity, "blue")

    metric_row([
        {"value": f"{result.coverage_score}%", "label": "Detection Coverage", "color": "blue"},
        {"value": result.security_maturity, "label": "Security Maturity", "color": maturity_color},
        {"value": str(len(result.missing_detection_use_cases)), "label": "Coverage Gaps", "color": "red"},
        {"value": str(len(result.missing_log_sources)), "label": "Missing Log Sources", "color": "amber"},
    ])

    section_divider()

    # ── Executive Summary ──
    st.markdown("##### Executive Summary")
    enterprise_card("Assessment", result.executive_summary, "accent-left")

    section_divider()

    # ── Gap Detail ──
    st.markdown("##### Detection Gaps")

    g1, g2 = st.columns(2)
    with g1:
        st.markdown("###### Missing Detection Coverage")
        checklist(result.missing_detection_use_cases, done=False)
    with g2:
        st.markdown("###### Missing Log Sources")
        checklist(result.missing_log_sources, done=False)

    section_divider()

    # ── MITRE Gaps ──
    st.markdown("##### Missing MITRE ATT&CK Coverage")
    enterprise_card(
        "Undetected Techniques",
        " · ".join(result.missing_mitre_coverage),
        "accent-danger",
    )

    section_divider()

    # ── Security Observations ──
    st.markdown("##### Security Observations")
    enterprise_card(
        "Findings",
        " · ".join(result.security_observations),
        "accent-warning",
    )

    section_divider()

    # ── Roadmap ──
    st.markdown("##### Detection Development Roadmap")

    for idx, item in enumerate(result.detection_roadmap, start=1):
        enterprise_card(f"Priority {idx}", item, "accent-left")

    section_divider()

    # ── Recommendations ──
    st.markdown("##### SOC Recommendations")
    checklist(result.recommendations)

    section_divider()

    # ── Knowledge ──
    st.markdown("##### Knowledge Generated")
    info_banner(
        "The following coverage intelligence has been added to the security knowledge base.",
        variant="success",
    )
    checklist(result.knowledge_generated)

    section_divider()

    info_banner(result.future_ai_usage, variant="context")

    developer_view(result.model_dump())
    nav_buttons()
