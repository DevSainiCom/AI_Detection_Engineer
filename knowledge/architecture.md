# AI Detection Engineering Platform
## Architecture, RAG Strategy & Knowledge Integration

**Prepared by:** EPAM  
**Classification:** Proof of Concept  
**Prepared for:** PMI  
**Version:** 0.3

---

## 1. Current Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Streamlit Frontend                    │
│  Customer Onboarding → Detection Engineering → Deploy   │
└────────────────────────────┬────────────────────────────┘
                             │
             ┌───────────────▼───────────────┐
             │       Workflow Engine          │
             │  (backend/core/workflow.py)    │
             └───┬───────────────────────────┘
                 │
    ┌────────────▼────────────┐
    │    Rule-Based Services  │   ← Current POC
    │                         │
    │  • threat_model_service │
    │  • app_analysis_service │
    │  • gap_analysis_service │
    │  • detection_context    │
    │  • log_validation       │
    │  • detection_review     │
    └────────────┬────────────┘
                 │
    ┌────────────▼────────────┐
    │   AI Services (Live)    │   ← Already working
    │                         │
    │  • kql_generation       │
    │  • mitre_mapping        │
    │  • llm_service          │
    └────────────┬────────────┘
                 │
    ┌────────────▼────────────┐
    │   Knowledge Base (RAG)  │   ← Flat files, no vector DB yet
    │                         │
    │  knowledge/             │
    │  ├── connectors/        │
    │  ├── kql/               │
    │  ├── mitre/             │
    │  ├── rules/             │
    │  └── sentinel/          │
    └─────────────────────────┘
```

**What works today:**
- Full 12-step workflow UI
- KQL generation via Azure OpenAI / GPT
- MITRE ATT&CK mapping via GPT
- Detection review (rule-based scoring)
- Knowledge base as Markdown files (read at runtime)

**What is mocked / rule-based:**
- Threat Model assessment
- Application Analysis
- Gap Analysis
- Detection Context collection
- Telemetry Validation

---

## 2. Target Architecture (Production)

```
┌──────────────────────────────────────────────────────────────┐
│                      Streamlit / React Frontend              │
└──────────────────────────────┬───────────────────────────────┘
                               │
              ┌────────────────▼──────────────────┐
              │         Orchestration Layer         │
              │  (Multi-Agent Workflow Controller)  │
              └──┬──────────────────────────────┬──┘
                 │                              │
    ┌────────────▼──────────┐    ┌──────────────▼──────────────┐
    │    Customer Agents     │    │    Detection Agents          │
    │                        │    │                              │
    │  • Threat Modeling     │    │  • Detection Planning        │
    │  • App Analysis        │    │  • Context Retrieval         │
    │  • Gap Analysis        │    │  • KQL Generation            │
    │  • Detection Context   │    │  • MITRE Mapping             │
    │  • Telemetry Analysis  │    │  • Detection Review          │
    │  • Log Validation      │    │  • Documentation             │
    └────────────┬───────────┘    └──────────────┬──────────────┘
                 │                               │
    ┌────────────▼───────────────────────────────▼──────────────┐
    │                 Knowledge Manager                          │
    │                                                            │
    │  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐  │
    │  │  Vector DB   │  │  Structured  │  │   Document     │  │
    │  │ (Azure AI    │  │  Knowledge   │  │   Store        │  │
    │  │  Search /    │  │  (JSON/SQL)  │  │  (Blob/ADLS)   │  │
    │  │  Chroma)     │  │              │  │                │  │
    │  └──────────────┘  └──────────────┘  └────────────────┘  │
    └────────────────────────────────────────────────────────────┘
                               │
              ┌────────────────▼──────────────────┐
              │           Azure OpenAI             │
              │    GPT-4o · text-embedding-3       │
              └───────────────────────────────────┘
```

---

## 3. RAG Implementation Plan

### What is RAG for this platform?

RAG (Retrieval-Augmented Generation) means before asking GPT to write a
detection, we first retrieve the relevant customer-specific knowledge
(parser docs, telemetry samples, existing rules) and inject it into the
prompt. This stops GPT from hallucinating table names, field names, or
detection logic that doesn't match the customer's actual Sentinel environment.

### Step-by-Step Implementation

```
Phase 1 — Indexing (One-time + incremental)

  Knowledge Sources
       │
       ▼
  Document Ingestion
  • Parse Markdown, PDF, DOCX, Confluence pages
  • Chunk into ~512 token segments
  • Preserve metadata (source, category, connector, version)
       │
       ▼
  Embedding
  • Azure OpenAI: text-embedding-3-small (1536 dims)
  • Or: text-embedding-3-large for higher accuracy
       │
       ▼
  Vector Store
  • Azure AI Search (recommended for Azure-native stack)
  • OR: Chroma (local dev) → Qdrant (production)
  • Index: kb_chunks { id, text, embedding, metadata }


