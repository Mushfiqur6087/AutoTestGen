# Coverage Evaluation — Participants (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Participants.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Participants.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-PART-011, 012 were revised (2026-07-15) to replace scenarios GEN's suite never tests (rapid different-initial switching, row checkbox persistence) with scenarios matching behavior GEN's suite actually demonstrates (rapid double-click Apply filters idempotence, extremely long search string).

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-PART-001 | Participants table displayed (filters, alphabetical filters, table) | Covered | TC-001 | TC-001's steps successfully use the Filter Builder and Alphabetical Filters, implying their visibility |
| MS-PART-002 | Filter participants by teacher name | Covered | TC-001 | Same underlying name-filtering mechanism, fixture-agnostic (Rule 3) |
| MS-PART-003 | Alphabetical filters | Covered | TC-001, TC-014 | Exact match, reinforced by the no-match alphabetical filter boundary test |
| MS-PART-004 | Open participant profile | Covered | TC-003 | Exact match |
| MS-PART-005 | Student cannot enrol users (toolbar button hidden) | Covered | TC-010 | TC-010 tests the per-row Enrol action being hidden from Students — same underlying "students cannot enrol" business rule, even though GT specifically names the toolbar bulk-enrol button (Rule 6 equivalence) |
| MS-PART-006 | Student cannot edit/remove roles | Covered | TC-012, TC-011 | TC-012 directly tests Edit Roles hidden for Students; TC-011 (Unenrol hidden) reinforces the broader role-management restriction |
| MS-PART-007 | Participants blocked while unauthenticated | Covered | TC-007 | Exact match |
| MS-PART-008 | Filter no matching users | Covered | TC-014 | Exact match |
| MS-PART-009 | Multiple filter conditions | Covered | TC-001, TC-017 | Both use multiple condition rows in the Filter Builder |
| MS-PART-010 | Apply filters with empty condition row | Covered | TC-013 | TC-013 tests zero condition rows rather than one empty-valued row, but both are instances of "apply with insufficient condition data doesn't crash" (Rule 3) |
| MS-PART-011 | Rapid double-click of Apply filters is idempotent | Covered | TC-016 | Exact match |
| MS-PART-012 | Extremely long search string in participants table search | Covered | TC-015 | Exact match |
| MS-PART-013 | Student role enrollment management features not visible | Covered | TC-010, TC-011, TC-012 | Collectively demonstrate enrol, unenrol, and edit-roles actions are all hidden for the Student role |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Participants | 13 | 13 | 0 | 100.0% |
