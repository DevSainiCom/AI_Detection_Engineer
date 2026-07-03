# Kerberoasting Detection

MITRE Technique

T1558.003

Credential Access

Typical Data Source

SecurityEvent

Important Event ID

4769

Recommended Detection Logic

Detect abnormal Kerberos Service Ticket requests.

Aggregate requests by requesting user.

Detect large numbers of unique SPNs requested.

Recommended Threshold

10 unique SPNs within one hour.

Common False Positives

- Backup software
- Vulnerability scanners
- Monitoring systems

Recommended Entity Mapping

Account

IP Address

Host

Best Practices

Use summarize.

Use configurable thresholds.

Project only investigation fields.

Filter TimeGenerated early.