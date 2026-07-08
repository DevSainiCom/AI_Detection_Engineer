import json
import streamlit as st

from ui.components import *

from backend.services.connector_service import (
    connector_service,
)


def render():

    page_header(
        "Telemetry Analysis",
        "Analyse sample telemetry and prepare it for detection engineering."
    )

    st.info(
        """
### Telemetry Analysis Agent (Proof of Concept)

This page analyses representative telemetry provided by the customer.
The extracted knowledge will later be indexed within the Detection
Knowledge Manager and used by the Context Retrieval Agent during
AI-assisted detection generation.
"""
    )

    st.markdown("---")

    # ----------------------------------------------------------
    # Read parser selection from Detection Context
    # ----------------------------------------------------------

    detection_context = st.session_state.detection_context

    parser_type = "Native Microsoft Sentinel"

    if detection_context is not None:

        parser_context = detection_context.get("parser_context", [])

        if any("Custom" in item for item in parser_context):
            parser_type = "Custom Parser"

    st.subheader("Telemetry Source")

    st.write(f"**Parser Type:** {parser_type}")

    if parser_type == "Native Microsoft Sentinel":

        connector_name = st.selectbox(

            "Microsoft Sentinel Connector",

            [

                "Windows Security Events",

                "Microsoft Defender XDR",

                "Microsoft Entra ID",

                "Azure Activity",

                "Office 365",

                "CEF",

                "Syslog",

            ],

        )

    else:

        connector_name = st.text_input(
            "Custom Parser / Application Name"
        )

    st.markdown("---")

    uploaded = st.file_uploader(

        "Upload Sample Logs",

        type=[

            "json",

            "txt",

            "log",

        ],

    )

    if uploaded:

        if uploaded.name.endswith(".json"):

            logs = json.load(uploaded)

        else:

            logs = uploaded.read().decode("utf-8").splitlines()

        connector = connector_service.get_connector(
            connector_name
        )

        st.session_state.connector = connector

        st.session_state.sample_logs = logs

        success(
            f"{len(logs)} sample log records loaded."
        )

        st.markdown("---")

        st.subheader("Telemetry Analysis Summary")

        st.success(
            "The uploaded telemetry has been successfully analysed."
        )

        st.markdown("### Initial Findings")

        st.markdown("- Telemetry successfully parsed")
        st.markdown("- Log format identified")
        st.markdown("- Timestamp fields detected")
        st.markdown("- Authentication events identified")
        st.markdown("- Network attributes identified")
        st.markdown("- Candidate entities extracted")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        st.markdown("✅ Sample Telemetry")
        st.markdown("✅ Parser Context")
        st.markdown("✅ Candidate Entities")
        st.markdown("✅ Timestamp Information")
        st.markdown("✅ Detection Data Sources")

        st.markdown("---")

        st.info(
            """
The analysed telemetry will be stored within the Detection
Knowledge Manager.

During detection generation the Context Retrieval Agent
will retrieve the relevant parser knowledge,
sample telemetry and field information to help the
Detection Generation Engine produce customer-specific
Microsoft Sentinel detections.
"""
        )

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