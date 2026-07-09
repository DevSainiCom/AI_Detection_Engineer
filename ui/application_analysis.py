"""
Application Analysis — Enterprise Redesign
=============================================
"""

import streamlit as st

from ui.components import *
from ui.design_system import (
    enterprise_card,
    metric_row,
    info_banner,
    checklist,
    section_divider,
)

from backend.services.application_analysis_service import (
    application_analysis_service,
)


def render():

    page_setup(
        title="Application Analysis",
        subtitle="Understand the application architecture, security posture, and telemetry requirements.",
        eyebrow="Customer Onboarding · Step 2 of 12",
        agent_name="Application Analysis Agent",
        agent_desc=(
            "Extracts application metadata, identifies critical assets, trust boundaries, "
            "and recommends detection opportunities based on the technology stack. "
            "<strong>Current POC:</strong> Rule-based analysis. "
            "<strong>Future:</strong> AI-powered analysis of architecture diagrams, "
            "Terraform templates, Kubernetes manifests, and API specifications."
        ),
    )

    # ── Input Form ──

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("##### Application Profile")

        app_name = st.text_input(
            "Application Name",
            value=st.session_state.threat_model.get("ApplicationName", ""),
        )

        app_type = st.selectbox(
            "Application Type",
            ["Web", "API", "Desktop", "Cloud Native", "Mobile"],
        )

        authentication = st.selectbox(
            "Authentication",
            ["Entra ID", "Active Directory", "OAuth", "Local"],
        )

    with col2:
        st.markdown("##### Environment")

        cloud = st.selectbox(
            "Hosting Platform",
            ["Azure", "AWS", "GCP", "On-Prem"],
        )

        classification = st.selectbox(
            "Data Classification",
            ["Public", "Internal", "Confidential", "Restricted"],
        )

        stack = st.text_input(
            "Technology Stack",
            placeholder=".NET, Java, SQL Server, AKS, React...",
        )

    section_divider()

    if st.button("🔍 Analyze Application", use_container_width=True, type="primary"):
        with st.spinner("Analysing application architecture..."):
            result = application_analysis_service.analyze(
                application_name=app_name,
                application_type=app_type,
                business_function=st.session_state.threat_model.get("BusinessFunction", ""),
                authentication=authentication,
                cloud_provider=cloud,
                technology_stack=[x.strip() for x in stack.split(",") if x.strip()],
                business_criticality=st.session_state.threat_model.get("Criticality", "Medium"),
                data_classification=classification,
            )
            st.session_state.application = result

    # ── Results ──

    if st.session_state.application is None:
        return

    result = st.session_state.application

    info_banner(
        f"Application analysis for <strong>{result.application_name}</strong> completed successfully.",
        variant="success",
    )

    # ── Metrics ──
    rating_color = {"High": "red", "Medium": "amber", "Low": "green"}.get(result.security_rating, "blue")

    metric_row([
        {"value": result.security_rating, "label": "Security Rating", "color": rating_color},
        {"value": str(len(result.critical_assets)), "label": "Critical Assets", "color": "purple"},
        {"value": str(len(result.recommended_log_sources)), "label": "Log Sources", "color": "blue"},
        {"value": str(len(result.recommended_detection_use_cases)), "label": "Detection Opportunities", "color": "green"},
    ])

    section_divider()

    # ── Executive Summary ──
    st.markdown("##### Executive Summary")
    enterprise_card("Assessment", result.executive_summary, "accent-left")

    section_divider()

    # ── Application Overview ──
    st.markdown("##### Application Overview")

    c1, c2 = st.columns(2)
    with c1:
        enterprise_card("Application", result.application_name, "accent-left")
        enterprise_card("Type", result.application_type, "accent-left")
        enterprise_card("Authentication", result.authentication, "accent-left")
        enterprise_card("Hosting", result.cloud_provider, "accent-left")
    with c2:
        enterprise_card("Business Function", result.business_function, "accent-left")
        enterprise_card("Criticality", result.business_criticality, "accent-left")
        enterprise_card("Data Classification", result.data_classification, "accent-left")
        enterprise_card("Technology Stack", " · ".join(result.technology_stack), "accent-left")

    section_divider()

    # ── Architecture ──
    st.markdown("##### Architecture Understanding")
    enterprise_card("Architecture Summary", result.architecture_summary, "accent-left")

    a1, a2 = st.columns(2)
    with a1:
        st.markdown("###### Critical Assets")
        checklist(result.critical_assets)
    with a2:
        st.markdown("###### Trust Boundaries")
        checklist(result.trust_boundaries)

    section_divider()

    # ── Security Observations ──
    st.markdown("##### Security Observations")
    enterprise_card(
        "Findings",
        " · ".join(result.security_observations),
        "accent-warning",
    )

    section_divider()

    # ── Telemetry & Detection ──
    st.markdown("##### Recommended Telemetry & Detection Opportunities")

    t1, t2 = st.columns(2)
    with t1:
        st.markdown("###### Expected Log Sources")
        checklist(result.recommended_log_sources)
    with t2:
        st.markdown("###### Detection Use Cases")
        checklist(result.recommended_detection_use_cases)

    section_divider()

    # ── Knowledge Generated ──
    st.markdown("##### Knowledge Generated")

    info_banner(
        "The following information has been added to the customer security knowledge base.",
        variant="success",
    )

    checklist(result.knowledge_generated)

    section_divider()

    # ── Impact ──
    st.markdown("##### Detection Engineering Impact")
    info_banner(result.future_ai_usage, variant="context")

    # ── Developer View ──
    developer_view(result.model_dump())

    # ── Navigation ──
    nav_buttons()
