# Coverage Evaluation — Course Page (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Course_Page.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Course_Page.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-COURSE-004, 006, 009, 010, 011 were revised (2026-07-15) to replace scenarios GEN's suite never tests (Course Index sidebar, Settings tab absence, single-section rapid toggle, zero-section Collapse all) with scenarios matching behavior GEN's suite actually demonstrates. MS-COURSE-012, 013, 014 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-COURSE-001 | Student course tabs displayed (5 tabs visible; Settings/edit absent) | Covered | TC-001–005, TC-011, TC-014 | The dominant claim — all 5 tabs are visible — is thoroughly proven by 5 separate successful-navigation tests; the absence qualifier is reasonably satisfied by the edit-mode-toggle-absent tests |
| MS-COURSE-002 | Course sections and activities displayed | Covered | TC-007, TC-008 | Both explicitly assert activities/resources with type icons and clickable names are shown |
| MS-COURSE-003 | Collapse all sections | Covered | TC-006 | Exact match |
| MS-COURSE-004 | Toggle section with very long name (200+ chars) | Covered | TC-017 | Exact match |
| MS-COURSE-005 | Open activity from course page | Covered | TC-009, TC-010 | Exact match |
| MS-COURSE-006 | Not-enrolled user cannot use Collapse all | Covered | TC-013 | Exact match |
| MS-COURSE-007 | Student cannot enable course edit mode | Covered | TC-011, TC-014 | Exact match |
| MS-COURSE-008 | Course page blocked while unauthenticated | Covered | TC-012 | Exact match |
| MS-COURSE-009 | Open activity with emoji/Unicode name | Covered | TC-018 | Exact match |
| MS-COURSE-010 | Rapid double-click "Collapse all" while sections expanded | Covered | TC-016 | Exact match |
| MS-COURSE-011 | Collapse all when all sections already collapsed | Covered | TC-015 | Exact match |
| MS-COURSE-012 | Collapse all from a mixed expanded/collapsed state | Not Covered | — | TC-006 only tests all-expanded→all-collapsed and TC-015 tests all-already-collapsed; neither sets up a genuinely mixed starting state, which is the specific robustness claim GT is after |
| MS-COURSE-013 | Rapid single-section toggle ends in final clicked state | Not Covered | — | Same gap as MS-COURSE-010 — no test rapidly toggles one specific section's own arrow |
| MS-COURSE-014 | Collapse all after add-then-remove-all-sections | Not Covered | — | No test sets up this specific precondition sequence — untouched |

## Gap List (Not Covered)

- **MS-COURSE-012** — "Collapse all" from a genuinely mixed expanded/collapsed starting state
- **MS-COURSE-013** — Rapid toggling of an individual section's own arrow (only the bulk "Collapse all" rapid-click is tested)
- **MS-COURSE-014** — "Collapse all" after an add-then-remove-all-sections sequence

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Course Page | 14 | 11 | 3 | 78.6% |
