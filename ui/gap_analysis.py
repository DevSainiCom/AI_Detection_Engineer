import streamlit as st

from ui.components import *

from backend.services.gap_analysis_service import (
    gap_analysis_service,
)


def render():

    page_header(
        "Gap Analysis",
        "Assess current detection coverage and identify monitoring improvements."
    )

    # -------------------------------------------------------
    # Ensure Application Analysis has been completed
    # -------------------------------------------------------

    if st.session_state.application is None:

        warning("Please complete Application Analysis first.")

    else:

        # -------------------------------------------------------
        # Generate Gap Analysis (only once)
        # -------------------------------------------------------

        if st.session_state.gap_analysis is None:

            st.session_state.gap_analysis = (
                gap_analysis_service.analyze(
                    st.session_state.application
                )
            )

        result = st.session_state.gap_analysis

        st.success("Gap analysis completed successfully.")

        st.markdown("---")

        st.subheader("Executive Summary")
        st.info(result.executive_summary)

        st.markdown("### Detection Coverage")

        st.progress(result.coverage_score / 100)

        st.metric(
            "Coverage Score",
            f"{result.coverage_score}%"
        )

        st.metric(
            "Security Maturity",
            result.security_maturity
        )

        st.markdown("---")

        st.subheader("Security Observations")

        for item in result.security_observations:
            st.markdown(f"• {item}")

        st.markdown("---")

        st.subheader("Missing Detection Coverage")

        for item in result.missing_detection_use_cases:
            st.markdown(f"🛡️ {item}")

        st.markdown("---")

        st.subheader("Recommended Log Sources")

        for item in result.missing_log_sources:
            st.markdown(f"📄 {item}")

        st.markdown("---")

        st.subheader("Missing MITRE ATT&CK Coverage")

        for item in result.missing_mitre_coverage:
            st.markdown(f"• {item}")

        st.markdown("---")

        st.subheader("SOC Recommendations")

        for item in result.recommendations:
            st.markdown(f"✔ {item}")

        st.markdown("---")

        st.subheader("Detection Development Roadmap")

        for idx, item in enumerate(result.detection_roadmap, start=1):
            st.markdown(f"{idx}. {item}")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        for item in result.knowledge_generated:
            st.markdown(f"✅ {item}")

        st.markdown("---")

        st.subheader("How This Analysis Will Be Used")

        st.info(result.future_ai_usage)

        st.markdown("---")

        st.subheader("Future AI Enhancement")

        st.warning(
            """
Future versions of the AI Gap Analysis Agent will automatically compare:

- Threat Model
- Application Analysis
- Existing Detection Library
- MITRE ATT&CK Coverage
- Microsoft Sentinel Analytics Rules
- Available Log Sources

The platform will continuously calculate detection coverage,
identify monitoring blind spots and recommend the highest-priority
detections to develop based on customer risk.
"""
        )

        with st.expander("Developer View"):

            st.json(result.model_dump())

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