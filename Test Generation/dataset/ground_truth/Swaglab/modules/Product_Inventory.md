# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Product Inventory

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-001 | Products displayed | User logged in | 1. View inventory page | All products displayed with name, description, price, and "Add to cart" button | High |
| SL-INV-002 | Add product to cart | User logged in | 1. Click "Add to cart" on any product | Button changes to "Remove", cart badge shows "1" | High |
| SL-INV-003 | Add multiple products | User logged in | 1. Add product 1 to cart<br>2. Add product 2 to cart<br>3. Add product 3 to cart | Cart badge shows "3" | High |
| SL-INV-004 | Remove product from cart | Product in cart | 1. Click "Remove" button | Button changes to "Add to cart", cart badge decrements | High |
| SL-INV-005 | Sort A-Z (default) | User logged in | 1. Check default sort order | Products sorted alphabetically A-Z | High |
| SL-INV-006 | Sort Z-A | User logged in | 1. Select "Name (Z to A)" from dropdown | Products sorted alphabetically Z-A | High |
| SL-INV-007 | Sort Price low to high | User logged in | 1. Select "Price (low to high)" | Products sorted by price ascending | High |
| SL-INV-008 | Sort Price high to low | User logged in | 1. Select "Price (high to low)" | Products sorted by price descending | High |
| SL-INV-009 | Navigate to product detail | User logged in | 1. Click on product name or image | Navigates to product detail page | High |
| SL-INV-010 | Cart icon navigation | User logged in | 1. Click cart icon | Navigates to shopping cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-011 | Access inventory without login | Not logged in | 1. Navigate directly to inventory URL | Redirected to login or access denied | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-012 | Product images displayed | User logged in | 1. View inventory | All products have images | Medium |
| SL-INV-013 | Price formatting | User logged in | 1. View product prices | Prices formatted as $XX.XX | Medium |
| SL-INV-014 | Cart badge visibility | User logged in, cart empty | 1. View cart icon | No badge shown when cart is empty | Medium |
| SL-INV-015 | Cart badge updates real-time | User logged in | 1. Add item<br>2. Observe badge | Badge updates immediately | High |
| SL-INV-016 | Sort dropdown options | User logged in | 1. Click sort dropdown | Shows 4 options: A-Z, Z-A, Price low-high, Price high-low | Medium |
| SL-INV-017 | Hamburger menu visible | User logged in | 1. View top-left corner | Hamburger menu icon visible | Medium |
