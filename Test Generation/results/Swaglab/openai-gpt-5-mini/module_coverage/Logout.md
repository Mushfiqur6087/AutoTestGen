# Coverage Evaluation — Logout (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Logout.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Logout.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-LOGOUT-001 | Successful logout | Covered | TC-001, TC-005 | Exact match, reinforced by the rapid-double-click test |
| SL-LOGOUT-002 | Session cleared (direct access redirects to login) | Covered | TC-007 | Exact match: direct URL navigation to a protected page after logout is blocked and redirected to sign-in |
| SL-LOGOUT-003 | Cart cleared on logout | Not Covered | — | No GEN test checks cart state across a logout-then-re-login cycle — feature area entirely untouched |
| SL-LOGOUT-004 | Back button after logout | Covered | TC-006 | Exact match |

## Gap List (Not Covered)

- **SL-LOGOUT-003** — Cart contents reset/persistence across a logout and subsequent re-login

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Logout | 4 | 3 | 1 | 75.0% |
