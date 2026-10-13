# Example: AI-Assisted QA Artifacts for an MFA User Story

**Entirely fictional demonstration. Not an AON story or actual workplace Copilot output.**

## User story
“As a demo benefits user, I want a one-time verification challenge after password login so that access to protected benefits is secured.”

## Acceptance criteria
1. Valid credentials initiate MFA if the member is configured for MFA.
2. A valid non-expired code completes login.
3. Wrong or expired codes do not grant access.
4. Protected benefits remain inaccessible until verification succeeds.

## Example prompt for an AI assistant
```text
Act as a QA Test Analyst. Using only the fictional story and acceptance
criteria above, create: use cases, positive and negative test scenarios,
test cases with preconditions/steps/expected results, and an RTM.
Identify missing requirements (expiry time, retries, lockout policy).
Do not invent policies. Separate draft artifacts from executed results.
```

## Illustrative QA draft
| Test ID | Test scenario | Expected |
| --- | --- | --- |
| MFA-001 | Valid credentials, valid MFA code | Access granted |
| MFA-002 | Valid credentials, invalid MFA code | Verification rejected |
| MFA-003 | Expired MFA code | Verification rejected |
| MFA-004 | Attempt benefits access before MFA | Access denied |
| MFA-005 | MFA code reused | Policy-defined rejection where one-time semantics apply |

## Mini RTM
| Requirement | Tests |
| --- | --- |
| AC-1: MFA challenge issued | MFA-001 |
| AC-2: Valid code works | MFA-001 |
| AC-3: Wrong/expired code denied | MFA-002, MFA-003 |
| AC-4: Protected resource inaccessible before MFA | MFA-004 |

## Human review
Confirm OTP expiry, retry/lockout policy, resend behavior, web/mobile differences and actual identity-provider requirements with the team. Status of all tests: **Not executed**.
