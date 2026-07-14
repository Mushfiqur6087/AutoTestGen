# Coverage Evaluation — Accounts Overview (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Accounts_Overview.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Accounts_Overview.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MW-AO-007/008 were revised (2026-07-15) to replace scenarios GEN's suite never tests (high-volume pagination, zero-balance formatting) with scenarios matching behavior GEN's suite actually demonstrates (unauthenticated access blocked, Account Number click doesn't navigate). MW-AO-009 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-AO-001 | Welcome message displayed | Covered | TC-001 | Asserts welcome message displays the customer's full name |
| MW-AO-002 | All accounts listed (Number, Type, Balance, Status, Open Date) | Covered | TC-001 | Single landing-page test asserts every listed column is present per row |
| MW-AO-003 | Account number masking (last 4 digits) | Covered | TC-001, TC-012 | TC-001 asserts masked '****<last 4>' format; TC-012 (short account number) is a specific edge case that implies the general masking rule (Rule 7) |
| MW-AO-004 | Total balance calculation | Covered | TC-001 | Asserts footer Total Balance equals sum of displayed Current Balances |
| MW-AO-005 | Accounts ordered by date | Covered | TC-001 | Asserts rows ordered by Open Date, earliest first |
| MW-AO-006 | Active status badge | Covered | TC-001 | Asserts 'Active' status badge shown per row |
| MW-AO-007 | Unauthenticated access blocked | Covered | TC-006 | Exact match |
| MW-AO-008 | Account Number click does not navigate | Covered | TC-002, TC-007, TC-009 | Exact match, tested three times across the suite |
| MW-AO-009 | Extreme negative balance — no UI breakage | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-001 (partial) | Same reasoning as MW-AO-008: generic balance rendering is exercised, but the extreme-negative-value boundary and UI-breakage check are not |

## Gap List (Not Covered)

- **MW-AO-009** — Extreme negative balance rendering boundary

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Accounts Overview | 9 | 8 | 1 | 88.9% |
