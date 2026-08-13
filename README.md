# GPTOptimizedRepo

A reference repository for getting more value from ChatGPT Plus across software development, research, project context, and recurring monitoring.

This repository is structured so ChatGPT Projects, Codex, Deep Research, Work, GitHub, and Scheduled Tasks can work together around one durable source of truth.

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
        +-- AGENTS.md
        +-- README.md
        +-- TODO.md
        +-- CHANGELOG.md
        +-- docs/
        +-- research/
        |
        +--> Codex implementation / testing / review
        |
        +--> Scheduled Tasks monitor connected GitHub/web state
```

## Start here

1. Read `docs/CHATGPT_PROJECT_SETUP.md` and create a ChatGPT Project named `GPTOptimizedRepo` with project-only memory.
2. Connect or reference this GitHub repository in the Project.
3. Use `AGENTS.md` as the repository-level operating contract for coding agents.
4. Use `docs/CODEX_WORKFLOW.md` for implementation tasks.
5. Use Deep Research for external uncertainty and save durable findings under `research/`.
6. Use `docs/SCHEDULED_TASKS.md` for recurring and conditional monitoring design.
7. Keep `TODO.md`, `CHANGELOG.md`, and this README aligned with repository changes.

## Operating principle

Do not rely on a single chat as the project database. Conversations are the working interface; GitHub is the durable state. Important decisions, research conclusions, operating rules, and implementation changes should end up in the repository.
