# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Product Detail

Total: **15** (positive: 7, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User logged in as <Authenticated user>, Product Detail page is open for <selected product>, Product is Not In Cart | 1. Click the 'Add to cart' button on the Product Detail page | Primary action button on the Product Detail page changes to 'Remove' and the Shopping Cart icon's badge increases to reflect the item is in the cart | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User logged in as <Authenticated user>, Product Detail page is open for <selected product>, Product is In Cart | 1. Click the 'Remove' button on the Product Detail page | Primary action button on the Product Detail page changes to 'Add to cart' and the Shopping Cart icon's badge decreases accordingly so the product is no longer shown as in-cart | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via Back to products | User logged in as <Authenticated user>, Product Detail page is open for <selected product> | 1. Click the 'Back to products' link on the Product Detail page | Product Inventory page is displayed | medium |
| TC-004 | WF-004 | Navigate to All Items via persistent header | User logged in as <Authenticated user>, Product Detail page is open for <selected product> | 1. Click 'All Items' in the persistent header | All Items page is displayed | medium |
| TC-005 | WF-005 | Navigate to Shopping Cart via persistent header | User logged in as <Authenticated user>, Product Detail page is open for <selected product> | 1. Click the 'Shopping Cart' icon/link in the persistent header | Shopping Cart page is displayed | high |
| TC-006 | WF-006 | Logout via persistent header | User logged in as <Authenticated user>, Product Detail page is open for <selected product> | 1. Click 'Logout' in the persistent header | Login screen is displayed, indicating the user has been logged out | medium |
| TC-007 | WF-007 | Reset app state via persistent header clears cart and resets product state | User logged in as <Authenticated user>, Product Detail page is open for <selected product>, Shopping cart contains at least one item | 1. Click 'Reset App State' in the persistent header<br>2. Confirm any reset confirmation if shown | Shopping Cart icon's badge resets to 0 and the primary action button for the Product Detail page shows 'Add to cart' (product is Not In Cart) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Unauthenticated user cannot open Product Detail page | User is not logged in, Product identifier available: <product id> | 1. Open the Product Detail page URL for <product id> while not signed in<br>2. Observe the page shown | User is redirected to the Login page; Product Detail content (product image, name, description, price, and action bar) is not displayed. No changes are made to the cart (cart item count remains unchanged). | high |
| TC-009 | WF-001 | Clicking 'Add to cart' while not logged in is blocked | User is not logged in, Product is in state: Not In Cart | 1. Ensure the user session is signed out<br>2. Navigate to Product Detail for <product id> that is Not In Cart<br>3. Click the 'Add to cart' button | Action is blocked: user is taken to the Login page (Login form displayed) or shown a login prompt; the product is not added to the cart (cart item count remains the same). The Product Detail page does not transition to In Cart state. | high |
| TC-010 | WF-002 | Remove action is not available when product is Not In Cart (wrong-state) | User is logged in as <authenticated user>, Product is in state: Not In Cart | 1. Sign in as <authenticated user><br>2. Open Product Detail for <product id> that is Not In Cart<br>3. Attempt to locate and click a 'Remove' button in the action bar | The 'Remove' button is not present/visible in the action bar for this product; only the 'Add to cart' button is shown. No remove action occurs and the cart remains unchanged (product remains Not In Cart). | high |
| TC-011 | WF-001 | Add to cart action is not available when product is already In Cart (wrong-state) | User is logged in as <authenticated user>, Product is in state: In Cart | 1. Sign in as <authenticated user><br>2. Ensure the product <product id> is already in the cart (state: In Cart)<br>3. Attempt to locate and click an 'Add to cart' button in the action bar | The 'Add to cart' button is not present/visible in the action bar for this product; only the 'Remove' button is shown. No add action occurs and the cart remains unchanged (product remains In Cart). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (interaction_edge) | WF-001 | Rapid double-click of Add to cart — ensure only one addition | Authenticated user, Product Detail page open for a product that is currently Not In Cart, Initial cart item count noted | 1. Observe the Add to cart button is visible and actionable<br>2. Click the Add to cart button<br>3. Immediately (within 1 second) click the Add to cart button again | First Add action succeeds: cart badge increments by one and the button updates to the In Cart state (Remove). Second Add attempt is blocked / ignored: cart badge does not increment further and Shopping Cart contains only one unit of this product. | medium |
| TC-013 (state_edge) | WF-001 | Immediate Remove after Add — consecutive state transitions | Authenticated user, Product Detail page open for a product that is currently Not In Cart, Initial cart item count noted | 1. Click Add to cart<br>2. Immediately click Remove (while UI may still be updating) | Add action succeeds: product is added to cart and cart badge increments. The subsequent Remove action also succeeds: cart badge returns to the original value and Shopping Cart shows zero instances of this product. | medium |
| TC-014 (state_edge) | WF-002 | Attempt Remove after external reset clears cart | Authenticated user, Product Detail page open showing product in In Cart state (Remove button visible), Product initially present in cart | 1. Click the header control Reset App State<br>2. Click the Remove button on the Product Detail page | Remove attempt is blocked / error shown: since the cart was externally reset and the product is no longer in the cart, the UI shows a visible error near the action (e.g., 'product not in cart' or equivalent) and no removal occurs in Shopping Cart. | medium |
| TC-015 (input_edge) |  | Very long product description rendering on Product Detail | Authenticated user, Product Inventory contains a product whose description length is very long (200+ characters) and the product is selectable | 1. From Product Inventory, click the product with the very long description to open Product Detail<br>2. Observe how the product description is rendered on the page | Long description is accepted and displayed without truncation that hides content: the Product Detail shows the full description in a readable manner (e.g., within a scrollable container or expanded block) with no layout overlap or horizontal overflow. There is no UI crash or broken layout. | low |

---
