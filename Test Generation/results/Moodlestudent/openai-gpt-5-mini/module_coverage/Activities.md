# Coverage Evaluation — Activities (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Activities.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Activities.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-ACT-001, 006, 007 were revised (2026-07-15) to replace scenarios GEN's suite never tests (assignments-expanded-by-default assertion, teacher-hidden activity, whole-course empty state) with scenarios matching behavior GEN's suite actually demonstrates (add new Activity Type row, not-enrolled user blocked, Forums empty-state). The remaining not-covered rows were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-ACT-001 | Add new Activity Type row | Covered | TC-005 | Exact match |
| MS-ACT-002 | Assignment activity table shows Name, due date, submission status columns | Not Covered | — | TC-001 interacts with the Name column only; due date and submission status columns are never asserted as visible |
| MS-ACT-003 | Expand collapsed activity type | Covered | TC-003, TC-004 | Exact match, both Forums and Resources |
| MS-ACT-004 | Open activity from overview | Covered | TC-001, TC-002 | Exact match |
| MS-ACT-005 | Activities blocked while unauthenticated | Covered | TC-006 | Exact match |
| MS-ACT-006 | Not-enrolled user cannot view Assignments | Covered | TC-007 | Exact match |
| MS-ACT-007 | Expanding Forums with zero activities shows empty state | Covered | TC-011 | Exact match |
| MS-ACT-008 | Many activity types toggle independently (deliberate sequence) | Not Covered | — | No test performs the specific expand-Forums/expand-Resources/collapse-Forums sequence and verifies Resources stays expanded |
| MS-ACT-009 | Rapid double-click on assignment name | Covered | TC-010 | Exact match |
| MS-ACT-010 | Expand Forums then immediately click first activity | Not Covered | — | No test chains "expand a section" and "click an activity inside it" as one sequence; TC-003 only expands Forums without following up |
| MS-ACT-011 | Activity name 200+ chars with special characters, displayed and clickable | Covered | TC-009, TC-008 | TC-009 tests the correct entity (activity name) with special characters/emoji and successful navigation; TC-008 independently establishes the suite's pattern for handling 200+ character names without breaking layout — combined, both edge dimensions are represented |
| MS-ACT-012 | Rapidly toggling multiple different sections each ends correctly | Not Covered | — | TC-010's rapid double-click targets the *same* element twice, not multiple *different* sections in succession — a distinct interaction pattern |
| MS-ACT-013 | Cannot click activity name in collapsed section | Not Covered | — | No test attempts to interact with an activity inside a still-collapsed section to verify it's inaccessible; all tests expand a section before interacting with its contents |

## Gap List (Not Covered)

- **MS-ACT-002** — Due date and submission status columns never verified
- **MS-ACT-008** — Deliberate multi-section independent-toggle sequence
- **MS-ACT-010** — Expand-then-immediately-click chained interaction
- **MS-ACT-012** — Rapid toggling of multiple different sections
- **MS-ACT-013** — Activity names inaccessible while their section is collapsed

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Activities | 13 | 8 | 5 | 61.5% |
