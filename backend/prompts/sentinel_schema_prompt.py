SCHEMA_PROMPT = """
You MUST return ONLY valid JSON.

Do NOT include markdown.

Do NOT include explanations.

Do NOT include code fences.

Return JSON matching EXACTLY this schema.

{
    "name": string,

    "description": string,

    "author": string,

    "version": string,

    "status": string,

    "severity": string,

    "risk_score": integer,

    "tactics": [
        string
    ],

    "techniques": [
        {
            "technique_id": string,
            "technique_name": string
        }
    ],

    "required_data_connectors": [
        string
    ],

    "query": string,

    "query_frequency": string,

    "query_period": string,

    "trigger_operator": string,

    "trigger_threshold": integer,

    "entity_mappings": [
        {
            "entity_type": string,
            "field": string
        }
    ],

    "suppression": {
        "enabled": boolean,
        "duration": string
    },

    "alert_details": {
        "display_name": string,
        "description": string
    },

    "false_positive_notes": string,

    "tuning_guidance": string,

    "references": [
        string
    ]
}
"""