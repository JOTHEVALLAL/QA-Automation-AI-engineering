# Example: Scoped Codex Prompt for Playwright Parsing

**Illustrative reconstruction, not a verbatim production prompt.**

## Context
A personal JavaScript/Playwright chart-analysis workflow extracts technical indicator values from a dynamic browser UI. A parser sometimes fails to identify the RSI field because legend formats vary.

## Example prompt
```text
Inspect the existing Playwright extraction flow and its unit/regression tests.
Goal: improve detection and numeric parsing of the RSI indicator.
Requirements:
1. Recognize known RSI labels without matching unrelated numbers.
2. Prefer label-associated values over positional guesses.
3. Handle temporarily missing/dynamic UI values with bounded retries.
4. Mark extraction as unavailable if no reliable value is found.
Constraints:
- Do not change TradingView layout, other indicator logic, weekly rules,
  candidate scoring or downstream report formats.
- Do not expose session details or credentials.
Validation:
- Add synthetic parsing cases (valid, missing, malformed, ambiguous).
- Run targeted regression tests and report pass/fail with file changes.
Output:
- Root cause summary; files changed; behavior before/after;
  test command and actual result; remaining limitations.
```

## Why this prompt is stronger
It defines scope, failure behavior, non-goals, regression expectations and measurable output. It also distinguishes a parser fix from a redesign of chart logic.

**Note:** The private personal project has had RSI extraction fixes. This example is a newly drafted teaching artifact.
