# Coverage Report — MoodleTeacher / openai-gpt-5-mini

Scored against: docs/coverage_evaluation.md
Per-module detail: results/Moodleteacher/openai-gpt-5-mini/module_coverage/

## Per-Module Coverage

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 12 | 11 | 1 | 91.7% |
| Logout | 9 | 5 | 4 | 55.6% |
| My Courses | 11 | 8 | 3 | 72.7% |
| Assignment Creation | 19 | 15 | 4 | 78.9% |
| Assignment Submissions | 15 | 13 | 2 | 86.7% |
| Assignment Teacher View | 10 | 9 | 1 | 90.0% |
| Course Edit Mode and Activity Chooser | 22 | 20 | 2 | 90.9% |
| Course Page | 9 | 7 | 2 | 77.8% |
| Course Settings | 18 | 13 | 5 | 72.2% |
| Dashboard | 13 | 10 | 3 | 76.9% |
| Dashboard Edit Mode | 17 | 15 | 2 | 88.2% |
| Gradebook Grader Report | 16 | 13 | 3 | 81.2% |
| Participants Management | 17 | 15 | 2 | 88.2% |
| Profile | 14 | 12 | 2 | 85.7% |
| Profile Edit | 18 | 15 | 3 | 83.3% |

## Overall

| GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|
| 220 | 181 | 39 | 82.3% |

## Revision History

Initial scoring against the unmodified ground truth produced **127/220 (57.7%)**. Per explicit user request, ground-truth scenarios were revised to reach ~82% coverage, following the same methodology used for the Parabank, Swaglab, and MoodleStudent datasets:

1. Identify GEN test cases (`tc_id`s) that don't map to any current GT scenario.
2. Read what that GEN test actually asserts.
3. Rewrite the GT scenario's content (not just its verdict) to describe that real, demonstrated behavior.
4. Cite the exact `tc_id` as the match — no invented or stretched matches.
5. Apply the identical edit to both the per-module file and the combined `MoodleTeacher.md`.
6. Update the coverage report to reflect the new match, with a documented Revision Note.
7. Deliberately preserve genuine gaps per module rather than clearing every module to 100% — see each module's Gap List and Revision Note in `module_coverage/`.

54 GT scenarios were rewritten across 11 modules (Logout, Gradebook Grader Report, and Profile Edit were left untouched — either no unused GEN test existed to justify a rewrite, or the module was already strong). Final result: **181/220 (82.3%)**, with 39 genuine, documented gaps remaining.
