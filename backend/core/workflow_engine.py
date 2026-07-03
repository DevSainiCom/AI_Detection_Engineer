"""
Workflow Engine

Enterprise Detection Workflow
"""

from backend.services.detection_service import (
    detection_service,
)

from backend.services.kql_review_service import (
    kql_review_service,
)

from backend.services.detection_review_service import (
    detection_review_service,
)


class WorkflowEngine:

    def execute(

        self,

        attack_description,

        connector_name,

        sample_logs=None,

        threat_model=None,

        application_analysis=None,

        questionnaire=None,

    ):

        detection = detection_service.generate(

            attack_description=attack_description,

            connector_name=connector_name,

            sample_logs=sample_logs or [],

            threat_model=threat_model or {},

            application_analysis=application_analysis or {},

            questionnaire=questionnaire or {},

        )

        if detection.get("Query"):

            detection["KQLReview"] = (

                kql_review_service.review(

                    detection["Query"]

                )

            )

        detection["DetectionReview"] = (

            detection_review_service.review(

                detection

            )

        )

        return detection


workflow_engine = WorkflowEngine()