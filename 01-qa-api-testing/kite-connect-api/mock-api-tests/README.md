# Kite Connect Mock API Test Suite (Python pytest)

[![Kite Connect Mock API Tests](https://github.com/JOTHEVALLAL/QA-Automation-AI-engineering/actions/workflows/kite-mock-api-tests.yml/badge.svg)](https://github.com/JOTHEVALLAL/QA-Automation-AI-engineering/actions/workflows/kite-mock-api-tests.yml)


**Executable test evidence — entirely offline.** This is a self-contained, dependency-injected Python wrapper and simulated Kite SDK client tests. It never contacts Zerodha, generates usable credentials, or executes trades.

## Run on Windows / Linux

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

For a detailed list of individual cases:

```bash
python -m pytest -v
```

Only `pytest` is required; the Kite SDK is **not** needed, because `unittest.mock.Mock` simulates all provider methods.

## What is tested?
- Successful request-token exchange and correct SDK method arguments
- Missing API key, secret and request token
- Missing, empty, null or non-string access-token response
- Rejected invalid / expired request tokens and simulated checksum error
- Authenticated profile response validation
- Invalid profile responses, expired-token rejection and simulated connection error

## GitHub Actions validation

[Successful CI run #2](https://github.com/JOTHEVALLAL/QA-Automation-AI-engineering/actions/runs/38382331711): both Python 3.11 and 3.12 matrix jobs completed successfully. GitHub recorded two test-result artifacts. This remains mocked offline testing, not live Kite validation.

## Verified local execution

```text
..................                                                       [100%]
18 passed in 0.06s
```

**Execution basis:** This suite was run in an offline local Python environment on October 13, 2026. This is not a hosted GitHub Actions run, nor a live Kite API integration test. See [test report](TEST-RESULTS.md).

## Files
- [kite_auth.py](kite_auth.py) — testable functions with an injected SDK client
- [tests/test_kite_auth.py](tests/test_kite_auth.py) — pytest tests and mocks
- [requirements-dev.txt](requirements-dev.txt) — test dependency
- [TEST-RESULTS.md](TEST-RESULTS.md) — verified test summary

## Security boundaries
All credentials and tokens in this code are static fake strings. No secret file, token screenshot, real trading account or vendor data is present. Never publish working credentials.
