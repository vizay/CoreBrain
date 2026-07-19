---
title: "Starlette"
tags:
  - python
  - asgi
  - web-toolkit
  - async
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/FastAPI - FastAPI.md"
related:
  - "[[FastAPI]]"
  - "[[Uvicorn]]"
summary: "Starlette is a lightweight ASGI web toolkit for Python that provides the web layer (routing, middleware, WebSockets, CORS) underlying FastAPI."
---

# Starlette

> **Summary**: Starlette is a lightweight ASGI web toolkit for Python that provides the web layer (routing, middleware, WebSockets, CORS) underlying FastAPI.

## Core Concept

Starlette is the web layer that [[FastAPI]] is built on. It provides all low-level HTTP routing, middleware, request/response handling, and async support. FastAPI adds the type-hint-driven validation, dependency injection, and automatic API documentation layer on top of Starlette's foundation.

## Key Points

- **ASGI-native**: Designed for the Asynchronous Server Gateway Interface standard, enabling high concurrency with [[Uvicorn]].
- **Performance**: In TechEmpower independent benchmarks, Starlette itself ranks above [[FastAPI]] (since FastAPI adds overhead on top). FastAPI's performance is described as "only below Starlette and Uvicorn themselves."
- **Features provided to FastAPI** (sourced from FastAPI docs):
  - WebSockets
  - CORS (Cross-Origin Resource Sharing)
  - Cookie Sessions
  - `TestClient` (via HTTPX integration)
  - Jinja2 template support
  - Form parsing (via `python-multipart`)
- **Standard dependencies** installed via `fastapi[standard]`:
  - `httpx` — for the `TestClient`
  - `jinja2` — for default template config
  - `python-multipart` — for form/file parsing

## Role in FastAPI

Listed as one of two **core requirements** of [[FastAPI]] (alongside [[Pydantic]]). The source states: "FastAPI stands on the shoulders of giants: Starlette for the web parts, Pydantic for the data parts."

## Related Concepts

- [[FastAPI]]
- [[Uvicorn]]

## Source References

- [FastAPI - FastAPI.md](../Raw/Sources/FastAPI%20-%20FastAPI.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation via wiki-ingest |
