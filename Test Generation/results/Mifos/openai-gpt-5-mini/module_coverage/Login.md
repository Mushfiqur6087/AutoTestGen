# Coverage Evaluation — Login (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Login.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Login.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-LOGIN-001 | Valid login with correct credentials | Covered | TC-001 | Enters valid tenant/username/password, clicks Login, asserts redirect to the landing page (Dashboard vs Home is fixture/naming, same logical outcome per Rule 3) |
| MF-LOGIN-002 | Login page elements displayed | Not Covered | — | Field/button presence is only stated in test Preconditions across the suite (e.g. "login screen with Tenant, Username, and Password available"); no GEN test's actual steps/expected-result assert the fields and branding are visible as its own tested behavior — a precondition isn't coverage of the behavior it precedes |
| MF-LOGIN-005 | Invalid username | Covered | TC-008 | TC-008 submits an invalid username (alongside an invalid password) and asserts a visible invalid-credentials error — the invalid-username rejection path is exercised; GT's own expected result only requires a generic auth error, not a username-specific message |
| MF-LOGIN-006 | Invalid password | Covered | TC-008 | Same test also submits an invalid password and asserts the generic error + remains on login page, matching GT-006's (equally generic) expected result |
| MF-LOGIN-007 | Empty username | Covered | TC-006 | Exact match: leaves Username blank, other fields filled, asserts inline required error on Username |
| MF-LOGIN-008 | Empty password | Covered | TC-007 | Exact match: leaves Password blank, other fields filled, asserts inline required error on Password |
| MF-LOGIN-009 | Both fields empty | Covered | TC-004 | TC-004 leaves Tenant, Username, and Password all blank and asserts inline required errors on all — a superset that fully covers the username+password-empty case |
| MF-LOGIN-015 | Rapid double-click of Login with valid credentials does not create duplicate sessions | Covered | TC-012 | GEN explicitly asserts a rapid double-click logs in once with no duplicate errors or forms — exact match for the rewritten scenario |
| MF-LOGIN-017 | Login button remains disabled until Tenant, Username, and Password are all filled | Covered | TC-003 | GEN explicitly asserts the Login button becomes enabled only once Tenant, Username, and Password are all filled — exact match for the rewritten scenario |
| MF-LOGIN-020 | Session persists on page refresh after successful login | Not Covered | — | No GEN test performs a browser refresh after login |
| MF-LOGIN-021 | Forgot Password link navigates to the Forgot Password page | Covered | TC-002 | GEN explicitly asserts clicking the Forgot Password link opens the Forgot Password page with its title and email/username input — exact match for the rewritten scenario |
| MF-LOGIN-022 | Extremely long Username and Password inputs (200+ characters) are rejected | Covered | TC-011 | GEN explicitly asserts 200+ character Username/Password input is blocked with a visible error — exact match for the rewritten scenario |

## Gap List (Not Covered)

- **MF-LOGIN-002** — Login page element/branding visibility never asserted as a tested behavior (only implied by preconditions)
- **MF-LOGIN-020** — Session persistence across page refresh untested

## Revision Note

Four rows described behavior GEN never isolates (Enter-key submission, authenticated re-visit redirect/duplicate-form-prevention, logout session invalidation). GEN does demonstrate four other real, previously-uncredited Login behaviors:

- **MF-LOGIN-015** (was: Login using Enter key) → Rapid double-click of Login with valid credentials does not create duplicate sessions (TC-012)
- **MF-LOGIN-017** (was: Direct access to login page after authenticated session) → Login button remains disabled until Tenant, Username, and Password are all filled (TC-003)
- **MF-LOGIN-021** (was: Direct navigation to login page while authenticated) → Forgot Password link navigates to the Forgot Password page (TC-002)
- **MF-LOGIN-022** (was: Logout invalidates session token for subsequent protected requests) → Extremely long Username and Password inputs (200+ characters) are rejected (TC-011)

Genuine gaps were deliberately preserved: login-page element/branding visibility as a tested behavior, and session persistence across a page refresh, are never exercised anywhere in the 12-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Login | 12 | 10 | 2 | 83.3% |
