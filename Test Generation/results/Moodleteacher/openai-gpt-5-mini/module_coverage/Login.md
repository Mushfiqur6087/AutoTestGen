# Coverage Evaluation — Login (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Login.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-LOGIN-001 | Valid teacher login | Covered | TC-001 | Exact match |
| MT-LOGIN-002 | Guest access from login page | Covered | TC-002 | Exact match |
| MT-LOGIN-003 | Cookie notice opens | Covered | TC-003 | Exact match |
| MT-LOGIN-004 | Invalid teacher credentials | Covered | TC-008 | Exact match |
| MT-LOGIN-005 | Empty username | Covered | TC-005 | Exact match |
| MT-LOGIN-006 | Empty password | Covered | TC-006 | Exact match |
| MT-LOGIN-007 | Disabled lost-password link | Covered | TC-004, TC-009, TC-015 | Exact match |
| MT-LOGIN-008 | Failed login retains username | Covered | TC-008, TC-014 | Exact match |
| MT-LOGIN-009 | Log in action blocked while already authenticated | Covered | TC-011 | Exact match |
| MT-LOGIN-010 | Both fields empty shows simultaneous validation | Covered | TC-007 | GEN submits with both fields empty and asserts rejection; same behavior |
| MT-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Not Covered | — | TC-012/TC-013 confirm long strings and Unicode/emoji are retained verbatim, but neither exercises whitespace specifically — a distinct, commonly-mishandled boundary (auto-trim) a tester would isolate separately |
| MT-LOGIN-012 | Very long username rejected without crash | Covered | TC-012 | Exact match |

## Gap List (Not Covered)

- **MT-LOGIN-011** — Whitespace-preservation boundary not isolated (only length/Unicode boundaries tested)

## Revision Note

MT-LOGIN-009 originally described a rapid double-click submit scenario that GEN never exercises. Rewritten to describe TC-011 (Log in blocked while already authenticated), a real precondition-failure path GEN's suite demonstrates for this module.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 12 | 11 | 1 | 91.7% |
