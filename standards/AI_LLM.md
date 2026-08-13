# AI and LLM Governance

- Put model/provider access behind explicit interfaces so business logic is not coupled to one vendor.
- Define timeout, retry, fallback, and circuit-breaking behavior for inference calls.
- Track model identity/version, prompt/template version, token usage, latency, and cost when those affect operation.
- Validate structured model output before using it as trusted application data.
- Treat model output as untrusted input when it can influence commands, file writes, network calls, database mutations, or user-visible facts.
- Keep prompts/templates versioned when changes can alter production behavior.
- Use deterministic fixtures or recorded responses for ordinary tests instead of relying on live paid inference.
- Define fallback behavior across cloud, local, and alternate providers when resilience or cost control matters.
- Bound context size, output size, retries, parallel calls, and total budget.
- Document privacy/data-retention implications before sending sensitive content to external inference services.
- Cache only when correctness, privacy, and invalidation semantics are understood.
- Evaluation criteria should measure task quality and failure modes rather than relying only on subjective spot checks.
