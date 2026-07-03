"""
Application Analysis Service
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

        log_sources = []

        if authentication.lower() in [
            "active directory",
            "entra id",
            "azure ad",
        ]:

            log_sources.extend([

                "SigninLogs",

                "IdentityLogonEvents",

            ])

        if cloud_provider.lower() == "azure":

            log_sources.append(

                "AzureActivity"

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

            recommended_log_sources=log_sources,

        )


application_analysis_service = ApplicationAnalysisService()