from pathlib import Path


class SchemaLoaderService:

    def __init__(self):

        self.schema_path = Path(
            "knowledge/schemas"
        )

        self.connector_path = Path(
            "knowledge/connectors"
        )

    def load_connector_documentation(
        self,
        filename: str,
    ) -> str:

        file = self.connector_path / filename

        if not file.exists():

            return ""

        return file.read_text(
            encoding="utf-8"
        )

    def load_schema(
        self,
        table_name: str,
    ) -> str:

        filename = table_name.lower() + ".md"

        file = self.schema_path / filename

        if not file.exists():

            return ""

        return file.read_text(
            encoding="utf-8"
        )


schema_loader_service = SchemaLoaderService()