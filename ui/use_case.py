import streamlit as st

from ui.components import *


def render():

    page_header(
        "Detection Planning",
        "Determine the customer-specific context required before AI generates a Microsoft Sentinel detection."
    )

    st.info(
        """
### Detection Planning Agent (Proof of Concept)

This page demonstrates how the Detection Planning Agent analyses
all previously collected onboarding information and determines
what knowledge is required before generating a detection.

The next page will use this plan to retrieve the required
customer context before calling the AI Detection Generation Engine.
"""
    )

    st.markdown("---")

    if st.button(
        "Generate Detection Plan",
        type="primary",
        use_container_width=True,
    ):

        threat = st.session_state.threat_model or {}
        application = st.session_state.application
        coverage = st.session_state.gap_analysis
        context = st.session_state.detection_context
        validation = st.session_state.validation

        plan = {

            "executive_summary":

                (
                    "The Detection Planning Agent has analysed the "
                    "customer onboarding information and determined "
                    "the knowledge required to generate a high-quality "
                    "Microsoft Sentinel detection."
                ),

            "detection_request":[

                "Business Threat Model",

                "Application Architecture",

                "Telemetry Validation",

                "Parser Context",

                "Detection Objectives",

            ],

            "required_context":[

                "Threat Model",

                "Application Analysis",

                "Coverage Analysis",

                "Detection Context",

                "Telemetry Analysis",

                "Telemetry Validation",

                "MITRE ATT&CK",

                "Detection Standards",

            ],

            "retrieval_plan":[

                "Business Context",

                "Critical Assets",

                "Authentication Model",

                "Technology Stack",

                "Parser Documentation",

                "Normalization Rules",

                "Available Entities",

                "MITRE Techniques",

                "Detection Library",

            ],

            "detection_strategy":[

                "Generate customer-specific Microsoft Sentinel detection",

                "Map to MITRE ATT&CK",

                "Use validated telemetry only",

                "Optimise for low false positives",

                "Generate documentation",

            ],

            "knowledge_generated":[

                "Detection Request",

                "Retrieval Plan",

                "Required Context",

                "Detection Strategy",

                "Knowledge Sources",

            ],

            "impact":

                (
                    "The Detection Planning Agent has determined "
                    "what knowledge must be retrieved before AI "
                    "generation begins. The Context Retrieval Agent "
                    "will now retrieve only the relevant customer "
                    "knowledge before the Detection Generation Engine "
                    "creates the Microsoft Sentinel detection."
                ),

        }

        st.session_state.use_case = plan

    # ----------------------------------------------------------
    # Display Planning Result
    # ----------------------------------------------------------

    if st.session_state.use_case is not None:

        plan = st.session_state.use_case

        st.success(
            "Detection plan generated successfully."
        )

        st.markdown("---")

        st.subheader("Executive Summary")

        st.info(plan["executive_summary"])

        st.markdown("---")

        st.subheader("Detection Request")

        for item in plan["detection_request"]:

            st.markdown(f"• {item}")

        st.markdown("---")

        st.subheader("Required Knowledge")

        for item in plan["required_context"]:

            st.markdown(f"✅ {item}")

        st.markdown("---")

        st.subheader("Context Retrieval Plan")

        for item in plan["retrieval_plan"]:

            st.markdown(f"📚 {item}")

        st.markdown("---")

        st.subheader("Detection Strategy")

        for item in plan["detection_strategy"]:

            st.markdown(f"🛡️ {item}")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        for item in plan["knowledge_generated"]:

            st.markdown(f"✔ {item}")

        st.markdown("---")

        st.subheader("Detection Engineering Impact")

        st.info(
            plan["impact"]
        )

        st.markdown("---")

        st.success(
            """
The Detection Planning phase is now complete.

The next stage will invoke the **Context Retrieval Agent**
to collect the required customer knowledge before
calling the AI Detection Generation Engine.
"""
        )

        with st.expander("Developer View"):

            st.json(plan)

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        if previous_button():

            st.session_state.step -= 1

            st.rerun()

    with c2:

        if next_button():

            st.session_state.step += 1

            st.rerun()