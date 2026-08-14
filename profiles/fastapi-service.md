# Profile: FastAPI Service

Apply the Python Service profile plus API governance.

Additional requirements:
- validate request/response models explicitly;
- keep route handlers thin and move domain logic behind clear interfaces;
- use async-capable clients/drivers in async paths;
- set outbound HTTP/database timeouts and bounded pools;
- document authentication/authorization boundaries;
- keep generated OpenAPI behavior synchronized with implementation;
- add integration tests for representative success and failure responses.
