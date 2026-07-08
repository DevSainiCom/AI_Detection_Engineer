import streamlit as st

from ui.components import *

from backend.core.workflow_engine import workflow_engine


def render():
    page_header(
        "Detection Generation",
        "Enterprise AI Detection Engineering",
    )

    if "step" not in st.session_state:
        st.session_state.step = 0

    connector = st.session_state.get("connector")

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
        with st.spinner("Generating enterprise detection..."):
            attack_description = st.session_state.get("attack_description", "")
            if not attack_description:
                threat_model = st.session_state.get("threat_model", {})
                attack_description = threat_model.get("AttackDescription", "")

            result = workflow_engine.execute(
                attack_description=attack_description,
                connector_name=connector_name,
                sample_logs=st.session_state.get("sample_logs", []),
                threat_model=st.session_state.get("threat_model", {}),
                application_analysis=st.session_state.get(
                    "application_analysis",
                    st.session_state.get("application", {}),
                ),
                questionnaire=st.session_state.get("questionnaire", {}),
            )
            st.session_state.detection = result

        success("Detection generated successfully.")

    detection = st.session_state.get("detection")

    if detection:
        st.markdown("---")
        st.subheader("Detection Summary")
        st.write(detection.get("Summary", detection.get("Description", "-")))

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Severity", detection.get("Severity", "-"))
        with c2:
            st.metric("Risk Score", detection.get("RiskScore", "-"))
        with c3:
            st.metric("Status", detection.get("Status", "-"))

        st.markdown("---")
        st.subheader("Detection Name")
        st.write(detection.get("DetectionName", "-"))

        st.subheader("Description")
        st.write(detection.get("Description", "-"))

        st.markdown("---")
        st.subheader("MITRE Tactics")
        st.write(detection.get("Tactics", []))

        st.subheader("MITRE Techniques")
        st.write(detection.get("Techniques", []))

        st.markdown("---")
        st.subheader("Generated KQL")
        st.code(detection.get("Query", ""), language="sql")

        if "KQLReview" in detection:
            st.markdown("---")
            st.subheader("KQL Review")
            st.json(detection["KQLReview"])

        st.markdown("---")
        st.subheader("Knowledge Sources")
        st.write(
            detection.get(
                "_knowledge_sources",
                detection.get("KnowledgeSources", []),
            )
        )

    st.markdown("---")

    c1, c2 = st.columns(2)
    with c1:
        if previous_button():
            current_step = st.session_state.get("step", 0)
            if current_step > 0:
                st.session_state.step = current_step - 1
                st.rerun()

    with c2:
        if next_button():
            current_step = st.session_state.get("step", 0)
            st.session_state.step = current_step + 1
            st.rerun()