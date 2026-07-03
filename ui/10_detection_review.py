import streamlit as st

from ui.components import page_title, previous_button, next_button
from backend.services.detection_review_service import detection_review_service


def render():

    page_title(
        "Detection Review",
        "Enterprise Detection Quality Assessment"
    )

    detection = st.session_state.get("detection")

    if not detection:
        st.warning("Generate a detection first.")
        previous_button()
        return

    review = detection_review_service.review(detection)

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

    for finding in review["DetectionReview"]["Findings"]:
        st.warning(finding)

    st.subheader("Recommendations")

    for recommendation in review["DetectionReview"]["Recommendations"]:
        st.info(recommendation)

    previous_button()
    next_button()