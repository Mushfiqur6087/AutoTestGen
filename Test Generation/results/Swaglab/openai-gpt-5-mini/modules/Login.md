# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Login

Total: **13** (positive: 5, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials redirects to Product Inventory | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | The Product Inventory page is displayed; the inventory page heading and the products list/grid are visible. | high |
| TC-002 | WF-002 | Attempt login with empty Username shows required-username error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field empty<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Username is required." | medium |
| TC-003 | WF-003 | Attempt login with empty Password shows required-password error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter standard_user in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Password is required." | medium |
| TC-004 | WF-004 | Attempt login with invalid credentials shows mismatch error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Username and password do not match any user in this service." | medium |
| TC-005 | WF-005 | Attempt login with locked_out_user shows locked-out error | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | An error banner is displayed with the text "Epic sadface: Sorry, this user has been locked out." | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Submit with Username blank (required text field) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field blank<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Username is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-007 | WF-003 | Submit with Password blank (required password field) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <valid username> in the Username field<br>2. Leave the Password field blank<br>3. Click the Login button | An error banner displays 'Epic sadface: Password is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-008 |  | Submit with all required fields empty | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click the Login button | Error banners display 'Epic sadface: Username is required.' and 'Epic sadface: Password is required.'; the form does not submit; user remains on the sign-in page. | high |
| TC-009 | WF-004 | Submit with filled but invalid credentials (authentication failure) | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Username and password do not match any user in this service.'; login is blocked; user remains on the sign-in page. | high |
| TC-010 | WF-005 | Attempt login with a locked-out account | User is unauthenticated and has reached the sign-in page with credentials available to submit. | 1. Enter <locked_out_user> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click the Login button | An error banner displays 'Epic sadface: Sorry, this user has been locked out.'; login is blocked; user remains on the sign-in page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Very long Username (200+ chars) treated as invalid credentials | User is unauthenticated and is on the sign-in page | 1. Enter a username consisting of 200+ characters into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button | Login is blocked; the page displays the error banner: Epic sadface: Username and password do not match any user in this service. | medium |
| TC-012 (input_edge) |  | Username with leading and trailing whitespace is trimmed and accepted | User is unauthenticated and is on the sign-in page, A known valid username is visible on the sign-in page (listed as an accepted test username) | 1. Enter the valid username shown on the sign-in page with one or more leading and trailing spaces into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button | Login succeeds; the user is redirected to the Product Inventory page and the Product Inventory page is displayed. | medium |
| TC-013 (interaction_edge) |  | Browser Back after successful login shows blank sign-in form (no pre-filled credentials) | User is unauthenticated and is on the sign-in page, A known valid username and the shared password are available | 1. Enter a known valid username into the Username field<br>2. Enter the shared password listed on the sign-in page into the Password field<br>3. Click the Login button<br>4. After redirect to the Product Inventory page, click the browser Back button | Sign-in page is shown and both Username and Password fields are empty (no credentials pre-filled). | low |

---
