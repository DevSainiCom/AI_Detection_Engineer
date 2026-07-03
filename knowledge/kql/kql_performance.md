# Microsoft Sentinel KQL Performance Guide

## Performance Principles

- Always filter TimeGenerated first.
- Reduce the dataset before joins.
- Project only required fields.
- Avoid full table scans.
- Use summarize after filtering.
- Avoid regex unless necessary.
- Prefer has over contains.
- Use in instead of multiple OR conditions.
- Minimize extend operations.
- Materialize expensive subqueries when reused.

## Expensive Operations

- join
- mv-expand
- parse_json
- regex
- externaldata

Only use them when necessary.

## Optimized Query Pattern

SecurityEvent
→ Time Filter
→ Event Filter
→ Project
→ Extend
→ Summarize
→ Join (if required)

## Query Cost Reduction

- Minimize scanned rows.
- Avoid duplicate calculations.
- Reduce returned columns.
- Filter before summarize.
- Filter before joins.

## Detection Engineering Recommendations

- Queries should complete in seconds.
- Support scheduled analytics rules.
- Optimize for production environments.
- Prefer deterministic logic.
- Avoid excessive memory consumption.