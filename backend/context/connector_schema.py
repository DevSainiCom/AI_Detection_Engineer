"""
Connector Schema

Represents the schema loaded from either
Microsoft Sentinel documentation or AI log analysis.
"""

from typing import Any

from pydantic import BaseModel, Field


class ConnectorSchema(BaseModel):

    connector_name: str

    connector_type: str

    table_name: str

    parser: str = ""

    platform: str = ""

    documentation: str = ""

    columns: list[dict[str, Any]] = Field(default_factory=list)

    required_fields: list[str] = Field(default_factory=list)

    entity_mapping: dict[str, str] = Field(default_factory=dict)

    supported_events: dict[str, str] = Field(default_factory=dict)

    mitre_mapping: dict[str, list[str]] = Field(default_factory=dict)

    model_config = {
        "extra": "allow"
    }