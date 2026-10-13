# Human Review and Validation Checklist

Every AI-assisted change should be reviewed before acceptance.

- [ ] Input is allowed to be shared with the selected AI tool.
- [ ] Original requirement and acceptance criteria are documented.
- [ ] Model assumptions and unsupported suggestions are identified.
- [ ] The change stays within the requested scope.
- [ ] Secret files, real tokens, PII and employer/client artifacts are absent.
- [ ] New tests include positive, negative and boundary scenarios as applicable.
- [ ] Actual results are recorded separately from expected results.
- [ ] Regression checks are performed for affected functionality.
- [ ] Logs, screenshots and reports are sanitized for publication.
- [ ] Limitations and unavailable data are disclosed.
- [ ] Human reviewer approves the changes.

## Interview framing
AI improves efficiency, but **the QA engineer remains responsible for test correctness, traceability and release-quality evidence**.
