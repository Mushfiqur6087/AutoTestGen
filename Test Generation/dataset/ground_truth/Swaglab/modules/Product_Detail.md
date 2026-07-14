# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Product Detail

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-001 | Product details displayed | User logged in | 1. Click on a product | Product name, description, price, and image displayed | High |
| SL-PD-002 | Add to cart from detail page | User logged in, on product detail | 1. Click "Add to cart" | Product added, button changes to "Remove", cart badge updates | High |
| SL-PD-003 | Remove from cart on detail page | Product in cart, on detail page | 1. Click "Remove" | Product removed, button changes to "Add to cart" | High |
| SL-PD-004 | Back to products | On product detail page | 1. Click "Back to products" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-005 | Large product image | On product detail | 1. View product image | Larger image than inventory thumbnail | Medium |
| SL-PD-006 | Price matches inventory | On product detail | 1. Compare price with inventory listing | Price is identical | High |
| SL-PD-007 | Cart state preserved | Product added from inventory | 1. Navigate to product detail | "Remove" button shown (not "Add to cart") | High |
