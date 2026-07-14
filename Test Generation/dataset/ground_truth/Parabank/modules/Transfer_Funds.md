# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Transfer Funds

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-TF-001 | Internal transfer | User logged in, multiple accounts | 1. Select "My ParaBank Account"<br>2. Enter amount<br>3. Select source account<br>4. Select destination account<br>5. Submit | "Transfer completed successfully." with transaction ID | High |
| MW-TF-002 | External transfer | User logged in | 1. Select "External Account"<br>2. Enter amount<br>3. Select source account<br>4. Enter and confirm external account number<br>5. Submit | "Transfer completed successfully." with transaction ID | High |
| MW-TF-003 | Source account filter | User logged in | 1. View source dropdown | Only Checking and Savings accounts shown | High |
| MW-TF-004 | Transfer type toggle | User logged in | 1. Select Internal<br>2. Select External | Destination options change appropriately | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-TF-005 | Empty amount | User logged in | 1. Leave amount empty<br>2. Submit | Validation error | High |
| MW-TF-006 | Zero amount | User logged in | 1. Enter $0<br>2. Submit | Validation error | High |
| MW-TF-007 | Negative amount | User logged in | 1. Enter -$100<br>2. Submit | Validation error | High |
| MW-TF-008 | Insufficient funds | User logged in | 1. Enter amount > source balance<br>2. Submit | Error: "Insufficient funds" | High |
| MW-TF-009 | Same source and destination | User logged in | 1. Select same account for source and destination<br>2. Submit | Error or prevented | High |
| MW-TF-010 | External account mismatch | User logged in | 1. Select External<br>2. Enter different account numbers<br>3. Submit | Error: "Account numbers do not match" | High |
| MW-TF-011 | No source selected | User logged in | 1. Don't select source account<br>2. Submit | Validation error | High |
| MW-TF-012 | No destination selected | Internal transfer | 1. Don't select destination<br>2. Submit | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-TF-013 | Transfer exact balance | User logged in | 1. Enter exact source balance<br>2. Submit | Transfer succeeds, source balance = $0 | Medium |
| MW-TF-014 | Minimum transfer ($0.01) | User logged in | 1. Enter $0.01<br>2. Submit | Transfer succeeds or minimum amount error | Low |
| MW-TF-015 | Transfer amount just above balance | User logged in | 1. Enter amount = balance + $0.01 | Insufficient funds error | Medium |
| MW-TF-016 | External routing number boundaries | User logged in | 1. Enter routing number < 9 or > 9 digits | Validation error | High |
