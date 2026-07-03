# False Positive Reduction Guide

## Objectives

Reduce alert fatigue while maintaining high detection quality.

## Best Practices

- Exclude known service accounts.
- Exclude health check accounts.
- Baseline normal administrator activity.
- Baseline scheduled tasks.
- Exclude vulnerability scanners.
- Suppress known maintenance windows.
- Use watchlists for approved systems.
- Correlate multiple events before alerting.
- Alert on behavioral anomalies instead of single events.
- Tune thresholds using historical data.

## Detection Tuning

Always include:

- Allow Lists
- Deny Lists
- Thresholds
- Time Windows
- User Risk
- Device Risk
- Geo Risk

## AI Recommendation

Suggest exclusions separately.

Never remove detection logic.
Only reduce unnecessary alerts.