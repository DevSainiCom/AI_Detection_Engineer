from typing import Any

from pydantic import BaseModel, Field


class DetectionContext(BaseModel):

    attack_description: str

    connector_name: str = "Custom"

    threat_model: dict[str, Any] = Field(default_factory=dict)

    application_analysis: dict[str, Any] = Field(default_factory=dict)

    questionnaire: dict[str, Any] = Field(default_factory=dict)

    sample_logs: list[dict[str, Any]] = Field(default_factory=list)

    log_schema: dict[str, Any] = Field(default_factory=dict)

    ai_event_mapping: dict[str, Any] = Field(default_factory=dict)

    similar_rules: str = ""

    knowledge: str = ""

    knowledge_sources: list[str] = Field(default_factory=list)