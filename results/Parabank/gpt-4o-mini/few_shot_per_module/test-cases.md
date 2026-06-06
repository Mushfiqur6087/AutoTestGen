# Test Cases — Parabank

Generated: 2026-06-04T14:58:54.370738Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 71 | 19 | 27 | 25 | 48 | 23 | 0 |

## Login

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User has a registered account with valid email and password | 1. Navigate to the Login page<br>2. Enter a valid email/username in the Email/Username field<br>3. Enter the correct password in the Password field<br>4. Click the Sign In button | Page shows 'Signed in successfully.' and redirects to the Accounts Overview page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt login with incorrect password | User has a registered account with valid email and an incorrect password | 1. Navigate to the Login page<br>2. Enter a valid email/username in the Email/Username field<br>3. Enter an incorrect password in the Password field<br>4. Click the Sign In button | An error message 'Incorrect email or password. Please try again.' is displayed; the password field is cleared | high |
| TC-003 |  | Attempt login with unregistered email | User has not registered an account | 1. Navigate to the Login page<br>2. Enter an unregistered email/username in the Email/Username field<br>3. Enter any password in the Password field<br>4. Click the Sign In button | An error message 'Incorrect email or password. Please try again.' is displayed; the password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Attempt login with minimum password length | User has a registered account with valid email and a password of exactly 8 characters | 1. Navigate to the Login page<br>2. Enter a valid email/username in the Email/Username field<br>3. Enter a password that is exactly 8 characters long, containing uppercase, lowercase, number, and special character<br>4. Click the Sign In button | Page shows 'Signed in successfully.' and redirects to the Accounts Overview page | medium |
| TC-005 |  | Attempt login with empty Email/Username field | User has a registered account | 1. Navigate to the Login page<br>2. Leave the Email/Username field empty<br>3. Enter a valid password in the Password field<br>4. Click the Sign In button | An error message 'Incorrect email or password. Please try again.' is displayed; the password field is cleared | medium |

---

## Register

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Successful registration with valid inputs |  | 1. Navigate to the Registration page<br>2. Enter 'John' in the First Name field<br>3. Enter 'Doe' in the Last Name field<br>4. Enter '123 Main St' in the Street Address field<br>5. Enter 'Anytown' in the City field<br>6. Select 'California' from the State dropdown<br>7. Enter '12345' in the ZIP Code field<br>8. Enter '(123) 456-7890' in the Phone Number field<br>9. Enter '123-45-6789' in the Social Security Number field<br>10. Enter 'john.doe@example.com' in the Username field<br>11. Enter 'Password123' in the Password field<br>12. Enter 'Password123' in the Confirm Password field<br>13. Click the Register button | Page shows 'Account created successfully — please sign in,' and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt registration with invalid email format for Username |  | 1. Navigate to the Registration page<br>2. Enter 'John' in the First Name field<br>3. Enter 'Doe' in the Last Name field<br>4. Enter '123 Main St' in the Street Address field<br>5. Enter 'Anytown' in the City field<br>6. Select 'California' from the State dropdown<br>7. Enter '12345' in the ZIP Code field<br>8. Enter '(123) 456-7890' in the Phone Number field<br>9. Enter '123-45-6789' in the Social Security Number field<br>10. Enter 'john.doeexample.com' in the Username field<br>11. Enter 'Password123' in the Password field<br>12. Enter 'Password123' in the Confirm Password field<br>13. Click the Register button | An error message 'Invalid email format' is displayed; registration is not processed | high |
| TC-008 |  | Attempt registration with mismatched Password and Confirm Password |  | 1. Navigate to the Registration page<br>2. Enter 'John' in the First Name field<br>3. Enter 'Doe' in the Last Name field<br>4. Enter '123 Main St' in the Street Address field<br>5. Enter 'Anytown' in the City field<br>6. Select 'California' from the State dropdown<br>7. Enter '12345' in the ZIP Code field<br>8. Enter '(123) 456-7890' in the Phone Number field<br>9. Enter '123-45-6789' in the Social Security Number field<br>10. Enter 'john.doe@example.com' in the Username field<br>11. Enter 'Password123' in the Password field<br>12. Enter 'Password321' in the Confirm Password field<br>13. Click the Register button | An error message 'Passwords do not match' is displayed; registration is not processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt registration with minimum length password |  | 1. Navigate to the Registration page<br>2. Enter 'John' in the First Name field<br>3. Enter 'Doe' in the Last Name field<br>4. Enter '123 Main St' in the Street Address field<br>5. Enter 'Anytown' in the City field<br>6. Select 'California' from the State dropdown<br>7. Enter '12345' in the ZIP Code field<br>8. Enter '(123) 456-7890' in the Phone Number field<br>9. Enter '123-45-6789' in the Social Security Number field<br>10. Enter 'john.doe@example.com' in the Username field<br>11. Enter 'Pass123' in the Password field<br>12. Enter 'Pass123' in the Confirm Password field<br>13. Click the Register button | Page shows 'Account created successfully — please sign in,' and redirects to the login page | medium |
| TC-010 |  | Attempt registration with maximum length for Username |  | 1. Navigate to the Registration page<br>2. Enter 'John' in the First Name field<br>3. Enter 'Doe' in the Last Name field<br>4. Enter '123 Main St' in the Street Address field<br>5. Enter 'Anytown' in the City field<br>6. Select 'California' from the State dropdown<br>7. Enter '12345' in the ZIP Code field<br>8. Enter '(123) 456-7890' in the Phone Number field<br>9. Enter '123-45-6789' in the Social Security Number field<br>10. Enter 'john.doe.longusername@example.com' in the Username field<br>11. Enter 'Password123' in the Password field<br>12. Enter 'Password123' in the Confirm Password field<br>13. Click the Register button | Page shows 'Account created successfully — please sign in,' and redirects to the login page | medium |

