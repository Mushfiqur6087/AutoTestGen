# Test Cases — Parabank

Generated: 2026-06-04T14:58:51.971506Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 92 | 21 | 36 | 35 | 56 | 35 | 1 |

## Login

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User has a registered account with valid email and password. | 1. Navigate to the login page.<br>2. Enter valid email in the Email/Username field.<br>3. Enter valid password in the Password field.<br>4. Click on the 'Sign In' button. | User sees 'Signed in successfully.' and is redirected to the Accounts Overview page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login attempt with incorrect password | User has a registered account with valid email and incorrect password. | 1. Navigate to the login page.<br>2. Enter valid email in the Email/Username field.<br>3. Enter incorrect password in the Password field.<br>4. Click on the 'Sign In' button. | User sees 'Incorrect email or password. Please try again,' and the password field is cleared. | high |
| TC-003 |  | Login attempt with unregistered email | User does not have an account. | 1. Navigate to the login page.<br>2. Enter unregistered email in the Email/Username field.<br>3. Enter any password in the Password field.<br>4. Click on the 'Sign In' button. | User sees 'Incorrect email or password. Please try again,' and the password field is cleared. | high |
| TC-004 |  | Login attempt with empty fields |  | 1. Navigate to the login page.<br>2. Leave the Email/Username field empty.<br>3. Leave the Password field empty.<br>4. Click on the 'Sign In' button. | User sees error messages indicating that both fields are required. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Login attempt with maximum length email and password | User has a registered account with maximum length email and password. | 1. Navigate to the login page.<br>2. Enter maximum length valid email in the Email/Username field.<br>3. Enter maximum length valid password in the Password field.<br>4. Click on the 'Sign In' button. | User sees 'Signed in successfully.' and is redirected to the Accounts Overview page. | medium |
| TC-006 |  | Login attempt with email in invalid format |  | 1. Navigate to the login page.<br>2. Enter an invalid email format in the Email/Username field.<br>3. Enter any password in the Password field.<br>4. Click on the 'Sign In' button. | User sees error message indicating that the email format is invalid. | medium |
| TC-007 |  | Login attempt with password missing required characters |  | 1. Navigate to the login page.<br>2. Enter valid email in the Email/Username field.<br>3. Enter a password that is less than 8 characters or missing required character types.<br>4. Click on the 'Sign In' button. | User sees error message indicating that the password does not meet the requirements. | medium |

---

## Register

