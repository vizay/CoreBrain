---
title: "Pydantic"
tags:
  - python
  - validation
  - data-modeling
  - type-hints
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/FastAPI - FastAPI.md"
related:
  - "[[Core: FastAPI]]"
  - "[[Core: Starlette]]"
summary: "Pydantic is a Python data validation library that uses standard type hints to validate, parse, and serialize data at runtime."
---

# Pydantic

> **Summary**: Pydantic is a Python data validation library that uses standard type hints to validate, parse, and serialize data at runtime.

## Core Concept

Pydantic is the data layer powering [[Core: FastAPI]]. It takes ordinary Python type annotations on class attributes or function parameters and enforces them at runtime — converting raw inputs (JSON, path params, query strings) into correctly typed Python objects, and raising clear validation errors when data is invalid.

## Key Points

- **Type-hint driven**: Define a model by subclassing `BaseModel` and annotating fields with Python types — Pydantic handles validation automatically.
- **Deeply nested support**: Validation works for arbitrarily nested JSON objects, not just flat structures.
- **Conversion in both directions**: Input (network → Python) and output (Python → JSON/network) conversion are both handled.
- **Clear error messages**: When validation fails, clients receive structured, readable error responses — not stack traces.
- **Optional dependencies**:
  - `pydantic-settings` — for settings/config management from environment variables
  - `pydantic-extra-types` — additional type definitions (e.g., color, payment cards)
  - `email-validator` — for email field validation (included in `fastapi[standard]`)

## Example (from source)

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
```

With this single declaration, [[Core: FastAPI]] validates incoming `PUT` bodies automatically, including type coercion and optional field handling.

## Role in FastAPI

Pydantic is listed as a **core requirement** of [[Core: FastAPI]]. It handles:
- Request body parsing and validation
- Query parameter type coercion
- Response model serialization
- Settings management (via `pydantic-settings`)

## Related Concepts

- [[Core: FastAPI]]
- [[Core: Starlette]]

## Source References

- [FastAPI - FastAPI.md](../Raw/Sources/FastAPI%20-%20FastAPI.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation via wiki-ingest |
