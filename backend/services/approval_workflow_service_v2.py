"""
Approval Workflow Service — v2
================================
Human review and approval layer for AI-generated detections.
Implements the PMI requirement: "All AI-generated outputs must undergo
review and validation by qualified human experts before being accepted."
"""

from datetime import datetime, timezone


VALID_STATUS = [
    "Pending Review",
    "Approved — Deploy to Staging",
    "Approved — Deploy to Production",
    "Needs Tuning",
    "Rejected",
]

REVIEW_CHECKLIST = [
    ("kql_logic_correct",     "KQL logic correctly detects the defined behaviour"),
    ("mitre_mapping_correct", "MITRE tactic/technique mapping is accurate"),
    ("dread_score_agreed",    "DREAD score and alert severity agreed"),
    ("entities_validated",    "Entity mapping and field references are valid"),
    ("whitelist_adequate",    "Whitelist / exclusions are sufficient"),
    ("fp_risk_acceptable",    "False positive risk is acceptable"),
    ("alert_routing_correct", "ITSM routing and alert severity are correct"),
    ("test_results_reviewed", "Test results reviewed and accepted"),
]


class ApprovalWorkflowService:

    VALID_STATUS = VALID_STATUS
    REVIEW_CHECKLIST = REVIEW_CHECKLIST

    def create_review_record(self, detection: dict, trace: dict) -> dict:
        """
        Create a structured review record for approver portal.
        Combines detection summary + trace + checklist.
        """
        dread = detection.get("DREADScore", {})
        return {
            "review_id":  "REV-" + detection.get("DetectionName","UC")[:8].upper().replace(" ","-"),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status":     "Pending Review",

            "detection_summary": {
                "name":           detection.get("DetectionName", "—"),
                "description":    detection.get("Description", "—"),
                "severity":       detection.get("Severity", "—"),
                "uc_category":    detection.get("UCCategory", "—"),
                "mitre_tactic":   detection.get("Tactics", []),
                "mitre_technique":detection.get("Techniques", []),
                "dread_total":    dread.get("Total", "—"),
                "dread_rating":   dread.get("Rating", "—"),
                "alert_severity": dread.get("AlertSeverity", "—"),
                "kql_query":      detection.get("Query", ""),
                "tables_used":    detection.get("TablesUsed", []),
                "entity_mapping": detection.get("EntityMappings", []),
            },

            "traceability": {
                "trace_id":        trace.get("trace_id", "—"),
                "ai_model":        trace.get("ai_generation", {}).get("model", "—"),
                "context_sources": trace.get("ai_generation", {}).get("context_sources", []),
                "all_checks_passed": trace.get("quality_checks", {}).get("all_checks_passed", False),
            },

            "checklist": {k: False for k, _ in REVIEW_CHECKLIST},

            "decision": {
                "status":         "Pending Review",
                "reviewer":       None,
                "timestamp":      None,
                "comments":       "",
                "tuning_requests":[],
            },

            "deployment_readiness": {
                "staging_ready":    False,
                "production_ready": False,
                "stability_period_end": None,
            },
        }

    def apply_decision(
        self,
        record: dict,
        status: str,
        reviewer: str,
        checklist_items: dict,
        comments: str = "",
        tuning_requests: list = None,
    ) -> dict:
        record["status"]                      = status
        record["decision"]["status"]          = status
        record["decision"]["reviewer"]        = reviewer
        record["decision"]["timestamp"]       = datetime.now(timezone.utc).isoformat()
        record["decision"]["comments"]        = comments
        record["decision"]["tuning_requests"] = tuning_requests or []
        record["checklist"]                   = checklist_items

        if status == "Approved — Deploy to Staging":
            record["deployment_readiness"]["staging_ready"] = True
        elif status == "Approved — Deploy to Production":
            record["deployment_readiness"]["staging_ready"]    = True
            record["deployment_readiness"]["production_ready"] = True

        return record

    def checklist_complete(self, record: dict) -> bool:
        return all(record.get("checklist", {}).values())

    def summary_card(self, record: dict) -> dict:
        """Return the compact summary shown in the approver portal card."""
        ds = record["detection_summary"]
        return {
            "name":         ds["name"],
            "severity":     ds["severity"],
            "dread":        f"{ds['dread_total']} ({ds['dread_rating']})",
            "mitre":        " · ".join(ds["mitre_technique"]),
            "status":       record["status"],
            "checks_ok":    record["traceability"]["all_checks_passed"],
            "checklist_pct":int(
                sum(record["checklist"].values()) /
                max(len(record["checklist"]), 1) * 100
            ),
        }


approval_workflow_service = ApprovalWorkflowService()
