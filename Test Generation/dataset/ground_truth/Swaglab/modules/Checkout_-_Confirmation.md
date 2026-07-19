# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Checkout - Confirmation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-001 | Confirmation displayed | Order completed | 1. Complete checkout | "Thank you for your order!" message displayed | High |
| SL-CHK3-002 | Cart cleared | Order completed | 1. View cart after order | Cart is empty, no badge | High |
| SL-CHK3-003 | Back to products | On confirmation page | 1. Click "Back Home" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-004 | Confirmation blocked if checkout not completed | Logged in, checkout not completed | 1. Navigate directly to Confirmation page URL | Access blocked, redirected into checkout flow | Medium |
| SL-CHK3-005 | Back Home then add item updates cart | On confirmation page | 1. Click "Back Home"<br>2. Immediately add a product from inventory | Cart badge increments to 1 for the newly added item | Medium |
