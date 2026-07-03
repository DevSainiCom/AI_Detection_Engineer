"""
Loads Microsoft Sentinel connector knowledge.
"""

from backend.services.connector_service import connector_service
from backend.services.schema_loader_service import schema_loader_service


class NativeConnectorService:

    def load(
        self,
        connector_name: str,
    ):

        connector = connector_service.get_connector(
            connector_name
        )

        documentation = (
            schema_loader_service.load_connector_documentation(
                connector.knowledge_file
            )
        )

        schema = (
            schema_loader_service.load_schema(
                connector.table_name
            )
        )

        return {

            "connector": connector.model_dump(),

            "documentation": documentation,

            "schema": schema,

        }


native_connector_service = NativeConnectorService()