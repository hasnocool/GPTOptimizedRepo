# Changelog

## Unreleased

### Added
- Expanded reusable governance standards covering architecture, dependencies, APIs, databases, configuration, observability, reliability, documentation, releases, Git/PRs, repository hygiene, licensing/provenance, deployment, CLI behavior, AI/LLM integrations, and coding-agent behavior.
- Reusable project profiles for Python services, Python CLIs, FastAPI services, scrapers/crawlers, local AI/LLM services, and dashboards.
- Dependency-free `scripts/check_repository_governance.py` for repository-wide policy checks.
- GitHub Actions repository-governance workflow.
- `docs/GOVERNANCE_FRAMEWORK.md` describing the composable governance model and cross-cutting baselines.

### Changed
- Expanded README and TODO state to document the broader governance framework and remaining downstream validation work.

## [0.1.0] - 2026-08-13

### Added
- Repository-level agent guidance in `AGENTS.md`.
- ChatGPT Project setup instructions.
- Codex workflow guidance.
- Scheduled Task guidance.
- Initial Deep Research findings.
- Expanded README describing the combined workflow.
- OpenClaude and Claude-style compatibility via `CLAUDE.md`.
- OpenCode project configuration via `opencode.json`.
- Oh My Pi native project context and sticky rules under `.omp/`.
- Prime Intellect repository-governance skill under `.prime/skills/`.
- Shared multi-agent policy in `AGENTS.md` for Codex, OpenCode, OpenClaude, Pi, Oh My Pi, and Prime.
- Reusable Python engineering standards under `standards/` for core Python, async/concurrency, testing, security, and performance.
- Reusable Python starter configuration under `templates/python/`.
- Dependency-free `scripts/check_python_governance.py` for structural and AST-based policy checks.
- GitHub Actions Python governance workflow covering Python 3.12, 3.13, and 3.14.

### Changed
- Marked creation of the `GPTOptimizedRepo` ChatGPT Project complete in `TODO.md`.
- Updated `AGENTS.md` so supported agents apply the reusable Python standards and mechanical checks when modifying Python.
- Updated README and TODO state to document the Python governance kit and remaining downstream validation work.
