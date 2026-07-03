import streamlit as st

from ui.components import *

from backend.services.use_case_generation_service import (
    use_case_generation_service,
)


def render():

    page_header(
        "Detection Use Case",
        "Generate the proposed detection."
    )

    if st.button("Generate Use Case"):

        use_case = use_case_generation_service.generate(
            st.session_state.threat_model
        )

        st.session_state.use_case = use_case

        success("Use case generated.")

        st.json(use_case)

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