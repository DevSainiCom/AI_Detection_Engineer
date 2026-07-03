"""
DREAD Risk Assessment Service
"""


class DREADService:

    def calculate(

        self,

        damage=8,

        reproducibility=8,

        exploitability=8,

        affected_users=8,

        discoverability=8,

    ):

        total = (

            damage

            + reproducibility

            + exploitability

            + affected_users

            + discoverability

        )

        score = total / 5

        if score >= 8:

            level = "Critical"

        elif score >= 6:

            level = "High"

        elif score >= 4:

            level = "Medium"

        else:

            level = "Low"

        return {

            "Damage": damage,

            "Reproducibility": reproducibility,

            "Exploitability": exploitability,

            "AffectedUsers": affected_users,

            "Discoverability": discoverability,

            "RiskScore": score,

            "RiskLevel": level,

        }


dread_service = DREADService()