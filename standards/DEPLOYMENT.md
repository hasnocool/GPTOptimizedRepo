# Deployment Governance

- Deployment configuration must be version controlled, reviewable, and environment-agnostic where practical.
- Containers should use pinned base-image versions, run as a non-root user where possible, include health checks when appropriate, and avoid unnecessary packages.
- Never bake credentials or local configuration into images or artifacts.
- Services must define startup, readiness, graceful shutdown, and restart behavior.
- Resource requests/limits should reflect measured operating needs for managed environments.
- Production deployment changes require rollback or forward-recovery planning.
- Prefer immutable artifacts promoted between environments over rebuilding different artifacts per environment.
- Deployment automation should validate configuration, migrations, and required health signals before declaring success.
- Document reverse-proxy, TLS, persistent-volume, backup, and networking expectations when they are part of operation.
