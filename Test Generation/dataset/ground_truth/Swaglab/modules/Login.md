# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-001 | Valid login with standard_user | None | 1. Navigate to login page<br>2. Enter "standard_user" as username<br>3. Enter "secret_sauce" as password<br>4. Click "Login" | User redirected to product inventory page | High |
| SL-LOGIN-002 | Login page elements displayed | None | 1. Navigate to login page | Username field, Password field, Login button, and accepted usernames/password info visible | Medium |
| SL-LOGIN-003 | Login with each valid user type | None | 1. Login with standard_user<br>2. Logout<br>3. Repeat for each user type | All valid users can log in (except locked_out_user) | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-004 | Invalid username | None | 1. Enter invalid username<br>2. Enter valid password<br>3. Click "Login" | Error message: "Epic sadface: Username and password do not match" | High |
| SL-LOGIN-005 | Invalid password | None | 1. Enter valid username<br>2. Enter incorrect password<br>3. Click "Login" | Error message displayed, user remains on login page | High |
| SL-LOGIN-006 | Empty username | None | 1. Leave username empty<br>2. Enter password<br>3. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-007 | Empty password | None | 1. Enter username<br>2. Leave password empty<br>3. Click "Login" | Error message: "Epic sadface: Password is required" | High |
| SL-LOGIN-008 | Both fields empty | None | 1. Leave both fields empty<br>2. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-009 | Locked out user | None | 1. Enter "locked_out_user"<br>2. Enter "secret_sauce"<br>3. Click "Login" | Error message: "Epic sadface: Sorry, this user has been locked out" | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-010 | Username with leading/trailing spaces | None | 1. Enter " standard_user " (with spaces)<br>2. Enter valid password<br>3. Click "Login" | Login fails or spaces trimmed and login succeeds | Medium |
| SL-LOGIN-011 | Case sensitivity | None | 1. Enter "Standard_User" (different case)<br>2. Enter valid password<br>3. Click "Login" | Login fails (username is case-sensitive) | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-012 | Password field masking | None | 1. Enter text in password field | Password characters are masked | High |
| SL-LOGIN-013 | Error message dismissible | SL-LOGIN-004 completed | 1. Click X button on error message | Error message disappears | Medium |
| SL-LOGIN-014 | Tab navigation | None | 1. Use Tab key to navigate | Focus moves: username → password → Login button | Medium |
| SL-LOGIN-015 | Enter key submission | None | 1. Fill credentials<br>2. Press Enter | Form submits | Medium |
