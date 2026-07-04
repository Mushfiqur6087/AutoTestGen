# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Reset App State

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Activate Reset App State from hamburger menu clears cart and resets UI state | User is logged in as <User>, User is logged in with an active session and the application has mutable state (e.g., items added to the cart or changed add/remove button states)., Persistent header with hamburger menu is visible on a post-login page (for example, Product Inventory) | 1. Click the hamburger menu in the persistent header to open the post-login menu<br>2. Click the 'Reset App State' menu item<br>3. Click the header Cart icon to open the Cart view | Clears the shopping cart and resets in-app UI state (for example, cart badge and add/remove button states) without logging the user out. Specifically: the header cart badge no longer displays an item count (cart badge cleared); the Cart view shows the empty-state UI indicating no items are present; product tiles that were previously modified now show the default add-button state (add control visible and enabled); the user remains logged in (persistent header and user avatar remain visible). | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Unauthenticated user attempts Reset App State from hamburger menu | User is not logged in (no active session) | 1. Navigate to the application landing page (not signed in)<br>2. Open the persistent header hamburger menu<br>3. Attempt to click the 'Reset App State' menu item (if visible) or select it | User is redirected to the Login page (login form is displayed); the Reset App State action is not performed and the shopping cart and UI state remain unchanged (no cart cleared, no add/remove button states reset). | high |
| TC-003 | WF-001 | Logged-in user with no mutable state attempts Reset App State (precondition: mutable state not met) | User is logged in with an active session, Application has no mutable state (cart is empty and add/remove button states are at defaults) | 1. Sign in and establish an active session<br>2. Verify the shopping cart is empty and item buttons are in default state (no items added)<br>3. Open the persistent header hamburger menu<br>4. Look for the 'Reset App State' menu item | The 'Reset App State' menu item is not visible in the hamburger menu (or is disabled); no reset occurs and the shopping cart and UI remain unchanged. The workflow does not execute because the required precondition (application has mutable state) is not met. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (state_edge) | WF-001 | Activate Reset when cart contains items — verify full state reset without logout | User is logged in with an active session, Shopping cart contains one or more items, Product list contains at least one item with add/remove state changed from default (e.g., showing Remove) | 1. Open the hamburger menu in the persistent header<br>2. Click the Reset App State menu item | Reset succeeds; shopping cart item list is empty (cart shows no items), cart badge is cleared/hidden or shows zero, product list add/remove button states are reverted to default (e.g., 'Add' state), and the user remains logged in (session persists; user is not logged out and logout option remains available). | medium |
| TC-005 (data_edge) | WF-001 | Activate Reset when cart is already empty — verify no-op behavior and no error | User is logged in with an active session, Shopping cart is already empty and cart badge is absent or zero | 1. Open the hamburger menu in the persistent header<br>2. Click the Reset App State menu item | Activation succeeds (no-op); cart remains empty and cart badge remains cleared/hidden or zero, no error is shown, product list states remain default, and the user remains logged in. | low |
| TC-006 (interaction_edge) | WF-001 | Rapid double-activation of Reset — verify idempotence and that duplicate activations are blocked/ignored | User is logged in with an active session, Shopping cart contains one or more items | 1. Open the hamburger menu in the persistent header<br>2. Click the Reset App State menu item<br>3. Immediately click the Reset App State menu item a second time (before the UI visibly finishes the first reset) | First activation succeeds and clears the cart and resets UI state; the second immediate activation is blocked/ignored (no additional state change occurs), there is no application crash, no duplicate side-effects are observed, and the user remains logged in. | medium |
| TC-007 (state_edge) | WF-001 | Activate Reset during an in-progress checkout step — observe how checkout state is affected | User is logged in with an active session, User is on a checkout page (mid-checkout) with items in the order summary | 1. While on the checkout page, open the hamburger menu in the persistent header<br>2. Click the Reset App State menu item | Reset succeeds; shopping cart and order summary are cleared (checkout page reflects an empty cart / no items in order summary), checkout cannot proceed with the previous items (visible indication that the order summary is empty), and the user remains logged in (no logout occurs). | medium |

---
