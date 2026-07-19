# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Checkout - Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-001 | Unauthenticated access blocked | User not logged in | 1. Navigate directly to Checkout - Overview URL | Redirected to login page, overview not shown | High |
| SL-CHK2-002 | Finish blocked with empty cart | On overview page, cart empty | 1. Click "Finish" | Finish blocked, error indicating cart is empty | High |
| SL-CHK2-003 | Tax calculated | On overview page | 1. View Tax amount | Tax calculated (typically 8%) | High |
| SL-CHK2-004 | Total correct | On overview page | 1. View Total | Total = Item Total + Tax | High |
| SL-CHK2-005 | Finish purchase | On overview page | 1. Click "Finish" | Order placed, confirmation page shown | High |
| SL-CHK2-006 | Cancel from overview | On overview page | 1. Click "Cancel" | Returns to Shopping Cart page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-007 | Rapid double-click Finish | On overview page | 1. Click "Finish"<br>2. Immediately click "Finish" again | Only one order placed, single confirmation shown | Medium |
| SL-CHK2-008 | Browser Back after Finish | On overview page | 1. Click "Finish"<br>2. Press browser Back button | Cannot resubmit a duplicate order | Medium |
| SL-CHK2-009 | Price breakdown clear | On overview page | 1. View totals section | Item total, Tax, and Total clearly labeled | Medium |
