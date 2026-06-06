# Test Cases — SwagLab

Generated: 2026-06-04T14:52:45.406703Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 38 | 12 | 14 | 12 | 23 | 15 | 0 |

## Login

Total: **7** (positive: 1, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Log in with valid credentials as standard_user | User is on the Swag Labs login page | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is redirected to the Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to log in with an empty username | User is on the Swag Labs login page | 1. Leave the Username field empty<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username is required.'; the user remains on the login page | high |
| TC-003 |  | Attempt to log in with an empty password | User is on the Swag Labs login page | 1. Enter 'standard_user' in the Username field<br>2. Leave the Password field empty<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Password is required.'; the user remains on the login page | high |
| TC-004 |  | Attempt to log in with invalid credentials | User is on the Swag Labs login page | 1. Enter 'invalid_user' in the Username field<br>2. Enter 'wrong_password' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username and password do not match any user in this service.'; the user remains on the login page | high |
| TC-005 |  | Attempt to log in with the locked-out user account | User is on the Swag Labs login page | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Sorry, this user has been locked out.'; the user remains on the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Log in with maximum length username and password | User is on the Swag Labs login page | 1. Enter a username with maximum allowed length (e.g., 20 characters) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click Login | User is redirected to the Product Inventory page | medium |
| TC-007 |  | Log in with minimum length username and password | User is on the Swag Labs login page | 1. Enter a single character in the Username field<br>2. Enter a single character in the Password field<br>3. Click Login | An error banner is displayed with the message 'Epic sadface: Username and password do not match any user in this service.'; the user remains on the login page | medium |

---

## Product Inventory

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Add a product to the cart and verify the cart badge count | User logged in as standard_user, Product Inventory page is displayed | 1. Click 'Add to cart' for a product<br>2. Observe the cart badge in the header | The cart badge count increases by one; the 'Add to cart' button changes to 'Remove' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to add a product to the cart when not logged in | User is on the Product Inventory page, User is not logged in | 1. Click 'Add to cart' for a product | An error message is displayed indicating that the user must log in to add items to the cart; the cart badge remains unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Sort products by price and verify the order | User logged in as standard_user, Product Inventory page is displayed with multiple products | 1. Select 'Price (low to high)' from the sort dropdown<br>2. Observe the order of products displayed<br>3. Select 'Price (high to low)' from the sort dropdown<br>4. Observe the order of products displayed | Products are displayed in ascending order when sorted by price (low to high) and in descending order when sorted by price (high to low) | medium |
| TC-011 |  | Add and remove the same product multiple times | User logged in as standard_user, Product Inventory page is displayed | 1. Click 'Add to cart' for a product<br>2. Click 'Remove' for the same product<br>3. Click 'Add to cart' for the product again<br>4. Click 'Remove' for the product again | The cart badge count reflects the correct number of items (0 after removal); the 'Add to cart' button changes to 'Remove' and back correctly | medium |

---

## Product Detail

Total: **4** (positive: 2, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Add a product to the cart from the Product Detail page | User logged in as standard_user, User is on the Product Detail page of a selected product | 1. Click the 'Add to cart' button | The button changes to 'Remove'; the cart badge count increases by 1 | high |
| TC-013 |  | Navigate back to the Product Inventory page from the Product Detail page | User is on the Product Detail page | 1. Click the 'Back to products' button | User is redirected to the Product Inventory page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Attempt to add a product to the cart when not logged in | User is on the Product Detail page of a selected product, User is not logged in | 1. Click the 'Add to cart' button | User is prompted to log in before adding the product to the cart; remains on the Product Detail page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Add a product to the cart and immediately remove it | User logged in as standard_user, User is on the Product Detail page of a selected product | 1. Click the 'Add to cart' button<br>2. Click the 'Remove' button | The button changes back to 'Add to cart'; the cart badge count decreases by 1 | medium |

---

## Shopping Cart

Total: **5** (positive: 3, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 |  | View items in the shopping cart | User logged in as standard_user, At least one product has been added to the cart | 1. Click the shopping cart icon to navigate to the Shopping Cart page | The Shopping Cart page displays the items added to the cart with their quantity, description, and 'Remove' buttons. | high |
| TC-017 |  | Remove an item from the shopping cart | User logged in as standard_user, At least one product has been added to the cart | 1. Click the shopping cart icon to navigate to the Shopping Cart page<br>2. Click the 'Remove' button for an item in the cart | The item is removed from the cart, and the cart updates to reflect the change. | high |
| TC-018 |  | Continue shopping from the shopping cart | User logged in as standard_user, At least one product has been added to the cart | 1. Click the shopping cart icon to navigate to the Shopping Cart page<br>2. Click 'Continue Shopping' | User is redirected to the Product Inventory page. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Attempt to checkout with an empty cart | User logged in as standard_user, Cart is empty | 1. Click the shopping cart icon to navigate to the Shopping Cart page<br>2. Click 'Checkout' | An error message is displayed indicating that the cart is empty; the user remains on the Shopping Cart page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Add maximum number of items to the cart and verify the display | User logged in as standard_user, Cart is empty | 1. On the Product Inventory page, add the maximum number of products available to the cart<br>2. Click the shopping cart icon to navigate to the Shopping Cart page | The Shopping Cart page displays all items added with correct quantities and 'Remove' buttons for each item. | medium |

---

## Checkout - Information

Total: **6** (positive: 1, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 |  | Successfully complete the checkout information form | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | User is navigated to the Overview page with the order summary displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 |  | Attempt to continue with missing First Name | User is on the Checkout Information page | 1. Leave the First Name field empty<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | An error banner is displayed with the message 'Error: First Name is required'; user remains on the Checkout Information page | high |
| TC-023 |  | Attempt to continue with missing Last Name | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Leave the Last Name field empty<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click Continue | An error banner is displayed with the message 'Error: Last Name is required'; user remains on the Checkout Information page | high |
| TC-024 |  | Attempt to continue with missing Zip/Postal Code | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | An error banner is displayed with the message 'Error: Postal Code is required'; user remains on the Checkout Information page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Submit the checkout information form with maximum length inputs | User is on the Checkout Information page | 1. Enter 'JohnJohnJohnJohn' in the First Name field (maximum length)<br>2. Enter 'DoeDoeDoeDoe' in the Last Name field (maximum length)<br>3. Enter '123456789' in the Zip/Postal Code field (maximum length)<br>4. Click Continue | User is navigated to the Overview page with the order summary displayed | medium |
| TC-026 |  | Submit the checkout information form with empty fields | User is on the Checkout Information page | 1. Leave the First Name field empty<br>2. Leave the Last Name field empty<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banners are displayed for all required fields; user remains on the Checkout Information page | medium |

---

## Checkout - Overview

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 |  | Complete the checkout process from the overview page | User logged in as standard_user, At least one item in the cart | 1. Review the order summary on the Overview page<br>2. Click Finish | Confirmation page displays 'Thank you for your order!'; the cart badge is no longer visible | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-028 |  | Click Cancel on the overview page | User logged in as standard_user, At least one item in the cart | 1. Review the order summary on the Overview page<br>2. Click Cancel | User is navigated back to the Shopping Cart page; no order is completed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Verify totals with maximum item quantities | User logged in as standard_user, Cart contains maximum allowable items | 1. Review the order summary on the Overview page<br>2. Verify that Item total, Tax, and Total are calculated correctly | The totals section displays accurate calculations based on maximum item quantities | medium |

---

## Checkout - Confirmation

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | View confirmation message after successful checkout | User has completed the checkout process | 1. Navigate to the confirmation page after finishing the checkout<br>2. Observe the success message displayed on the page<br>3. Click the 'Back Home' button | The confirmation message 'Thank you for your order!' is displayed; the user is redirected to the Product Inventory page and the cart is cleared | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Attempt to access confirmation page without completing checkout | User is on the Product Inventory page | 1. Try to navigate directly to the confirmation page via URL<br>2. Observe the response from the system | The user is redirected to the login page or an error message is displayed indicating that the checkout process must be completed first | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Check confirmation page after multiple rapid checkouts | User has completed multiple checkouts in quick succession | 1. Complete a checkout process<br>2. Immediately complete another checkout process<br>3. Navigate to the confirmation page after the second checkout | The confirmation message is displayed for the second checkout; the cart is cleared and the user can navigate back to the Product Inventory page without issues | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Successfully log out and return to the login page | User is logged in as standard_user | 1. Click the menu icon in the top left corner<br>2. Select 'Logout' from the menu | User is redirected to the login page; the session is ended | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Attempt to access protected pages after logout | User is logged in as standard_user, User has logged out | 1. Try to navigate to the Inventory page<br>2. Try to navigate to the Cart page<br>3. Try to navigate to the Checkout page | User is redirected to the login page for each attempt; access to protected pages is denied | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-035 |  | Log out multiple times in quick succession | User is logged in as standard_user | 1. Click the menu icon in the top left corner<br>2. Select 'Logout' from the menu<br>3. Immediately click 'Logout' again from the login page | User remains on the login page without any errors; session is still ended | medium |

---

## Reset App State

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Reset app state with items in the cart | User logged in as standard_user, At least one product has been added to the cart | 1. Click the menu icon in the top left corner<br>2. Select 'Reset App State' from the menu | The cart is cleared, the cart badge is no longer visible, and all 'Add to cart' buttons are reset to their original state | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | Attempt to reset app state when not logged in | User is on the Swag Labs main page, User is not logged in | 1. Click the menu icon in the top left corner<br>2. Select 'Reset App State' from the menu | An error message is displayed indicating that the user must be logged in to reset the app state; the app state remains unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Reset app state with an empty cart | User logged in as standard_user, Cart is empty | 1. Click the menu icon in the top left corner<br>2. Select 'Reset App State' from the menu | The app state remains unchanged; the cart badge is still not visible and all buttons remain in their default state | medium |

---
