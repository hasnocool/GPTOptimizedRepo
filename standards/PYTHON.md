# Python Engineering Standard

This standard is mandatory when a supported agent creates or modifies Python code.

## Baseline

- Target Python 3.12+ unless the repository explicitly declares another supported version.
- Use `pyproject.toml` as the primary Python project/tool configuration file.
- Prefer a `src/` layout for installable applications and libraries.
- Keep application code out of the repository root.
- Organize modules by domain/responsibility; avoid catch-all `utils.py`, `helpers.py`, and `common.py` modules.
- Keep `__init__.py` lightweight and free of expensive I/O or surprising side effects.
- Avoid circular imports by correcting module boundaries rather than hiding them.

## Design

- Give functions one clear responsibility and keep side effects near system boundaries.
- Prefer small composable functions over long branch-heavy functions.
- Prefer plain functions when persistent state or polymorphism is unnecessary.
- Prefer `dataclasses`, enums, protocols, and domain-specific models over dictionaries whose schema exists only by convention.
- Favor composition over deep inheritance.
- Do not introduce abstraction layers until there is a concrete repeated concept to abstract.
- Delete dead code instead of commenting it out.

## Typing

- Type public functions, methods, constructors, dataclasses, and important internal interfaces.
- Prefer modern syntax such as `list[str]`, `dict[str, int]`, and `str | None`.
- Avoid `Any` unless interoperability genuinely requires it.
- Use `Protocol` for structural interfaces when that reduces coupling.
- Do not use casts merely to silence a type checker when the underlying model can be corrected.

## Imports and naming

- Keep imports at module scope unless delayed import is deliberate and documented.
- Never use wildcard imports.
- Prefer absolute package imports and let Ruff order import groups.
- Do not manipulate `sys.path` as a normal import strategy.
- Use precise domain names; avoid vague names such as `data`, `item`, `obj`, `temp`, or `manager` when a clearer name exists.
- Boolean names should normally read as predicates such as `is_ready`, `has_access`, or `should_retry`.

## Dependencies

- Keep runtime and development dependencies separate.
- Prefer the standard library or an existing dependency when adequate.
- Remove dependencies that are no longer used.
- Before adding a dependency, consider maintenance, license, security history, transitive cost, package size, Python support, and whether it materially simplifies the design.
- Use the repository's chosen lockfile/package manager and do not hand-edit generated lockfiles.

## Errors and resources

- Never use bare `except:`.
- Catch the narrowest exception that can actually be handled.
- Never silently swallow errors.
- Preserve exception context with `raise ... from ...` when translating failures.
- Use context managers for files, sockets, locks, transactions, and other lifecycle-bound resources.
- Prefer `pathlib.Path` over manual path-string manipulation.

## Configuration and logging

- Keep runtime configuration outside source code.
- Parse and validate configuration in one defined layer rather than scattering environment reads through business logic.
- Use `logging` or the project's structured logging layer rather than `print()` for application diagnostics.
- Never log credentials, tokens, authorization headers, private keys, full environment dictionaries, or other secrets.

## Tooling

Unless the repository already has an established equivalent toolchain, use Ruff for formatting/linting and a configured static type checker.

Before merging Python changes, run the applicable checks:

```bash
ruff format --check .
ruff check .
python scripts/check_python_governance.py --strict-project
```

Run the repository's type checker and test suite as well.

## Definition of done

Python work is incomplete until tests, formatting, linting, typing, async-safety checks, documentation, dependency hygiene, generated-file hygiene, and final diff review agree with the intended behavior.
