"""
Detection Context Service

This service demonstrates how the Detection Context Agent
collects and structures customer-specific business,
security and telemetry context.

The collected knowledge will later be stored within the
Detection Knowledge Manager and retrieved by the
Context Retrieval Agent during AI-assisted
Microsoft Sentinel detection generation.
"""


class DetectionContextService:

    def generate(
        self,
        threat_model: dict,
        application,
        coverage_analysis,
        parser_type: str,
    ):

        # ----------------------------------------------------------
        # Extract Business Context
        # ----------------------------------------------------------

        business_function = (
            threat_model.get("BusinessFunction")
            or "Business Application"
        )

        criticality = (
            threat_model.get("Criticality")
            or "Medium"
        )

        parser_type = parser_type or "Native Microsoft Sentinel"

        # ----------------------------------------------------------
        # Parser Context
        # ----------------------------------------------------------

        if parser_type.lower() == "custom parser":

            parser_context = [

                "Custom parser implementation",

                "Parser documentation available",

                "Field mapping required",

                "Normalization rules required",

                "Sample raw logs available",

                "Sample parsed logs available",

                "Schema version tracking",

                "Parser maintenance process",

            ]

            rag_sources = [

                "Parser Documentation",

                "Field Mapping",

                "Normalization Rules",

                "Sample Raw Logs",

                "Sample Parsed Logs",

                "Data Dictionary",

            ]

        else:

            parser_context = [

                "Native Microsoft Sentinel Connector",

                "Microsoft supported schema",

                "ASIM normalization",

                "Standard Sentinel tables",

                "Microsoft Learn documentation",

            ]

            rag_sources = [

                "Microsoft Learn",

                "Connector Documentation",

                "ASIM Documentation",

                "Sentinel Table Schema",

            ]

        # ----------------------------------------------------------
        # Business Context
        # ----------------------------------------------------------

        business_context = [

            f"Business Function: {business_function}",

            f"Business Criticality: {criticality}",

            "Customer detection objectives",

            "Business priorities",

        ]

        # ----------------------------------------------------------
        # Operational Context
        # ----------------------------------------------------------

        operational_context = [

            "Microsoft Sentinel",

            "Microsoft Defender XDR",

            "Entra ID",

            "Threat Intelligence",

            "SOC Investigation Workflow",

        ]

        # ----------------------------------------------------------
        # Knowledge Generated
        # ----------------------------------------------------------

        knowledge_generated = [

            "Business Context",

            "Operational Context",

            "Telemetry Context",

            "Parser Context",

            "Detection Objectives",

            "Detection Constraints",

            "Normalization Knowledge",

            "Knowledge Sources",

        ]

        # ----------------------------------------------------------
        # Executive Summary
        # ----------------------------------------------------------

        executive_summary = (
            "The Detection Context Agent has successfully collected "
            "customer-specific business, operational and telemetry "
            "information required for Microsoft Sentinel detection "
            "engineering."
        )

        # ----------------------------------------------------------
        # Detection Engineering Impact
        # ----------------------------------------------------------

        detection_engineering_impact = (
            "The collected knowledge will be stored within the "
            "Detection Knowledge Manager. During detection generation, "
            "the Detection Planning Agent will determine which context "
            "is required, while the Context Retrieval Agent will "
            "retrieve parser documentation, telemetry information, "
            "field mappings and operational knowledge before the "
            "Detection Generation Engine creates customer-specific "
            "Microsoft Sentinel detections."
        )

        return {

            "executive_summary": executive_summary,

            "business_context": business_context,

            "parser_context": parser_context,

            "operational_context": operational_context,

            "rag_sources": rag_sources,

            "knowledge_generated": knowledge_generated,

            "detection_engineering_impact": detection_engineering_impact,

        }


detection_context_service = DetectionContextService()