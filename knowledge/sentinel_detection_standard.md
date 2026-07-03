# Microsoft Sentinel Detection Engineering Standard

Version: 1.0

---

# 1. Purpose

This document defines the engineering standard used by the AI Detection Engineer project to generate, review, score, and improve Microsoft Sentinel Analytics Rules.

The objective is to ensure every generated detection is:

- Technically accurate
- Operationally useful
- Performance optimized
- Easy to maintain
- Aligned with MITRE ATT&CK
- Suitable for production deployment

This standard is the source of truth for:

- Detection generation
- Detection review
- Prompt engineering
- Future Retrieval-Augmented Generation (RAG)
- Streamlit dashboard
- Azure deployment

---

# 2. Detection Engineering Principles

Every detection should follow these principles.

## Accuracy

The detection must identify the intended attacker behaviour while minimizing missed detections.

---

## Low False Positives

A detection that generates excessive noise provides little operational value.

Every rule should include:

- meaningful filtering
- exclusions
- allowlists where appropriate
- tuning guidance

---

## Performance

KQL must be efficient.

Avoid unnecessary scans.

Project only required columns.

Limit time ranges.

Use efficient operators.

---

## Maintainability

Rules should be readable.

Complex logic should be split using let statements.

Comments should explain important assumptions.

---

## Operational Value

A SOC analyst should immediately understand:

- what happened
- who is affected
- why the alert triggered
- what to investigate next

---

# 3. Detection Lifecycle

Threat Scenario

↓

Detection Request

↓

AI Detection Generation

↓

Schema Validation

↓

Detection Review

↓

Human Approval

↓

Production Deployment

---

# 4. Canonical Detection Schema

Every generated detection MUST conform to the project's SentinelDetection schema.

The AI must never invent field names.

The schema is owned by this project.

---

# 5. Review Framework

Every detection is reviewed using a 100-point scoring framework.

| Category | Points |
|----------|--------|
| Detection Title | 5 |
| Description | 5 |
| MITRE Mapping | 10 |
| Severity | 5 |
| KQL Quality | 45 |
| False Positives | 10 |
| Performance | 5 |
| Entity Mapping | 5 |
| Tuning Guidance | 5 |
| Documentation | 5 |

Total = 100

---

This document will evolve with future releases.