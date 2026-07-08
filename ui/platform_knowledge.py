"""
Platform Knowledge
==================
Architecture, AI Agents, Knowledge Base, Roadmap, Version History.
Accessible from the sidebar — not part of the workflow.
"""

import streamlit as st
from ui.design_system import (
    inject_css,
    enterprise_banner,
    page_header,
    enterprise_card,
    metric_row,
    info_banner,
    section_divider,
)


def render():
    inject_css()
    enterprise_banner()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏗️ Architecture",
        "🤖 AI Agents",
        "📚 Knowledge Base",
        "🗺️ Roadmap",
        "📝 Version History",
    ])

    # ──────────────────────────────────────────────────────────
    # Architecture
    # ──────────────────────────────────────────────────────────

    with tab1:
        st.subheader("Platform Architecture")

        info_banner(
            "The AI Detection Engineering Platform uses a multi-agent "
            "architecture to automate the full detection lifecycle for "
            "Microsoft Sentinel.",
        )

        st.markdown("### Detection Lifecycle")

        st.code("""
Customer Onboarding
        │
        ├── Threat Model
        ├── Application Analysis
        ├── Coverage Analysis
        ├── Detection Context
        ├── Telemetry Analysis
        └── Telemetry Validation
                │
                ▼
    Knowledge Manager  ◄──►  Vector Database
                │
                ▼
Detection Engineering
        │
        ├── Detection Planning Agent
        ├── Context Retrieval Agent
        ├── Prompt Builder
        ├── Azure OpenAI (GPT)
        ├── Detection Review Agent
        └── MITRE Mapping Agent
                │
                ▼
    Deployment
        │
        ├── Approval Workflow
        └── Deployment Package
                │
                ▼
    Microsoft Sentinel
        """, language="text")

        section_divider()

        st.markdown("### Technology Stack")

        col1, col2 = st.columns(2)

        with col1:
            enterprise_card("Frontend", "Streamlit · Python 3.13")
            enterprise_card("AI Engine", "Azure OpenAI · GPT-4o")
            enterprise_card("Knowledge", "RAG · Markdown Knowledge Base")

        with col2:
            enterprise_card("Target SIEM", "Microsoft Sentinel")
            enterprise_card("Framework", "MITRE ATT&CK Enterprise")
            enterprise_card("Query Language", "KQL (Kusto Query Language)")

    # ──────────────────────────────────────────────────────────
    # AI Agents
    # ──────────────────────────────────────────────────────────

    with tab2:
        st.subheader("Multi-Agent Architecture")

        info_banner(
            "Each agent is responsible for one stage of the detection "
            "engineering lifecycle. Agents marked as <strong>Implemented</strong> "
            "use rule-based logic in this POC and will be replaced with "
            "AI-powered agents in production.",
            variant="info",
        )

        agents = [
            ("Threat Modeling Agent", "Analyses and structures threat models", "Rule-Based", "Planned"),
            ("Application Analysis Agent", "Extracts application metadata and security posture", "Rule-Based", "Planned"),
            ("Gap Analysis Agent", "Identifies detection coverage gaps", "Rule-Based", "Planned"),
            ("Detection Context Agent", "Collects telemetry and parser context", "Rule-Based", "Planned"),
            ("Detection Planning Agent", "Determines required context for detection", "Rule-Based", "Planned"),
            ("Context Retrieval Agent", "Retrieves knowledge from RAG", "RAG", "Planned"),
            ("KQL Generation Agent", "Writes Microsoft Sentinel detection queries", "GPT", "Implemented"),
            ("MITRE Mapping Agent", "Maps detections to ATT&CK framework", "GPT", "Implemented"),
            ("Detection Review Agent", "Validates detection quality and accuracy", "Rule-Based", "Implemented"),
            ("Documentation Agent", "Generates detection documentation", "Rule-Based", "Planned"),
            ("Deployment Agent", "Handles Sentinel deployment packaging", "Rule-Based", "Implemented"),
        ]

        for name, purpose, engine, status in agents:
            status_icon = "✅" if status == "Implemented" else "🔲"
            enterprise_card(
                f"{status_icon} {name}",
                f"{purpose}<br/>"
                f"<small style='color:#9ca3af'>Engine: {engine} · Status: {status}</small>",
            )

    # ──────────────────────────────────────────────────────────
    # Knowledge Base
    # ──────────────────────────────────────────────────────────

    with tab3:
        st.subheader("Knowledge Sources")

        info_banner(
            "The platform maintains a structured knowledge base that "
            "feeds the AI detection generation pipeline. Each source "
            "is stored as Markdown and will be indexed for RAG retrieval.",
            variant="info",
        )

        sources = {
            "Threat Intelligence": [
                "Threat Models", "Application Analysis", "MITRE ATT&CK Patterns",
            ],
            "Detection Standards": [
                "Sentinel Detection Guidelines", "KQL Best Practices",
                "Entity Mapping Standards", "False Positive Reduction",
            ],
            "Microsoft Sentinel": [
                "Sentinel Tables Schema", "Analytics Rule Standards",
                "Entity Mapping Reference",
            ],
            "Connector Knowledge": [
                "Microsoft Entra ID", "Defender XDR", "Azure Activity",
                "Windows Security Events", "Office 365", "CEF", "Syslog",
                "AWS CloudTrail", "GCP Audit",
            ],
            "Detection Library": [
                "Password Spray", "Kerberoasting", "Credential Dumping",
                "Privilege Escalation", "Impossible Travel", "MFA Bypass",
                "Ransomware Patterns", "Web Shell Detection", "Data Exfiltration",
            ],
            "Customer Context": [
                "Customer Policies (future)", "Environment Configuration (future)",
                "Existing Detections (future)",
            ],
        }

        for category, items in sources.items():
            with st.expander(f"📁 {category} ({len(items)} sources)"):
                for item in items:
                    st.markdown(f"- {item}")

    # ──────────────────────────────────────────────────────────
    # Roadmap
    # ──────────────────────────────────────────────────────────

    with tab4:
        st.subheader("Development Roadmap")

        phases = [
            (
                "Sprint 1 — Foundation",
                "✅ Complete",
                "green",
                [
                    "Threat Model page",
                    "Application Analysis",
                    "Gap Analysis",
                    "KQL Generation (GPT)",
                    "Basic workflow navigation",
                ],
            ),
            (
                "Sprint 2 — Workflow Redesign",
                "✅ Complete",
                "green",
                [
                    "Detection Context page",
                    "Telemetry Analysis & Validation",
                    "Detection Planning",
                    "Detection Review",
                    "Rename pages to architecture alignment",
                    "Onboarding UX improvements",
                ],
            ),
            (
                "Sprint 3 — Enterprise UI",
                "▶️ In Progress",
                "amber",
                [
                    "Enterprise design system",
                    "Professional sidebar with grouped navigation",
                    "Platform Knowledge portal",
                    "Consistent card and metric components",
                    "Executive-grade presentation",
                ],
            ),
            (
                "Sprint 4 — AI Agents",
                "🔲 Planned",
                "blue",
                [
                    "Replace rule-based agents with GPT-powered agents",
                    "RAG-based context retrieval",
                    "Vector database integration",
                    "Multi-agent orchestration",
                ],
            ),
            (
                "Sprint 5 — Production",
                "🔲 Planned",
                "blue",
                [
                    "Azure deployment",
                    "Sentinel API integration",
                    "ARM template generation",
                    "Multi-tenant support",
                    "Confluence synchronization",
                ],
            ),
        ]

        for title, status, color, items in phases:
            enterprise_card(
                f"{title}  —  {status}",
                "<br/>".join(f"• {item}" for item in items),
            )

    # ──────────────────────────────────────────────────────────
    # Version History
    # ──────────────────────────────────────────────────────────

    with tab5:
        st.subheader("Version History")

        versions = [
            (
                "v0.3 — Enterprise UI & Platform Knowledge",
                "July 2026",
                [
                    "Enterprise design system (CSS, cards, metrics, banners)",
                    "Professional grouped sidebar navigation",
                    "Platform Knowledge portal (Architecture, Agents, KB, Roadmap)",
                    "Consistent page headers and layout",
                    "Executive-grade presentation layer",
                ],
            ),
            (
                "v0.2 — Detection Workflow Redesign",
                "July 2026",
                [
                    "Detection Context page",
                    "Telemetry Analysis & Validation",
                    "Detection Planning Agent (rule-based)",
                    "Detection Review Agent",
                    "Renamed all pages to architecture alignment",
                ],
            ),
            (
                "v0.1 — Initial POC",
                "July 2026",
                [
                    "Threat Model input",
                    "Application Analysis (rule-based)",
                    "Gap Analysis (rule-based)",
                    "KQL Generation via GPT",
                    "Basic export and approval workflow",
                ],
            ),
        ]

        for title, date, changes in versions:
            enterprise_card(
                f"{title}  ·  {date}",
                "<br/>".join(f"• {c}" for c in changes),
            )
