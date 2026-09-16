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
| MF-LOGIN-015 | Rapid double-click of Login with valid credentials does not create duplicate sessions | Valid account exists for the selected tenant | 1. Enter valid Tenant, Username, and Password<br>2. Rapidly click the Login button twice in immediate succession | Login succeeds once; user is redirected to the landing page and no duplicate error messages or duplicate login forms are displayed | Medium   |
| MF-LOGIN-017 | Login button remains disabled until Tenant, Username, and Password are all filled | None                   | 1. Observe the Login button state before filling any fields<br>2. Enter Tenant, Username, and Password one at a time, observing the button state after each | The Login button becomes enabled and clickable only after Tenant, Username, and Password are all filled | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                          | Preconditions          | Steps                                                                                      | Expected Result                                                            | Priority |
| ------------ | ------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------- |
| MF-LOGIN-020 | Session persists on page refresh after successful login            | User logged in         | 1. Login successfully<br>2. Refresh browser tab                                            | User remains authenticated and current page reloads successfully           | High     |
| MF-LOGIN-021 | Forgot Password link navigates to the Forgot Password page | None | 1. On the Login page, click the 'Forgot Password?' link | The Forgot Password page is displayed showing its page title and an input to enter the account email or username | Medium   |
| MF-LOGIN-022 | Extremely long Username and Password inputs (200+ characters) are rejected | Tenant is selected or defaults to the default tenant | 1. Enter a very long string (200+ characters) into the Username field<br>2. Enter a very long string (200+ characters) into the Password field<br>3. Click Login | Login is blocked; an inline validation message or the invalid-credentials error is shown on the login form | High     |