---

## Accounts Overview

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | View Accounts Overview with multiple accounts | User logged in, User has multiple accounts | 1. Navigate to Accounts Overview from the dashboard<br>2. Observe the welcome message with the user's name<br>3. Review the table displaying all customer accounts | The page shows a welcome message with the user's name and a table listing all accounts with correct details including Account Number, Account Type, Current Balance, Account Status, and Open Date | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | View Accounts Overview without being logged in | User is not logged in | 1. Attempt to navigate to Accounts Overview | The user is redirected to the login page with an error message indicating that login is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | View Accounts Overview with a single account | User logged in, User has only one account | 1. Navigate to Accounts Overview from the dashboard<br>2. Observe the table displaying the single account | The page shows a welcome message with the user's name and a table with one account entry, displaying all details correctly including masked Account Number | medium |
| TC-014 |  | View Accounts Overview with maximum number of accounts | User logged in, User has the maximum allowed number of accounts | 1. Navigate to Accounts Overview from the dashboard<br>2. Observe the table displaying all accounts | The page shows a welcome message with the user's name and a table listing all accounts correctly, with the total balance footer reflecting the sum of all accounts | medium |

---

## Open New Account

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Open a Checking account with valid initial deposit | User logged in, A funding account with at least $25 exists | 1. Navigate to Open New Account<br>2. Select the Checking account type card<br>3. Enter 25 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Checking account appears | high |
| TC-016 |  | Open a Savings account with valid initial deposit | User logged in, A funding account with at least $100 exists | 1. Navigate to Open New Account<br>2. Select the Savings account type card<br>3. Enter 100 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Savings account appears | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Attempt to open a Checking account with insufficient initial deposit | User logged in, A funding account with less than $25 exists | 1. Navigate to Open New Account<br>2. Select the Checking account type card<br>3. Enter 20 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | An error message 'Minimum deposit for Checking account is $25' is displayed; no account is opened | high |
| TC-018 |  | Attempt to open a Savings account with insufficient initial deposit | User logged in, A funding account with less than $100 exists | 1. Navigate to Open New Account<br>2. Select the Savings account type card<br>3. Enter 50 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | An error message 'Minimum deposit for Savings account is $100' is displayed; no account is opened | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Open a Checking account with the exact minimum deposit amount | User logged in, A funding account with at least $25 exists | 1. Navigate to Open New Account<br>2. Select the Checking account type card<br>3. Enter exactly 25 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Checking account appears | medium |
| TC-020 |  | Open a Savings account with the exact minimum deposit amount | User logged in, A funding account with at least $100 exists | 1. Navigate to Open New Account<br>2. Select the Savings account type card<br>3. Enter exactly 100 in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Savings account appears | medium |
| TC-021 |  | Open an account with a non-numeric initial deposit | User logged in, A funding account with sufficient balance exists | 1. Navigate to Open New Account<br>2. Select the Checking account type card<br>3. Enter 'abc' in the Initial Deposit Amount field<br>4. Select <funding account> from the Funding Source Account dropdown<br>5. Click Open Account | An error message 'Initial Deposit Amount must be numeric' is displayed; no account is opened | high |

