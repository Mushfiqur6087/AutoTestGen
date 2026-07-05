# Test Cases — Moodleteacher

Generated: 2026-07-04T16:52:18.651847Z  
Model: openai/gpt-5-mini  

## Login

Total: **15** (positive: 4, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials redirects to Dashboard for teacher | User is not authenticated (logged out) and has access to the Login page | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the 'Log in' button | The Dashboard page is displayed; the top navigation bar and course navigation are visible, showing the user has been authenticated and landed on the Dashboard | high |
| TC-002 | WF-002 | Access as a guest redirects to Dashboard in guest mode | User is not authenticated (logged out) and has access to the Login page | 1. Click the 'Access as a guest' button | The Dashboard page is displayed; the top navigation bar is visible and the UI shows an indicator that the session is unauthenticated guest access | medium |
| TC-003 | WF-003 | Open Cookies notice displays cookie usage information | User is not authenticated (logged out) and has access to the Login page | 1. Click the 'Cookies notice' button | A Cookies information dialog/panel opens displaying cookie usage information | low |
| TC-004 |  | Disabled 'Lost password?' link is visible but not clickable on test site | User is not authenticated (logged out) and has access to the Login page, The 'Lost password?' link is disabled on this test site | 1. Attempt to click the 'Lost password?' link | The 'Lost password?' link remains visually disabled and no navigation or dialog is opened | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Username blank and submit (required text field representative) | User is on the Login page, User is logged out | 1. Ensure the User_Name field is empty (leave it blank)<br>2. Enter <valid password> in the Password field<br>3. Click the 'Log in' button | Inline error message "Invalid or empty credentials" is displayed; the form is not submitted; Password field is cleared; User_Name remains blank (no value retained); the user stays on the Login page | high |
| TC-006 |  | Leave Password blank and submit (password field representative) | User is on the Login page, User is logged out | 1. Enter <valid username> in the User_Name field<br>2. Leave the Password field empty<br>3. Click the 'Log in' button | Inline error message "Invalid or empty credentials" is displayed; the form is not submitted; Password field is cleared (remains empty); User_Name value is retained on the form; the user stays on the Login page | high |
| TC-007 |  | Submit with all required fields empty | User is on the Login page, User is logged out | 1. Ensure the User_Name field is empty<br>2. Ensure the Password field is empty<br>3. Click the 'Log in' button | Inline error message "Invalid or empty credentials" is displayed; the form is not submitted; Password field is cleared (remains empty); User_Name remains blank; the user stays on the Login page | high |
| TC-008 | WF-001 | Submit invalid credentials (authentication failure) | User is on the Login page, User is logged out | 1. Enter <existing username> in the User_Name field<br>2. Enter <incorrect password> in the Password field<br>3. Click the 'Log in' button | Inline error message "Invalid or empty credentials" is displayed; the form is not submitted; Password field is cleared; User_Name remains populated with the entered username; the user stays on the Login page | high |
| TC-009 |  | Click 'Lost password?' link when it is disabled on this site | User is on the Login page, Test site has the Lost password? link disabled | 1. Observe the 'Lost password?' link on the page<br>2. Attempt to click the 'Lost password?' link | The 'Lost password?' link is displayed as disabled or non-interactive and is not clickable; clicking it has no effect and there is no navigation to a password-recovery page | medium |
| TC-010 | WF-002 | Attempt 'Access as a guest' while already authenticated (precondition failure) | User is authenticated (logged in) and on the Dashboard | 1. While authenticated as <valid user>, navigate to the Login page<br>2. Locate the 'Access as a guest' button<br>3. Attempt to click the 'Access as a guest' button | The 'Access as a guest' action is not allowed when the user is authenticated: the button is either not visible or is disabled/non-interactive; clicking it does not start an unauthenticated session and no navigation to a guest Dashboard occurs; user remains authenticated | high |
| TC-011 |  | Attempt to use Log in action while already authenticated (precondition failure) | User is authenticated (logged in) and on the Dashboard | 1. While authenticated as <valid user>, navigate to the Login page<br>2. Attempt to interact with the 'Log in' button or submit the login form | The 'Log in' action is not allowed when the user is already authenticated: the Log in button is either not visible or is disabled/non-interactive; attempting to submit does not create a new login session or switch to an unauthenticated/guest session; user remains authenticated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) | WF-001 | Very long username is preserved after failed login | User is logged out and on the Login page | 1. Enter a very long string (200+ characters) in the User_Name field<br>2. Enter <an incorrect password> in the Password field<br>3. Click Log in | Inline error is shown; Password field is cleared; User_Name input retains the very long string exactly as entered (visible in the username input) — the login attempt is blocked with the inline error | medium |
| TC-013 (input_edge) | WF-001 | Username with emoji and non-Latin Unicode characters is retained on failure | User is logged out and on the Login page | 1. Enter a string containing emoji and non-Latin Unicode characters in the User_Name field<br>2. Enter <an incorrect password> in the Password field<br>3. Click Log in | Inline error is shown; Password field is cleared; User_Name input retains the exact Unicode/emoji characters as entered (visible in the username input) — the login attempt is blocked with the inline error | medium |
| TC-014 (state_edge) | WF-001 | Password cleared and username retained when credentials are invalid | User is logged out and on the Login page | 1. Enter any value in the User_Name field<br>2. Enter any incorrect value in the Password field<br>3. Click Log in | Inline error displays the configured message "Invalid or empty credentials"; Password field is cleared; User_Name field remains populated with the value entered (the login attempt is blocked with the inline error) | medium |
| TC-015 (interaction_edge) |  | Disabled 'Lost password?' link is non-interactive | User is logged out and on the Login page | 1. Click the 'Lost password?' link | No navigation or modal opens; the 'Lost password?' link remains on the page and the login form remains visible (click produces no effect) | low |

---
