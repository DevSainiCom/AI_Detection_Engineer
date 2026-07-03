"""
Threat Model → Detection Use Case Generator
"""


class UseCaseGenerationService:

    def generate(

        self,

        threat_model,

    ):

        attack = threat_model.get(

            "AttackDescription",

            ""

        )

        use_case = {

            "Threat": attack,

            "DetectionObjective":

                f"Detect {attack}",

            "Priority": "High",

            "MITRE": [],

            "RecommendedDetections": [

                "Authentication Monitoring",

                "Privilege Escalation",

                "Persistence",

            ],

        }

        return use_case


use_case_generation_service = (

    UseCaseGenerationService()

)