"""
AI Log Validation Service
"""

from backend.services.log_analysis_service import (
    log_analysis_service,
)


class LogValidationService:

    def validate(
        self,
        connector,
        sample_logs,
    ):

        schema = log_analysis_service.analyze(

            connector.connector_type,

            connector.table_name,

            sample_logs,

        )

        return {

            "valid": True,

            "table_name": schema.table_name,

            "parser": schema.parser,

            "platform": schema.platform,

            "schema": schema.model_dump(),

        }


log_validation_service = LogValidationService()