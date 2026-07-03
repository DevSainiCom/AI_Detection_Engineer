import streamlit as st

from ui.components import *


def render():

    page_header(
        "Explainability",
        "AI reasoning behind the generated detection."
    )

    detection = st.session_state.get("detection")

    if detection:

        st.subheader("Knowledge Sources")

        st.write(
            detection.get(
                "_knowledge_sources",
                []
            )
        )

        st.subheader("Detection")

        st.json(detection)

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