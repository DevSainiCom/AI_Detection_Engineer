import streamlit as st

STEPS = [

    "Threat Model",

    "Application",

    "Gap Analysis",

    "Questionnaire",

    "Log Source",

    "Validation",

    "Use Case",

    "Detection",

    "KQL Review",

    "Detection Review",

    "Explainability",

    "Approval",

    "Export",

]


def render():

    st.sidebar.title(

        "AI Detection Engineer"

    )

    current = st.session_state.step

    for index, item in enumerate(STEPS):

        if index < current:

            icon = "✅"

        elif index == current:

            icon = "▶"

        else:

            icon = "⚪"

        st.sidebar.write(

            f"{icon} {item}"

        )

    st.sidebar.divider()

    st.sidebar.progress(

        (current + 1) / len(STEPS)

    )

    st.sidebar.caption(

        f"Step {current+1} of {len(STEPS)}"

    )