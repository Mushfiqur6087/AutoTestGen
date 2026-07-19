# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Product Inventory

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-001 | Products displayed | User logged in | 1. View inventory page | All products displayed with name, description, price, and "Add to cart" button | High |
| SL-INV-002 | Add product to cart | User logged in | 1. Click "Add to cart" on any product | Button changes to "Remove", cart badge shows "1" | High |
| SL-INV-003 | Immediate Add then Remove nets zero | User logged in | 1. Click "Add to cart"<br>2. Immediately click "Remove" | Cart badge returns to original count, button shows "Add to cart" | High |
| SL-INV-004 | Remove product from cart | Product in cart | 1. Click "Remove" button | Button changes to "Add to cart", cart badge decrements | High |
| SL-INV-005 | Sort A-Z (default) | User logged in | 1. Check default sort order | Products sorted alphabetically A-Z | High |
| SL-INV-006 | Open About page from hamburger menu | User logged in | 1. Open hamburger menu<br>2. Click "About" | About page displayed | High |
| SL-INV-007 | Sort Price low to high | User logged in | 1. Select "Price (low to high)" | Products sorted by price ascending | High |
| SL-INV-008 | Logout via hamburger menu | User logged in | 1. Open hamburger menu<br>2. Click "Logout" | Sign-in page displayed | High |
| SL-INV-009 | Navigate to product detail | User logged in | 1. Click on product name or image | Navigates to product detail page | High |
| SL-INV-010 | Cart button opens Checkout sequence | User logged in | 1. Click "Cart" button in header | Checkout sequence opens at the Information step | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-011 | Access inventory without login | Not logged in | 1. Navigate directly to inventory URL | Redirected to login or access denied | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-012 | Unauthenticated user cannot open Cart/Checkout | User not logged in | 1. Attempt to open Cart/Checkout | Redirected to login page, checkout not opened | Medium |
| SL-INV-013 | Add to cart control hidden when already in cart | Product already in cart | 1. View product in inventory list | "Add to cart" not visible, "Remove" shown instead | Medium |
| SL-INV-014 | Remove control hidden when not in cart | Product not in cart | 1. View product in inventory list | "Remove" not visible, "Add to cart" shown instead | Medium |
| SL-INV-015 | Cart badge updates real-time | User logged in | 1. Add item<br>2. Observe badge | Badge updates immediately | High |
| SL-INV-016 | Very long product name handled | Product name >= 200 chars | 1. View inventory listing<br>2. Open product detail | Name truncated/wrapped without breaking layout on inventory; full name shown on detail page | Medium |
| SL-INV-017 | Hamburger menu visible | User logged in | 1. View top-left corner | Hamburger menu icon visible | Medium |
