import streamlit as st

from ui.components import *

from backend.services.log_validation_service import (
    log_validation_service,
)


def render():

    page_header(

        "Telemetry Validation",

        "Validate the uploaded telemetry for detection engineering readiness."

    )

    st.info(
        """
### Telemetry Validation Agent (Proof of Concept)

This page validates that the uploaded telemetry contains
sufficient information to support high-quality Microsoft
Sentinel detections.
"""
    )

    logs = st.session_state.sample_logs

    detection_context = st.session_state.detection_context

    if not logs:

        warning(
            "Please upload sample telemetry on the previous page."
        )

    else:

        parser_type = "Native Microsoft Sentinel"

        if detection_context:

            if any(
                "Custom" in item
                for item in detection_context.get(
                    "parser_context",
                    [],
                )
            ):
                parser_type = "Custom Parser"

        if st.button(
            "Validate Telemetry",
            type="primary",
        ):

            result = log_validation_service.validate(

                sample_logs=logs,

                parser_type=parser_type,

            )

            st.session_state.validation = result

        if st.session_state.validation:

            result = st.session_state.validation

            success("Telemetry validation completed.")

            st.markdown("---")

            st.subheader("Executive Summary")

            st.info(result["executive_summary"])

            st.markdown("### Detection Readiness")

            st.progress(result["telemetry_score"] / 100)

            st.metric(
                "Readiness Score",
                f"{result['telemetry_score']}%"
            )

            st.markdown("---")

            st.subheader("Available Security Entities")

            for item in result["available_entities"]:

                st.markdown(f"✅ {item}")

            st.markdown("---")

            st.subheader("Missing Security Entities")

            for item in result["missing_entities"]:

                st.markdown(f"⚠ {item}")

            st.markdown("---")

            st.subheader("Telemetry Recommendations")

            for item in result["recommendations"]:

                st.markdown(f"• {item}")

            st.markdown("---")

            st.subheader("Knowledge Generated")

            for item in result["knowledge_generated"]:

                st.markdown(f"✔ {item}")

            st.markdown("---")

            st.subheader("Detection Engineering Impact")

            st.info(
                result["detection_engineering_impact"]
            )

            with st.expander("Developer View"):

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