"""
Gap Analysis Service

Rule-based implementation for the POC.

Future versions will compare:

- Threat Model
- Application Analysis
- Existing Detections
- MITRE Coverage
- Log Sources

using AI reasoning.
"""

from backend.models.gap_analysis import GapAnalysis


class GapAnalysisService:

    def analyze(self, application):

        coverage = 72

        maturity = "Intermediate"

        observations = [
            "Identity monitoring is partially implemented.",
            "Cloud monitoring should be expanded.",
            "Business critical assets require additional analytics.",
            "Authentication events should be correlated with administrative actions.",
        ]

        missing_logs = []

        if "SigninLogs" not in application.recommended_log_sources:
            missing_logs.append("SigninLogs")

        if "AuditLogs" not in application.recommended_log_sources:
            missing_logs.append("AuditLogs")

        if application.cloud_provider == "Azure":
            missing_logs.extend(
                [
                    "AzureDiagnostics",
                    "KeyVault",
                    "AzureFirewall",
                ]
            )

        detections = [
            "Password Spray",
            "Impossible Travel",
            "Privilege Escalation",
            "Service Account Abuse",
            "OAuth Consent Abuse",
            "Administrative Activity Monitoring",
        ]

        mitre = [
            "T1078",
            "T1110",
            "T1098",
            "T1556",
            "T1484",
        ]

        recommendations = [
            "Enable all recommended Microsoft Sentinel connectors.",
            "Improve privileged account monitoring.",
            "Increase authentication visibility.",
            "Deploy high priority identity detections.",
            "Expand cloud workload monitoring.",
        ]

        roadmap = [
            "Identity Monitoring",
            "Privilege Escalation Detection",
            "Cloud Monitoring",
            "API Monitoring",
            "Insider Threat Analytics",
        ]

        knowledge = [
            "Coverage Score",
            "Security Maturity",
            "Missing Log Sources",
            "Missing Detection Opportunities",
            "Missing MITRE Coverage",
            "SOC Recommendations",
            "Detection Roadmap",
        ]

        future = (
            "Future Detection Planning will automatically reference "
            "these identified gaps when generating Microsoft Sentinel "
            "detections to prioritise the customer's highest risks."
        )

        summary = (
            "Current monitoring provides reasonable visibility into "
            "identity-based attacks but additional detections are "
            "recommended for privileged access, cloud administration "
            "and service account monitoring."
        )

        return GapAnalysis(

            executive_summary=summary,

            security_maturity=maturity,

            coverage_score=coverage,

            security_observations=observations,

            missing_log_sources=sorted(list(set(missing_logs))),

            missing_detection_use_cases=detections,

            missing_mitre_coverage=mitre,

            recommendations=recommendations,

            detection_roadmap=roadmap,

            knowledge_generated=knowledge,

            future_ai_usage=future,
        )


gap_analysis_service = GapAnalysisService()