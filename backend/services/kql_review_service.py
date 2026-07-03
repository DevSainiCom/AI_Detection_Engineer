from backend.reviewers.kql_reviewer import kql_reviewer


class KQLReviewService:

    def review(
        self,
        kql: str,
    ) -> dict:

        review = kql_reviewer.review(
            kql
        )

        review["optimized_kql"] = kql

        return review


kql_review_service = KQLReviewService()