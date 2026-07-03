import streamlit as st

from ui.components import *


def render():

    page_header(

        "Threat Model",

        "Describe the attack scenario."

    )

    model = {

        "ApplicationName":

        st.text_input(

            "Application Name"

        ),

        "BusinessFunction":

        st.text_input(

            "Business Function"

        ),

        "ThreatActor":

        st.selectbox(

            "Threat Actor",

            [

                "Cyber Criminal",

                "APT",

                "Insider",

                "Hacktivist",

            ],

        ),

        "Criticality":

        st.selectbox(

            "Business Criticality",

            [

                "Low",

                "Medium",

                "High",

                "Critical",

            ],

        ),

        "AttackDescription":

        st.text_area(

            "Attack Description",

            height=180,

        ),

    }

    st.session_state.threat_model = model

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col2:

        if next_button():

            st.session_state.step += 1

            st.rerun()