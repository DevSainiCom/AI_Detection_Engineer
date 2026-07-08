import streamlit as st

from ui.components import *


def render():

    page_header(
        "Threat Model",
        "Describe the application's threat landscape and business risk."
    )

    # ----------------------------------------------------------
    # POC Banner
    # ----------------------------------------------------------

    st.info("""
## 🚀 AI Threat Modeling Agent (Proof of Concept)

This module demonstrates the planned AI-powered Threat Modeling capability.

**Current POC**
- The assessment below is generated using rule-based logic to demonstrate the future user experience.
- Your inputs are used to personalise the generated assessment.

**Future Platform**
- AI will automatically analyse uploaded Threat Models, Architecture Diagrams,
  Security Documents, Microsoft Threat Modeling Tool exports, Data Flow Diagrams,
  Security Assessments and related documentation.

The report below represents the planned output of the future AI Threat Modeling Agent.
""")

    # ----------------------------------------------------------
    # Session
    # ----------------------------------------------------------

    if "threat_model_completed" not in st.session_state:
        st.session_state.threat_model_completed = False

    # ----------------------------------------------------------
    # Input Form
    # ----------------------------------------------------------

    model = {

        "ApplicationName":

        st.text_input(
            "Application Name",
            placeholder="e.g. Online Banking Portal",
        ),

        "BusinessFunction":

        st.text_input(
            "Business Function",
            placeholder="e.g. Retail Banking",
        ),

        "ThreatActor":

        st.selectbox(
            "Threat Actor",
            [
                "Cyber Criminal",
                "APT",
                "Insider",
                "Hacktivist",
            ],
            index=None,
            placeholder="Select Threat Actor",
        ),

        "Criticality":

        st.selectbox(
            "Business Criticality",
            [
                "Low",
                "Medium",
                "High",
                "Critical",
            ],
            index=None,
            placeholder="Select Business Criticality",
        ),

        "AttackDescription":

        st.text_area(
            "Attack Description",
            height=220,
            placeholder="""
Example:

The application is Internet-facing and processes customer financial transactions.

Primary concerns include:

- Password Spraying
- Credential Theft
- Account Takeover
- API Abuse
- Privilege Escalation
- Session Hijacking
""",
        ),
    }

    st.session_state.threat_model = model

    st.markdown("---")

    # ----------------------------------------------------------
    # Generate Button
    # ----------------------------------------------------------

    if not st.session_state.threat_model_completed:

        if st.button(
            "🚀 Generate Threat Assessment",
            use_container_width=True,
            type="primary",
        ):

            with st.spinner("Analysing threat model..."):

                import time

                time.sleep(2)

            st.session_state.threat_model_completed = True

            st.rerun()

    # ----------------------------------------------------------
    # Threat Assessment
    # ----------------------------------------------------------

    if st.session_state.threat_model_completed:

        risk = model["Criticality"] or "Medium"

        application = (
            model["ApplicationName"]
            if model["ApplicationName"]
            else "the application"
        )

        business = (
            model["BusinessFunction"]
            if model["BusinessFunction"]
            else "the business service"
        )

        actor = (
            model["ThreatActor"]
            if model["ThreatActor"]
            else "identified threat actors"
        )

        st.success("Threat Assessment generated successfully.")

        st.markdown("---")

        st.subheader("Executive Summary")

        st.info(
            f"""
The submitted threat model indicates that **{application}**
supports **{business}** and is primarily exposed to
activities associated with **{actor}**.

Based on the supplied business context, attack description
and business criticality, the application has been assessed
as **{risk} Risk**.

The identified threats, business context and recommended
monitoring priorities will become part of the customer's
Security Knowledge Base and will be referenced by future
Detection Planning and Microsoft Sentinel Detection Generation.
"""
        )

        st.markdown("---")

        st.subheader("Business Context")

        st.table(
            {
                "Attribute": [
                    "Application",
                    "Business Function",
                    "Threat Actor",
                    "Business Criticality",
                ],
                "Value": [
                    application,
                    business,
                    actor,
                    risk,
                ],
            }
        )

        st.markdown("---")

        st.subheader("Threat Landscape")

        st.markdown("""
### Primary Threat Categories

- Credential Theft
- Password Spraying
- Account Takeover
- Public Facing Application Exploitation
- API Abuse
- Privilege Escalation
- Service Account Abuse
- Insider Threat
""")

        st.markdown("---")

        st.subheader("Critical Assets")

        st.markdown("""
- Customer Accounts
- Authentication Services
- Application APIs
- Business Data
- Identity Platform
- Privileged Accounts
- Financial Information
""")

        st.markdown("---")

        st.subheader("Relevant MITRE ATT&CK Techniques")

        st.table(
            {
                "Technique": [
                    "T1078",
                    "T1110",
                    "T1190",
                    "T1098",
                    "T1021",
                ],
                "Description": [
                    "Valid Accounts",
                    "Password Guessing",
                    "Public Facing Application",
                    "Account Manipulation",
                    "Remote Services",
                ],
                "Priority": [
                    "Critical",
                    "Critical",
                    "High",
                    "High",
                    "Medium",
                ],
            }
        )
        st.markdown("---")

        st.subheader("Recommended Detection Priorities")

        st.markdown("""
1. Password Spray Detection

2. Impossible Travel

3. Suspicious Authentication

4. Privileged Account Monitoring

5. Service Account Abuse

6. Administrative Activity Monitoring

7. OAuth Abuse Detection

8. API Abuse Detection
""")

        st.markdown("---")

        st.subheader("SOC Recommendations")

        st.markdown("""
- Enable comprehensive identity monitoring.
- Collect authentication and administrative logs.
- Enable Microsoft Sentinel analytics for privileged accounts.
- Correlate authentication events with application activity.
- Monitor service accounts and privileged identities.
- Continuously review business-critical assets.
- Validate logging coverage across the application landscape.
""")

        st.markdown("---")

        st.subheader("Knowledge Generated")

        st.success("""
The following knowledge has been generated and will be available for future Detection Engineering:

✅ Business Context

✅ Business Criticality

✅ Threat Actor Profile

✅ Threat Landscape

✅ Critical Assets

✅ MITRE ATT&CK Mapping

✅ Detection Priorities

✅ Monitoring Recommendations

✅ Security Context
""")

        st.markdown("---")

        st.subheader("Detection Engineering Impact")

        st.info(f"""
The assessment for **{application}** has established the initial security context for this application.

Future Detection Generation will automatically consider:

• Application business context

• Threat actor profile

• Business criticality

• Critical assets

• Relevant MITRE ATT&CK techniques

• Detection priorities

• Recommended monitoring strategy

This enables customer-specific Microsoft Sentinel detections instead of generic analytics.
""")

        st.markdown("---")

        st.subheader("Executive Assessment")

        st.success(f"""
Overall Risk Rating: **{risk}**

Based on the submitted information, this application should be prioritised
for continuous monitoring due to its business importance and exposure to
identity-focused attack techniques.

The generated assessment will become one of the core knowledge sources
used throughout the Detection Engineering lifecycle.
""")

        st.markdown("---")

        st.success("✅ Threat Model Assessment completed successfully.")

        st.info(
            "Click **Continue** to proceed to **Application Analysis**."
        )

        col1, col2 = st.columns(2)

        with col2:

            if st.button(
                "Continue to Application Analysis ➜",
                use_container_width=True,
                type="primary",
            ):

                st.session_state.step += 1
                st.rerun()