"""
AI Gap Analysis Service
"""


class GapAnalysisService:

    def analyze(

        self,

        application,

    ):

        gaps = []

        recommendations = []

        if not application.recommended_log_sources:

            gaps.append(

                "No recommended log sources identified."

            )

        if application.authentication == "Unknown":

            gaps.append(

                "Authentication mechanism not identified."

            )

        if application.business_criticality == "Critical":

            recommendations.append(

                "Enable high fidelity detections."

            )

        recommendations.append(

            "Validate connector health."

        )

        recommendations.append(

            "Validate log retention."

        )

        return {

            "Gaps": gaps,

            "Recommendations": recommendations,

        }


gap_analysis_service = GapAnalysisService()