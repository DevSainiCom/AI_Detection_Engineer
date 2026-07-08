import streamlit as st
import time

from ui.components import *

from backend.services.detection_context_service import (
    detection_context_service,
)


def render():

    page_header(
        "Detection Context",
        "Capture the telemetry, parser and operational context required for customer-specific Microsoft Sentinel detection engineering."
    )

    st.info(
        """
### Detection Context Agent (Proof of Concept)

This page demonstrates the expected output of the **Detection Context Agent**.

The agent collects customer-specific telemetry, parser and operational knowledge
required for high-quality detection engineering.

The collected knowledge will later be stored within the **Detection Knowledge Manager**
and retrieved by the **Context Retrieval Agent** during AI-assisted detection generation.
"""
    )

    st.markdown("---")

    # ==========================================================
    # Parser Strategy
    # ==========================================================

    st.subheader("Telemetry Collection Strategy")

    parser_type = st.radio(
        "Telemetry Source",
        [
            "Native Microsoft Sentinel",
            "Custom Parser",
        ],
        horizontal=True,
    )

    st.markdown("---")

    # ==========================================================
    # Native Connector
    # ==========================================================

    if parser_type == "Native Microsoft Sentinel":

        connector_name = st.selectbox(
            "Microsoft Sentinel Connector",
            [
                "Microsoft Entra ID",
                "Microsoft Defender XDR",
                "Azure Activity",
                "Microsoft 365",
                "Windows Security Events",
                "Syslog",
                "AWS CloudTrail",
                "Google Cloud",
                "Other",
            ],
        )

        asim = st.selectbox(
            "ASIM Normalization",
            [
                "Implemented",
                "Partially Implemented",
                "Not Implemented",
            ],
        )

        tables = st.text_input(
            "Available Sentinel Tables",
            placeholder="SigninLogs, DeviceEvents, SecurityEvent..."
        )

        dcr = st.selectbox(
            "Data Collection Rules",
            [
                "Configured",
                "Partially Configured",
                "Not Used",
            ],
        )

        transformations = st.selectbox(
            "Custom Transformations",
            [
                "None",
                "Some",
                "Extensive",
            ],
        )

    # ==========================================================
    # Custom Parser
    # ==========================================================

    else:

        parser_name = st.text_input(
            "Parser Name"
        )

        parser_language = st.selectbox(
            "Parser Technology",
            [
                "KQL Parser",
                "Logstash",
                "Fluent Bit",
                "Fluentd",
                "Cribl",
                "Python",
                "Other",
            ],
        )

        parser_docs = st.selectbox(
            "Parser Documentation Available",
            [
                "Yes",
                "Partial",
                "No",
            ],
        )

        field_mapping = st.selectbox(
            "Field Mapping Document",
            [
                "Available",
                "Partial",
                "Not Available",
            ],
        )

        normalization = st.selectbox(
            "Normalization Rules",
            [
                "Documented",
                "Partially Documented",
                "Unknown",
            ],
        )

        raw_logs = st.selectbox(
            "Sample Raw Logs",
            [
                "Available",
                "Limited",
                "Unavailable",
            ],
        )

        parsed_logs = st.selectbox(
            "Sample Parsed Logs",
            [
                "Available",
                "Limited",
                "Unavailable",
            ],
        )

    st.markdown("---")

    # ==========================================================
    # Operational Context
    # ==========================================================

    st.subheader("Operational Context")

    telemetry_quality = st.selectbox(
        "Telemetry Quality",
        [
            "High",
            "Medium",
            "Low",
        ],
    )

    retention = st.selectbox(
        "Log Retention",
        [
            "30 Days",
            "90 Days",
            "180 Days",
            "1 Year",
            "More than 1 Year",
        ],
    )

    enrichment = st.multiselect(
        "Available Enrichment Sources",
        [
            "CMDB",
            "Asset Inventory",
            "Microsoft Entra ID",
            "Threat Intelligence",
            "GeoIP",
            "Vulnerability Scanner",
            "Identity Database",
        ],
    )

    st.markdown("---")

    if st.button(
        "Generate Detection Context",
        type="primary",
        use_container_width=True,
    ):

        with st.spinner(
            "Generating Detection Context..."
        ):

            time.sleep(1)

            result = detection_context_service.generate(

                threat_model=st.session_state.threat_model,

                application=st.session_state.application,

                coverage_analysis=st.session_state.gap_analysis,

                parser_type=parser_type,

            )

            st.session_state.detection_context = result

            st.rerun()

    # ==========================================================
    # Display Results
    # ==========================================================

    if st.session_state.detection_context is not None:

        result = st.session_state.detection_context

        st.success(
            "Detection context generated successfully."
        )

        st.markdown("---")

        st.subheader("Executive Summary")

        st.info(result["executive_summary"])

        st.markdown("---")

        st.subheader("Business Context")

        for item in result["business_context"]:
            st.markdown(f"• {item}")

        st.markdown("---")

        st.subheader("Telemetry & Parser Context")

        for item in result["parser_context"]:
            st.markdown(f"📄 {item}")
        st.markdown("---")

        st.subheader("Knowledge Sources for Context Retrieval")

        st.write(
            "The following knowledge sources will be indexed within the "
            "Detection Knowledge Manager and retrieved by the Context "
            "Retrieval Agent during detection generation."
        )

        for item in result["rag_sources"]:
            st.markdown(f"📚 {item}")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        st.success(
            "The following customer-specific knowledge has been added "
            "to the Detection Knowledge Manager:"
        )

        for item in result["knowledge_generated"]:
            st.markdown(f"✅ {item}")

        st.markdown("---")

        st.subheader("Detection Engineering Impact")

        st.info(result["detection_engineering_impact"])

        st.markdown("---")

        st.subheader("How the Multi-Agent Platform Uses This Information")

        st.success(
            """
The Detection Context Agent has now completed customer onboarding.

During detection generation:

1. The **Detection Planning Agent** determines what information is
   required for the requested detection.

2. The **Context Retrieval Agent** retrieves the relevant
   business context, parser knowledge, telemetry information,
   normalization rules and documentation from the Detection
   Knowledge Manager.

3. The **Detection Generation Engine** combines this context with
   the detection requirements to generate customer-specific
   Microsoft Sentinel detections.

4. The **Detection Quality Agent** validates the generated
   detection before it is approved for deployment.
"""
        )

        st.markdown("---")

        with st.expander("Developer View (Structured Data)"):

            st.json(result)

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        if previous_button():

            st.session_state.step -= 1

            st.rerun()

    with c2:

        if next_button():

            st.session_state.step += 1

            st.rerun()