# Momentum Edge Module Catalog

| Page | Main responsibility | Representative validations |
| --- | --- | --- |
| Home | KPI summary and candidates | Totals, completeness, timestamp |
| Market Breadth | Market health participation | Source coverage, stale/partial warnings |
| Momentum Edge | Equity swing screening | Eligibility filters, rank, verdict consistency |
| IPO Console | Recently listed stocks | Listing-date age filters and classification |
| Short-Term Radar | PDH/ORB/VWAP contextual setups | Price levels, missing-session data, next-session status |
| Long-Term Radar | Weekly context and longer-term review | Weekly data completeness and Final Review criteria |

### Selected strategy terminology
ADR (Average Daily Range), liquidity, EMA, MACD, RSI, breakout freshness, stop-loss distance, trade priority and volume quality. These are **domain rules and data fields**; they are not software frameworks.

### Integration contract in plain language
The application exports selected candidates as structured JSON. The separate Playwright agent consumes those candidates and provides additional chart-derived validation/reporting. The feed's original classifications and downstream agent verdicts remain distinguishable.
