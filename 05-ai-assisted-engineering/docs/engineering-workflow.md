# AI-Assisted Engineering Workflow

```mermaid
flowchart TD
 A[Requirement or Defect] --> B[Clarify Scope and Acceptance Criteria]
 B --> C[Prepare Structured Prompt]
 C --> D[AI Draft / Proposed Code Change]
 D --> E[Human Code and Requirement Review]
 E --> F[Run Unit / Integration / Regression Checks]
 F --> G{Meets Criteria?}
 G -->|No| H[Diagnose and Refine Prompt]
 H --> D
 G -->|Yes| I[Document Evidence and Limitations]
 I --> J[Commit / Review / Release per Controls]
```

## How tools fit
- **ChatGPT:** planning, explanation, design alternatives, QA questions and prompt drafting.
- **Copilot:** assisted drafting of use cases, scenarios, cases and RTM entries using approved stories.
- **Codex:** codebase inspection, scoped implementation, debugging and permitted test execution.
- **GitHub Actions:** independently executes configured automated checks after code is pushed.

## Example from personal work
For browser extraction issues, isolate the failing stock/indicator, provide a reproducible symptom, request limited parser changes, then run targeted and regression tests. Preserve existing scoring and templates unless explicitly approved.

Historical project examples are summarized here; this public module does not publish original private transcripts.