Phase 2 — Retrieval (Per detection request)

  Detection Request
  "Detect password spray against Entra ID"
       │
       ▼
  Query Embedding
  text-embedding-3-small → [0.12, -0.87, ...]
       │
       ▼
  Vector Similarity Search
  Top-K chunks (k=8–12) by cosine similarity
  Filtered by: connector=EntraID, category=detection
       │
       ▼
  Reranker (optional, high value)
  Cross-encoder reranker to re-score top-20 → top-8
       │
       ▼
  Context Assembly
  {
    "customer_context": [...],      # from customer onboarding
    "parser_docs": [...],           # from telemetry analysis
    "detection_examples": [...],    # from rules library
    "kql_patterns": [...],          # from kql/ knowledge
    "mitre_context": [...],         # from mitre/ knowledge
    "sentinel_schema": [...],       # table schemas
  }


Phase 3 — Generation

  Assembled Context + Detection Request
       │
       ▼
  Prompt Builder
  System prompt + few-shot examples + retrieved context
       │
       ▼
  GPT-4o
       │
       ▼
  Detection Review Agent validates output
```

### Recommended Tech Stack

| Component | Dev/POC | Production (Azure) |
|-----------|---------|---------------------|
| Vector DB | Chroma (local) | Azure AI Search |
| Embeddings | OpenAI text-embedding-3-small | same |
| Reranker | None | Azure AI Search semantic ranking |
| Document Store | Local files | Azure Blob Storage / ADLS |
| Orchestration | LangChain / LlamaIndex | Azure AI Foundry |
| Chunking | LangChain RecursiveTextSplitter | same |

### Chunk Strategy for Detection Engineering

```python
# Recommended chunking per knowledge type

chunk_strategy = {
    "detection_rules":     {"size": 400,  "overlap": 50},  # Keep rules intact
    "kql_patterns":        {"size": 300,  "overlap": 30},  # KQL snippets
    "mitre_techniques":    {"size": 512,  "overlap": 80},  # Technique context
    "parser_docs":         {"size": 600,  "overlap": 100}, # Parser field tables
    "sentinel_schema":     {"size": 256,  "overlap": 20},  # Table schemas
    "customer_context":    {"size": 512,  "overlap": 80},  # Business context
}
```

---

## 4. Alternatives to RAG

### Option A — Fine-Tuning (GPT Fine-Tune)

Train a base GPT model on your detection library.

```
Pros:
  • No retrieval step — knowledge is baked in
  • Faster inference
  • Better stylistic consistency

Cons:
  • Expensive: $3–8 per 1M training tokens
  • Static: must retrain when knowledge changes
  • Can't use customer-specific data without separate fine-tune per customer
  • Hallucination risk still present

Verdict for this platform: NOT recommended as primary strategy.
Use fine-tuning only for KQL style consistency on top of RAG.
```

### Option B — Long Context Window (Prompt Stuffing)

GPT-4o supports 128K tokens. Just paste everything into the prompt.

```
Pros:
  • Zero infrastructure
  • Simple to implement now (POC-friendly)

Cons:
  • Cost: ~$5–15 per detection at full context
  • Slow: 30–60 second latency with large context
  • "Lost in the middle" problem — GPT ignores middle of long prompts
  • Not scalable when customer knowledge grows

