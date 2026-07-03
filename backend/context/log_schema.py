from typing import Any

from pydantic import BaseModel, Field


class LogSchema(BaseModel):

    table_name: str

    platform: str

    parser: str = ""

    columns: list[dict[str, Any]] = Field(default_factory=list)

    timestamp_field: str = ""

    event_field: str = ""

    user_field: str = ""

    ip_field: str = ""

    host_field: str = ""

    custom_event_mapping: dict[str, str] = Field(default_factory=dict)