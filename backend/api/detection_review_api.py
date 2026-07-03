from backend.services.detection_review_service import (
    detection_review_service,
)


class DetectionReviewAPI:

    def review(
        self,
        detection,
    ):

        return detection_review_service.review(
            detection
        )


detection_review_api = DetectionReviewAPI()