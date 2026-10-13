# AI-Assisted QA Test Design — Example

This is a **new fictional example**, not a workplace Copilot conversation, confidential user story or proof of a specific generated artifact.

## Sample user story
> As a member of DemoBenefits, I want to complete a one-time code challenge after sign-in so that my account has an additional security check.

## Example structured prompt
```text
Act as a QA analyst. Use ONLY this fictional user story and the acceptance criteria below.
Draft positive, negative, boundary and session-related scenarios for web and mobile.
For each test, give ID, precondition, steps and expected result.
Map scenarios to requirement IDs in an RTM.
Do not assume unprovided token durations, lockout thresholds or vendor settings.
Flag missing requirements as questions rather than inventing details.
Acceptance criteria:
- A configured user must complete MFA before protected benefits are displayed.
- Incorrect codes are rejected.
- Expired codes are rejected.
```

## Human review checklist
1. Verify that proposed tests are grounded in acceptance criteria.
2. Add negative, boundary, authentication and authorization checks.
3. Resolve open questions with BA/PO (e.g., expiry duration and retry limits).
4. Assign stable test IDs and prepare test data.
5. Link tests to requirements in RTM.
6. Execute tests in an authorized environment and record actual results.

**Interview framing:** AI can accelerate drafts; QA ownership remains with the human reviewer who validates accuracy, coverage and executed results.
