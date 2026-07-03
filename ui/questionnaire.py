import streamlit as st

from ui.components import *

from backend.services.questionnaire_service import (

    questionnaire_service,

)


def render():

    page_header(

        "Questionnaire",

        "Collect missing detection information."

    )

    connector = st.radio(

        "Connector Type",

        [

            "native",

            "custom",

        ],

    )

    questions = questionnaire_service.generate(

        st.session_state.threat_model,

        connector,

    )

    answers = {}

    for question in questions:

        answers[question] = st.text_input(

            question

        )

    st.session_state.questionnaire = answers

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