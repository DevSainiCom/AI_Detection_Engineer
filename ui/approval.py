"""
Approval Workflow — Human Expert Review Portal
================================================
The human validation layer required by PMI RFP.
Approver sees full detection summary, DREAD score, traceability,
and completes a structured checklist before approving/rejecting.
"""

import streamlit as st

from ui.components import *
from ui.design_system import (
    enterprise_card, metric_row, info_banner,
    checklist, section_divider,
)
from backend.services.approval_workflow_service_v2 import (
    approval_workflow_service,
    REVIEW_CHECKLIST,
)
from backend.services.traceability_service import traceability_service


def render():

    page_setup(
        title="Approval Workflow",
        subtitle="Human expert review and sign-off for AI-generated detections before Sentinel deployment.",
        eyebrow="Deployment · Step 11 of 12",
        agent_name="Human Review Gate",
        agent_desc=(
            "<strong>PMI RFP Requirement:</strong> "
            "'All AI-generated outputs must undergo review and validation by qualified "
            "human experts before being accepted or delivered. The supplier remains fully "
            "accountable for the correctness and quality of deliverables, regardless of AI assistance.' "
            "This portal is the formal gate between AI generation and production deployment."
        ),
    )

    detection = st.session_state.get("detection")
    trace     = st.session_state.get("trace", {})

    if not detection:
        info_banner(
            "No detection available. Complete <strong>AI Detection Generation</strong> first.",
            variant="warning",
        )
        nav_buttons()
        return

    # ── Build review record if not already created ──
    if "review_record" not in st.session_state or st.session_state.review_record is None:
        st.session_state.review_record = approval_workflow_service.create_review_record(
            detection, trace
        )

    record = st.session_state.review_record
    summary = approval_workflow_service.summary_card(record)
    ds = record["detection_summary"]
    tr = record["traceability"]

    # ──────────────────────────────────────────────────────────────
    # Status Banner
    # ──────────────────────────────────────────────────────────────
    status = record["status"]
    variant_map = {
        "Pending Review":                 "warning",
        "Approved — Deploy to Staging":   "success",
        "Approved — Deploy to Production":"success",
        "Needs Tuning":                   "warning",
        "Rejected":                       "warning",
    }
    info_banner(
        f"Review Status: <strong>{status}</strong>  ·  "
        f"Review ID: <code>{record['review_id']}</code>",
        variant=variant_map.get(status, "info"),
    )

    # ──────────────────────────────────────────────────────────────
    # Detection Summary Card
    # ──────────────────────────────────────────────────────────────
    st.markdown("##### Detection Summary")

    m1, m2, m3, m4 = st.columns(4)
    dread_d = ds.get("dread_total", "—")
    dread_r = ds.get("dread_rating", "—")
    sev     = ds.get("alert_severity", ds.get("severity","—"))
    chk_pct = summary["checklist_pct"]

    with m1: metric_card(str(dread_d), "DREAD Score", "red" if dread_r in ("Critical","High") else "amber")
    with m2: metric_card(dread_r,      "Risk Rating",  "red" if dread_r in ("Critical","High") else "amber")
    with m3: metric_card(sev,          "Alert Severity","blue")
    with m4: metric_card(f"{chk_pct}%","Checklist",    "green" if chk_pct == 100 else "amber")

    section_divider()

    d1, d2 = st.columns(2, gap="large")
    with d1:
        enterprise_card("Detection Name", ds["name"],                    "accent-left")
        enterprise_card("MITRE Tactic",   " · ".join(ds["mitre_tactic"]),    "accent-left")
        enterprise_card("MITRE Technique"," · ".join(ds["mitre_technique"]),  "accent-left")
    with d2:
        enterprise_card("Description",    ds["description"],             "accent-left")
        enterprise_card("UC Category",    ds["uc_category"],             "accent-left")
        enterprise_card("KQL Tables",     " · ".join(ds.get("tables_used",["—"])), "accent-left")

    section_divider()

    # ──────────────────────────────────────────────────────────────
    # KQL + Traceability Side by Side
    # ──────────────────────────────────────────────────────────────
    kql_col, trace_col = st.columns([3, 2], gap="large")

    with kql_col:
        st.markdown("##### KQL Query Under Review")
        st.code(ds.get("kql_query", ""), language="sql")

    with trace_col:
        st.markdown("##### Traceability Summary")

        enterprise_card("Trace ID",    tr["trace_id"],  "accent-left")
        enterprise_card("AI Model",    tr["ai_model"],  "accent-left")

        all_ok = tr["all_checks_passed"]
        enterprise_card(
            "Hallucination Checks",
            "✅ All validation checks passed" if all_ok
            else "⚠️ One or more checks need review",
            "accent-success" if all_ok else "accent-warning",
        )

        st.markdown("###### Context Sources Used")
        for src in tr["context_sources"]:
            st.markdown(f"&nbsp;&nbsp;📄 `{src}`")

    section_divider()

    # ──────────────────────────────────────────────────────────────
    # Reviewer Checklist
    # ──────────────────────────────────────────────────────────────
    st.markdown("##### Expert Review Checklist")

    info_banner(
        "Complete all checklist items before approving for deployment. "
        "Each item represents a mandatory validation point per PMI ITPF standards.",
        variant="info",
    )

    checklist_state = record.get("checklist", {k: False for k,_ in REVIEW_CHECKLIST})
    new_checklist   = {}

    cl1, cl2 = st.columns(2, gap="large")
    items = list(REVIEW_CHECKLIST)
    for i, (key, label) in enumerate(items):
        col = cl1 if i < len(items) // 2 else cl2
        with col:
            new_checklist[key] = st.checkbox(
                label,
                value=checklist_state.get(key, False),
                key=f"chk_{key}",
            )

    # Update record
    record["checklist"] = new_checklist
    pct = int(sum(new_checklist.values()) / max(len(new_checklist), 1) * 100)
    st.progress(pct / 100)
    st.caption(f"Checklist: {sum(new_checklist.values())}/{len(new_checklist)} items complete ({pct}%)")

    section_divider()

    # ──────────────────────────────────────────────────────────────
    # Decision Panel
    # ──────────────────────────────────────────────────────────────
    st.markdown("##### Review Decision")

    rev1, rev2 = st.columns(2, gap="large")

    with rev1:
        reviewer = st.text_input(
            "Reviewer Name / Email",
            placeholder="engineer@epam.com",
        )
        new_status = st.selectbox(
            "Decision",
            approval_workflow_service.VALID_STATUS,
        )

    with rev2:
        comments = st.text_area(
            "Comments / Observations",
            height=120,
            placeholder=(
                "e.g. 'KQL logic is correct. Threshold adjusted from 5 to 10 "
                "to reduce FP rate on this application. Approved for staging.'"
            ),
        )
        tuning_request = st.text_input(
            "Tuning Request (if Needs Tuning)",
            placeholder="e.g. Add exclusion for service account svc_monitor",
        )

    section_divider()

    if st.button("✅ Submit Review Decision", use_container_width=True, type="primary"):
        if not reviewer:
            st.error("Please enter reviewer name before submitting.")
            return

        updated = approval_workflow_service.apply_decision(
            record          = record,
            status          = new_status,
            reviewer        = reviewer,
            checklist_items = new_checklist,
            comments        = comments,
            tuning_requests = [tuning_request] if tuning_request else [],
        )

        # Update traceability
        if trace:
            updated_trace = traceability_service.add_review(
                trace    = trace.copy(),
                reviewer = reviewer,
                decision = new_status,
                comments = comments,
            )
            if "Deploy to Staging" in new_status:
                updated_trace = traceability_service.mark_deployed(
                    updated_trace, "staging"
                )
            if "Deploy to Production" in new_status:
                updated_trace = traceability_service.mark_deployed(
                    updated_trace, "production",
                    sentinel_rule_id="sentinel-rule-" + record["review_id"].lower(),
                )
            st.session_state.trace = updated_trace

        st.session_state.review_record  = updated
        st.session_state.review         = updated
        detection["_review"]            = updated
        st.session_state.detection      = detection
        st.rerun()

    # ──────────────────────────────────────────────────────────────
    # Decision History (if decided)
    # ──────────────────────────────────────────────────────────────
    decision = record.get("decision", {})
    if decision.get("reviewer"):
        section_divider()
        st.markdown("##### Decision Record")

        info_banner(
            f"Decision: <strong>{decision['status']}</strong>  ·  "
            f"Reviewer: <strong>{decision['reviewer']}</strong>  ·  "
            f"Timestamp: {str(decision.get('timestamp','—'))[:19]}",
            variant="success" if "Approved" in str(decision.get("status","")) else "warning",
        )

        if decision.get("comments"):
            enterprise_card("Reviewer Comments", decision["comments"], "accent-success")

        if decision.get("tuning_requests"):
            for req in decision["tuning_requests"]:
                if req:
                    enterprise_card("Tuning Request", req, "accent-warning")

        # Deployment readiness
        dr = record.get("deployment_readiness", {})
        st.markdown("##### Deployment Readiness")

        dep1, dep2 = st.columns(2)
        with dep1:
            metric_card(
                "✅ Ready" if dr.get("staging_ready") else "⏳ Pending",
                "Staging",
                "green" if dr.get("staging_ready") else "amber",
            )
        with dep2:
            metric_card(
                "✅ Ready" if dr.get("production_ready") else "⏳ Pending",
                "Production",
                "green" if dr.get("production_ready") else "amber",
            )

    developer_view(record)
    nav_buttons()
