# Momentum Edge — Conceptual Architecture

```mermaid
flowchart TD
    A[Excel / CSV / JSON Candidate Inputs] --> B[Input Schema and Freshness Checks]
    M[Authorized Market Data APIs] --> B
    B --> C[Python / Pandas Processing]
    C --> D[Eligibility and Technical Rules]
    D --> E[Ranking / Risk / Verdict]
    E --> F[Streamlit Pages and Filters]
    E --> G[Structured JSON Exports]
    G --> H[Separate Node.js / Playwright Agent AI]
    H --> I[Validation Reports]
    C --> J[Snapshot Store / Fallback Handling]
    J --> F
```

Conceptual presentation of the personal project, not a line-by-line source map. Integrations may be unavailable or stale depending on data source and session.

## Distinct responsibilities
- **Python/Pandas:** ingestion, transformation, indicator-derived features and decisions.
- **Streamlit:** interactive presentation, controls and tables.
- **Market data integration:** authorized access, response checks and freshness.
- **Agent AI:** separate JavaScript/Playwright workflow; not a Streamlit component.
