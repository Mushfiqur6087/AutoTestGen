# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Shopping Cart

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-001 | Item description with special characters displayed intact | Item with emoji/unicode in description added | 1. Click cart icon<br>2. View item description | Emoji and unicode characters rendered intact, no placeholders | High |
| SL-CART-002 | Remove item from cart | Items in cart | 1. Click "Remove" on an item | Item removed from cart, list updates | High |
| SL-CART-003 | Continue shopping | On cart page | 1. Click "Continue Shopping" | Returns to inventory page | High |
| SL-CART-004 | Proceed to checkout | Items in cart | 1. Click "Checkout" | Navigates to checkout information page | High |
| SL-CART-005 | Cart persists across pages | Items added | 1. Navigate to different pages<br>2. Return to cart | Items still in cart | High |
| SL-CART-006 | Unauthenticated access blocked | User not logged in | 1. Navigate directly to Shopping Cart URL | Redirected to login page, cart not shown | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-007 | Empty cart | No items added | 1. Navigate to cart | Empty cart state or message displayed | Medium |
| SL-CART-008 | Checkout blocked when not logged in | Not logged in, items in cart | 1. Navigate to cart<br>2. Try to checkout | Redirected to login page, checkout not begun | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-009 | Leading/trailing whitespace trimmed in display | Item name/description saved with extra whitespace | 1. View cart | Whitespace trimmed in displayed name and description | Medium |
| SL-CART-010 | Remove button for each item | Multiple items in cart | 1. View cart | Each item has its own "Remove" button | Medium |
