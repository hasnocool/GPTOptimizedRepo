# Configuration Governance

- Centralize configuration parsing and validation instead of scattering environment-variable reads throughout business logic.
- Define precedence between defaults, config files, environment variables, CLI flags, and remote configuration.
- Validate configuration at startup and fail early with actionable errors.
- Keep secrets separate from ordinary configuration and never commit secret values.
- Document every supported user-facing setting, its type, default, units, and operational impact.
- Avoid hidden magic defaults for safety-critical or cost-critical behavior.
- Configuration changes that alter behavior materially belong in CHANGELOG/release notes.
- Prefer typed configuration models and immutable runtime configuration once startup completes unless hot reload is explicitly designed.
- Treat configuration keys as compatibility surfaces; rename/remove them through deprecation or migration when users may depend on them.
