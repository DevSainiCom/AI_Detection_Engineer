from typing import Any

from pydantic import BaseModel, Field


class SampleLog(BaseModel):

    table_name: str

    raw_log: dict[str, Any]

    normalized_log: dict[str, Any] = Field(default_factory=dict)