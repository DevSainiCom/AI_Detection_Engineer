"""
Application Analysis Service

This service performs a rule-based application analysis for the POC.

Future versions will replace this logic with an AI-powered
Application Analysis Agent while keeping the same output model.
"""

from backend.models.application_analysis import ApplicationAnalysis


class ApplicationAnalysisService:

    def analyze(
        self,
        application_name: str,
        application_type: str,
        business_function: str,
        authentication: str,
        cloud_provider: str,
        technology_stack: list[str],
        business_criticality: str,
        data_classification: str,
    ) -> ApplicationAnalysis:

        # ==========================================================
        # Handle Missing Values
        # ==========================================================

        application_name = application_name or "Unknown Application"
        application_type = application_type or "Unknown"
        business_function = business_function or "Not Specified"
        authentication = authentication or "Unknown"
        cloud_provider = cloud_provider or "Unknown"
        business_criticality = business_criticality or "Medium"
        data_classification = data_classification or "Internal"
        technology_stack = technology_stack or []

        auth = authentication.lower()
        cloud = cloud_provider.lower()
        criticality = business_criticality.lower()

        # ==========================================================
        # Determine Expected Log Sources
        # ==========================================================

        log_sources = []

        if auth in [
            "active directory",
            "entra id",
            "azure ad",
            "oauth",
        ]:
            log_sources.extend(
                [
                    "SigninLogs",
                    "AuditLogs",
                    "IdentityLogonEvents",
                ]
            )

        if cloud == "azure":
            log_sources.extend(
                [
                    "AzureActivity",
                    "AzureDiagnostics",
                    "AzureAD",
                    "KeyVault",
                ]
            )

        if cloud == "aws":
            log_sources.extend(
                [
                    "CloudTrail",
                    "CloudWatch",
                ]
            )

        if cloud == "gcp":
            log_sources.extend(
                [
                    "Cloud Audit Logs",
                    "Cloud Logging",
                ]
            )

        log_sources = sorted(list(set(log_sources)))

        # ==========================================================
        # Security Rating
        # ==========================================================

        if criticality in ["critical", "high"]:
            security_rating = "High"

        elif criticality == "medium":
            security_rating = "Medium"

        else:
            security_rating = "Low"

        # ==========================================================
        # Executive Summary
        # ==========================================================

        executive_summary = (
            f"The application '{application_name}' has been analysed "
            f"as a {application_type} application supporting "
            f"'{business_function}'. The application is hosted on "
            f"{cloud_provider} using {authentication} authentication. "
            f"Based on the supplied information, the overall security "
            f"risk has been assessed as {security_rating}."
        )

        # ==========================================================
        # Architecture Summary
        # ==========================================================

        architecture_summary = (
            f"The application is deployed within a "
            f"{cloud_provider} environment using "
            f"{authentication} for authentication. "
            f"The identified technology stack includes: "
            f"{', '.join(technology_stack) if technology_stack else 'Not Specified'}."
        )

        # ==========================================================
        # Security Observations
        # ==========================================================

        observations = [
            "Authentication should be continuously monitored.",
            "Privileged account activity should be audited.",
            "Business critical applications require enhanced monitoring.",
            "Application activity should be correlated with identity events.",
            "Administrative actions should generate alerts.",
        ]

        # ==========================================================
        # Recommended Detection Use Cases
        # ==========================================================

        detections = [
            "Password Spray Detection",
            "Impossible Travel",
            "Suspicious Authentication",
            "Privilege Escalation",
            "Service Account Abuse",
            "Unauthorized Administrative Activity",
            "Impossible Location Login",
            "Multiple Failed Login Attempts",
        ]

        # ==========================================================
        # Critical Assets
        # ==========================================================

        assets = [
            "Authentication Service",
            "Application Server",
            "User Accounts",
            "Business Data",
        ]

        if cloud == "azure":
            assets.extend(
                [
                    "Azure Key Vault",
                    "Azure Storage",
                ]
            )

        # ==========================================================
        # Trust Boundaries
        # ==========================================================

        trust_boundaries = [
            "Internet",
            "Identity Provider",
            "Application",
            "Database",
        ]

        # ==========================================================
        # Knowledge Generated
        # ==========================================================

        knowledge = [
            "Application Metadata",
            "Authentication Model",
            "Technology Stack",
            "Business Criticality",
            "Cloud Platform",
            "Expected Log Sources",
            "Critical Assets",
            "Trust Boundaries",
            "Detection Priorities",
        ]

        # ==========================================================
        # Future AI Usage
        # ==========================================================

        future_usage = (
            "This analysis will become part of the customer's "
            "security knowledge base. Future Detection Planning "
            "will automatically reference the application's "
            "architecture, authentication model, technology stack, "
            "critical assets and expected telemetry to generate "
            "customer-specific Microsoft Sentinel detections instead "
            "of generic templates."
        )

        return ApplicationAnalysis(

            application_name=application_name,

            application_type=application_type,

            business_function=business_function,

            internet_facing=True,

            authentication=authentication,

            cloud_provider=cloud_provider,

            hosting_environment="Cloud",

            business_criticality=business_criticality,

            data_classification=data_classification,

            technology_stack=technology_stack,

            executive_summary=executive_summary,

            security_rating=security_rating,

            architecture_summary=architecture_summary,

            security_observations=observations,

            recommended_log_sources=log_sources,

            recommended_detection_use_cases=detections,

            critical_assets=assets,

            trust_boundaries=trust_boundaries,

            knowledge_generated=knowledge,

            future_ai_usage=future_usage,
        )


application_analysis_service = ApplicationAnalysisService()