import streamlit as st

from ui.components import *

from backend.services.log_validation_service import (
    log_validation_service,
)


def render():

    page_header(
        "Log Validation",
        "Validate uploaded sample logs."
    )

    connector = st.session_state.connector
    logs = st.session_state.sample_logs

    if connector is None:

        warning("Please select a connector first.")

    else:

        if st.button("Validate Logs"):

            result = log_validation_service.validate(
                connector,
                logs,
            )

            st.session_state.validation = result

            success("Validation completed.")

            st.json(result)

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