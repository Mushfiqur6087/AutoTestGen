# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Checkout - Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-001 | Order summary displayed | Completed checkout info | 1. View checkout overview | All cart items listed with prices | High |
| SL-CHK2-002 | Item total correct | Items in cart | 1. View Item total | Sum of all item prices | High |
| SL-CHK2-003 | Tax calculated | On overview page | 1. View Tax amount | Tax calculated (typically 8%) | High |
| SL-CHK2-004 | Total correct | On overview page | 1. View Total | Total = Item Total + Tax | High |
| SL-CHK2-005 | Finish purchase | On overview page | 1. Click "Finish" | Order placed, confirmation page shown | High |
| SL-CHK2-006 | Cancel from overview | On overview page | 1. Click "Cancel" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-007 | Payment info displayed | On overview page | 1. View payment section | Shows "SauceCard #31337" | Medium |
| SL-CHK2-008 | Shipping info displayed | On overview page | 1. View shipping section | Shows shipping method (Free Pony Express) | Medium |
| SL-CHK2-009 | Price breakdown clear | On overview page | 1. View totals section | Item total, Tax, and Total clearly labeled | Medium |
