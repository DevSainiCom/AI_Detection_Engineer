"""
AI Questionnaire Service
"""


class QuestionnaireService:

    def generate(
        self,
        threat_model: dict,
        connector_type: str,
    ):

        questions = []

        if connector_type == "custom":

            questions.extend([

                "What parser is available?",

                "How are authentication events represented?",

                "Which field contains usernames?",

                "Which field contains source IP?",

                "Which field contains timestamps?",

            ])

        else:

            questions.extend([

                "Which Sentinel connector is enabled?",

                "Are all recommended tables available?",

                "Is data normalized?",

            ])

        return questions


questionnaire_service = QuestionnaireService()