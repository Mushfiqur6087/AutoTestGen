# Coverage Evaluation — Floating Rates (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Floating_Rates.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Floating_Rates.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-FRATE-001 | View floating rates list | Covered | TC-001, TC-003 | TC-001 opens the create form from the listing and TC-003 clicks a row's View link from the listing table — both presuppose and exercise the Floating Rates list being displayed (Rule 7) |
| MF-FRATE-002 | Create floating rate successfully | Covered | TC-002 | Direct match: name and a rate period entered, Create clicked, new row appears in the listing |
| MF-FRATE-003 | Add floating rate period | Covered | TC-006 | TC-006 opens an existing floating rate, adds a new Rate Period row (From Date, Interest Rate), saves, and the new period is confirmed in the Rate Periods list — direct match |
| MF-FRATE-004 | View floating rate history | Covered | TC-003 | TC-003 asserts the detail page shows a Rate Periods history table with From Date, Interest Rate, and differential-rate flag rows |
| MF-FRATE-005 | Edit floating rate metadata | Covered | TC-004, TC-006 | TC-004 opens the edit form pre-populated with metadata; TC-006 edits the name/active flag and saves, confirming updated values persist |
| MF-FRATE-006 | Create floating rate without mandatory name | Covered | TC-007 | Direct match: blank Floating Rate Name blocked with inline required-field error |
| MF-FRATE-007 | Add rate period with overlapping effective date range | Not Covered | — | No GEN test adds a rate period whose effective date range overlaps an existing period |
| MF-FRATE-008 | Add rate period with invalid rate value | Covered | TC-010 | TC-010 enters a non-numeric Interest Rate value and asserts a blocked submission with inline validation — matches "invalid rate value" generically (Rule 1) |
| MF-FRATE-009 | Loan product linked to floating rate uses latest applicable period | Not Covered | — | GEN never links a floating rate to a loan product or inspects resolved/effective rates on a loan |
| MF-FRATE-010 | Future-dated floating rate period does not affect current calculations before effective date | Not Covered | — | No GEN test inspects loan/product calculations relative to a future-dated period |
| MF-FRATE-011 | Floating rate history remains immutable for already effective periods where business rules restrict edits | Not Covered | — | GEN's only related boundary test (TC-016) concerns the Is Base Lending Rate uniqueness rule, not immutability of already-effective historical rate periods |

## Gap List (Not Covered)

- **MF-FRATE-007** — Overlapping effective-date validation for rate periods is never tested
- **MF-FRATE-009** — Loan product resolving the latest applicable floating-rate period is never tested
- **MF-FRATE-010** — Future-dated period not affecting current calculations is never tested
- **MF-FRATE-011** — Immutability of already-effective historical rate periods is never tested

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Floating Rates | 11 | 7 | 4 | 63.6% |
