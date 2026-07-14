# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login | Registered user exists | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click "Login" | User is redirected to the dashboard or prior protected page | High |
| LOGIN-002 | Remember Me login | Registered user exists | 1. Enter valid credentials<br>2. Check "Remember Me"<br>3. Click "Login" | Session remains active according to remember-me behavior | Medium |
| LOGIN-003 | Login page alternate options displayed | None | 1. Navigate to login page | Forgot password link, signup link, and any enabled social login buttons are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-004 | Invalid email or password | None | 1. Enter invalid email or password<br>2. Click "Login" | Error message is displayed and login does not succeed | High |
| LOGIN-005 | Empty email | None | 1. Leave email empty<br>2. Enter password<br>3. Click "Login" | Validation or login error is displayed | High |
| LOGIN-006 | Empty password | None | 1. Enter email<br>2. Leave password empty<br>3. Click "Login" | Validation or login error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Email retained after failed login | None | 1. Enter email<br>2. Enter invalid password<br>3. Click "Login" | Email remains populated while password is cleared | Medium |
| LOGIN-008 | Multiple failed login attempts | None | 1. Submit invalid credentials repeatedly | Site consistently handles repeated failures and may activate additional protection such as CAPTCHA | Low |
