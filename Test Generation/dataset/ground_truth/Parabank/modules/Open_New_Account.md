# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Open New Account

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-ONA-001 | Open Checking account | User logged in, sufficient funds | 1. Navigate to Open New Account<br>2. Select Checking card<br>3. Enter deposit >= $25<br>4. Select funding account<br>5. Click "Open Account" | "Account opened successfully!" message, redirect to overview | High |
| MW-ONA-002 | Open Savings account | User logged in, sufficient funds | 1. Select Savings card<br>2. Enter deposit >= $100<br>3. Select funding account<br>4. Click "Open Account" | Account opened successfully | High |
| MW-ONA-004 | Real-time validation | User logged in | 1. Enter invalid deposit amount | Immediate validation error displayed | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-ONA-005 | No account type selected | User logged in | 1. Don't select account type<br>2. Try to submit | Validation error: account type required | High |
| MW-ONA-006 | Checking deposit < $25 | User logged in | 1. Select Checking<br>2. Enter $20<br>3. Submit | Validation error: minimum $25 required | High |
| MW-ONA-007 | Savings deposit < $100 | User logged in | 1. Select Savings<br>2. Enter $50<br>3. Submit | Validation error: minimum $100 required | High |
| MW-ONA-008 | Non-numeric deposit | User logged in | 1. Enter "abc" as deposit<br>2. Submit | Validation error: must be numeric | High |
| MW-ONA-009 | Insufficient funding balance | User logged in | 1. Enter deposit > funding account balance<br>2. Submit | Validation error: insufficient funds in funding account | High |
| MW-ONA-010 | No funding account selected | User logged in | 1. Don't select funding account<br>2. Submit | Validation error: funding account required | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-ONA-011 | Exact minimum Checking ($25) | User logged in | 1. Select Checking<br>2. Enter exactly $25<br>3. Submit | Account opens successfully | Medium |
| MW-ONA-012 | Exact minimum Savings ($100) | User logged in | 1. Select Savings<br>2. Enter exactly $100<br>3. Submit | Account opens successfully | Medium |
| MW-ONA-013 | Just below minimum | User logged in | 1. Select Checking<br>2. Enter $24.99 | Validation error | Medium |
| MW-ONA-014 | Deposit with excessive precision | User logged in | 1. Enter $25.1234 | Rounded to $25.12 or rejected | Medium |
| MW-ONA-015 | Duplicate account prevention | User logged in | 1. Submit form<br>2. Click Back<br>3. Submit again | Prevented or handled gracefully | Medium |
