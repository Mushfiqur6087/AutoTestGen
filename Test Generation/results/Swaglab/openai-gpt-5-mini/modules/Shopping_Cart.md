# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Shopping Cart

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <Registered user>, Shopping Cart contains an item with description <item description> and quantity 1 (added from Product Inventory) | 1. Navigate to the Shopping Cart page (e.g., click the cart icon in the header)<br>2. In the Shopping Cart table, click the Remove action for the row with description <item description> | The Shopping Cart table no longer displays a row with description <item description>; the cart item count badge in the header reflects the removal (shows a decreased count) | high |
| TC-002 | WF-002 | Continue shopping navigates to Product Inventory | User logged in as <Registered user>, Shopping Cart contains one or more items | 1. Navigate to the Shopping Cart page (e.g., click the cart icon in the header)<br>2. Click the Continue Shopping link in the Shopping Cart action bar | The Product Inventory page opens; the 'Product Inventory' heading and the product listing are visible | medium |
| TC-003 | WF-003 | Begin checkout from the Shopping Cart | User logged in as <Registered user>, Shopping Cart contains one or more items | 1. Navigate to the Shopping Cart page (e.g., click the cart icon in the header)<br>2. Click the Checkout button in the Shopping Cart action bar | The Checkout - Information page opens; the checkout form is visible and the checkout step indicator shows the 'Information' step | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Access Shopping Cart while not logged in is blocked | User is not logged in | 1. From a signed-out browser session, click the shopping cart icon or navigate to the Shopping Cart page | Navigation is blocked; the Login page is displayed and the Shopping Cart contents are not shown (the user is not taken into the cart or checkout flow) | high |
| TC-005 | WF-003 | Clicking Checkout while not logged in does not begin checkout | User is not logged in, Shopping cart contains one or more items (added as a guest or pre-existing in session) | 1. As a signed-out user, add an item to the cart from Product Inventory (if necessary) so the cart has at least one item<br>2. Navigate to the Shopping Cart page<br>3. Click the Checkout button in the Shopping Cart action bar | Checkout is blocked due to authentication precondition; the user is redirected to the Login page (or shown a login prompt) and the Checkout flow does not begin; the Shopping Cart page remains unchanged and no checkout screens are shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click Remove on a single cart row | Logged-in user with at least one item present in the Shopping Cart (single cart row visible), Cart badge shows the current item count | 1. Open the Shopping Cart page<br>2. Double-click the Remove button on the visible cart row (two clicks in quick succession) | Remove action succeeds once: the cart row for that item disappears from the table and the cart badge count decrements by one; the second click is ignored and no error message is shown | medium |
| TC-007 (input_edge) |  | Item description containing emoji and non-Latin unicode is displayed intact | Logged-in user with an item previously added to the cart whose description contains emoji and non-Latin/unicode characters | 1. Open the Shopping Cart page<br>2. Locate the description cell for the item containing the special characters | Shopping Cart displays the emoji and non-Latin/unicode characters intact in the item's description cell (visible characters match the stored description); no placeholder glyphs or inline error indicators are shown | low |
| TC-008 (input_edge) |  | Leading and trailing whitespace in stored product text is trimmed in cart display | Logged-in user with an item previously added to the cart whose name/description was saved with leading and/or trailing whitespace | 1. Open the Shopping Cart page<br>2. Inspect the displayed product name and description for that cart row | Leading and trailing whitespace is trimmed in the Shopping Cart display: the product name and description visible in the table have no extra spaces at the start or end | low |

---
