from backend.context.detection_context import DetectionContext


def build_detection_prompt(
    context: DetectionContext,
):

    return f"""
You are a Senior Microsoft Sentinel Detection Engineer.

Generate a PRODUCTION READY Microsoft Sentinel Analytics Rule.

====================================================
Threat Model
====================================================

{context.threat_model}

====================================================
Application Analysis
====================================================

{context.application_analysis}

====================================================
Questionnaire
====================================================

{context.questionnaire}

====================================================
Connector
====================================================

{context.connector_name}

====================================================
Sample Logs
====================================================

{context.sample_logs[:20]}

====================================================
Schema
====================================================

{context.log_schema}

====================================================
Custom Event Mapping
====================================================

{context.ai_event_mapping}

====================================================
Similar Rules
====================================================

{context.similar_rules}

====================================================
Knowledge
====================================================

{context.knowledge}

====================================================

Return ONLY VALID JSON.

Do NOT explain anything.

Do NOT use markdown.

The JSON MUST contain EXACTLY these fields.

{{
    "DetectionName":"",
    "Description":"",
    "Product":"Microsoft Sentinel",
    "LogSourceTypes":[],
    "Severity":"Medium",
    "RiskScore":50,
    "Tactics":[],
    "Techniques":[],
    "QueryFrequency":"1h",
    "QueryPeriod":"1h",
    "Query":"",
    "EntityMappings":[],
    "FalsePositives":[],
    "DetectionLogic":"",
    "RecommendedActions":[],
    "References":[],
    "Version":"1.0",
    "Status":"Draft",
    "Author":"AI Detection Engineer"
}}

Requirements

- Use Microsoft Sentinel best practices.
- Generate production quality KQL.
- Use configurable thresholds.
- Filter TimeGenerated first.
- Reduce false positives.
- Use summarize where appropriate.
- Use EntityMappings.
- Use MITRE ATT&CK.
- Use the supplied sample logs.
- Use connector schema.
- Use custom event mapping.
- Use the supplied knowledge.
- Return ONLY JSON.
"""