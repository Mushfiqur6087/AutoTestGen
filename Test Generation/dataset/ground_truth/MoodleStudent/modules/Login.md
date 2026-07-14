# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-001 | Valid student login | `student1` account exists and is active | 1. Navigate to the Moodle login page<br>2. Enter `student1` username<br>3. Enter the student password<br>4. Click "Log in" | Student is redirected to Dashboard and the user menu shows the student initials/name | High |
| MS-LOGIN-002 | Guest access from login page | Guest access is enabled | 1. Open login page<br>2. Click "Access as a guest" | Guest browsing opens without authenticating as student | Medium |
| MS-LOGIN-003 | Login page elements displayed | None | 1. Open login page | Username, Password, Log in, Lost password, Access as guest, and Cookies notice controls are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-004 | Invalid student credentials | Login page is visible | 1. Enter `student1` username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login error is shown, password is cleared, username remains populated, and Dashboard is not opened | High |
| MS-LOGIN-005 | Empty username | Login page is visible | 1. Leave Username empty<br>2. Enter the student password<br>3. Click "Log in" | Login is rejected, username field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-006 | Empty password | Login page is visible | 1. Enter `student1` username<br>2. Leave Password empty<br>3. Click "Log in" | Login is rejected, password field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-007 | Disabled lost-password link | Lost-password feature is disabled | 1. Click "Lost password?" | Recovery flow does not open | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-008 | Failed login retains username | Login page is visible | 1. Enter invalid credentials<br>2. Submit login | Username remains populated and password is cleared | Medium |
| MS-LOGIN-009 | Long username failure handling | Login page is visible | 1. Enter 200+ character username and invalid password<br>2. Submit | Login error is shown, password is cleared, the long username remains in the username field, and Log in remains clickable | Low |
| MS-LOGIN-010 | Both fields empty — all validation errors shown simultaneously | Login page is visible | 1. Leave Username and Password both empty<br>2. Click "Log in" | Both username and password fields are flagged with validation errors simultaneously; no authenticated page opens | High |
| MS-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Login page is visible | 1. Enter `  student1  ` (with leading and trailing spaces) as the username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login is rejected with error; username field retains the entered string including the surrounding whitespace | Low |
| MS-LOGIN-012 | Rapid double submission of Log in results in single failure response | Login page is visible; invalid credentials ready | 1. Enter invalid credentials<br>2. Double-click "Log in" rapidly | Exactly one login-error response is displayed; the form is not submitted twice and no duplicate error message is stacked | Medium |
