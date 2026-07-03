<<<<<<< HEAD
# 🛡️ AI Detection Engineer

AI-powered Microsoft Sentinel Detection Engineering Assistant.

Generate production-ready Microsoft Sentinel Analytics Rules using GPT-5, Retrieval-Augmented Generation (RAG Lite), and Detection Engineering best practices.

---

## Features

- AI-generated Microsoft Sentinel Analytics Rules
- Kusto Query Language (KQL) generation
- MITRE ATT&CK mapping
- Severity and Risk Scoring
- Entity Mapping
- Detection Logic
- False Positive Guidance
- Recommended Actions
- Detection References
- RAG Lite using curated Detection Engineering knowledge
- Streamlit Web UI
- Download Detection as JSON

---

## Architecture

```
            Streamlit UI

                  │

                  ▼

        Attack Description

                  │

                  ▼

         Knowledge Retrieval
            (Markdown RAG)

                  │

                  ▼

            Prompt Builder

                  │

                  ▼

             GPT-5-mini API

                  │

                  ▼

    Microsoft Sentinel Detection

                  │

                  ▼

           JSON + KQL Output
```

---

## Technology Stack

- Python 3.13
- OpenAI GPT-5-mini
- Streamlit
- Microsoft Sentinel
- Kusto Query Language (KQL)
- MITRE ATT&CK
- Retrieval-Augmented Generation (RAG Lite)

---

## Project Structure

```
backend/
frontend/
knowledge/
outputs/
scripts/
tests/
streamlit_app.py
main.py
```

---

## Example Workflow

1. Describe an attack.
2. AI retrieves relevant Detection Engineering knowledge.
3. GPT generates a production-ready Sentinel Analytics Rule.
4. Detection is displayed in the UI.
5. Download as JSON.

---

## Current Version

v0.1 MVP

### Implemented

- Detection Generation
- Streamlit UI
- RAG Lite
- Microsoft Sentinel JSON Output

### Planned

- Detection Review Engine
- Docker Support
- Azure Deployment
- Vector Database RAG
- Multi-Agent Detection Engineering

---

## Author

Devender
Security Architect
Microsoft Sentinel | Detection Engineering | AI Security
=======
# AI_Detection_Engineer
>>>>>>> e5b1d605c93f5d17d04023e3f1a1d2adfb59de11
