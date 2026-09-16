# Coverage Evaluation — Tax Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Tax_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Tax_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-TAX-001 | View tax components list | Covered | TC-001, TC-004 | TC-001 clicks a Name link in the Tax Components table and TC-004 clicks a Name link in the Tax Groups table — both presuppose the components/groups lists are displayed |
| MF-TAX-002 | Create tax component successfully | Covered | TC-003 | Direct match: name/percentage/debit-credit accounts/start date entered, Create clicked, new row appears |
| MF-TAX-003 | Create tax group successfully | Covered | TC-006 | Direct match: group created with one tax component row, new row appears in the Tax Groups table |
| MF-TAX-004 | Link tax group to applicable charge/product where supported | Covered | TC-008 | Direct match: Enable Withhold Tax checked on a Savings Product, Tax Group selected, saved, and the product configuration reflects the selected group |
| MF-TAX-005 | View tax configuration details | Covered | TC-001, TC-004 | TC-001 shows component details (Percentage, Debit/Credit accounts, Start Date) and TC-004 shows group details (associated components with Start/End Date) — matches "details display correct rates and applicability" |
| MF-TAX-006 | Create tax component without mandatory fields | Covered | TC-012, TC-013, TC-014 | Direct matches: all-fields-empty, Name-blank, and Percentage-blank submissions each blocked with inline required-field errors |
| MF-TAX-007 | Create tax component with invalid rate | Covered | TC-015 | TC-015 enters a non-numeric Percentage value and asserts a blocked submission with inline validation — matches "invalid rate" generically (Rule 1) |
| MF-TAX-008 | Create tax group without components where at least one is required | Not Covered | — | GEN's only zero-component scenario (TC-020) adds then removes a component row and asserts the group SAVES SUCCESSFULLY with an empty components list — the opposite outcome GT requires; TC-016 tests a different validation (a blank Tax_Component selector within an added row, not a zero-row submission) — reclassified from Partially Covered because no GEN test actually confirms the "at least one component required" business rule GT describes |
| MF-TAX-010 | Tax is applied correctly on configured charge transaction | Not Covered | — | No GEN test triggers a charge transaction or inspects computed/posted tax amounts |
| MF-TAX-011 | Updating tax rate affects future transactions only | Not Covered | — | No GEN test updates a tax rate and compares historical vs. new transactions |
| MF-TAX-012 | Tax breakdown is visible in transaction details where supported | Not Covered | — | No GEN test opens a transaction detail view to inspect a tax component breakdown |

## Gap List (Not Covered)

- **MF-TAX-008** — "At least one component required" validation on Tax Group creation is never confirmed; GEN's related test asserts the opposite (empty group saves successfully)
- **MF-TAX-010** — Tax computed/posted on a charge transaction is never tested
- **MF-TAX-011** — Rate-change effect on future-vs-historical transactions is never tested
- **MF-TAX-012** — Tax breakdown visibility in transaction detail is never tested

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Tax Management | 11 | 7 | 4 | 63.6% |
