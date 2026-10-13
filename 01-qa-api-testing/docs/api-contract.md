# Fictional DemoBenefits API Contract

**Base URL:** `https://api.demobenefits.example/v1` (reserved example domain; **does not host a real API**).

| Method | Endpoint | Intent | Expected statuses |
|---|---|---|---|
| POST | `/auth/login` | Submit sample credentials and initiate authentication | 200 or 202, 400, 401 |
| POST | `/auth/mfa/verify` | Verify a simulated one-time code | 200, 400, 401, 429 |
| POST | `/auth/logout` | End an active session | 204, 401 |
| GET | `/benefits` | Read the signed-in member's permitted benefits | 200, 401, 403 |
| GET | `/benefits/{id}` | Read an authorized benefit by identifier | 200, 401, 403, 404 |
| POST | `/auth/password-reset/request` | Request a password reset in a demo flow | 202, 400 |

## Example request
```http
GET /v1/benefits HTTP/1.1
Host: api.demobenefits.example
Authorization: Bearer DEMO_TOKEN_NOT_VALID
Accept: application/json
```

## Example successful response
```json
{"items":[{"id":"BEN-1001","type":"health","status":"active"}],"count":1}
```

## Example error shape
```json
{"error":{"code":"UNAUTHENTICATED","message":"Authentication required"}}
```

**HTTP notes:** 401 means authentication is missing or invalid; 403 means the authenticated caller is not permitted. A real API may return different responses to avoid resource enumeration. 202 on login represents a simulated MFA challenge in this example, not a universal API standard. No credentials or tokens here are usable.
