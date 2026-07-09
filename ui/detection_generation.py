"""
AI Detection Generation — with DREAD + Traceability
"""

import streamlit as st

from ui.components import *
from ui.design_system import (
    enterprise_card, metric_row, info_banner,
    checklist, section_divider, arch_context,
)
from backend.core.workflow_engine import workflow_engine
from backend.services.dread_scoring_service import dread_scoring_service
from backend.services.traceability_service import traceability_service


# ── UC Category options ──────────────────────────────────────────────
UC_CATEGORIES = [
    "Compliance Monitoring",
    "Threat Detection",
    "Health Monitoring",
]

MITRE_QUICK = {
    "Password Spray":           ("T1110.003", "Credential Access"),
    "Brute Force":              ("T1110.001", "Credential Access"),
    "MFA Bypass":               ("T1556",    "Credential Access"),
    "Privilege Escalation":     ("T1068",    "Privilege Escalation"),
    "Lateral Movement":         ("T1021",    "Lateral Movement"),
    "Credential Dumping":       ("T1003.001","Credential Access"),
    "Kerberoasting":            ("T1558.003","Credential Access"),
    "Ransomware":               ("T1486",    "Impact"),
    "C2 Beacon":                ("T1071",    "Command & Control"),
    "Data Exfiltration":        ("T1048",    "Exfiltration"),
    "Web Shell":                ("T1505.003","Persistence"),
    "LOLBins Execution":        ("T1218",    "Defense Evasion"),
    "Account Manipulation":     ("T1098",    "Persistence"),
    "Audit Log Cleared":        ("T1562.002","Defense Evasion"),
    "Suspicious Authentication":("T1078",    "Initial Access"),
}


