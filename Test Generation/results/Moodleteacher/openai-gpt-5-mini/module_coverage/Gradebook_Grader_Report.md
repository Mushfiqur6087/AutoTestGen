# Coverage Evaluation — Gradebook Grader Report (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Gradebook_Grader_Report.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Gradebook_—_Grader_Report.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-GRADE-001 | Grader report table displayed | Covered | TC-001, TC-003, TC-004 | Activity columns, student rows, grade cells, and the Average row are all exercised, implying visibility |
| MT-GRADE-002 | Switch report type | Not Covered | — | No GEN test switches to User report or Overview report |
| MT-GRADE-003 | Search/filter gradebook users | Covered | TC-004 | Exact match |
| MT-GRADE-004 | Edit individual grade cell | Covered | TC-001, TC-003 | Grade edit + Average row recalculation is demonstrated; explicit reload step not repeated but same underlying persistence claim |
| MT-GRADE-005 | Edit activity grade settings | Covered | TC-002 | Exact match |
| MT-GRADE-006 | Gradebook blocked while unauthenticated | Covered | TC-014 | Exact match |
| MT-GRADE-007 | Out-of-range grade blocked | Covered | TC-009, TC-016 | Same validation mechanism (value above configured maximum rejected) |
| MT-GRADE-008 | Student cannot access grader report | Not Covered | TC-012, TC-013 | GEN's non-teacher tests assume the student *can* view the Grader report (just not use certain controls); GT expects the whole report to be inaccessible — a different access model, not merely untested |
| MT-GRADE-011 | Edit a Grade cell when Edit Mode is disabled | Covered | TC-011 | Exact match |
| MT-GRADE-012 | Enter non-numeric value into Grade cell | Covered | TC-007 | Exact match |
| MT-GRADE-014 | Grade one unit above activity maximum | Covered | TC-016 | Exact match |
| MT-GRADE-009 | Minimum valid grade | Covered | TC-017 | Exact match |
| MT-GRADE-010 | Decimal grade precision | Covered | TC-022 | TC-022 establishes decimal grades are accepted and displayed per the system's defined precision, which implies a one-decimal value like 89.5 is preserved rather than rounded to a whole number |
| MT-GRADE-013 | Grade exactly equals activity maximum | Covered | TC-015 | Exact match |
| MT-GRADE-015 | Grade exactly equals activity minimum | Covered | TC-017 | Exact match |
| MT-GRADE-016 | Very long comment in grade cell | Not Covered | — | GEN's suite only exercises the numeric New_Grade field; no test targets a separate comment field |

## Gap List (Not Covered)

- **MT-GRADE-002** — Report-type switching untested
- **MT-GRADE-008** — GEN's access model for non-teacher roles differs from GT's expectation (partial page access vs. full block)
- **MT-GRADE-016** — Grade-cell comment field never exercised

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Gradebook Grader Report | 16 | 13 | 3 | 81.2% |
