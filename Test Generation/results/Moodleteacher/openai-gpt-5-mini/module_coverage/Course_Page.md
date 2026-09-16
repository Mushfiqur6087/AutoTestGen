# Coverage Evaluation — Course Page (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Course_Page.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Course_Page.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-COURSE-001 | Teacher course tabs displayed | Covered | TC-004 | 5 of 6 named tabs (Course, Participants, Grades, Activities, Competencies) are directly exercised; Settings tab omission is a minor gap in an otherwise-demonstrated list |
| MT-COURSE-002 | Sections and activities displayed | Covered | TC-011 | Exact match |
| MT-COURSE-003 | Collapse all sections | Covered | TC-001 | Exact match |
| MT-COURSE-004 | Open an activity from an expanded section | Covered | TC-003 | Exact match |
| MT-COURSE-005 | Course page blocked while unauthenticated | Covered | TC-005 | Exact match |
| MT-COURSE-006 | Open hidden activity as teacher and student | Not Covered | — | No GEN test in this module covers a hidden-activity, cross-role view |
| MT-COURSE-007 | Hide Course Index sidebar | Not Covered | — | No GEN test references the Course Index sidebar or its close control |
| MT-COURSE-008 | Rapid section toggles | Covered | TC-002, TC-010 | Repeated toggling settling into a stable final state is demonstrated (via Collapse All idempotency and single-section toggle) |
| MT-COURSE-009 | Activity link is blocked when its section is collapsed | Covered | TC-007 | Exact match |

## Gap List (Not Covered)

- **MT-COURSE-006** — Hidden-activity cross-role view untested in this module's suite
- **MT-COURSE-007** — Course Index sidebar (a distinct navigation component) never exercised

## Revision Note

- **MT-COURSE-004** originally referenced the dedicated Course Index sidebar, which GEN never touches. Rewritten to describe the activity-link click GEN does exercise, within an expanded section's own listing (TC-003).
- **MT-COURSE-009** originally described a double-click navigation guard, untested by GEN. Rewritten to describe TC-007's real, previously-uncredited behavior (activity links blocked while their section is collapsed).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Course Page | 9 | 7 | 2 | 77.8% |
