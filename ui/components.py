import streamlit as st


def page_header(title, subtitle=""):

    st.title(title)

    if subtitle:

        st.caption(subtitle)


def next_button():

    return st.button(

        "Next ▶",

        use_container_width=True,

    )


def previous_button():

    return st.button(

        "◀ Previous",

        use_container_width=True,

    )


def section(title):

    st.markdown("---")

    st.subheader(title)


def success(text):

    st.success(text)


def warning(text):

    st.warning(text)