"""
AI Detection Engineering Assistant

Main Streamlit Application
"""

import streamlit as st

from backend.workflow.workflow_state import workflow_state

from ui.threat_model_ui import render as threat_model

from ui.application_analysis_ui import render as application_analysis


# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="AI Detection Engineering Assistant",
    page_icon="🛡️",
    layout="wide",
)

workflow_state.initialize()

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.title("🛡️ AI Detection Engineering Assistant")

st.caption(
    "Enterprise AI Assistant for Microsoft Sentinel Detection Engineering"
)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

workflow = st.sidebar.radio(
    "Detection Engineering Workflow",
    (
        "Threat Model",
        "Application Analysis",
        "Questionnaire",
        "Log Validation",
        "Use Case Proposal",
        "Detection Generation",
        "KQL Review",
        "Detection Review",
        "Human Review",
    ),
)

# ----------------------------------------------------------
# Workflow Routing
# ----------------------------------------------------------

if workflow == "Threat Model":

    threat_model()

elif workflow == "Application Analysis":

    application_analysis()

elif workflow == "Questionnaire":

    st.info("Questionnaire module coming next.")

elif workflow == "Log Validation":

    st.info("Log Validation module coming next.")

elif workflow == "Use Case Proposal":

    st.info("Use Case Proposal module coming next.")

elif workflow == "Detection Generation":

    st.info("Detection Generation module coming next.")

elif workflow == "KQL Review":

    st.info("KQL Review module coming next.")

elif workflow == "Detection Review":

    st.info("Detection Review module coming next.")

elif workflow == "Human Review":

    st.info("Human Review module coming next.")