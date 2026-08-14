# Dependency Governance

- Prefer the standard library and existing dependencies before introducing a new package.
- Every new dependency should have a clear purpose, active maintenance, compatible license, supported runtime versions, and acceptable transitive cost.
- Keep runtime, development, test, and optional dependencies separated.
- Use the repository's lockfile/package manager and keep lockfiles synchronized with manifests.
- Remove unused dependencies promptly.
- Avoid multiple libraries that solve the same problem without a documented reason.
- Do not import optional dependencies at module import time when that makes unrelated functionality unusable.
- Security and maintenance updates should be reviewed regularly; automated update tools may propose changes but must not bypass tests.
- For critical dependencies, document replacement risk or vendor lock-in when meaningful.

## Supply-chain checks

Use vulnerability scanning, license checks, lockfile consistency checks, and dependency review in CI when the ecosystem supports them. Do not automatically merge major-version dependency upgrades without compatibility validation.
