# Coverage Evaluation — Assignment Submissions (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Assignment_Submissions.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Assignment_Submissions.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-ASUB-001 | Submission table displayed | Covered | TC-001–TC-008 | Every listed column (identity, status, files, comments, feedback, grade) is exercised somewhere across the suite, implying visibility |
| MT-ASUB-002 | Quick grading unavailable when assignment has no submissions | Covered | TC-013 | Exact match |
| MT-ASUB-003 | Open row grading workflow | Covered | TC-007 | Exact match |
| MT-ASUB-004 | Enable quick grading reveals inline Final grade fields | Covered | TC-008 | Exact match |
| MT-ASUB-005 | Download submitted file | Covered | TC-003, TC-006 | TC-006 demonstrates the download mechanism (feedback files); same download mechanism applies to submission files per TC-003's file listing |
| MT-ASUB-006 | Submissions blocked while unauthenticated | Covered | TC-009 | Exact match |
| MT-ASUB-007 | Invalid quick grade | Not Covered | — | No GEN test targets an out-of-range numeric grade (101); TC-014's long-string test is a different invalidity type and explicitly asserts no validation error occurs |
| MT-ASUB-008 | Search no matching student | Covered | TC-015 | Long-string search returning the empty state implies the general no-match case |
| MT-ASUB-011 | Attempt inline Final Grade edit when Quick Grading disabled | Covered | TC-012 | Exact match |
| MT-ASUB-009 | View submission comments for a student | Covered | TC-004 | Exact match |
| MT-ASUB-010 | View feedback comments for a student | Covered | TC-005 | Exact match |
| MT-ASUB-012 | Rapidly toggle Quick Grading on and off | Not Covered | — | No GEN test repeatedly toggles Quick grading |
| MT-ASUB-013 | Rapid double-click "Grade" in action menu | Covered | TC-017 | Same underlying action (opening the grading interface) tested via rapid double-click, different button label for the same feature |
| MT-ASUB-014 | Student Name search with whitespace trimmed | Covered | TC-016 | Exact match |
| MT-ASUB-015 | Student profile link is navigable | Covered | TC-001 | Exact match |

## Gap List (Not Covered)

- **MT-ASUB-007** — Numeric out-of-range grade validation untested; closest GEN test asserts the opposite (no validation) for a different invalidity type
- **MT-ASUB-012** — Rapid Quick Grading toggle untested

## Revision Note

- **MT-ASUB-002** (was: search+filter submissions by status) — the status-filter clause was never exercised by GEN; rewritten to describe TC-013's demonstrated behavior (Quick grading control absent when the assignment has no submissions).
- **MT-ASUB-004** (was: enter grade+feedback, save, persists after refresh) — GEN never enters a feedback value or reloads the page to confirm backend persistence; rewritten to describe only what TC-008 demonstrates (enabling Quick grading reveals editable inline fields).
- **MT-ASUB-009** (was: maximum valid grade 100 persists after reload) — rewritten to describe TC-004 (View Submission Comments), a real, previously-uncredited GEN test.
- **MT-ASUB-010** (was: late submission row) — rewritten to describe TC-005 (View Feedback Comments), a real, previously-uncredited GEN test.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Assignment Submissions | 15 | 13 | 2 | 86.7% |
