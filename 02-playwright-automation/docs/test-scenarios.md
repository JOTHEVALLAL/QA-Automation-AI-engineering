# Sample QA Test Scenarios — Browser Automation & Reporting

> Portfolio test-design examples using fictional data. These are **not** evidence of executed production test cases.

| ID | Scenario | Expected result |
|---|---|---|
| BA-001 | Valid candidate JSON with required fields | Input is accepted and each candidate is queued once |
| BA-002 | Missing symbol field | Record is rejected or marked with explicit validation error |
| BA-003 | Invalid numeric price | Validation produces a meaningful error rather than silently converting bad data |
| BA-004 | Dynamic chart loads slowly | Readiness check waits within configured limit; timeout is recorded |
| BA-005 | Indicator field is missing | Extraction marked incomplete; score is not falsely reported as validated |
| BA-006 | Temporary extraction failure | Bounded retry is logged; persistent failures remain visible |
| BA-007 | Entry risk exceeds allowed rule | Risk decision is independent of a high agent score |
| BA-008 | Candidate processing ends | HTML report contains count, per-record status and consistent columns |
| BA-009 | Malformed JSON file | Controlled parsing error without partial misleading report |
| BA-010 | Output contains HTML special characters | Values are escaped to avoid markup injection |

## Example validation formula
`riskPercent = ((entry - plannedStopLoss) / entry) * 100`

The demonstration HTML uses fabricated values and decisions. Real project thresholds are not disclosed or inferred from this sample.
