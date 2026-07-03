"""
Threat Model UI
"""

import streamlit as st

from backend.api.threat_model_api import threat_model_api
from backend.schemas.threat_model_request import ThreatModelRequest
from backend.workflow.workflow_state import workflow_state

workflow_state.initialize()


def render():

    st.header("Threat Modeling")

    application_name = st.text_input(
        "Application Name"
    )

    business_function = st.text_input(
        "Business Function"
    )

    description = st.text_area(
        "Application Description",
        height=150,
    )

    if st.button(
        "Generate Threat Model",
        use_container_width=True,
    ):

        if not application_name.strip():

            st.warning("Application Name is required.")

            return

        if not business_function.strip():

            st.warning("Business Function is required.")

            return

        request = ThreatModelRequest(
            application_name=application_name,
            business_function=business_function,
            description=description,
        )

        with st.spinner("Generating Threat Model..."):

            threat_model = threat_model_api.generate(request)

        # SAVE FOR NEXT STEPS
        st.session_state["threat_model"] = threat_model

        st.success("Threat Model Generated")

        st.json(threat_model.model_dump())