# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Update Contact Info

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-UCI-001 | Pre-populated form | User logged in | 1. Navigate to Update Contact Info | All fields pre-filled with current user data | High |
| MW-UCI-002 | Successful update | User logged in | 1. Modify any field<br>2. Click "Update Profile" | "Profile updated successfully." message, data refreshed | High |
| MW-UCI-003 | Update First Name | User logged in | 1. Change First Name<br>2. Submit | Updated successfully | Medium |
| MW-UCI-004 | Update Last Name | User logged in | 1. Change Last Name<br>2. Submit | Updated successfully | Medium |
| MW-UCI-005 | Update Address | User logged in | 1. Change Street Address<br>2. Submit | Updated successfully | Medium |
| MW-UCI-006 | Update City | User logged in | 1. Change City<br>2. Submit | Updated successfully | Medium |
| MW-UCI-007 | Update State | User logged in | 1. Change State<br>2. Submit | Updated successfully | Medium |
| MW-UCI-008 | Update ZIP Code | User logged in | 1. Change ZIP Code<br>2. Submit | Updated successfully | Medium |
| MW-UCI-009 | Update Phone | User logged in | 1. Change Phone Number<br>2. Submit | Updated successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-UCI-010 | First Name empty | User logged in | 1. Clear First Name<br>2. Submit | Validation error, error banner displayed | High |
| MW-UCI-011 | Last Name empty | User logged in | 1. Clear Last Name<br>2. Submit | Validation error | High |
| MW-UCI-012 | Address empty | User logged in | 1. Clear Street Address<br>2. Submit | Validation error | High |
| MW-UCI-013 | City empty | User logged in | 1. Clear City<br>2. Submit | Validation error | High |
| MW-UCI-014 | State empty | User logged in | 1. Clear State<br>2. Submit | Validation error | High |
| MW-UCI-015 | ZIP Code empty | User logged in | 1. Clear ZIP Code<br>2. Submit | Validation error | High |
| MW-UCI-016 | Phone empty | User logged in | 1. Clear Phone Number<br>2. Submit | Validation error | High |
| MW-UCI-017 | Invalid ZIP format | User logged in | 1. Enter invalid ZIP<br>2. Submit | Validation error | High |
| MW-UCI-018 | Invalid Phone format | User logged in | 1. Enter invalid phone<br>2. Submit | Validation error | High |
| MW-UCI-019 | Special characters in City | User logged in | 1. Enter City with numbers/symbols | Validation error | Medium |
| MW-UCI-020 | Non-US ZIP code format | User logged in | 1. Enter alphanumeric ZIP | Validation error | Low |
