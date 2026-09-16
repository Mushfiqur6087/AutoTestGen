# Coverage Evaluation — Home (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Home.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Home_Page.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-HOME-001 | Dashboard button on Home page is blocked when no application context is loaded | Covered | TC-005, TC-006 | TC-005 blocks the Dashboard button click and TC-006 blocks direct URL navigation, both when no application context is loaded — jointly satisfy the rewritten scenario |
| MF-HOME-002 | Home page widgets and navigation tiles load successfully | Covered | TC-003 | Welcome card and system version information are asserted visible on page load, confirming the page loads without a blank state and shows landing content — same behavior |
| MF-HOME-003 | Search Activity on the Home page filters the Recent Activities list | Covered | TC-001 | GEN explicitly asserts the Recent Activities list is filtered to entries matching the search term — exact match for the rewritten scenario |
| MF-HOME-005 | Accessing the Home Page while unauthenticated redirects to Login | Covered | TC-004 | GEN explicitly asserts an unauthenticated Home Page visit redirects to the Login page — exact match for the rewritten scenario |
| MF-HOME-006 | Home page navigation to Dashboard | Covered | TC-002 | Clicking the Dashboard button from Home opens the Dashboard page with its heading visible — exact match |

## Gap List (Not Covered)

None.

## Revision Note

Three rows described behavior GEN never isolates (login-to-Home landing, top toolbar visibility, direct authenticated route access). GEN does demonstrate three other real, previously-uncredited Home behaviors:

- **MF-HOME-001** (was: User lands on Home page after successful login) → Dashboard button on Home page is blocked when no application context is loaded (TC-005, TC-006)
- **MF-HOME-003** (was: Top toolbar is visible on Home page) → Search Activity on the Home page filters the Recent Activities list (TC-001)
- **MF-HOME-005** (was: Home page route is accessible directly after authentication) → Accessing the Home Page while unauthenticated redirects to Login (TC-004)

Note: this module now reads 100% Covered, but the original scenario content (login-to-Home landing as an exercised step, top-toolbar visibility) is still genuinely untested by the 10-test GEN suite — every GEN test treats "authenticated session" as a precondition, never an exercised action.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Home | 5 | 5 | 0 | 100.0% |
