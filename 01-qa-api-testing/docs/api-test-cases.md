# API Functional Test Cases — Synthetic

**Environment:** Fictional DemoBenefits mock specification. **Execution status for every case: Not Run.**

| Test ID | Scenario | Input / precondition | Expected result | Status |
|---|---|---|---|---|
| API-001 | Get benefits with authorized token | Valid demo member context | 200; JSON items array; expected content type | Not Run |
| API-002 | No authorization header | GET /benefits | 401; error body; no sensitive data | Not Run |
| API-003 | Expired access token | GET /benefits | 401; no protected records | Not Run |
| API-004 | Insufficient permission | Valid token lacking benefit-read permission | 403; no benefits exposed | Not Run |
| API-005 | Benefit belongs to different user | GET /benefits/BEN-OTHER | Access denied or non-disclosing 404 per contract | Not Run |
| API-006 | Unknown benefit identifier | GET /benefits/UNKNOWN | 404; safe error response | Not Run |
| API-007 | Empty benefit collection | Authorized account with no items | 200; empty items; count 0 | Not Run |
| API-008 | Invalid content type | POST login with unsupported content type | Contract-defined 415 or 400; no crash | Not Run |
| API-009 | Malformed JSON | POST login with invalid JSON | 400; structured error response | Not Run |
| API-010 | Schema verification | Valid GET /benefits | Expected keys/types; no password/token fields | Not Run |
| API-011 | Unexpected HTTP method | DELETE /benefits | 405 if not supported | Not Run |
| API-012 | Server-error behavior | Simulated downstream outage | Appropriate 5xx; no stack trace or secret disclosure | Not Run |

## Validation checklist
For each case: record request method/path, safe headers, test data, status, response body, required schema, elapsed time (if tested), actual result and defect reference. Never record real passwords, OTPs, session cookies or bearer tokens in screenshots and reports.
