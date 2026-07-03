"""
Enterprise Detection Reviewer
"""


class DetectionReviewer:

    def review(
        self,
        detection: dict,
    ) -> dict:

        score = 100

        findings = []

        recommendations = []

        required = [

            "DetectionName",
            "Description",
            "Severity",
            "Query",
            "EntityMappings",
            "Tactics",
            "Techniques",
            "FalsePositives",
            "DetectionLogic",
            "RecommendedActions",

        ]

        for field in required:

            if not detection.get(field):

                score -= 5

                findings.append(
                    f"{field} is missing."
                )

        if len(detection.get("Query", "")) < 50:

            score -= 10

            findings.append(
                "KQL query is too short."
            )

        if not detection.get("EntityMappings"):

            recommendations.append(
                "Add Entity Mapping."
            )

        if not detection.get("FalsePositives"):

            recommendations.append(
                "Document False Positive guidance."
            )

        if score >= 90:

            rating = "Excellent"

        elif score >= 75:

            rating = "Good"

        elif score >= 60:

            rating = "Fair"

        else:

            rating = "Needs Improvement"

        return {

            "OverallScore": score,

            "Rating": rating,

            "Findings": findings,

            "Recommendations": recommendations,

        }


detection_reviewer = DetectionReviewer()