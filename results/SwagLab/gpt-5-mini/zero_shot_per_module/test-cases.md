# Test Cases — SwagLab

Generated: 2026-06-04T14:54:22.127313Z  
Model: gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 105 | 38 | 28 | 39 | 57 | 37 | 11 |

## Login

Total: **16** (positive: 5, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Login with standard_user and correct password | Login page is loaded, Accepted usernames list shown on page includes standard_user, Password secret_sauce is known | 1. In Username field enter: standard_user<br>2. In Password field enter: secret_sauce<br>3. Click the Login button | User is authenticated and redirected to the Product Inventory page | high |
| TC-002 |  | Login with problem_user and correct password | Login page is loaded, Accepted usernames list shown on page includes problem_user | 1. Enter problem_user into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | User is authenticated and redirected to the Product Inventory page | high |
| TC-003 |  | Login with performance_glitch_user and correct password (may be slow) | Login page is loaded, Accepted usernames list includes performance_glitch_user | 1. Enter performance_glitch_user into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | User is authenticated and redirected to the Product Inventory page (note: page load may take longer than normal) | medium |
| TC-004 |  | Login with visual_user and correct password | Login page is loaded, Accepted usernames list includes visual_user | 1. Enter visual_user into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | User is authenticated and redirected to the Product Inventory page | medium |
| TC-005 |  | Login with error_user and correct password | Login page is loaded, Accepted usernames list includes error_user | 1. Enter error_user into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | User is authenticated and redirected to the Product Inventory page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt login with locked_out_user | Login page is loaded, Accepted usernames list includes locked_out_user | 1. Enter locked_out_user into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | An error banner is shown with message: "Epic sadface: Sorry, this user has been locked out." | high |
| TC-007 |  | Valid username with incorrect password | Login page is loaded, standard_user is listed as accepted username | 1. Enter standard_user into Username<br>2. Enter incorrect_password into Password<br>3. Click Login | An error banner is shown with message: "Epic sadface: Username and password do not match any user in this service." | high |
| TC-008 |  | Unknown username with any password | Login page is loaded | 1. Enter unknown_user_123 into Username<br>2. Enter anyPassword into Password<br>3. Click Login | An error banner is shown with message: "Epic sadface: Username and password do not match any user in this service." | high |
| TC-009 |  | Empty username with filled password | Login page is loaded | 1. Leave Username field empty<br>2. Enter secret_sauce into Password<br>3. Click Login | An error banner is shown with message: "Epic sadface: Username is required." | high |
| TC-010 |  | Filled username with empty password | Login page is loaded | 1. Enter standard_user into Username<br>2. Leave Password field empty<br>3. Click Login | An error banner is shown with message: "Epic sadface: Password is required." | high |
| TC-011 |  | Both username and password empty | Login page is loaded | 1. Leave Username empty<br>2. Leave Password empty<br>3. Click Login | An error banner is shown; at minimum the Username required message is displayed: "Epic sadface: Username is required." | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Username with leading/trailing spaces is trimmed and accepted | Login page is loaded, standard_user is an accepted username | 1. Enter ' standard_user ' (with leading and trailing spaces) into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | System trims whitespace and authenticates the user, redirecting to the Product Inventory page. If trimming is not implemented, an error banner is shown with: "Epic sadface: Username and password do not match any user in this service." (test verifies trimming behavior) | medium |
| TC-013 |  | Very long username input (256+ chars) | Login page is loaded | 1. Enter a username string of 256 characters into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | Login is rejected; an error banner is shown with message: "Epic sadface: Username and password do not match any user in this service." or a validation error if the field enforces a maximum length | low |
| TC-014 |  | Attempt SQL-injection style username | Login page is loaded | 1. Enter "' OR '1'='1" into Username<br>2. Enter secret_sauce into Password<br>3. Click Login | Login is rejected and no injection occurs; error banner shows: "Epic sadface: Username and password do not match any user in this service." | high |
| TC-015 |  | Password field masks input (password obscured) | Login page is loaded | 1. Type any characters into the Password field<br>2. Observe how characters are displayed while typing | Password input is masked (characters are not displayed in plain text) and only obscured characters are visible | medium |
| TC-016 |  | Accepted usernames list is visible on the login page | Login page is loaded | 1. View the login page<br>2. Locate the list of accepted test usernames | The page shows accepted test usernames (for example: standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user) | medium |

---

## Product Inventory

Total: **12** (positive: 7, negative: 1, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Product list displays after login | User is logged in, At least one product exists in the catalog | 1. Navigate to the Product Inventory page | The page lists all products; each product row displays name, description, price and an 'Add to cart' button | high |
| TC-018 |  | Sort products by name A–Z | User is logged in, Multiple products with different names exist | 1. Open the Product Inventory page<br>2. Open the sort dropdown and select 'Name (A–Z)' | Products are reordered so names are in ascending alphabetical order (A to Z) | high |
| TC-019 |  | Sort products by price low–high | User is logged in, Multiple products with different prices exist | 1. Open the Product Inventory page<br>2. Open the sort dropdown and select 'Price (low–high)' | Products are reordered so prices are in ascending order (lowest price first) | high |
| TC-020 |  | Open Product Detail by clicking product name | User is logged in, At least one product is listed | 1. On the Product Inventory page, click the name of a product | The Product Detail page for the clicked product opens and displays product details | high |
| TC-021 |  | Open Product Detail by clicking product image | User is logged in, At least one product is listed with an image | 1. On the Product Inventory page, click the image of a product | The Product Detail page for the clicked product opens and displays product details | high |
| TC-022 |  | Add a product to cart updates button and badge | User is logged in, At least one product is listed, Cart badge shows current item count (e.g., 0) | 1. On the Product Inventory page, click the 'Add to cart' button for a product | The clicked product's button changes to 'Remove' and the cart badge increments by 1 | high |
| TC-023 |  | Remove product from cart updates button and badge | User is logged in, A product is already added to the cart (button shows 'Remove'), Cart badge reflects the product in the cart | 1. On the Product Inventory page, click the 'Remove' button for the product that is in the cart | The clicked product's button changes back to 'Add to cart' and the cart badge decrements by 1 | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Access Product Inventory while logged out | User is logged out | 1. Navigate directly to the Product Inventory page URL | User is redirected to the login page or shown an access-required message; product list is not displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Empty inventory displays no-products message | User is logged in, No products exist in the catalog | 1. Open the Product Inventory page | The page shows a clear 'no products' or 'no items available' message; no product rows or 'Add to cart' buttons are present and the cart badge remains unchanged | medium |
| TC-026 |  | Very long product name and description rendering | User is logged in, A product exists with a very long name and description (e.g., >500 characters) | 1. Open the Product Inventory page | Long name/description is displayed safely (truncated or wrapped) without breaking layout; price and 'Add to cart' button remain visible and functional | low |
| TC-027 |  | Sorting with duplicate names or identical prices | User is logged in, Multiple products exist that share the same name or the same price | 1. Open the Product Inventory page<br>2. Select 'Name (A–Z)' then verify order of products with identical names<br>3. Select 'Price (low–high)' then verify order of products with identical prices | Sorting executes without error; products with identical sort keys are grouped and order is consistent (deterministic) after each sort selection | medium |
| TC-028 |  | Rapid add/remove toggling keeps cart badge consistent | User is logged in, At least one product is listed, Initial cart badge count is known (e.g., 0) | 1. On the Product Inventory page, rapidly click 'Add to cart' then 'Remove' for the same product five times<br>2. Observe the cart badge after the rapid sequence | UI remains responsive; button toggles between 'Add to cart' and 'Remove' on each click and the cart badge accurately reflects the current state (ends at initial count) | low |

---

## Product Detail

Total: **14** (positive: 6, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Display product image, name, description, and price | User is logged in (if required) or anonymous browsing allowed, Product with id P123 exists and has image, name, description, and price | 1. Navigate to the Product Inventory page<br>2. Click on the product with id P123 to open the Product Detail page | Product Detail page displays the product image, product name, product description, and product price correctly | high |
| TC-030 |  | Add product to cart when not already in cart | User has at least view access, Product P124 is not in the shopping cart | 1. Open Product Detail for product P124<br>2. Verify the action button shows 'Add to cart'<br>3. Click the 'Add to cart' button | Product is added to the shopping cart; button label changes to 'Remove' (or appropriate remove state); cart icon badge increments accordingly | high |
| TC-031 |  | Remove product from cart when already in cart | Product P125 is already present in the shopping cart, User is on the Product Detail page for P125 | 1. Verify the action button shows 'Remove'<br>2. Click the 'Remove' button | Product is removed from the shopping cart; button label changes to 'Add to cart'; cart icon badge decrements accordingly | high |
| TC-032 |  | Back to products navigates to Product Inventory page | User is on the Product Detail page for any product | 1. Click the 'Back to products' button | User is navigated back to the Product Inventory page and product list is displayed | high |
| TC-033 |  | Cart icon is visible and navigates to Shopping Cart | User is on the Product Detail page | 1. Verify the cart icon is visible on the Product Detail page<br>2. Click the cart icon | User is navigated to the Shopping Cart page | high |
| TC-034 |  | Action button reflects current cart state on page load | There are two products: P126 not in cart and P127 already in cart | 1. Open Product Detail for P126 and verify button shows 'Add to cart'<br>2. Open Product Detail for P127 and verify button shows 'Remove' | Action button text/state correctly reflects whether the product is in the cart for each product | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-035 |  | Server error when adding to cart shows error message and does not change UI state | Product P128 is not in cart, Backend API for adding to cart is mocked to return HTTP 500 | 1. Open Product Detail for P128<br>2. Click 'Add to cart'<br>3. Observe the UI response | An error message is displayed (e.g., 'Unable to add to cart'); the button remains 'Add to cart' and cart badge does not increment | high |
| TC-036 |  | Invalid product id in URL shows error or redirects to inventory/404 | User attempts to open Product Detail page with invalid product id (e.g., /product/invalid-id) | 1. Directly navigate to the Product Detail URL with an invalid product id<br>2. Observe the page response | Application shows an appropriate error message or 404 page or redirects to Product Inventory; no product details are displayed | high |
| TC-037 |  | Attempt to add to cart while offline shows offline notification | Product P129 exists and is not in cart, Device/network is set to offline mode | 1. Open Product Detail for P129 while offline<br>2. Click 'Add to cart' | User is notified of network/offline error (e.g., 'No internet connection'); product is not added and button state remains unchanged | medium |
| TC-038 |  | Missing price field displays 'Price unavailable' or shows validation | Product P130 exists but backend returns null/empty price for the product | 1. Open Product Detail for P130<br>2. Observe the price area | UI displays a sensible fallback (e.g., 'Price unavailable') or an error indicator; Add to cart may be disabled if business rule requires price | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Very long product name and description render without breaking layout | Product P131 has a name of 500+ characters and description of 5000+ characters | 1. Open Product Detail for P131<br>2. Scroll through the page and inspect layout and text wrapping | Long text is wrapped or truncated per UI design; page remains usable (no overflow off-screen or broken layout); back and cart buttons remain accessible | medium |
| TC-040 |  | Extremely large or high-precision price displays with correct formatting | Product P132 has price set to a very large number (e.g., 9999999999.9999) | 1. Open Product Detail for P132<br>2. Observe how the price is formatted and displayed | Price is formatted according to locale/currency rules (rounded/displayed correctly) and does not break layout; if beyond allowed range, an appropriate message is shown | medium |
| TC-041 |  | Broken product image displays placeholder or alt text | Product P133 has an image URL that returns 404 or is corrupt | 1. Open Product Detail for P133<br>2. Observe the image area | A placeholder image or descriptive alt text is shown instead of a broken image icon; page layout remains intact | low |
| TC-042 |  | Rapid repeated Add/Remove clicks do not duplicate cart entries | Product P134 is not in cart, Application and backend available | 1. Open Product Detail for P134<br>2. Rapidly click 'Add to cart' and then 'Remove' multiple times in quick succession (10+ clicks)<br>3. Open Shopping Cart to inspect item quantity/entries | Cart contains at most one entry for P134 with correct quantity; UI remains responsive and no duplicate entries or inconsistent state occur | high |

---

## Shopping Cart

Total: **11** (positive: 5, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Cart page displays added items with quantity, description and Remove button | User is logged in, User has added 2 distinct products to the cart (from Product Inventory) | 1. Navigate to the Shopping Cart page | Both products are listed; each line shows quantity = 1, the product description, and a visible 'Remove' button for each item | high |
| TC-044 |  | Remove an item from the cart | User is on the Shopping Cart page, Cart contains at least 2 items | 1. Click the 'Remove' button for one specific item<br>2. Observe the cart contents update | The selected item is removed from the list, the remaining items remain visible, and item count updates accordingly | high |
| TC-045 |  | Remove last item results in empty cart state | User is on the Shopping Cart page, Cart contains exactly 1 item | 1. Click the 'Remove' button for the only item in the cart<br>2. Observe the cart page after removal | Cart shows an empty-state message (e.g. 'Your cart is empty'), there are no item rows, and Checkout is disabled or not available while Continue Shopping remains available | high |
| TC-046 |  | Continue Shopping navigates back to Product Inventory | User is on the Shopping Cart page | 1. Click the 'Continue Shopping' button/link | The application navigates to the Product Inventory page (product list visible) and the user can continue adding items | medium |
| TC-047 |  | Checkout starts checkout process | User is on the Shopping Cart page, Cart contains at least 1 item | 1. Click the 'Checkout' button | The application navigates to the first step of checkout (shipping/payment or order summary), indicating checkout has begun | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Checkout attempt when cart is empty is blocked | User is on the Shopping Cart page, Cart is empty | 1. Click the 'Checkout' button (if enabled) or attempt to start checkout<br>2. Observe system response | Checkout is blocked: either the Checkout button is disabled or an error/notification appears (e.g. 'Your cart is empty') and the checkout flow is not started | high |
| TC-049 |  | Remove action fails due to server error | User is on the Shopping Cart page, Cart contains at least 1 item, Server-side delete API is returning an error (simulated by test stub or network condition) | 1. Click the 'Remove' button for an item<br>2. Observe the UI response and any error messaging | An error message is displayed (e.g. 'Unable to remove item, please try again'), the item remains visible in the cart, and the UI does not incorrectly remove the item | medium |
| TC-053 |  | Checkout blocked when item data is invalid (missing price) | User is on the Shopping Cart page, Cart contains an item with missing or invalid price data (data error) | 1. Click the 'Checkout' button<br>2. Observe any validation or error messaging preventing checkout | Checkout is prevented; an error message is shown explaining the problem (e.g. 'One or more items have missing price information') and user cannot proceed until data is corrected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Cart displays and remains usable with a large number of items | User is on the Shopping Cart page, Cart contains a large number of items (e.g. 50+ items) | 1. Load the Shopping Cart page<br>2. Scroll through the list and attempt to remove one item from the middle of the list | All items are rendered accessibly (list scrolls/paginates as designed), performance remains acceptable, and removing one item updates the list correctly without UI breakage | medium |
| TC-051 |  | Very long item description is handled without layout break | User is on the Shopping Cart page, Cart contains an item with an extremely long description (e.g. 2000+ characters) | 1. Load the Shopping Cart page and inspect the item row with the long description | The long description is truncated or wrapped per UI requirements (no horizontal overflow breaking layout); full description is accessible via tooltip or expand control if specified | medium |
| TC-052 |  | Quantity is displayed as 1 and cannot be edited | User is on the Shopping Cart page, Cart contains at least 1 item | 1. Inspect the quantity value displayed for an item<br>2. Attempt to edit the quantity (click, type, or look for increment/decrement controls) | Quantity is displayed as '1' for each item; no editable controls are available and attempts to change quantity do not alter the displayed value | low |

---

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Continue with valid First Name, Last Name, Postal Code | User has items in the shopping cart, User is on the Checkout - Information page | 1. Enter a valid First Name (e.g. "John")<br>2. Enter a valid Last Name (e.g. "Doe")<br>3. Enter a valid Postal Code (e.g. "12345")<br>4. Click the "Continue" button | User is taken to the Checkout - Overview step/page showing order summary | high |
| TC-055 |  | Cancel returns to Shopping Cart | User has items in the shopping cart, User is on the Checkout - Information page | 1. Click the "Cancel" button | User is returned to the Shopping Cart page and Checkout is aborted | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Missing First Name shows error | User is on the Checkout - Information page | 1. Leave First Name empty<br>2. Enter a valid Last Name (e.g. "Doe")<br>3. Enter a valid Postal Code (e.g. "12345")<br>4. Click the "Continue" button | An error banner is displayed stating "Error: First Name is required" and user remains on the Information page | high |
| TC-057 |  | Missing Last Name shows error | User is on the Checkout - Information page | 1. Enter a valid First Name (e.g. "John")<br>2. Leave Last Name empty<br>3. Enter a valid Postal Code (e.g. "12345")<br>4. Click the "Continue" button | An error banner is displayed stating "Error: Last Name is required" and user remains on the Information page | high |
| TC-058 |  | Missing Postal Code shows error | User is on the Checkout - Information page | 1. Enter a valid First Name (e.g. "John")<br>2. Enter a valid Last Name (e.g. "Doe")<br>3. Leave Postal Code empty<br>4. Click the "Continue" button | An error banner is displayed stating "Error: Postal Code is required" and user remains on the Information page | high |
| TC-059 |  | All required fields missing shows all errors | User is on the Checkout - Information page | 1. Leave First Name empty<br>2. Leave Last Name empty<br>3. Leave Postal Code empty<br>4. Click the "Continue" button | Error banners are displayed for each missing field (e.g. "Error: First Name is required", "Error: Last Name is required", "Error: Postal Code is required") and user remains on the Information page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Whitespace-only First Name is treated as missing | User is on the Checkout - Information page | 1. Enter whitespace only into First Name (e.g. "   ")<br>2. Enter a valid Last Name (e.g. "Doe")<br>3. Enter a valid Postal Code (e.g. "12345")<br>4. Click the "Continue" button | An error banner is displayed stating "Error: First Name is required" (whitespace is treated as empty) and user remains on the Information page | medium |
| TC-061 |  | Very long input values are accepted if non-empty | User is on the Checkout - Information page | 1. Enter a very long First Name (e.g. 255 characters)<br>2. Enter a very long Last Name (e.g. 255 characters)<br>3. Enter a very long Postal Code (e.g. 50 characters)<br>4. Click the "Continue" button | If the application only enforces required-field validation, user is taken to the Checkout - Overview step; if there is a maxlength validation, a validation error is shown indicating the offending field. (Tester should verify whether the system accepts or rejects long values) | medium |
| TC-062 |  | Names with special characters and numbers are accepted as valid input | User is on the Checkout - Information page | 1. Enter First Name with special characters/numbers (e.g. "O'Connor-Jr 3")<br>2. Enter Last Name with special characters (e.g. "Smith-Wesson")<br>3. Enter a valid Postal Code (e.g. "A1B 2C3")<br>4. Click the "Continue" button | Fields are accepted (since required validation is met) and user is taken to the Checkout - Overview step | low |
| TC-063 |  | Alphanumeric postal code with spaces is accepted | User is on the Checkout - Information page | 1. Enter a valid First Name (e.g. "John")<br>2. Enter a valid Last Name (e.g. "Doe")<br>3. Enter an alphanumeric Postal Code with space (e.g. "A1B 2C3")<br>4. Click the "Continue" button | Postal Code is accepted (treated as non-empty) and user is taken to the Checkout - Overview step | medium |

---

## Checkout - Overview

Total: **12** (positive: 3, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-064 |  | Order summary and totals display correctly | User has at least two items in cart with known prices, Tax rules are configured for the current account/location, User has completed payment and shipping information and is on the Overview step | 1. Navigate to the Checkout - Overview step<br>2. Inspect the order summary list and the totals section (Item total, Tax, Total), and payment and shipping info | Order summary lists all cart items with correct names, quantities and per-item prices; Item total equals sum of item line totals; Tax is calculated per configured tax rules; Total equals Item total plus Tax; payment and shipping information are visible and match the previously saved details | high |
| TC-065 |  | Finish completes the order and navigates to confirmation page | User is on Checkout - Overview with valid payment and shipping information displayed, Backend order creation service is available | 1. On the Overview step, click the 'Finish' button | The system creates the order and navigates to the order confirmation page showing order number, summary, and success message; Overview is no longer shown and cart is cleared or updated | high |
| TC-066 |  | Cancel exits checkout and returns user to cart | User is on Checkout - Overview step | 1. Click the 'Cancel' button on the Overview step | Checkout flow is exited and the user is navigated back to the cart page (or previously configured page); no order is created | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Finish blocked when payment information is missing or invalid | User has items in cart and is on Overview, Payment information is missing or marked invalid in the Overview (e.g., expired card) | 1. On the Overview step, attempt to click 'Finish' | The system prevents order completion, displays a clear validation error or inline message indicating missing/invalid payment information, and stays on the Overview step | high |
| TC-068 |  | Finish blocked when shipping information is missing | User has items in cart and is on Overview, Shipping address is missing or incomplete in the Overview | 1. Click the 'Finish' button | The system prevents completion, shows an error/instruction to provide shipping information, and remains on the Overview step | high |
| TC-073 |  | Prevent duplicate orders when Finish is clicked multiple times rapidly | User is on Overview with valid payment and shipping information, Order creation endpoint processes single request per order by expected behavior | 1. Rapidly click the 'Finish' button twice or more<br>2. Observe button state and result | The UI disables the Finish button or shows a processing indicator after first click; only one order is created and the confirmation page is displayed once; no duplicate order confirmations appear | high |
| TC-074 |  | Server/network error when finishing shows an error and allows retry | User is on Overview with valid payment and shipping information, Simulate server/network failure (e.g., 500 or timeout) when creating the order | 1. Click the 'Finish' button<br>2. Simulate server returning an error or a network timeout | Overview shows a clear error message (e.g., 'Unable to complete your order, please try again'), the user remains on Overview with Finish enabled for retry or a Retry option is presented; no confirmation page is shown and no order is created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-069 |  | Overview handling for empty cart (zero items) | User has an empty cart or cart was emptied after navigation and user navigates to Overview (direct URL or back button) | 1. Open the Checkout - Overview step with an empty cart | Overview displays a clear 'cart is empty' message or redirects the user back to the cart page; 'Finish' is disabled or not available and no order can be placed | medium |
| TC-070 |  | Large totals and quantities render correctly and do not overflow | Cart contains items with very large quantities and/or prices producing very large totals, User is on Overview | 1. Navigate to the Overview step<br>2. Inspect the totals and UI layout (Item total, Tax, Total) and ensure no UI breakage | UI displays large numeric values correctly (correct formatting and currency symbol), no overflow or layout break occurs, and totals are accurate according to calculations | medium |
| TC-071 |  | Tax rounding boundary values display correctly | Cart contains items priced to create tax amounts that require rounding (e.g., fractional cents), Tax rounding rules are known (e.g., round to 2 decimal places), User is on Overview | 1. Open the Overview step<br>2. Verify the tax and total values and rounding behavior | Tax and Total are displayed rounded according to configured business rules (e.g., two decimal places) and the displayed Item total + displayed Tax equals displayed Total after rounding | medium |
| TC-072 |  | Very long shipping address and cardholder name display without UI break | User has a shipping address and cardholder name that exceed typical lengths (long strings) and is on Overview | 1. Navigate to the Overview step<br>2. Inspect how shipping and payment fields render with long text | Long text wraps or truncates per design (no overlapping of other UI elements), all information remains readable or accessible (e.g., tooltip or expand), and layout remains usable | low |
| TC-075 |  | Zero-price items or discounts resulting in zero total can be completed | Cart items and applied discounts result in Item total = 0 and Tax = 0, User is on Overview with payment and shipping information present | 1. Review the Overview totals showing zero amounts<br>2. Click the 'Finish' button | The system allows order completion even when total is zero, navigates to confirmation page showing order details and total 0.00, and no payment processing is attempted | medium |

---

## Checkout - Confirmation

Total: **10** (positive: 4, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-076 |  | Confirmation page displays success message after checkout | User is logged in (if required), User has items in cart, User completes checkout flow successfully (payment accepted) | 1. Complete the checkout flow and allow redirection to the confirmation page<br>2. Observe the content of the confirmation page | A visible success message is displayed (e.g. "Thank you for your order!") and order summary/order number is present on the confirmation page | high |
| TC-077 |  | Back Home button returns to Product Inventory and clears cart | User completed checkout and is on the confirmation page, Cart had one or more items prior to checkout | 1. Click the "Back Home" button on the confirmation page<br>2. Verify the destination page and the cart state | User is redirected to the Product Inventory page and the shopping cart is empty (cart count = 0 or cart message shows empty) | high |
| TC-078 |  | Back Home button operable via keyboard (accessibility) | User completed checkout and is on the confirmation page, Keyboard navigation is enabled | 1. Use Tab/Shift+Tab to focus the "Back Home" button<br>2. Press Enter or Space to activate the button | Activation via keyboard navigates the user to the Product Inventory and the cart is cleared | medium |
| TC-079 |  | Confirmation message persists after page refresh | User completed checkout and landed on the confirmation page | 1. Refresh the confirmation page using browser refresh<br>2. Observe whether the success message and order details are still displayed | Success message (and order details, if applicable) remain visible after refresh and no cart items are present | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-083 |  | Direct access to confirmation page without completing checkout is rejected/redirected | User has not completed checkout, User is not currently in a post-checkout session | 1. Manually enter the confirmation page URL in the browser address bar<br>2. Press Enter to navigate to that URL | System does not show a valid order confirmation; user is redirected to Product Inventory (or shown an informative error/redirect) and cart remains unchanged | high |
| TC-084 |  | Server error prevents clearing cart when clicking Back Home | User completed checkout and is on the confirmation page, Simulate server-side failure for the cart-clear endpoint (e.g., HTTP 500) | 1. Click the "Back Home" button while the cart-clear endpoint is failing<br>2. Observe navigation and any error messages | User remains on the confirmation page (or is shown an error state) and an appropriate error message/notification is displayed indicating cart could not be cleared; cart retains previous items until resolved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-080 |  | Multiple rapid clicks on Back Home do not cause duplicate navigation or errors | User is on confirmation page after a successful checkout | 1. Rapidly click the "Back Home" button multiple times (e.g., 3-5 clicks)<br>2. Observe navigation behavior and application state | Application performs a single navigation to Product Inventory without errors or duplicate requests, and the cart is cleared | medium |
| TC-081 |  | Back Home clears very large cart (stress) | User had a very large number of items in cart (e.g., 100+ or configured system limit) and completed checkout, User is on confirmation page | 1. Click the "Back Home" button<br>2. Verify Product Inventory loads and check cart count/state | Product Inventory loads and the cart is cleared (cart count = 0) without timeouts or errors | medium |
| TC-082 |  | Browser back after returning Home does not restore cleared cart | User completed checkout and clicked "Back Home" to return to Product Inventory, Cart is confirmed cleared | 1. From Product Inventory (after Back Home), press the browser back button<br>2. Observe the page and cart state | User navigates back to the confirmation page (or previous history entry) but the shopping cart remains cleared (cart count = 0) | medium |
| TC-085 |  | Empty or missing success message falls back to default confirmation text | User completed checkout, Server returns an empty or null success message string for the confirmation page | 1. Load the confirmation page when the server provides an empty success message<br>2. Observe the displayed confirmation text | UI displays a sensible fallback confirmation message (e.g., generic "Order placed" or default "Thank you for your order!") so user still receives confirmation, and Back Home remains available | low |

---

## Logout

Total: **10** (positive: 3, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-086 |  | Standard logout from protected page | User is logged in, User is on a protected page (e.g., Inventory) | 1. Click the application menu or user avatar (where logout is shown)<br>2. Click 'Logout' (or equivalent) from the menu | User is returned to the login page, session is ended, and protected pages require login again | high |
| TC-087 |  | Attempt to open protected URL after logout | User is logged in, User has just logged out (completed LOG-001) | 1. In the browser address bar enter the URL of a protected page (e.g., /inventory or /checkout)<br>2. Press Enter to navigate | User is redirected to the login page (or shown login screen) and cannot access the protected content without logging in | high |
| TC-088 |  | Re-login after logout | User has logged out and is on the login page | 1. Enter valid username and password on the login page<br>2. Click 'Login' (or submit credentials) | User is successfully logged in again and granted access to protected pages | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-089 |  | Trigger logout while not logged in | User is not logged in (on login page) | 1. Attempt to navigate directly to the logout endpoint (e.g., /logout) or click a logout link if present on login page<br>2. Observe application response | Application stays on (or returns to) the login page and does not crash; an informative message may be shown (e.g., 'Not logged in' or silent redirect to login) | medium |
| TC-090 |  | Network/server error during logout | User is logged in, Network can be simulated as failing or server returns error | 1. Simulate network failure or configure server to return error for logout request<br>2. Click 'Logout'<br>3. Observe UI behavior and any error messages | Application shows a clear error message indicating logout failed (or network error); session state is handled gracefully (no client crash). User may remain logged in until logout succeeds | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-091 |  | Use browser back button after logout to access protected page | User is logged in and viewing a protected page, User has just logged out (completed LOG-001) | 1. After logout, click the browser back button to return to the previously viewed protected page<br>2. Observe whether the protected content is displayed or access is blocked | Protected content is not accessible. The application either redirects to the login page or shows a non-authenticated view; sensitive data is not available from cache | high |
| TC-092 |  | Logout in one tab invalidates session in other open tabs | User is logged in in two separate browser tabs (Tab A and Tab B) | 1. In Tab A, perform logout<br>2. Switch to Tab B and attempt to navigate or interact with a protected page (refresh inventory or click to access cart/checkout) | Tab B is treated as logged out: attempts to access protected pages redirect to login (no protected content visible) without requiring manual logout in Tab B | high |
| TC-093 |  | Verify session token/cookie and local storage cleared after logout | User is logged in, Browser developer tools available to inspect cookies and storage | 1. Inspect session cookie/localStorage/sessionStorage while logged in and note session identifiers<br>2. Perform logout<br>3. Re-inspect cookies and storage | Session cookie and any client-side session tokens are removed or invalidated after logout; no usable session identifiers remain client-side | medium |
| TC-094 |  | Repeated/double-click logout action | User is logged in and logout button/menu is available | 1. Rapidly click 'Logout' twice (or click logout, then click again immediately)<br>2. Observe UI response and error messages | Action is idempotent: user ends up on login page without errors or duplicate failures; no broken UI state | low |
| TC-095 |  | Submit protected POST action (checkout) after logout | User was logged in and had a prepared checkout POST payload, User has logged out | 1. After logout, attempt to submit the checkout POST request (e.g., via a saved form or REST client) to the checkout endpoint<br>2. Observe server response and client redirect behavior | Server rejects the request or responds with an authentication required status; client is redirected to login page and checkout action is not performed | medium |

---

## Reset App State

Total: **10** (positive: 3, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-096 |  | Reset clears cart after adding a single item and preserves login | User is logged in, Product A is available, Cart is initially empty | 1. Navigate to Product A page<br>2. Tap 'Add to cart' for Product A<br>3. Verify cart badge shows 1 and cart contains Product A<br>4. Open app menu and tap 'Reset App State'<br>5. Confirm reset if a confirmation dialog appears | Cart is empty, cart badge is cleared or shows 0, Product A's add button is back to 'Add' state, user remains logged in (still sees user profile/name) | high |
| TC-097 |  | Reset clears multiple items and restores add/remove button states across product list | User is logged in, Cart contains multiple items (at least 3) added from product list, On product list screen some 'Remove'/'Added' button states are active | 1. Open product list and verify some items show 'Added' or 'Remove' state<br>2. Open cart and verify it contains the multiple items and cart badge count is correct<br>3. Tap 'Reset App State' from app menu<br>4. If confirmation appears, confirm the reset<br>5. Return to product list | Cart is empty, cart badge cleared/hidden, all product list buttons show default 'Add' state (no 'Added' or 'Remove' states), user still logged in | high |
| TC-098 |  | Reset while on checkout page clears cart and shows empty cart/checkout message | User is logged in, User is on checkout page with items in cart | 1. On checkout page verify items and totals are present<br>2. Tap 'Reset App State' (via menu or settings)<br>3. Confirm reset if prompted<br>4. Observe checkout/cart page content after reset | Checkout shows an empty cart message or redirect to empty cart screen, totals reset to zero, cart badge cleared, user remains logged in | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-100 |  | Reset fails due to server error (simulate HTTP 500) and shows error message | User is logged in, Cart contains items, Backend reset API is simulated to return 500 Internal Server Error | 1. Open cart and verify items exist and badge shows correct count<br>2. Tap 'Reset App State'<br>3. Observe error handling and any displayed messages | App displays an appropriate error message (e.g. 'Unable to reset app state. Please try again.'), cart and UI states remain unchanged (items still present, add/remove button states unchanged), user remains logged in | high |
| TC-101 |  | Reset attempted with expired/invalid session is rejected and prompts re-login | User session is expired or invalidated server-side (simulate expiration), Cart contains items | 1. Attempt to tap 'Reset App State'<br>2. Observe app response and any redirect to authentication | App rejects reset due to unauthorized session and prompts the user to re-login (error message or redirect to login). Cart state should remain unchanged or be handled consistently; user is not silently logged out without notice | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-099 |  | Reset when cart is already empty does not produce error | User is logged in, Cart is already empty | 1. Verify cart is empty and cart badge is hidden or shows 0<br>2. Tap 'Reset App State'<br>3. Confirm reset if prompted | No error is shown, UI remains stable (cart still empty, badge remains hidden/0), and user remains logged in | low |
| TC-102 |  | Rapid repeated taps on Reset App State (double/triple click) are idempotent and do not corrupt state | User is logged in, Cart contains items, Reset control is visible | 1. While on main screen, rapidly tap the 'Reset App State' control multiple times in quick succession<br>2. Observe UI behavior during and after the taps | Only one reset action is applied (or actions are safely serialized). No duplicate errors, no partial clears; final state is cart empty, badge cleared, add buttons reset, and user remains logged in | high |
| TC-103 |  | Reset with very large cart (stress test) completes and restores UI | User is logged in, Cart contains a large number of items (e.g. 200-1000 items) | 1. Verify cart shows the large item count and performance baseline<br>2. Tap 'Reset App State' and confirm if necessary<br>3. Measure time to completion and observe UI responsiveness | Reset completes successfully within acceptable time (no app crash), cart becomes empty, badge cleared, product buttons reset, and user remains logged in; app remains responsive | medium |
| TC-104 |  | Reset while device is offline (no network) is handled gracefully | User is logged in, Cart contains items, Device is offline (airplane mode or disabled network) | 1. Verify device has no network connectivity<br>2. Tap 'Reset App State'<br>3. Observe app behavior, messages shown, and final UI state | App displays an appropriate offline/network error or queues the reset action per design. There should be no silent data loss; cart either remains unchanged with an error message or local UI is updated with clear feedback. User is not logged out | medium |
| TC-105 |  | Reset invoked while an add/remove operation is in progress resolves to a consistent final state | User is logged in, An add or remove operation is artificially delayed (simulate slow network), Cart has at least one item | 1. Start adding or removing an item and ensure the operation is in pending state (e.g. spinner shown)<br>2. While operation is pending, tap 'Reset App State'<br>3. Wait for pending operations to complete or timeout and observe the final state | Final state is consistent: either pending operation is canceled and cart is cleared, or operation completes and system still ends up with an empty cart. No partial UI states remain (no stuck spinners or incorrect add/remove labels). User remains logged in | low |

---
