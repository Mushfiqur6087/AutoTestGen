# Coverage Evaluation — Accounting - Closures (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Accounting_-_Closures.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Accounting_—_Journal_Entries_&_Closures.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

Note: this GT module shares its GEN source file with Accounting_-_Journal_Entries.md (combined GEN suite "Accounting — Journal Entries & Closures"). Only the closure-relevant GEN tests are cited here; a tc_id may legitimately also appear as a match in the Journal Entries report where it genuinely supports both.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-CLOSE-001 | View accounting closures list | Covered | TC-004, TC-005 | TC-004 navigates to the Closing Entries page (implying the existing-closures table is displayed); TC-005 shows a created closure appearing as a row with Office, Closing Date, and Created Date — confirms the list displays closures by office/date. |
| MF-CLOSE-002 | Create accounting closure successfully | Covered | TC-005 | TC-005 selects Office and Closing Date, submits, and asserts a new row appears in the Closing Entries table — direct match. |
| MF-CLOSE-003 | View closure details | Covered | TC-005 | TC-005's resulting table row exposes Office, Closing Date, and Created Date metadata; while not a dedicated detail page, the same office/date metadata GT-003 requires is verified visible (Rule 3: fixture/UI-shape agnosticism — minor difference in presentation, not a distinct behavior). |
| MF-CLOSE-004 | Create duplicate closure for same office/date constraints | Not Covered | — | No GEN test attempts to create two closures for the same office/date scope to verify a duplicate is blocked. |
| MF-CLOSE-005 | Create closure without required office/date | Covered | TC-014 | TC-014 leaves Closing Date blank and asserts an inline required-field error blocking the closure; the GT scenario names "office/date" generically and this establishes the required-field validation mechanism on the closure form (Rule 6 equivalence class). |
| MF-CLOSE-006 | Backdated transaction after closure is blocked | Covered | TC-013, TC-017 | TC-013 and TC-017 both create/assume a closure and then attempt a journal entry dated on/before the Closing Date, asserting the post is blocked — direct match for "backdated posting blocked by closure." |
| MF-CLOSE-007 | Closure impacts all relevant accounting transactions for scoped office | Not Covered | — | GEN only verifies closure blocking for manual Journal Entry posting (TC-013, TC-017); GT explicitly calls for "various posting workflows" being restricted consistently, which is a broader, distinct claim not exercised by any other transaction type in this suite. |
| MF-CLOSE-008 | Closure list can be filtered or sorted where supported | Not Covered | — | No GEN test applies filter/sort controls to the Closing Entries table (TC-006's filter test targets the Journal Entries table's Entry Type filter, a different list). |

## Gap List (Not Covered)

- **MF-CLOSE-004** — No test verifies a duplicate closure for the same office/date scope is rejected.
- **MF-CLOSE-007** — Closure-blocking is only proven for manual journal entries, not "various posting workflows" broadly.
- **MF-CLOSE-008** — No filter/sort interaction is exercised against the Closing Entries list.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Accounting - Closures | 8 | 5 | 3 | 62.5% |
