# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-LOGIN-001 | Valid login with email | Registered user exists | 1. Navigate to login page<br>2. Enter valid email (admin@parabank.com)<br>3. Enter valid password (Admin123!@#)<br>4. Click "Sign In" | Flash message "Signed in successfully." displayed, redirected to Accounts Overview | High |
| MW-LOGIN-002 | Valid login with username | Registered user exists | 1. Enter username instead of email<br>2. Enter valid password<br>3. Click "Sign In" | User logged in successfully | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-LOGIN-004 | Invalid email format | None | 1. Enter invalid email format (no @)<br>2. Try to submit | Validation error: invalid email format | High |
| MW-LOGIN-005 | Incorrect password | Registered user exists | 1. Enter valid email<br>2. Enter incorrect password<br>3. Click "Sign In" | Error: "Incorrect email or password. Please try again.", password field cleared | High |
| MW-LOGIN-006 | Unregistered email | None | 1. Enter non-existent email<br>2. Enter any password<br>3. Click "Sign In" | Error message displayed | High |
| MW-LOGIN-007 | Empty email | None | 1. Leave email empty<br>2. Enter password<br>3. Click "Sign In" | Validation error for email field | High |
| MW-LOGIN-008 | Empty password | None | 1. Enter email<br>2. Leave password empty<br>3. Click "Sign In" | Validation error for password field | High |
| MW-LOGIN-009 | Password less than 8 chars | None | 1. Enter valid email<br>2. Enter password < 8 characters<br>3. Click "Sign In" | Validation error: password must be at least 8 characters | High |
| MW-LOGIN-010 | Forgot Password link | None | 1. Click "Forgot Password?" link on login form | Password Reset page opens with Email/Username field and submit control | Medium |
| MW-LOGIN-011 | Already-authenticated user redirected from Sign In | User already logged in | 1. Navigate to the Sign In page while authenticated | Sign In form not displayed; user remains on/redirected to Accounts Overview | Medium |
| MW-LOGIN-012 | Email whitespace trimmed | Registered user exists | 1. Enter registered email with leading/trailing whitespace<br>2. Enter valid password<br>3. Click "Sign In" | Whitespace trimmed, sign-in succeeds | Low |
| MW-LOGIN-013 | Password without special char | None | 1. Enter password without special character | Validation error: password must contain special character | Medium |
| MW-LOGIN-014 | Login with extremely long email | None | 1. Enter email > 255 chars | Validation error or prevented | Low |
| MW-LOGIN-015 | SQL injection in email | None | 1. Enter "' OR 1=1 --" in email | Error message, no login | High |
