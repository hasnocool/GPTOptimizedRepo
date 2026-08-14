# API Governance

- Treat public HTTP/RPC/event schemas as compatibility contracts.
- Validate external input at the boundary and convert it into well-defined internal types early.
- Use explicit API versions when compatibility cannot otherwise be preserved.
- Breaking changes require migration notes and a deliberate version change.
- Define consistent error shapes, status semantics, pagination, filtering, and request identifiers.
- Set explicit timeouts for outbound calls and propagate meaningful timeout/cancellation failures.
- Make retryable operations idempotent where practical; document idempotency behavior for writes.
- Avoid leaking database/vendor objects directly through public APIs.
- Keep generated OpenAPI/schema artifacts synchronized when applicable.
- Deprecations need an announced replacement and removal window when users may depend on the old behavior.

## Review checklist

API changes must identify compatibility impact, authorization implications, validation rules, failure semantics, observability, and tests for both success and expected failure paths.
