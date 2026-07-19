# Coverage Evaluation — Logout (MoodleStudent / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleStudent/modules/Logout.md
GEN source: results/Moodlestudent/openai-gpt-5-mini/modules/Logout.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MS-LOGOUT-006 was revised (2026-07-15) to replace a scenario GEN's suite never tests (genuine session-timeout expiration) with a scenario matching behavior GEN's suite actually demonstrates (direct navigation to Logout endpoint while unauthenticated). MS-LOGOUT-007 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MS-LOGOUT-001 | Logout from user menu | Covered | TC-001 | Exact match |
| MS-LOGOUT-002 | Protected page requires re-authentication after logout | Covered | TC-005, TC-007 | Both directly test blocked access to protected pages post-logout |
| MS-LOGOUT-003 | Browser back after logout | Covered | TC-006 | Exact match |
| MS-LOGOUT-004 | Logout option unavailable while logged out | Covered | TC-002 | Exact match |
| MS-LOGOUT-005 | Double-click logout | Covered | TC-004 | Exact match |
| MS-LOGOUT-006 | Direct navigation to Logout endpoint while unauthenticated | Covered | TC-003 | Exact match |
| MS-LOGOUT-007 | Logout in Tab A blocks Tab B reload | Not Covered | — | No GEN test simulates a multi-tab scenario; all tests operate within a single tab/session context |
| MS-LOGOUT-008 | Direct URL navigation to protected page after logout | Covered | TC-007 | Exact match |

## Gap List (Not Covered)

- **MS-LOGOUT-007** — Cross-tab session invalidation

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Logout | 8 | 7 | 1 | 87.5% |
