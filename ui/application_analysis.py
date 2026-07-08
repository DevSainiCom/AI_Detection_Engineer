import streamlit as st

from ui.components import *

from backend.services.application_analysis_service import (
    application_analysis_service,
)


def render():

    page_header(
        "Application Analysis",
        "Understand the application architecture and security posture."
    )

    app_name = st.text_input(
        "Application Name",
        value=st.session_state.threat_model.get(
            "ApplicationName",
            "",
        ),
    )

    app_type = st.selectbox(
        "Application Type",
        [
            "Web",
            "API",
            "Desktop",
            "Cloud Native",
            "Mobile",
        ],
    )

    authentication = st.selectbox(
        "Authentication",
        [
            "Entra ID",
            "Active Directory",
            "OAuth",
            "Local",
        ],
    )

    cloud = st.selectbox(
        "Hosting",
        [
            "Azure",
            "AWS",
            "GCP",
            "On-Prem",
        ],
    )

    classification = st.selectbox(
        "Data Classification",
        [
            "Public",
            "Internal",
            "Confidential",
            "Restricted",
        ],
    )

    stack = st.text_input(
        "Technology Stack",
        placeholder=".NET, Java, SQL Server, AKS, React..."
    )

    st.markdown("---")

    if st.button("Analyze Application"):

        result = application_analysis_service.analyze(

            application_name=app_name,

            application_type=app_type,

            business_function=st.session_state.threat_model.get(
                "BusinessFunction",
                "",
            ),

            authentication=authentication,

            cloud_provider=cloud,

            technology_stack=[
                x.strip()
                for x in stack.split(",")
                if x.strip()
            ],

            business_criticality=st.session_state.threat_model.get(
                "Criticality",
                "Medium",
            ),

            data_classification=classification,
        )

        st.session_state.application = result

    # -------------------------------------------------------
    # Display Analysis
    # -------------------------------------------------------

    if st.session_state.application is not None:

        result = st.session_state.application

        st.success("Application analysis completed successfully.")

        st.markdown("---")

        st.subheader("Executive Summary")
        st.info(result.executive_summary)

        st.markdown("### Overall Security Rating")

        if result.security_rating == "High":
            st.error(result.security_rating)
        elif result.security_rating == "Medium":
            st.warning(result.security_rating)
        else:
            st.success(result.security_rating)

        st.markdown("---")

        st.subheader("Application Overview")

        st.table(
            {
                "Attribute": [
                    "Application",
                    "Application Type",
                    "Business Function",
                    "Authentication",
                    "Hosting Platform",
                    "Business Criticality",
                    "Data Classification",
                ],
                "Value": [
                    result.application_name,
                    result.application_type,
                    result.business_function,
                    result.authentication,
                    result.cloud_provider,
                    result.business_criticality,
                    result.data_classification,
                ],
            }
        )

        st.markdown("---")

        st.subheader("Architecture Understanding")
        st.write(result.architecture_summary)

        st.markdown("#### Technology Stack")

        for item in result.technology_stack:
            st.markdown(f"- {item}")

        st.markdown("#### Critical Assets")

        for asset in result.critical_assets:
            st.markdown(f"✅ {asset}")

        st.markdown("#### Trust Boundaries")

        for boundary in result.trust_boundaries:
            st.markdown(f"- {boundary}")

        st.markdown("---")

        st.subheader("Security Observations")

        for observation in result.security_observations:
            st.markdown(f"• {observation}")

        st.markdown("---")

        st.subheader("Expected Security Telemetry")

        st.write(
            "Based on the application characteristics, the following "
            "Microsoft Sentinel log sources are recommended."
        )

        for log in result.recommended_log_sources:
            st.markdown(f"📄 {log}")

        st.markdown("---")

        st.subheader("Recommended Detection Opportunities")

        st.write(
            "The following detections should be prioritised for this application."
        )

        for detection in result.recommended_detection_use_cases:
            st.markdown(f"🛡️ {detection}")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        st.success(
            "The following information has been added to the customer's "
            "security knowledge base:"
        )

        for item in result.knowledge_generated:
            st.markdown(f"✔ {item}")

        st.markdown("---")

        st.subheader("How This Analysis Will Be Used")
        st.info(result.future_ai_usage)

        st.markdown("---")

        st.subheader("Future AI Enhancement")

        st.warning(
            """
Future versions of the platform will replace this rule-based analysis
with an AI-powered Application Analysis Agent.

The agent will analyse:

- Architecture Diagrams
- Application Documentation
- API Specifications
- Terraform Templates
- Kubernetes Manifests
- Azure Resources
- PDF / Word Documents
- Security Assessments

The extracted knowledge will automatically enrich future
Microsoft Sentinel detection generation.
"""
        )

        with st.expander("Developer View (Structured Data)"):
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