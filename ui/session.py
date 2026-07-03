import streamlit as st


def initialize():

    defaults = {

        "step": 0,

        "threat_model": {},

        "application": {},

        "gap_analysis": {},

        "questionnaire": {},

        "connector": None,

        "sample_logs": [],

        "validation": {},

        "use_case": {},

        "context": None,

        "detection": None,

        "review": None,

        "audit": None,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value