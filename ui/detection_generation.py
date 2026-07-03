import streamlit as st

from ui.components import *

from backend.core.workflow_engine import (
    workflow_engine,
)


def render():

    page_header(

        "Detection Generation",

        "Enterprise AI Detection Engineering"

    )

    connector = st.session_state.get(

        "connector"

    )

    if connector is None:

        connector_name = "Custom"

    elif isinstance(connector, str):

        connector_name = connector

    elif hasattr(connector, "name"):

        connector_name = connector.name

    else:

        connector_name = str(connector)

    if st.button(

        "🚀 Generate Detection",

        use_container_width=True,

    ):

        with st.spinner(

            "AI is generating detection..."

        ):

            result = workflow_engine.execute(

                attack_description=

                st.session_state.threat_model.get(

                    "AttackDescription",

                    "",

                ),

                connector_name=connector_name,

                sample_logs=

                st.session_state.get(

                    "sample_logs",

                    [],

                ),

                threat_model=

                st.session_state.get(

                    "threat_model",

                    {},

                ),

                application_analysis=

                st.session_state.get(

                    "application",

                    {},

                ),

                questionnaire=

                st.session_state.get(

                    "questionnaire",

                    {},

                ),

            )

            st.session_state.detection = result

        success(

            "Detection generated successfully."

        )

    detection = st.session_state.get(

        "detection"

    )

    if detection:

    st.markdown("---")

st.subheader("Detection Summary")

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Severity",
        detection.get(
            "Severity",
            "-"
        )
    )

    st.metric(
        "Risk Score",
        detection.get(
            "RiskScore",
            "-"
        )
    )

with c2:

    st.metric(
        "Status",
        detection.get(
            "Status",
            "-"
        )
    )

    st.metric(
        "Version",
        detection.get(
            "Version",
            "-"
        )
    )

st.markdown("---")

st.subheader("Detection Name")

st.write(

    detection.get(

        "DetectionName",

        ""

    )

)

st.subheader("Description")

st.write(

    detection.get(

        "Description",

        ""

    )

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

st.markdown("---")

st.subheader("Generated KQL")

st.code(

    detection.get(

        "Query",

        ""

    ),

    language="sql",

)

st.markdown("---")

st.subheader("False Positives")

st.write(

    detection.get(

        "FalsePositives",

        []

    )

)

st.markdown("---")

st.subheader("Recommended Actions")

st.write(

    detection.get(

        "RecommendedActions",

        []

    )

)

st.markdown("---")

st.subheader("Knowledge Sources")

st.write(

    detection.get(

        "_knowledge_sources",

        []

    )

)

if "KQLReview" in detection:

    st.markdown("---")

    st.subheader(

        "KQL Review"

    )

    st.json(

        detection["KQLReview"]

    )