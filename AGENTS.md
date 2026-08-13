# AGENTS.md

## Purpose

This repository is a reference workspace for using ChatGPT Projects, Codex, Deep Research, Work, GitHub, and Scheduled Tasks together without losing project context or letting documentation drift.

## Before every task

1. Read `README.md`, `TODO.md`, `CHANGELOG.md`, and the relevant files under `docs/`.
2. Inspect the current repository state before modifying anything.
3. Define the smallest coherent implementation scope.
4. Prefer existing project conventions over introducing new ones.
5. Preserve backwards compatibility unless the task explicitly requires a breaking change.
6. Never commit credentials, tokens, secrets, private keys, `.env` contents, or generated credential files.
7. When Python is introduced, target Python 3.12+.
8. For asynchronous Python, use non-blocking I/O and thread-safe operations; move unavoidable blocking work off the event loop.
9. Add or update tests for behavior changes.
10. Update documentation in the same change when behavior, workflow, architecture, or user-facing instructions change.

## Task lifecycle

For implementation work, use this sequence:

1. **Orient** — inspect architecture, open issues/PRs, TODOs, and recent changes.
2. **Plan** — state assumptions, acceptance criteria, risks, and affected files.
3. **Implement** — make the smallest complete change.
4. **Validate** — run the most relevant tests, linters, type checks, and smoke checks available.
5. **Review** — inspect the final diff for regressions, secrets, generated junk, blocking I/O, and unnecessary scope.
6. **Document** — update `README.md`, `CHANGELOG.md`, `TODO.md`, and affected docs.
7. **Publish** — use a feature branch and pull request for non-trivial changes.

## Documentation governance

- `README.md` describes the current user-facing state.
- `TODO.md` describes planned work only; completed work should be removed or marked complete with a reference.
- `CHANGELOG.md` records meaningful repository changes.
- `docs/` holds deeper workflows, architecture, research, and operating guides.
- Do not allow code or workflow changes to make these documents stale.

## Codex operating rules

When using Codex:

- Start by reading this file and the repository documentation.
- Ask Codex for a repo-level plan before broad changes.
- Prefer narrow, reviewable commits and PRs.
- Run commands/tests rather than assuming a change works.
- Inspect the diff before publishing.
- Do not silently broaden scope.
- Treat research conclusions as hypotheses until verified against authoritative sources or the repository itself.
- If a task can be parallelized safely, separate independent research, testing, and implementation work rather than interleaving unrelated edits.

## Research rules

Deep Research outputs should:

- answer a concrete decision question;
- prefer primary/official sources where possible;
- record source date and access date for time-sensitive claims;
- distinguish facts, inference, and recommendations;
- identify unresolved questions and follow-up experiments;
- be saved under `research/` when they materially affect future work.

## Scheduled-task rules

Scheduled Tasks should monitor external or connected state, not depend on ChatGPT Project file attachments. For this repository, use GitHub as the durable source for recurring checks. Tasks should notify only when there is a meaningful action, risk, regression, dependency update, failed CI state, stale PR, or research development worth reviewing.

## Security

- Never print or commit secrets.
- Use secret managers, environment variables, or GitHub Actions secrets for credentials.
- Redact accidental credentials from logs and documentation.
- Avoid destructive Git operations unless explicitly required.

## Definition of done

A task is done only when its implementation, validation, documentation, and next-step state agree with each other.
