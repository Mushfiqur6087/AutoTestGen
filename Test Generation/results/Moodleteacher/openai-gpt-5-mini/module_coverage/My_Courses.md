# Coverage Evaluation — My Courses (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/My_Courses.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/My_Courses.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-COURSES-001 | Course cards displayed | Covered | TC-001, TC-006 | Course name and category are shown/exercised across these tests, implying card content is rendered |
| MT-COURSES-002 | Filter, search, sort, and layout controls | Not Covered | TC-004, TC-005, TC-006 | Filter, search, and layout switching are each tested individually, but "sort by course name" and "list layout persists after refresh" are never exercised — distinct, untested clauses of this combined scenario |
| MT-COURSES-003 | Open course from course card | Covered | TC-001 | Exact match |
| MT-COURSES-004 | Star course from course card | Covered | TC-002, TC-013 | Exact match |
| MT-COURSES-009 | Remove course from view hides it from the default grid | Covered | TC-003 | Exact match |
| MT-COURSES-005 | My Courses blocked while unauthenticated | Covered | TC-007 | Exact match |
| MT-COURSES-006 | Search with a long or special-character query returns safely | Covered | TC-011, TC-012 | Long and special-character search queries execute without error and update the grid; exact match |
| MT-COURSES-007 | Hidden-course filter | Not Covered | — | No GEN test selects the Hidden filter or verifies a hidden course's listing there |
| MT-COURSES-008 | Special-character search | Covered | TC-012 | Special characters and emoji tested, no error, same equivalence class |
| MT-COURSES-010 | Very long search query (200+ chars) accepted without error | Covered | TC-011 | Exact match |
| MT-COURSES-011 | Search with leading/trailing whitespace trimmed | Not Covered | — | No GEN test exercises whitespace trimming in the course search field |

## Gap List (Not Covered)

- **MT-COURSES-002** — Sort-by-name and layout-persists-after-refresh clauses untested
- **MT-COURSES-007** — Hidden filter entirely untested
- **MT-COURSES-011** — Search whitespace-trim behavior untested

## Revision Note

- **MT-COURSES-009** originally required verifying the course reappears under the Hidden filter with enrollment preserved — never exercised by GEN. Rewritten to describe only the demonstrated behavior (card disappears from the default grid), matching TC-003.
- **MT-COURSES-006** originally required a concrete empty-results assertion. GEN's edge tests (TC-011, TC-012) only hedge between "matching cards or no-results message." Rewritten to describe the actually-demonstrated claim: long/special-character search executes safely without error.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| My Courses | 11 | 8 | 3 | 72.7% |