def render():

    page_setup(
        title="AI Detection Generation",
        subtitle="Generate AI-native Microsoft Sentinel detections with DREAD scoring, MITRE mapping, and full traceability.",
        eyebrow="Detection Engineering · Step 8 of 12",
        agent_name="KQL Generation Agent + MITRE Mapping Agent",
        agent_desc=(
            "Uses RAG-retrieved context from the Knowledge Manager to generate "
            "customer-specific KQL rules via Azure OpenAI GPT-4o. "
            "Every detection is scored with DREAD, mapped to MITRE ATT&CK, "
            "and a full traceability record is created for audit purposes. "
            "<strong>RFP requirement:</strong> AI-mandatory generation with human expert review."
        ),
    )

    # ──────────────────────────────────────────────────────────────
    # Config Panel
    # ──────────────────────────────────────────────────────────────
    st.markdown("##### Detection Configuration")

    cfg1, cfg2, cfg3 = st.columns(3, gap="large")

    with cfg1:
        uc_category = st.selectbox(
            "Use Case Category",
            UC_CATEGORIES,
            index=1,
        )

        threat_selection = st.selectbox(
            "Threat Pattern",
            list(MITRE_QUICK.keys()),
        )
        mitre_technique, mitre_tactic = MITRE_QUICK[threat_selection]

        st.caption(f"Auto-mapped → **{mitre_technique}** · *{mitre_tactic}*")

    with cfg2:
        connector = st.session_state.get("connector")
        if connector and hasattr(connector, "name"):
            connector_name = connector.name
        else:
            connector_name = st.selectbox(
                "Log Source / Connector",
                [
                    "Microsoft Entra ID",
                    "Windows Security Events",
                    "Microsoft Defender XDR",
                    "Azure Activity",
                    "AWS CloudTrail",
                    "Syslog",
                    "Custom Application",
                ],
            )

        data_classification = st.selectbox(
            "Data Classification",
            ["Public", "Internal", "Confidential", "Restricted"],
            index=2,
        )

    with cfg3:
        business_criticality = st.session_state.threat_model.get(
            "Criticality"
        ) or st.selectbox(
            "Business Criticality",
            ["Low", "Medium", "High", "Critical"],
            index=2,
        )

        st.info(
            f"**Criticality from Threat Model:** {business_criticality}"
            if st.session_state.threat_model.get("Criticality")
            else "Set criticality above ↑"
        )

    section_divider()

    # ──────────────────────────────────────────────────────────────
    # DREAD Preview (before generation)
    # ──────────────────────────────────────────────────────────────
    dread = dread_scoring_service.score_use_case(
        uc_name              = threat_selection,
        mitre_technique      = mitre_technique,
        business_criticality = business_criticality,
        uc_category          = uc_category,
        data_classification  = data_classification,
    )

    st.markdown("##### DREAD Score Preview")

    dread_cols = st.columns(6, gap="small")
    dims = [
        ("Damage",          dread.damage),
        ("Reproducibility", dread.reproducibility),
        ("Exploitability",  dread.exploitability),
        ("Affected Users",  dread.affected_users),
        ("Discoverability", dread.discoverability),
        ("TOTAL",           round(dread.total, 1)),
    ]
    colors = ["red","amber","amber","red","amber","blue"]
    for col, (label, val), color in zip(dread_cols, dims, colors):
        with col:
            from ui.design_system import metric_card
            metric_card(str(val), label, color)

    st.markdown(
        f"**Risk Rating: {dread.rating}**  ·  "
        f"Alert Severity → **{dread.alert_severity}**"
    )

    section_divider()

    # ──────────────────────────────────────────────────────────────
    # Generate Button
    # ──────────────────────────────────────────────────────────────
    if st.button("🚀 Generate Detection", use_container_width=True, type="primary"):
        with st.spinner("Running AI Detection Generation pipeline..."):

            attack_description = (
                st.session_state.threat_model.get("AttackDescription")
                or threat_selection
            )

            result = workflow_engine.execute(
                attack_description   = attack_description,
                connector_name       = connector_name,
                sample_logs          = st.session_state.get("sample_logs", []),
                threat_model         = st.session_state.get("threat_model", {}),
                application_analysis = st.session_state.get("application", {}),
                questionnaire        = st.session_state.get("questionnaire", {}),
            )

            # Enrich with DREAD
            result["DREADScore"]     = dread.to_dict()
            result["UCCategory"]     = uc_category
            result["MITREAutoMap"]   = {
                "Technique": mitre_technique,
                "Tactic":    mitre_tactic,
            }

            # Build traceability
            context_sources = traceability_service.build_context_sources(
                connector_name   = connector_name,
                uc_category      = uc_category,
                mitre_technique  = mitre_technique,
                has_sample_logs  = bool(st.session_state.get("sample_logs")),
            )

            kql_validation = traceability_service.validate_kql(
                kql             = result.get("Query", ""),
                expected_tables = result.get("TablesUsed", [connector_name.replace(" ","")]),
            )

            trace = traceability_service.create_trace(
                uc_name              = result.get("DetectionName", threat_selection),
                uc_category          = uc_category,
                application_name     = st.session_state.threat_model.get("ApplicationName","Unknown"),
                mitre_technique      = mitre_technique,
                context_sources      = context_sources,
                prompt_summary       = f"Generate Sentinel detection for {threat_selection} on {connector_name}",
                kql_query            = result.get("Query", ""),
                dread_score          = dread.to_dict(),
                hallucination_checks = kql_validation,
            )

            result["_trace"]  = trace
            result["_dread"]  = dread.to_dict()

            st.session_state.detection = result
            st.session_state.trace     = trace

        success("✅ Detection generated. Review below.")

    # ──────────────────────────────────────────────────────────────
    # Results
    # ──────────────────────────────────────────────────────────────
    detection = st.session_state.get("detection")
    if not detection:
        return

    trace = st.session_state.get("trace", {})

    section_divider()

    # ── Summary Metrics ──
    st.markdown("##### Detection Summary")

    d_dread = detection.get("DREADScore", dread.to_dict())
    metric_row([
        {"value": d_dread.get("Rating", "—"),        "label": "DREAD Rating",    "color": "red"},
        {"value": str(d_dread.get("Total","—")),      "label": "DREAD Score",     "color": "amber"},
        {"value": detection.get("Severity","—"),      "label": "Alert Severity",  "color": "blue"},
        {"value": detection.get("RiskScore","—"),     "label": "Risk Score",      "color": "purple"},
    ])

    section_divider()

    # ── Detection Info ──
    c1, c2 = st.columns(2, gap="large")
    with c1:
        enterprise_card("Detection Name",  detection.get("DetectionName","-"), "accent-left")
        enterprise_card("UC Category",     detection.get("UCCategory","-"),    "accent-left")
        enterprise_card("MITRE Tactic",    " · ".join(detection.get("Tactics",[])), "accent-left")
        enterprise_card("MITRE Technique", " · ".join(detection.get("Techniques",[])), "accent-left")
    with c2:
        enterprise_card("Description", detection.get("Description","-"), "accent-left")
        enterprise_card("Connector",   connector_name,                   "accent-left")
        enterprise_card("Status",      detection.get("Status","Draft"),  "accent-left")
        enterprise_card("Version",     detection.get("Version","1.0"),   "accent-left")

    section_divider()

    # ── DREAD Full Breakdown ──
    st.markdown("##### DREAD Score Breakdown")

    d = detection.get("DREADScore", {})
    dread_rows = [
        ("Damage",          d.get("Damage","—"),          "How bad if successfully exploited?"),
        ("Reproducibility", d.get("Reproducibility","—"), "How easy to reproduce the attack?"),
        ("Exploitability",  d.get("Exploitability","—"),  "Skill level required to exploit?"),
        ("Affected Users",  d.get("AffectedUsers","—"),   "Number of users/systems affected?"),
        ("Discoverability", d.get("Discoverability","—"), "How easy to discover this vector?"),
    ]
    for dim, val, desc in dread_rows:
        enterprise_card(f"{dim}  —  Score: {val}/10", desc, "accent-left")

    enterprise_card(
        f"Total DREAD: {d.get('Total','—')}  ·  Rating: {d.get('Rating','—')}",
        f"Alert Severity mapped to: **{d.get('AlertSeverity','—')}**",
        "accent-warning" if d.get("Rating") in ("Critical","High") else "accent-success",
    )

    section_divider()

    # ── KQL ──
    st.markdown("##### Generated KQL Query")
    st.code(detection.get("Query",""), language="sql")

    section_divider()

    # ── Traceability ──
    st.markdown("##### Traceability Record")

    info_banner(
        "Full audit trail recorded for this AI-generated detection. "
        "Required by PMI RFP Section 1.2 — explainability and traceability.",
        variant="info",
    )

    if trace:
        t_ai = trace.get("ai_generation", {})
        t_qc = trace.get("quality_checks", {})

        tc1, tc2 = st.columns(2)
        with tc1:
            enterprise_card("Trace ID",     trace.get("trace_id","—"), "accent-left")
            enterprise_card("AI Model",     t_ai.get("model","—"),     "accent-left")
            enterprise_card("Prompt Hash",  t_ai.get("prompt_hash","—")[:20]+"...", "accent-left")
        with tc2:
            enterprise_card("Generated At", trace.get("generated_at","—")[:19], "accent-left")
            enterprise_card("KQL Hash",     trace.get("detection",{}).get("kql_hash","—"), "accent-left")
            all_ok = t_qc.get("all_checks_passed", False)
            enterprise_card(
                "Quality Checks",
                "✅ All checks passed" if all_ok else "⚠️ Review required",
                "accent-success" if all_ok else "accent-warning",
            )

        st.markdown("###### Context Sources Retrieved")
        checklist(t_ai.get("context_sources", []))

        h_checks = t_qc.get("hallucination_validation", {})
        if h_checks:
            st.markdown("###### Hallucination Validation")
            for check, passed in h_checks.items():
                icon = "✅" if passed else "❌"
                st.markdown(f"{icon} `{check}`")

    section_divider()

    info_banner(
        "Detection generated successfully. Proceed to "
        "<strong>Detection Review</strong> for quality scoring, then "
        "<strong>Approval</strong> for the human expert review.",
        variant="success",
    )

    developer_view(detection)
    nav_buttons()
