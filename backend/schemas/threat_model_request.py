"""
Threat Model Request Schema

Defines the user input required to generate a Threat Model.
"""

from pydantic import BaseModel, Field


class ThreatModelRequest(BaseModel):
    """
    Input request for Threat Model generation.
    """

    application_name: str = Field(
        ...,
        description="Name of the application"
    )

    business_function: str = Field(
        ...,
        description="Primary business purpose"
    )

    description: str = Field(
        default="",
        description="Additional application description"
    )