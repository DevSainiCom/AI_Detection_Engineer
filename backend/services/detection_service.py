import json

from backend.prompts.system_prompt import SYSTEM_PROMPT
from backend.prompts.detection_prompt import build_detection_prompt

from backend.schemas.detection_request import DetectionRequest

from backend.rag.knowledge_service import knowledge_service

from backend.services.llm_service import llm_service


class DetectionService:
    """
    Generates Microsoft Sentinel detections.
    """

    def generate_detection(
        self,
        request: DetectionRequest,
    ) -> dict:

        knowledge, sources = knowledge_service.retrieve(
            request.attack_description
        )

        prompt = build_detection_prompt(
            request.attack_description,
            knowledge,
        )

        response = llm_service.generate(
            SYSTEM_PROMPT,
            prompt,
        )

        detection = json.loads(response)

        detection["_knowledge_sources"] = sources

        return detection


detection_service = DetectionService()