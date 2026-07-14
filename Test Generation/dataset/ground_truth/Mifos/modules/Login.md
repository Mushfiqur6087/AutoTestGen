# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Login

### Functional Tests

| TC ID        | Test Case                            | Preconditions          | Steps                                                                                                                                            | Expected Result                                                                                                 | Priority |
| ------------ | ------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------- |
| MF-LOGIN-001 | Valid login with correct credentials | Mifos instance running | 1. Navigate to login page<br>2. Enter "default" as Tenant<br>3. Enter "mifos" as Username<br>4. Enter "password" as Password<br>5. Click "Login" | User is redirected to Home page, toolbar shows username                                                         | High     |
| MF-LOGIN-002 | Login page elements displayed        | None                   | 1. Navigate to login page                                                                                                                        | Tenant Identifier field, Username field, Password field, and Login button are visible with application branding | Medium   |

### Negative Tests

| TC ID        | Test Case         | Preconditions | Steps                                                                                                    | Expected Result                                       | Priority |
| ------------ | ----------------- | ------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-LOGIN-005 | Invalid username  | None          | 1. Enter valid tenant<br>2. Enter invalid username<br>3. Enter any password<br>4. Click "Login"          | Error message for invalid authentication is displayed | High     |
| MF-LOGIN-006 | Invalid password  | None          | 1. Enter valid tenant<br>2. Enter "mifos" as username<br>3. Enter incorrect password<br>4. Click "Login" | Error message displayed, user remains on login page   | High     |
| MF-LOGIN-007 | Empty username    | None          | 1. Enter valid tenant<br>2. Leave username empty<br>3. Enter password<br>4. Click "Login"                | Inline validation error shown for username            | High     |
| MF-LOGIN-008 | Empty password    | None          | 1. Enter valid tenant<br>2. Enter username<br>3. Leave password empty<br>4. Click "Login"                | Inline validation error shown for password            | High     |
| MF-LOGIN-009 | Both fields empty | None          | 1. Leave Username and Password empty<br>2. Click "Login"                                                 | Validation errors shown for all mandatory fields      | Medium   |

### Boundary Tests

| TC ID        | Test Case                                               | Preconditions          | Steps                                                                             | Expected Result                                                | Priority |
| ------------ | ------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- |
| MF-LOGIN-015 | Login using Enter key                                   | None                   | 1. Enter valid Tenant, Username, and Password<br>2. Press Enter in Password field | Login is submitted and user is redirected on success           | Medium   |
| MF-LOGIN-017 | Direct access to login page after authenticated session | User already logged in | 1. Login successfully<br>2. Navigate again to login URL                           | User is redirected to Home page or active session is preserved | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                          | Preconditions          | Steps                                                                                      | Expected Result                                                            | Priority |
| ------------ | ------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------- |
| MF-LOGIN-020 | Session persists on page refresh after successful login            | User logged in         | 1. Login successfully<br>2. Refresh browser tab                                            | User remains authenticated and current page reloads successfully           | High     |
| MF-LOGIN-021 | Direct navigation to login page while authenticated                | User already logged in | 1. Enter login page URL manually                                                           | User is redirected to Home page or duplicate login form usage is prevented | Medium   |
| MF-LOGIN-022 | Logout invalidates session token for subsequent protected requests | User logged in         | 1. Login successfully<br>2. Logout<br>3. Navigate to protected route or call protected API | Request is rejected and user is returned to login page                     | High     |
