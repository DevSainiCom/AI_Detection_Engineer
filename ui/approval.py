import streamlit as st

from ui.components import *

from backend.services.approval_workflow_service import (
    approval_workflow_service,
)


def render():

    page_header(
        "Approval Workflow"
    )

    detection = st.session_state.detection

    if detection:

        status = st.selectbox(

            "Status",

            approval_workflow_service.VALID_STATUS,

        )

        if st.button("Update Status"):

            approval_workflow_service.update_status(

                detection,

                status,

            )

            success("Status Updated")

    else:

        warning("Generate detection first.")

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