# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-001 | Valid teacher login | `teacher1` account exists and is active | 1. Navigate to the Moodle login page<br>2. Enter `teacher1` username<br>3. Enter the teacher password<br>4. Click "Log in" | Teacher is redirected to Dashboard and the user menu shows the teacher initials/name | High |
| MT-LOGIN-002 | Guest access from login page | Guest access is enabled | 1. Open login page<br>2. Click "Access as a guest" | Guest browsing opens without authenticating as teacher | Medium |
| MT-LOGIN-003 | Cookie notice opens | Login page is visible | 1. Click "Cookies notice" | Cookie usage information is displayed without clearing login fields | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-004 | Invalid teacher credentials | Login page is visible | 1. Enter `teacher1` username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login error is shown, password is cleared, username remains populated, and Dashboard is not opened | High |
| MT-LOGIN-005 | Empty username | Login page is visible | 1. Leave Username empty<br>2. Enter the teacher password<br>3. Click "Log in" | Login is rejected, username field is identified as missing, and no authenticated page is opened | High |
| MT-LOGIN-006 | Empty password | Login page is visible | 1. Enter `teacher1` username<br>2. Leave Password empty<br>3. Click "Log in" | Login is rejected, password field is identified as missing, and no authenticated page is opened | High |
| MT-LOGIN-007 | Disabled lost-password link | Lost-password feature is disabled | 1. Click "Lost password?" | Recovery flow does not open and user remains on the login page | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-008 | Failed login retains username | Login page is visible | 1. Enter invalid username and password<br>2. Submit login | Username remains populated and password is cleared | Medium |
| MT-LOGIN-009 | Log in action blocked while already authenticated | Teacher is already authenticated and on Dashboard | 1. While authenticated, navigate to the Login page<br>2. Attempt to interact with the "Log in" button or submit the login form | The Log in action is not allowed while already authenticated: the button is not visible or is disabled/non-interactive; submitting does not create a new session or switch to a guest session; teacher remains authenticated | Medium |
| MT-LOGIN-010 | Both fields empty shows simultaneous validation | Login page is visible | 1. Leave Username and Password both empty<br>2. Click "Log in" | Both username and password fields are flagged with validation errors simultaneously; no authenticated page opens | High |
| MT-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Login page is visible | 1. Enter `  teacher1  ` (with spaces) as the username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login is rejected with error; username field retains the entered string including the surrounding whitespace | Low |
| MT-LOGIN-012 | Very long username rejected without crash | Login page is visible | 1. Enter a 200+ character username and an invalid password<br>2. Click "Log in" | Login error is shown, the long username remains populated without breaking the page layout, and password is cleared | Low |
