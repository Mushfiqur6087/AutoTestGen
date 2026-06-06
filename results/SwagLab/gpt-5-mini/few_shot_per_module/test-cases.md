# Test Cases — SwagLab

Generated: 2026-06-04T14:54:22.091692Z  
Model: gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 82 | 30 | 25 | 27 | 41 | 35 | 6 |

## Login

Total: **12** (positive: 3, negative: 6, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with standard_user | User is on the Swag Labs login page, Network connection available | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is authenticated and redirected to the Product Inventory page; Inventory page elements (product list, header, and cart icon) are visible | high |
| TC-002 |  | Successful login with problem_user | User is on the Swag Labs login page, Network connection available | 1. Enter 'problem_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is authenticated and redirected to the Product Inventory page; page loads and product list is displayed (note: product images or behavior may be intentionally problematic but login succeeds) | high |
| TC-003 |  | Successful login with visual_user | User is on the Swag Labs login page, Network connection available | 1. Enter 'visual_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is authenticated and redirected to the Product Inventory page; login succeeds though visual differences may be present for this user | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt to log in with locked_out_user | User is on the Swag Labs login page | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Sorry, this user has been locked out.'; the user remains on the login page | high |
| TC-005 |  | Attempt to log in with invalid username and/or password | User is on the Swag Labs login page | 1. Enter 'invalid_user' in the Username field<br>2. Enter 'wrong_password' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username and password do not match any user in this service.'; the user remains on the login page | high |
| TC-006 |  | Attempt to log in with missing username | User is on the Swag Labs login page | 1. Leave the Username field empty<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username is required.'; the user remains on the login page | high |
| TC-007 |  | Attempt to log in with missing password | User is on the Swag Labs login page | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field empty<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Password is required.'; the user remains on the login page | high |
| TC-008 |  | Attempt to log in with both username and password empty | User is on the Swag Labs login page | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Login | An error banner is displayed indicating required credentials (e.g., 'Epic sadface: Username is required.' or combined validation); the user remains on the login page | high |
| TC-009 |  | Attempt SQL injection or special characters in username and password fields | User is on the Swag Labs login page | 1. Enter "' OR '1'='1" in the Username field<br>2. Enter "' OR '1'='1" in the Password field<br>3. Click Login | Login is rejected; an error banner displays 'Epic sadface: Username and password do not match any user in this service.' (no unauthorized access granted) | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Login with performance_glitch_user (verify eventual success despite delay) | User is on the Swag Labs login page, Network connection available | 1. Enter 'performance_glitch_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login and observe response time | The application may respond slowly, but the user is eventually authenticated and redirected to the Product Inventory page; no functional failure occurs due to delay | medium |
| TC-011 |  | Login attempt using username with leading and trailing whitespace | User is on the Swag Labs login page | 1. Enter ' standard_user ' (with leading and trailing spaces) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | If the system trims input, the user is authenticated and redirected to the Product Inventory page; if not, an error banner displays 'Epic sadface: Username and password do not match any user in this service.'; tester should document actual behavior | medium |
| TC-012 |  | Login attempt with a very long username (boundary test) | User is on the Swag Labs login page | 1. Enter a very long username (e.g., 500 characters) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | Login is rejected with an appropriate error (e.g., 'Epic sadface: Username and password do not match any user in this service.') or an input validation message; application does not crash | medium |

---

## Product Inventory

Total: **12** (positive: 7, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Add a single product to the cart updates button and cart badge | User logged in as standard_user, Product Inventory page is displayed, Cart is empty | 1. On the Product Inventory page, locate a product (e.g., 'Sauce Labs Backpack')<br>2. Click the product's 'Add to cart' button | The product's button text changes to 'Remove'; the cart badge appears with count '1'; the product remains listed on the inventory page | high |
| TC-014 |  | Remove a product from the cart updates button and cart badge | User logged in as standard_user, Product Inventory page is displayed, At least one product has been added to the cart (cart badge shows >=1) | 1. On the Product Inventory page, locate a product with button 'Remove'<br>2. Click the product's 'Remove' button | The product's button text changes back to 'Add to cart'; the cart badge decrements by 1 (or disappears if count becomes 0) | high |
| TC-015 |  | Open Product Detail page by clicking product name | User logged in as standard_user, Product Inventory page is displayed | 1. On the Product Inventory page, click the name/title of a product<br>2. Observe navigation to the Product Detail page | The Product Detail page opens for the selected product and displays the correct product name, description, and price | high |
| TC-016 |  | Open Product Detail page by clicking product image | User logged in as standard_user, Product Inventory page is displayed | 1. On the Product Inventory page, click the image of a product<br>2. Observe navigation to the Product Detail page | The Product Detail page opens for the selected product and displays the correct product name, description, and price | medium |
| TC-017 |  | Sort products by Name (A–Z) displays ascending alphabetical order | User logged in as standard_user, Product Inventory page is displayed with multiple products | 1. Open the sort dropdown on the Product Inventory page<br>2. Select 'Name (A to Z)' or equivalent option<br>3. Observe the order of product names in the list | Products are displayed in ascending alphabetical order by product name (A–Z); product entries still show name, description, price, and 'Add to cart' button | high |
| TC-018 |  | Sort products by Name (Z–A) displays descending alphabetical order | User logged in as standard_user, Product Inventory page is displayed with multiple products | 1. Open the sort dropdown on the Product Inventory page<br>2. Select 'Name (Z to A)' or equivalent option<br>3. Observe the order of product names in the list | Products are displayed in descending alphabetical order by product name (Z–A) | medium |
| TC-019 |  | Sort products by Price (low–high and high–low) displays correct numeric order | User logged in as standard_user, Product Inventory page is displayed with products having varying prices | 1. Open the sort dropdown and select 'Price (low to high)'<br>2. Verify the products are ordered from lowest price to highest price<br>3. Open the sort dropdown and select 'Price (high to low)'<br>4. Verify the products are ordered from highest price to lowest price | Products reorder correctly for both price sort options; prices are displayed and numeric ordering is correct | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 |  | Attempt to access Product Inventory page without being logged in | User is logged out, Browser is at application base URL or direct inventory URL | 1. Navigate directly to the Product Inventory page URL or refresh the page while logged out<br>2. Observe the resulting page or redirection | User is redirected to the Login page (or shown an authentication required message) and cannot see the Product Inventory; no 'Add to cart' buttons or cart badge are accessible | high |
| TC-024 |  | Select an invalid sort option (manipulated/unsupported) and verify system handles it gracefully | User logged in as standard_user, Product Inventory page is displayed | 1. Using developer tools or an automated script, set the sort dropdown value to an unsupported/invalid option (e.g., 'unknown') and trigger the change event<br>2. Observe the product list and any error messages | The application does not crash or expose raw errors; it either ignores the invalid sort and retains the previous/default order or falls back to a documented default sort; no visible error stack traces are shown to the user | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Add all available products to the cart and verify cart badge and button states | User logged in as standard_user, Product Inventory page is displayed, Cart is empty | 1. On the Product Inventory page, click 'Add to cart' for every product listed<br>2. Observe the cart badge after adding all items<br>3. Verify the state of each product's add/remove button | Cart badge count equals the total number of products listed; every product's button text is 'Remove'; inventory still displays product details | medium |
| TC-021 |  | Rapidly toggle Add to cart and Remove for a product and verify final state | User logged in as standard_user, Product Inventory page is displayed, Cart is empty | 1. On the Product Inventory page, pick a product and click 'Add to cart' then immediately click 'Remove', repeat multiple times rapidly<br>2. After the rapid toggles, inspect the product's button text and the cart badge count | After rapid toggling, the product button shows the final correct state ('Add to cart' if removed, 'Remove' if added) and the cart badge accurately reflects the final number of items (no negative counts or duplicate increments) | medium |
| TC-022 |  | Sort behavior when multiple products have identical names or identical prices | User logged in as standard_user, Product Inventory page is displayed with at least two products sharing the same name or same price | 1. On the Product Inventory page, apply 'Name (A to Z)' and observe items with identical names<br>2. Apply 'Price (low to high)' and observe items with identical prices<br>3. Note the relative ordering of items that have identical sort keys | Products with identical sort keys remain in a consistent order (stable sort) or follow the application's documented secondary sort rule; no products are lost or duplicated | low |

---

## Product Detail

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Open Product Detail and verify UI elements | User logged in as standard_user, From Product Inventory, at least one product is visible | 1. From the Product Inventory page, click a product name or image to open its Product Detail page<br>2. Observe the product image, name, description, and price<br>3. Observe the Add to cart / Remove button state<br>4. Observe the Back to products button and the cart icon in the header | Product image, name, description, and price are displayed; Add to cart (or Remove if already in cart) button is present; Back to products button and cart icon are visible and enabled | high |
| TC-026 |  | Add product to cart from Product Detail | User logged in as standard_user, Selected product is not in the cart, User is on that product's Product Detail page | 1. On the Product Detail page click the 'Add to cart' button<br>2. Observe the button text/state after the click<br>3. Observe the cart badge in the header | Button text changes from 'Add to cart' to 'Remove'; cart badge increments by 1 and reflects the new cart count; product can be seen in the Shopping Cart page | high |
| TC-027 |  | Remove product from cart from Product Detail | User logged in as standard_user, Selected product is already in the cart, User is on that product's Product Detail page | 1. On the Product Detail page click the 'Remove' button<br>2. Observe the button text/state after the click<br>3. Observe the cart badge in the header | Button text changes from 'Remove' to 'Add to cart'; cart badge decrements by 1 (or disappears if count becomes 0); product is removed from the Shopping Cart page | high |
| TC-028 |  | Navigate back to Product Inventory and to Shopping Cart from Product Detail | User logged in as standard_user, User is on any Product Detail page | 1. Click 'Back to products' on the Product Detail page<br>2. From Product Inventory, click the cart icon in the header | Clicking 'Back to products' returns user to the Product Inventory page; clicking the cart icon navigates to the Shopping Cart page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Open Product Detail with an invalid/non-existent product ID in the URL | User logged in as standard_user or on login page, User can edit the browser URL | 1. Manually modify the browser URL to reference a non-existent product id (e.g. /inventory-item.html?id=9999) and press Enter<br>2. Observe the behavior of the application | Application shows an error message or redirects to the Product Inventory page; Product Detail content is not shown for the invalid id and no broken/empty UI is presented | high |
| TC-030 |  | Product Detail fails to load due to server/network error | User logged in as standard_user, User is on Product Inventory page | 1. Simulate a server or network error for the product detail API (e.g. block request or return 500)<br>2. Click a product to open its Product Detail page<br>3. Observe any error UI presented | An informative error message is displayed (e.g. 'Failed to load product details'); user remains on a recoverable state (option to retry or navigate back to products) and the UI does not crash | medium |
| TC-031 |  | Attempt to add to cart while offline | User logged in as standard_user, User is on a Product Detail page, Browser can be set to offline mode | 1. Turn the browser/network to offline mode<br>2. Click the 'Add to cart' button on the Product Detail page<br>3. Observe the result and any user-facing error or retry option | Operation fails gracefully with an error or offline indicator; the UI displays a message such as 'Unable to update cart while offline' and the local button state does not incorrectly indicate success | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Open Product Detail for a product already in the cart and verify initial state | User logged in as standard_user, Product A has already been added to the cart from another page | 1. From Product Inventory click to open Product A's Product Detail page<br>2. Observe the Add to cart / Remove button and the cart badge | Product Detail shows the button as 'Remove' (reflecting that the item is in the cart); cart badge count matches the number of items in the cart | medium |
| TC-033 |  | Rapidly toggle Add to cart and Remove to check UI and cart count consistency | User logged in as standard_user, User is on a Product Detail page, Network is responsive | 1. Repeatedly click 'Add to cart' then 'Remove' on the Product Detail page several times in quick succession (e.g. 5-10 toggles)<br>2. After toggling, navigate to the Shopping Cart and refresh Product Detail page<br>3. Observe the final button state and cart badge/count | Final button state and cart badge accurately reflect the true cart contents (no duplicate entries or stale counts); application remains stable with no UI glitches | medium |
| TC-034 |  | Display product with extremely long name and description | User logged in as standard_user, Test product exists with an extremely long name and description (very long strings) | 1. From Product Inventory click the test product with long text to open Product Detail<br>2. Observe layout, wrapping, scroll behavior, and visibility of Add to cart and Back to products controls | Long name and description wrap or scroll without breaking layout; Add to cart, Back to products and cart icon remain visible and usable; no overflow causes controls to become inaccessible | low |

---

## Shopping Cart

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-035 |  | Remove a single item from the cart | User logged in as standard_user, At least one product has been added to the cart | 1. Click the shopping cart icon to navigate to the Shopping Cart page<br>2. Locate an item listed in the cart and click its 'Remove' button | The selected item is removed from the Shopping Cart list; the cart badge in the header decreases by one (or disappears if no items remain); the removed item's entry (description and quantity) is no longer visible | high |
| TC-036 |  | Return to Product Inventory using Continue Shopping | User logged in as standard_user, Cart contains one or more items | 1. From the Shopping Cart page, click the 'Continue Shopping' button<br>2. Observe the destination page | The application navigates to the Product Inventory page (header/title shows 'Products'); the cart badge remains visible in the header reflecting current cart count | high |
| TC-037 |  | Begin checkout from Shopping Cart | User logged in as standard_user, Cart contains one or more items | 1. From the Shopping Cart page, click the 'Checkout' button<br>2. Observe the next page | The user is navigated to the Checkout: Your Information page (checkout flow begins) and the cart contents are shown on the following overview step | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Attempt to start checkout with an empty cart | User logged in as standard_user, Cart is empty | 1. Navigate to the Shopping Cart page<br>2. Click the 'Checkout' button | Checkout is not completed: either the Checkout button is disabled or the application remains on the Shopping Cart page and displays an appropriate message (for example, 'Your cart is empty') indicating checkout cannot proceed | high |
| TC-039 |  | Access the Shopping Cart page without being logged in | User is logged out | 1. Attempt to navigate directly to the Shopping Cart page URL or click a cart link while logged out | The application redirects to the Login page (or shows a login prompt) and does not display cart items; user must authenticate before accessing the Shopping Cart | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Add all available products, verify each cart entry shows quantity 1 and has 'Remove' button | User logged in as standard_user, Cart is empty, Multiple products available in inventory | 1. On the Product Inventory page, click 'Add to cart' for every product listed<br>2. Click the shopping cart icon to open the Shopping Cart page<br>3. Inspect each item row for quantity and the presence of a 'Remove' button<br>4. Observe the cart badge count in the header | Every product added appears in the Shopping Cart as a separate line item with quantity displayed as '1' and a 'Remove' button; the cart badge count equals the number of products added; all 'Add to cart' buttons on the inventory have changed to 'Remove' | medium |
| TC-041 |  | Remove the last item and verify empty cart state and badge disappearance | User logged in as standard_user, Cart contains exactly one item | 1. Navigate to the Shopping Cart page<br>2. Click 'Remove' for the only item in the cart<br>3. Observe the Shopping Cart page and header cart badge | The cart list shows no items (empty state); the cart badge in the header disappears or is not shown (count zero); UI does not display leftover item entries or 'Remove' buttons | medium |
| TC-042 |  | Rapidly remove multiple items to verify UI consistency and count synchronization | User logged in as standard_user, Cart contains multiple items | 1. Open the Shopping Cart page<br>2. Rapidly click 'Remove' on several different items in quick succession (one after another)<br>3. Observe the cart list and cart badge after each removal | UI remains responsive; each removed item disappears from the list; the cart badge count updates accurately after each removal without temporary duplication or negative counts; no JavaScript errors are shown to the user | medium |

---

## Checkout - Information

Total: **8** (positive: 3, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Enter valid First Name, Last Name, Postal Code and continue to Overview | User logged in as standard_user, At least one product has been added to the cart, User is on the Checkout: Your Information page | 1. In the First Name field enter 'John'<br>2. In the Last Name field enter 'Doe'<br>3. In the Postal Code field enter '90210'<br>4. Click Continue | User is navigated to the Checkout: Overview page; order summary and item list are displayed; no error banner is shown | high |
| TC-044 |  | Click Cancel returns user to the Shopping Cart | User logged in as standard_user, At least one product has been added to the cart, User is on the Checkout: Your Information page | 1. Click Cancel on the Checkout: Your Information page | User is returned to the Shopping Cart page; cart contents remain unchanged; no Checkout error banner is shown | medium |
| TC-045 |  | Accept names with hyphen/apostrophe and postal code with hyphen | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. In the First Name field enter 'Anne-Marie'<br>2. In the Last Name field enter "O'Connor"<br>3. In the Postal Code field enter '12345-6789'<br>4. Click Continue | User is navigated to the Checkout: Overview page; entered name and postal code are accepted and displayed on the Overview summary; no error banner is shown | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Submit form with First Name missing | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. Leave First Name empty<br>2. In the Last Name field enter 'Doe'<br>3. In the Postal Code field enter '90210'<br>4. Click Continue | An error banner is displayed with the message 'Error: First Name is required'; the user remains on the Checkout: Your Information page | high |
| TC-047 |  | Submit form with Last Name missing | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. In the First Name field enter 'John'<br>2. Leave Last Name empty<br>3. In the Postal Code field enter '90210'<br>4. Click Continue | An error banner is displayed with the message 'Error: Last Name is required'; the user remains on the Checkout: Your Information page | high |
| TC-048 |  | Submit form with Postal Code missing | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. In the First Name field enter 'John'<br>2. In the Last Name field enter 'Doe'<br>3. Leave Postal Code empty<br>4. Click Continue | An error banner is displayed with the message 'Error: Postal Code is required'; the user remains on the Checkout: Your Information page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Enter very long values in all fields (boundary length) | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. In the First Name field enter a 256-character string (e.g. 'A' repeated 256 times)<br>2. In the Last Name field enter a 256-character string<br>3. In the Postal Code field enter a 50-character string<br>4. Click Continue | The application accepts or reliably handles the long inputs without crashing; if accepted, user is navigated to the Checkout: Overview page and the entered values are preserved or appropriately truncated with no unexpected errors | medium |
| TC-050 |  | Enter only whitespace characters in fields | User logged in as standard_user, At least one product in cart, User is on the Checkout: Your Information page | 1. In the First Name field enter '   ' (spaces)<br>2. In the Last Name field enter '   ' (spaces)<br>3. In the Postal Code field enter '   ' (spaces)<br>4. Click Continue | Whitespace-only input is treated as missing input; an error banner is displayed (at minimum 'Error: First Name is required') and the user remains on the Checkout: Your Information page | medium |

---

## Checkout - Overview

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-051 |  | Complete order from Overview by clicking Finish | User logged in as standard_user, At least one product is in the cart, User has completed Checkout: Information step (first name, last name, zip provided), User is on the Checkout: Overview page | 1. Review the list of items and totals shown on the Overview page<br>2. Confirm payment and shipping information displayed are correct<br>3. Click the Finish button | The app navigates to the confirmation page showing 'Thank you for your order!'; the shopping cart badge is cleared (no items shown); order summary/receipt is displayed on the confirmation page | high |
| TC-052 |  | Exit checkout from Overview using Cancel | User logged in, One or more products in the cart, User is on the Checkout: Overview page | 1. Click the Cancel button on the Overview page | The app exits the checkout flow and navigates back to the Shopping Cart page; all items remain in the cart and quantities are unchanged | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-053 |  | Finish fails when server returns an order submission error | User logged in, Cart contains one or more items, User is on the Checkout: Overview page, Order submission API is mocked or forced to return an error (e.g., 500 response) | 1. Click the Finish button on the Overview page while the backend is returning an error | An error message/banner is displayed indicating the order could not be completed (e.g., 'Order submission failed. Please try again.'); the user remains on the Overview page and cart contents are not cleared | high |
| TC-054 |  | Attempt to complete checkout from Overview with an empty cart | User logged in, Cart is empty (user navigated to Overview URL or manipulated flow to reach Overview with empty cart), User is on the Checkout: Overview page | 1. Confirm the Items list on the Overview page shows no products<br>2. Click the Finish button | The system prevents order completion, displays an error message such as 'Your cart is empty' or redirects user back to the Shopping Cart page; no confirmation page is shown and no order is created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Add all available products to cart and verify totals and cart badge on Overview | User logged in as standard_user, Cart is empty | 1. On the Product Inventory page, click 'Add to cart' for every product available<br>2. Click the cart icon and proceed through Checkout: Information step with valid data<br>3. On the Checkout: Overview page, note the item total, tax, and total<br>4. Verify the cart badge count in the header equals the number of products added | Cart badge equals the total number of products added; Overview page lists every product added; Item total equals the sum of each product price; Tax is calculated correctly from Item total and Total equals Item total plus Tax; all product action buttons in inventory changed to 'Remove' previously | medium |
| TC-056 |  | Display long payment and shipping information on Overview (text wrapping/truncation) | User logged in, At least one product in cart, User completes Checkout: Information step using very long strings for first name, last name, and postal code fields (extremely long names/addresses) | 1. Proceed to Checkout: Overview page after submitting long payment and shipping information<br>2. Observe how the payment and shipping information is rendered on the Overview page | Long payment and shipping fields are displayed without breaking layout (text either wraps or is truncated with ellipsis according to UI spec); no overlapping UI elements or horizontal scrolling is introduced and the Finish/Cancel buttons remain visible and usable | medium |
| TC-057 |  | Verify totals and rounding when item prices produce fractional tax amounts | User logged in, Cart contains items with prices that when summed produce tax requiring rounding (e.g., prices that lead to fractional cents) | 1. Proceed through Checkout to the Overview page<br>2. Note the Item total, Tax amount, and Total amount<br>3. Calculate expected Tax and Total using the configured tax rate and rounding rules and compare to displayed values | Displayed Tax and Total match the expected values according to the application's rounding rules (no off-by-one-cent errors); Item total equals sum of item prices | low |

---

## Checkout - Confirmation

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | Display success message and Back Home clears cart after completing checkout | User logged in as standard_user, At least one product in the cart, User has completed Checkout Information and is on the Overview page | 1. On the Overview page, click Finish to complete the order<br>2. Observe the Confirmation page<br>3. Click the Back Home button | Confirmation page displays success message such as 'Thank you for your order!'; clicking Back Home navigates to the Product Inventory page and the cart is cleared (no cart badge visible or count = 0) | high |
| TC-059 |  | Back Home clears cart when multiple items were purchased | User logged in as standard_user, Multiple products (2 or more) were added to the cart and checkout completed to reach Confirmation page | 1. On the Confirmation page, verify the presence of the success message<br>2. Click Back Home<br>3. On the Product Inventory page, verify the cart badge and cart content | User is navigated to Product Inventory; the cart badge is no longer visible (or shows 0) and the cart contains no items | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Attempt to access Confirmation page directly without completing checkout | User logged in as standard_user, Cart may be empty or have items, but user has NOT completed the checkout flow (has not clicked Finish) | 1. Manually navigate to the Confirmation page URL (e.g., /checkout-complete.html) or click a direct link to it<br>2. Observe the resulting page | User is not shown the order confirmation for a completed purchase; the app either redirects to the Product Inventory or Checkout page (or shows an appropriate message indicating the order was not completed) and no 'Thank you for your order!' confirmation is displayed | high |
| TC-061 |  | Attempt to access Confirmation page while not logged in | User is logged out, User attempts to access the Confirmation page URL directly | 1. In a browser session where the user is not authenticated, navigate to the Confirmation page URL<br>2. Observe the resulting page or redirection | The application redirects the user to the Login page (or displays an authentication-required message); the Confirmation page and its 'Thank you for your order!' message are not displayed to unauthenticated users | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-062 |  | Refresh the Confirmation page repeatedly and verify Back Home remains functional | User logged in as standard_user, User has completed checkout and is on the Confirmation page | 1. On the Confirmation page, verify the success message is displayed<br>2. Refresh the browser page several times (e.g., 3 times), observing the message each time<br>3. After the refreshes, click Back Home | The success message persists across refreshes; clicking Back Home after refresh navigates to Product Inventory and the cart is cleared (no cart badge visible) | medium |
| TC-063 |  | Click Back Home, then use browser Back to confirm cart remains cleared | User logged in as standard_user, User completed checkout and is on the Confirmation page | 1. On the Confirmation page, click Back Home to return to Product Inventory<br>2. Verify the cart is cleared (no cart badge)<br>3. Use the browser Back button to return to the Confirmation page<br>4. Use the browser Forward button (or click Back Home again) to return to Product Inventory | After the initial Back Home click the cart is cleared; navigating back to the Confirmation page and forward again does not repopulate the cart — the cart remains empty on Product Inventory | medium |
| TC-064 |  | Click Back Home multiple times (idempotence) and verify stable behavior | User logged in as standard_user, User is on the Confirmation page after completing checkout | 1. Click Back Home once and verify navigation to Product Inventory and that the cart is cleared<br>2. On Product Inventory, click the Back Home button again if present in header or repeat navigation action multiple times<br>3. Observe application behavior | Multiple Back Home clicks (or repeated navigation to home) do not cause errors; the user remains on Product Inventory and the cart remains cleared (no items added back) | low |

---

## Logout

Total: **8** (positive: 3, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Logout from the Inventory page via the menu | User is logged in (e.g., standard_user), User is on the Product Inventory page | 1. Click the hamburger/menu button in the header<br>2. Click 'Logout' in the menu | User is returned to the Login page (login form visible); protected pages (inventory, product detail, cart, checkout) are not accessible without logging in again | high |
| TC-066 |  | Logout from a Product Detail page | User is logged in, User is viewing a product detail page | 1. On the product detail page, click the hamburger/menu button<br>2. Click 'Logout' in the menu | Application navigates to the Login page; attempting to access the product detail URL now redirects to the Login page until user logs in | high |
| TC-067 |  | Logout while on the Cart or Checkout pages | User is logged in, User is on the Shopping Cart page or Checkout Information page | 1. Click the hamburger/menu button<br>2. Click 'Logout' | User is taken to the Login page; subsequent navigation to cart or checkout pages redirects to Login until authentication occurs | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Attempt to access Inventory URL directly after logging out | User has logged out and is on the Login page | 1. In the browser address bar, navigate directly to the inventory URL (e.g., /inventory.html)<br>2. Press Enter to load the page | User is redirected to the Login page (no access to inventory); protected content is not displayed without valid authentication | high |
| TC-069 |  | Use browser Back button after logout to try to return to protected page | User was on a protected page (inventory, detail, cart or checkout) and has just clicked Logout | 1. After logout completes and the Login page is shown, click the browser Back button<br>2. Observe the page displayed | Protected content is not re-displayed; the application stays on the Login page or redirects back to Login if a protected URL is requested | high |
| TC-070 |  | Attempt an authenticated action (e.g., add-to-cart API) using a stale session token after logout | User was logged in, then performed Logout, Tester has captured the previous session cookie or token | 1. Using a REST client or browser devtools, send an API request that requires authentication (for example POST /cart/add) including the old session cookie/token<br>2. Observe the response | Server rejects the request (401/302 to login or equivalent); the action is not performed and protected APIs require a valid, current authentication | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-071 |  | Logout in one browser tab, then interact with the app in a second tab that still shows protected content | User is logged in in two browser tabs, Tab A is on Inventory, Tab B is also on Inventory or Product Detail | 1. In Tab A, open the menu and click 'Logout' to log out<br>2. Switch to Tab B (which still displays protected content) and attempt an authenticated action (e.g., click 'Add to cart' or navigate to another protected page)<br>3. Observe the behavior in Tab B | Tab B does not allow the authenticated action; it either redirects to the Login page or prompts re-authentication. Protected actions require the user to log in again. | medium |
| TC-072 |  | Rapidly click Logout multiple times (double/triple click) to verify idempotence | User is logged in, User is on any protected page featuring the menu logout option | 1. Open the menu and click 'Logout' rapidly multiple times (double/triple click)<br>2. Observe the application's response and any errors | Application remains stable and ends the session once; user lands on Login page with no error dialogs or unexpected behaviors; repeated clicks do not produce duplicate sessions or errors | low |

---

## Reset App State

Total: **10** (positive: 3, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Reset app state clears cart and resets Add/Remove buttons | User logged in as standard_user, At least two products have been added to the cart, User is on the Products (Inventory) page | 1. Click the menu (burger) icon to open the side menu<br>2. Click 'Reset App State'<br>3. Close the menu (if it does not auto-close) and observe the header and product list | Cart badge is no longer visible (or shows 0); all product 'Remove' buttons that were previously shown revert to 'Add to cart'; cart contents are cleared; the user remains logged in (still on the Inventory page) | high |
| TC-074 |  | Reset app state does not log the user out | User logged in as standard_user, Cart contains one or more items | 1. Note a visible indication that the user is logged in (e.g., menu accessible, username present if applicable)<br>2. Open the menu and click 'Reset App State'<br>3. After reset completes, attempt to access a user-only area (e.g., open Products page or open menu options) | User remains logged in and can access user-only pages; login page is not shown and session persists after reset | high |
| TC-075 |  | Reset app state while on the Checkout flow clears the cart | User logged in as standard_user, At least one item in cart, User has navigated to Checkout: Information or Overview page | 1. On the Checkout Information or Overview page, click the menu (burger) icon<br>2. Click 'Reset App State'<br>3. Return to the header and observe the cart badge and checkout page contents | Cart badge is removed or shows 0; checkout page reflects an empty cart (no items listed or item totals updated to zero); user remains logged in (not redirected to login) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-076 |  | Reset App State option is not available when user is not logged in | User is on the Swag Labs login page (not authenticated) | 1. Attempt to open the application menu (if accessible) from the login page or check the UI for 'Reset App State' option<br>2. If the menu is not present, attempt to navigate to Inventory without logging in and inspect the menu<br>3. Try to perform any action that would trigger 'Reset App State' | 'Reset App State' option is not visible or accessible when the user is not authenticated; no state reset occurs and the user remains on the login page | high |
| TC-077 |  | Reset App State fails with network/server error and shows an error message | User logged in as standard_user, Cart contains one or more items, Test environment can simulate a server or network failure | 1. Simulate a network/server error condition (e.g., disable network or mock server to return error for reset endpoint)<br>2. Open the menu and click 'Reset App State'<br>3. Observe any error message or banner and the cart state | An error banner or message is displayed indicating the reset failed (e.g., 'Could not reset app state'); the cart contents and add/remove button states remain unchanged until the operation succeeds; user remains logged in | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-078 |  | Reset App State when cart is already empty | User logged in as standard_user, Cart is empty (no cart badge displayed) | 1. Open the menu and click 'Reset App State'<br>2. Observe the header, product buttons, and any messages after the action | No errors occur; UI remains stable; cart remains empty and all product buttons show 'Add to cart'; user remains logged in | medium |
| TC-079 |  | Reset App State after adding all products (max items) to the cart | User logged in as standard_user, All available products have been added to the cart so cart badge equals total product count | 1. Verify every product shows 'Remove' and cart badge equals total number of products<br>2. Open the menu and click 'Reset App State'<br>3. Verify each product button and the cart badge | Cart badge is removed or shows 0; every product button reverts to 'Add to cart'; cart contents cleared; user remains logged in | medium |
| TC-080 |  | Quick add then reset to test race condition | User logged in as standard_user, Cart empty | 1. Rapidly click 'Add to cart' on a product<br>2. Immediately open the menu and click 'Reset App State' before any delayed UI updates complete<br>3. Observe the final cart badge and button state after UI stabilizes | After UI stabilizes, cart is cleared and the product button shows 'Add to cart'; no duplicate or ghost items remain in the cart; user remains logged in | medium |
| TC-081 |  | Reset App State for performance_glitch_user (slow UI) clears state eventually | User logged in as performance_glitch_user, At least one product in cart, Application may respond slowly | 1. Open the menu and click 'Reset App State'<br>2. Wait an extended period (accounting for slow responses) and observe the cart badge and product buttons<br>3. Verify user is still logged in | Despite slow UI performance, after the operation completes the cart badge is removed or shows 0 and product buttons revert to 'Add to cart'; user remains logged in; no partial state remains | medium |
| TC-082 |  | Reset App State for problem_user (UI inconsistencies) resets visible state | User logged in as problem_user, Cart contains items; product buttons may behave inconsistently for this user type | 1. Open the menu and click 'Reset App State'<br>2. Observe product button labels, cart badge, and any visually inconsistent elements after reset<br>3. Manually verify cart contents via the Shopping Cart page | Cart is cleared and visible state is reset (cart badge removed, products show 'Add to cart'); any UI inconsistencies do not prevent the cart from being emptied; user remains logged in | medium |

---
