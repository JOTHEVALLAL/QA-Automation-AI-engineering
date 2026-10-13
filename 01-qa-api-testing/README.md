# API Testing & Authentication Validation — QA Portfolio

> **Synthetic demonstration only.** This module uses a fictional insurance-benefits service named **DemoBenefits**. It is not AON, Okta, or any employer/client implementation. No actual user data, client specifications, tokens or recordings are included.

## Objective
Demonstrate practical QA test design for REST APIs and web/mobile authentication flows: positive/negative testing, request and response validation, SSO/MFA concepts, role-based access checks, defect reporting and requirements traceability.

## Scope
- **API testing:** HTTP methods, status codes, schema/field validation, bad input, unauthorized and forbidden access, and error response structure.
- **Authentication and authorization:** sign-in, MFA verification, expiration, logout, role-based access and password reset.
- **Test artifacts:** sample API contract, JSON examples, manual test cases, RTM, bug report, and Copilot-assisted drafting example.
- **Security:** Conceptual OWASP API risks such as broken object-level authorization; no intrusive tests against real systems.

## Architecture
See [conceptual architecture](docs/architecture.md).

## Artifacts
| Artifact | Link |
| --- | --- |
| Fictional API contract | [API specification](docs/api-contract.md) |
| Sample requests/responses | [JSON example](samples/api-examples.synthetic.json) |
| API test cases | [API test matrix](docs/api-test-cases.md) |
| Authentication/MFA test cases | [Authentication test matrix](docs/auth-test-cases.md) |
| Requirements traceability | [RTM](docs/requirement-traceability.md) |
| Example defect report | [Defect report](docs/sample-defect-report.md) |
| AI-assisted test design | [Prompt example](docs/copilot-test-design-example.md) |

## Interview demonstration
1. Explain how an API client sends a request and validates status, headers, body and schema.
2. Walk through one valid API response and one unauthorized response.
3. Compare **401 Unauthenticated** versus **403 Forbidden**.
4. Describe how an MFA challenge may be issued and verified without exposing OTPs or secrets.
5. Show how a requirement maps to test cases in an RTM.
6. Explain AI-assisted test design: prompt -> draft -> human review -> traceability -> test execution.

## Important limitations
The sample contracts, statuses and workflows are intentionally invented for teaching. They are **not evidence that automated API or penetration tests were executed**. Real SSO, MFA and OAuth/OIDC details vary by identity provider and application. Only test systems you own or have authorization to test.
