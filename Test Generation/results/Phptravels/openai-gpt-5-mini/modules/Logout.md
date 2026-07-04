# Test Cases — Phptravels

Generated: 2026-07-04T15:28:55.340647Z  
Model: openai/gpt-5-mini  

## Logout

Total: **11** (positive: 2, negative: 3, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Logout from Dashboard redirects to Home and ends session | User logged in as <Authenticated User>, User is on the <Dashboard> | 1. Click the Logout button in the account/navigation area | Terminate current session, clear sensitive session data, redirect the user to the Home page; subsequent attempts to access protected pages redirect to the Login page. | high |
| TC-002 | WF-001 | After Logout, direct navigation to a protected page redirects to Login | User logged in as <Authenticated User>, User is on any protected page or the <Dashboard> | 1. Click the Logout button in the account/navigation area<br>2. Enter <protected page URL> in the browser address bar and press Enter | The Login page is displayed and shows the <Login form>, indicating the user must re-authenticate before accessing protected pages. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user cannot see or use the Logout control (precondition not met) | User is not authenticated (no active session) | 1. Ensure the user is not authenticated (clear cookies / open a new browser session with no login).<br>2. Navigate to the site and open the main navigation Account/Login area where Logout would normally appear. | The Account/Login area does not display a 'Logout' control; the 'Login' / 'Sign in' control is visible instead. The user cannot initiate a logout because there is no active session (no session termination occurs). | high |
| TC-004 | WF-001 | Direct access to the logout endpoint while unauthenticated is blocked and redirects to Login | User is not authenticated (no active session) | 1. Ensure the user is not authenticated (no active session).<br>2. In the browser address bar, navigate directly to the logout endpoint URL: <logout URL>. | Browser is redirected to the Login page (URL becomes '<login URL>'); the Login form is displayed. The logout action does not proceed because there was no active session (no session clearing occurs). | high |
| TC-005 | WF-001 | After performing Logout, attempts to access a protected page are blocked (postcondition enforced) | User is authenticated with an active session | 1. Authenticate as a user to create an active session (log in).<br>2. Click the Logout button.<br>3. Wait for redirect to the Home page to complete.<br>4. In the browser address bar, navigate to a protected page URL: <protected page URL>. | Navigation to the protected page is blocked: browser is redirected to the Login page (URL becomes '<login URL>'); the protected content is not displayed and the Login form is visible. The user's session remains terminated (no access to protected areas). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click of Logout button (duplicate requests) | User is authenticated and is on a protected page or dashboard. | 1. Click the Logout button.<br>2. Immediately click the Logout button again (before the first redirect completes). | First logout action succeeds: user is redirected to the Home page and protected UI elements are removed. The second click sends a duplicate request that is ignored/handled idempotently and results in no server error or second session; the UI remains on Home page (no additional entity created). | medium |
| TC-007 (interaction_edge) | WF-001 | Browser back navigation after logout | User is authenticated and is on a protected page. | 1. Click the Logout button.<br>2. On the Home page after redirect, click the browser Back button to navigate to the previously viewed protected page. | Navigation to the protected page is blocked: the protected page request is intercepted and the user is redirected to the Login page (access is blocked). | medium |
| TC-008 (interaction_edge) | WF-001 | Open protected URL in a new tab after logging out in original tab | User is authenticated in Tab A and a protected resource URL is known. | 1. In Tab A, click the Logout button.<br>2. In a new browser tab (Tab B), navigate directly to a protected page URL and press Enter. | Access to the protected URL in Tab B is blocked: the browser is redirected to the Login page (access is blocked) rather than showing protected content. | medium |
| TC-009 (interaction_edge) | WF-001 | Perform an authenticated action from a stale (already-open) tab after logout in another tab | User is authenticated with Tab A and Tab B both open on protected pages (Tab B has the page loaded earlier). | 1. In Tab A, click the Logout button.<br>2. In Tab B (which still shows authenticated UI), click a button that triggers a protected action (e.g., Save or Update). | The action from Tab B is blocked: the server rejects the request as unauthorized and the client redirects the user to the Login page (protected action is not applied and access is blocked). | medium |
| TC-010 (state_edge) | WF-001 | Click Logout after the session has already expired (idle timeout) | User was previously authenticated but the session has expired due to idle timeout (user is still on a protected page but backend session is invalid). | 1. Click the Logout button. | Logout action succeeds (no server error): user is redirected to the Home page and no sensitive session data remains. Subsequent navigation to protected pages redirects to the Login page. | medium |
| TC-011 (state_edge) | WF-001 | In-flight authenticated request interrupted by Logout (race condition) | User is authenticated and initiates a long-running authenticated request from a protected page (e.g., a large save or upload). | 1. Start the long-running authenticated request (e.g., click Save that triggers a backend operation).<br>2. While the request is still in progress, click the Logout button.<br>3. Wait for the in-flight request to complete or return. | The in-flight request is blocked/treated as unauthorized once the session is terminated: the request is rejected (no protected update is applied) and the client redirects the user to the Login page or shows an authentication-required view (action is blocked). | medium |

---
