"""
AI Event Framework Service
"""


class AIEventFrameworkService:

    EVENT_MAP = {

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

    def build(
        self,
        sample_logs,
        event_field,
    ):

        framework = {}

        for log in sample_logs:

            event = str(

                log.get(

                    event_field,

                    ""

                )

            )

            framework[event] = self.EVENT_MAP.get(

                event,

                "UNKNOWN"

            )

        return framework


ai_event_framework_service = AIEventFrameworkService()