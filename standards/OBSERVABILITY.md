# Observability Governance

- Use structured logging for application diagnostics; libraries must not configure the root logger.
- Never log secrets, tokens, passwords, authorization headers, entire environments, or unnecessarily sensitive payloads.
- Attach request/job/trace correlation identifiers where asynchronous or distributed work crosses boundaries.
- Define stable metric names, units, labels, and ownership; avoid unbounded-cardinality labels.
- Services should expose appropriate health/readiness signals that distinguish process liveness from dependency readiness.
- Background-task failures must be surfaced; do not let task exceptions disappear silently.
- Alert on actionable symptoms and sustained failures rather than every transient error.
- Avoid logging the same exception at every layer.
- Important external calls should expose latency, outcome, retry, and saturation information where practical.
- Operational dashboards and runbooks should map signals to concrete actions.
