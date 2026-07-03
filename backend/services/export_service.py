"""
Export Service
"""

import json
import yaml


class ExportService:

    def export_json(
        self,
        detection,
    ):

        return json.dumps(

            detection,

            indent=4,

        )

    def export_yaml(
        self,
        detection,
    ):

        return yaml.dump(

            detection,

            sort_keys=False,

            allow_unicode=True,

        )


export_service = ExportService()