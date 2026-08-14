# Profile: Scraper / Crawler

Apply: PYTHON, ASYNC_PYTHON, ARCHITECTURE, DEPENDENCIES, SECURITY, PERFORMANCE, TESTING, DATABASE, CONFIGURATION, OBSERVABILITY, RELIABILITY, DOCUMENTATION, RELEASES, GIT_AND_PRS, REPOSITORY_HYGIENE, DEPLOYMENT, LICENSING_IP, and AGENT_BEHAVIOR.

Additional requirements:
- bounded concurrency, connection pooling, explicit request timeouts, rate limits, and exponential backoff with jitter;
- resumable frontier/checkpoint state and restart-safe jobs;
- deduplication and idempotent persistence;
- batch database writes when it improves throughput without risking excessive loss on failure;
- preserve source URL/timestamp/provenance for extracted records;
- avoid unbounded in-memory queues or whole-dataset loading;
- expose crawl throughput, HTTP outcomes, retry counts, queue depth, and storage latency;
- keep extraction fixtures so parser changes can be tested offline.
