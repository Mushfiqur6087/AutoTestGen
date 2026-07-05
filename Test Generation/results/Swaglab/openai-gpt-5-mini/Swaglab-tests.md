# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 92 | 32 | 29 | 31 | 44 | 38 | 10 |

## Login

Total: **13** (positive: 5, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials redirects to Product Inventory | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | The Product Inventory page is displayed; the inventory page heading and the products list/grid are visible. | high |
| TC-002 | WF-002 | Attempt login with empty Username shows required-username error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field empty<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Username is required." | medium |
| TC-003 | WF-003 | Attempt login with empty Password shows required-password error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter standard_user in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Password is required." | medium |
| TC-004 | WF-004 | Attempt login with invalid credentials shows mismatch error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-005 | WF-005 | Attempt login with locked_out_user shows locked-out error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Sorry, this user has been locked out." | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Submit with Username blank (required text field) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Username is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-007 | WF-003 | Submit with Password blank (required password field) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | An error banner displays 'Epic sadface: Password is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-008 |  | Submit with all required fields empty | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Error banners display 'Epic sadface: Username is required.' and 'Epic sadface: Password is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-009 | WF-004 | Submit with filled but invalid credentials (authentication failure) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Username and password do not match any user in this service.'; login is blocked; user remains on the sign-in page. | high |
| TC-010 | WF-005 | Attempt login with a locked-out account | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <locked_out_user> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Sorry, this user has been locked out.'; login is blocked; user remains on the sign-in page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Very long Username (200+ chars) treated as invalid credentials | User is unauthenticated and is on the sign-in page | 1. Enter a username consisting of 200+ characters into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button | Login is blocked; the page displays the error banner: Epic sadface: Username and password do not match any user in this service. | medium |
| TC-012 (input_edge) |  | Username with leading and trailing whitespace is trimmed and accepted | User is unauthenticated and is on the sign-in page, A known valid username is visible on the sign-in page (listed as an accepted test username) | 1. Enter the valid username shown on the sign-in page with one or more leading and trailing spaces into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button | Login succeeds; the user is redirected to the Product Inventory page and the Product Inventory page is displayed. | medium |
| TC-013 (interaction_edge) |  | Browser Back after successful login shows blank sign-in form (no pre-filled credentials) | User is unauthenticated and is on the sign-in page, A known valid username and the shared password are available | 1. Enter a known valid username into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button<br>4. After redirect to the Product Inventory page, click the browser Back button | Sign-in page is shown and both Username and Password fields are empty (no credentials pre-filled). | low |

---

## Product Inventory

Total: **17** (positive: 10, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open 'All Items' from header hamburger menu | User logged in as <Authenticated user>, Product Inventory page is open | 1. Click the hamburger menu in the header<br>2. Click the 'All Items' menu item | All Items page is displayed (All Items page heading and content are visible) | medium |
| TC-002 | WF-002 | Open 'About' from header hamburger menu | User logged in as <Authenticated user>, Product Inventory page is open | 1. Click the hamburger menu in the header<br>2. Click the 'About' menu item | About page is displayed (About page heading and content are visible) | medium |
| TC-003 | WF-003 | Logout via header hamburger menu | User logged in as <Authenticated user>, Product Inventory page is open | 1. Click the hamburger menu in the header<br>2. Click the 'Logout' menu item<br>3. If a logout confirmation appears, click Confirm | Sign-in page is displayed (sign-in form and heading are visible) | high |
| TC-004 | WF-004 | Reset App State via header hamburger menu | User logged in as <Authenticated user>, Product Inventory page is open, Cart contains one or more items | 1. Click the hamburger menu in the header<br>2. Click the 'Reset App State' menu item<br>3. If a confirmation appears, click Confirm | Product Inventory page shows default application state: product list in default sort order and the cart badge displays '0' | medium |
| TC-005 | WF-005 | Open Cart button to start Checkout sequence | User logged in as <Authenticated user>, Product Inventory page is open | 1. Click the 'Cart' button in the header | Checkout sequence opens at the Information step (Checkout - Information heading and its form are visible) | high |
| TC-006 | WF-006 | Change sort order to 'Price (low–high)' | User logged in as <Authenticated user>, Product Inventory page is open, Multiple products are listed | 1. Open the 'Sort By' dropdown<br>2. Select 'Price (low–high)' | Product list is reordered by price ascending: items are displayed in low-to-high price order according to the selected 'Price (low–high)' option | medium |
| TC-007 | WF-007 | Open Product Detail by clicking product name | User logged in as <Authenticated user>, Product Inventory page is open, At least one product is listed | 1. Click the product name link for <a product><br>2. Wait for Product Detail page to load | Product Detail page is displayed for the selected product (product title and detailed description are visible) | high |
| TC-008 | WF-008 | Open Product Detail by clicking product image | User logged in as <Authenticated user>, Product Inventory page is open, At least one product is listed | 1. Click the product image link for <a product><br>2. Wait for Product Detail page to load | Product Detail page is displayed for the selected product (product title and detailed description are visible) | high |
| TC-009 | WF-009 | Add an item to the cart from the Product Inventory | User logged in as <Authenticated user>, Product Inventory page is open, <a product not in cart> is visible in the product list, Note the current cart badge count | 1. Click the 'Add to cart' button for <a product not in cart> | The product's action button label changes to 'Remove'; the cart badge count increases by 1 | high |
| TC-010 | WF-010 | Remove an item from the cart from the Product Inventory | User logged in as <Authenticated user>, Product Inventory page is open, <a product currently in cart> is visible in the product list, Note the current cart badge count | 1. Click the 'Remove' button for <a product currently in cart> | The product's action button label changes to 'Add to cart'; the cart badge count decreases by 1 | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Unauthenticated user cannot access Product Inventory page (requires authenticated session) | User is not authenticated (no active session) | 1. In a new browser session ensure the user is signed out<br>2. Navigate directly to the Product Inventory page URL | Navigation is blocked: the Sign-in page is displayed instead of the Product Inventory page; Product Inventory content (product list, header cart badge) is not visible | high |
| TC-012 | WF-005 | Unauthenticated user cannot open Cart / Checkout (Cart button precondition requires authentication) | User is not authenticated (no active session) | 1. In a new browser session ensure the user is signed out<br>2. Attempt to open the Cart (click the Cart button in the header or navigate to the Checkout entry URL) | Checkout navigation is blocked: the user is redirected to the Sign-in page; the Checkout sequence (Information → Overview → Confirmation) is not opened | high |
| TC-013 | WF-009 | Cannot 'Add to cart' when product is already in cart (Add button should be hidden when Item_In_Cart == true) | <specific product currently in cart (Item_In_Cart == true)> | 1. Sign in and open the Product Inventory page<br>2. Locate the product that is already in the cart (<specific product currently in cart>)<br>3. Observe the Add to cart control area for that product | The Add to cart button is not visible for that product; the Remove button is visible instead; attempting to add is not possible and the cart contents and cart badge count remain unchanged | high |
| TC-014 | WF-010 | Cannot 'Remove' when product is not in cart (Remove button should be hidden when Item_In_Cart == false) | <specific product not currently in cart (Item_In_Cart == false)> | 1. Sign in and open the Product Inventory page<br>2. Locate the product that is not in the cart (<specific product not currently in cart>)<br>3. Observe the Remove control area for that product | The Remove button is not visible for that product; the Add to cart button is visible instead; attempting to remove is not possible and the cart contents and cart badge count remain unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (interaction_edge) | WF-009 | Rapid double-click 'Add to cart' on same product | Authenticated user on Product Inventory page, Target product is visible in the list and currently not in cart (button shows 'Add to cart'), Note current cart badge count | 1. Click the 'Add to cart' button for the target product.<br>2. Immediately (before the UI visibly updates) click the 'Add to cart' button for the same target product a second time. | Succeeds: Only a single addition is applied — the cart badge increments by exactly +1 relative to the noted precondition, the product card now displays 'Remove', and the cart contents show a single entry for that product (no duplicate entries). | medium |
| TC-016 (interaction_edge) |  | Immediate toggle: click Add then immediately click Remove | Authenticated user on Product Inventory page, Target product is visible and currently not in cart (button shows 'Add to cart'), Note current cart badge count | 1. Click the 'Add to cart' button for the target product.<br>2. Immediately click the 'Remove' button for the same target product (second click occurs before or just after the cart badge updates). | Succeeds: The net effect is zero — the cart badge returns to the original count from the precondition and the product card shows 'Add to cart'. No residual incorrect badge increments remain visible. | medium |
| TC-017 (input_edge) | WF-007 | Product with a very long product name (display/truncation and detail view) | Authenticated user on Product Inventory page, A product exists whose Product_Name length is very large (>= 200 characters) and is present in the product list | 1. Open the Product Inventory page (reload if already open).<br>2. Locate the product card for the very-long-name product in the product list.<br>3. Visually inspect the product name rendering in the product card.<br>4. Click the product name link for that product to navigate to the Product Detail page.<br>5. Observe the product name displayed on the Product Detail page. | Succeeds: On the inventory page the very-long product name does not break the product-card layout (it is truncated or wrapped to fit and an overflow indicator is visible); clicking the product name opens the Product Detail page which displays the full product name. All visual changes are visible to the user. | low |

---

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

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete required fields and continue to Overview | User logged in as <Buyer>, Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Ensure the Checkout - Information page is open (first step of the checkout flow).<br>2. Enter <first name> in the First Name field<br>3. Enter <last name> in the Last Name field<br>4. Enter <postal code> in the Postal Code field<br>5. Click the Continue button | The Checkout - Overview page is displayed with the page heading 'Checkout - Overview' | high |
| TC-002 | WF-002 | Click Cancel returns to Shopping Cart | User logged in as <Buyer>, Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Ensure the Checkout - Information page is open (first step of the checkout flow).<br>2. Click the Cancel button | The Shopping Cart page is displayed; the cart listing shows the previously added item(s) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave required text field (First Name) blank and submit | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Navigate to Checkout - Information as a logged-in user with at least one item in the Shopping Cart.<br>2. Leave the First Name field blank.<br>3. Enter <valid Last Name> in the Last Name field.<br>4. Enter <valid Postal Code> in the Postal Code field.<br>5. Click the Continue button. | An error banner is shown on the page: "Error: First Name is required"; the form does not navigate to Checkout - Overview and the user remains on the Checkout - Information page. | high |
| TC-004 | WF-001 | Submit with all required fields empty | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Navigate to Checkout - Information as a logged-in user with at least one item in the Shopping Cart.<br>2. Leave the First Name field blank.<br>3. Leave the Last Name field blank.<br>4. Leave the Postal Code field blank.<br>5. Click the Continue button. | Error banners are shown for each missing field: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required"; the form does not submit and the user remains on the Checkout - Information page. | high |
| TC-005 |  | Access Checkout - Information while unauthenticated | User is not authenticated (no active session). | 1. From a browser with no authenticated session, navigate to the Checkout - Information URL or attempt to start checkout from the Shopping Cart. | Access is blocked: the user is redirected to the Login page (Checkout - Information form is not displayed) and cannot proceed to Checkout - Overview without authenticating. | high |
| TC-006 |  | Attempt to open Checkout - Information with an empty Shopping Cart | Logged in with an active session and the Shopping Cart contains no items. | 1. Log in as a Buyer with an active session.<br>2. Ensure the Shopping Cart has no items.<br>3. From the Shopping Cart, click the control to begin checkout or navigate directly to Checkout - Information. | Access is blocked: the Checkout - Information form is not displayed and the user remains on the Shopping Cart (cannot proceed to Checkout - Overview without at least one item in the cart). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-001 | Very long First and Last Name accepted and carried to Overview | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <very long string 200+ characters> in the First Name field<br>2. Enter <very long string 200+ characters> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the entered First Name and Last Name (the full long text) without truncation errors | medium |
| TC-008 (input_edge) | WF-001 | Names containing special characters and emoji accepted | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <string containing special characters and emoji> in the First Name field<br>2. Enter <string containing special characters and emoji> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the entered First Name and Last Name including the special characters/emoji | medium |
| TC-009 (input_edge) | WF-001 | Leading and trailing whitespace is trimmed before validation | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <string with leading and trailing spaces> in the First Name field<br>2. Enter <string with leading and trailing spaces> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the First Name and Last Name with leading and trailing whitespace removed (trimmed) | medium |
| TC-010 (boundary) | WF-001 | Whitespace-only First Name is treated as missing and blocks continue | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <spaces-only string> in the First Name field<br>2. Enter <valid Last Name> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Continue is blocked; the page displays the error banner 'Error: First Name is required' (visible to the user) | medium |

---

## Checkout - Overview

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout and navigate to Confirmation | User logged in, Cart contains one or more items, Checkout contact/payment/shipping information has been entered on the Checkout - Information step | 1. Open the Checkout - Overview page<br>2. Verify the Order summary is visible and displays Item total, Tax, and Total; verify Payment information and Shipping information sections are visible<br>3. Click the Finish button | The Checkout - Confirmation page is displayed with a confirmation heading; the page shows an order summary listing Item total, Tax, and Total that match the Overview and a visible order confirmation section | high |
| TC-002 | WF-002 | Cancel checkout and return to Shopping Cart | User logged in, Cart contains one or more items, Checkout contact/payment/shipping information has been entered on the Checkout - Information step | 1. Open the Checkout - Overview page<br>2. Click the Cancel button | The Shopping Cart page is displayed showing the cart items list; the Checkout - Overview page is no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Access Overview while not authenticated | User is not logged in, Cart may contain items or be empty | 1. In a browser session where the user is logged out, navigate to the Checkout - Overview page URL (or click Checkout from the Cart)<br>2. Observe the resulting page | User is not shown the Checkout - Overview; the UI redirects to or displays the login screen (or an authentication prompt). The checkout is not accessible and no Finish/Cancel actions are performed. | high |
| TC-004 | WF-001 | Click Finish when cart is empty | User is logged in, Cart contains no items, Checkout contact/payment/shipping information may or may not be present | 1. Navigate to the Checkout - Overview page while signed in and with an empty cart<br>2. Click the Finish button | Finish does not complete; the page does not navigate to Checkout - Confirmation. An inline validation/error indicator is shown in or near the order summary indicating the cart is empty or that items are required. The order is not created and the user remains on Checkout - Overview. | high |
| TC-005 | WF-001 | Click Finish with missing payment or shipping information | User is logged in, Cart contains one or more items, Checkout contact/payment/shipping information has NOT been provided on the previous information step | 1. Navigate to the Checkout - Overview page while signed in and with items in the cart but without entering payment/shipping/contact information<br>2. Click the Finish button | Finish does not complete; the page does not navigate to Checkout - Confirmation. Inline validation errors appear on the missing information area(s) (for example, Payment information and/or Shipping information) indicating those details are required. The order is not created and the user remains on Checkout - Overview. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click of Finish (duplicate submit) | User is logged in, cart contains one or more items, and checkout contact/payment/shipping information has been entered on the Checkout - Information step., User is on the Checkout - Overview page showing order summary and Finish button. | 1. Click the Finish button once.<br>2. Immediately click the Finish button a second time (while the first submission is still processing).<br>3. Observe the UI after the clicks. | Second submission attempt is blocked: after the first click the Finish button becomes disabled or shows an in-progress indicator and the second click does not navigate again; the user is taken to the Checkout - Confirmation page once and no duplicate confirmation UI is shown. | medium |
| TC-007 (interaction_edge) | WF-001 | Browser Back after successful Finish (prevent duplicate order) | User is logged in, cart contains one or more items, and checkout contact/payment/shipping information has been entered on the Checkout - Information step., User is on the Checkout - Overview page. | 1. Click the Finish button and wait until the Checkout - Confirmation page is shown.<br>2. Use the browser Back button once to return to the Checkout - Overview page.<br>3. Observe the Overview page and the state of the cart and Finish/Cancel controls. | Visible outcome: returning to Checkout - Overview shows the cart as emptied or the page in a non-submittable state (Finish disabled) indicating the order was completed; the page does not produce a second confirmation or allow an immediate duplicate submission. | medium |
| TC-008 (input_edge) |  | Very long / special-character shipping address entered on prior step is displayed in Overview | User is logged in and cart contains one or more items., User is on the Checkout - Information step. | 1. Enter a shipping address value of 200+ characters containing a mix of special characters and emoji into the Shipping Address field on the Checkout - Information step.<br>2. Click Continue to navigate to Checkout - Overview.<br>3. Observe how the Checkout - Overview displays the shipping address in the summary view (layout, truncation indicator, or visible full value). | Visible outcome: the Overview either shows the full long shipping address without layout-breaking overflow or shows a visibly truncated address with a truncation/overflow indicator (e.g., ellipsis or 'show more') — the page remains usable and no rendering errors are shown. | low |

---

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
