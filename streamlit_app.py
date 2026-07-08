import streamlit as st

from ui.session import initialize
from ui.navigation import render as navigation

from ui import (
    threat_model,
    application_analysis,
    gap_analysis,
    detection_context,
    log_source,
    log_validation,
    use_case,
    detection_generation,
    detection_review,
    explainability,
    approval,
    export,
)

st.set_page_config(
    page_title="AI Detection Engineering Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize()

navigation()

PAGES = [
    # Customer Onboarding
    threat_model,
    application_analysis,
    gap_analysis,
    detection_context,
    log_source,
    log_validation,

    # Detection Engineering
    use_case,
    detection_generation,
    detection_review,
    explainability,

    # Deployment
    approval,
    export,
]

step = st.session_state.step

if step >= len(PAGES):
    st.session_state.step = 0
    step = 0

PAGES[step].render()
