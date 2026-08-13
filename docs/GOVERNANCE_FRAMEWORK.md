# Governance Framework

This repository includes reusable engineering standards, project profiles, and mechanical checks for agent-assisted software development.

## Standards

The `standards/` directory covers Python, async/concurrency, architecture, dependencies, security, performance, testing, API design, databases, configuration, observability, reliability, documentation, releases, Git and pull requests, repository hygiene, licensing and provenance, deployment, CLI behavior, AI/LLM integrations, and coding-agent behavior.

Projects should also apply cross-cutting supply-chain and frontend rules: explicit CI/action versions, minimal workflow permissions, reproducible dependency resolution, traceable artifacts, accessible responsive interfaces, explicit loading/error states, configuration-driven endpoints, and appropriate automated frontend checks.

## Profiles

The `profiles/` directory provides practical policy selections for Python services, Python CLIs, FastAPI services, scrapers/crawlers, local AI services, and dashboards.

For data pipelines, combine the Python/async, architecture, dependency, security, performance, testing, database, configuration, observability, reliability, documentation, release, hygiene, deployment, licensing, and agent standards. Add restart-safe stages, durable progress, bounded memory, schema/provenance tracking, and throughput/error metrics.

## Mechanical enforcement

Run:

```bash
python scripts/check_repository_governance.py
```

Python repositories should additionally run:

```bash
python scripts/check_python_governance.py
```

Use `--strict-project` for downstream Python repositories that require `pyproject.toml`, `src/`, and `tests/`.

## Agent use

`AGENTS.md` remains the canonical agent contract. Apply the standards relevant to the change, use the closest project profile where available, run the matching checks, and keep documentation synchronized with behavior.
