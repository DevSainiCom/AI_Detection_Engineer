from backend.context.detection_context import DetectionContext


def build_kql_prompt(
    context: DetectionContext,
) -> str:

    return f"""
You are a Principal Microsoft Sentinel Detection Engineer.

Generate ONLY production-ready Microsoft Sentinel KQL.

=========================
ATTACK
=========================

{context.attack_description}

=========================
THREAT MODEL
=========================

{context.threat_model}

=========================
APPLICATION
=========================

{context.application_analysis}

=========================
LOG SCHEMA
=========================

{context.log_schema}

=========================
SAMPLE LOGS
=========================

{context.sample_logs}

=========================
AI EVENT FRAMEWORK
=========================

{context.ai_event_mapping}

=========================
SIMILAR RULES
=========================

{context.similar_rules}

=========================
KNOWLEDGE
=========================

{context.knowledge}

Requirements

- Use supplied table name.
- Never invent field names.
- Use supplied schema.
- Optimize performance.
- Reduce false positives.
- Follow Microsoft Sentinel standards.
- Return ONLY KQL.
"""