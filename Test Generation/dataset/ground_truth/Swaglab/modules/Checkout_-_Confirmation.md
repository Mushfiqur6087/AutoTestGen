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
| SL-CHK3-004 | Success image displayed | Order completed | 1. View confirmation page | Pony Express image or checkmark visible | Medium |
| SL-CHK3-005 | Order dispatch message | Order completed | 1. View confirmation page | "Your order has been dispatched" or similar message | Medium |
