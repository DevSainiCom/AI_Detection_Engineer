"""
Detection Context — Enterprise Redesign
"""

import streamlit as st
import time

from ui.components import *
from ui.design_system import (
    enterprise_card, metric_row, info_banner, checklist, section_divider,
)
from backend.services.detection_context_service import detection_context_service


def render():

    page_setup(
        title="Detection Context",
        subtitle="Capture telemetry, parser, and operational context required for customer-specific Microsoft Sentinel detection engineering.",
        eyebrow="Customer Onboarding · Step 4 of 12",
        agent_name="Detection Context Agent",
        agent_desc=(
            "Collects customer-specific telemetry and parser knowledge that will be stored "
            "in the Detection Knowledge Manager and retrieved during AI detection generation. "
            "<strong>Current POC:</strong> Rule-based context collection. "
            "<strong>Future:</strong> Automatic parser discovery, log schema extraction, "
            "and knowledge indexing via RAG pipeline."
        ),
    )

    # ── Telemetry Source ──

    st.markdown("##### Telemetry Collection Strategy")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        parser_type = st.radio(
            "Telemetry Source",
            ["Native Microsoft Sentinel", "Custom Parser"],
            horizontal=True,
        )

    section_divider()

    # ── Native vs Custom ──

    left, right = st.columns(2, gap="large")

    if parser_type == "Native Microsoft Sentinel":

        with left:
            st.markdown("##### Sentinel Configuration")
            connector_name = st.selectbox(
                "Connector",
                [
                    "Microsoft Entra ID", "Microsoft Defender XDR",
                    "Azure Activity", "Microsoft 365",
                    "Windows Security Events", "Syslog",
                    "AWS CloudTrail", "Google Cloud", "Other",
                ],
            )
            asim = st.selectbox(
                "ASIM Normalization",
                ["Implemented", "Partially Implemented", "Not Implemented"],
            )
            dcr = st.selectbox(
                "Data Collection Rules",
                ["Configured", "Partially Configured", "Not Used"],
            )

        with right:
            st.markdown("##### Tables & Transforms")
            tables = st.text_input(
                "Available Sentinel Tables",
                placeholder="SigninLogs, DeviceEvents, SecurityEvent...",
            )
            transformations = st.selectbox(
                "Custom Transformations",
                ["None", "Some", "Extensive"],
            )
            telemetry_quality = st.selectbox(
                "Telemetry Quality",
                ["High", "Medium", "Low"],
            )

    else:

        with left:
            st.markdown("##### Parser Details")
            parser_name = st.text_input("Parser Name")
            parser_language = st.selectbox(
                "Parser Technology",
                ["KQL Parser", "Logstash", "Fluent Bit", "Fluentd", "Cribl", "Python", "Other"],
            )
            parser_docs = st.selectbox(
                "Documentation Available",
                ["Yes", "Partial", "No"],
            )
            field_mapping = st.selectbox(
                "Field Mapping Document",
                ["Available", "Partial", "Not Available"],
            )

        with right:
            st.markdown("##### Sample Data")
            normalization = st.selectbox(
                "Normalization Rules",
                ["Documented", "Partially Documented", "Unknown"],
            )
            raw_logs = st.selectbox(
                "Sample Raw Logs",
                ["Available", "Limited", "Unavailable"],
            )
            parsed_logs = st.selectbox(
                "Sample Parsed Logs",
                ["Available", "Limited", "Unavailable"],
            )
            telemetry_quality = st.selectbox(
                "Telemetry Quality",
                ["High", "Medium", "Low"],
            )

    section_divider()

    # ── Operational Context ──

    st.markdown("##### Operational Context")

    op1, op2 = st.columns(2, gap="large")

    with op1:
        retention = st.selectbox(
            "Log Retention",
            ["30 Days", "90 Days", "180 Days", "1 Year", "More than 1 Year"],
        )

    with op2:
        enrichment = st.multiselect(
            "Available Enrichment Sources",
            ["CMDB", "Asset Inventory", "Microsoft Entra ID",
             "Threat Intelligence", "GeoIP", "Vulnerability Scanner", "Identity Database"],
        )

    section_divider()

    if st.button("⚙️ Generate Detection Context", type="primary", use_container_width=True):
        with st.spinner("Generating detection context..."):
            time.sleep(1)
            result = detection_context_service.generate(
                threat_model=st.session_state.threat_model,
                application=st.session_state.application,
                coverage_analysis=st.session_state.gap_analysis,
                parser_type=parser_type,
            )
            st.session_state.detection_context = result
            st.rerun()

    # ── Results ──

    if st.session_state.detection_context is None:
        return

    result = st.session_state.detection_context

    info_banner(
        "Detection context generated and added to the Knowledge Manager.",
        variant="success",
    )

    # ── Summary ──
    st.markdown("##### Executive Summary")
    enterprise_card("Context Summary", result["executive_summary"], "accent-left")

    section_divider()

    # ── Context Detail ──
    st.markdown("##### Context Details")

    ctx1, ctx2 = st.columns(2)
    with ctx1:
        st.markdown("###### Business Context")
        checklist(result["business_context"])
    with ctx2:
        st.markdown("###### Telemetry & Parser Context")
        checklist(result["parser_context"])

    section_divider()

    # ── Knowledge Sources ──
    st.markdown("##### Knowledge Sources for RAG Retrieval")

    info_banner(
        "The following sources will be indexed in the Detection Knowledge Manager "
        "and retrieved by the Context Retrieval Agent during detection generation.",
        variant="info",
    )

    checklist(result["rag_sources"])

    section_divider()

    # ── Knowledge Generated ──
    st.markdown("##### Knowledge Generated")
    info_banner(
        "Customer-specific knowledge added to the Detection Knowledge Manager.",
        variant="success",
    )
    checklist(result["knowledge_generated"])

    section_divider()

    # ── Pipeline ──
    st.markdown("##### Detection Engineering Pipeline")

    enterprise_card(
        "How This Context Is Used",
        "1. <strong>Detection Planning Agent</strong> — determines what knowledge is required.<br/>"
        "2. <strong>Context Retrieval Agent</strong> — retrieves parser knowledge, telemetry "
        "information, and normalisation rules from the Knowledge Manager.<br/>"
        "3. <strong>Detection Generation Engine</strong> — combines context with detection "
        "requirements to generate customer-specific Microsoft Sentinel detections.<br/>"
        "4. <strong>Detection Review Agent</strong> — validates quality before deployment.",
        "accent-left",
    )

    section_divider()

    info_banner(result["detection_engineering_impact"], variant="context")

    developer_view(result)
    nav_buttons()
