"""
Application Analysis UI

Collects application details after Threat Modeling.
"""

import streamlit as st

from backend.workflow.workflow_state import workflow_state

workflow_state.initialize()


def render():

    st.header("📦 Application Analysis")

    threat_model = st.session_state.get("threat_model")

    if threat_model is None:

        st.warning(
            "Please generate a Threat Model first."
        )

        return

    st.success(
        f"Threat Model loaded for: {threat_model.application_name}"
    )

    st.write(
        "Complete the application profile before continuing."
    )

    application_type = st.selectbox(
        "Application Type",
        [
            "Web Application",
            "REST API",
            "Database",
            "Identity Platform",
            "SaaS",
            "Hybrid",
            "Desktop Application",
        ],
    )

    internet_facing = st.radio(
        "Internet Facing",
        [
            "Yes",
            "No",
        ],
        horizontal=True,
    )

    authentication = st.selectbox(
        "Authentication",
        [
            "Microsoft Entra ID",
            "Active Directory",
            "OAuth",
            "SAML",
            "LDAP",
            "Local Accounts",
        ],
    )

    cloud_provider = st.selectbox(
        "Cloud Provider",
        [
            "Azure",
            "AWS",
            "Google Cloud",
            "Hybrid",
            "On-Premises",
        ],
    )

    hosting_environment = st.selectbox(
        "Hosting Environment",
        [
            "Azure VM",
            "Azure App Service",
            "AKS",
            "Kubernetes",
            "VMware",
            "Physical Server",
        ],
    )

    business_criticality = st.selectbox(
        "Business Criticality",
        [
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
    )

    data_classification = st.selectbox(
        "Data Classification",
        [
            "Public",
            "Internal",
            "Confidential",
            "Restricted",
        ],
    )

    technology_stack = st.text_input(
        "Technology Stack",
        placeholder="Example: .NET, IIS, SQL Server, Redis"
    )

    if st.button(
        "Save Application Analysis",
        use_container_width=True,
    ):

        st.session_state["application_analysis"] = {

            "application_name": threat_model.application_name,

            "business_function": threat_model.business_function,

            "application_type": application_type,

            "internet_facing": internet_facing,

            "authentication": authentication,

            "cloud_provider": cloud_provider,

            "hosting_environment": hosting_environment,

            "business_criticality": business_criticality,

            "data_classification": data_classification,

            "technology_stack": [
                item.strip()
                for item in technology_stack.split(",")
                if item.strip()
            ],
        }

        st.success(
            "Application Analysis saved successfully."
        )

        st.json(
            st.session_state["application_analysis"]
        )