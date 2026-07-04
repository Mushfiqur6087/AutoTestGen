# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Shopping Cart

Total: **11** (positive: 3, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart using the row Remove action | Logged in user with one or more items already added to the cart., Shopping Cart page is open with at least one item listed | 1. Locate the table row for <target item> in the Shopping Cart table<br>2. Click the 'Remove' action for <target item> | The row for <target item> is no longer visible in the Shopping Cart table; remaining items continue to display their quantity and description columns | high |
| TC-002 | WF-002 | Navigate to Product Inventory using Continue Shopping link | Logged in user with one or more items already added to the cart., Shopping Cart page is open | 1. Click the 'Continue Shopping' link in the Shopping Cart action bar | Product Inventory page is displayed (navigation to Product Inventory confirmed) | medium |
| TC-003 | WF-003 | Begin checkout flow using Checkout button | Logged in user with one or more items already added to the cart., Shopping Cart page is open | 1. Click the 'Checkout' button in the Shopping Cart action bar | Checkout - Information step of the checkout flow is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Shopping Cart page | User is not authenticated (logged out) | 1. Ensure the user is logged out<br>2. Navigate to the Shopping Cart page (click the cart icon or visit the cart URL) | Navigation is blocked: the user is redirected to the Login page; Shopping Cart content (item table, Remove buttons, Checkout button) is not displayed and no checkout flow begins. | high |
| TC-005 | WF-003 | Begin Checkout is blocked when cart contains zero items (submit-time constraint) | User is authenticated, There is at least one item in the cart at test start | 1. Log in as a valid user<br>2. Open the Shopping Cart page<br>3. Click 'Remove' on the remaining item(s) until the cart shows zero items (cart becomes empty)<br>4. Click the 'Checkout' button | The Checkout action is blocked: clicking 'Checkout' does not navigate to the checkout flow; the page remains on Shopping Cart. A visible inline message or UI indicator appears near the 'Checkout' control stating that checkout cannot begin because the cart contains no items; no checkout flow is started and cart state remains unchanged (empty). | high |
| TC-006 | WF-003 | Checkout control is unavailable on page load when cart is empty (timing check) | User is authenticated, Cart is empty before opening the Shopping Cart page | 1. Log in as a valid user<br>2. Ensure the user's cart contains zero items<br>3. Open the Shopping Cart page | On page load the 'Checkout' control is not actionable: the 'Checkout' button is either not visible or is displayed in a disabled (greyed-out) state; it cannot be clicked to start checkout. A visible UI indication is present near where the control would be, indicating checkout requires at least one cart item; no navigation to the checkout flow occurs. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-003 | Checkout succeeds when cart contains exactly one item (minimum count boundary) | Logged in user, Shopping cart contains exactly one item | 1. Open the Shopping Cart page<br>2. Confirm exactly one row is present in the items table<br>3. Click the Checkout button in the Shopping Cart Action Bar | Checkout begins and navigation to the Checkout flow succeeds; user is navigated to the Checkout - Information page (Checkout action succeeds). The Shopping Cart no longer blocks the transition. | medium |
| TC-008 (boundary) | WF-003 | Checkout is blocked when cart contains zero items (past-boundary of the 'one or more items' requirement) | Logged in user, Shopping cart is empty (zero items) | 1. Open the Shopping Cart page<br>2. Confirm no rows are present in the items table<br>3. Click the Checkout button in the Shopping Cart Action Bar | Checkout is blocked / error shown: the UI displays a visible inline message near the Checkout button indicating that one or more items are required (Checkout does not begin and the user remains on the Shopping Cart page). | medium |
| TC-009 (state_edge) | WF-001 | Remove the only item then immediately attempt Checkout (state boundary/race) | Logged in user, Shopping cart contains exactly one item | 1. Open the Shopping Cart page<br>2. Click Remove on the single item row<br>3. Immediately (within one second) click the Checkout button | Remove action succeeds and the item row is removed from the table; because the cart becomes empty, the subsequent Checkout attempt is blocked and a visible inline message is shown indicating one or more items are required (remove succeeds; Checkout is blocked / error shown). | medium |
| TC-010 (interaction_edge) | WF-001 | Rapid double-click of Remove on the same item does not produce duplicate removals or errors | Logged in user, Shopping cart contains at least one item | 1. Open the Shopping Cart page<br>2. Rapidly click Remove on the same item row twice in quick succession | First Remove click succeeds and removes the row; the second rapid click has no additional effect because the row is no longer present (no duplicate removal operations are performed and no persistent error is shown). The table ends with the row removed exactly once. | low |
| TC-011 (input_edge) |  | Very long item description rendering in the cart (display edge) | Logged in user, A product with a very long description (>= 200 characters) has been added to the cart | 1. Open the Shopping Cart page<br>2. Observe the description cell for the long-description item row | The Shopping Cart displays the long description without breaking the page layout. The UI either shows the full text wrapped across lines or shows a truncated description with an obvious affordance (e.g., ellipsis and a tooltip or expand control) to view the full text; no layout overflow or functional regression occurs and the cart remains usable (long-description rendering succeeds or is gracefully truncated with a visible indicator). | low |

---
