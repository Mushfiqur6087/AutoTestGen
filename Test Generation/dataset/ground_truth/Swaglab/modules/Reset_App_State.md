# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Reset App State

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-RESET-001 | Reset clears cart | Items in cart | 1. Open hamburger menu<br>2. Click "Reset App State" | Cart cleared, badge removed | High |
| SL-RESET-002 | Reset button states | Items added (buttons show "Remove") | 1. Click "Reset App State" | All "Remove" buttons revert to "Add to cart" | High |
| SL-RESET-003 | Reset preserves login | User logged in with items | 1. Click "Reset App State" | User remains logged in | Medium |
