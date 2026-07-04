# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Checkout - Confirmation

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Confirmation page shows an order success message after submission | User logged in as <User>, User has completed the Checkout - Overview step with an order submitted. | 1. Navigate to the Checkout - Confirmation page<br>2. Observe the page content for the order confirmation message | A success message is visible on the Checkout - Confirmation page indicating the order was received (for example: 'Thank you for your order!') | medium |
| TC-002 | WF-001 | Click Back Home returns user to Product Inventory and clears the cart | User logged in as <User>, User has completed the Checkout - Overview step with an order submitted. | 1. Navigate to the Checkout - Confirmation page<br>2. Click the 'Back Home' button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user cannot access Confirmation page | User is not logged in, User has items in cart (optional) but has not authenticated in this session | 1. Ensure the user is logged out<br>2. In the browser, navigate to <confirmation page URL> (Checkout - Confirmation)<br>3. Observe the browser behavior and displayed page | Browser redirects to <login page>; the Confirmation page does not render (no success message like 'Thank you for your order!' is shown) and the Back Home button is not available. The cart state remains unchanged (items remain in cart). | high |
| TC-004 | WF-001 | Logged-in user without a submitted order cannot use Back Home from Confirmation | User is logged in, User has NOT completed Checkout - Overview and has NOT submitted an order (no completed order exists) | 1. Log in as <user account> who has items in cart but has not completed Checkout - Overview<br>2. Navigate to <confirmation page URL> (attempt to open Confirmation page directly)<br>3. Check whether the Confirmation success message and Back Home button are visible<br>4. If Back Home is visible, click the Back Home button | Access is blocked: the Confirmation success message is not shown and the Back Home button is either not visible or disabled. If navigation is attempted, the user is redirected to <shopping cart page> (or the appropriate checkout step) instead of seeing Confirmation. The cart remains unchanged (items still present); no confirmation state is shown. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Back Home is idempotent and clears cart once | User is logged in and has completed the Checkout - Overview step with an order submitted, User is on the Checkout - Confirmation page showing the success message and Back Home button | 1. Click the Back Home button<br>2. Immediately click the Back Home button a second time (within <1 second) without waiting for navigation to complete<br>3. Observe the Product Inventory page and the cart item count indicator | First click succeeds: user is navigated to Product Inventory and the cart item count indicator displays 0. The second click is ignored (no error shown, no duplicate navigation and no duplicate order creation). | medium |
| TC-006 (interaction_edge) | WF-001 | Back Home clicked while network is offline shows a visible error and does not clear the cart | User is logged in and has completed the Checkout - Overview step with an order submitted, User is on the Checkout - Confirmation page showing the success message and Back Home button, User can toggle the client device network connectivity (simulate offline) | 1. Disable network connectivity on the client device (go offline)<br>2. Click the Back Home button<br>3. Observe the Confirmation page UI and the cart item count indicator | Action is blocked / error shown: an inline error message is displayed indicating the return failed due to network/connectivity issues, the user remains on the Confirmation page, and the cart remains populated (cart indicator is not cleared). | medium |
| TC-007 (state_edge) | WF-001 | Use browser Back after Back Home navigation — cart remains cleared and re-invoking Back Home is safe | User is logged in and has completed the Checkout - Overview step with an order submitted, User is on the Checkout - Confirmation page showing the success message and Back Home button | 1. Click the Back Home button<br>2. Observe the Product Inventory page and the cart item count indicator<br>3. Press the browser Back button once<br>4. Observe the Confirmation page and the cart item count indicator<br>5. Click the Back Home button again from the Confirmation page | First Back Home click succeeds: user is navigated to Product Inventory and cart indicator displays 0. Pressing browser Back returns to the Confirmation page (may be cached) but the cart indicator remains 0 (cart not resurrected). Re-clicking Back Home succeeds and the cart remains 0; no duplicate orders are created. | medium |
| TC-008 (interaction_edge) | WF-001 | Back Home invoked from multiple browser tabs — action is idempotent and cart remains cleared | User is logged in and has completed the Checkout - Overview step with an order submitted, Two browser tabs (Tab A and Tab B) both have the Checkout - Confirmation page loaded | 1. In Tab A, click the Back Home button<br>2. Observe Tab A navigates to Product Inventory and the cart item count indicator<br>3. Switch to Tab B (which still displays the Confirmation page) and click the Back Home button<br>4. Observe Tab B navigates to Product Inventory and the cart item count indicator | Tab A's Back Home click succeeds and clears the cart (cart indicator 0). Tab B's Back Home click also succeeds but does not cause errors or duplicate orders; both tabs show Product Inventory and the cart indicator remains 0 (action is idempotent). | medium |

---
