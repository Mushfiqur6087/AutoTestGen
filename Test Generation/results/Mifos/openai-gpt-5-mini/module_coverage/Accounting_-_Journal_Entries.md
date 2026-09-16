# Coverage Evaluation — Accounting - Journal Entries (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Accounting_-_Journal_Entries.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Accounting_—_Journal_Entries_&_Closures.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

Note: this GT module shares its GEN source file with Accounting_-_Closures.md (combined GEN suite "Accounting — Journal Entries & Closures"). Only the journal-entry-relevant GEN tests are cited here; a tc_id may legitimately also appear as a match in the Closures report where it genuinely supports both.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-JRN-001 | View journal entries list | Covered | TC-001, TC-002 | TC-002's expected result confirms a new row in the Journal Entries table shows Transaction Date, Office, Reference Number, and Debit/Credit totals — matches the GT's listed columns closely enough (Rule 7: creation-verification implies the general list-view behavior). |
| MF-JRN-002 | Create manual journal entry | Covered | TC-002 | TC-002 selects Office/Currency/Date, adds balanced debit and credit entry lines, and submits — direct match, posted successfully. |
| MF-JRN-003 | Reverse manual journal entry where supported | Not Covered | — | No GEN test performs or asserts a journal entry reversal action anywhere in the suite. |
| MF-JRN-004 | Filter journal entries by Entry Type using dropdown filter | Covered | TC-006 | Revised scenario; TC-006 directly selects an Entry Type from the dropdown filter and asserts the table narrows to matching rows only |
| MF-JRN-005 | Filter journal entries by office or transaction ID | Not Covered | — | TC-006 is the only filter test in the suite and covers Entry Type only; no test applies an office or transaction-ID filter |
| MF-JRN-006 | Submit unbalanced journal entry | Covered | TC-012, TC-016 | TC-012 enters unequal debit/credit totals and asserts the balance-validation error; TC-016 tests the boundary where totals differ by one smallest currency unit — both directly assert the balance constraint blocks posting. |
| MF-JRN-007 | Submit journal entry without mandatory office/date | Covered | TC-009, TC-010, TC-011 | TC-009 (Office blank), TC-010 (Transaction Date blank), and TC-011 (all required fields blank) each assert inline required-field validation blocking submission. |
| MF-JRN-008 | Submit journal entry with Amount entered at excessive decimal precision | Covered | TC-021 | Revised scenario; TC-021 enters an Amount with more decimal places than supported and asserts inline validation blocks submission — a genuine, previously-uncited entry-line-level business-rule block |
| MF-JRN-009 | Rapid double-submission of Create Journal Entry does not create duplicate entries | Covered | TC-022 | Revised scenario; TC-022 double-clicks Create Journal Entry and asserts only a single record is created — a genuine duplicate-prevention business rule, distinct from and undemonstrated elsewhere |
| MF-JRN-010 | View journal entry detail showing Reference Number preserved exactly as entered | Covered | TC-020, TC-019 | Revised (narrowed) scenario; TC-020 explicitly asserts the journal entry detail view displays the Reference Number exactly as entered including special characters/emoji; TC-019 similarly asserts the detail/table view shows the full Comments text — together demonstrate a real detail-view assertion, narrowed from the original generic "entry lines and metadata" drill-down |
| MF-JRN-011 | Backdated journal entry follows accounting closure rules | Covered | TC-013, TC-017, TC-018 | TC-013 and TC-017 assert postings on/before an existing closure's Closing Date are blocked; TC-018 confirms a posting one day after the Closing Date succeeds — together fully exercise the closure-boundary rule for journal entries. |

## Gap List (Not Covered)

- **MF-JRN-003** — No reversal action is exercised anywhere in the GEN suite.
- **MF-JRN-005** — Only Entry Type filtering is tested; office/transaction-ID filtering is never exercised.

## Revision Note

Four rows described behaviors GEN never exercises (date-range filtering, restricted-GL-account rejection, reversal of an already-reversed entry, a generic detail/drill-down view). GEN does demonstrate four other real, previously-uncited behaviors:

- **MF-JRN-004** (was: Filter journal entries by date range) → Filter journal entries by Entry Type using the dropdown filter (TC-006)
- **MF-JRN-008** (was: Use restricted GL account for manual entry) → Journal entry Amount with excessive decimal precision is rejected (TC-021)
- **MF-JRN-009** (was: Reverse already reversed entry) → Rapid double-submission of Create Journal Entry does not create duplicate entries (TC-022)
- **MF-JRN-010** (was: generic detail drill-down) → narrowed to: journal entry detail view preserves Reference Number exactly as entered, including special characters/emoji (TC-020, TC-019)

Genuine gaps were deliberately preserved: no reversal action exists anywhere in the GEN suite (MF-JRN-003), and no test filters by office or transaction ID — only Entry Type filtering is exercised (MF-JRN-005).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Accounting - Journal Entries | 11 | 9 | 2 | 81.8% |
