# Test Cases — Moodlestudent

Generated: 2026-07-04T15:14:26.541109Z  
Model: openai/gpt-5-mini  

## Logout

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select 'Log out' from user menu redirects to Login page | User logged in as <Authenticated user>, User is currently authenticated (active session) and has access to the top navigation user menu. | 1. Click the <User menu> (user avatar) in the top navigation to open the user menu<br>2. Click the 'Log out' link in the user menu | The Login page is displayed with the login form visible; the current authenticated session has been terminated and the user was redirected to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user navigates directly to the logout endpoint | User is not authenticated (no active session) | 1. Ensure there is no active session (log out or open a new private browser session)<br>2. In the browser address bar navigate to <logout endpoint URL> (the URL that performs the Log out action) | Browser is redirected to the <login page URL>; the Login page with the sign-in form is displayed (e.g. Username/Email and Password fields visible). No 'session terminated' success flow occurs and no authenticated session exists after navigation. | high |
| TC-003 |  | Unauthenticated visitor does not see 'Log out' in the user menu | User is not authenticated (no active session) | 1. Ensure there is no active session (log out or open a new private browser session)<br>2. Navigate to a page that shows the top navigation bar (e.g. Home)<br>3. Open the top navigation user menu / user avatar dropdown | The 'Log out' / 'Log out' menu item is not visible in the user menu. Instead the user menu shows options to sign in or does not display user-specific menu items. No logout action is available to unauthenticated users. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Log out link | User is authenticated and on any protected page, User menu is accessible in the top navigation | 1. Click the user menu in the top navigation<br>2. Click the 'Log out' link (first click)<br>3. Immediately click the 'Log out' link again (second click) before the redirect completes | Logout succeeds: the application processes a single logout and the user is redirected to the login page once; no error message is shown and no duplicate redirects or visible side-effects occur. | medium |
| TC-005 (state_edge) | WF-001 | Close tab immediately after clicking Log out (server-side logout completion validation) | User is authenticated and on any protected page, User menu is accessible in the top navigation | 1. Click the user menu in the top navigation<br>2. Click the 'Log out' link<br>3. Immediately close the browser tab before the login page loads<br>4. Open a new browser tab and navigate to a known protected page URL | Logout succeeds server-side: access to the protected page is blocked and the new tab is redirected to the login page (no authenticated content is shown). | medium |
| TC-006 (interaction_edge) | WF-001 | Use browser Back after successful logout to attempt returning to protected page | User is authenticated and on a protected page, User menu is accessible in the top navigation | 1. Click the user menu in the top navigation<br>2. Click the 'Log out' link<br>3. Wait for redirect to the login page to complete<br>4. Press the browser Back button once | Navigation back to protected content is blocked: the browser should display the login page (or re-redirect to it) and no protected content is visible — logout succeeds and protected pages are not accessible from back navigation. | low |
| TC-007 (state_edge) | WF-001 | Log out in one tab then perform an authenticated action in another tab that was left open | User is authenticated and has two browser tabs open showing protected pages, User menu is accessible in the top navigation on both tabs | 1. In Tab A, click the user menu in the top navigation<br>2. In Tab A, click the 'Log out' link and wait for redirect to the login page<br>3. Switch to Tab B (left open, showing a protected page) and click a link or button that requires authentication (for example, navigate to a protected section)<br>4. Observe the behavior in Tab B | Authenticated actions in Tab B are blocked after logout: the attempted action is redirected to the login page or otherwise prevented from showing protected content — logout succeeds server-side and other open tabs lose authenticated access. | medium |

---
