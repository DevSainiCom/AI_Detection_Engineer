from backend.services.questionnaire_service import (
    questionnaire_service,
)


class QuestionnaireAPI:

    def generate(

        self,

        threat_model,

        connector_type,

    ):

        return questionnaire_service.generate(

            threat_model,

            connector_type,

        )


questionnaire_api = QuestionnaireAPI()