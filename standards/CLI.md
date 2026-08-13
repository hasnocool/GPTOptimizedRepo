# CLI Governance

- Every public command should provide useful `--help` output and stable exit-code semantics.
- Separate normal machine-consumable output from diagnostics by using stdout and stderr consistently.
- Destructive operations require explicit confirmation or an unambiguous noninteractive override.
- Support noninteractive automation for commands intended for scripts or CI.
- Document precedence between CLI flags, environment variables, and config files.
- Preserve backward compatibility for widely used flags and output formats or provide a migration path.
- Prefer structured output modes such as JSON for automation where useful.
- Avoid hidden network access or side effects in commands that appear read-only.
- Long operations should expose useful progress without corrupting structured output.
