# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Logout

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Logout via header menu returns user to the sign-in page | User logged in as <Authenticated User>, User is currently authenticated and on a protected page (e.g., Product Inventory, Product Detail, Shopping Cart, or Checkout). | 1. Click the header hamburger/menu button to open the persistent header menu<br>2. Click the 'Logout' button/item in the header menu | The Sign-in page is displayed; the sign-in form with Email and Password fields and a 'Sign In' button is visible, and the previous protected page content is no longer visible | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user cannot access Logout; protected page access is blocked | User is not authenticated | 1. In a new browser session, navigate to a protected page: <Product Inventory page URL><br>2. Observe the page that loads<br>3. Open the header / hamburger menu | Navigation to <Product Inventory page> does not reveal protected content and the application displays or redirects to the sign-in page; the header/hamburger menu does not contain a Logout button (Logout is not available to unauthenticated users). | high |
| TC-003 | WF-001 | Logout is not available when authenticated user is on a public (non-protected) page; precondition 'on a protected page' not met | User is authenticated and on a public/non-protected page (e.g., <About page>) | 1. Log in as <valid user><br>2. Navigate to a public page: <About page><br>3. Open the header / hamburger menu<br>4. Attempt to click a Logout button if it is present | Header/hamburger menu does not show a Logout button while on the public page (precondition 'on a protected page' not met). If a Logout control is present despite the precondition, clicking it does not terminate the session or redirect the user to the sign-in page; the user remains on the public page and the session remains active. | high |
| TC-004 | WF-001 | Logout control must not be usable when user is already unauthenticated (stale UI protection) | User session is not active (user is already logged out and on the sign-in page) | 1. Ensure the application is on the sign-in page and the user is logged out<br>2. Open the header / hamburger menu if visible<br>3. If a Logout button is visible, click the Logout button | Logout button should not be present on the sign-in page. If a Logout button is visible despite the user being unauthenticated, clicking it does not change application state: the app remains on the sign-in page and no protected content becomes accessible (no session termination/transition occurs because no session exists). | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Logout button | User is authenticated and on a protected page | 1. Click the header hamburger menu<br>2. Click the Logout button<br>3. Immediately click the Logout button again (within a short interval) | Logout succeeds; the sign-in page with visible login form is displayed once, and the second click is ignored (no additional navigation or duplicate session changes are visible). | medium |
| TC-006 (interaction_edge) | WF-001 | Browser Back after successful logout | User is authenticated and on a protected page | 1. Click the header hamburger menu<br>2. Click the Logout button<br>3. Wait until the sign-in page with visible login form is displayed<br>4. Press the browser Back button | Access to the previously viewed protected page is blocked; the browser remains on or is redirected back to the sign-in page with the login form visible (protected page content is not shown). | medium |
| TC-007 (state_edge) | WF-001 | Direct navigation to a protected URL after logout | User is authenticated and on a protected page | 1. Click the header hamburger menu<br>2. Click the Logout button<br>3. Wait until the sign-in page with visible login form is displayed<br>4. Enter the URL of a protected page (e.g., product detail or cart) into the browser address bar and press Enter | Navigation to the protected URL is blocked; the browser displays the sign-in page with the login form visible instead of the protected page. | medium |

---
