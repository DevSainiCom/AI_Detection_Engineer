from backend.services.kql_review_service import (
    kql_review_service,
)


class KQLReviewAPI:

    def review(
        self,
        kql: str,
    ) -> dict:

        return kql_review_service.review(
            kql
        )


kql_review_api = KQLReviewAPI()