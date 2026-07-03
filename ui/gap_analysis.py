import streamlit as st

from ui.components import *

from backend.services.gap_analysis_service import (

    gap_analysis_service,

)


def render():

    page_header(

        "Gap Analysis",

        "Identify monitoring gaps."

    )

    app = st.session_state.application

    if app:

        result = gap_analysis_service.analyze(

            app

        )

        st.session_state.gap_analysis = result

        st.json(result)

    else:

        warning(

            "Run Application Analysis first."

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