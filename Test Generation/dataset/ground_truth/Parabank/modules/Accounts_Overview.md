# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Accounts Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-AO-001 | Welcome message displayed | User logged in | 1. View Accounts Overview | "Welcome, [First Name]" message displayed | High |
| MW-AO-002 | All accounts listed | User logged in | 1. View accounts table | All accounts shown: Account Number, Type, Balance, Status, Open Date | High |
| MW-AO-003 | Account number masking | User logged in | 1. View account numbers | Only last 4 digits shown (****5001) | High |
| MW-AO-004 | Total balance calculation | User logged in | 1. View total row | Total = sum of all account balances | High |
| MW-AO-005 | Accounts ordered by date | User logged in | 1. View accounts table | Ordered by Open Date (earliest first) | Medium |
| MW-AO-006 | Active status badge | User logged in | 1. View Status column | "Active" badge displayed for active accounts | Medium |
| MW-AO-007 | High volume of accounts | User logged in with >50 accounts | 1. View Accounts Overview | Pagination or scroll handles accounts gracefully | Medium |
| MW-AO-008 | Zero balance display | User logged in | 1. View account with $0.00 | Balance displays exactly $0.00 without negative sign | Medium |
| MW-AO-009 | Extreme negative balance | User logged in | 1. View account with very large negative balance | Renders without UI breakage | Low |
