import streamlit as st

from ui.components import page_title, previous_button, next_button

from backend.services.approval_workflow_service import (
    approval_workflow_service,
)


def render():

    page_title(
        "Approval Workflow"
    )

    detection = st.session_state.get("detection")

    if not detection:

        st.warning("Generate a detection first.")

        previous_button()

        return

    status = st.selectbox(

        "Status",

        approval_workflow_service.VALID_STATUS,

    )

    if st.button("Update Status"):

        approval_workflow_service.update_status(

            detection,

            status,

        )

        st.success("Status updated.")

        st.json(detection)

    previous_button()

    next_button()