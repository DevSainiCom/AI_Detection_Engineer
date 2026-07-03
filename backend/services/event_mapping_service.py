"""
AI Event Mapping Service
"""


class EventMappingService:

    DEFAULT_MAPPING = {

        "4624": "AI_AUTH_SUCCESS",

        "4625": "AI_AUTH_FAILURE",

        "4740": "AI_ACCOUNT_LOCKED",

        "1": "AI_AUTH_SUCCESS",

        "23": "AI_AUTH_FAILURE",

        "51": "AI_ACCOUNT_LOCKED",

        "SUCCESS": "AI_AUTH_SUCCESS",

        "FAILED": "AI_AUTH_FAILURE",

        "LOCKED": "AI_ACCOUNT_LOCKED",

    }

    def normalize(
        self,
        sample_logs,
        event_field,
    ):

        mapping = {}

        if not event_field:

            return mapping

        for log in sample_logs:

            event = str(
                log.get(
                    event_field,
                    ""
                )
            )

            mapping[event] = self.DEFAULT_MAPPING.get(

                event,

                "UNKNOWN"

            )

        return mapping


event_mapping_service = EventMappingService()