# Python Performance Standard

- Optimize measured bottlenecks rather than guessing.
- Prefer better algorithms and data structures before micro-optimizing syntax.
- Avoid repeated serialization, filesystem scans, network handshakes, database queries, and unnecessary copies.
- Reuse connection pools and clients.
- Stream or iterate over large datasets where practical instead of loading everything into memory.
- Batch database/network operations when doing so reduces round trips without creating excessive latency or memory use.
- Use bounded queues and worker pools; do not create unlimited tasks, threads, or processes.
- Keep caches explicit, bounded, invalidatable, and observable.
- Avoid unnecessary disk writes when content has not changed; use atomic replacement for important state files.
- Profile CPU, memory, disk I/O, and network I/O separately because each class of bottleneck requires different fixes.
- For CPU-heavy work in async applications, use process-based parallelism or another execution mechanism that does not block the event loop.
- Add a benchmark or reproducible measurement when a performance characteristic is part of the feature contract.
- Record before/after measurements for performance-focused changes.
