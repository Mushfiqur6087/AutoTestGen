# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Shopping Cart

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-001 | View cart with items | Items added to cart | 1. Click cart icon | All added items displayed with name, description, price, quantity | High |
| SL-CART-002 | Remove item from cart | Items in cart | 1. Click "Remove" on an item | Item removed from cart, list updates | High |
| SL-CART-003 | Continue shopping | On cart page | 1. Click "Continue Shopping" | Returns to inventory page | High |
| SL-CART-004 | Proceed to checkout | Items in cart | 1. Click "Checkout" | Navigates to checkout information page | High |
| SL-CART-005 | Cart persists across pages | Items added | 1. Navigate to different pages<br>2. Return to cart | Items still in cart | High |
| SL-CART-006 | Quantity display | Items in cart | 1. View cart | Quantity shown as "1" for each item | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-007 | Empty cart | No items added | 1. Navigate to cart | Empty cart state or message displayed | Medium |
| SL-CART-008 | Checkout with empty cart | No items in cart | 1. Navigate to cart<br>2. Try to checkout | Prevented or appropriate error | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-009 | Cart item layout | Items in cart | 1. View cart | Each item shows quantity, name, description, price | Medium |
| SL-CART-010 | Remove button for each item | Multiple items in cart | 1. View cart | Each item has its own "Remove" button | Medium |