Total: **9** (positive: 1, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Successful registration with valid inputs |  | 1. Navigate to the registration page.<br>2. Fill in all required fields with valid data.<br>3. Click the 'Register' button. | Account created successfully — please sign in, then redirect to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Registration with invalid email format |  | 1. Navigate to the registration page.<br>2. Enter an invalid email format in the Username field.<br>3. Fill in all other required fields with valid data.<br>4. Click the 'Register' button. | Error message indicating invalid email format is displayed. | high |
| TC-010 |  | Registration with mismatched passwords |  | 1. Navigate to the registration page.<br>2. Fill in all required fields with valid data.<br>3. Enter a different value in the Confirm Password field than in the Password field.<br>4. Click the 'Register' button. | Error message indicating passwords do not match is displayed. | high |
| TC-013 |  | Registration with invalid phone number format |  | 1. Navigate to the registration page.<br>2. Enter an invalid phone number format in the Phone Number field.<br>3. Fill in all other required fields with valid data.<br>4. Click the 'Register' button. | Error message indicating invalid phone number format is displayed. | high |
| TC-015 |  | Registration with invalid ZIP Code format |  | 1. Navigate to the registration page.<br>2. Enter an invalid ZIP Code format in the ZIP Code field.<br>3. Fill in all other required fields with valid data.<br>4. Click the 'Register' button. | Error message indicating invalid ZIP Code format is displayed. | high |
| TC-016 |  | Registration with invalid SSN format |  | 1. Navigate to the registration page.<br>2. Enter an invalid SSN format in the Social Security Number field.<br>3. Fill in all other required fields with valid data.<br>4. Click the 'Register' button. | Error message indicating invalid SSN format is displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 |  | Registration with maximum length username |  | 1. Navigate to the registration page.<br>2. Enter a valid email with maximum length (e.g., 254 characters) in the Username field.<br>3. Fill in all other required fields with valid data.<br>4. Click the 'Register' button. | Account created successfully — please sign in, then redirect to the login page. | medium |
| TC-012 |  | Registration with empty fields |  | 1. Navigate to the registration page.<br>2. Leave all fields empty.<br>3. Click the 'Register' button. | Error messages indicating all fields are required are displayed. | high |
| TC-014 |  | Registration with maximum length password |  | 1. Navigate to the registration page.<br>2. Enter a password with maximum length (e.g., 128 characters) in the Password field.<br>3. Enter the same value in the Confirm Password field.<br>4. Fill in all other required fields with valid data.<br>5. Click the 'Register' button. | Account created successfully — please sign in, then redirect to the login page. | medium |

---

## Accounts Overview

Total: **7** (positive: 3, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Display welcome message with user's name | User is logged in | 1. Navigate to the Accounts Overview module. | The dashboard displays a welcome message with the user's name. | high |
| TC-018 |  | Display customer accounts table | User is logged in, User has customer accounts | 1. Navigate to the Accounts Overview module. | A table of all customer accounts is displayed with correct details. | high |
| TC-022 |  | Display total balance in footer | User is logged in, User has customer accounts | 1. Navigate to the Accounts Overview module. | The footer row displays the correct total balance across all accounts. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Display accounts table when user has no accounts | User is logged in, User has no customer accounts | 1. Navigate to the Accounts Overview module. | A message indicating that no accounts are available is displayed. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Display accounts with maximum number of accounts | User is logged in, User has maximum allowed customer accounts | 1. Navigate to the Accounts Overview module. | All customer accounts are displayed correctly in the table, ordered by open date. | medium |
| TC-021 |  | Display accounts with edge case account numbers | User is logged in, User has accounts with edge case account numbers | 1. Navigate to the Accounts Overview module. | Account numbers are masked correctly, showing only the last 4 digits. | low |
| TC-023 |  | Display accounts with varying account statuses | User is logged in, User has accounts with different statuses | 1. Navigate to the Accounts Overview module. | All accounts are displayed with their respective statuses, including active badges. | medium |

---

## Open New Account

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | Open Checking Account with Valid Deposit | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Checking' account type<br>2. Enter '50' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Account opened successfully! User is redirected to accounts overview. | high |
| TC-025 |  | Open Savings Account with Valid Deposit | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Savings' account type<br>2. Enter '150' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Account opened successfully! User is redirected to accounts overview. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Open Account without Selecting Account Type | User is on the Open New Account page | 1. Leave account type unselected<br>2. Enter '50' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Error message indicating that account type must be selected. | high |
| TC-027 |  | Open Account with Insufficient Deposit for Checking | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Checking' account type<br>2. Enter '10' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Error message indicating that the deposit amount must be at least $25. | high |
| TC-028 |  | Open Account with Insufficient Deposit for Savings | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Savings' account type<br>2. Enter '50' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Error message indicating that the deposit amount must be at least $100. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Open Account with Maximum Deposit Amount | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Checking' account type<br>2. Enter '999999' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Account opened successfully! User is redirected to accounts overview. | medium |
| TC-030 |  | Open Account with Zero Deposit Amount | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Savings' account type<br>2. Enter '0' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Error message indicating that the deposit amount must be greater than $0. | medium |
| TC-031 |  | Open Account with Non-Numeric Deposit Amount | User is on the Open New Account page, User has a valid funding source with sufficient balance | 1. Select 'Checking' account type<br>2. Enter 'abc' in the Initial Deposit Amount field<br>3. Select a funding source account from the dropdown<br>4. Click on 'Open Account' button | Error message indicating that the deposit amount must be numeric. | medium |

---

## Transfer Funds

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Successful internal transfer | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'My ParaBank Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter a valid transfer amount<br>5. Click on 'Transfer' button | Transfer completed successfully. Transaction ID is displayed. | high |
| TC-033 |  | Successful external transfer | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'External Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter a valid transfer amount<br>5. Enter a valid external account number<br>6. Confirm the external account number<br>7. Click on 'Transfer' button | Transfer completed successfully. Transaction ID is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Transfer with insufficient funds | User is logged in, User has insufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'My ParaBank Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter a transfer amount greater than the available balance<br>5. Click on 'Transfer' button | Error message 'Insufficient funds' is displayed. | high |
| TC-035 |  | Transfer with mismatched external account numbers | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'External Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter a valid transfer amount<br>5. Enter a valid external account number<br>6. Enter a different external account number in confirmation<br>7. Click on 'Transfer' button | Error message 'Account numbers do not match' is displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Transfer with zero amount | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'My ParaBank Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter '0' in the transfer amount field<br>5. Click on 'Transfer' button | Error message indicating that the transfer amount must be greater than zero is displayed. | medium |
| TC-037 |  | Transfer with maximum length account number | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'External Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Enter a valid transfer amount<br>5. Enter a maximum length valid external account number<br>6. Confirm the external account number<br>7. Click on 'Transfer' button | Transfer completed successfully. Transaction ID is displayed. | medium |
| TC-038 |  | Transfer with empty transfer amount | User is logged in, User has sufficient funds in the selected account | 1. Navigate to the Transfer Funds page<br>2. Select 'My ParaBank Account' as transfer type<br>3. Select a source account from the dropdown<br>4. Leave the transfer amount field empty<br>5. Click on 'Transfer' button | Error message indicating that the transfer amount is required is displayed. | medium |

---

## Payments

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Successful payment submission | User is logged in, User has sufficient funds | 1. Navigate to the bill-payment page.<br>2. Fill in all required fields with valid data.<br>3. Click the 'Pay' button. | Payment submitted successfully with a reference code displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Account numbers do not match | User is logged in | 1. Navigate to the bill-payment page.<br>2. Fill in all fields with valid data except for Payee Account Number and Confirm Account Number (make them different).<br>3. Click the 'Pay' button. | Error message 'Account numbers do not match' is displayed inline. | high |
| TC-041 |  | Insufficient funds | User is logged in, User has insufficient funds | 1. Navigate to the bill-payment page.<br>2. Fill in all fields with valid data.<br>3. Click the 'Pay' button. | Error message 'Insufficient funds' is displayed inline. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Empty fields submission | User is logged in | 1. Navigate to the bill-payment page.<br>2. Leave all fields empty.<br>3. Click the 'Pay' button. | Error messages for all required fields are displayed inline. | medium |
| TC-043 |  | Maximum length input | User is logged in | 1. Navigate to the bill-payment page.<br>2. Fill in all fields with maximum allowed character lengths.<br>3. Click the 'Pay' button. | Payment submitted successfully with a reference code displayed. | medium |
| TC-044 |  | Boundary value for payment amount | User is logged in, User has sufficient funds | 1. Navigate to the bill-payment page.<br>2. Fill in all fields with valid data and set Payment Amount to the exact available balance.<br>3. Click the 'Pay' button. | Payment submitted successfully with a reference code displayed. | medium |

---

## Request Loan

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Successful Personal Loan Request | User is on the loan request page, User selects Personal loan type | 1. Enter loan amount as $10,000<br>2. Enter down payment as $1,000<br>3. Select collateral account with sufficient funds<br>4. Submit the loan request | Loan approved and created successfully! Account details are displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Loan Amount Below Minimum for Auto Loan | User is on the loan request page, User selects Auto loan type | 1. Enter loan amount as $4,000<br>2. Enter down payment as $500<br>3. Select collateral account<br>4. Submit the loan request | Error message indicating loan amount is below the minimum required for Auto loan. | high |
| TC-047 |  | Down Payment Greater Than Loan Amount | User is on the loan request page, User selects Home loan type | 1. Enter loan amount as $100,000<br>2. Enter down payment as $120,000<br>3. Select collateral account<br>4. Submit the loan request | Error message indicating down payment must be less than loan amount. | high |
| TC-050 |  | Insufficient Collateral Value | User is on the loan request page, User selects Auto loan type | 1. Enter loan amount as $20,000<br>2. Enter down payment as $2,000<br>3. Select collateral account with insufficient funds<br>4. Submit the loan request | Error message indicating inadequate collateral value. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Maximum Loan Amount for Home Loan | User is on the loan request page, User selects Home loan type | 1. Enter loan amount as $500,000<br>2. Enter down payment as $100,000<br>3. Select collateral account with sufficient funds<br>4. Submit the loan request | Loan approved and created successfully! Account details are displayed. | medium |
| TC-049 |  | Minimum Down Payment for Personal Loan | User is on the loan request page, User selects Personal loan type | 1. Enter loan amount as $5,000<br>2. Enter down payment as $500<br>3. Select collateral account with sufficient funds<br>4. Submit the loan request | Loan approved and created successfully! Account details are displayed. | medium |
| TC-051 |  | Empty Loan Amount Field | User is on the loan request page, User selects Home loan type | 1. Leave loan amount field empty<br>2. Enter down payment as $10,000<br>3. Select collateral account<br>4. Submit the loan request | Error message indicating loan amount is required. | high |

---

## Update Contact Info

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Update profile with valid data | User is logged in, User is on the customer profile page | 1. Edit the First Name to 'John'<br>2. Edit the Last Name to 'Doe'<br>3. Edit the Street Address to '123 Main St'<br>4. Edit the City to 'Anytown'<br>5. Edit the State to 'CA'<br>6. Edit the ZIP Code to '90210'<br>7. Edit the Phone Number to '123-456-7890'<br>8. Click the 'Update Profile' button | Profile updated successfully. The data is refreshed with the new values. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-053 |  | Attempt to update profile with missing First Name | User is logged in, User is on the customer profile page | 1. Leave the First Name field empty<br>2. Fill in Last Name with 'Doe'<br>3. Fill in Street Address with '123 Main St'<br>4. Fill in City with 'Anytown'<br>5. Fill in State with 'CA'<br>6. Fill in ZIP Code with '90210'<br>7. Fill in Phone Number with '123-456-7890'<br>8. Click the 'Update Profile' button | Inline error banner displays 'First Name is required.' and highlights the First Name field. | high |
| TC-054 |  | Attempt to update profile with invalid ZIP Code | User is logged in, User is on the customer profile page | 1. Edit the First Name to 'John'<br>2. Edit the Last Name to 'Doe'<br>3. Edit the Street Address to '123 Main St'<br>4. Edit the City to 'Anytown'<br>5. Edit the State to 'CA'<br>6. Edit the ZIP Code to 'ABCDE'<br>7. Edit the Phone Number to '123-456-7890'<br>8. Click the 'Update Profile' button | Inline error banner displays 'Invalid ZIP Code format.' and highlights the ZIP Code field. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Update profile with maximum length fields | User is logged in, User is on the customer profile page | 1. Edit the First Name to 'JohnathanMaxLength'<br>2. Edit the Last Name to 'DoeMaximumLength'<br>3. Edit the Street Address to '123 Main Street, Apartment 456, Very Long Address'<br>4. Edit the City to 'AnytownVeryLongCityName'<br>5. Edit the State to 'California'<br>6. Edit the ZIP Code to '99999'<br>7. Edit the Phone Number to '123-456-7890'<br>8. Click the 'Update Profile' button | Profile updated successfully. The data is refreshed with the new values. | medium |
| TC-056 |  | Update profile with empty fields | User is logged in, User is on the customer profile page | 1. Leave all fields empty<br>2. Click the 'Update Profile' button | Inline error banner displays 'All fields are required.' and highlights all fields. | high |

---

## Manage Cards

Total: **8** (positive: 2, negative: 4, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-057 |  | Submit valid card request | User is logged in, User has a valid account with good standing | 1. Navigate to the Manage Cards page.<br>2. Select 'Debit' as Card Type.<br>3. Choose a valid account to link.<br>4. Enter a complete shipping address.<br>5. Click on 'Request Card' button. | System shows 'Card request submitted successfully.' with a tracking ID. | high |
| TC-061 |  | Update card controls with valid inputs | User is logged in, User has an existing card | 1. Navigate to the Manage Cards page.<br>2. Select an existing card from the dropdown.<br>3. Enter a new spending limit within policy.<br>4. Optionally enter travel notice dates and destinations.<br>5. Set Card Status to 'Active'.<br>6. Click on 'Update Controls' button. | System shows 'Card controls updated successfully.' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | Submit card request with incomplete address | User is logged in, User has a valid account with good standing | 1. Navigate to the Manage Cards page.<br>2. Select 'Credit' as Card Type.<br>3. Choose a valid account to link.<br>4. Enter an incomplete shipping address.<br>5. Click on 'Request Card' button. | System shows an error message indicating the address is incomplete. | high |
| TC-059 |  | Submit card request with invalid account status | User is logged in, User has a valid account with bad standing | 1. Navigate to the Manage Cards page.<br>2. Select 'Debit' as Card Type.<br>3. Choose an account with bad standing.<br>4. Enter a complete shipping address.<br>5. Click on 'Request Card' button. | System shows an error message indicating the account is not in good standing. | high |
| TC-062 |  | Update card controls with spending limit above policy | User is logged in, User has an existing card | 1. Navigate to the Manage Cards page.<br>2. Select an existing card from the dropdown.<br>3. Enter a new spending limit above the allowed policy.<br>4. Click on 'Update Controls' button. | System shows an inline error message indicating the limit exceeds policy. | high |
| TC-064 |  | Update card controls with invalid travel notice dates | User is logged in, User has an existing card | 1. Navigate to the Manage Cards page.<br>2. Select an existing card from the dropdown.<br>3. Enter valid spending limit.<br>4. Enter travel notice dates that are in the past.<br>5. Click on 'Update Controls' button. | System shows an inline error message indicating the travel notice dates are invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | Submit card request with maximum length address | User is logged in, User has a valid account with good standing | 1. Navigate to the Manage Cards page.<br>2. Select 'Debit' as Card Type.<br>3. Choose a valid account to link.<br>4. Enter a shipping address at the maximum allowed length.<br>5. Click on 'Request Card' button. | System shows 'Card request submitted successfully.' with a tracking ID. | medium |
| TC-063 |  | Update card controls with maximum spending limit | User is logged in, User has an existing card | 1. Navigate to the Manage Cards page.<br>2. Select an existing card from the dropdown.<br>3. Enter the maximum allowed spending limit.<br>4. Click on 'Update Controls' button. | System shows 'Card controls updated successfully.' | medium |

---

## Investments

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Successful Buy Trade Execution | User is logged in, User has sufficient buying power, Fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol<br>4. Enter a quantity greater than zero<br>5. Select a funding account<br>6. Click on 'Execute Trade' | Trade executed successfully. Order ID is displayed. | high |
| TC-066 |  | Successful Recurring Investment Plan Creation | User is logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol<br>3. Enter a contribution amount that meets the minimum<br>4. Select frequency (Weekly or Monthly)<br>5. Enter a start date in the future<br>6. Select a funding account<br>7. Click on 'Create Plan' | Plan created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Trade Execution with Insufficient Buying Power | User is logged in, User has insufficient buying power, Fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol<br>4. Enter a quantity greater than zero<br>5. Select a funding account<br>6. Click on 'Execute Trade' | Error message indicating insufficient buying power is displayed. | high |
| TC-068 |  | Trade Execution with Non-Existent Fund Symbol | User is logged in | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a non-existent fund symbol<br>4. Enter a quantity greater than zero<br>5. Select a funding account<br>6. Click on 'Execute Trade' | Error message indicating that the fund symbol does not exist is displayed. | high |
| TC-069 |  | Recurring Investment Plan Creation with Past Start Date | User is logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol<br>3. Enter a contribution amount that meets the minimum<br>4. Select frequency (Weekly or Monthly)<br>5. Enter a start date in the past<br>6. Select a funding account<br>7. Click on 'Create Plan' | Error message indicating that the start date must be in the future is displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-070 |  | Trade Execution with Maximum Quantity | User is logged in, User has sufficient buying power, Fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol<br>4. Enter the maximum allowable quantity<br>5. Select a funding account<br>6. Click on 'Execute Trade' | Trade executed successfully. Order ID is displayed. | medium |
| TC-071 |  | Recurring Investment Plan Creation with Minimum Contribution Amount | User is logged in, User has sufficient balance in the funding account | 1. Navigate to the Investments page<br>2. Enter a valid fund symbol<br>3. Enter the minimum contribution amount<br>4. Select frequency (Weekly or Monthly)<br>5. Enter a start date in the future<br>6. Select a funding account<br>7. Click on 'Create Plan' | Plan created successfully. | medium |
| TC-072 |  | Trade Execution with Zero Quantity | User is logged in, Fund symbol exists | 1. Navigate to the Investments page<br>2. Select 'Buy' from the Action dropdown<br>3. Enter a valid fund symbol<br>4. Enter a quantity of zero<br>5. Select a funding account<br>6. Click on 'Execute Trade' | Error message indicating quantity must be greater than zero is displayed. | medium |

---

## Account Statements

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-073 |  | Generate statement with valid date range | User is logged in, User has at least one account | 1. Navigate to the Statements page.<br>2. Select a valid month-and-year or custom date range.<br>3. Choose an account from the dropdown.<br>4. Click on the 'Generate Statement' button. | Statement generated successfully. | high |
| TC-076 |  | Save e-statement preference with valid email | User is logged in | 1. Navigate to the Statements page.<br>2. Check the checkbox for paperless statements.<br>3. Enter a valid email address in the Email Address field.<br>4. Click on the 'Save Preference' button. | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-074 |  | Generate statement with invalid date range | User is logged in, User has at least one account | 1. Navigate to the Statements page.<br>2. Select an invalid date range (e.g., end date before start date).<br>3. Choose an account from the dropdown.<br>4. Click on the 'Generate Statement' button. | Unable to generate statement — please try again later. | high |
| TC-077 |  | Save e-statement preference with invalid email | User is logged in | 1. Navigate to the Statements page.<br>2. Check the checkbox for paperless statements.<br>3. Enter an invalid email address in the Email Address field (e.g., 'invalid-email').<br>4. Click on the 'Save Preference' button. | Email field highlighted with guidance. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-075 |  | Generate statement with maximum date range | User is logged in, User has at least one account | 1. Navigate to the Statements page.<br>2. Select the maximum allowed date range (e.g., 1 year).<br>3. Choose an account from the dropdown.<br>4. Click on the 'Generate Statement' button. | Statement generated successfully. | medium |
| TC-078 |  | Save e-statement preference with maximum length email | User is logged in | 1. Navigate to the Statements page.<br>2. Check the checkbox for paperless statements.<br>3. Enter an email address at the maximum allowed length (e.g., 254 characters).<br>4. Click on the 'Save Preference' button. | e-Statement preference updated. | medium |
| TC-079 |  | Generate statement with empty fields | User is logged in, User has at least one account | 1. Navigate to the Statements page.<br>2. Leave the Statement Period field empty.<br>3. Choose an account from the dropdown.<br>4. Click on the 'Generate Statement' button. | Unable to generate statement — please try again later. | medium |

---

## Security Settings

Total: **6** (positive: 1, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-080 |  | Change password successfully with valid inputs | User is logged in, Current password is known | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Enter the current password in the Current Password field.<br>4. Enter a valid new password in the New Password field.<br>5. Confirm the new password in the Confirm New Password field.<br>6. Click the Change Password button. | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-081 |  | Attempt to change password with incorrect current password | User is logged in, Current password is known | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Enter an incorrect current password in the Current Password field.<br>4. Enter a valid new password in the New Password field.<br>5. Confirm the new password in the Confirm New Password field.<br>6. Click the Change Password button. | Error message indicating the current password is incorrect. | high |
| TC-082 |  | Attempt to change password with non-matching new passwords | User is logged in, Current password is known | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Enter the current password in the Current Password field.<br>4. Enter a valid new password in the New Password field.<br>5. Enter a different password in the Confirm New Password field.<br>6. Click the Change Password button. | Error message indicating the new passwords do not match. | high |
| TC-083 |  | Attempt to change password with empty fields | User is logged in | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Leave all fields empty.<br>4. Click the Change Password button. | Error messages indicating that all fields are required. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-084 |  | Change password with maximum length password | User is logged in, Current password is known | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Enter the current password in the Current Password field.<br>4. Enter a new password of maximum allowed length in the New Password field.<br>5. Confirm the new password in the Confirm New Password field.<br>6. Click the Change Password button. | Password changed successfully. | medium |
| TC-085 |  | Change password with a strong password containing special characters | User is logged in, Current password is known | 1. Navigate to the Security Settings page.<br>2. Expand the change password panel.<br>3. Enter the current password in the Current Password field.<br>4. Enter a strong password with special characters in the New Password field.<br>5. Confirm the new password in the Confirm New Password field.<br>6. Click the Change Password button. | Password changed successfully. | medium |

---

## Support Center

Total: **7** (positive: 2, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-086 |  | Send a secure message successfully | User is logged in, User is on the Support Center page | 1. Enter a valid subject in the Subject field.<br>2. Select a category from the dropdown.<br>3. Enter a message in the Message Body.<br>4. Optionally attach a valid file.<br>5. Click on the 'Send Message' button. | Message sent successfully. Ticket ID is displayed. | high |
| TC-090 |  | Request a callback successfully | User is logged in, User is on the Support Center page | 1. Select a reason for the call from the dropdown.<br>2. Select a preferred date that is at least the next business day.<br>3. Select a preferred time window.<br>4. Verify the Phone Number is pre-filled and editable.<br>5. Click on the 'Request Callback' button. | Callback request submitted. An email confirmation is sent. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-087 |  | Attempt to send a secure message without a message body | User is logged in, User is on the Support Center page | 1. Enter a valid subject in the Subject field.<br>2. Select a category from the dropdown.<br>3. Leave the Message Body empty.<br>4. Click on the 'Send Message' button. | Inline guidance shows an error message indicating that the message body is required. | high |
| TC-088 |  | Attempt to send a secure message with an invalid attachment type | User is logged in, User is on the Support Center page | 1. Enter a valid subject in the Subject field.<br>2. Select a category from the dropdown.<br>3. Enter a message in the Message Body.<br>4. Attach an invalid file type (e.g., .exe).<br>5. Click on the 'Send Message' button. | Inline guidance shows an error message indicating that the attachment type is not allowed. | medium |
| TC-091 |  | Attempt to request a callback with an invalid phone number format | User is logged in, User is on the Support Center page | 1. Select a reason for the call from the dropdown.<br>2. Select a preferred date that is at least the next business day.<br>3. Select a preferred time window.<br>4. Enter an invalid phone number format.<br>5. Click on the 'Request Callback' button. | Inline guidance shows an error message indicating that the phone number format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-089 |  | Send a secure message with maximum subject length | User is logged in, User is on the Support Center page | 1. Enter a subject with the maximum allowed length.<br>2. Select a category from the dropdown.<br>3. Enter a message in the Message Body.<br>4. Click on the 'Send Message' button. | Message sent successfully. Ticket ID is displayed. | medium |
| TC-092 |  | Request a callback for the earliest possible date | User is logged in, User is on the Support Center page | 1. Select a reason for the call from the dropdown.<br>2. Select today's date if it is a business day or the next business day if today is not.<br>3. Select a preferred time window.<br>4. Click on the 'Request Callback' button. | Callback request submitted. An email confirmation is sent. | medium |

---
