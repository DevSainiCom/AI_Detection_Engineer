"""
Application Analysis Domain Model
"""

from typing import List

from pydantic import BaseModel


class ApplicationAnalysis(BaseModel):

    # ----------------------------
    # Basic Information
    # ----------------------------

    application_name: str

    application_type: str

    business_function: str

    internet_facing: bool

    authentication: str

    cloud_provider: str

    hosting_environment: str

    business_criticality: str

    data_classification: str

    technology_stack: List[str]

    # ----------------------------
    # Analysis
    # ----------------------------

    executive_summary: str

    security_rating: str

    architecture_summary: str

    security_observations: List[str]

    recommended_log_sources: List[str]

    recommended_detection_use_cases: List[str]

    critical_assets: List[str]

    trust_boundaries: List[str]

    knowledge_generated: List[str]

    future_ai_usage: str