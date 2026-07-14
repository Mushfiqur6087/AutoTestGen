# Coverage Evaluation — Open New Account (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Open_New_Account.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Open_New_Account.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-ONA-001 | Open Checking account | Covered | TC-001 | Exact match |
| MW-ONA-002 | Open Savings account | Covered | TC-002 | Exact match |
| MW-ONA-004 | Real-time validation on invalid deposit | Covered | TC-022 | TC-022 shows an inline validation error appearing immediately upon the amount becoming invalid relative to the selected type, without requiring submit — same "immediate feedback" behavior, triggered via account-type switch rather than direct entry (Rule 3: same logical path) |
| MW-ONA-005 | No account type selected | Covered | TC-005 | Exact match |
| MW-ONA-006 | Checking deposit < $25 | Covered | TC-010, TC-016 | TC-010 direct match; TC-016 reinforces with the one-unit-below boundary |
| MW-ONA-007 | Savings deposit < $100 | Covered | TC-011, TC-018 | TC-011 direct match; TC-018 reinforces with the one-unit-below boundary |
| MW-ONA-008 | Non-numeric deposit | Covered | TC-009 | Exact match |
| MW-ONA-009 | Insufficient funding balance | Covered | TC-012, TC-020 | TC-012 direct match; TC-020 reinforces with the exact-shortfall boundary |
| MW-ONA-010 | No funding account selected | Covered | TC-007 | Exact match |
| MW-ONA-011 | Exact minimum Checking ($25) | Covered | TC-015 | Exact boundary match |
| MW-ONA-012 | Exact minimum Savings ($100) | Covered | TC-017 | Exact boundary match |
| MW-ONA-013 | Just below minimum ($24.99) | Covered | TC-016 | Exact match: one unit below Checking minimum blocked |
| MW-ONA-014 | Deposit with excessive precision | Covered | TC-021 | Exact match: high-precision decimal rejected, satisfying the "or rejected" branch of GT's expected result |
| MW-ONA-015 | Duplicate account prevention (submit, back, resubmit) | Not Covered | — | No GEN test exercises the back-then-resubmit flow; the module's edge tests cover account-type switching and decimal precision but nothing touching duplicate/resubmission prevention |

## Gap List (Not Covered)

- **MW-ONA-015** — Duplicate account prevention via browser back + resubmit (feature area entirely untested)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Open New Account | 14 | 13 | 1 | 92.9% |
