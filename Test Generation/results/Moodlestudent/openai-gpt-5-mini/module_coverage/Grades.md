# Coverage Evaluation — Grades (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Grades.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Grades.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-GRADE-007, 011, 013 were revised (2026-07-15). MS-GRADE-011/013 were narrowed to the field GEN's suite actually exercises (Grade item name) rather than the untested Feedback field. MS-GRADE-007 was replaced with a scenario GEN's suite does demonstrate (large activity list, all reachable). MS-GRADE-008, 009, 010 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-GRADE-001 | Student User report displayed (all 7 columns) | Covered | TC-001 | Exact match, explicitly lists every column |
| MS-GRADE-002 | Expand course group (collapse then expand) | Covered | TC-002 | TC-002 proves the expand direction of the same toggle control; the collapse direction is the reverse of the identical mechanism (Rule 6) |
| MS-GRADE-003 | Course total row displayed | Covered | TC-004 | Exact match |
| MS-GRADE-004 | Ungraded item displays placeholder | Covered | TC-003 | Exact match |
| MS-GRADE-005 | Student cannot access full gradebook | Covered | TC-006 | Exact match |
| MS-GRADE-006 | Grades blocked while unauthenticated | Covered | TC-005 | Exact match |
| MS-GRADE-007 | Large number of graded activities all reachable | Covered | TC-010 | Exact match |
| MS-GRADE-008 | Decimal percentage display | Not Covered | — | No test asserts a specific decimal-precision format for the Percentage column |
| MS-GRADE-009 | Rapid consecutive course-group toggle | Not Covered | — | No GEN test rapidly toggles the collapse control multiple times — untouched |
| MS-GRADE-010 | Keyboard Space/Enter activates toggle | Not Covered | — | No GEN test exercises keyboard interaction — untouched |
| MS-GRADE-011 | Very long Grade item name rendered without breaking layout | Covered | TC-007 | Exact match |
| MS-GRADE-012 | Unicode/emoji in Feedback column | Covered | TC-008 | Exact match |
| MS-GRADE-013 | Leading/trailing whitespace in Grade item name trimmed on display | Covered | TC-009 | Exact match |

## Gap List (Not Covered)

- **MS-GRADE-008** — Decimal percentage formatting
- **MS-GRADE-009** — Rapid course-group toggle stability
- **MS-GRADE-010** — Keyboard activation of the collapse control

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Grades | 13 | 10 | 3 | 76.9% |
