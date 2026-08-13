# Codex Workflow

## Goal

Use Codex as the implementation and verification engine for repository work while keeping GitHub as the auditable source of truth.

## Recommended loop

### 1. Orient

Ask Codex to inspect:

- `AGENTS.md`
- `README.md`
- `TODO.md`
- `CHANGELOG.md`
- the relevant source/tests/docs
- current git status and branch

### 2. Plan

For non-trivial work, request:

- current behavior;
- desired behavior;
- affected files;
- compatibility risks;
- tests/checks to run;
- documentation that must change.

### 3. Implement

Keep the patch coherent and scoped. Prefer existing dependencies and architecture unless replacing them has a measurable benefit.

For Python work, target Python 3.12+ and ensure asynchronous paths do not perform blocking disk/network/process work on the event loop. Use async-native libraries or move unavoidable blocking operations to an appropriate worker/thread boundary.

### 4. Validate

Codex should run the strongest checks the repository provides, such as:

- unit/integration tests;
- linting/formatting;
- static typing;
- build/package validation;
- targeted smoke tests.

Failures must be explained rather than ignored.

### 5. Review the final diff

Before publishing, explicitly inspect for:

- accidental secrets;
- unrelated edits;
- generated/cache files;
- stale docs;
- missing tests;
- blocking I/O in asynchronous code;
- backwards compatibility regressions.

### 6. Publish through a PR

Use feature branches for meaningful changes. The PR should explain what changed, why, validation performed, risks, and follow-up work.

## Useful Codex prompt pattern

```text
Read AGENTS.md and the repository documentation first.

Task: <specific outcome>

Before editing, inspect the current implementation and give me a concise plan with acceptance criteria and validation steps. Then implement the complete change, run the relevant tests/checks, inspect the final diff for regressions and secrets, and update README/CHANGELOG/TODO/docs where required. Keep existing behavior intact unless the task explicitly changes it.
```

## When not to use Codex

Use normal Chat for quick explanation or planning. Use Deep Research when the core uncertainty is external knowledge rather than repository implementation. Use Work for a long deliverable spanning multiple apps/files when code editing is not the primary task.
