"""
AI Log Parser Service

Extracts useful metadata from uploaded sample logs.
"""


class AILogParserService:

    def parse(
        self,
        sample_logs: list[dict],
    ) -> dict:

        if not sample_logs:

            return {}

        sample = sample_logs[0]

        fields = []

        for key, value in sample.items():

            fields.append({

                "field": key,

                "type": type(value).__name__,

            })

        return {

            "table_detected": False,

            "fields": fields,

            "sample_count": len(sample_logs),

            "recommended_entities": self.recommend_entities(sample),

        }

    def recommend_entities(
        self,
        sample,
    ):

        entities = {}

        for field in sample:

            name = field.lower()

            if "user" in name:

                entities[field] = "Account"

            elif "ip" in name:

                entities[field] = "IP"

            elif "host" in name or "computer" in name:

                entities[field] = "Host"

            elif "process" in name:

                entities[field] = "Process"

        return entities


ai_log_parser_service = AILogParserService()