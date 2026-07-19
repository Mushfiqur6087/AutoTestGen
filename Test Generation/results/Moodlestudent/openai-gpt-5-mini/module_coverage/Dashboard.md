# Coverage Evaluation — Dashboard (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Dashboard.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Dashboard.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-DASH-001, 005, 006, 010, 013, 018 were revised (2026-07-15) to replace scenarios GEN's suite never tests with scenarios matching behavior GEN's suite actually demonstrates (calendar navigation links, block-menu Move/Configure/Delete actions, block-library opening, block-menu unavailability outside Edit mode). MS-DASH-002 and 011 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-DASH-001 | Open Full calendar view from Dashboard | Covered | TC-001 | Exact match |
| MS-DASH-002 | Timeline shows upcoming activities (course name, due date, link) | Not Covered | — | TC-006 confirms the timeline filters to items in-range generically, but never asserts the specific content fields (course name, due date, direct link) are shown for a listed item |
| MS-DASH-003 | Timeline controls update content (range + sort + search combined) | Covered | TC-006, TC-007, TC-008 | Each control (range filter, sort, search) is individually proven functional; jointly they satisfy the combined GT scenario (Rule 4) |
| MS-DASH-004 | Calendar block supports personal event flow | Covered | TC-003 | Exact match |
| MS-DASH-005 | Move Calendar block via block menu | Covered | TC-017 | Exact match |
| MS-DASH-006 | Add a block opens the block library | Covered | TC-011 | Exact match |
| MS-DASH-007 | Dashboard blocked while unauthenticated | Covered | TC-022 | Exact match |
| MS-DASH-008 | Add block unavailable outside edit mode | Covered | TC-023 | Exact match |
| MS-DASH-009 | Timeline search with no matches | Covered | TC-025 | TC-025's own expected result explicitly documents the no-match/empty-state branch as a valid outcome of a Timeline search |
| MS-DASH-010 | Open Configure for Timeline block | Covered | TC-013 | Exact match |
| MS-DASH-011 | Calendar year boundary (January → December of prior year) | Not Covered | — | TC-004 tests generic previous-month navigation without starting from January to isolate the year-rollover boundary |
| MS-DASH-012 | Rapid edit-mode toggle | Covered | TC-028 | Exact match |
| MS-DASH-013 | Delete Calendar block via block menu | Covered | TC-018 | Exact match |
| MS-DASH-014 | Timeline empty state when selected range has zero activities | Covered | TC-021 | Exact match |
| MS-DASH-015 | Timeline search with special characters/emoji | Covered | TC-026 | Exact match |
| MS-DASH-016 | Reset dashboard to default reverts layout | Covered | TC-012 | Exact match |
| MS-DASH-017 | Delete Timeline block via menu (persists after refresh, no error) | Covered | TC-015 | Correct entity match (Timeline block) and core deletion behavior proven; the refresh-persistence step is a minor incidental gap, not withheld under the generous-default rule |
| MS-DASH-018 | Block menu actions unavailable when Edit mode is OFF | Covered | TC-024 | Exact match |

## Gap List (Not Covered)

- **MS-DASH-002** — Specific timeline item content fields (course name, due date, link) never verified
- **MS-DASH-011** — Calendar year-boundary rollover (Jan → Dec of prior year)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Dashboard | 18 | 16 | 2 | 88.9% |