---

## Transfer Funds

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 |  | Transfer funds between two internal ParaBank accounts | User logged in, At least two Checking or Savings accounts exist with sufficient balance | 1. Navigate to Transfer Funds from the left-hand menu<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter <transfer amount> in the Transfer Amount field<br>4. Select <source account> from the Source Account dropdown<br>5. Select <destination account> from the destination dropdown<br>6. Click Transfer | Page shows 'Transfer completed successfully.' with a transaction ID; navigating to Accounts Overview shows the source account balance decreased and the destination account balance increased by the transfer amount | high |
| TC-023 |  | Transfer funds to an external account with valid details | User logged in, A Checking or Savings account exists with sufficient balance | 1. Navigate to Transfer Funds<br>2. Select 'External Account' as the transfer type<br>3. Enter <transfer amount> in the Transfer Amount field<br>4. Select <source account> from the Source Account dropdown<br>5. Enter a valid external account number in the Account Number field<br>6. Confirm the external account number<br>7. Click Transfer | Page shows 'Transfer completed successfully.' with a transaction ID; the source account balance decreased by the transfer amount | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Attempt a fund transfer with an amount exceeding the source account balance | User logged in, A Checking or Savings account exists with a known balance | 1. Navigate to Transfer Funds<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter an amount greater than the source account balance<br>4. Select the source and a destination account<br>5. Click Transfer | An error message 'Insufficient funds' is displayed; no transfer is processed | high |
| TC-025 |  | Attempt a fund transfer to an external account with mismatched account numbers | User logged in, A Checking or Savings account exists with sufficient balance | 1. Navigate to Transfer Funds<br>2. Select 'External Account' as the transfer type<br>3. Enter <transfer amount> in the Transfer Amount field<br>4. Select <source account> from the Source Account dropdown<br>5. Enter a valid external account number in the Account Number field<br>6. Enter a different number in the Confirm Account Number field<br>7. Click Transfer | An error message 'Account numbers do not match' is displayed; no transfer is processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Transfer funds with the exact balance of the source account | User logged in, A Checking or Savings account exists with a known balance | 1. Navigate to Transfer Funds<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter the exact balance amount in the Transfer Amount field<br>4. Select the source and a destination account<br>5. Click Transfer | Page shows 'Transfer completed successfully.' with a transaction ID; the source account balance is now zero and the destination account balance increased by the transfer amount | medium |
| TC-027 |  | Transfer funds with a very large amount within system limits | User logged in, A Checking or Savings account exists with sufficient balance | 1. Navigate to Transfer Funds<br>2. Select 'My ParaBank Account' as the transfer type<br>3. Enter a very large amount (e.g., maximum allowed) in the Transfer Amount field<br>4. Select the source and a destination account<br>5. Click Transfer | Page shows 'Transfer completed successfully.' with a transaction ID; the source account balance decreased by the transfer amount | medium |

---

