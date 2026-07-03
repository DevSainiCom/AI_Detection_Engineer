import json
import streamlit as st

from backend.schemas.detection_request import DetectionRequest
from backend.services.detection_service import detection_service

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="AI Detection Engineer",
    page_icon="🛡️",
    layout="wide",
)

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.title("🛡️ AI Detection Engineer")
st.caption(
    "AI-Powered Microsoft Sentinel Detection Engineering Assistant"
)

# ----------------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Platform",
        "Sentinel"
    )

with col2:
    st.metric(
        "Model",
        "GPT-5-mini"
    )

with col3:
    st.metric(
        "Knowledge",
        "6 Docs"
    )

with col4:
    st.metric(
        "Status",
        "🟢 Ready"
    )

st.divider()

# ----------------------------------------------------------
# User Input
# ----------------------------------------------------------

attack_description = st.text_area(
    "Describe the attack",
    height=170,
    placeholder="""
Examples

• Detect Kerberoasting using Event ID 4769

• Detect Password Spray against Azure AD

• Detect PowerShell downloading payloads

• Detect Golden Ticket attacks
"""
)

generate = st.button(
    "🚀 Generate Detection",
    use_container_width=True,
)

# ----------------------------------------------------------
# Detection Generation
# ----------------------------------------------------------

if generate:

    if not attack_description.strip():

        st.warning(
            "Please enter an attack description."
        )

        st.stop()

    request = DetectionRequest(
        attack_description=attack_description
    )

    with st.spinner(
        "🧠 Understanding attack...\n\nGenerating KQL...\n\nMapping MITRE ATT&CK...\n\nBuilding Sentinel Analytics Rule..."
    ):

        detection = detection_service.generate_detection(
            request
        )

    st.success(
        "Microsoft Sentinel Detection generated successfully."
    )

    # ------------------------------------------------------
    # Detection Summary
    # ------------------------------------------------------

    st.divider()

    st.header("📋 Detection Summary")

    c1, c2, c3 = st.columns(3)

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
            "Platform",
            detection.get(
                "Product",
                "Sentinel"
            )
        )

        st.metric(
            "Status",
            detection.get(
                "Status",
                "-"
            )
        )

    with c3:

        st.metric(
            "Version",
            detection.get(
                "Version",
                "-"
            )
        )

        st.metric(
            "Author",
            detection.get(
                "Author",
                "-"
            )
        )

    st.subheader(
        detection.get(
            "DetectionName",
            "Unknown Detection"
        )
    )

    st.write(
        detection.get(
            "Description",
            ""
        )
    )

    # ------------------------------------------------------
    # Tabs
    # ------------------------------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "💻 KQL",
            "📄 JSON",
            "🎯 MITRE",
            "📚 Knowledge"
        ]
    )

    # ------------------------------------------------------
    # KQL
    # ------------------------------------------------------

    with tab1:

        st.code(
            detection.get(
                "Query",
                ""
            ),
            language="sql",
        )

    # ------------------------------------------------------
    # JSON
    # ------------------------------------------------------

    with tab2:

        st.json(
            detection
        )

    # ------------------------------------------------------
    # MITRE
    # ------------------------------------------------------

    with tab3:

        st.write("### Tactics")

        for tactic in detection.get(
            "Tactics",
            []
        ):

            st.write(f"• {tactic}")

        st.write("### Techniques")

        for technique in detection.get(
            "Techniques",
            []
        ):

            st.write(f"• {technique}")

    # ------------------------------------------------------
    # Knowledge
    # ------------------------------------------------------

    with tab4:

        sources = detection.get(
            "_knowledge_sources",
            []
        )

        if sources:

            st.success(
                "Knowledge used during generation"
            )

            for source in sources:

                st.write(f"✅ {source}")

        else:

            st.info(
                "No knowledge documents matched."
            )

    # ------------------------------------------------------
    # Download
    # ------------------------------------------------------

    st.download_button(
        "⬇ Download Sentinel Detection",
        data=json.dumps(
            detection,
            indent=4,
        ),
        file_name="sentinel_detection.json",
        mime="application/json",
        use_container_width=True,
    )

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.title("🛡️ Project")

st.sidebar.success(
    "Backend Status\n\n🟢 Running"
)

st.sidebar.info(
"""
### AI Detection Engineer

Version

0.1 MVP

Platform

Microsoft Sentinel

Model

GPT-5-mini

Knowledge Base

6 Documents

Architecture

RAG Lite
"""
)

st.sidebar.divider()

st.sidebar.subheader("🚀 Roadmap")

st.sidebar.checkbox(
    "AI Detection Generation",
    value=True,
    disabled=True,
)

st.sidebar.checkbox(
    "Streamlit UI",
    value=True,
    disabled=True,
)

st.sidebar.checkbox(
    "Knowledge Retrieval (RAG Lite)",
    value=True,
    disabled=True,
)

st.sidebar.checkbox(
    "Detection Review",
    value=False,
    disabled=True,
)

st.sidebar.checkbox(
    "Docker",
    value=False,
    disabled=True,
)

st.sidebar.checkbox(
    "Azure Deployment",
    value=False,
    disabled=True,
)