# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Security Settings

### Change Password Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-SS-001 | Successful password change | User logged in | 1. Enter current password<br>2. Enter new password meeting requirements<br>3. Confirm new password<br>4. Click "Change Password" | "Password changed successfully." | High |
| MW-SS-002 | Incorrect current password | User logged in | 1. Enter wrong current password<br>2. Enter new password<br>3. Submit | Validation error: current password incorrect | High |
| MW-SS-003 | New password too short | User logged in | 1. Enter correct current<br>2. Enter new password < 8 chars<br>3. Submit | Validation error: password policy | High |
| MW-SS-004 | Unauthenticated access blocked | User not logged in | 1. Navigate directly to Security Settings page URL | Redirected to login page, Change Password form not accessible | High |
| MW-SS-005 | Rapid double-submit of Change Password | User logged in, valid form filled | 1. Click "Change Password"<br>2. Immediately click "Change Password" again | Only one success confirmation shown, no duplicate | Low |
| MW-SS-006 | New password composed of emoji/Unicode characters | User logged in | 1. Enter new password made entirely of emoji/extended Unicode characters<br>2. Submit | Validation error: does not meet strong-password policy | Low |
| MW-SS-007 | New password missing special char | User logged in | 1. Enter new password without special char<br>2. Submit | Validation error | High |
| MW-SS-008 | Passwords don't match | User logged in | 1. Enter different values for new and confirm<br>2. Submit | Validation error: passwords must match | High |
| MW-SS-009 | New password matches current password | User logged in | 1. Enter new password identical to current | Error: Cannot reuse old password | High |
| MW-SS-010 | Passwords match but differ by trailing space | User logged in | 1. Add trailing space to confirm | Validation error: passwords must match | Medium |
| MW-SS-011 | Extreme length password | User logged in | 1. Enter password > 128 chars | System handles gracefully | Low |
