import streamlit as st

from ui.components import *

from backend.services.kql_review_service import (
    kql_review_service,
)


def render():

    page_header(
        "KQL Review",
        "AI Quality Assessment"
    )

    detection = st.session_state.detection

    if detection:

        review = kql_review_service.review(

            detection["Query"]

        )

        st.session_state.review = review

        st.metric(

            "KQL Score",

            review["score"]

        )

        st.json(review)

    else:

        warning(
            "Generate a detection first."
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