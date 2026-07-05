# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Checkout - Confirmation

Total: **7** (positive: 1, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Back Home returns user to Product Inventory and clears the cart | User logged in as <User>, User has completed the checkout steps and is on the Checkout Confirmation page, Checkout Confirmation page is open and displays the success message "Thank you for your order!" | 1. On the Checkout Confirmation page, click the 'Back Home' button in the action bar | The Product Inventory page is displayed showing the product listing; the shopping cart shows an empty state (no items listed and the cart badge indicates no items); the Checkout Confirmation page and its success message "Thank you for your order!" are no longer visible | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user cannot access Confirmation page (login required) | User is not logged in | 1. In a new browser session where no user is authenticated, navigate directly to the Checkout - Confirmation page URL | Access is blocked: the user is redirected to the Login page; the Confirmation page content (success message and 'Back Home' button) is not displayed | high |
| TC-003 | WF-001 | Logged-in user who has not completed checkout cannot view Confirmation page | User is logged in, User has not completed the checkout steps and no order has been submitted for this session | 1. Ensure the user is logged in<br>2. From the Product Inventory, do NOT complete Checkout (leave at Shopping Cart or Checkout - Information)<br>3. Navigate directly to the Checkout - Confirmation page URL | Access is blocked: the Confirmation page content (success message and 'Back Home' button) is not displayed; the app returns the user to the checkout flow (redirected to the Checkout - Information page) instead | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid double-click of Back Home button | User is logged in and has completed the checkout steps with an order submitted (on Confirmation page with cart cleared on success) | 1. On the Confirmation page, locate the Back Home button<br>2. Click the Back Home button twice in rapid succession (double-click) | Succeeds: Product Inventory page is displayed and the cart count UI shows 0 (cart cleared); the UI shows a single navigation to Product Inventory (user ends on Product Inventory and the Confirmation-specific UI is no longer visible). | medium |
| TC-005 (input_edge) |  | Confirmation page display with very long product name in the completed order | User is logged in and completed checkout with an order that includes at least one product whose name is extremely long (200+ characters) | 1. Navigate to the Confirmation page for that completed order | Succeeds: Confirmation page displays the success message and the long product name is visible in the order summary area without obscuring or removing the Back Home button (the Back Home button remains visible and clickable). | low |
| TC-006 (input_edge) |  | Confirmation page display with product names containing emoji and special unicode characters | User is logged in and completed checkout with an order that includes product names containing emoji and special unicode characters | 1. Navigate to the Confirmation page for that completed order | Succeeds: Confirmation page displays the success message and the product names with emoji/special characters are rendered in the order summary area (characters appear in the UI rather than being removed); Back Home button remains visible and clickable. | low |
| TC-007 (state_edge) | WF-001 | Click Back Home then immediately add an item from Product Inventory | User is logged in and has completed the checkout steps with an order submitted (on Confirmation page) | 1. On the Confirmation page, click the Back Home button once<br>2. On the Product Inventory page (arrived from Back Home), immediately click Add-to-cart on a product | Succeeds: After clicking Back Home the Product Inventory page is shown and the cart count UI initially shows 0; after immediately adding a product the cart count UI increments to 1 (cart was cleared by Back Home and new add is reflected). | medium |

---
