"""
Application Analysis Domain Model
"""

from typing import List

from pydantic import BaseModel


class ApplicationAnalysis(BaseModel):

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

    recommended_log_sources: List[str]