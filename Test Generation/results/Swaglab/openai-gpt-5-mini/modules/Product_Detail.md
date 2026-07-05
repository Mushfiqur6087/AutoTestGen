# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Product Detail

Total: **12** (positive: 4, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User logged in, User has selected a specific product and is on the Product Detail page, Selected product is Not In Cart | 1. Click the 'Add to cart' button on the Product Detail page | The action button label on the Product Detail page changes to 'Remove', indicating the product is now in the cart | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User logged in, User has selected a specific product and is on the Product Detail page, Selected product is In Cart | 1. Click the 'Remove' button on the Product Detail page | The action button label on the Product Detail page changes to 'Add to cart', indicating the product is not in the cart | high |
| TC-003 | WF-003 | Navigate back to Product Inventory using Back to products link | User logged in, User has selected a specific product and is on the Product Detail page | 1. Click the 'Back to products' link on the Product Detail page | The Product Inventory page is shown | medium |
| TC-004 | WF-004 | Open Shopping Cart via header cart icon | User logged in, User has selected a specific product and is on the Product Detail page | 1. Click the cart icon in the header | The Shopping Cart page is shown | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Click 'Add to cart' while not logged in | User is not logged in, A product <product> exists in the catalog | 1. Navigate to the Product Inventory page<br>2. Click the <product> name or image to open the Product Detail page for <product><br>3. Click the 'Add to cart' button on the Product Detail page | Action is blocked: the UI prompts the user to sign in (redirects to the login page or displays a sign-in modal); the Product Detail page does not add the product to the cart and the cart item count in the header does not increase | high |
| TC-006 | WF-001 | Attempt 'Add to cart' when product is already in cart (button should not be available) | User is logged in, The product <product> is already in the user's cart | 1. Sign in as a user who has <product> in their cart<br>2. Navigate to the Product Detail page for <product> | The 'Add to cart' action is not available on the Product Detail page for a product that is already in the cart: the 'Add to cart' control is not visible (or is disabled); the 'Remove' control is visible instead; no additional item is added to the cart and the cart item count does not increase | high |
| TC-007 | WF-002 | Attempt 'Remove' when product is not in cart (button should not be available) | User is logged in, The product <product> is not in the user's cart | 1. Sign in as a user who does not have <product> in their cart<br>2. Navigate to the Product Detail page for <product><br>3. Attempt to click a 'Remove' control on the Product Detail page (if present) | The 'Remove' action is not available on the Product Detail page for a product that is not in the cart: the 'Remove' control is not visible (or is disabled); the 'Add to cart' control is visible instead; no removal occurs and the cart item count remains unchanged | high |
| TC-008 | WF-004 | Click header cart icon while not logged in | User is not logged in, A product <product> exists in the catalog | 1. Navigate to the Product Detail page for <product><br>2. Click the header cart icon | Action is blocked: user is redirected to the login page or shown a sign-in prompt instead of the Shopping Cart; the Shopping Cart page is not displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (state_edge) | WF-001 | Rapid double-click 'Add to cart' when product is Not In Cart | User is logged in, User is viewing Product Detail for a product that is Not In Cart | 1. Verify the Product Detail action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. Immediately (within ~500ms) click the 'Add to cart' button again. | Second 'Add to cart' click is blocked; the Product Detail action button label changes to 'Remove' and remains 'Remove' (visible on-screen). When opening the Shopping Cart from the header, the product appears exactly once (no duplicate entries). | medium |
| TC-010 (state_edge) | WF-002 | Rapid double-click 'Remove' when product is In Cart | User is logged in, Product is already In Cart, User is viewing Product Detail for that product and sees the action button labeled 'Remove' | 1. Verify the Product Detail action button label reads 'Remove'.<br>2. Click the 'Remove' button.<br>3. Immediately (within ~500ms) click the 'Remove' button again. | Second 'Remove' click is blocked; the Product Detail action button label changes to 'Add' and remains 'Add' (visible on-screen). When opening the Shopping Cart from the header, the product is absent (removed exactly once). | medium |
| TC-011 (interaction_edge) | WF-004 | Click 'Add to cart' then immediately open Shopping Cart via header icon and navigate back | User is logged in, User is viewing Product Detail for a product that is Not In Cart | 1. Verify the Product Detail action button label reads 'Add to cart'.<br>2. Click the 'Add to cart' button.<br>3. Immediately click the Header Cart Icon ('Go to Shopping Cart').<br>4. Press the browser Back button to return to the Product Detail page. | Navigation to the Shopping Cart page succeeds and the Shopping Cart page is displayed (visible page content indicates Shopping Cart). After pressing Back, the Product Detail page is displayed and the action button label is 'Remove' (reflecting the product being in the cart). | medium |
| TC-012 (state_edge) | WF-002 | Open Product Detail when product is already In Cart (state boundary on entry) | User is logged in, Product is already In Cart prior to navigation | 1. Navigate from Product Inventory to the Product Detail page for that product. | Product Detail page displays and the Product Detail action button label is 'Remove' (succeeds). | medium |

---
