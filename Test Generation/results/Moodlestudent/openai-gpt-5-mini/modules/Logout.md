# Test Cases — Moodlestudent

Generated: 2026-07-04T16:43:47.211887Z  
Model: openai/gpt-5-mini  

## Logout

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log out via user menu redirects to the Login page | User logged in as <authenticated user>, An active authenticated user session (user is logged in and has access to protected pages). | 1. From any protected page, click the initials icon in the top navigation bar to open the user menu dropdown.<br>2. Click the 'Log out' button in the user menu. | The Login page is displayed showing the credential entry form (fields to enter username/email and password) and the primary authentication button; authenticated-only UI elements such as the user initials in the top navigation are no longer visible. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Unauthenticated user cannot see or invoke Log out from User Menu | User is not authenticated (no active session) | 1. Open the application main page as a user with no active session<br>2. Inspect the top navigation bar (right side) for the initials icon / user menu<br>3. Attempt to open the user menu | Initials icon / User menu is not present in the top navigation; the 'Log out' option is not visible or clickable. No logout action can be performed from the UI while unauthenticated. | high |
| TC-003 | WF-001 | Direct navigation to Logout endpoint while unauthenticated is blocked/redirected | User is not authenticated (no active session) | 1. Ensure there is no active authenticated session<br>2. In the browser address bar navigate directly to the application's Logout endpoint/route (the URL or route that triggers Log out)<br>3. Observe the resulting page shown to the user | Navigation to the Logout endpoint does not perform a logout (no active session to terminate) and the user is presented with the login page / is redirected to the login screen; no logout confirmation or protected content is shown. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Log out button | User is logged in and currently viewing a protected page | 1. Click the initials icon in the top navigation bar to open the user menu dropdown<br>2. Click the Log out button<br>3. Immediately click the Log out button again (second click occurs before the UI redirect completes) | The first click terminates the session and redirects to the login page; the second rapid click does not produce an error and is ignored. Logout succeeds and the login page is visible. | medium |
| TC-005 (interaction_edge) | WF-001 | Click Log out then immediately navigate to a protected page via top navigation | User is logged in and currently viewing a protected page | 1. Click the initials icon in the top navigation bar to open the user menu dropdown<br>2. Click the Log out button<br>3. Immediately (before the login page finishes rendering) click a top-navigation link that points to another protected page | The attempt to view the protected page after logout is blocked; the login page is shown. Access is blocked and a re-authentication prompt (login page) is visible. | medium |
| TC-006 (interaction_edge) | WF-001 | Use browser Back button immediately after logout | User is logged in and currently viewing a protected page | 1. Click the initials icon in the top navigation bar to open the user menu dropdown<br>2. Click the Log out button<br>3. After the app redirects to the login page, press the browser Back button once | Using the browser Back button does not reveal protected content; navigation is blocked and the login page remains visible (protected pages are not displayed). Access is blocked. | low |
| TC-007 (data_edge) | WF-001 | Manually enter a protected page URL after logout | User is logged in and currently viewing a protected page | 1. Click the initials icon in the top navigation bar to open the user menu dropdown<br>2. Click the Log out button<br>3. After being redirected to the login page, type a known protected page URL into the browser address bar and press Enter | Direct navigation to the protected URL is blocked; the login page is shown and the protected page content is not displayed. Access is blocked. | medium |

---
