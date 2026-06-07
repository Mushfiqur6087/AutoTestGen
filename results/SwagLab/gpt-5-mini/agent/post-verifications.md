# Post-Verification Specifications

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory page`
- **Observe**:
  - <target product> row displays 'Add to cart' button (product is not in cart)
  - record the cart badge current count (baseline count before action)

**Post-Check**
- **Navigate To**: `Product Inventory page -> Shopping Cart page`
- **Observe**:
  - <target product> row displays 'Remove' button
  - cart badge count is baseline count + 1
  - Shopping Cart page lists <target product> with correct name and price

**Expected Change**: The selected product is added to the cart: the product row button changes from 'Add to cart' to 'Remove', the cart badge increments by one relative to the recorded baseline, and the Shopping Cart contains an entry for the product with the expected details.

---

### [TC-003] Unauthenticated user cannot perform Reset App State
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application page that contains the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** Action is blocked: the user is redirected to the Login page (or shown an authentication prompt); Reset App State is not performed — the cart contents remain unchanged and the cart badge and add/remove button states remain as before; no 'reset' confirmation is shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory page`
- **Observe**:
  - target product row is present in the list
  - target product's action button text is 'Remove'
  - cart badge displays the current item count (>= 1)
  - optional: Shopping Cart page lists the target product (verify by navigating to Cart if needed)

**Post-Check**
- **Navigate To**: `Product Inventory page, then Shopping Cart page`
- **Observe**:
  - target product's action button text is 'Add to cart' on the Product Inventory page
  - cart badge count has decreased by one compared to pre_check
  - Shopping Cart page no longer lists the target product

**Expected Change**: The target product is removed from the cart: the inventory row button changes from 'Remove' to 'Add to cart', the cart badge count decrements by one, and the Shopping Cart does not contain the product anymore.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Detail page for the selected product; then open Shopping Cart page to confirm absence`
- **Observe**:
  - 'Add to cart' button is visible on the Product Detail page for the selected product
  - Shopping Cart page does NOT contain the selected product
  - Record the current cart badge value (or absence of badge) as pre_count

**Post-Check**
- **Navigate To**: `Product Detail page for the selected product; then open Shopping Cart page`
- **Observe**:
  - 'Remove' button is visible on the Product Detail page for the selected product
  - Product is labelled as 'In Cart' on the Product Detail page (or button text shows 'Remove')
  - Shopping Cart page contains the selected product with correct name and price
  - Cart badge value has increased by 1 compared to pre_count (or a badge is now present if previously absent)

**Expected Change**: The selected product transitions from Not In Cart to In Cart: the Product Detail page shows a 'Remove' button and 'In Cart' state, and the Shopping Cart lists the product with the cart badge incremented accordingly.

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Detail page for <product> (and optionally open Shopping Cart to confirm presence)`
- **Observe**:
  - 'Remove' button is visible on the Product Detail page for <product> indicating it is currently in cart
  - cart badge displays a count >= 1
  - Shopping Cart (if opened) contains a row for <product>

**Post-Check**
- **Navigate To**: `Product Detail page for <product> -> Shopping Cart`
- **Observe**:
  - 'Add to cart' button is visible on the Product Detail page for <product>
  - cart badge value is decremented by 1 compared to pre-check (or badge is no longer shown if it reached zero)
  - Shopping Cart no longer contains a row for <product>

**Expected Change**: The product has been removed from the cart: the Product Detail page shows the 'Add to cart' button instead of 'Remove', the cart badge count is decremented (or removed if zero), and the Shopping Cart no longer lists the product.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart page`
- **Observe**:
  - Shopping Cart table contains a row for <target item> (name, price, quantity visible)
  - Remove button is present on the <target item> row
  - Cart badge (top-right) shows count >= 1

**Post-Check**
- **Navigate To**: `Shopping Cart page (or refresh current page); optionally visit Inventory page for the removed product`
- **Observe**:
  - Shopping Cart table does NOT contain a row for <target item>
  - Cart badge count is decremented by one relative to pre-check
  - On Inventory or Product Detail page the product shows 'Add to cart' (not 'Remove')

**Expected Change**: The removed item is absent from the Shopping Cart list, the cart badge count has decreased accordingly, and the product is available to add again from Inventory/Product Detail pages.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout -> Overview (Order Summary) page`
- **Observe**:
  - order summary lists all items in cart (product names and prices)
  - totals section shows Item total, Tax, and Total values
  - payment information section displays the valid payment method
  - shipping information section displays the shipping address or method
  - Finish button is visible and enabled

**Post-Check**
- **Navigate To**: `Checkout -> Complete / Confirmation page`
- **Observe**:
  - confirmation message 'Thank you for your order!' (or equivalent success text) is visible
  - success image or checkmark (order dispatched visual) is displayed
  - cart badge is not displayed (no item count)
  - navigating to the Shopping Cart shows no items / empty cart state

**Expected Change**: The application shows the order confirmation page with a success message and image, and the user's cart is cleared (no cart badge and cart page is empty).

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Order Confirmation page`
- **Observe**:
  - "Thank you for your order!" confirmation message is visible
  - Cart icon is visible (note whether a cart badge is present and its value)
  - Option to click 'Back Home' button is present

**Post-Check**
- **Navigate To**: `Product Inventory page (Home) after clicking 'Back Home'`
- **Observe**:
  - Product inventory list/grid is displayed (product names and prices visible)
  - Cart badge is not visible or shows no items (no numeric badge)
  - Opening the cart (click cart icon) shows an empty cart or message indicating no items

**Expected Change**: The app navigates to the Product Inventory page and the shopping cart is cleared: there is no cart badge indicating items and the cart contents list is empty.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Inventory page and Cart page`
- **Observe**:
  - cart badge displays a positive count (greater than 0)
  - Cart page lists the previously added items (one or more item rows present)
  - On Inventory page, at least one product's action button shows 'Remove'

**Post-Check**
- **Navigate To**: `Inventory page and Cart page`
- **Observe**:
  - cart badge is not visible or shows '0' (no active badge)
  - Cart page shows empty state or message and no item rows
  - On Inventory page, all product action buttons show 'Add to cart' instead of 'Remove'
  - User remains logged in (hamburger menu present and user not redirected to login)

**Expected Change**: The cart is cleared (no items listed and no cart badge), all 'Remove' buttons have reverted to 'Add to cart', and the user session remains active (user stays logged in).

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Inventory (Products) page - logged in user`
- **Observe**:
  - cart badge is not present (no items)
  - each product tile shows an 'Add to cart' button (no 'Remove' buttons)
  - hamburger menu icon is visible (indicates user is logged in)

**Post-Check**
- **Navigate To**: `Inventory (Products) page - after clicking Reset App State`
- **Observe**:
  - cart badge is not present (no items)
  - each product tile still shows an 'Add to cart' button (no 'Remove' buttons)
  - hamburger menu icon remains visible and logout option is accessible
  - no error or unexpected notification is displayed

**Expected Change**: The application remains in a cleared state: the cart stays empty (no badge), all product buttons remain 'Add to cart' (no items marked in-cart), and the user session remains active (hamburger menu/logout still available).

---
