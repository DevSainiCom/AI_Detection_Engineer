from typing import Any

import json

from pydantic import BaseModel, Field, field_validator


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

    @field_validator("sample_logs", mode="before")
    @classmethod
    def validate_sample_logs(cls, value):

        if value is None:
            return []

        # Already valid
        if (
            isinstance(value, list)
            and (len(value) == 0 or isinstance(value[0], dict))
        ):
            return value

        # JSON string
        if isinstance(value, str):

            try:
                parsed = json.loads(value)

                if isinstance(parsed, list):
                    return [
                        item
                        for item in parsed
                        if isinstance(item, dict)
                    ]

            except Exception:
                return []

        # List of strings (joined JSON)
        if (
            isinstance(value, list)
            and len(value) > 0
            and isinstance(value[0], str)
        ):

            try:

                parsed = json.loads("\n".join(value))

                if isinstance(parsed, list):
                    return [
                        item
                        for item in parsed
                        if isinstance(item, dict)
                    ]

            except Exception:
                return []

        return []