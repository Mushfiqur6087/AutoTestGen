# Test Cases — Moodleteacher

Generated: 2026-07-04T16:52:18.651847Z  
Model: openai/gpt-5-mini  

## Logout

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log out via top navigation user menu redirects to Login page | User is currently authenticated (logged in) with access to the top navigation user menu., User logged in as <authenticated user> | 1. Click the top navigation user initials to open the user menu.<br>2. Click 'Log out' in the user menu. | The Login page is displayed (login form is visible). The top navigation no longer shows the user initials dropdown, indicating the previous authenticated session has ended and protected areas require re-authentication. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to use Log out when not authenticated (precondition not met) | User is not authenticated (no active session) | 1. Launch the application in a fresh browser session where the user is not logged in<br>2. Navigate to the application home page<br>3. Click the top navigation user menu (right-side user initials) if present<br>4. Look for a 'Log out' / 'Log Out' link in the user menu | The 'Log out' link is not present in the top navigation user menu; there is no visible control to terminate a session and no logout action can be triggered while unauthenticated. The user remains on the public page and is not redirected. | high |
| TC-003 | WF-001 | Verify protected pages are blocked after logging out (requires re-authentication) | User is authenticated and has access to the top navigation user menu | 1. Authenticate as a valid user and confirm the top navigation user menu is available<br>2. Open the top navigation user menu<br>3. Click the 'Log out' link<br>4. After logout completes, attempt to navigate to a protected page (for example, click the Dashboard link or enter a protected page URL) without re-authenticating | After clicking 'Log out' the application redirects to the Login page. When attempting to access a protected page without re-authenticating, access is blocked: the protected content is not displayed and the user is kept on or redirected to the Login page until valid credentials are provided. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click on Log out link | User is authenticated and a protected page is visible, Top navigation user menu (user initials) is present | 1. Click the user initials in the top navigation to open the user menu<br>2. Click the 'Log out' link<br>3. Immediately click the 'Log out' link a second time | Logout succeeds; after the first click the Login page is displayed (Login form present). The immediate second click has no additional effect — the Login page remains visible and no protected content is shown. | medium |
| TC-005 (interaction_edge) | WF-001 | Press browser Back after logging out | User is authenticated and a protected page is visible, Top navigation user menu (user initials) is present | 1. Click the user initials in the top navigation to open the user menu<br>2. Click the 'Log out' link<br>3. After the app redirects, press the browser Back button | Logout succeeds; the Login page is displayed (Login form present) after logout and remains visible after pressing Back. Protected pages are not accessible from the Back navigation (user remains logged out). | medium |
| TC-006 (state_edge) | WF-001 | Navigate directly to a protected URL after logout | User is authenticated and a protected page is visible, Top navigation user menu (user initials) is present | 1. Click the user initials in the top navigation to open the user menu<br>2. Click the 'Log out' link<br>3. In the browser address bar, enter the URL of a known protected page (e.g., Dashboard) and press Enter | Attempted navigation to the protected URL is blocked; the Login page is shown (Login form present) and the protected page content is not displayed. | medium |

---
