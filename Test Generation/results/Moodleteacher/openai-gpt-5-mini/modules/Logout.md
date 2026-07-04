# Test Cases — Moodleteacher

Generated: 2026-07-04T15:16:12.934753Z  
Model: openai/gpt-5-mini  

## Logout

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log out via user menu redirects to Login page | User is currently authenticated (logged in) with an active session and the user menu is available., User logged in as <User> | 1. Click the user initials dropdown in the top navigation to open the user menu<br>2. Click the 'Log out' button in the user menu | Login page is displayed; Terminates the current authenticated session and redirects the user to the login page; access to protected pages requires re-authentication. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user cannot see or trigger Log out from the user menu | User is not authenticated (no active session); application opened in a fresh browser session | 1. Start a fresh browser session where no user is logged in<br>2. Inspect the top-right corner of the global navigation where the user initials dropdown normally appears<br>3. Attempt to open the user initials dropdown / user menu | The user initials dropdown / user menu is not present and therefore the 'Log out' option is not visible; the UI does not offer a Log out control to an unauthenticated user (user remains unauthenticated and on the login or public landing view) | high |
| TC-003 | WF-001 | Direct navigation to logout endpoint while not authenticated is blocked and redirects to login | User is not authenticated (no active session); application opened in a fresh browser session | 1. Start a fresh browser session where no user is logged in<br>2. In the browser address bar, navigate to <logout URL> (the application endpoint/route used to perform logout)<br>3. Observe the resulting page | Browser is redirected to the Login page (login view is displayed); the application does not perform a logout operation because no session existed, and the user remains unauthenticated (no protected page is shown) | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Log out button | User is authenticated and the user menu is available | 1. Click the user initials to open the user menu<br>2. Rapidly double-click the "Log out" button (two clicks in quick succession) | Single logout action succeeds; the user is redirected to the login page, the user menu no longer shows authenticated options, and no duplicate-logout error message or additional redirects are shown. Protected pages require re-authentication. | medium |
| TC-005 (interaction_edge) | WF-001 | Press browser Back immediately after logout | User is authenticated and the user menu is available | 1. Click the user initials to open the user menu<br>2. Click the "Log out" button<br>3. After the app redirects to the login page, press the browser Back button | Back navigation is blocked; the login page remains visible (or the app immediately redirects back to the login page) and previously accessible protected page content is not presented. Any attempt to view protected pages requires re-authentication. | medium |
| TC-006 (state_edge) | WF-001 | Logout in one tab then refresh a protected page in another tab | User is authenticated with two browser tabs open: Tab A (any app page) and Tab B (a protected page loaded) | 1. In Tab A, click the user initials to open the user menu<br>2. In Tab A, click the "Log out" button<br>3. In Tab B, click the browser Refresh button while the user is logged out | Refresh is blocked: the protected page reload results in a redirect to the login page (user must re-authenticate); cached protected content is not left accessible in Tab B. | medium |

---
