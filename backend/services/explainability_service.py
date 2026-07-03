"""
Explainability Service
"""


class ExplainabilityService:

    def build(

        self,

        context,

    ):

        return {

            "knowledge_sources":

                context.knowledge_sources,

            "similar_rules_used":

                bool(context.similar_rules),

            "threat_model_used":

                bool(context.threat_model),

            "application_analysis_used":

                bool(context.application_analysis),

            "log_schema_used":

                bool(context.log_schema),

            "sample_logs_used":

                len(context.sample_logs),

            "ai_event_framework_used":

                bool(context.ai_event_mapping),

            "reason":

                "Detection generated using enterprise knowledge, log schema, AI event mapping and Microsoft Sentinel best practices."

        }


explainability_service = ExplainabilityService()