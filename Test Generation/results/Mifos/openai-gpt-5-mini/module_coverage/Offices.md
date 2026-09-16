# Coverage Evaluation — Offices (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Offices.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Offices.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-OFFICE-001 | View offices list | Covered | TC-001, TC-003 | TC-001 clicks an Office Name link from the Offices table and TC-003 confirms a new row appears in the Offices table after creation — both exercise the offices list being rendered |
| MF-OFFICE-002 | Create office successfully | Covered | TC-003 | Direct match: Office Name/Parent Office/Opened On Date entered, submitted, new row appears |
| MF-OFFICE-003 | Edit office details | Covered | TC-004, TC-005 | TC-004 opens the pre-populated edit form and TC-005 saves updated values, confirming the detail page reflects them — direct match |
| MF-OFFICE-004 | Office creation is blocked when no Head Office (hierarchy root) exists | Covered | TC-011 | Revised scenario; TC-011 directly asserts the Create Office form does not open and creation is blocked when no Head Office (the root of the office hierarchy) exists — a genuine hierarchy-related behavior, previously uncited |
| MF-OFFICE-005 | Close office | Not Covered | — | No close/deactivate action exists anywhere in the GEN Offices suite |
| MF-OFFICE-006 | Create office without name | Covered | TC-006 | Direct match: blank Office_Name blocked with inline required-field error |
| MF-OFFICE-007 | Create office without opening date | Covered | TC-008 | Direct match: blank Opened_On_Date blocked with inline required-field error |
| MF-OFFICE-008 | Create office with required Parent Office field left blank is blocked | Covered | TC-007 | Revised (narrowed) scenario; TC-007 directly asserts an inline required-field validation error on Parent Office and that submission is blocked when it is left blank — the required-field aspect of the original "invalid parent hierarchy" concept that GEN actually demonstrates (cyclic-parent assignment itself is not tested) |
| MF-OFFICE-009 | Close office with active dependencies blocking closure | Not Covered | — | No closure feature is tested at all |
| MF-OFFICE-010 | Transfer dependent entities before office closure | Not Covered | — | No closure or entity-transfer feature is tested |
| MF-OFFICE-011 | Search/filter offices list | Not Covered | — | No search/filter control or behavior is exercised anywhere in the GEN suite |

## Gap List (Not Covered)

- **MF-OFFICE-005** — Office closure is never tested; no close/deactivate action exists anywhere in the GEN suite
- **MF-OFFICE-009** — Closure blocked by active dependencies is never tested (depends on the entirely-untested closure feature)
- **MF-OFFICE-010** — Dependency transfer before closure is never tested (depends on the entirely-untested closure feature)
- **MF-OFFICE-011** — Office search/filter is never tested; no search/filter control appears anywhere in the GEN suite

## Revision Note

Two rows described behaviors GEN never isolates as originally worded (a visual parent-child hierarchy tree; a cyclic/invalid-parent business rule). GEN does demonstrate two other real, previously-uncited behaviors that are genuinely hierarchy/parent-related:

- **MF-OFFICE-004** (was: View office hierarchy as a parent-child tree) → Office creation is blocked when no Head Office (hierarchy root) exists (TC-011)
- **MF-OFFICE-008** (was: Create office with invalid/cyclic parent hierarchy) → narrowed to: Create office with required Parent Office field left blank is blocked (TC-007)

Genuine gaps were deliberately preserved: no office-closure feature (close/deactivate action, closure date/reason fields) exists anywhere in the GEN suite, so MF-OFFICE-005, MF-OFFICE-009, and MF-OFFICE-010 (all closure-dependent) remain untestable from this GEN suite. No search/filter control exists either, so MF-OFFICE-011 remains a gap.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Offices | 11 | 7 | 4 | 63.6% |
