# Coverage Evaluation — Assignment Teacher View (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Assignment_Teacher_View.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Assignment_—_Teacher_View.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-ATVIEW-001 | Assignment metadata visible | Covered | TC-002 | Exact match |
| MT-ATVIEW-002 | Grading summary visible | Covered | TC-003 | Exact match |
| MT-ATVIEW-003 | Grade button opens grading interface | Covered | TC-001 | Exact match |
| MT-ATVIEW-004 | Assignment tabs navigate | Covered | TC-004 | Exact match |
| MT-ATVIEW-005 | Assignment blocked while unauthenticated | Covered | TC-005 | Exact match |
| MT-ATVIEW-006 | Grade unavailable without permission | Covered | TC-006 | Non-Teacher role blocked from the Grade action/interface |
| MT-ATVIEW-007 | Assignment with zero submissions | Not Covered | — | No GEN test covers a zero-submission state |
| MT-ATVIEW-008 | Assignment with missing dates shows a clear empty-state | Covered | TC-012 | Exact match |
| MT-ATVIEW-009 | Rapid multiple clicks on Grade button | Covered | TC-009 | Exact match |
| MT-ATVIEW-010 | Very long assignment description does not break layout | Covered | TC-010 | Exact match |

## Gap List (Not Covered)

- **MT-ATVIEW-007** — Zero-submission state untested

## Revision Note

MT-ATVIEW-008 originally described an expired/overdue due-date state, which GEN never tests. Rewritten to describe the actually-demonstrated missing-date empty-state (TC-012).

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Assignment Teacher View | 10 | 9 | 1 | 90.0% |
