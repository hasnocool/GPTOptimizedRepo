# Repository Hygiene Governance

- Keep the repository root intentional; application code, scripts, docs, fixtures, and generated artifacts belong in defined locations.
- Do not commit caches, bytecode, virtual environments, coverage output, build artifacts, editor swap files, temporary exports, crash dumps, or local databases unless explicitly required as fixtures.
- Avoid abandoned empty directories and unexplained one-off files.
- Remove dead code and obsolete commented-out implementations instead of preserving them indefinitely.
- Keep `.gitignore` aligned with the tools the repository actually uses.
- Large binaries require an explicit reason and appropriate storage strategy such as Git LFS or external artifact storage.
- Avoid duplicate configuration files that configure the same tool or policy unless compatibility requires them.
- Generated files should identify their source/generator and should not be hand-edited.
- Periodically audit stale docs, scripts, fixtures, branches, and test artifacts.
