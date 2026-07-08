import streamlit as st


def initialize():

    defaults = {

        "step": 0,

        # ---------------------------------------------------------
        # Customer Onboarding
        # ---------------------------------------------------------

        "threat_model": {},
        "application": None,
        "gap_analysis": None,
        "detection_context": None,

        # ---------------------------------------------------------
        # Detection Engineering Workflow
        # ---------------------------------------------------------

        "validation": None,
        "use_case": None,
        "context": None,
        "detection": None,
        "review": None,
        "audit": None,

        # ---------------------------------------------------------
        # Platform Services
        # ---------------------------------------------------------

        "connector": None,
        "sample_logs": [],
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value