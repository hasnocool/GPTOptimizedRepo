# Sticky repository rules

- Follow the root `AGENTS.md` as the canonical project contract.
- Never commit secrets, API keys, authentication state, tokens, private keys, or `.env` contents.
- Preserve non-blocking async behavior and thread safety when asynchronous Python is introduced or modified.
- Run relevant validation before claiming a change is complete.
- Keep `README.md`, `TODO.md`, `CHANGELOG.md`, and affected documentation aligned with behavior changes.
- Do not publish, merge, rewrite history, or perform destructive Git operations unless the user explicitly requests it.
- Keep changes scoped; do not silently broaden the task.
