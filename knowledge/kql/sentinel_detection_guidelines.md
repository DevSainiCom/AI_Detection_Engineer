# Microsoft Sentinel Detection Engineering Guidelines

## Analytics Rule Standards

Every rule should contain:

- Detection Name
- Description
- MITRE Mapping
- Severity
- Tactics
- Techniques
- Entity Mapping
- Alert Details
- Scheduling
- Lookback
- Threshold
- Version
- Author

## Detection Quality

Rules should

- Be deterministic
- Be production ready
- Support investigation
- Reduce false positives
- Map to ATT&CK
- Use optimized KQL

## Naming

Prefix with technology if required.

Example

AAD - Password Spray

Windows - Kerberoasting

Azure - Impossible Travel

## Scheduling

Use smallest practical lookback.

Avoid unnecessary execution frequency.

## Alert Enrichment

Always populate

- Account
- Host
- IP
- URL
- Process
- File
- Device

where available.