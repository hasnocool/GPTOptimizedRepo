# Release and Version Governance

- Follow semantic versioning for public releases unless a project explicitly documents another scheme.
- Keep package/runtime version sources synchronized; prefer one canonical source where tooling allows.
- Every release must have corresponding CHANGELOG/release-note entries.
- Breaking changes require explicit migration guidance and a major-version change once the project is stable.
- Tags must follow the repository's documented release format and point to reviewed commits.
- Do not publish artifacts from an unclean or unvalidated tree.
- Release automation must fail if required tests, linting, typing, governance, migrations, or artifact-build checks fail.
- Generated release artifacts should be reproducible where practical and traceable to source commit/version.
- Security-sensitive releases should document any required key rotation, configuration changes, or migration steps without exposing secrets.
- Deprecations must identify replacement behavior and intended removal version/window.
