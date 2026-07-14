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
| MW-BP-005 | Unauthenticated access blocked | User not logged in | 1. Navigate to Payments page without logging in | Redirected to login page, Pay form not accessible | High |
| MW-BP-006 | Amount exactly equals available balance | User logged in, source account balance = amount entered | 1. Enter amount equal to source account balance<br>2. Submit | "Payment submitted successfully." with reference code, balance reduced to $0.00 | Medium |
| MW-BP-007 | Amount one unit over available balance | User logged in | 1. Enter amount = balance + smallest currency unit<br>2. Submit | Error: "Insufficient funds" | Medium |
| MW-BP-008 | Account Number and Confirm Account exact match | User logged in | 1. Enter identical values in Account Number and Confirm Account<br>2. Submit | "Payment submitted successfully." with reference code | Medium |
| MW-BP-009 | Account numbers differ by one digit | User logged in | 1. Enter Account Number and Confirm Account differing by a single digit<br>2. Submit | Error: "Account numbers do not match" | Medium |
| MW-BP-010 | Rapid double-click on Pay button | User logged in, valid form filled | 1. Click "Pay"<br>2. Immediately click "Pay" again | Only one payment processed, single confirmation and reference code shown | Low |
| MW-BP-011 | Confirm Account whitespace-only difference | User logged in | 1. Enter Confirm Account matching Account Number but with leading/trailing whitespace<br>2. Submit | Error: "Account numbers do not match" | Low |
| MW-BP-012 | Account numbers mismatch | User logged in | 1. Enter different account numbers<br>2. Submit | Error: "Account numbers do not match" | High |
| MW-BP-013 | Non-numeric amount | User logged in | 1. Enter non-numeric value in Amount<br>2. Submit | Validation error: must be numeric | Medium |
| MW-BP-014 | Insufficient funds | User logged in | 1. Enter amount > source balance<br>2. Submit | Error: "Insufficient funds" | High |
| MW-BP-015 | Source account has no available funds | User logged in, source account balance = $0 | 1. Select $0-balance source account<br>2. Submit | Validation error: no funded source account available | High |
| MW-BP-016 | Payee name maximum length | User logged in | 1. Enter payee name > 50 chars | Validation error or truncation | Low |
| MW-BP-017 | XSS payload in Payee Name | User logged in | 1. Enter "<script>alert(1)</script>" | Payload neutralized | High |
