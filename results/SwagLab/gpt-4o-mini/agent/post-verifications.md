# Post-Verification Specifications

### [TC-002] Attempt to reset app state without any preconditions
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Reset App State button

**Original Expected Result:** The app state does not reset; the cart remains unchanged

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Shopping Cart`
- **Observe**:
  - cart is empty

**Post-Check**
- **Navigate To**: `User Dashboard -> Shopping Cart`
- **Observe**:
  - cart contains the added product
  - cart badge shows '1'

**Expected Change**: The cart now contains the newly added product, and the cart badge reflects the correct item count.

---

### [TC-003] Attempt to logout when not logged in
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session ended.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - product listed in cart

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - product not listed in cart
  - cart badge shows updated count

**Expected Change**: The product is removed from the cart, and the cart badge reflects the correct number of items.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Shopping Cart`
- **Observe**:
  - cart is empty
  - cart badge shows '0'

**Post-Check**
- **Navigate To**: `User Dashboard -> Shopping Cart`
- **Observe**:
  - cart contains the newly added product
  - cart badge shows '1'

**Expected Change**: The cart now contains the newly added product, and the cart badge reflects the correct item count.

---

### [TC-003] Attempt to logout when not logged in
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session ended.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - item is present in the cart
  - Remove button is visible for the item

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - item is no longer present in the cart
  - Remove button is no longer visible for the item

**Expected Change**: The item has been successfully removed from the cart.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout Information page`
- **Observe**:
  - First Name field is empty
  - Last Name field is empty
  - Zip/Postal Code field is empty

**Post-Check**
- **Navigate To**: `Checkout Overview page`
- **Observe**:
  - Order summary displayed
  - Item total is correct
  - Tax is calculated
  - Total is correct

**Expected Change**: The user is navigated to the Checkout Overview page, where the order summary and totals are displayed correctly.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout Overview`
- **Observe**:
  - order summary
  - item totals
  - tax amount
  - total amount

**Post-Check**
- **Navigate To**: `Checkout Confirmation`
- **Observe**:
  - confirmation message
  - thank you note
  - order details

**Expected Change**: The user is redirected to the confirmation page, and a confirmation message is displayed indicating the order has been successfully completed.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - items displayed in cart
  - cart badge shows item count

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - cart is empty
  - cart badge is removed

**Expected Change**: The cart is cleared and the cart badge is removed after resetting the app state.

---
