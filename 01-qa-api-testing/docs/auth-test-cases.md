# Authentication, SSO and MFA Test Scenarios — Synthetic

**System:** Fictional web/mobile benefits application. **Not AON or actual Okta configuration. All statuses: Not Run.**

| Test ID | Area | Test scenario | Expected result |
|---|---|---|---|
| AUTH-001 | Login | Valid account credentials | Authenticated flow or MFA challenge as specified |
| AUTH-002 | Login | Incorrect password | Safe failure; no login session |
| AUTH-003 | SSO | Start sign-in from web client | Redirect to configured identity provider and return to allowed callback |
| AUTH-004 | SSO | Unapproved redirect URI | Redirect rejected |
| AUTH-005 | MFA | Correct valid OTP | Challenge accepted once within validity window |
| AUTH-006 | MFA | Incorrect OTP | Challenge rejected without authentication |
| AUTH-007 | MFA | Expired OTP | Challenge rejected |
| AUTH-008 | MFA | Reused OTP | Reuse blocked when one-time semantics apply |
| AUTH-009 | MFA | Repeated invalid attempts | Rate limiting/lockout per policy |
| AUTH-010 | Authorization | Logged-in user accesses another user's resources | No unauthorized data exposed |
| AUTH-011 | Session | Logout, then access protected endpoint | Prior session/token no longer accepted as specified |
| AUTH-012 | Session | Session expiration | Reauthentication required |
| AUTH-013 | Password reset | Valid reset flow | Only authorized reset action succeeds |
| AUTH-014 | Password reset | Expired or reused reset link | Reset rejected |
| AUTH-015 | Mobile | Background/resume with expired session | Secure handling and reauthentication as required |
| AUTH-016 | Error messages | Unknown username vs wrong password | Avoid unnecessary account-enumeration disclosure |

## Terminology for interviews
- **Authentication:** confirming identity.
- **Authorization:** determining permissions.
- **SSO:** single sign-on across configured applications.
- **MFA:** requiring more than one independent authentication factor.
- **OIDC/OAuth 2.0:** commonly used identity / delegated authorization protocols; not interchangeable.
- **JWT:** a possible token format, not a requirement for every SSO solution.

Expected results depend on the approved application's business/security requirements.
