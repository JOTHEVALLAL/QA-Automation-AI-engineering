# Conceptual API and Authentication Architecture

```mermaid
flowchart TD
  U[Web or Mobile Client] --> A[DemoBenefits REST API]
  U --> I[Identity Provider - Conceptual SSO / MFA]
  I --> U
  A --> V[Token Validation and Authorization]
  V --> S[Benefits Service]
  S --> D[Demo Data Store]
  A --> R[JSON Response]
  R --> U
  T[QA API Client / Test Runner] --> A
```

This is a conceptual teaching diagram, **not** a depiction of AON infrastructure.

## Test boundaries
- **Authentication:** Who is the user? Session/token validity and MFA challenge states.
- **Authorization:** What resources may the authenticated user access?
- **API contract:** HTTP method, endpoint, request payload, response payload and status code.
- **Data checks:** Required fields, formats, values and sensitive-field exposure.
- **Negative testing:** Invalid parameters, missing auth, expired token, forbidden resource access, wrong OTP, excessive attempts (in an authorized environment).
