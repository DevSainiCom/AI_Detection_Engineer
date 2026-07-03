from pathlib import Path

from backend.context.connector import Connector


class ConnectorService:

    def __init__(self):

        self.connector_path = Path(
            "knowledge/connectors"
        )

        self.native_connectors = {

            "Windows Security Events": {
                "table": "SecurityEvent",
                "parser": "AMA",
                "knowledge": "windows_security.md",
            },

            "Microsoft Defender XDR": {
                "table": "DeviceEvents",
                "parser": "MDE",
                "knowledge": "microsoft_defender_xdr.md",
            },

            "Microsoft Entra ID": {
                "table": "SigninLogs",
                "parser": "Entra",
                "knowledge": "microsoft_entra_id.md",
            },

            "Azure Activity": {
                "table": "AzureActivity",
                "parser": "Azure",
                "knowledge": "azure_activity.md",
            },

            "Syslog": {
                "table": "Syslog",
                "parser": "Syslog",
                "knowledge": "syslog.md",
            },

            "CEF": {
                "table": "CommonSecurityLog",
                "parser": "CEF",
                "knowledge": "cef.md",
            },

            "Office 365": {
                "table": "OfficeActivity",
                "parser": "Office365",
                "knowledge": "office365.md",
            }

        }

    def get_connector(
        self,
        connector_name: str,
    ) -> Connector:

        if connector_name in self.native_connectors:

            info = self.native_connectors[
                connector_name
            ]

            return Connector(

                name=connector_name,

                connector_type="native",

                product=connector_name,

                table_name=info["table"],

                parser=info["parser"],

                supported_connector=True,

                knowledge_file=info["knowledge"],

            )

        return Connector(

            name=connector_name,

            connector_type="custom",

            product=connector_name,

            parser="JSON",

            supported_connector=False,

            knowledge_file="custom_application.md",

        )


connector_service = ConnectorService()