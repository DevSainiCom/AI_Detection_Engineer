import streamlit as st

from ui.components import page_title, previous_button

from backend.services.export_service import (
    export_service,
)


def render():

    page_title(
        "Export"
    )

    detection = st.session_state.get("detection")

    if not detection:

        st.warning("Generate a detection first.")

        previous_button()

        return

    json_export = export_service.export_json(
        detection
    )

    yaml_export = export_service.export_yaml(
        detection
    )

    st.download_button(

        "Download JSON",

        json_export,

        file_name="sentinel_detection.json",

        mime="application/json",

    )

    st.download_button(

        "Download YAML",

        yaml_export,

        file_name="sentinel_detection.yaml",

        mime="text/yaml",

    )

    st.code(json_export)

    previous_button()