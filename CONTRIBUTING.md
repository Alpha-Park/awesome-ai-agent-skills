# Contributing to Awesome AI Agent Skills

Thank you for your interest in contributing to the **Awesome AI Agent Skills & Native MCP Servers** directory!

## Quality Standards

To maintain standard-setting quality, all contributed skills must meet the following criteria:

1. **Zero External Dependencies**: Must run entirely on Python 3.9+ standard library (`math`, `re`, `json`, `sys`, `time`, `hashlib`, etc.). No external `pip` packages are permitted.
2. **Native Model Context Protocol (MCP)**: Must include a standalone `mcp_server.py` compliant with the standard JSON-RPC 2.0 stdio protocol.
3. **Deterministic Implementation**: Must provide a clean `client.py` with real mathematical, spatial, or algorithmic logic. Mocked placeholders or static stubs are not accepted.
4. **Verification Test Suite**: Must include an `example_usage.py` testing core methods with assertions.
5. **Declarative Metadata**: Must include a valid `skill.json` schema.

## Submission Process

1. Fork this repository.
2. Add your skill entry to the appropriate domain category in `README.md`.
3. Open a Pull Request with a link to your repository and test execution log.
