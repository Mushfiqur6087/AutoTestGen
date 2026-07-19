# Coverage Evaluation — Login (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Login.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-LOGIN-001 | Valid student login | Covered | TC-001 | Exact match |
| MS-LOGIN-002 | Guest access from login page | Covered | TC-003 | Exact match |
| MS-LOGIN-003 | Login page elements displayed | Covered | TC-001, TC-003, TC-004, TC-011 | Every listed control (Username, Password, Log in, Lost password, Access as guest, Cookies notice) is successfully interacted with somewhere across the suite, implying visibility |
| MS-LOGIN-004 | Invalid student credentials | Covered | TC-002, TC-008 | Exact match |
| MS-LOGIN-005 | Empty username | Covered | TC-005, TC-007 | Exact match |
| MS-LOGIN-006 | Empty password | Covered | TC-006, TC-007 | Exact match |
| MS-LOGIN-007 | Disabled lost-password link | Covered | TC-011 | Exact match |
| MS-LOGIN-008 | Failed login retains username | Covered | TC-002, TC-008 | Exact match |
| MS-LOGIN-009 | Long username failure handling | Covered | TC-012 | Exact match |
| MS-LOGIN-010 | Both fields empty — all errors shown simultaneously | Covered | TC-007 | Exact match |
| MS-LOGIN-011 | Username whitespace retained (not trimmed) after failed login | Not Covered | — | TC-013 asserts the *opposite* outcome — that whitespace is trimmed from the retained username — directly contradicting GT's expectation that whitespace is preserved as entered |
| MS-LOGIN-012 | Rapid double submission of Log in | Covered | TC-015 | Exact match |

## Gap List (Not Covered)

- **MS-LOGIN-011** — GEN's only touchpoint on this behavior asserts the opposite of what GT expects (trims whitespace instead of preserving it)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 12 | 11 | 1 | 91.7% |
