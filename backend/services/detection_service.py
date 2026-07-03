import json

from backend.prompts.system_prompt import SYSTEM_PROMPT
from backend.prompts.detection_prompt import build_detection_prompt
from backend.services.context_builder import context_builder
from backend.services.llm_service import llm_service


class DetectionService:
    """
    Enterprise Detection Generation Service
    """

    def generate(
        self,
        attack_description,
        connector_name,
        sample_logs,
        threat_model,
        application_analysis,
        questionnaire,
    ):

        context = context_builder.build(
            attack_description=attack_description,
            connector_name=connector_name,
            sample_logs=sample_logs,
            threat_model=threat_model,
            application_analysis=application_analysis,
            questionnaire=questionnaire,
        )

        prompt = build_detection_prompt(context)

        response = llm_service.generate(
            SYSTEM_PROMPT,
            prompt,
        )

        print("\n================ GPT RAW RESPONSE ================\n")
        print(response)
        print("\n==================================================\n")

        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            detection = json.loads(response)

        except Exception as ex:

            raise Exception(
                f"""
GPT did not return valid JSON.

================ RESPONSE ================

{response}

==========================================
"""
            ) from ex

        detection["_knowledge_sources"] = context.knowledge_sources
        detection["_connector"] = context.connector_name

        return detection


detection_service = DetectionService()