# Coverage Evaluation — Accounting - Chart of Accounts (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Accounting_-_Chart_of_Accounts.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Accounting_—_Chart_of_Accounts.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-COA-001 | View chart of accounts | Covered | TC-001, TC-002 | TC-001/TC-002 navigate to Chart of Accounts and assert accounts appear under their Account Type in the hierarchy, confirming the grouped tree/list view (Rule 7: specific create/detail flows imply the general list-view behavior). |
| MF-COA-002 | Create header account | Not Covered | — | No GEN test selects Account Usage = Header when creating a GL account; TC-002/TC-003 both create Detail accounts (TC-002 explicitly selects "Detail"). Header-account creation is a distinct, untested path. |
| MF-COA-003 | Create non-header account | Covered | TC-002 | TC-002 creates a GL account selecting Account Type, GL Code, Account Name, and "Detail" usage — matches this scenario directly. |
| MF-COA-004 | Edit GL account | Covered | TC-004 | TC-004 opens an existing GL account, edits Account Name and the Manual Entries Allowed toggle, saves, and asserts changes persist. |
| MF-COA-005 | Disable or close GL account | Covered | TC-005 | GT scenario title itself treats "disable" and "close" as interchangeable; TC-005 removes the account via Delete with confirmation, achieving the same "account becomes unavailable for future use" outcome asserted by a success notification and its removal from the tree. |
| MF-COA-006 | View GL account usage details | Covered | TC-001 | TC-001's detail view explicitly shows Account Type, Manual Entries Allowed, Usage (Header/Detail), and Description — matches "classification, usage type, and relationships." |
| MF-COA-007 | Create GL account without name | Covered | TC-010 | TC-010 (all required fields empty) explicitly asserts an inline validation error on Account Name among the fields checked (Rule 4: combined scenario satisfies the individual field claim). |
| MF-COA-008 | Create GL account without account type | Covered | TC-008, TC-010 | TC-008 is a dedicated test leaving Account Type blank and asserting the required-field error; TC-010 reinforces it as part of the all-blank case. |
| MF-COA-009 | Duplicate GL account code | Covered | TC-011 | TC-011 enters an existing GL Code and asserts a duplicate/uniqueness validation error, blocking creation — direct match. |
| MF-COA-010 | Disable GL account that is constrained by business rules | Not Covered | — | GEN's only removal test (TC-005 Delete) exercises the unconstrained success path; no GEN test attempts disable/delete on an account protected by business rules and asserts the operation is blocked. |
| MF-COA-011 | Manual entries allowed only for accounts with correct usage type | Not Covered | — | TC-001/TC-002 surface a "Manual Entries Allowed" flag/indicator on GL accounts, but no GEN test attempts a manual journal entry against a restricted account (or verifies only eligible accounts are usable) within this module's suite — the enforcement behavior itself is untested. |

## Gap List (Not Covered)

- **MF-COA-002** — No test creates a GL account with Account Usage = Header; only Detail-usage creation is exercised.
- **MF-COA-010** — No test attempts to disable/delete a business-rule-constrained (linked/protected) GL account to verify the operation is blocked.
- **MF-COA-011** — No test verifies that manual journal-entry posting is actually restricted to accounts with the correct usage/manual-entries flag.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Accounting - Chart of Accounts | 11 | 8 | 3 | 72.7% |
