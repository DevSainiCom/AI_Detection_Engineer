"""
Threat Model Prompt Builder
"""

THREAT_MODEL_SYSTEM_PROMPT = """
You are a Principal Microsoft Sentinel Detection Engineer,
Cloud Security Architect,
Threat Modeling Expert,
and MITRE ATT&CK Specialist.

Your responsibility is to produce enterprise-grade threat models.

Think like a Security Architect designing detections for Microsoft Sentinel.

Always return valid JSON only.

Do not use markdown.

Do not explain your reasoning.

Return only JSON.
"""


def build_threat_model_prompt(
    application_name: str,
    business_function: str,
    description: str,
    knowledge: str
) -> str:

    return f"""
Application Name:
{application_name}

Business Function:
{business_function}

Description:
{description}

Relevant Security Knowledge:
{knowledge}

Create a complete Threat Model.

Include:

- Executive Summary
- Critical Assets
- Trust Boundaries
- Entry Points
- Threat Actors
- Threat Scenarios
- MITRE ATT&CK Mapping
- Security Controls
- Detection Opportunities
- Residual Risks
- Confidence Score

Return JSON only.
"""