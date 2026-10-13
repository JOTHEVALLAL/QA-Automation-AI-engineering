# Example: Next.js + FastAPI Migration Prompt

**Fictionalized, newly drafted demonstration based on the public architecture case study.**

```text
ROLE: Full-stack developer supporting a QA-reviewed migration.
CONTEXT: A Streamlit analytics application already contains Python
business rules. The new website uses Next.js/React/TypeScript and FastAPI.
GOAL: Migrate the user interface without rewriting approved calculations.
REQUIREMENTS:
- Reusable navigation shell with six routes.
- GET backend endpoints for health, home, market breadth, momentum,
  IPO, short-term and long-term data.
- JSON response handling with source freshness and partial-data states.
- Meaningful loading, error and retry display.
CONSTRAINTS:
- Keep existing Python source-of-truth calculations.
- Do not fabricate missing market data.
- Never commit brokerage secrets or personal holdings.
- Avoid unrelated business-rule changes.
VALIDATION:
- TypeScript checking, lint, production build.
- Backend regression tests and route/response checks.
- Browser validation for loading/error/filter behavior.
DELIVERABLE:
- Changed files, architecture notes, test results and known limitations.
```

## Review checklist
Confirm that old and new classifications agree for the same immutable input; report snapshot age and missing dependencies instead of suggesting a live feed; record unresolved integration issues.
