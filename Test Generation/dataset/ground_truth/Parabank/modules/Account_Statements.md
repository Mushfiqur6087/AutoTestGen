# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Account Statements

### Generate Statement Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-AS-001 | Generate monthly statement | User logged in | 1. Select month-and-year period<br>2. Select account<br>3. Click "Generate Statement" | "Statement generated successfully." | High |
| MW-AS-002 | Generate custom date range | User logged in | 1. Select custom date range<br>2. Enter start and end dates<br>3. Select account<br>4. Submit | Statement generated | High |
| MW-AS-003 | Invalid date range | User logged in | 1. Enter end date before start date<br>2. Submit | Validation error | High |
| MW-AS-004 | Month and Year left blank when selected | User logged in | 1. Select "Month and Year" period<br>2. Leave Month and Year blank<br>3. Select account<br>4. Submit | Validation error, form does not submit | High |
| MW-AS-005 | Unauthenticated access blocked | User not logged in | 1. Navigate directly to Account Statements page URL | Redirected to login page, Statements content not accessible | Medium |

### E-Statement Preference Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-AS-006 | Opt-in to paperless | User logged in | 1. Check paperless checkbox<br>2. Enter email<br>3. Click "Save Preference" | "e-Statement preference updated." | High |
| MW-AS-007 | Opt-out of paperless | Previously opted-in | 1. Uncheck paperless checkbox<br>2. Submit | Preference updated | High |
| MW-AS-008 | Invalid email | User logged in | 1. Enter invalid email<br>2. Submit | Validation error, email field highlighted | High |
| MW-AS-009 | Empty email with opt-in | User logged in | 1. Check paperless<br>2. Leave email empty<br>3. Submit | Validation error | High |
| MW-AS-010 | Custom date range spanning years | User logged in | 1. Enter > 5 years range | Statement generated or date range limit error | Medium |
| MW-AS-011 | Opt-out clears email field | Previously opted-in | 1. Uncheck paperless | Email field disabled or cleared | Low |
| MW-AS-012 | Invalid characters in email | User logged in | 1. Enter email with spaces/invalid chars | Validation error | High |
