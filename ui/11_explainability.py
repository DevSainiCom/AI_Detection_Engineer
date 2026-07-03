import streamlit as st

from ui.components import page_title, previous_button, next_button
from backend.services.explainability_service import explainability_service


def render():

    page_title(
        "Explainability"
    )

    detection = st.session_state.get("detection")

    if not detection:
        st.warning("Generate a detection first.")
        previous_button()
        return

    context = st.session_state.get("context")

    if context:

        explanation = explainability_service.build(
            context
        )

        st.json(explanation)

    else:

        st.info("No explainability available.")

    previous_button()
    next_button()