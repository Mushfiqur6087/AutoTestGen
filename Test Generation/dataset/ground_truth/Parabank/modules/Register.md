# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Register

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-REG-001 | Successful registration | None | 1. Navigate to Register page<br>2. Fill all fields with valid data<br>3. Click "Register" | "Account created successfully — please sign in." message, redirected to login | High |
| MW-REG-003 | State dropdown | None | 1. Click State dropdown | All US states displayed | Medium |
| MW-REG-004 | Phone auto-formatting | None | 1. Enter phone digits: 5551234567 | Auto-formatted to (555) 123-4567 | High |
| MW-REG-005 | SSN auto-formatting | None | 1. Enter SSN digits: 123456789 | Auto-formatted to 123-45-6789 | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-REG-006 | First Name empty | None | 1. Leave First Name empty<br>2. Fill other fields<br>3. Submit | Validation error on First Name | High |
| MW-REG-007 | Last Name empty | None | 1. Leave Last Name empty<br>2. Submit | Validation error on Last Name | High |
| MW-REG-008 | Street Address empty | None | 1. Leave Street Address empty<br>2. Submit | Validation error on Street Address | High |
| MW-REG-009 | City empty | None | 1. Leave City empty<br>2. Submit | Validation error on City | High |
| MW-REG-010 | State not selected | None | 1. Don't select State<br>2. Submit | Validation error on State | High |
| MW-REG-011 | ZIP Code empty | None | 1. Leave ZIP Code empty<br>2. Submit | Validation error on ZIP Code | High |
| MW-REG-012 | Invalid ZIP format | None | 1. Enter ZIP: 1234 (4 digits)<br>2. Submit | Validation error: must be 5 digits or 5+4 format | High |
| MW-REG-013 | Valid 5+4 ZIP | None | 1. Enter ZIP: 12345-6789<br>2. Submit | Accepted | Medium |
| MW-REG-014 | Phone Number empty | None | 1. Leave Phone empty<br>2. Submit | Validation error on Phone | High |
| MW-REG-015 | Invalid Phone format | None | 1. Enter partial phone: 555123<br>2. Submit | Validation error: must be (123) 456-7890 format | High |
| MW-REG-016 | SSN empty | None | 1. Leave SSN empty<br>2. Submit | Validation error on SSN | High |
| MW-REG-017 | Invalid SSN format | None | 1. Enter partial SSN: 12345<br>2. Submit | Validation error: must be 123-45-6789 format | High |
| MW-REG-018 | Username not email format | None | 1. Enter username without @ symbol<br>2. Submit | Validation error: must be valid email format | High |
| MW-REG-019 | Password less than 8 chars | None | 1. Enter password < 8 characters<br>2. Submit | Validation error on password | High |
| MW-REG-020 | Password mismatch | None | 1. Enter different values for Password and Confirm Password<br>2. Submit | Validation error: passwords must match | High |
| MW-REG-021 | Confirm Password empty | None | 1. Leave Confirm Password empty<br>2. Submit | Validation error on Confirm Password | High |
| MW-REG-022 | All fields empty | None | 1. Submit empty form | Field-level errors displayed for all required fields | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-REG-023 | Minimum valid inputs | None | 1. Enter minimum valid data for all fields<br>2. Submit | Registration succeeds | Medium |
| MW-REG-024 | Maximum length inputs | None | 1. Enter very long strings<br>2. Submit | System handles gracefully | Low |
| MW-REG-025 | Email with leading/trailing spaces | None | 1. Enter email with spaces<br>2. Submit | Successfully registers, trims spaces | Medium |
| MW-REG-026 | Registration session timeout | None | 1. Leave page open for 30 mins<br>2. Submit | Error: Session expired | Medium |
