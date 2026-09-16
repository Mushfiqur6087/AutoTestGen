# Coverage Evaluation — Logout (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Logout.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Logout.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| LOGOUT-001 | Logout from user dropdown | Covered | TC-001 | Exact match (fixture-agnostic: "Account/Login area" vs "user dropdown") |
| LOGOUT-002 | Access protected page after logout | Covered | TC-002, TC-004 | Exact match |

## Gap List (Not Covered)

None — both GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Logout | 2 | 2 | 0 | 100.0% |
