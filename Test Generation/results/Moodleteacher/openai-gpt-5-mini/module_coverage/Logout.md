# Coverage Evaluation — Logout (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Logout.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Logout.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-LOGOUT-001 | Logout from user menu | Covered | TC-001 | Exact match |
| MT-LOGOUT-002 | Protected page requires re-authentication after logout | Covered | TC-003, TC-006 | Exact match |
| MT-LOGOUT-003 | Browser back after logout | Covered | TC-005 | Exact match |
| MT-LOGOUT-004 | Logout action unavailable while logged out | Covered | TC-002 | Exact match |
| MT-LOGOUT-005 | Double-click logout | Covered | TC-004 | Exact match |
| MT-LOGOUT-006 | Session timeout behaves like logout | Not Covered | — | No GEN test exercises session expiry; GEN only tests explicit logout, not timeout |
| MT-LOGOUT-007 | Concurrent sessions log out | Not Covered | — | No GEN test covers a two-tab/session scenario |
| MT-LOGOUT-008 | Logout URL CSRF protection | Not Covered | — | No GEN test exercises the logout.php CSRF-token path |
| MT-LOGOUT-009 | Rapid navigation during logout | Not Covered | — | TC-004 tests rapid double-click of Log out itself, not clicking an unrelated nav link mid-redirect; the specific race condition isn't exercised |

## Gap List (Not Covered)

- **MT-LOGOUT-006** — Session-timeout path entirely untested
- **MT-LOGOUT-007** — Concurrent multi-tab session behavior entirely untested
- **MT-LOGOUT-008** — CSRF protection on the logout endpoint entirely untested
- **MT-LOGOUT-009** — Race between logout redirect and a separate navigation click not exercised

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Logout | 9 | 5 | 4 | 55.6% |