## Payments

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-028 |  | Submit a valid bill payment | User logged in, User has a valid source account with sufficient funds | 1. Navigate to the Payments page<br>2. Enter a valid Payee Name<br>3. Enter a valid Street Address<br>4. Enter a valid City<br>5. Select a valid State from the dropdown<br>6. Enter a valid ZIP Code<br>7. Enter a valid Phone Number<br>8. Enter a valid Payee Account Number<br>9. Enter the same Payee Account Number in the Confirm Account Number field<br>10. Enter a valid Payment Amount that is less than or equal to the available balance<br>11. Select a Source Account from the dropdown<br>12. Click Pay | Page shows 'Payment submitted successfully.' with a reference code; the source account balance is updated accordingly | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Attempt to submit a bill payment with mismatched account numbers | User logged in, User has a valid source account with sufficient funds | 1. Navigate to the Payments page<br>2. Enter a valid Payee Name<br>3. Enter a valid Street Address<br>4. Enter a valid City<br>5. Select a valid State from the dropdown<br>6. Enter a valid ZIP Code<br>7. Enter a valid Phone Number<br>8. Enter a valid Payee Account Number<br>9. Enter a different Payee Account Number in the Confirm Account Number field<br>10. Enter a valid Payment Amount<br>11. Select a Source Account from the dropdown<br>12. Click Pay | An error message 'Account numbers do not match' is displayed; the form remains editable | high |
| TC-030 |  | Attempt to submit a bill payment with insufficient funds | User logged in, User has a valid source account with insufficient funds | 1. Navigate to the Payments page<br>2. Enter a valid Payee Name<br>3. Enter a valid Street Address<br>4. Enter a valid City<br>5. Select a valid State from the dropdown<br>6. Enter a valid ZIP Code<br>7. Enter a valid Phone Number<br>8. Enter a valid Payee Account Number<br>9. Enter the same Payee Account Number in the Confirm Account Number field<br>10. Enter a Payment Amount greater than the available balance<br>11. Select a Source Account from the dropdown<br>12. Click Pay | An error message 'Insufficient funds' is displayed; the form remains editable | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Submit a bill payment with the maximum length of input fields | User logged in, User has a valid source account with sufficient funds | 1. Navigate to the Payments page<br>2. Enter a Payee Name with maximum allowed characters<br>3. Enter a Street Address with maximum allowed characters<br>4. Enter a City with maximum allowed characters<br>5. Select a valid State from the dropdown<br>6. Enter a ZIP Code with maximum allowed characters<br>7. Enter a Phone Number with maximum allowed characters<br>8. Enter a Payee Account Number with maximum allowed characters<br>9. Enter the same Payee Account Number in the Confirm Account Number field<br>10. Enter a valid Payment Amount that is less than or equal to the available balance<br>11. Select a Source Account from the dropdown<br>12. Click Pay | Page shows 'Payment submitted successfully.' with a reference code; the source account balance is updated accordingly | medium |

---

## Request Loan

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Request a Personal loan within the valid range | User logged in, User has sufficient credit history | 1. Navigate to Request Loan<br>2. Select Personal loan type card<br>3. Enter 20000 in the Loan Amount field<br>4. Enter 2000 in the Down Payment Amount field<br>5. Select a collateral account from the dropdown<br>6. Click Submit | Page shows 'Loan approved and created successfully!' with account details | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Request a loan with a down payment less than 10% of the loan amount | User logged in, User has sufficient credit history | 1. Navigate to Request Loan<br>2. Select Auto loan type card<br>3. Enter 10000 in the Loan Amount field<br>4. Enter 500 in the Down Payment Amount field<br>5. Select a collateral account from the dropdown<br>6. Click Submit | An error message 'Minimum down payment requirement is 10%' is displayed; loan request is not processed | high |
| TC-035 |  | Request a loan with insufficient collateral value | User logged in, User has sufficient credit history | 1. Navigate to Request Loan<br>2. Select Auto loan type card<br>3. Enter 30000 in the Loan Amount field<br>4. Enter 3000 in the Down Payment Amount field<br>5. Select a collateral account with less than 20% of the loan amount value<br>6. Click Submit | An error message 'Inadequate collateral value' is displayed; loan request is not processed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Request a Home loan with the exact minimum down payment | User logged in, User has sufficient credit history | 1. Navigate to Request Loan<br>2. Select Home loan type card<br>3. Enter 500000 in the Loan Amount field<br>4. Enter 10000 in the Down Payment Amount field<br>5. Select a collateral account from the dropdown<br>6. Click Submit | Page shows 'Loan approved and created successfully!' with account details | medium |
| TC-036 |  | Request a loan with the maximum allowable loan amount | User logged in, User has sufficient credit history | 1. Navigate to Request Loan<br>2. Select Home loan type card<br>3. Enter 500000 in the Loan Amount field<br>4. Enter 10000 in the Down Payment Amount field<br>5. Select a collateral account from the dropdown<br>6. Click Submit | Page shows 'Loan approved and created successfully!' with account details | medium |

---

## Update Contact Info

