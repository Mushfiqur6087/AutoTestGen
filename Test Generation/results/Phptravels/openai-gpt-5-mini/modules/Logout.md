# Test Cases — Phptravels

Generated: 2026-07-04T16:37:37.073226Z  
Model: openai/gpt-5-mini  

## Logout

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User clicks Logout from top navigation and is returned to Home page | User logged in as <authenticated user>, An active authenticated user session exists (user is logged in). | 1. From any page, click the Account/Login area in the top navigation to reveal account actions<br>2. Click the 'Logout' button | The Home page is displayed; the top navigation shows a 'Login' entry indicating no user is signed in | high |
| TC-002 | WF-001 | After logout, attempting to open a protected page redirects to the Login page | User logged in as <authenticated user>, An active authenticated user session exists (user is logged in). | 1. From any page, click the Account/Login area in the top navigation to reveal account actions<br>2. Click the 'Logout' button<br>3. In the browser address bar, enter the URL of <protected page> (a page that requires authentication) and navigate to it | The Login page is displayed with the sign-in form visible | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt Logout when no active authenticated session exists | No active authenticated user session (user is not logged in) | 1. Open the application in a new browser session where the user is not logged in<br>2. Observe the top navigation Account/Login area for a Logout control<br>3. Directly navigate the browser to the Logout endpoint (<Logout endpoint>) and press Enter | Top navigation Account/Login area does not display a Logout button; navigating to the Logout endpoint redirects the browser to the Login page; no authenticated session is created. | high |
| TC-004 | WF-001 | After logging out, accessing a protected page must be blocked | An active authenticated user session exists (user is logged in) | 1. Ensure the user is authenticated (active session exists)<br>2. Click the Logout button in the Account area<br>3. After the application redirects to the Home page, enter the URL of a protected page (<protected page URL>) and press Enter | Browser redirects to the Login page when attempting to access the protected page; the protected page content is not displayed and the user remains unauthenticated. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Logout button | User is authenticated and on a page containing the Logout button | 1. Ensure the page with the Logout button is visible and the user is authenticated<br>2. Click the Logout button<br>3. Immediately click the Logout button again (second click within a fraction of a second) | succeeds; the first click initiates logout and the user is redirected to the Home page (Home page visible). The second click has no visible effect (no duplicate redirect, no error message shown). | medium |
| TC-006 (state_edge) | WF-001 | Click Logout while browser is offline / network unavailable | User is authenticated and on a page containing the Logout button, Browser network state set to offline (no network connectivity) before clicking Logout | 1. Ensure the page with the Logout button is visible and the user is authenticated<br>2. Toggle the browser to offline / disable network connectivity<br>3. Click the Logout button | is blocked; an inline error message is shown indicating logout failed due to network/unavailability and the user remains on the current page (protected UI still visible). | medium |
| TC-007 (interaction_edge) | WF-001 | Press browser Back immediately after successful logout | User is authenticated and on a page containing the Logout button | 1. Click the Logout button<br>2. Wait for redirect to the Home page and confirm the Home page is visible<br>3. Press the browser Back button once | is blocked; the Back navigation does not reveal protected content — the browser shows the Login page (Login page visible) instead of the previously protected page. | medium |
| TC-008 (data_edge) | WF-001 | Navigate directly to a protected URL immediately after logout | User is authenticated and on a page containing the Logout button | 1. Click the Logout button<br>2. Wait for redirect to the Home page and confirm the Home page is visible<br>3. Enter a known protected page URL into the browser address bar and navigate to it | is blocked; navigation to the protected URL is redirected to the Login page and the Login page is visible (protected content is not displayed). | medium |

---
