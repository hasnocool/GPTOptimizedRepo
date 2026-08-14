# Git and Pull Request Governance

- Use feature branches for non-trivial work; avoid direct commits to the protected default branch.
- Keep PRs coherent and reviewable; split unrelated behavior into separate changes.
- PR descriptions should explain what changed, why, user/developer impact, validation, risks, and migration notes when applicable.
- Never bypass required checks by disabling them, weakening assertions, or adding blanket ignores without justification.
- Review the final diff for secrets, generated junk, dead code, unrelated formatting churn, and scope creep.
- Prefer squash or rebase workflows that preserve understandable history according to repository policy.
- Do not force-push shared branches unless the workflow explicitly permits it.
- Branch names and commit messages should describe intent clearly.
- Link relevant issues/ADRs/research when they materially explain the change.
- Stale branches should be removed after merge when no longer needed.
- Merge only after the reviewed head commit and required CI state are known.
