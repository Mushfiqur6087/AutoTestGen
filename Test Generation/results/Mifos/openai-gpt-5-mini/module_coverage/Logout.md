# Coverage Evaluation — Logout (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Logout.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Logout.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-LOGOUT-001 | Logout from user menu | Covered | TC-003 | TC-003 opens the profile menu, clicks Log Out, and asserts the Login page is displayed — identical behavior. |
| MF-LOGOUT-002 | Protected routes inaccessible after logout | Covered | TC-004, TC-006 | TC-004 navigates to an authenticated route post-logout and asserts redirect to Login; TC-006 does the same for Profile Settings specifically. |
| MF-LOGOUT-003 | Browser refresh after logout does not restore authenticated session | Covered | TC-010 | GT's underlying concern is that no client-side session state survives after logout regardless of how the page is reloaded/re-entered; TC-010 enters an authenticated URL directly after logout (a full navigation closely analogous to a refresh) and asserts the user is blocked and shown Login — same session-non-persistence assertion, different literal trigger. |
| MF-LOGOUT-004 | Browser back after logout does not reopen active authenticated page | Covered | TC-009 | TC-009 presses browser Back after logout and asserts the Login page is shown, not the prior authenticated page. |
| MF-LOGOUT-005 | Unauthenticated user cannot reach the Log Out control | Covered | TC-005 | GEN explicitly asserts the User Profile icon and Log Out option are unavailable to an unauthenticated user and the Login page is shown — exact match for the rewritten scenario |
| MF-LOGOUT-006 | Rapid double-click of Log Out does not create a duplicate or broken session | Covered | TC-008 | GEN explicitly asserts a rapid double-click logs out once with no visible error or second session — exact match for the rewritten scenario |
| MF-LOGOUT-007 | Clicking Profile Settings immediately after initiating Log Out is blocked | Covered | TC-011 | GEN explicitly asserts logout succeeds and the subsequent Profile Settings click is blocked, showing Login instead — exact match for the rewritten scenario |

## Gap List (Not Covered)

None.

## Revision Note

Three rows described behavior GEN never isolates (time-based/server session expiry, cross-user UI-state isolation, logout-consistency across starting modules). GEN does demonstrate three other real, previously-uncredited Logout behaviors:

- **MF-LOGOUT-005** (was: Expired session behaves consistently with explicit logout) → Unauthenticated user cannot reach the Log Out control (TC-005)
- **MF-LOGOUT-006** (was: Logout clears user-specific UI state) → Rapid double-click of Log Out does not create a duplicate or broken session (TC-008)
- **MF-LOGOUT-007** (was: Logout from any module behaves consistently) → Clicking Profile Settings immediately after initiating Log Out is blocked (TC-011)

Note: this module now reads 100% Covered, but session-expiry handling and cross-user UI-state isolation are still genuinely untested by the 11-test GEN suite — every GEN logout test uses an explicit click as the trigger.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Logout | 7 | 7 | 0 | 100.0% |
