# Momentum Edge — Example QA Validation Checklist

These are documentation examples, **not a claim of executed tests**.

| ID | Validation | Expected result |
| --- | --- | --- |
| ME-001 | Required Excel column absent | Controlled validation message; no fabricated values |
| ME-002 | Candidate records have missing price/volume | Incomplete fields flagged |
| ME-003 | Liquidity eligibility not met | Candidate excluded or marked per approved rule |
| ME-004 | Multiple candidate ranks | Sorting stable and deterministic for tied values |
| ME-005 | Workbook timestamp stale | Stale state visible to user |
| ME-006 | Market API unavailable | Graceful partial/unavailable state |
| ME-007 | Session closes | Clearly labeled latest post-market snapshot if fallback applies |
| ME-008 | Filtering by symbol | Visible table and counts update together |
| ME-009 | JSON export | Correct candidate IDs, field names and source metadata |
| ME-010 | Change in analytics UI | Existing business classifications do not unexpectedly change |

## Example test-design technique
Use boundary values immediately above, at and below each configured threshold. Compare input, transformed values and displayed output; verify negative cases and error status.
