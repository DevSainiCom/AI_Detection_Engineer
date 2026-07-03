"""
Application Analysis UI
"""

import streamlit as st

from backend.workflow.workflow_state import workflow_state

workflow_state.initialize()


def render():

    st.header("Application Analysis")

    threat_model = st.session_state.get("threat_model")

    if threat_model is None:

        st.warning(
            "Please complete Threat Modeling first."
        )

        return

    st.success(
        f"Threat Model loaded for {threat_model.application_name}"
    )

    st.subheader("Application Profile")

    application_type = st.selectbox(
        "Application Type",
        [
            "Web Application",
            "API",
            "Database",
            "Identity Platform",
            "SaaS",
            "Hybrid",
        ],
    )

    internet_facing = st.radio(
        "Internet Facing",
        [
            "Yes",
            "No",
        ],
    )

    authentication = st.selectbox(
        "Authentication",
        [
            "Microsoft Entra ID",
            "Active Directory",
            "OAuth",
            "SAML",
            "LDAP",
            "Local Authentication",
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

    hosting = st.selectbox(
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

    criticality = st.selectbox(
        "Business Criticality",
        [
            "Low",
            "Medium",
            "High",
            "Critical",
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

    technology = st.text_input(
        "Technology Stack",
        placeholder="Example: IIS, .NET, SQL Server"
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

            "hosting_environment": hosting,

            "business_criticality": criticality,

            "data_classification": classification,

            "technology_stack": technology,

        }

        st.success(
            "Application Analysis completed."
        )

        st.json(
            st.session_state["application_analysis"]
        )