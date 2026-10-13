# AI-Assisted Engineering & Prompt Engineering

> **Personal portfolio case study.** This module describes AI-assisted QA and software engineering practices, with **fictional, newly written prompt examples**. It contains no employer prompts, private conversations, credentials or client documents.

## Purpose
Show how ChatGPT, Microsoft 365 Copilot and OpenAI Codex support requirements understanding, QA documentation, application development, troubleshooting and test validation—while maintaining human responsibility for accuracy.

## Tools and scope

| Tool | Practical use | Important distinction |
| --- | --- | --- |
| ChatGPT | Explore requirements, clarify technical concepts, draft structured instructions and review explanations | Suggested outputs must be checked |
| Microsoft 365 Copilot | Assist with deriving use cases, test scenarios, test cases and RTM drafts from authorized user stories | Human QA review validates coverage and expected results |
| OpenAI Codex | Inspect code, implement bounded changes, debug, run permitted checks and summarize results | Passing checks and human review determine acceptance |

These tools were used in AI-assisted personal development and QA workflows. **Using AI to write Playwright scripts does not mean the Playwright runtime is an LLM agent.**

## Structured prompting approach
1. **Context:** application, users, affected module and existing behavior.
2. **Objective:** precisely describe the defect or required change.
3. **Input:** approved requirements or reproducible sample data.
4. **Constraints:** preserve existing functionality, no unrelated edits, no secrets.
5. **Acceptance criteria:** observable and testable expected behavior.
6. **Validation:** tests, build/lint, regression checks and edge cases.
7. **Output:** changes, files, evidence, risks and limitations.

[Prompt design guide](docs/prompt-design-guide.md) · [AI workflow](docs/engineering-workflow.md) · [QA guardrails](docs/review-checklist.md)

## Example portfolio demonstrations

| Example | Link |
| --- | --- |
| Synthetic web/mobile MFA user story -> QA artifacts | [Copilot-style test design](examples/copilot-qa-example.md) |
| Playwright indicator extraction bug -> scoped engineering prompt | [Codex-style debugging prompt](examples/codex-debugging-example.md) |
| Next.js/FastAPI migration -> architecture-preserving prompt | [Migration prompt](examples/fullstack-migration-prompt.md) |

## Related project evidence
- [Mocked Kite authentication pytest suite and GitHub Actions](../01-qa-api-testing/kite-connect-api/mock-api-tests/)
- [Playwright automation and report previews](../02-playwright-automation/)
- [Momentum Edge Python/Streamlit](../03-momentum-edge/)
- [Next.js and FastAPI migration](../04-fullstack-website/)

## What this module does NOT claim
- No training or fine-tuning of proprietary AI models.
- No assertion that Copilot automatically assures complete test coverage.
- No claim that sample prompts are verbatim prompts used at work.
- No claim that AI-generated code is production-ready without validation.

## Interview explanation
“I use ChatGPT, Microsoft 365 Copilot and OpenAI Codex to accelerate requirements analysis, test design, coding and debugging. I provide structured context, constraints and acceptance criteria, then review the output and validate changes through testing. My core background remains manual/functional QA, with additional personal experience in automation and AI-assisted engineering.”
