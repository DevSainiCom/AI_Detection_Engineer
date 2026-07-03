import streamlit as st

from ui.components import *

from backend.services.application_analysis_service import (
    application_analysis_service,
)


def render():

    page_header(

        "Application Analysis",

        "Understand the application architecture."

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

        placeholder="Java,.NET,SQL Server"

    )

    if st.button("Analyze"):

        result = application_analysis_service.analyze(

            application_name=app_name,

            application_type=app_type,

            business_function=

            st.session_state.threat_model.get(

                "BusinessFunction",

                "",

            ),

            authentication=authentication,

            cloud_provider=cloud,

            technology_stack=[

                x.strip()

                for x in stack.split(",")

                if x

            ],

            business_criticality=

            st.session_state.threat_model.get(

                "Criticality",

                "Medium",

            ),

            data_classification=classification,

        )

        st.session_state.application = result

        success("Application analyzed.")

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