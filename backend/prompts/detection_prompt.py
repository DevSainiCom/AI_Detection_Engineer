def build_detection_prompt(
    attack_description: str,
    knowledge: str,
) -> str:
    """
    Builds the prompt for generating a Microsoft Sentinel Detection.
    """

    return f"""
You are generating a Microsoft Sentinel Analytics Rule.

Attack Description

{attack_description}

------------------------------------------------------------

Relevant Detection Engineering Knowledge

{knowledge}

------------------------------------------------------------

Instructions

Generate a production-ready Microsoft Sentinel Detection.

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT explain the response.

Include:

- DetectionName
- Description
- Product
- LogSourceTypes
- Severity
- RiskScore
- Tactics
- Techniques
- QueryFrequency
- QueryPeriod
- Query
- EntityMappings
- FalsePositives
- DetectionLogic
- RecommendedActions
- References
- Version
- Status
- Author

The KQL must:

- Follow Microsoft Sentinel best practices.
- Use configurable thresholds.
- Filter TimeGenerated early.
- Use summarize where appropriate.
- Project only investigation fields.
- Minimize false positives.
"""