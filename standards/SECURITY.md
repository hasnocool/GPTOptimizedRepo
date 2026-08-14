# Python Security Standard

- Never commit or log credentials, tokens, private keys, `.env` secrets, authorization headers, or credential files.
- Never use `eval()` or `exec()` on untrusted data.
- Never deserialize untrusted pickle data.
- Prefer safe structured formats such as JSON for untrusted interchange.
- Use parameterized database queries; never interpolate untrusted values into SQL.
- Prefer subprocess argument arrays and avoid shell execution unless shell behavior is explicitly required and inputs are controlled.
- Validate user-controlled paths and defend against path traversal when reading or writing outside a fixed trusted path.
- Use `secrets` rather than `random` for security-sensitive tokens and identifiers.
- Validate untrusted/external data at system boundaries before converting it into internal domain types.
- Apply explicit network timeouts and response-size limits where untrusted peers could otherwise consume unbounded resources.
- Bound decompression, parsing, queueing, retries, and concurrency for attacker-controlled inputs.
- Do not suppress dependency/security warnings merely to make CI green; document accepted risk explicitly when no immediate remediation is available.
- Keep sensitive values out of exception messages returned to untrusted callers.
