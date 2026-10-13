# FastAPI Route Overview

**Illustrative host:** `http://127.0.0.1:8000` when run locally. Routes below are based on the user's project-stage implementation notes. Detailed schemas vary by module.

| Method | Route | Purpose |
| --- | --- | --- |
| GET | /api/health | Backend responsiveness |
| GET | /api/home | KPI summary and Home page data |
| GET | /api/market-breadth | Breadth assessment |
| GET | /api/momentum | Momentum list |
| GET | /api/ipo | IPO screening |
| GET | /api/short-term | Short-term setup results |
| GET | /api/long-term | Weekly/long-term review |

## Conceptual JSON response (synthetic, not captured)
```json
{
  "source_status": "STALE",
  "as_of": "2026-10-01T00:00:00+05:30",
  "items": [
    {"symbol": "DEMO_ALPHA", "verdict": "WATCH"}
  ],
  "note": "Example only. Schema is illustrative."
}
```

This JSON is **not** a literal copy of the application's response contract. Confirm actual response field names using local FastAPI's OpenAPI documentation or source code before writing runnable contract tests.

## API QA examples
- Successful GET and valid JSON response
- Error handling when approved data source unavailable
- Stale/partial/current flags remain consistent with data timestamps
- Search/filter behavior at frontend matches returned API records
- Regression checks preserve Python classification outputs
