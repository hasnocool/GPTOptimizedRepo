# Architecture Governance

## Principles

- Organize code around clear domains and responsibilities, not arbitrary file size alone.
- Define allowed dependency directions and keep higher-level domain logic independent of transport, persistence, vendor SDKs, and UI concerns where practical.
- Prefer explicit interfaces at architectural boundaries.
- Avoid circular dependencies; repair ownership or boundaries instead of hiding cycles with delayed imports.
- New services, packages, frameworks, queues, databases, and abstraction layers require a concrete need and documented tradeoff.
- Keep public surfaces intentionally small. Treat exported APIs, CLI flags, schemas, events, and configuration keys as compatibility contracts.
- Significant architectural decisions should be captured as an ADR under `docs/adr/` when they materially constrain future work.

## Change rules

Before broad architecture changes, agents must identify the current boundaries, proposed dependency direction, migration strategy, backward-compatibility impact, and rollback path. Do not combine unrelated architectural cleanup with feature behavior unless required for correctness.

## Mechanical candidates

Repositories should add project-specific checks for forbidden imports, dependency cycles, package-boundary violations, and unexpectedly large strongly-coupled modules when the architecture is mature enough to define those rules reliably.
