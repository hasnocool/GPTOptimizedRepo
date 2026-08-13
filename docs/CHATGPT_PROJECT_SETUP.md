# ChatGPT Project Setup

## Recommended project configuration

Create a new ChatGPT Project named `GPTOptimizedRepo` and choose **Project-only memory** during creation. This keeps repository discussions, uploaded files, and project chats isolated from unrelated conversations.

Project-only memory must be selected when creating the project; existing projects cannot later be converted to project-only memory.

## Add these project sources

Use GitHub as the durable source of truth. In the ChatGPT Project, add or reference:

- the `hasnocool/GPTOptimizedRepo` repository through the GitHub connection;
- `AGENTS.md`;
- `README.md`;
- `TODO.md`;
- `CHANGELOG.md`;
- the files under `docs/` and `research/` that are relevant to the current task.

Avoid copying secrets or `.env` files into project context.

## Suggested Project instructions

Use this repository as the authoritative project context. Read `AGENTS.md` before implementation work. Prefer current repository state over assumptions from old chats. Keep tasks narrow and verifiable. For code changes, plan first, preserve existing behavior unless explicitly changing it, run the most relevant tests and checks, inspect the final diff, and update documentation in the same change. Never expose or commit credentials. When Python is introduced, target Python 3.12+ and keep asynchronous I/O non-blocking and thread-safe.

## Conversation organization

Use separate chats for durable workstreams rather than one giant chat:

- `Architecture and roadmap`
- `Implementation / Codex`
- `Deep Research`
- `PR and CI review`
- `Product and monetization analysis`
- `Operations and scheduled monitoring`

Keep decisions that need to survive chat history in the repository, not only in conversation memory.

## What belongs where

| Need | Best surface |
| --- | --- |
| Quick questions, planning, review | Chat |
| Long multi-step deliverables | Work |
| Repository implementation/testing | Codex |
| Multi-source investigation with citations | Deep Research |
| Durable project decisions | GitHub repository |
| Repeated or conditional monitoring | Scheduled Tasks |

## Why GitHub remains the source of truth

Scheduled Tasks cannot access files attached to a ChatGPT Project. GitHub therefore provides the persistent external state that both interactive chats and recurring monitoring can inspect.
