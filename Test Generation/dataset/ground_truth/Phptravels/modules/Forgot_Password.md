# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Forgot Password

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-001 | Request password reset with existing email | Registered user exists | 1. Open Forgot Password page<br>2. Enter registered email<br>3. Click submit | Confirmation message indicates reset email was sent | High |
| FP-002 | Reset password with valid link | Valid reset link is available | 1. Open reset password page from email link<br>2. Enter valid new password<br>3. Confirm password<br>4. Submit | Password is changed and user is returned to login with success feedback | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-003 | Unknown email address | None | 1. Enter non-existent email on Forgot Password page<br>2. Submit | Error message indicates no account exists for that email | High |
| FP-004 | Empty email field | None | 1. Leave email field empty<br>2. Submit | Validation error is displayed | High |
| FP-005 | Reset password mismatch | Valid reset link is available | 1. Enter new password<br>2. Enter different confirm password<br>3. Submit | Password reset is blocked and mismatch error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-006 | Expired reset link | Expired reset link is available | 1. Open expired reset link | Link is rejected and user is prompted to request a new reset email | Medium |
