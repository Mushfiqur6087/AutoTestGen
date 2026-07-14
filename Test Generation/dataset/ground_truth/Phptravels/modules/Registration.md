# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Registration page elements displayed | None | 1. Navigate to the signup page | Required fields, mobile number country code selector, terms checkbox, and "Sign Up" button are visible | High |
| REG-002 | Successful registration | Email address is not already registered | 1. Enter valid required data<br>2. Accept terms and conditions<br>3. Click "Sign Up" | Account is created and success message or post-registration redirect is shown | High |
| REG-003 | Country code selector works | None | 1. Open mobile country code selector<br>2. Select another country code | Selected country code is applied to the mobile number field | Medium |

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
| REG-009 | Minimum password length boundary | None | 1. Enter password at the minimum accepted length<br>2. Fill other valid data<br>3. Submit form | Registration succeeds or validates consistently at the minimum boundary | Low |
| REG-010 | Mobile number with selected country code | None | 1. Select country code<br>2. Enter valid number at expected length boundary | Number is accepted in the expected format | Low |
