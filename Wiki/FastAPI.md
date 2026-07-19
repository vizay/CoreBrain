---
title: "FastAPI"
tags:
  - web-framework
  - python
  - api
  - rest
  - openapi
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/FastAPI - FastAPI.md"
related:
  - "[[Pydantic]]"
  - "[[Starlette]]"
  - "[[Uvicorn]]"
  - "[[OpenAPI]]"
summary: "FastAPI is a modern, high-performance Python web framework for building APIs using standard Python type hints, backed by Pydantic and Starlette."
---

# FastAPI

> **Summary**: FastAPI is a modern, high-performance Python web framework for building APIs using standard Python type hints, backed by Pydantic and Starlette.

## Core Concept

FastAPI is a Python web framework designed for building APIs rapidly without sacrificing performance or correctness. It leverages standard Python type hints to drive automatic data validation, serialization, and interactive API documentation — all without requiring any custom DSL or code generation step.

It is built on two core libraries:
- [[Pydantic]] — for data validation and settings management
- [[Starlette]] — for the ASGI web layer (routing, middleware, WebSockets)

## Key Points

- **Performance**: Benchmarked on par with NodeJS and Go; one of the fastest Python frameworks, only below Starlette and [[Uvicorn]] themselves.
- **Type-hint driven**: A single parameter declaration (`item_id: int`) automatically provides editor completion, type checking, validation, error messages, and API docs.
- **Standards-based**: Fully compatible with [[OpenAPI]] (formerly Swagger) and JSON Schema. Generates interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) automatically.
- **Async-native**: Supports both `def` and `async def` route handlers transparently.
- **Developer velocity**: Internal team estimates ~200–300% speed increase in feature development vs. alternatives.
- **Production-ready**: Used in production by Microsoft (ML services), Uber (Ludwig predictions), Netflix (Dispatch), and Cisco.

## Installation

```bash
pip install "fastapi[standard]"
```

The `[standard]` extra includes [[Uvicorn]] with high-performance extras, `fastapi-cli`, HTTPX (for testing), Jinja2, and `python-multipart`.

## Minimal Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

Run with:
```bash
fastapi dev main.py   # development (auto-reload)
```

## Advanced Features (from source)

- Dependency Injection system
- OAuth2 + JWT token authentication
- HTTP Basic auth
- Deeply nested JSON model validation (via [[Pydantic]])
- GraphQL integration (Strawberry)
- WebSockets (via [[Starlette]])
- CORS, Cookie Sessions
- HTTPX-based testing utilities

## Related Concepts

- [[Pydantic]]
- [[Starlette]]
- [[Uvicorn]]
- [[OpenAPI]]

## Source References

- [FastAPI - FastAPI.md](../Raw/Sources/FastAPI%20-%20FastAPI.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation via wiki-ingest |
