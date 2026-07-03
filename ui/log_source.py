import json

import streamlit as st

from ui.components import *

from backend.services.connector_service import (

    connector_service,

)


def render():

    page_header(

        "Log Source",

        "Select a native connector or upload custom logs."

    )

    source = st.radio(

        "Source Type",

        [

            "Microsoft Sentinel Native Connector",

            "Custom Application",

        ],

    )

    if source == "Microsoft Sentinel Native Connector":

        connector_name = st.selectbox(

            "Connector",

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

            "Application Name"

        )

    uploaded = st.file_uploader(

        "Upload Sample Logs",

        type=["json"],

    )

    if uploaded:

        logs = json.load(uploaded)

        connector = connector_service.get_connector(

            connector_name

        )

        st.session_state.connector = connector

        st.session_state.sample_logs = logs

        success(

            f"{len(logs)} sample logs loaded."

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