Verdict: Use NOW in POC (what you're doing today).
Replace with RAG for Sprint 4 production.
```

### Option C — Knowledge Graph (GraphRAG)

Model the detection domain as a graph:
Application → uses → EntraID → logs → SigninLogs → used_in → PasswordSprayDetection

```
Pros:
  • Captures relationships, not just similarity
  • Better for complex multi-hop reasoning
  • "Which detections use this log source?" — trivially answerable

Cons:
  • Significant build effort (6–12 weeks)
  • Requires knowledge graph maintenance
  • Overkill for MVP

Verdict: Roadmap item for v2.0. Combine with RAG for best results.
Microsoft's GraphRAG (open-source) is worth evaluating.
```

### Option D — Structured Retrieval (SQL/JSON store)

Store detections, techniques, connectors as structured data.
Query with exact filters instead of semantic search.

```
Pros:
  • Deterministic — no hallucination on structured fields
  • Fast and cheap
  • Perfect for MITRE mappings, connector schemas, table names

Cons:
  • Can't handle unstructured text (docs, threat reports)
  • Doesn't capture semantic similarity

Verdict: Use AS COMPLEMENT to RAG.
Structured store for schemas + RAG for narrative knowledge.
```

### Recommended Hybrid Architecture

```
Detection Request
      │
      ├──► Structured Lookup ──► Exact match: table names, MITRE IDs,
      │                          connector schemas, existing rule IDs
      │
      ├──► Vector Search ──────► Semantic match: detection patterns,
      │                          threat descriptions, parser docs
      │
      └──► Customer Context ───► Session state from onboarding workflow

All three → Prompt Builder → GPT-4o → Detection Review
```

---

## 5. Confluence as a Knowledge Source

### YES — Confluence is high-value for this platform.

Confluence pages likely contain:
- Detection runbooks and investigation guides
- Threat intelligence reports
- Application architecture decisions
- Security policies and standards
- Incident post-mortems with detection insights
- SOC procedures

### Integration Options

#### Option A — Confluence REST API (Recommended)

```python
import requests

class ConfluenceKnowledgeCollector:
    """
    Pull pages from Confluence spaces and index into vector store.
    """

    def __init__(self, base_url, username, api_token):
        self.base = base_url  # e.g. https://yourcompany.atlassian.net
        self.auth = (username, api_token)

    def get_pages_from_space(self, space_key):
        """
        Fetch all pages from a Confluence space.
        Recommended spaces:
          - SECOPS → SOC procedures, runbooks
          - DETECT → Detection library, KQL patterns
          - THREAT → Threat intelligence
          - ARCH   → Application architecture
        """
        url = f"{self.base}/wiki/rest/api/content"
        params = {
            "spaceKey": space_key,
            "expand": "body.storage,metadata.labels,version",
            "limit": 100,
        }
        response = requests.get(url, params=params, auth=self.auth)
        return response.json()["results"]

    def extract_text(self, page):
        """Strip Confluence storage format to plain text."""
        from bs4 import BeautifulSoup
        html = page["body"]["storage"]["value"]
        return BeautifulSoup(html, "html.parser").get_text()

    def build_metadata(self, page, space_key):
        return {
            "source": "confluence",
            "space": space_key,
            "title": page["title"],
            "url": f"{self.base}/wiki{page['_links']['webui']}",
            "labels": [l["name"] for l in page.get("metadata", {}).get("labels", {}).get("results", [])],
            "last_updated": page["version"]["when"],
        }
```

#### Option B — Confluence MCP (Modern Approach)

Atlassian now provides an MCP server for Confluence.
Claude/GPT can query Confluence directly as a tool call
without pre-indexing — useful for fresh, real-time data.

#### Recommended Confluence Space Structure

```
Knowledge Manager Source Map:

SECOPS space
  ├── Detection Runbooks       → customer_context index
  ├── Investigation Guides     → customer_context index
  └── SOC Procedures           → customer_context index

DETECT space
  ├── Detection Library        → detection_rules index
  ├── KQL Patterns             → kql_patterns index
  └── False Positive Notes     → detection_rules index

THREAT space
  ├── Threat Intelligence      → threat_context index
  └── Incident Post-Mortems    → threat_context index

ARCH space
  ├── Application Architecture → customer_context index
  └── Data Flow Diagrams       → customer_context index
```

#### Sync Strategy

```
Option 1 — Scheduled Sync (Simple)
  Nightly job: pull Confluence → chunk → re-embed changed pages
  Trigger: page "last_updated" timestamp comparison

Option 2 — Webhook Sync (Real-time)
  Confluence webhook → Azure Function → chunk → upsert vector store
  On page create/update/delete

Option 3 — On-Demand Sync
  User clicks "Sync Knowledge" in Platform Knowledge UI
  Good for POC
```

---

## 6. CMDB as a Knowledge Source

### YES — CMDB is extremely valuable. Often underused.

A CMDB (ServiceNow, BMC Helix, Azure Service Management) knows:
- Every application, service, and component in the environment
- Owners, teams, and business criticality classifications
- Network zones, dependencies, and data flows
- Patch status and vulnerability exposure
- CI relationships (App → Runs On → Server → In Zone → Network)

This directly enriches detections:

```
Without CMDB:
  "Detect privilege escalation on servers"

With CMDB:
  "Detect privilege escalation on servers tagged as:
   - Business Criticality: High
   - Application: Online Banking Portal
   - Owner: Finance Team
   - Network Zone: PCI-DSS Scope
   Generate high-severity alert, route to Finance SOC queue"
```

### What to Pull from CMDB

```python
cmdb_knowledge_targets = {

    "applications": {
        "fields": [
            "name", "business_criticality", "owner",
            "data_classification", "environment",
            "compliance_scope",           # PCI, HIPAA, SOX
        ],
        "use_in": "detection context, alert severity, routing",
    },

    "servers_and_hosts": {
        "fields": [
            "hostname", "ip_address", "os", "patch_level",
            "network_zone", "business_criticality",
            "owned_by_application",
        ],
        "use_in": "KQL entity filters, allowlisting, alert context",
    },

    "service_accounts": {
        "fields": [
            "account_name", "owning_application",
            "expected_behaviour", "privileged",
        ],
        "use_in": "service account abuse detection, baseline building",
    },

    "network_zones": {
        "fields": [
            "zone_name", "ip_ranges", "sensitivity",
            "allowed_communication",
        ],
        "use_in": "lateral movement detection, impossible travel",
    },

    "users_and_identities": {
        "fields": [
            "department", "role", "privileged_access",
            "normal_working_hours", "location",
        ],
        "use_in": "UBA baselines, impossible travel, after-hours alerts",
    },
}
```

### Integration Pattern

```python
class CMDBKnowledgeCollector:
    """
    Pull CIs from ServiceNow CMDB and structure for detection context.
    """

    def __init__(self, instance_url, username, password):
        self.base = instance_url  # e.g. https://company.service-now.com
        self.auth = (username, password)

    def get_applications(self):
        url = f"{self.base}/api/now/table/cmdb_ci_appl"
        params = {
            "sysparm_fields": "name,u_criticality,u_data_class,u_owner,u_env",
            "sysparm_limit": 500,
        }
        return requests.get(url, params=params, auth=self.auth).json()

    def build_detection_context(self, app_name):
        """
        Return structured context for a specific application —
        injected directly into the detection prompt.
        """
        # Query relationships: App → Servers → Users → Accounts
        ...

    def get_high_value_assets(self):
        """Return all CIs with criticality = High or Critical."""
        ...
```

### CMDB → KQL Enrichment Example

```kql
// Without CMDB context (generic)
SecurityEvent
| where EventID == 4625
| where FailureCount > 10

// With CMDB context (customer-specific, AI-generated)
SecurityEvent
| where EventID == 4625
| where Computer in (
    "BANKAPP01", "BANKAPP02", "PAYMENTDB01"  // ← from CMDB: PCI-scope servers
)
| where TargetUserName !in (
    "svc_bankapp", "svc_monitoring"          // ← from CMDB: known service accounts
)
| where FailureCount > 10
| extend BusinessCriticality = "Critical"    // ← from CMDB: app criticality
| extend ComplianceScope = "PCI-DSS"         // ← from CMDB: compliance tag
```

---

## 7. Combined Knowledge Architecture

```
                    KNOWLEDGE MANAGER
    ┌───────────────────────────────────────────────┐
    │                                               │
    │  ┌─────────────┐   ┌─────────────────────┐   │
    │  │  PLATFORM   │   │    CUSTOMER-SPECIFIC │   │
    │  │  KNOWLEDGE  │   │    KNOWLEDGE         │   │
    │  │             │   │                      │   │
    │  │ • KQL rules │   │ • Confluence pages   │   │
    │  │ • MITRE     │   │ • CMDB CI data       │   │
    │  │ • Sentinel  │   │ • Threat models      │   │
    │  │   schemas   │   │ • App analysis       │   │
    │  │ • Detection │   │ • Parser docs        │   │
    │  │   library   │   │ • Sample telemetry   │   │
    │  │ • Connector │   │ • Existing detections│   │
    │  │   docs      │   │ • SOC runbooks       │   │
    │  └──────┬──────┘   └──────────┬───────────┘   │
    │         │                     │               │
    │         └──────────┬──────────┘               │
    │                    │                          │
    │           ┌────────▼────────┐                 │
    │           │   Vector Store  │                 │
    │           │  (Azure AI      │                 │
    │           │   Search)       │                 │
    │           └─────────────────┘                 │
    └───────────────────────────────────────────────┘
                          │
               ┌──────────▼──────────┐
               │  Context Retrieval  │
               │       Agent         │
               └──────────┬──────────┘
                          │
               ┌──────────▼──────────┐
               │    GPT-4o           │
               │  (Azure OpenAI)     │
               └─────────────────────┘
```

---

## 8. Recommended Sprint Plan

| Sprint | Focus |
|--------|-------|
| Sprint 3 (now) | Enterprise UI polish |
| Sprint 4 | Replace rule-based agents with GPT agents |
| Sprint 5 | Chroma vector DB + Markdown knowledge indexing |
| Sprint 6 | Confluence API connector + sync pipeline |
| Sprint 7 | CMDB connector (ServiceNow API) |
| Sprint 8 | Azure AI Search migration + semantic reranker |
| Sprint 9 | Sentinel API integration (ARM template deploy) |
| Sprint 10 | Multi-tenant production release |

---

*Document maintained in `knowledge/architecture.md`*  
*Auto-renders in Platform Knowledge → Architecture tab*
