"""
Builds the Detection Context used by the AI Detection Engine.
"""

from backend.context.detection_context import DetectionContext
from backend.rag.knowledge_service import knowledge_service


class ContextBuilder:

    def build(
        self,
        attack_description: str,
        connector_name: str,
        sample_logs=None,
        threat_model=None,
        application_analysis=None,
        questionnaire=None,
        ai_event_mapping=None,
    ):

        sample_logs = sample_logs or []

        knowledge, sources = knowledge_service.retrieve(
            attack_description
        )

        schema = {}

        if ai_event_mapping is None:
            ai_event_mapping = {}

        similar = ""

        if hasattr(application_analysis, "model_dump"):
            application_analysis = application_analysis.model_dump()
        elif hasattr(application_analysis, "dict"):
            application_analysis = application_analysis.dict()
        else:
            application_analysis = application_analysis or {}

        return DetectionContext(
            attack_description=attack_description,
            connector_name=connector_name,
            threat_model=threat_model or {},
            application_analysis=application_analysis,
            questionnaire=questionnaire or {},
            sample_logs=sample_logs,
            log_schema=schema,
            ai_event_mapping=ai_event_mapping,
            similar_rules=similar,
            knowledge=knowledge,
            knowledge_sources=sources,
        )


context_builder = ContextBuilder()