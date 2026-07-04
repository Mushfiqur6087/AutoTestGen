# Test Cases — Moodleteacher

Generated: 2026-07-04T15:16:12.934753Z  
Model: openai/gpt-5-mini  

## Login

Total: **14** (positive: 3, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful teacher login redirects to Dashboard | User is unauthenticated and at the site's login page; valid <teacher credentials> are available | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the 'Log in' button | User is redirected to the Dashboard; the Dashboard page is displayed | high |
| TC-002 | WF-002 | Access site as a guest to browse limited content | User is unauthenticated and at the site's login page | 1. Click the 'Access as a guest' button | Limited unauthenticated browsing of site content is granted and guest-accessible content is displayed | medium |
| TC-003 | WF-003 | Open Cookies notice to view cookie usage information | User is unauthenticated and at the site's login page | 1. Click the 'Cookies notice' button | A dialog or panel opens displaying cookie usage information | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Submit with Username blank (required text) | User is unauthenticated and on the login page | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click the "Log in" button | Inline validation error appears on the Username field indicating it is required; the form does not submit; user remains on the login page and is not authenticated | high |
| TC-005 |  | Submit with Password blank (required password) | User is unauthenticated and on the login page | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the "Log in" button | Inline validation error appears on the Password field indicating it is required; the form does not submit; user remains on the login page and is not authenticated | high |
| TC-006 |  | Submit with both Username and Password empty | User is unauthenticated and on the login page | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the "Log in" button | Inline validation errors appear on both Username and Password fields indicating they are required; the form does not submit; user remains on the login page and is not authenticated | high |
| TC-007 | WF-001 | Submit with invalid credentials (wrong password) | User is unauthenticated and on the login page, A valid Username exists to test incorrect authentication | 1. Enter <valid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the "Log in" button | Inline authentication error appears on the form indicating sign-in failed; the Password field is cleared; the Username field retains its value; the form does not submit and the user remains unauthenticated (no redirect to Dashboard) | high |
| TC-008 |  | Click 'Lost password?' when the link is disabled on this test site | User is unauthenticated and on the login page, The 'Lost password?' link is marked disabled on this test site (per spec) | 1. Locate the 'Lost password?' link on the login form<br>2. Click the 'Lost password?' link | The 'Lost password?' link is disabled/unresponsive (not navigable); no password-reset page or flow opens; no navigation occurs and the user remains on the login page | medium |
| TC-009 |  | Attempt to access the login page / perform Log in while already authenticated (precondition violation) | User is already authenticated and has an active session | 1. With an authenticated session, navigate to the site's login page<br>2. Attempt to view or interact with the Login form or click the "Log in" button | Access to the login form is blocked for authenticated users: the system redirects the user away from the login page to the Dashboard (or the Login form is not visible); the Log in action is not available and no re-authentication occurs | high |
| TC-010 | WF-002 | Attempt 'Access as a guest' while authenticated (precondition violation) | User is already authenticated and has an active session | 1. With an authenticated session, navigate to the page containing the 'Access as a guest' control<br>2. Attempt to click the 'Access as a guest' button | The 'Access as a guest' action is not available to authenticated users: the button is either not visible or is disabled; clicking it does not grant limited unauthenticated browsing and the user's authenticated session remains active | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) | WF-001 | Username with leading and trailing whitespace causes credential mismatch | User is unauthenticated and at the site's login page, Valid credentials (username without extra whitespace and matching password) are available | 1. Enter a username with leading and trailing whitespace in the Username field<br>2. Enter the valid matching password in the Password field<br>3. Click the Log in button | Login is blocked / error shown: an inline error message is displayed; the Password field is cleared; the Username field retains the entered value including leading/trailing whitespace as shown on the page | medium |
| TC-012 (input_edge) | WF-001 | Username and Password containing emoji / non-ASCII characters | User is unauthenticated and at the site's login page, No account in the system contains the exact emoji/non-ASCII-padded credentials | 1. Enter a Username containing emoji and other non-ASCII characters in the Username field<br>2. Enter a Password containing emoji and other non-ASCII characters in the Password field<br>3. Click the Log in button | Login is blocked / error shown: an inline error message is displayed; the Password field is cleared; the Username field retains the entered emoji/non-ASCII characters as shown on the page | medium |
| TC-013 (interaction_edge) | WF-001 | Rapid double-submit of Log in button with valid credentials | User is unauthenticated and at the site's login page, Valid credentials are available for successful sign-in | 1. Enter the valid Username in the Username field<br>2. Enter the valid Password in the Password field<br>3. Click the Log in button twice in rapid succession | Form submits successfully; user is redirected to the Dashboard once; the second rapid click is ignored (no additional navigation or duplicate side effects occur) | medium |
| TC-014 (interaction_edge) |  | Clicking disabled 'Lost password?' link is ignored | User is unauthenticated and at the site's login page, 'Lost password?' link is disabled on this test site | 1. Click the 'Lost password?' link | Click is blocked / no navigation: no password reset UI or navigation appears; the page remains on the login screen and the 'Lost password?' control remains visually disabled | low |

---
