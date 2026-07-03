"""
Connector Domain Model

Represents a Microsoft Sentinel connector or a
custom application log source.
"""

from typing import Literal

from pydantic import BaseModel, Field


class Connector(BaseModel):

    # Display Name
    name: str

    # Native Sentinel or Custom
    connector_type: Literal[
        "native",
        "custom",
    ]

    # Example:
    # Microsoft Defender XDR
    # Windows Security Events
    # Custom Payroll Application
    product: str

    # Sentinel Table
    table_name: str = ""

    # Parser (CEF, Syslog, AMA, JSON...)
    parser: str = ""

    # Sample Logs uploaded by customer
    sample_logs: list[dict] = Field(
        default_factory=list
    )

    # Whether Microsoft already provides
    # a supported connector
    supported_connector: bool = False

    # Documentation file loaded from RAG
    knowledge_file: str = ""

    # Optional connector version
    version: str = ""

    # Optional vendor
    vendor: str = ""

    # Optional description
    description: str = ""

    model_config = {
        "extra": "allow"
    }