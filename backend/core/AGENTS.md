# AGENTS.md

## Project Goals

This repository is an enterprise AI Detection Engineering Platform. Its purpose is to help security teams design, generate, validate, review, and document production-grade detection engineering content.

Primary goals:

- Generate Microsoft Sentinel detections with high-quality KQL.
- Map detections to MITRE ATT&CK tactics and techniques.
- Produce structured, validated detection outputs.
- Support repeatable workflows for planning, generation, review, documentation, and export.
- Keep business logic independent from UI frameworks.
- Prepare the codebase for future RAG, LangGraph, and Azure OpenAI integrations.

## Folder Responsibilities

- `backend/core/`: Core configuration, provider clients, shared infrastructure, and repository-level engineering guidance.
- `backend/services/`: Business services and orchestration logic. Services should coordinate prompts, clients, schemas, validators, and domain workflows.
- `backend/schemas/`: Pydantic request and response models. These define public contracts between layers.
- `backend/prompts/`: Prompt templates and prompt builders. Prompt construction belongs here, not in services or UI.
- `backend/api/`: Future API routes, controllers, and dependency wiring.
- `backend/models/`: Future domain models that are not API schemas.
- `backend/utils/`: Small reusable utilities with no business-specific ownership.
- `agents/`: Future specialized agent implementations, such as KQL generation, MITRE mapping, review, and documentation.
- `frontend/`: Future UI only. UI code must not contain detection generation business logic.
- `rag/`: Future retrieval, ingestion, vectorstore, and knowledge grounding components.
- `knowledge/`: Curated detection engineering knowledge, examples, templates, standards, and reference material.
- `parsers/`: Future parsers for Sigma, YAML, JSON, KQL, documentation, or uploaded detection content.
- `generators/`: Future output generators for rules, documents, exports, or platform-specific artifacts.
- `workflows/`: Future workflow orchestration definitions.
- `tests/`: Unit and integration tests.
- `docs/`: Human-facing documentation.
- `scripts/`: Developer or operational scripts. Scripts must not become hidden application entrypoints.
- `config/`: Non-secret configuration files.
- `data/`: Local input or processed data. Do not commit sensitive customer data.
- `outputs/`: Generated artifacts. Treat as disposable unless explicitly promoted to fixtures or examples.
- `logs/`: Runtime logs. Do not commit logs.

## Coding Standards

- Write production-quality, maintainable code.
- Keep modules focused and small.
- Keep business logic outside UI files.
- Prefer explicit dependencies over hidden global behavior.
- Avoid unrelated refactors when implementing a feature.
- Do not duplicate prompt, schema, or provider logic across layers.
- Do not hardcode secrets, tenant values, model names, or environment-specific URLs.
- Use clear, professional docstrings for public classes, functions, and service methods.
- Use type hints for all function parameters, return values, class attributes, and important local variables.
- Prefer simple, readable code over clever abstractions.

## Architecture

Follow a layered architecture:

1. UI or API layer receives input and returns output.
2. Service layer owns business workflow and orchestration.
3. Prompt layer builds model instructions and user prompts.
4. LLM abstraction layer coordinates provider-specific clients.
5. Provider client layer communicates with OpenAI or future providers.
6. Schema layer validates all structured inputs and outputs.

Rules:

- UI and API layers must call services, not provider clients.
- Services should call `LLMService`, not `OpenAIClient` directly, unless implementing the LLM abstraction itself.
- Provider-specific code belongs in `backend/core/` or a future provider package.
- Prompt construction belongs in `backend/prompts/`.
- Pydantic schemas define contracts between layers.
- Detection output must be validated before being returned from business services.

## Python Standards

- Target Python 3.13.
- Use modern Python typing syntax, such as `list[str]`, `dict[str, Any]`, and `str | None`.
- Prefer `pathlib.Path` over string paths for filesystem work.
- Use standard library features before adding dependencies.
- Avoid mutable default arguments.
- Keep imports ordered: standard library, third-party, local application.
- Avoid broad `except Exception` unless adding context and re-raising or converting to a domain error.
- Do not use print statements for application logging.

## OpenAI SDK Standards

