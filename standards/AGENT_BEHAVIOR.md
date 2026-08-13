# Coding Agent Governance

- Inspect repository state, governing docs, open work, and affected code before editing.
- State assumptions and acceptance criteria for broad or risky tasks.
- Do not silently broaden scope or rewrite unrelated files.
- Preserve unexplained user changes and avoid destructive Git operations unless explicitly required.
- Never disable tests, checks, lint rules, or security controls merely to make a change pass.
- Run the most relevant validation available and report what was and was not executed.
- Prefer small coherent changes over speculative frameworks or large refactors.
- Keep README, TODO, CHANGELOG, architecture docs, and configuration documentation aligned with behavior.
- Record uncertainty explicitly; do not invent repository behavior or external facts.
- Inspect the final diff for regressions, generated artifacts, secrets, dead code, and accidental scope expansion.
- Use the repository's native branch/PR workflow for non-trivial changes.
- When multiple agents/harnesses are supported, `AGENTS.md` remains canonical and tool-specific files contain only compatibility deltas.
