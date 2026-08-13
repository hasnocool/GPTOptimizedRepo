# Async Python Standard

Read this in addition to `standards/PYTHON.md` whenever Python concurrency, networking, subprocesses, filesystem work, databases, queues, workers, or background tasks are involved.

## Event-loop safety

- Async code must remain non-blocking.
- Never call `time.sleep()` from `async def`; use `asyncio.sleep()`.
- Do not perform blocking network, filesystem, subprocess, database, or CPU-heavy work directly on an asyncio event-loop thread.
- Prefer native async APIs. When unavoidable blocking work must be called, offload it safely with `asyncio.to_thread()`, an executor, or a process pool as appropriate.
- Do not use `requests` in async execution paths; prefer the project's async HTTP client.

## Structured concurrency

- Prefer `asyncio.TaskGroup` when related tasks share a lifecycle.
- Do not create untracked fire-and-forget tasks.
- Retain task references and define cancellation/error behavior.
- Propagate cancellation correctly; do not broadly catch exceptions in ways that hide cancellation.
- Bound task creation, worker counts, queue sizes, fan-out, and retry loops.

## Synchronization

- Use `asyncio.Lock`, `Semaphore`, `Event`, `Condition`, or queues for asyncio-owned state as appropriate.
- Use thread-safe synchronization for state shared across threads.
- Do not assume normal mutable containers become safe merely because operations appear atomic on one interpreter.
- Avoid holding locks across slow or unbounded external I/O unless serialization is an explicit invariant.

## Network I/O

- Configure explicit connection and request timeouts.
- Reuse long-lived clients/connection pools rather than opening a new connection per operation.
- Retry only failures that are safe to retry.
- Use bounded exponential backoff with jitter for transient failures.
- Respect rate limits and implement backpressure.

## Filesystem and subprocesses

- For significant filesystem work in async paths, use an async-capable API or move blocking work off the event loop.
- Stream large files instead of loading them entirely into memory when practical.
- Avoid `subprocess.run`, `Popen.wait`, or similar blocking subprocess calls in async functions; use `asyncio.create_subprocess_exec()` / `create_subprocess_shell()` when asynchronous subprocess control is required.
- Prefer argument arrays and avoid shell invocation unless shell semantics are genuinely necessary.

## Shutdown and lifecycle

- Services must define clean startup and shutdown behavior.
- Cancel and await background tasks during shutdown.
- Close network clients, pools, files, queues, and subprocess transports deterministically.
- Avoid orphan threads/processes/tasks.

## Review checklist

Before merging async changes, verify:

1. No event-loop blocking calls were introduced.
2. Every spawned task has an owner and lifecycle.
3. Concurrency and queues are bounded.
4. Cancellation and shutdown paths work.
5. Timeouts exist around external operations.
6. Retries are bounded and safe.
7. Shared mutable state is synchronized appropriately.
8. Blocking compatibility bridges are explicitly offloaded.
