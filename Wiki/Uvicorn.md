---
title: "Uvicorn"
tags:
  - python
  - asgi
  - server
  - async
created_date: "2026-07-19"
updated_date: "2026-07-19"
sources:
  - "Raw/Sources/FastAPI - FastAPI.md"
related:
  - "[[FastAPI]]"
  - "[[Starlette]]"
summary: "Uvicorn is a high-performance ASGI server for Python used to run FastAPI and Starlette applications, optionally with uvloop for maximum throughput."
---

# Uvicorn

> **Summary**: Uvicorn is a high-performance ASGI server for Python used to run FastAPI and Starlette applications, optionally with uvloop for maximum throughput.

## Core Concept

Uvicorn is the ASGI server that runs [[FastAPI]] and [[Starlette]] applications. It acts as the network entry point — receiving HTTP requests and passing them to the ASGI app. [[FastAPI]]'s `fastapi dev` CLI command starts a Uvicorn server automatically.

## Key Points

- **ASGI server**: Implements the Asynchronous Server Gateway Interface, enabling async Python web apps to handle concurrent connections efficiently.
- **Performance leader**: In TechEmpower benchmarks, Uvicorn itself ranks above both [[Starlette]] and [[FastAPI]], making it the performance ceiling for the entire stack.
- **uvloop**: The `uvicorn[standard]` install includes `uvloop`, an ultra-fast event loop implementation that significantly increases throughput on Linux/macOS.
- **Auto-reload**: `fastapi dev` starts Uvicorn with auto-reload enabled for local development workflows.
- **Included in `fastapi[standard]`**: Uvicorn (with `uvicorn[standard]`) is bundled as a standard dependency — no separate install required when using `pip install "fastapi[standard]"`.

## Usage

Started automatically via FastAPI CLI:
```bash
fastapi dev main.py    # development with auto-reload
fastapi run main.py    # production mode
```

Or directly:
```bash
uvicorn main:app --reload
```

## Role in FastAPI

Uvicorn is the **runtime server** dependency of [[FastAPI]], included via `fastapi-cli[standard]`. The source explicitly states it is used "for the server that loads and serves your application."

## Related Concepts

- [[FastAPI]]
- [[Starlette]]

## Source References

- [FastAPI - FastAPI.md](../Raw/Sources/FastAPI%20-%20FastAPI.md)

## Changelog

| Date | Change |
|---|---|
| 2026-07-19 | Initial creation via wiki-ingest |
