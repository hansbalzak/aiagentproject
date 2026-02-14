# Tracing and Observability

## 1. Purpose

This project implements local tracing to ensure auditability,
debuggability, and behavioral transparency.

Tracing exists to answer:

- What happened?
- When did it happen?
- Why did the agent behave this way?
- Which internal systems were involved?

This is not telemetry.
This is local observability.

---

## 2. Trace Model

Each user interaction is assigned a unique trace identifier (`trace_id`).

A trace records:

- Timestamp (start / end)
- Model configuration (model, temperature, token limits)
- Context size (character counts)
- Tool invocations (type, arguments, bounded output)
- Claim extraction results
- Reflection results (when enabled)
- Errors and recovery paths

Traces are written to:
traces/YYYY-MM-DD.jsonl
