"""
Audit Trail Service
"""

from datetime import datetime


class AuditService:

    def build(

        self,

        context,

        detection,

    ):

        return {

            "Timestamp":

                datetime.utcnow().isoformat(),

            "Model":

                "GPT-5-mini",

            "KnowledgeSources":

                context.knowledge_sources,

            "PromptVersion":

                "DetectionPrompt_v2",

            "ThreatModel":

                bool(context.threat_model),

            "ApplicationAnalysis":

                bool(context.application_analysis),

            "Connector":

                context.log_schema.get(

                    "table_name",

                    "",

                ),

            "DetectionName":

                detection.get(

                    "DetectionName",

                    "",

                ),

            "Version":

                detection.get(

                    "Version",

                    "1.0",

                ),

        }


audit_service = AuditService()