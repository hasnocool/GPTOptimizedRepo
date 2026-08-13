# GPTOptimizedRepo

A reference repository for getting more value from ChatGPT Plus across software development, research, project context, recurring monitoring, and consistent multi-agent engineering governance.

This repository is structured so ChatGPT Projects, Codex, Deep Research, Work, GitHub, Scheduled Tasks, and multiple terminal coding agents can share one durable source of truth.

## Workflow

```text
ChatGPT Project (project-only memory)
        |
        +-- Chat / Work
        +-- Deep Research
        +-- GitHub connection
        |
        v
GitHub repository (durable source of truth)
        |
        +-- AGENTS.md (canonical agent contract)
        +-- CLAUDE.md (OpenClaude / Claude compatibility)
        +-- opencode.json (OpenCode project configuration)
        +-- .omp/ (Oh My Pi context + sticky rules)
        +-- .prime/ (Prime skill)
        +-- standards/ (reusable engineering standards)
        +-- templates/ (starter project configuration)
        +-- scripts/ (mechanical governance checks)
        +-- .github/workflows/ (CI enforcement)
        +-- README.md / TODO.md / CHANGELOG.md
        +-- docs/ / research/
        |
        +--> Codex / OpenCode / OpenClaude / Pi / Oh My Pi / Prime workflows
        |
        +--> Scheduled Tasks monitor connected GitHub/web state
```

## Supported coding-agent harnesses

`AGENTS.md` is the canonical shared policy. Tool-specific files contain only compatibility glue or tool-specific additions so rules do not drift between agents.

- **Codex:** reads root `AGENTS.md`.
- **OpenCode:** reads root `AGENTS.md`; `opencode.json` also loads the durable project documents.
- **OpenClaude:** uses `CLAUDE.md`, which delegates shared policy to `AGENTS.md`.
- **Pi:** natively reads root `AGENTS.md`; no duplicate Pi policy is required.
- **Oh My Pi:** uses `.omp/AGENTS.md` plus sticky `.omp/RULES.md`.
- **Prime Intellect:** uses root `AGENTS.md` plus `.prime/skills/repo-governance/SKILL.md` for Prime-specific workflows.

## Python governance kit

The repository includes a reusable Python governance profile intended to be copied or adapted into other repositories:

- `standards/PYTHON.md` — Python 3.12+, organization, typing, dependencies, errors, configuration, logging, and definition-of-done rules.
- `standards/ASYNC_PYTHON.md` — non-blocking asyncio, structured concurrency, thread safety, bounded concurrency, timeouts, retries, subprocesses, and shutdown.
- `standards/TESTING.md` — deterministic tests, regression coverage, async testing, and performance-test guidance.
- `standards/SECURITY.md` — safe input handling, secrets, SQL, subprocesses, deserialization, paths, and resource bounds.
- `standards/PERFORMANCE.md` — CPU, memory, disk, database, and network-efficiency rules.
- `templates/python/pyproject.toml` — modern starter configuration for Python 3.12+, Ruff, mypy, and pytest.
- `templates/python/.gitignore` — standard Python caches, virtual environments, build outputs, and local-secret exclusions.
- `scripts/check_python_governance.py` — dependency-free AST/repository checks for common policy violations.
- `.github/workflows/python-governance.yml` — runs the governance checker on Python 3.12, 3.13, and 3.14.

For this repository:

```bash
python scripts/check_python_governance.py
```

For a conventional downstream Python repository using `src/`, `tests/`, and `pyproject.toml`:

```bash
python scripts/check_python_governance.py --strict-project
ruff format --check .
ruff check .
```

Then run the repository's configured type checker and tests.

## Start here

1. Use the ChatGPT Project named `GPTOptimizedRepo` with project-only memory.
2. Connect or reference this GitHub repository in the Project.
3. Use `AGENTS.md` as the repository-level operating contract for coding agents.
4. Use `docs/CODEX_WORKFLOW.md` for implementation tasks.
5. Use Deep Research for external uncertainty and save durable findings under `research/`.
6. Use `docs/SCHEDULED_TASKS.md` for recurring and conditional monitoring design.
7. For Python work, read the applicable files under `standards/` and run the mechanical governance checks.
8. Keep `TODO.md`, `CHANGELOG.md`, and this README aligned with repository changes.

## Operating principle

Do not rely on a single chat as the project database. Conversations are the working interface; GitHub is the durable state. Important decisions, research conclusions, operating rules, and implementation changes should end up in the repository.