- Use OpenAI Python SDK 2.x.
- Use the Responses API for model generation.
- Read model and provider configuration from `backend/core/config.py`.
- Use `MODEL_NAME` from configuration.
- Request structured JSON outputs for machine-consumed responses.
- Never rely on markdown parsing for production data contracts.
- Keep OpenAI-specific exceptions and SDK details inside the provider client layer.
- Convert provider failures into clear application exceptions with useful context.
- Do not expose API keys, raw secrets, or full sensitive prompts in logs.
- Keep the LLM service as the abstraction boundary for future provider changes.

## Pydantic Usage

- Use Pydantic models for request and response contracts.
- Validate all LLM-generated structured output before returning it from services.
- Prefer explicit field names that match domain language.
- Add field descriptions when schemas become API-facing or externally documented.
- Use model validation instead of manual dictionary access when possible.
- Do not pass unvalidated dictionaries deep into business logic.

## Git Workflow

- Keep commits focused on one logical change.
- Do not commit secrets, `.env`, logs, virtual environments, generated caches, or disposable outputs.
- Preserve unrelated user changes.
- Do not rewrite history or reset work without explicit approval.
- Use clear commit messages that describe the behavioral change.
- Before committing, run relevant tests and formatting checks when available.

## Testing Strategy

- Unit test prompt builders, schemas, services, and validators.
- Mock OpenAI provider calls in unit tests.
- Add integration tests for end-to-end generation paths when provider access is intentionally enabled.
- Test error cases, including invalid JSON, missing fields, provider failures, and schema validation failures.
- Keep tests deterministic by default.
- Do not require network access for normal unit tests.
- Add regression tests for every fixed bug.

## Naming Conventions

- Use `snake_case` for modules, functions, variables, and file names.
- Use `PascalCase` for classes and Pydantic models.
- Use `UPPER_SNAKE_CASE` for constants.
- Service classes should end with `Service`.
- Provider client classes should end with `Client`.
- Prompt builder functions should begin with `build_`.
- Schema names should describe their contract, such as `DetectionRequest` or `DetectionResponse`.

## SOLID Principles

- Single Responsibility: each module and class should have one clear reason to change.
- Open/Closed: add new providers, workflows, or output formats through extension points rather than rewriting core logic.
- Liskov Substitution: future provider clients should satisfy the same behavior expected by service abstractions.
- Interface Segregation: keep abstractions small and task-specific.
- Dependency Inversion: business services should depend on abstractions, not concrete SDK details.

## Prompt Engineering Rules

- Keep prompts versionable, centralized, and reusable.
- Do not embed large prompts directly in services or UI.
- System prompts define role, constraints, output format, and safety boundaries.
- User prompts define task-specific inputs.
- Require JSON for structured outputs.
- Explicitly prohibit markdown when the response is consumed by code.
- Include expected fields and domain constraints in prompts.
- Keep prompts deterministic where practical.
- Avoid leaking secrets or sensitive customer data into prompts.
- Future prompt changes should be tested against representative detection requests.

## Logging Standards

- Use the `logging` module for application logs.
- Configure log level through settings.
- Log major workflow steps, provider failures, validation failures, and operational errors.
- Do not log API keys, bearer tokens, customer secrets, or sensitive detection data.
- Prefer structured log messages that include stable identifiers when available.
- Avoid noisy logs in tight loops or prompt construction paths.

## Error Handling

- Fail fast on missing required configuration.
- Wrap provider-specific exceptions at the provider boundary.
- Raise clear errors that explain what failed and where.
- Preserve original exceptions with exception chaining using `raise ... from exc`.
- Validate external inputs and LLM outputs before use.
- Keep error messages professional and actionable.
- Do not silently fall back to unsafe or unvalidated behavior.

## Future Azure OpenAI Compatibility

Design provider integration so Azure OpenAI can be added without changing business services.

Guidelines:

- Keep provider-specific configuration isolated.
- Avoid hardcoding OpenAI public endpoint assumptions outside provider clients.
- Ensure the LLM service can route to different provider clients in the future.
- Keep request and response contracts provider-neutral.
- Do not expose OpenAI SDK-specific response objects outside provider clients.

## Future LangGraph Compatibility

Design workflows so they can later be represented as LangGraph nodes and edges.

Guidelines:

- Keep agent responsibilities explicit and small.
- Use Pydantic models for state passed between workflow steps.
- Keep side effects isolated in services or provider clients.
- Prefer pure prompt builders and validators where possible.
- Make workflow steps independently testable.
- Do not couple agent logic to UI or API frameworks.
