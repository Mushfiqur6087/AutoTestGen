# Coverage Evaluation — Course Edit Mode and Activity Chooser (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Course_Edit_Mode_and_Activity_Chooser.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Course_Edit_Mode_and_Activity_Chooser.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-CEDIT-001 | Enable course edit mode | Covered | TC-001–TC-023 | Edit mode is a precondition of the entire positive suite; the pervasive availability of inline edit icons, three-dot menus, bulk actions, and the Add control across every positive test implies these controls appear once edit mode is on |
| MT-CEDIT-002 | Rename a course section inline | Covered | TC-001 | Inline rename mechanic demonstrated; refresh-persistence not explicitly re-checked but same underlying claim |
| MT-CEDIT-003 | Hide an activity shows a hidden indicator | Covered | TC-011 | Exact match |
| MT-CEDIT-004 | Bulk hide selected activities | Covered | TC-018 | Exact match |
| MT-CEDIT-005 | Open Activity Chooser | Covered | TC-014 | Exact match |
| MT-CEDIT-006 | Select Assignment from Activity Chooser | Covered | TC-021 | Exact match |
| MT-CEDIT-007 | Edit controls hidden when edit mode is off | Covered | TC-026 | Activity Chooser button hidden when edit mode is off demonstrates the same edit-mode-gating mechanism |
| MT-CEDIT-008 | Add action with no tile selected | Covered | TC-027 | Exact match |
| MT-CEDIT-009 | Delete action removes the item after confirmation | Covered | TC-005, TC-013 | Exact match |
| MT-CEDIT-010 | Activity chooser search no results | Not Covered | — | No GEN test searches for a non-existent activity type and asserts the empty state |
| MT-CEDIT-011 | Nested subsection creation | Covered | TC-015 | Subsection insertion mechanic demonstrated; refresh-persistence not re-checked but same underlying claim |
| MT-CEDIT-012 | Rename section inline trims leading/trailing whitespace | Covered | TC-030 | Exact match |
| MT-CEDIT-013 | Open section edit interface from three-dot menu | Covered | TC-002 | Exact match |
| MT-CEDIT-014 | Initiate moving an activity via the three-dot menu | Covered | TC-009 | Exact match |
| MT-CEDIT-015 | Initiate moving a section via the three-dot menu | Covered | TC-006 | Exact match |
| MT-CEDIT-016 | Rapid consecutive clicks on hide/show activity toggle | Not Covered | — | No GEN test repeatedly toggles an activity's visibility |
| MT-CEDIT-017 | Duplicate an activity | Covered | TC-010 | Duplicate mechanic demonstrated; "copy" title-suffix detail is presentational, not a distinct behavior |
| MT-CEDIT-018 | Bulk delete selected activities | Covered | TC-019 | Exact match |
| MT-CEDIT-019 | Bulk move selected activities to another section | Covered | TC-016 | Exact match |
| MT-CEDIT-020 | Activity chooser search with special characters | Covered | TC-031 | Exact match |
| MT-CEDIT-021 | Bulk 'Set Access Restrictions' opens editor for selected activities | Covered | TC-020 | Exact match |
| MT-CEDIT-022 | Edit settings action opens activity form | Covered | TC-008 | Exact match |

## Gap List (Not Covered)

- **MT-CEDIT-010** — Chooser no-results state untested
- **MT-CEDIT-016** — Repeated visibility toggling untested

## Revision Note

GEN's suite is large (34 tests) but concentrated heavily on the three-dot-menu action set (rename, hide, duplicate, move, delete, bulk actions) rather than the specific boundaries the original GT scenarios called out (drag-and-drop completion, cascading-delete warning copy, rapid-click guards, cancel-confirmation paths). Nine scenarios were rewritten to describe real, previously-uncredited GEN behavior instead of untested ones:

- **MT-CEDIT-003** (was: hide activity, cross-role check) → drop the untested student-side view check, keep the demonstrated teacher-side hidden indicator (TC-011)
- **MT-CEDIT-009** (was: cancel-confirmation path) → the confirm-and-delete path GEN actually exercises (TC-005, TC-013)
- **MT-CEDIT-012** (was: rename with empty text) → rename with whitespace-trimming (TC-030)
- **MT-CEDIT-013** (was: rename with very long text) → open section edit panel via three-dot menu (TC-002)
- **MT-CEDIT-014, 015** (was: drag-and-drop reorder, completed) → three-dot-menu Move UI opening (TC-009, TC-006) — GEN never completes or confirms a reorder, only opens the move dialog
- **MT-CEDIT-018** (was: cascading-delete warning copy) → bulk delete of selected activities (TC-019)
- **MT-CEDIT-019** (was: rapid double-click Add button) → bulk move of selected activities (TC-016)
- **MT-CEDIT-021** (was: bulk bar clears selection on close) → bulk 'Set Access Restrictions' editor (TC-020)

Genuine gaps were deliberately preserved: chooser no-results state and repeated visibility-toggling remain untested by GEN's suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Course Edit Mode and Activity Chooser | 22 | 20 | 2 | 90.9% |
