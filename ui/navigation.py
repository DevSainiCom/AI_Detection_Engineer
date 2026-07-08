import streamlit as st

STEPS = [

    "Threat Model",

    "Application Analysis",

    "Coverage Analysis",

    "Detection Context",

    "Telemetry Analysis",

    "Telemetry Validation",

    "Detection Planning",

    "AI Detection Generation",

    "Detection Review",

    "Detection Explanation",

    "Approval",

    "Deployment Package",

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
        f"Step {current + 1} of {len(STEPS)}"
    )