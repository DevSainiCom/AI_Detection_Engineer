import streamlit as st

from ui.session import initialize
from ui.navigation import render as navigation

from ui import (
    threat_model,
    application_analysis,
    gap_analysis,
    questionnaire,
    log_source,
    log_validation,
    use_case,
    detection_generation,
    kql_review,
    detection_review,
    explainability,
    approval,
    export,
)

st.set_page_config(

    page_title="AI Detection Engineer",

    page_icon="🛡️",

    layout="wide",

)

initialize()

navigation()

PAGES = [

    threat_model,

    application_analysis,

    gap_analysis,

    questionnaire,

    log_source,

    log_validation,

    use_case,

    detection_generation,

    kql_review,

    detection_review,

    explainability,

    approval,

    export,

]

step = st.session_state.step

if step >= len(PAGES):

    st.session_state.step = 0

    step = 0

PAGES[step].render()