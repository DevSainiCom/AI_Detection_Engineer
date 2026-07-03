"""
Workflow State

Stores data between workflow steps using
Streamlit Session State.
"""

import streamlit as st


class WorkflowState:

    @staticmethod
    def initialize():

        defaults = {

            "threat_model": None,
            "application_analysis": None,
            "questionnaire": None,
            "log_validation": None,
            "use_case": None,
            "detection": None,
            "kql_review": None,
            "detection_review": None,
            "human_review": None,

        }

        for key in defaults:

            if key not in st.session_state:

                st.session_state[key] = defaults[key]


workflow_state = WorkflowState()