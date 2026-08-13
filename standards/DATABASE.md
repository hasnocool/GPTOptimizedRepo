# Database Governance

- Schema changes must use the repository's migration mechanism; do not mutate production schema ad hoc at application startup.
- Keep transaction boundaries explicit and as small as correctness allows.
- Use parameterized queries; never interpolate untrusted values into SQL.
- Document migration rollback/forward-fix strategy for risky changes.
- New query patterns should be reviewed for indexes, N+1 behavior, cardinality, and expected data volume.
- Avoid holding transactions open across slow network calls or user interaction.
- Database access used from async code must use a non-blocking driver or be safely offloaded.
- Backups and restores must remain compatible with schema evolution.
- Destructive migrations require explicit review, data-retention consideration, and a recovery plan.
- Tests should exercise migrations from supported prior states when the project has persistent installations.
