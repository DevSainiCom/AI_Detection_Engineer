import streamlit as st

from ui.components import *

from backend.services.detection_review_service import (
    detection_review_service,
)


def render():

    page_header(
        "Detection Review",
        "Enterprise Detection Quality Review"
    )

    detection = st.session_state.detection

    if detection:

        review = detection_review_service.review(
            detection
        )

        st.session_state.review = review

        st.metric(
            "Overall Score",
            review["DetectionReview"]["OverallScore"]
        )

        st.metric(
            "Rating",
            review["DetectionReview"]["Rating"]
        )

        st.subheader("Findings")

        for item in review["DetectionReview"]["Findings"]:
            st.warning(item)

        st.subheader("Recommendations")

        for item in review["DetectionReview"]["Recommendations"]:
            st.info(item)

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