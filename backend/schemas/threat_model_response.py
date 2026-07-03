"""
Threat Model Response Schema

Enterprise Threat Model Response
"""

from typing import Any

from pydantic import BaseModel, Field


class ThreatModelResponse(BaseModel):

    application_name: str

    business_function: str

    summary: str | None = None

    critical_assets: list[Any] = Field(default_factory=list)

    trust_boundaries: list[Any] = Field(default_factory=list)

    entry_points: list[Any] = Field(default_factory=list)

    threat_actors: list[Any] = Field(default_factory=list)

    threat_scenarios: list[Any] = Field(default_factory=list)

    security_controls: Any = None

    detection_opportunities: list[Any] = Field(default_factory=list)

    residual_risks: list[Any] = Field(default_factory=list)

    confidence_score: Any = None

    model_config = {
        "extra": "allow"
    }