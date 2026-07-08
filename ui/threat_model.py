"""
Threat Model — Enterprise Redesign
====================================
"""

import time
import streamlit as st

from ui.components import *
from ui.design_system import (
    enterprise_card,
    metric_row,
    info_banner,
    checklist,
    section_divider,
    arch_context,
)


def render():

    page_setup(
        title="Threat Model",
        subtitle="Describe the application's threat landscape and business risk to establish the security context for detection engineering.",
        eyebrow="Customer Onboarding · Step 1 of 12",
        agent_name="Threat Modeling Agent",
        agent_desc=(
            "This agent analyses threat models, architecture diagrams, and security documents "
            "to establish the security context for the application. "
            "<strong>Current POC:</strong> Rule-based assessment. "
            "<strong>Future:</strong> AI-powered analysis of uploaded documents, "
            "Microsoft Threat Modeling Tool exports, and architecture diagrams."
        ),
    )

    # ──────────────────────────────────────────────────────────
    # Session
    # ──────────────────────────────────────────────────────────

    if "threat_model_completed" not in st.session_state:
        st.session_state.threat_model_completed = False

    # ──────────────────────────────────────────────────────────
    # Input Form
    # ──────────────────────────────────────────────────────────

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:

        st.markdown("##### Application Details")

        model_app = st.text_input(
            "Application Name",
            placeholder="e.g. Online Banking Portal",
        )

        model_biz = st.text_input(
            "Business Function",
            placeholder="e.g. Retail Banking",
        )

        model_actor = st.selectbox(
            "Threat Actor",
            ["Cyber Criminal", "APT", "Insider", "Hacktivist"],
            index=None,
            placeholder="Select threat actor",
        )

    with col_right:

        st.markdown("##### Risk Assessment")

        model_crit = st.selectbox(
            "Business Criticality",
            ["Low", "Medium", "High", "Critical"],
            index=None,
            placeholder="Select criticality",
        )

        model_attack = st.text_area(
            "Attack Description",
            height=162,
            placeholder=(
                "Describe the primary threats...\n\n"
                "Example:\n"
                "The application is Internet-facing and processes "
                "customer financial transactions. Primary concerns "
                "include password spraying, credential theft, "
                "account takeover, and privilege escalation."
            ),
        )

    model = {
        "ApplicationName": model_app,
        "BusinessFunction": model_biz,
        "ThreatActor": model_actor,
        "Criticality": model_crit,
        "AttackDescription": model_attack,
    }

    st.session_state.threat_model = model

    section_divider()

    # ──────────────────────────────────────────────────────────
    # Generate Button
    # ──────────────────────────────────────────────────────────

    if not st.session_state.threat_model_completed:
        if st.button(
            "🚀 Generate Threat Assessment",
            use_container_width=True,
            type="primary",
        ):
            with st.spinner("Analysing threat model..."):
                time.sleep(2)
            st.session_state.threat_model_completed = True
            st.rerun()
        return  # Don't render results until generated

    # ──────────────────────────────────────────────────────────
    # Results
    # ──────────────────────────────────────────────────────────

    risk = model["Criticality"] or "Medium"
    application = model["ApplicationName"] or "the application"
    business = model["BusinessFunction"] or "the business service"
    actor = model["ThreatActor"] or "identified threat actors"

    # Risk color
    risk_color = {"Critical": "red", "High": "amber", "Medium": "amber", "Low": "green"}.get(risk, "blue")

    info_banner(
        f"Threat assessment for <strong>{application}</strong> completed successfully. "
        f"The application supports <strong>{business}</strong> and is primarily exposed to "
        f"<strong>{actor}</strong> activity. Risk rating: <strong>{risk}</strong>.",
        variant="success",
    )

    # ── Metrics ──
    metric_row([
        {"value": risk, "label": "Risk Rating", "color": risk_color},
        {"value": "5", "label": "MITRE Techniques", "color": "blue"},
        {"value": "8", "label": "Detection Priorities", "color": "purple"},
        {"value": "7", "label": "Critical Assets", "color": "green"},
    ])

    section_divider()

    # ── Business Context Card ──
    st.markdown("##### Business Context")

    c1, c2 = st.columns(2)
    with c1:
        enterprise_card("Application", f"{application}", "accent-left")
        enterprise_card("Threat Actor", f"{actor}", "accent-left")
    with c2:
        enterprise_card("Business Function", f"{business}", "accent-left")
        enterprise_card("Business Criticality", f"{risk}", "accent-left")

    section_divider()

    # ── Threat Landscape ──
    st.markdown("##### Threat Landscape")

    t1, t2 = st.columns(2)
    with t1:
        enterprise_card(
            "Primary Threat Categories",
            "Credential Theft · Password Spraying · Account Takeover · "
            "Public Facing Application Exploitation · API Abuse · "
            "Privilege Escalation · Service Account Abuse · Insider Threat",
            "accent-warning",
        )
    with t2:
        enterprise_card(
            "Critical Assets",
            "Customer Accounts · Authentication Services · Application APIs · "
            "Business Data · Identity Platform · Privileged Accounts · Financial Information",
            "accent-danger",
        )

    section_divider()

    # ── MITRE ATT&CK ──
    st.markdown("##### MITRE ATT&CK Mapping")

    mitre_data = {
        "Technique": ["T1078", "T1110", "T1190", "T1098", "T1021"],
        "Name": [
            "Valid Accounts",
            "Password Guessing",
            "Public Facing Application",
            "Account Manipulation",
            "Remote Services",
        ],
        "Priority": ["Critical", "Critical", "High", "High", "Medium"],
    }
    st.table(mitre_data)

    section_divider()

    # ── Detection Priorities ──
    st.markdown("##### Recommended Detection Priorities")

    p1, p2 = st.columns(2)
    with p1:
        checklist([
            "Password Spray Detection",
            "Impossible Travel",
            "Suspicious Authentication",
            "Privileged Account Monitoring",
        ])
    with p2:
        checklist([
            "Service Account Abuse",
            "Administrative Activity Monitoring",
            "OAuth Abuse Detection",
            "API Abuse Detection",
        ])

    section_divider()

    # ── SOC Recommendations ──
    st.markdown("##### SOC Recommendations")

    enterprise_card(
        "Monitoring Strategy",
        "Enable comprehensive identity monitoring · "
        "Collect authentication and administrative logs · "
        "Enable Microsoft Sentinel analytics for privileged accounts · "
        "Correlate authentication events with application activity · "
        "Monitor service accounts and privileged identities · "
        "Continuously review business-critical assets · "
        "Validate logging coverage across the application landscape",
        "accent-success",
    )

    section_divider()

    # ── Knowledge Generated ──
    st.markdown("##### Knowledge Generated")

    info_banner(
        "The following knowledge has been added to the customer security knowledge base "
        "and will be referenced during Detection Planning and AI Detection Generation.",
        variant="success",
    )

    k1, k2 = st.columns(2)
    with k1:
        checklist([
            "Business Context",
            "Business Criticality",
            "Threat Actor Profile",
            "Threat Landscape",
            "Critical Assets",
        ])
    with k2:
        checklist([
            "MITRE ATT&CK Mapping",
            "Detection Priorities",
            "Monitoring Recommendations",
            "Security Context",
        ])

    section_divider()

    # ── Detection Engineering Impact ──
    st.markdown("##### Detection Engineering Impact")

    info_banner(
        f"The assessment for <strong>{application}</strong> has established the initial security context. "
        f"Future Detection Generation will automatically consider the application business context, "
        f"threat actor profile, business criticality, critical assets, relevant MITRE ATT&CK techniques, "
        f"and detection priorities — enabling customer-specific Microsoft Sentinel detections "
        f"instead of generic analytics.",
        variant="context",
    )

    section_divider()

    # ── Navigate ──
    c1, c2 = st.columns(2)
    with c2:
        if st.button(
            "Continue to Application Analysis ▶",
            use_container_width=True,
            type="primary",
        ):
            st.session_state.step += 1
            st.rerun()
