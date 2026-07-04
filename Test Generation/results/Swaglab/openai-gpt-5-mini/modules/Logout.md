# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Logout

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open hamburger menu and navigate to All Items | User logged in as <Authenticated User>, An active authenticated user session (logged in) on a protected page such as Product Inventory, Product Detail, Shopping Cart, or any Checkout step. | 1. Click the hamburger menu in the persistent header.<br>2. Click the 'All Items' link in the hamburger menu. | Navigates to the All Items page; the All Items page is displayed. | medium |
| TC-002 | WF-002 | Open hamburger menu and navigate to About page | User logged in as <Authenticated User>, An active authenticated user session (logged in) on a protected page such as Product Inventory, Product Detail, Shopping Cart, or any Checkout step. | 1. Click the hamburger menu in the persistent header.<br>2. Click the 'About' link in the hamburger menu. | Navigates to the About page; the About page content is displayed. | medium |
| TC-003 | WF-003 | Open hamburger menu and Logout (end session) returns to Login page | User logged in as <Authenticated User>, An active authenticated user session (logged in) on a protected page such as Product Inventory, Product Detail, Shopping Cart, or any Checkout step. | 1. Click the hamburger menu in the persistent header.<br>2. Click the 'Logout' link in the hamburger menu. | Ends the current authenticated session and navigates the user to the login page; protected pages are not accessible until re-authentication. Specifically, the Login page is displayed. | high |
| TC-004 | WF-004 | Open hamburger menu and trigger Reset App State | User logged in as <Authenticated User>, An active authenticated user session (logged in) on a protected page such as Product Inventory, Product Detail, Shopping Cart, or any Checkout step. | 1. Click the hamburger menu in the persistent header.<br>2. Click the 'Reset App State' button in the hamburger menu.<br>3. If a confirmation dialog appears, click Confirm on the Reset App State dialog. | Resets the application's local state; a visible confirmation (for example, a toast or in-app confirmation) is shown and the application's local UI state is cleared. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Logout option not available when user is unauthenticated | User is not authenticated (no active session) | 1. Navigate to the application's public entry page as an unauthenticated user<br>2. Click the hamburger menu in the header | The Logout link is not present in the hamburger menu; there is no visible control to end a session. The user cannot initiate a logout action because the Logout option is not shown. | high |
| TC-006 | WF-003 | Protected pages remain inaccessible after logging out | User has an active authenticated session | 1. Sign in using <valid user credentials><br>2. Click the hamburger menu in the header<br>3. Click the Logout link<br>4. After logout completes, attempt to navigate directly to the <Product Inventory URL> | After step 3 the app navigates to the login page and the authenticated session is terminated. On step 4 navigation to <Product Inventory URL> is blocked: the user is redirected to the login page and Product Inventory content is not displayed. The user remains unauthenticated until re-authentication. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-003 | Rapid / double-click Logout from hamburger menu | User is authenticated and on a protected page (e.g. Product Inventory) | 1. Click the persistent header hamburger menu<br>2. Click the 'Logout' menu item<br>3. Immediately (within a fraction of a second) click the 'Logout' menu item again (double-click / second click) | First logout click succeeds and navigates the user to the login page; the immediate second click is ignored (no second navigation or duplicate state change) and no UI error is shown. After this, attempts to access protected content require re-authentication. | medium |
| TC-008 (interaction_edge) | WF-003 | Use browser Back button after logout to attempt to return to protected page | User is authenticated and on a protected page, A protected page URL is present in the browser history | 1. Click the persistent header hamburger menu<br>2. Click the 'Logout' menu item<br>3. Once navigated to the login page, click the browser Back button | Attempt to return to the protected page using the Back button is blocked; the login page is displayed (or the user is redirected to the login page) and protected-page content is not shown. The user remains unauthenticated until they sign in again. | medium |
| TC-009 (state_edge) | WF-003 | Logout in one tab while a second tab has an open protected page; then interact in the second tab | User is authenticated, The same authenticated account has a protected page open in two separate browser tabs | 1. In Tab A, click the persistent header hamburger menu<br>2. In Tab A, click the 'Logout' menu item<br>3. Switch to Tab B (still showing a protected page without refresh)<br>4. In Tab B, click a protected-page action or refresh the page | Logout in Tab A succeeds and ends the session; the interaction or refresh in Tab B is blocked and presents the login page (or redirects to login) instead of allowing access to protected functionality. No protected actions succeed without re-authentication. | medium |
| TC-010 (interaction_edge) | WF-004 | Reset App State immediately before Logout | User is authenticated and on a protected page | 1. Click the persistent header hamburger menu<br>2. Click the 'Reset App State' button<br>3. After the reset completes, click the persistent header hamburger menu again<br>4. Click the 'Logout' menu item | Reset App State succeeds (local state is cleared) and subsequent Logout succeeds and navigates the user to the login page. After logout, protected pages are inaccessible until re-authentication and no residual protected state remains visible. | low |

---
