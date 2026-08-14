# Documentation Governance

- `README.md` must describe current user-facing behavior and supported workflows.
- `TODO.md` contains planned work; completed items should be removed or marked complete with context.
- `CHANGELOG.md` records meaningful user/developer-visible changes.
- Significant architecture decisions belong in ADRs when they constrain future work.
- Examples, CLI snippets, API examples, and configuration samples must be kept current and executable when practical.
- Document invariants, reasons, constraints, and operational consequences rather than narrating obvious code.
- Any change that alters behavior, configuration, architecture, deployment, API, or operational workflow must update the corresponding documentation in the same PR.
- Avoid duplicate sources of truth. Link to canonical policy/docs rather than copying them.
- Mark experimental or provisional guidance clearly.
