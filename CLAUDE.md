# CLAUDE.md

This repository uses `AGENTS.md` as the canonical operating contract for all coding agents.

Before doing any work:

1. Read `AGENTS.md` in full.
2. Follow its task lifecycle, security, testing, documentation, async/thread-safety, and publication rules.
3. Read `README.md`, `TODO.md`, `CHANGELOG.md`, and relevant files under `docs/` before broad changes.
4. Treat this file as a compatibility entrypoint, not a second independent policy source.

## OpenClaude / Claude-style compatibility

OpenClaude and Claude-compatible harnesses should preserve the same repository behavior as Codex and other agents. Do not create conflicting instructions here. If a Claude/OpenClaude-specific rule becomes necessary, add only that delta below and keep shared policy in `AGENTS.md`.

## Tool-specific delta

- Prefer repository-native tools and existing scripts before inventing new automation.
- For broad changes, form a plan before editing and validate the final diff before publishing.
- Never place API keys, provider credentials, authentication exports, or session material in this repository.
