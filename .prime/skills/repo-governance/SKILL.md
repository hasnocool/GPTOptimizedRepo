---
name: repo-governance
description: Apply GPTOptimizedRepo repository governance before implementation, review, evaluation, or training changes.
---

# Repository governance

Use the repository root `AGENTS.md` as the canonical operating contract.

Before changing this workspace:

1. Read `AGENTS.md`.
2. Read `README.md`, `TODO.md`, `CHANGELOG.md`, and relevant documentation.
3. Keep changes narrow and verifiable.
4. Run the most relevant validation available.
5. Keep documentation aligned with behavior.
6. Never commit credentials, API keys, authentication state, or generated secret material.
7. When Python is involved, target Python 3.12+ and preserve non-blocking, thread-safe asynchronous behavior.

Prime-specific experiments, evaluations, or training work must not silently alter the general repository contract. Put shared policy in `AGENTS.md` and Prime-specific workflow guidance in this skill.
