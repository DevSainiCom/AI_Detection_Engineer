from typing import List

from pydantic import BaseModel


class Technique(BaseModel):
    technique_id: str
    technique_name: str


class EntityMapping(BaseModel):
    entity_type: str
    field: str


class AlertDetails(BaseModel):
    display_name: str
    description: str


class Suppression(BaseModel):
    enabled: bool
    duration: str


class SentinelDetection(BaseModel):
    """
    Canonical Microsoft Sentinel Detection Rule.
    All AI generated detections MUST conform to this schema.
    """

    name: str

    description: str

    author: str

    version: str

    status: str

    severity: str

    risk_score: int

    tactics: List[str]

    techniques: List[Technique]

    required_data_connectors: List[str]

    query: str

    query_frequency: str

    query_period: str

    trigger_operator: str

    trigger_threshold: int

    entity_mappings: List[EntityMapping]

    suppression: Suppression

    alert_details: AlertDetails

    false_positive_notes: str

    tuning_guidance: str

    references: List[str]