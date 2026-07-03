"""
Detection Review Service
"""

from backend.reviewers.detection_reviewer import (
    detection_reviewer,
)

from backend.services.kql_review_service import (
    kql_review_service,
)


class DetectionReviewService:

    def review(
        self,
        detection: dict,
    ):

        detection_review = (

            detection_reviewer.review(

                detection

            )

        )

        kql_review = (

            kql_review_service.review(

                detection["Query"]

            )

        )

        return {

            "DetectionReview": detection_review,

            "KQLReview": kql_review,

        }


detection_review_service = DetectionReviewService()