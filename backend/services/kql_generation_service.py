from backend.context.detection_context import DetectionContext

from backend.prompts.system_prompt import SYSTEM_PROMPT

from backend.prompts.detection.kql_generation_prompt import (
    build_kql_prompt,
)

from backend.services.llm_service import llm_service


class KQLGenerationService:

    def generate(
        self,
        context: DetectionContext,
    ) -> str:

        prompt = build_kql_prompt(
            context
        )

        return llm_service.generate(

            SYSTEM_PROMPT,

            prompt,

        )


kql_generation_service = KQLGenerationService()