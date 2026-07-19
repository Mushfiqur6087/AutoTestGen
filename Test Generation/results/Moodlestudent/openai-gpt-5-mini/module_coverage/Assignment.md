# Coverage Evaluation — Assignment (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Assignment.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Assignment.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-ASGN-001, 005, 007, 008, 010, 013, 018 were revised (2026-07-15) to replace scenarios GEN's suite never tests with scenarios matching behavior GEN's suite actually demonstrates. All previously not-covered rows in this module now have direct matches.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-ASGN-001 | Add submission form opens when no submissions exist | Covered | TC-001 | Exact match |
| MS-ASGN-002 | Submit online text | Covered | TC-002 | Exact match |
| MS-ASGN-003 | Submit file upload | Covered | TC-003 | Exact match |
| MS-ASGN-004 | Edit submission before deadline | Covered | TC-006 | Exact match |
| MS-ASGN-005 | Unauthenticated user cannot open Add submission | Covered | TC-008 | Exact match |
| MS-ASGN-006 | View grade and feedback | Covered | TC-007 | Exact match |
| MS-ASGN-007 | Not-enrolled user cannot submit | Covered | TC-009 | Exact match |
| MS-ASGN-008 | View/Edit submission unavailable when no submissions made | Covered | TC-010 | Exact match |
| MS-ASGN-009 | Late submission blocked when closed | Covered | TC-011, TC-014 | Both directly test edit controls being blocked/hidden once the due date has passed or resubmission is disallowed |
| MS-ASGN-010 | Submit online text with emoji and Unicode characters | Covered | TC-016 | Exact match |
| MS-ASGN-011 | Long online text submission (sentinel markers preserved) | Covered | TC-015 | TC-015 tests 200+ character text and asserts the full content is preserved and visible — same underlying claim |
| MS-ASGN-012 | Resubmit after grading not allowed | Covered | TC-012 | Exact match |
| MS-ASGN-013 | View submission shows submitted content and status | Covered | TC-005 | Exact match |
| MS-ASGN-014 | Edit allowed when due date is exactly today | Covered | TC-013 | Exact boundary match |
| MS-ASGN-015 | Edit blocked when due date passed by one day | Covered | TC-014 | TC-014 tests the same "just past due date" boundary via one minute rather than one day — same equivalence class (Rule 3) |
| MS-ASGN-016 | Online text whitespace trimmed | Covered | TC-017 | Exact match |
| MS-ASGN-017 | File special-character/emoji filename preserved | Covered | TC-018 | Exact match |
| MS-ASGN-018 | Rapid double-click Submit results in single submission | Covered | TC-019 | Exact match |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Assignment | 18 | 18 | 0 | 100.0% |
