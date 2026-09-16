# Coverage Evaluation — Forgot Password (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Forgot_Password.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Forgot_Password.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| FP-001 | Request password reset with existing email | Covered | TC-001 | Exact match |
| FP-002 | Reset password with valid link | Covered | TC-002 | Exact match |
| FP-003 | Unknown email address | Covered | TC-005 | Exact match |
| FP-004 | Empty email field | Covered | TC-003 | Exact match |
| FP-005 | Reset password mismatch | Covered | TC-007 | Exact match |
| FP-006 | Expired reset link | Covered | TC-008, TC-011 | Exact match, plus the one-unit-past-expiry boundary test |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Forgot Password | 6 | 6 | 0 | 100.0% |
