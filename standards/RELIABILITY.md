# Reliability Governance

- Every external I/O operation should have an explicit timeout or bounded deadline.
- Retries must be bounded, limited to failures that are plausibly transient, and safe for the operation being retried.
- Prefer exponential backoff with jitter; never create tight infinite retry loops.
- Bound queues, worker counts, task creation, thread/process pools, buffers, and fan-out.
- Preserve backpressure instead of converting overload into unbounded memory growth.
- Long-running jobs should be restart-safe and idempotent or checkpointed when practical.
- Define graceful startup/shutdown behavior and cancellation semantics.
- Critical state writes should be atomic or transactional where partial writes would corrupt recovery.
- Degraded dependency behavior should be explicit: fail closed, fail open, serve stale data, queue work, or disable a feature deliberately.
- Circuit breakers and bulkheads are appropriate when they solve a demonstrated failure-amplification problem, not as default complexity.
- Recovery procedures for important persistent state should be tested periodically.
