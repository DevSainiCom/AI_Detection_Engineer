import streamlit as st


def reset_workflow():

    keep = {
        "theme",
    }

    keys = list(st.session_state.keys())

    for key in keys:

        if key not in keep:

            del st.session_state[key]

    st.session_state.step = 0

    st.rerun()