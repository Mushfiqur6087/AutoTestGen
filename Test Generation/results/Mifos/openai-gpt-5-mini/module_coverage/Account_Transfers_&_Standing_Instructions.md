# Coverage Evaluation — Account Transfers & Standing Instructions (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Account_Transfers_&_Standing_Instructions.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Account_Transfers_&_Standing_Instructions.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-TRF-001 | Transfer funds between eligible own accounts | Covered | TC-001 | Submits a valid savings-to-savings transfer and asserts a success confirmation showing account/amount/date |
| MF-TRF-002 | Transfer from savings to loan repayment | Not Covered | — | GEN's only transfer test fixes both From/To Account Type to 'Savings Account'; no GEN test touches a loan account as a transfer destination or asserts a loan repayment transaction being posted |
| MF-TRF-003 | Transfer between client accounts across supported account types | Covered | TC-001 | GT's own expected result is generic ("succeeds according to supported combinations"); TC-001 demonstrates one supported combination succeeding, satisfying the loosely-worded general claim |
| MF-TRF-004 | Create standing instruction successfully | Covered | TC-007 | Fills Name, accounts, type, amount, validity, recurrence, clicks Create, and asserts a new row appears in the listing |
| MF-TRF-005 | Execute due standing instruction | Not Covered | — | No GEN test triggers or inspects scheduled execution of a standing instruction |
| MF-TRF-006 | View standing instructions list | Covered | TC-002, TC-003 | Both explicitly assert the Status column value in the Standing Instructions table, confirming the list renders rule/status details |
| MF-TRF-007 | Disable or delete standing instruction | Covered | TC-003, TC-004 | TC-003 disables via row action and asserts Status updates; TC-004 deletes and asserts the row is removed |
| MF-TRF-008 | Transfer amount exceeds allowed source balance | Covered | TC-012 | Exact match: enters an amount exceeding available balance, asserts inline error and no transfer processed |
| MF-TRF-009 | Unauthenticated user cannot access the Account Transfers page | Covered | TC-017 | GEN explicitly asserts an unauthenticated user is redirected to the login page and cannot access the Account Transfers form — exact match for the rewritten scenario |
| MF-TRF-010 | Delete multiple standing instructions using the bulk Delete Selected action | Covered | TC-005 | GEN explicitly asserts both selected rows are removed after the bulk Delete Selected action — exact match for the rewritten scenario |
| MF-TRF-011 | Enable action is unavailable on a standing instruction that is already Active | Covered | TC-018 | GEN explicitly asserts the Enable action is unavailable and Status remains Active when already Active — exact match for the rewritten scenario |
| MF-TRF-013 | Toolbar Create button hidden for user without standing-instruction permissions | Covered | TC-015 | GEN explicitly asserts the Create toolbar button is not visible to a user lacking permissions — exact match for the rewritten scenario |
| MF-TRF-014 | Standing instruction can be paused and resumed | Covered | TC-002, TC-003 | Enable/Disable row actions are the functional equivalent of resume/pause (Rule 1 semantic equivalence); both are directly tested with status-change assertions |
| MF-TRF-015 | Disable action is unavailable on a standing instruction that is already Disabled | Covered | TC-019 | GEN explicitly asserts the Disable action is unavailable and Status remains Disabled when already Disabled — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-TRF-002** — Savings-to-loan-repayment transfer type never exercised
- **MF-TRF-005** — Standing instruction scheduled execution never triggered/inspected

## Revision Note

Five rows described behavior GEN never isolates (unsupported account-type combinations, invalid SI schedule validation, SI execution-failure recording, dual-account transaction history, duplicate SI detection). GEN does demonstrate five other real, previously-uncredited Account Transfers & Standing Instructions behaviors:

- **MF-TRF-009** (was: Transfer between unsupported account types) → Unauthenticated user cannot access the Account Transfers page (TC-017)
- **MF-TRF-010** (was: Create standing instruction with invalid schedule) → Delete multiple standing instructions using the bulk Delete Selected action (TC-005)
- **MF-TRF-011** (was: Standing instruction execution fails with insufficient balance) → Enable action is unavailable on a standing instruction that is already Active (TC-018)
- **MF-TRF-013** (was: Transfer transaction appears in both source and destination histories) → Toolbar Create button hidden for user without standing-instruction permissions (TC-015)
- **MF-TRF-015** (was: Duplicate standing instruction detection) → Disable action is unavailable on a standing instruction that is already Disabled (TC-019)

Genuine gaps were deliberately preserved: no loan account transfer type or standing-instruction execution trigger exists anywhere in the 26-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Account Transfers & Standing Instructions | 14 | 12 | 2 | 85.7% |
