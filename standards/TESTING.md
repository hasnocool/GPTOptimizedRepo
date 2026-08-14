# Python Testing Standard

- Every bug fix should add a regression test when practical.
- Every meaningful new behavior should have automated tests.
- Test observable behavior and contracts rather than private implementation details.
- Keep tests deterministic and independent of execution order.
- Do not depend on live external services in the normal unit-test suite.
- Mock or fake external boundaries rather than every internal function.
- Avoid arbitrary sleeps in tests; synchronize on explicit events, conditions, clocks, or test doubles.
- Keep fixtures focused, composable, and easy to understand.
- Prefer parametrized tests for meaningful input matrices over copy/pasted test bodies.
- Test expected failure modes as well as successful paths.
- For async code, test cancellation, timeout, retry, queue saturation, and shutdown behavior where relevant.
- A failing test must not be 'fixed' by deleting or weakening the assertion unless the expected behavior genuinely changed.
- Keep slow/integration tests clearly marked so fast local checks remain useful.
- Add benchmarks when performance is an explicit requirement with regression risk.

Recommended baseline for new projects:

```bash
pytest
ruff format --check .
ruff check .
python scripts/check_python_governance.py --strict-project
```
