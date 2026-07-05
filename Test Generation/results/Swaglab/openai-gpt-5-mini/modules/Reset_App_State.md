# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Reset App State

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Invoke Reset App State from hamburger menu when app has non-default state | User logged in as <User>, User is signed in with an active session and the application has a non-default state (e.g., items in cart or modified add/remove button states). | 1. Open the hamburger menu<br>2. Click the 'Reset App State' menu item | The cart badge no longer displays an item count (badge hidden or shows 0); the Cart page displays an empty-cart state with no items listed when opened; product tiles in the All Items list and product detail screens show the 'Add' button (not 'Remove') for items that had been added previously; the hamburger menu still shows the 'Logout' item indicating the user remains signed in. | high |
| TC-002 | WF-002 | Open All Items from hamburger menu | User logged in as <User> | 1. Open the hamburger menu<br>2. Click the 'All Items' menu item | The All Items view opens; the page heading 'All Items' is visible and a list of product tiles is displayed. | medium |
| TC-003 | WF-003 | Open About page from hamburger menu | User logged in as <User> | 1. Open the hamburger menu<br>2. Click the 'About' menu item | The About page opens and the About page heading or content is visible on screen. | low |
| TC-004 | WF-004 | Logout using hamburger menu | User logged in as <User> | 1. Open the hamburger menu<br>2. Click the 'Logout' menu item | The application displays the signed-out/authentication screen (sign-in form or 'Sign In' button is visible) indicating the user is logged out; the authenticated menu items (e.g., 'Logout') are no longer available without signing back in. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Reset App State menu item not available to unauthenticated user | User is not signed in (app at signed-out / initial screen) | 1. Launch the app to the signed-out / initial screen as <unauthenticated user><br>2. Tap the hamburger menu icon to open the menu | 'Reset App State' menu item is not visible in the hamburger menu; there is no visible control to invoke Reset App State while not signed in | high |
| TC-006 | WF-001 | Attempt Reset App State when application is already in default state (precondition not met) | User is signed in with an active session, Application is in the default state: <cart empty> and <default add/remove button and cart badge states> | 1. Sign in as <signed-in user> and confirm active session<br>2. Ensure the shopping cart is empty and UI controls are in their default states<br>3. Open the hamburger menu<br>4. Tap the 'Reset App State' menu item | 'Reset App State' action is blocked: the control is shown but inactive for default-state scenarios (visibly disabled) or tapping it produces an inline indication that nothing will be changed; the shopping cart remains empty and UI states remain unchanged; the user remains signed in (no sign-out occurs) | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) |  | Invoke Reset App State when cart is already empty (idempotence) | User is signed in and hamburger menu is visible (Visible_When: user is signed in)., Application is in default state: shopping cart is empty and add/remove buttons are in their default (pre-add) state. | 1. Open the hamburger menu.<br>2. Click the 'Reset App State' menu item. | The Reset App State action succeeds; the cart remains empty (empty-cart UI still visible), cart badge remains absent, UI stays signed in (Logout remains visible in the hamburger menu). No error is shown. | low |
| TC-008 (interaction_edge) | WF-001 | Rapid double-invoke of Reset App State when cart contains items | User is signed in and hamburger menu is visible (Visible_When: user is signed in)., Application is in non-default state: shopping cart contains at least one item. | 1. Open the hamburger menu.<br>2. Click the 'Reset App State' menu item.<br>3. Immediately click the 'Reset App State' menu item again before UI completes the first action. | Reset App State succeeds; the first click clears the cart and removes the cart badge. The immediate second click is ignored (no additional visible changes or duplicate confirmations) and does not produce an error. User remains signed in. | medium |
| TC-009 (data_edge) | WF-001 | Invoke Reset App State while on Checkout page with items in cart | User is signed in and hamburger menu is visible (Visible_When: user is signed in)., User is currently on the Checkout page and the cart contains items (non-default state). | 1. From the Checkout page, open the hamburger menu.<br>2. Click the 'Reset App State' menu item. | Reset App State succeeds; the Checkout page updates to reflect an empty cart (line items removed or empty-cart UI visible), the cart badge is cleared, and the user remains signed in. No error is shown. | medium |
| TC-010 (state_edge) | WF-001 | Invoke Reset App State to restore product-detail add/remove button to default | User is signed in and hamburger menu is visible (Visible_When: user is signed in)., A product detail page currently shows a non-default add/remove state indicating the product is in the cart (non-default UI state). | 1. Open the hamburger menu while on or after visiting the product detail page.<br>2. Click the 'Reset App State' menu item.<br>3. Navigate to (or refresh) the same product detail page for that product. | Reset App State succeeds; the product detail page shows the default pre-added button state (add option available), the cart badge is cleared, and the user remains signed in. No error is shown. | low |

---
