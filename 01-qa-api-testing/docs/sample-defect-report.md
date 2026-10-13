# Sample Defect Report — FICTIONAL / NOT OBSERVED

**Defect ID:** DEMO-BUG-001  
**Title:** Protected benefits endpoint returns data after simulated session expiry  
**Severity:** High (illustrative)  
**Environment:** DemoBenefits mock test environment (fictional)  
**Status:** Example only; no real defect reported

## Preconditions
- A demo test user has previously authenticated.
- A test session is configured to expire.

## Steps to reproduce
1. Authenticate as the fictional test user in a mock environment.
2. Allow the mock session/token to expire.
3. Send `GET /v1/benefits` with the expired demo token.
4. Observe the response.

## Expected
HTTP 401 (per demo contract), with no benefits data.

## Illustrative actual behavior
HTTP 200 with a benefits list (**invented for demonstration**).

## Suggested evidence
Sanitized request/response excerpts, reproducible timestamps, build number and environment.

## Retest
After a hypothetical fix, repeat the expired-token scenario and relevant valid-token regression cases.
