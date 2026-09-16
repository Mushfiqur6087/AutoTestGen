# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Registration page elements displayed | None | 1. Navigate to the signup page | Required fields, mobile number country code selector, terms checkbox, and "Sign Up" button are visible | High |
| REG-002 | Successful registration | Email address is not already registered | 1. Enter valid required data<br>2. Accept terms and conditions<br>3. Click "Sign Up" | Account is created and success message or post-registration redirect is shown | High |
| REG-003 | Registration blocked while already authenticated | User is already authenticated and has access to the Dashboard | 1. While authenticated, navigate to the Registration page or click the Register link in navigation | Registration is blocked for authenticated users: the Registration form or Register button is not presented; no ability to submit a new registration is available while authenticated | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-004 | First name empty | None | 1. Leave first name empty<br>2. Fill other required fields<br>3. Submit form | Validation error is displayed for first name | High |
| REG-005 | Invalid email format | None | 1. Enter invalid email format<br>2. Fill other required fields<br>3. Submit form | Validation error indicates email format is invalid | High |
| REG-006 | Password mismatch | None | 1. Enter password<br>2. Enter different confirm password<br>3. Submit form | Validation error indicates passwords do not match | High |
| REG-007 | Duplicate email | Existing user with same email already exists | 1. Enter already-registered email<br>2. Fill other valid data<br>3. Submit form | Registration is blocked and duplicate-email error is displayed | High |
| REG-008 | Terms and conditions unchecked | None | 1. Fill valid registration data<br>2. Leave terms unchecked<br>3. Submit form | Registration is blocked and user is prompted to accept terms | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-009 | Very long First Name accepted (200+ characters) | Visitor is not authenticated and is on the Registration form | 1. Enter a string of 200+ characters in the First Name field<br>2. Fill other required fields with valid values<br>3. Submit form | Form submission succeeds; no inline field errors are displayed for First Name (registration proceeds) | Low |
| REG-010 | Mobile number with selected country code | None | 1. Select country code<br>2. Enter valid number at expected length boundary | Number is accepted in the expected format | Low |
