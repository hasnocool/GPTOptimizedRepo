# ChatGPT Plus Repository Workflow Research

Date: 2026-08-13

## Question

How should a software repository be organized to make effective use of ChatGPT Projects, Codex, Deep Research, Work, GitHub, and Scheduled Tasks?

## Conclusion

Use GitHub as the durable source of truth. Use a ChatGPT Project with project-only memory as the interactive context boundary. Use Codex for implementation, review, and testing. Use Deep Research for external multi-source questions. Use Work for long multi-step deliverables. Use Scheduled Tasks for recurring or conditional checks against web and connected-app state.

## Projects

OpenAI documents project memory as a way to keep related chats and resources together. Project-only memory prevents chats from referencing conversations outside the project and must be selected when the project is created.

Source: https://help.openai.com/en/articles/10169521-projects-in-chatgpt

## Codex

OpenAI describes Codex as a coding agent for writing, reviewing, and shipping code. Durable repository rules should therefore live in the repository rather than relying only on chat history.

Source: https://help.openai.com/en/articles/11369540-codex-in-chatgpt-faq

## Deep Research

Deep Research can use the public web, selected websites, uploaded files, and enabled connected apps. It creates a research plan and returns a report with citations.

Source: https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt

## Work

Work is designed for longer multi-step tasks and deliverables, while Codex remains a separate coding-focused experience.

Source: https://help.openai.com/en/articles/20001275

## Scheduled Tasks

Scheduled Tasks can run recurring work and monitor for meaningful changes using the web and connected apps. Plus currently supports up to five active tasks. Scheduled Tasks cannot access files attached to a ChatGPT Project.

Source: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt

## Recommended loop

1. Capture the goal in the ChatGPT Project.
2. Read current GitHub state before planning.
3. Use Deep Research when external evidence materially affects the decision.
4. Save durable research conclusions under `research/`.
5. Use Codex for implementation and validation under `AGENTS.md`.
6. Run tests and inspect the final diff.
7. Publish meaningful changes through a pull request.
8. Use Scheduled Tasks to watch connected GitHub or web state for actionable follow-up.

## Follow-up experiments

- Compare repeated repository tasks with project-only memory versus ordinary chat context.
- Compare Codex outcomes with and without explicit repository-level agent instructions.
- Track scheduled-monitoring signal-to-noise and tighten triggers when notifications are not actionable.
