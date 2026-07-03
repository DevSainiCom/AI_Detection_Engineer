import json
import streamlit as st

from ui.components import *


def render():

    page_header(
        "Export Detection",
        "Export the generated detection package."
    )

    detection = st.session_state.get("detection")

    if not detection:

        warning(
            "Generate a detection before exporting."
        )

    else:

        st.success(
            "Detection is ready for export."
        )

        st.markdown("### Detection Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Severity",
                detection.get(
                    "Severity",
                    "-"
                )
            )

        with c2:
            st.metric(
                "Status",
                detection.get(
                    "Status",
                    "Draft"
                )
            )

        with c3:
            st.metric(
                "Version",
                detection.get(
                    "Version",
                    "1.0"
                )
            )

        st.markdown("---")

        st.subheader("Detection Name")

        st.write(
            detection.get(
                "DetectionName",
                "-"
            )
        )

        st.subheader("Description")

        st.write(
            detection.get(
                "Description",
                "-"
            )
        )

        st.subheader("KQL")

        st.code(
            detection.get(
                "Query",
                ""
            ),
            language="sql",
        )

        st.subheader("MITRE ATT&CK")

        st.write(
            detection.get(
                "Tactics",
                []
            )
        )

        st.write(
            detection.get(
                "Techniques",
                []
            )
        )

        st.subheader("Entity Mappings")

        st.json(
            detection.get(
                "EntityMappings",
                []
            )
        )

        st.subheader("Recommended Actions")

        st.write(
            detection.get(
                "RecommendedActions",
                []
            )
        )

        st.markdown("---")

        export_json = json.dumps(
            detection,
            indent=4,
        )

        st.download_button(
            label="⬇ Download Detection JSON",
            data=export_json,
            file_name="sentinel_detection.json",
            mime="application/json",
            use_container_width=True,
        )

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        if previous_button():

            st.session_state.step -= 1
            st.rerun()

    with c2:

        if primary_button("Finish"):

            st.success(
                "Detection Engineering workflow completed successfully."
            )