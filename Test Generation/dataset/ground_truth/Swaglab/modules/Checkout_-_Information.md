# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Checkout - Information

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-001 | Complete checkout info | Items in cart, on checkout page | 1. Enter First Name<br>2. Enter Last Name<br>3. Enter Postal Code<br>4. Click "Continue" | Navigates to checkout overview | High |
| SL-CHK1-002 | Cancel checkout | On checkout info page | 1. Click "Cancel" | Returns to cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-003 | First Name empty | On checkout info | 1. Leave First Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: First Name is required" | High |
| SL-CHK1-004 | Last Name empty | On checkout info | 1. Leave Last Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Last Name is required" | High |
| SL-CHK1-005 | Postal Code empty | On checkout info | 1. Leave Postal Code empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Postal Code is required" | High |
| SL-CHK1-006 | All fields empty | On checkout info | 1. Leave all fields empty<br>2. Click "Continue" | Error message for first required field | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-007 | Single character inputs | On checkout info | 1. Enter single character in each field<br>2. Click "Continue" | Form accepts or rejects appropriately | Low |
| SL-CHK1-008 | Very long inputs | On checkout info | 1. Enter very long strings<br>2. Click "Continue" | System handles gracefully (truncates or accepts) | Low |
| SL-CHK1-009 | Special characters | On checkout info | 1. Enter special characters in fields<br>2. Click "Continue" | System handles appropriately | Low |
| SL-CHK1-010 | Numeric First/Last Name | On checkout info | 1. Enter numbers in name fields<br>2. Click "Continue" | May accept (no strict validation) | Low |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-011 | Form elements displayed | On checkout info | 1. View page | First Name, Last Name, Postal Code fields, Continue and Cancel buttons visible | Medium |
| SL-CHK1-012 | Error message style | Error triggered | 1. Submit with empty field | Error displayed with red styling and X icon | Medium |
