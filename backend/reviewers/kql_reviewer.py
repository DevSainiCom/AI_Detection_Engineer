class KQLReviewer:

    def review(
        self,
        kql: str,
    ):

        score = 100

        findings = []

        if "TimeGenerated" not in kql:

            score -= 15

            findings.append(
                "Missing TimeGenerated filter."
            )

        if "project" not in kql.lower():

            score -= 10

            findings.append(
                "Missing project operator."
            )

        if "summarize" not in kql.lower():

            score -= 10

            findings.append(
                "Missing summarize."
            )

        if "contains" in kql.lower():

            score -= 5

            findings.append(
                "Prefer 'has' over 'contains'."
            )

        if "join" in kql.lower():

            findings.append(
                "Verify join performance."
            )

        return {

            "score": score,

            "findings": findings,

        }


kql_reviewer = KQLReviewer()