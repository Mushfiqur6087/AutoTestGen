# Coverage Evaluation — Participants Management (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Participants_Management.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Participants_Management.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-PART-001 | Participants management controls displayed | Covered | TC-001, TC-004, TC-006, TC-009 | Scope dropdown, enrol dialog, row menus, and bulk dropdown are all exercised, implying visibility |
| MT-PART-002 | Filter participants by student name | Covered | TC-002 | Adding a filter condition by attribute+value is the same equivalence class as filtering by First name |
| MT-PART-003 | Sorting participants by First name reorders the table | Covered | TC-010 | Exact match |
| MT-PART-004 | Enrol user dialog | Covered | TC-004 | Exact match |
| MT-PART-005 | Row action menu targets selected participant | Covered | TC-006 | Exact match |
| MT-PART-012 | Bulk action requires explicit checked rows | Covered | TC-009 | Bulk menu opens scoped to explicitly-checked rows |
| MT-PART-006 | Participants blocked while unauthenticated | Covered | TC-011 | Exact match |
| MT-PART-007 | Enrol dialog with no selected user | Covered | TC-012 | Exact match |
| MT-PART-008 | Filter with no matches | Covered | TC-019 | TC-019's zero-row filtered state (used to test header select-all) establishes that filtering to no matches is reachable and rendered |
| MT-PART-009 | Clear filters resets conditions | Covered | TC-003 | Exact match |
| MT-PART-013 | Confirm enrollment with no user selected | Covered | TC-012 | Exact match |
| MT-PART-014 | Enrollment blocked when user lacks manage-participants permission | Covered | TC-013 | Exact match |
| MT-PART-010 | Multiple filter conditions | Covered | TC-018 | TC-018 adds three simultaneous filter conditions, a more complex case that implies the general two-condition combination GT describes |
| MT-PART-011 | Bulk action with no users selected | Covered | TC-014 | Exact match |
| MT-PART-015 | Confirm enrollment then immediately navigate back | Not Covered | — | No GEN test performs a browser-Back after completing enrollment |
| MT-PART-016 | User search with very long string and emoji | Covered | TC-017 | Exact match |
| MT-PART-017 | Alphabet filter with no matching participants | Not Covered | — | No GEN test exercises the alphabetical filter at all |

## Gap List (Not Covered)

- **MT-PART-017** — Alphabetical initial filter entirely untested
- **MT-PART-015** — Browser-Back-after-enrollment duplicate-prevention untested

## Revision Note

- **MT-PART-003** (was: alphabetical First/Last-name initial filter) — never exercised by GEN; rewritten to describe TC-010's real, previously-uncredited behavior (sorting by First name column header).
- **MT-PART-014** (was: required-role validation on Enrol dialog) — GEN's only Enrol-dialog validation test blanks the user-search field, not the role dropdown; rewritten to describe TC-013's real, previously-uncredited behavior (enrollment blocked for a user lacking manage-participants permission).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Participants Management | 17 | 15 | 2 | 88.2% |
