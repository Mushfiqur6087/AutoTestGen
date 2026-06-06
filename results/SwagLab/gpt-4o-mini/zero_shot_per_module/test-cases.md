# Test Cases — SwagLab

Generated: 2026-06-04T14:52:44.780205Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 54 | 14 | 17 | 23 | 25 | 22 | 7 |

## Login

Total: **8** (positive: 1, negative: 4, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User is on the login page. | 1. Enter 'standard_user' in the Username field.<br>2. Enter 'secret_sauce' in the Password field.<br>3. Click the Login button. | User is redirected to the Product Inventory page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login attempt with empty username | User is on the login page. | 1. Leave the Username field empty.<br>2. Enter 'secret_sauce' in the Password field.<br>3. Click the Login button. | Error banner shows 'Epic sadface: Username is required.' | high |
| TC-003 |  | Login attempt with empty password | User is on the login page. | 1. Enter 'standard_user' in the Username field.<br>2. Leave the Password field empty.<br>3. Click the Login button. | Error banner shows 'Epic sadface: Password is required.' | high |
| TC-004 |  | Login attempt with invalid credentials | User is on the login page. | 1. Enter 'invalid_user' in the Username field.<br>2. Enter 'wrong_password' in the Password field.<br>3. Click the Login button. | Error banner shows 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-005 |  | Login attempt with locked out user | User is on the login page. | 1. Enter 'locked_out_user' in the Username field.<br>2. Enter 'secret_sauce' in the Password field.<br>3. Click the Login button. | Error banner shows 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Login attempt with maximum length username | User is on the login page. | 1. Enter a username with maximum allowed length (e.g., 20 characters).<br>2. Enter 'secret_sauce' in the Password field.<br>3. Click the Login button. | User is redirected to the Product Inventory page or an appropriate error message is shown if the username is invalid. | medium |
| TC-007 |  | Login attempt with special characters in username | User is on the login page. | 1. Enter '@user!' in the Username field.<br>2. Enter 'secret_sauce' in the Password field.<br>3. Click the Login button. | Error banner shows 'Epic sadface: Username and password do not match any user in this service.' | medium |
| TC-008 |  | Login attempt with empty fields | User is on the login page. | 1. Leave both Username and Password fields empty.<br>2. Click the Login button. | Error banner shows 'Epic sadface: Username is required.' and 'Epic sadface: Password is required.' | medium |

---

## Product Inventory

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Add product to cart | User is logged in, Product Inventory page is open | 1. Locate a product in the list<br>2. Click on the 'Add to cart' button | The product is added to the cart, the button changes to 'Remove', and the cart badge count updates accordingly. | high |
| TC-010 |  | Remove product from cart | User is logged in, Product is already added to the cart | 1. Locate the product in the cart<br>2. Click on the 'Remove' button | The product is removed from the cart, the button changes back to 'Add to cart', and the cart badge count updates accordingly. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Attempt to add a product without being logged in | User is not logged in, Product Inventory page is open | 1. Locate a product in the list<br>2. Click on the 'Add to cart' button | An error message is displayed indicating that the user must log in to add products to the cart. | high |
| TC-012 |  | Attempt to remove a product not in the cart | User is logged in, No products are in the cart | 1. Locate a product in the cart<br>2. Click on the 'Remove' button | An error message is displayed indicating that there are no products to remove. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Sort products by name A-Z | User is logged in, Product Inventory page is open with multiple products | 1. Open the sort dropdown<br>2. Select 'Name A-Z' | The product list is sorted alphabetically from A to Z. | medium |
| TC-014 |  | Sort products by price low-high | User is logged in, Product Inventory page is open with multiple products | 1. Open the sort dropdown<br>2. Select 'Price low-high' | The product list is sorted by price from lowest to highest. | medium |
| TC-015 |  | Add maximum number of products to cart | User is logged in, Product Inventory page is open, Maximum cart limit is known | 1. Add products to the cart until the maximum limit is reached | The cart allows adding products up to the maximum limit, and an error message is displayed if the limit is exceeded. | low |
| TC-016 |  | Check product detail page navigation | User is logged in, Product Inventory page is open | 1. Click on a product name or image | The Product Detail page for the selected product opens successfully. | medium |

---

## Product Detail

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Add product to cart successfully | User is on the Product Detail page, Product is available in stock | 1. Click on the 'Add to cart' button | Product is added to the cart, and the button changes to 'Remove' | high |
| TC-019 |  | Navigate back to product inventory | User is on the Product Detail page | 1. Click on the 'Back to products' button | User is redirected to the Product Inventory page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | Attempt to add out-of-stock product to cart | User is on the Product Detail page, Product is out of stock | 1. Click on the 'Add to cart' button | An error message is displayed indicating the product is out of stock | high |
| TC-020 |  | Check cart icon functionality when cart is empty | User is on the Product Detail page, Cart is empty | 1. Click on the cart icon | User is taken to the Shopping Cart page with a message indicating the cart is empty | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 |  | Check product detail with maximum length description | User is on the Product Detail page, Product has a description at maximum character limit | 1. View the product description | Product description is displayed correctly without truncation or errors | low |
| TC-022 |  | Check product detail with empty fields | User is on the Product Detail page, Product has no image or name | 1. View the product detail | Placeholder text or default image is displayed for empty fields | low |

---

## Shopping Cart

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 |  | User successfully views items in the cart | User has added items to the shopping cart | 1. Navigate to the Shopping Cart page. | The Shopping Cart page displays the items added to the cart with their quantity and description. | high |
| TC-024 |  | User clicks 'Continue Shopping' button | User is on the Shopping Cart page | 1. Click on the 'Continue Shopping' button. | User is redirected to the Product Inventory page. | medium |
| TC-025 |  | User clicks 'Checkout' button | User is on the Shopping Cart page | 1. Click on the 'Checkout' button. | User is redirected to the Checkout page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | User tries to remove an item that is not in the cart | User is on the Shopping Cart page with no items | 1. Attempt to click the 'Remove' button for a non-existent item. | An error message is displayed indicating that there are no items to remove. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 |  | User views cart with maximum number of items | User has added the maximum allowed number of items to the cart | 1. Navigate to the Shopping Cart page. | The Shopping Cart page displays all items correctly without any layout issues. | low |
| TC-028 |  | User views cart with one item | User has added one item to the cart | 1. Navigate to the Shopping Cart page. | The Shopping Cart page displays the single item correctly with its quantity and description. | low |
| TC-029 |  | User views cart with empty state | User has not added any items to the cart | 1. Navigate to the Shopping Cart page. | The Shopping Cart page displays a message indicating that the cart is empty. | medium |

---

## Checkout - Information

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | Successful checkout with valid inputs | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click on 'Continue' | User is taken to the overview step without any error messages. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Error when First Name is missing | User is on the Checkout Information page | 1. Leave the First Name field empty<br>2. Enter 'Doe' in the Last Name field<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click on 'Continue' | An error banner displays 'Error: First Name is required'. | high |
| TC-032 |  | Error when Last Name is missing | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Leave the Last Name field empty<br>3. Enter '12345' in the Zip/Postal Code field<br>4. Click on 'Continue' | An error banner displays 'Error: Last Name is required'. | high |
| TC-033 |  | Error when Postal Code is missing | User is on the Checkout Information page | 1. Enter 'John' in the First Name field<br>2. Enter 'Doe' in the Last Name field<br>3. Leave the Zip/Postal Code field empty<br>4. Click on 'Continue' | An error banner displays 'Error: Postal Code is required'. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Check behavior with maximum length inputs | User is on the Checkout Information page | 1. Enter 'JohnJohnJohnJohn' (16 characters) in the First Name field<br>2. Enter 'DoeDoeDoeDoe' (15 characters) in the Last Name field<br>3. Enter '123456789012345' (15 characters) in the Zip/Postal Code field<br>4. Click on 'Continue' | User is taken to the overview step without any error messages. | medium |
| TC-035 |  | Check behavior with empty fields | User is on the Checkout Information page | 1. Leave all fields empty<br>2. Click on 'Continue' | An error banner displays 'Error: First Name is required', 'Error: Last Name is required', and 'Error: Postal Code is required'. | high |
| TC-036 |  | Check behavior with special characters in inputs | User is on the Checkout Information page | 1. Enter 'John@123' in the First Name field<br>2. Enter 'Doe#456' in the Last Name field<br>3. Enter '12345-6789' in the Zip/Postal Code field<br>4. Click on 'Continue' | User is taken to the overview step without any error messages. | medium |

---

## Checkout - Overview

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | Complete order successfully | User has items in the cart, User is on the checkout overview page | 1. Review the order summary<br>2. Click on 'Finish' button | User is navigated to the confirmation page with a success message. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Cancel checkout process | User is on the checkout overview page | 1. Click on 'Cancel' button | User is exited from the checkout process and returned to the previous page. | medium |
| TC-040 |  | Attempt to finish order with empty cart | User has an empty cart, User is on the checkout overview page | 1. Click on 'Finish' button | Error message is displayed indicating that the cart is empty. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Order summary with maximum items | User has the maximum allowed items in the cart | 1. Review the order summary with maximum items<br>2. Click on 'Finish' button | User is navigated to the confirmation page with a success message. | low |
| TC-041 |  | Order summary with zero total | User has items with zero price in the cart, User is on the checkout overview page | 1. Review the order summary showing zero total<br>2. Click on 'Finish' button | User is navigated to the confirmation page with a success message indicating a zero total. | medium |

---

## Checkout - Confirmation

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Successful order confirmation | User has completed the checkout process successfully. | 1. Navigate to the confirmation page.<br>2. Observe the success message. | The message 'Thank you for your order!' is displayed. | high |
| TC-046 |  | Back Home button functionality | User is on the confirmation page. | 1. Click on the 'Back Home' button. | User is redirected to the Product Inventory page and the cart is cleared. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Order confirmation without completing checkout | User has not completed the checkout process. | 1. Attempt to navigate to the confirmation page directly. | An error message is displayed indicating that the checkout process must be completed first. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-044 |  | Confirmation page with empty cart | User has an empty cart. | 1. Navigate to the confirmation page.<br>2. Observe the success message. | The message 'Thank you for your order!' is displayed, indicating that the system handles empty cart scenarios gracefully. | medium |
| TC-045 |  | Confirmation page with maximum length message | User has completed the checkout process successfully. | 1. Navigate to the confirmation page.<br>2. Observe the success message with maximum length. | The message 'Thank you for your order!' is displayed without truncation. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Successful logout | User is logged in and on a protected page. | 1. Click on the logout button.<br>2. Wait for the page to redirect. | User is redirected to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Logout without being logged in | User is not logged in. | 1. Attempt to click on the logout button. | Logout button is disabled or an error message is displayed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Logout while session is about to expire | User is logged in and session is near expiration. | 1. Click on the logout button just before session expiration.<br>2. Wait for the page to redirect. | User is redirected to the login page without session expiration error. | medium |
| TC-050 |  | Logout from multiple tabs | User is logged in on multiple tabs. | 1. Click on the logout button in one tab.<br>2. Switch to another tab and try to access a protected page. | User is redirected to the login page when accessing the protected page in the second tab. | low |

---

## Reset App State

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-051 |  | Reset app state successfully | User is logged in, User has items in the cart | 1. Navigate to the app settings.<br>2. Click on 'Reset App State' button.<br>3. Confirm the action. | The cart is cleared, and the in-app state is reset without logging the user out. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Attempt to reset app state while logged out | User is logged out | 1. Navigate to the app settings.<br>2. Click on 'Reset App State' button. | An error message is displayed indicating that the user must be logged in to reset the app state. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-053 |  | Reset app state with an empty cart | User is logged in, User has an empty cart | 1. Navigate to the app settings.<br>2. Click on 'Reset App State' button.<br>3. Confirm the action. | The app state is reset successfully, and the user remains logged in. | medium |
| TC-054 |  | Reset app state multiple times in quick succession | User is logged in, User has items in the cart | 1. Navigate to the app settings.<br>2. Click on 'Reset App State' button.<br>3. Confirm the action.<br>4. Immediately click 'Reset App State' again. | The app state is reset successfully without any errors, and the user remains logged in. | medium |

---
