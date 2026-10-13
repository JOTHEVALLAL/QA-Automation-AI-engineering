# Authentication and Token Lifecycle — Conceptual

```mermaid
flowchart TD
  A[Open official Kite login] --> B[User completes sign-in]
  B --> C[Redirect returns short-lived request_token]
  C --> D[Python KiteConnect SDK]
  D --> E[generate_session using API secret]
  E --> F[Access token returned]
  F --> G[Set access token on client]
  G --> H[Authenticated profile / market-data request]
  H --> I{Request accepted?}
  I -->|Yes| J[Process permitted JSON response]
  I -->|No| K[Handle auth failure and reauthenticate as appropriate]
```

### Key distinction
- **Generate token:** exchange `request_token` for `access_token`.
- **Validate token:** call a permitted protected endpoint (for example, profile), then inspect success/error response. This is not the same as merely verifying that a token string is nonempty.
- **Expire/revoke:** avoid assuming a token is valid just because it was previously generated.

The input screenshots demonstrate the first operation. Protected-endpoint validation is a **proposed test step**.
