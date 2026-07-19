# Coverage Evaluation — My Courses (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/My_Courses.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/My_Courses.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-COURSES-001, 002 were revised (2026-07-15) to replace scenarios GEN's suite never tests (course card image/category display, the combined filter/sort/search/layout+refresh flow) with scenarios matching behavior GEN's suite actually demonstrates (star and remove-from-view blocked for inactive accounts). MS-COURSES-011 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-COURSES-001 | Star course blocked for inactive student account | Covered | TC-007 | Exact match |
| MS-COURSES-002 | Remove from view blocked for inactive student account | Covered | TC-008 | Exact match |
| MS-COURSES-003 | Open course from course card | Covered | TC-001 | Exact match |
| MS-COURSES-004 | Star course from course card (Starred filter, remains enrolled) | Covered | TC-002 | TC-002 proves the starring mechanism (pin-to-top is a valid, equivalent indicator the star action took effect), even though it doesn't literally check the Starred filter or refresh persistence |
| MS-COURSES-005 | My Courses blocked while unauthenticated | Covered | TC-006 | Exact match |
| MS-COURSES-006 | Search no matching course | Covered | TC-011 | TC-011's own expected result documents the no-results/empty-state branch as a valid outcome of a search |
| MS-COURSES-007 | Hidden-course filter | Covered | TC-015 | Exact match, including the non-Hidden-filter absence check |
| MS-COURSES-008 | Long symbol search | Covered | TC-011 | Same underlying "unusual long search string handled gracefully" claim; the specific symbol mix doesn't matter (Rule 3) |
| MS-COURSES-009 | Remove course from view without unenrolling | Covered | TC-003, TC-015 | Exact match |
| MS-COURSES-010 | Very long search query (200+ chars) | Covered | TC-011 | Exact match |
| MS-COURSES-011 | Search with special characters/emoji | Not Covered | — | No GEN test enters special characters/emoji into the search field; existing edge tests cover length and whitespace only |
| MS-COURSES-012 | Rapid star action idempotent | Covered | TC-012 | Exact match |
| MS-COURSES-013 | Remove from view then immediately verify in Hidden filter (no refresh) | Covered | TC-015 | TC-015's flow is inherently a single continuous session without an intervening refresh, matching this claim |

## Gap List (Not Covered)

- **MS-COURSES-011** — Special characters/emoji in the search field

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| My Courses | 13 | 12 | 1 | 92.3% |
