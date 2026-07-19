# Coverage Evaluation — Reset App State (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Reset_App_State.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Reset_App_State.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-RESET-001 | Reset clears cart | Covered | TC-001, TC-008 | Exact match, reinforced by the rapid double-invoke test |
| SL-RESET-002 | Reset button states revert to "Add to cart" | Covered | TC-001, TC-010 | Exact match, reinforced by the product-detail button reset test |
| SL-RESET-003 | Reset preserves login | Covered | TC-001, TC-007, TC-008, TC-009, TC-010 | Every test in the suite explicitly asserts the user remains signed in (Logout still visible) after Reset App State |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Reset App State | 3 | 3 | 0 | 100.0% |
