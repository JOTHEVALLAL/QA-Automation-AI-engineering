# Structured Prompt Design Guide

## A reusable prompt template
```text
ROLE: Act as a [QA Analyst / Python Developer / Test Automation Engineer].
CONTEXT: [Describe the application, stack and relevant existing behavior].
GOAL: [One specific result].
INPUTS: [Approved user story, sample payload or reproducible defect].
REQUIREMENTS: [Detailed behavior and edge cases].
CONSTRAINTS: [What must remain unchanged; no secrets; scope limits].
ACCEPTANCE CRITERIA: [Observable conditions of success].
VALIDATION: [Tests to execute and evidence to provide].
DELIVERABLE: [Code or test artifacts plus change summary and limitations].
```

## Prompt-engineering concepts
| Keyword | Practical meaning |
| --- | --- |
| Context | Background and architecture supplied to the model |
| Role prompting | Define the requested perspective/task |
| Constraints | Explicit scope and restrictions |
| Few-shot | Provide safe examples of expected input and output |
| Iteration | Refine the instruction after examining output |
| Hallucination | Confident but unsupported information |
| Human-in-the-loop | Human review and approval |
| Acceptance criteria | Testable completion requirements |
| Grounding | Base answers on supplied requirements and actual files |
| Least privilege | Allow only the tools/files needed for the task |

## QA prompting mistakes to avoid
- Do not tell AI to “ensure 100% coverage” without defining coverage and reviewing gaps.
- Do not invent requirement details, HTTP statuses or security policy.
- Do not paste customer records, access tokens, source secrets or non-approved content.
- Do not confuse generated test cases with executed evidence.
- Request a list of assumptions and open questions.
