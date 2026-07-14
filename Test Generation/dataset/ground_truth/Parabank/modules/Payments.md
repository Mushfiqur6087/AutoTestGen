# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Payments

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-BP-001 | Successful bill payment | User logged in, sufficient funds | 1. Fill all fields: Payee Name, Address, City, State, ZIP, Phone, Account Number, Confirm Account, Amount<br>2. Select source account<br>3. Click "Pay" | "Payment submitted successfully." with reference code | High |
| MW-BP-002 | Quick select payee | User logged in | 1. Select from quick payees (Electric Company, Gas Utility, Internet Provider) | Payee fields auto-populated | High |
| MW-BP-003 | Balance updated | MW-BP-001 completed | 1. View Accounts Overview | Source account balance reduced | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-BP-004 | Payee Name empty | User logged in | 1. Leave Payee Name empty<br>2. Submit | Validation error | High |
| MW-BP-005 | Street Address empty | User logged in | 1. Leave Address empty<br>2. Submit | Validation error | High |
| MW-BP-006 | City empty | User logged in | 1. Leave City empty<br>2. Submit | Validation error | High |
| MW-BP-007 | State empty | User logged in | 1. Leave State empty<br>2. Submit | Validation error | High |
| MW-BP-008 | ZIP Code empty | User logged in | 1. Leave ZIP empty<br>2. Submit | Validation error | High |
| MW-BP-009 | Phone empty | User logged in | 1. Leave Phone empty<br>2. Submit | Validation error | High |
| MW-BP-010 | Account Number empty | User logged in | 1. Leave Account Number empty<br>2. Submit | Validation error | High |
| MW-BP-011 | Confirm Account empty | User logged in | 1. Leave Confirm Account empty<br>2. Submit | Validation error | High |
| MW-BP-012 | Account numbers mismatch | User logged in | 1. Enter different account numbers<br>2. Submit | Error: "Account numbers do not match" | High |
| MW-BP-013 | Amount empty | User logged in | 1. Leave Amount empty<br>2. Submit | Validation error | High |
| MW-BP-014 | Insufficient funds | User logged in | 1. Enter amount > source balance<br>2. Submit | Error: "Insufficient funds" | High |
| MW-BP-015 | No source account | User logged in | 1. Don't select source<br>2. Submit | Validation error | High |
| MW-BP-016 | Payee name maximum length | User logged in | 1. Enter payee name > 50 chars | Validation error or truncation | Low |
| MW-BP-017 | XSS payload in Payee Name | User logged in | 1. Enter "<script>alert(1)</script>" | Payload neutralized | High |
