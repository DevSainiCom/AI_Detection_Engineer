"""
Threat Model Service

Generates enterprise Threat Models using
GPT-5 and the Markdown Knowledge Base.
"""

import json

from backend.models.threat_model import ThreatModel
from backend.prompts.threat_model_prompt import (
    THREAT_MODEL_SYSTEM_PROMPT,
    build_threat_model_prompt,
)
from backend.rag.knowledge_service import knowledge_service
from backend.schemas.threat_model_request import (
    ThreatModelRequest,
)
from backend.schemas.threat_model_response import (
    ThreatModelResponse,
)
from backend.services.llm_service import llm_service


class ThreatModelService:
    """
    Generates Threat Models.
    """

    def generate(
        self,
        request: ThreatModelRequest,
    ) -> ThreatModelResponse:

        search_text = " ".join(
            [
                request.application_name,
                request.business_function,
                request.description,
            ]
        )

        knowledge, sources = knowledge_service.retrieve(
            search_text
        )

        user_prompt = build_threat_model_prompt(
            application_name=request.application_name,
            business_function=request.business_function,
            description=request.description,
            knowledge=knowledge,
        )

        response = llm_service.generate(
            system_prompt=THREAT_MODEL_SYSTEM_PROMPT,
            user_prompt=user_prompt,
        )

        data = json.loads(response)

        threat_model = ThreatModel(**data)

        return ThreatModelResponse(
            **threat_model.model_dump()
        )


threat_model_service = ThreatModelService()