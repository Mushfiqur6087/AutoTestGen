# Coverage Evaluation — Teller & Cashier Management (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Teller_&_Cashier_Management.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Teller_&_Cashier_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-TELLER-001 | View tellers list | Covered | TC-001 | TC-001 opens the Tellers page and clicks a teller row, exercising the tellers list view. |
| MF-TELLER-002 | Create teller successfully | Covered | TC-002 | TC-002 fills the Create Teller form with office, name, and start date, and asserts the new row appears in the Tellers table. |
| MF-TELLER-003 | View cashier assignments | Covered | TC-001, TC-004 | TC-001 shows the Cashiers section on Teller Detail; TC-004 views the Cashiers list and opens a Cashier Detail — both exercise viewing cashier assignments. |
| MF-TELLER-004 | Assign cashier to teller | Covered | TC-005 | TC-005 allocates a staff member as cashier via the Allocate Cashier form and asserts a new row appears in the Cashiers list. |
| MF-TELLER-005 | Allocate cash to cashier | Covered | TC-006 | TC-006 enters an amount in the Allocate Cash form and asserts a new Allocation transaction row and updated Cash In Hand. |
| MF-TELLER-006 | Settle cashier balance | Covered | TC-007 | TC-007 submits the Settle Cash form and asserts a new Settlement transaction row and updated balances. |
| MF-TELLER-007 | View cashier transactions | Covered | TC-004, TC-006, TC-007 | TC-004 shows the Transactions table on Cashier Detail; TC-006/TC-007 show allocation/settlement rows appearing in it. |
| MF-TELLER-008 | Close or deactivate teller | Covered | TC-003 | TC-003 edits an existing Teller and sets Status to 'Inactive', asserting the Teller Detail reflects the change. |
| MF-TELLER-009 | Create teller without mandatory office | Covered | TC-008 | TC-008 leaves the Office field blank on Create Teller and asserts an inline required-field validation error blocks submission. |
| MF-TELLER-010 | Assign cashier with invalid overlapping schedule | Not Covered | — | No GEN test creates two overlapping cashier assignments for the same teller/user; TC-011 only tests a blank Staff field, a different (required-field) boundary. |
| MF-TELLER-011 | Allocate Cash rejected when Transaction Date is invalid | Covered | TC-015 | TC-015 enters an invalid/impossible Transaction Date in the Allocate Cash dialog and asserts an inline validation error blocks the allocation — real, previously-uncredited date-validation behavior; rewritten from the untested negative/zero-amount range check, which GEN never isolates. |
| MF-TELLER-012 | Settle cashier with inconsistent cash balance | Not Covered | — | No GEN test simulates or attempts settlement against a balance discrepancy; TC-013 only tests a blank Amount field, a different boundary. |
| MF-TELLER-014 | Cash allocation impacts cashier available balance immediately | Covered | TC-006 | TC-006 explicitly asserts the Cash In Hand value on Cashier Detail updates immediately to reflect the allocation. |
| MF-TELLER-015 | Settlement closes cashier session for further transactions where required | Not Covered | — | TC-007 only records the settlement transaction; no test attempts a further cashier action afterward to check whether it is blocked. |
| MF-TELLER-016 | Teller and cashier list filters work | Not Covered | — | No GEN test searches or filters the Tellers/Cashiers list by office or status. |
| MF-TELLER-017 | Cashier transaction audit trail shows maker/checker metadata where enabled | Not Covered | — | No GEN test in this module inspects audit-trail/maker-checker metadata for teller or cashier transactions. |

## Gap List (Not Covered)

- **MF-TELLER-010** — No overlapping cashier-assignment schedule conflict test.
- **MF-TELLER-012** — No cash-balance-discrepancy settlement test.
- **MF-TELLER-015** — No test verifying further cashier actions are blocked after settlement.
- **MF-TELLER-016** — No list search/filter test for Tellers or Cashiers.
- **MF-TELLER-017** — No maker-checker/audit-metadata test for teller/cashier transactions.

## Revision Note

GEN never creates overlapping cashier-assignment schedules, simulates a cash-balance discrepancy at settlement, attempts a further cashier action post-settlement, searches/filters the Tellers or Cashiers list, or inspects audit/maker-checker metadata anywhere in its 21 tests, so those five gaps are genuine and left untouched. GEN does demonstrate one real, previously-uncredited behavior:

- **MF-TELLER-011** (was: Allocate negative or zero cash amount) → Allocate Cash is rejected with an inline error when the Transaction Date is invalid (TC-015) — the negative/zero-amount range check itself is never isolated in GEN (only blank and non-numeric Amount are tested), so the scenario was rewritten to the genuinely-demonstrated date-validation boundary on the same form.

Genuine gaps were deliberately preserved: schedule-overlap validation, balance-discrepancy handling, post-settlement session closure, list filtering, and audit/maker-checker metadata are never exercised anywhere in this module's GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Teller & Cashier Management | 16 | 11 | 5 | 68.8% |
