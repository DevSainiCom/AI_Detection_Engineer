# Microsoft Sentinel KQL Best Practices

## General Principles

- Always filter on TimeGenerated first.
- Filter as early as possible.
- Use project to reduce unnecessary columns.
- Prefer has over contains where applicable.
- Avoid wildcard searches.
- Avoid unnecessary joins.
- Use summarize only after filtering.
- Use let statements for reusable logic.
- Prefer lookup instead of join for small datasets.
- Use materialize() for repeated expensive queries.

## Query Order

TimeGenerated
↓

Filtering
↓

Project
↓

Extend
↓

Summarize
↓

Join

## Naming

Use meaningful variable names.

## Performance

Never scan the whole table if unnecessary.

Always limit the time window.

Avoid dynamic parsing unless required.

## Detection Engineering

Rules should be readable.

Rules should be deterministic.

Rules should minimize false positives.

Rules should support MITRE ATT&CK mapping.