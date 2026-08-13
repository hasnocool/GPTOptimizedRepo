# Profile: Local AI / LLM Service

Apply: PYTHON, ASYNC_PYTHON, ARCHITECTURE, DEPENDENCIES, SECURITY, PERFORMANCE, TESTING, API, CONFIGURATION, OBSERVABILITY, RELIABILITY, AI_LLM, DOCUMENTATION, RELEASES, GIT_AND_PRS, REPOSITORY_HYGIENE, DEPLOYMENT, LICENSING_IP, and AGENT_BEHAVIOR.

Additional requirements:
- isolate provider/model adapters behind a common interface;
- record model identity, quantization/runtime, latency, tokens, memory use, and failures where available;
- bound prompt/context/output size, concurrent inference, retries, and total resource budget;
- validate structured outputs before downstream use;
- support explicit fallback ordering and distinguish retry from fallback;
- avoid blocking inference orchestration on an asyncio event loop; offload CPU-bound/blocking runtimes deliberately;
- use fixtures or deterministic stubs for normal tests rather than requiring live inference;
- document privacy and external-provider data handling for any cloud fallback.
