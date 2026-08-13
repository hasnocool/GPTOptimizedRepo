# Scheduled Tasks

## Repository health monitor

The companion ChatGPT Scheduled Task should check the connected GitHub repository and relevant official OpenAI documentation for meaningful changes that require action.

Recommended trigger conditions:

- an open pull request has failing checks;
- an open pull request has gone stale and appears blocked;
- repository documentation is obviously drifting from current workflow state;
- an official OpenAI change materially affects Projects, Codex, Deep Research, Work, or Scheduled Tasks;
- a meaningful follow-up from `TODO.md` becomes actionable.

The task should stay quiet when there is nothing actionable.

## Design constraint

Scheduled Tasks cannot access files attached to a ChatGPT Project, so recurring monitoring should inspect connected GitHub/web state rather than depend on project uploads.

## Noise policy

Prefer one concise notification containing:

1. what changed;
2. why it matters;
3. the repository item or official source involved;
4. the recommended next action.