Total: **4** (positive: 1, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | Update contact information with valid data | User logged in, User is on the customer profile page | 1. Navigate to the customer profile page<br>2. Edit the First Name field to 'John'<br>3. Edit the Last Name field to 'Doe'<br>4. Edit the Street Address field to '123 Main St'<br>5. Edit the City field to 'Anytown'<br>6. Edit the State field to 'CA'<br>7. Edit the ZIP Code field to '90210'<br>8. Edit the Phone Number field to '(123) 456-7890'<br>9. Click the 'Update Profile' button | Page shows 'Profile updated successfully.' and the updated contact information is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Attempt to update contact information with an invalid ZIP Code | User logged in, User is on the customer profile page | 1. Navigate to the customer profile page<br>2. Edit the ZIP Code field to '1234'<br>3. Click the 'Update Profile' button | An inline error banner is displayed highlighting the ZIP Code field as invalid; the profile is not updated | high |
| TC-039 |  | Attempt to update contact information with missing required fields | User logged in, User is on the customer profile page | 1. Navigate to the customer profile page<br>2. Clear the First Name field<br>3. Click the 'Update Profile' button | An inline error banner is displayed highlighting the First Name field as required; the profile is not updated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Update contact information with maximum length fields | User logged in, User is on the customer profile page | 1. Navigate to the customer profile page<br>2. Edit the First Name field to 'A very long first name that exceeds typical length'<br>3. Edit the Last Name field to 'A very long last name that exceeds typical length'<br>4. Edit the Street Address field to '123 A very long street address that exceeds typical length'<br>5. Edit the City field to 'A very long city name that exceeds typical length'<br>6. Edit the State field to 'California'<br>7. Edit the ZIP Code field to '90210'<br>8. Edit the Phone Number field to '(123) 456-7890'<br>9. Click the 'Update Profile' button | Page shows 'Profile updated successfully.' and the updated contact information is displayed, assuming the system accepts the maximum lengths | medium |

---

## Manage Cards

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | Request a new Debit card with valid details | User logged in, User has a valid account in good standing, User has a complete shipping address | 1. Navigate to Manage Cards<br>2. Select 'Debit' as the Card Type<br>3. Select an account to link from the dropdown<br>4. Enter a complete shipping address<br>5. Click 'Request Card' | Page shows 'Card request submitted successfully.' with a tracking ID | high |
| TC-044 |  | Update card controls with valid new spending limit | User logged in, User has an existing card | 1. Navigate to Manage Cards<br>2. Select an existing card from the dropdown<br>3. Enter a valid new spending limit within policy<br>4. Click 'Update Controls' | Page shows 'Card controls updated successfully.' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Attempt to request a card with an incomplete shipping address | User logged in, User has a valid account in good standing | 1. Navigate to Manage Cards<br>2. Select 'Credit' as the Card Type<br>3. Select an account to link from the dropdown<br>4. Enter an incomplete shipping address<br>5. Click 'Request Card' | An error message indicating 'Shipping address is incomplete' is displayed; no card request is submitted | high |
| TC-045 |  | Attempt to update card controls with a spending limit above policy | User logged in, User has an existing card | 1. Navigate to Manage Cards<br>2. Select an existing card from the dropdown<br>3. Enter a spending limit above the allowed maximum<br>4. Click 'Update Controls' | An inline error message indicating 'Spending limit exceeds policy' is displayed; form remains editable | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Request a new Credit card with maximum allowed shipping address length | User logged in, User has a valid account in good standing | 1. Navigate to Manage Cards<br>2. Select 'Credit' as the Card Type<br>3. Select an account to link from the dropdown<br>4. Enter a shipping address with the maximum allowed character length<br>5. Click 'Request Card' | Page shows 'Card request submitted successfully.' with a tracking ID | medium |
| TC-046 |  | Update card controls with a spending limit of zero | User logged in, User has an existing card | 1. Navigate to Manage Cards<br>2. Select an existing card from the dropdown<br>3. Enter '0' in the New Spending Limit field<br>4. Click 'Update Controls' | An inline error message indicating 'Spending limit cannot be zero' is displayed; form remains editable | medium |

---

## Investments

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Execute a successful trade for a valid fund symbol | User logged in, User has sufficient buying power, Valid fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol in the Fund Symbol field<br>4. Enter a quantity greater than zero in the Quantity field<br>5. Select a funding account from the Funding Account dropdown<br>6. Click 'Execute Trade' | Page shows 'Trade executed successfully.' with an order ID; portfolio snapshot updates to reflect new holdings | high |
| TC-051 |  | Create a recurring investment plan with valid inputs | User logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol in the Fund Symbol field<br>3. Enter a valid contribution amount in the Contribution Amount field<br>4. Select 'Weekly' or 'Monthly' from the Frequency dropdown<br>5. Enter a future date in the Start Date field<br>6. Select a funding account from the Funding Account dropdown<br>7. Click 'Create Plan' | Page shows 'Plan created successfully.'; the recurring investment plan appears in the user's plans | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Attempt to execute a trade with an invalid fund symbol | User logged in, User has sufficient buying power | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter an invalid fund symbol in the Fund Symbol field<br>4. Enter a valid quantity greater than zero<br>5. Select a funding account from the Funding Account dropdown<br>6. Click 'Execute Trade' | An inline error message 'Fund symbol does not exist' is displayed; no trade is executed | high |
| TC-049 |  | Attempt to execute a trade with insufficient buying power | User logged in, User has insufficient buying power, Valid fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol in the Fund Symbol field<br>4. Enter a quantity that exceeds the buying power<br>5. Select a funding account from the Funding Account dropdown<br>6. Click 'Execute Trade' | An inline error message 'Insufficient buying power' is displayed; no trade is executed | high |
| TC-052 |  | Attempt to create a recurring investment plan with a past start date | User logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol in the Fund Symbol field<br>3. Enter a valid contribution amount in the Contribution Amount field<br>4. Select 'Weekly' or 'Monthly' from the Frequency dropdown<br>5. Enter a past date in the Start Date field<br>6. Select a funding account from the Funding Account dropdown<br>7. Click 'Create Plan' | An inline error message 'Start date must be in the future' is displayed; no plan is created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Execute a trade with the maximum allowable quantity | User logged in, User has sufficient buying power, Valid fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol in the Fund Symbol field<br>4. Enter the maximum allowable quantity in the Quantity field<br>5. Select a funding account from the Funding Account dropdown<br>6. Click 'Execute Trade' | Page shows 'Trade executed successfully.' with an order ID; portfolio snapshot updates to reflect new holdings | medium |
| TC-053 |  | Create a recurring investment plan with the minimum contribution amount | User logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol in the Fund Symbol field<br>3. Enter the minimum contribution amount in the Contribution Amount field<br>4. Select 'Weekly' or 'Monthly' from the Frequency dropdown<br>5. Enter a future date in the Start Date field<br>6. Select a funding account from the Funding Account dropdown<br>7. Click 'Create Plan' | Page shows 'Plan created successfully.'; the recurring investment plan appears in the user's plans | medium |

---

## Account Statements

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Generate a statement for a valid date range | User logged in, At least one account exists with transactions in the selected date range | 1. Navigate to the Statements page<br>2. Select a valid month-and-year or custom date range in the Statement Period field<br>3. Select an account from the Account dropdown<br>4. Click Generate Statement | Page shows 'Statement generated successfully.' and displays the relevant transactions for the selected period | high |
| TC-057 |  | Update e-statement preference with a valid email address | User logged in | 1. Navigate to the Statements page<br>2. Check the checkbox to opt into paperless statements<br>3. Enter a valid email address in the Email Address field<br>4. Click Save Preference | Page shows 'e-Statement preference updated.' and the preference is saved | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Attempt to generate a statement with an invalid date range | User logged in, At least one account exists | 1. Navigate to the Statements page<br>2. Enter an invalid date range in the Statement Period field<br>3. Select an account from the Account dropdown<br>4. Click Generate Statement | An error message 'Unable to generate statement — please try again later.' is displayed; no statement is generated | high |
| TC-058 |  | Attempt to update e-statement preference with an invalid email address | User logged in | 1. Navigate to the Statements page<br>2. Check the checkbox to opt into paperless statements<br>3. Enter an invalid email address in the Email Address field<br>4. Click Save Preference | The email field is highlighted with guidance on the valid email format; preference is not updated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Generate a statement for the maximum date range | User logged in, At least one account exists with transactions spanning the maximum date range | 1. Navigate to the Statements page<br>2. Select the maximum allowable date range in the Statement Period field<br>3. Select an account from the Account dropdown<br>4. Click Generate Statement | Page shows 'Statement generated successfully.' and displays the relevant transactions for the maximum date range | medium |
| TC-059 |  | Update e-statement preference with an email address at maximum length | User logged in | 1. Navigate to the Statements page<br>2. Check the checkbox to opt into paperless statements<br>3. Enter an email address with the maximum allowed length in the Email Address field<br>4. Click Save Preference | Page shows 'e-Statement preference updated.' and the preference is saved | medium |

---

## Security Settings

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Change password with valid current and new passwords | User logged in, User knows the current password | 1. Navigate to Security Settings<br>2. Enter valid current password in the Current Password field<br>3. Enter a strong new password in the New Password field<br>4. Confirm the new password in the Confirm New Password field<br>5. Click Change Password | Page shows 'Password changed successfully.' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Attempt to change password with incorrect current password | User logged in, User knows the correct current password | 1. Navigate to Security Settings<br>2. Enter an incorrect current password in the Current Password field<br>3. Enter a strong new password in the New Password field<br>4. Confirm the new password in the Confirm New Password field<br>5. Click Change Password | An error message 'Current password is incorrect' is displayed; password is not changed. | high |
| TC-062 |  | Attempt to change password with non-matching new passwords | User logged in, User knows the current password | 1. Navigate to Security Settings<br>2. Enter valid current password in the Current Password field<br>3. Enter a strong new password in the New Password field<br>4. Enter a different password in the Confirm New Password field<br>5. Click Change Password | An error message 'New passwords do not match' is displayed; password is not changed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | Change password with the maximum length for new password | User logged in, User knows the current password | 1. Navigate to Security Settings<br>2. Enter valid current password in the Current Password field<br>3. Enter a new password with the maximum allowed length in the New Password field<br>4. Confirm the new password in the Confirm New Password field<br>5. Click Change Password | Page shows 'Password changed successfully.' | medium |
| TC-064 |  | Change password with a weak password that meets length requirement | User logged in, User knows the current password | 1. Navigate to Security Settings<br>2. Enter valid current password in the Current Password field<br>3. Enter a weak password (e.g., 'password123') in the New Password field<br>4. Confirm the weak password in the Confirm New Password field<br>5. Click Change Password | An error message indicating 'Password does not meet strength requirements' is displayed; password is not changed. | high |

---

## Support Center

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Send a secure message with valid inputs | User logged in | 1. Navigate to the Support Center page<br>2. Select 'Account' from the Category dropdown<br>3. Enter a valid subject in the Subject field<br>4. Enter a message in the Message Body field<br>5. Optionally attach a valid file<br>6. Click the 'Send Message' button | Page shows 'Message sent successfully.' with a ticket ID | high |
| TC-069 |  | Request a callback with valid inputs | User logged in | 1. Navigate to the Support Center page<br>2. Select a reason for the call from the Reason for Call dropdown<br>3. Enter a valid date that is at least the next business day<br>4. Select a preferred time window<br>5. Verify the Phone Number field is pre-filled and editable<br>6. Click the 'Request Callback' button | Page shows 'Callback request submitted.' and an email confirmation is sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-066 |  | Attempt to send a secure message without a message body | User logged in | 1. Navigate to the Support Center page<br>2. Select 'Technical' from the Category dropdown<br>3. Enter a valid subject in the Subject field<br>4. Leave the Message Body field empty<br>5. Click the 'Send Message' button | An inline error message indicates 'Message body is required.'; no message is sent | high |
| TC-067 |  | Attempt to send a secure message with an invalid attachment type | User logged in | 1. Navigate to the Support Center page<br>2. Select 'Other' from the Category dropdown<br>3. Enter a valid subject in the Subject field<br>4. Enter a message in the Message Body field<br>5. Attach an invalid file type (e.g., .exe)<br>6. Click the 'Send Message' button | An inline error message indicates 'Invalid attachment type.'; no message is sent | high |
| TC-070 |  | Request a callback with an invalid phone number format | User logged in | 1. Navigate to the Support Center page<br>2. Select a reason for the call from the Reason for Call dropdown<br>3. Enter a valid date that is at least the next business day<br>4. Select a preferred time window<br>5. Enter an invalid phone number format (e.g., '12345')<br>6. Click the 'Request Callback' button | An inline error message indicates 'Invalid phone number format.'; no callback request is submitted | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Send a secure message with the maximum allowed subject length | User logged in | 1. Navigate to the Support Center page<br>2. Select 'Security' from the Category dropdown<br>3. Enter a subject with the maximum allowed length (e.g., 255 characters)<br>4. Enter a message in the Message Body field<br>5. Click the 'Send Message' button | Page shows 'Message sent successfully.' with a ticket ID | medium |
| TC-071 |  | Request a callback for the earliest possible date | User logged in | 1. Navigate to the Support Center page<br>2. Select a reason for the call from the Reason for Call dropdown<br>3. Enter tomorrow's date as the Preferred Date<br>4. Select a preferred time window<br>5. Click the 'Request Callback' button | Page shows 'Callback request submitted.' and an email confirmation is sent | medium |

---
