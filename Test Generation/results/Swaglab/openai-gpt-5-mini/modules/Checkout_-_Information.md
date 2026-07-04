# Test Cases — Swaglab

Generated: 2026-07-04T15:05:38.152771Z  
Model: openai/gpt-5-mini  

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete required fields and continue to Overview | User logged in as <Customer>, Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Postal Code field<br>4. Click the Continue button | The Checkout - Overview page is displayed (navigates to Checkout - Overview) | high |
| TC-002 | WF-002 | Click Cancel returns user to Shopping Cart | User logged in as <Customer>, Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Click the Cancel button | The Shopping Cart page is displayed (returns to Shopping Cart) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Submit with a required text field (First Name) left blank | User is logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Navigate to the Checkout - Information page from the Shopping Cart<br>2. Leave the First Name field blank<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid postal code> in the Postal Code field<br>5. Click the Continue button | Form does not submit; user remains on Checkout - Information; an error banner and/or inline message is displayed indicating the First Name is required: "Error: First Name is required" and the First Name field is highlighted. No navigation to Checkout - Overview occurs. | high |
| TC-004 | WF-001 | Submit with ALL required fields empty | User is logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Navigate to the Checkout - Information page from the Shopping Cart<br>2. Leave the First Name field blank<br>3. Leave the Last Name field blank<br>4. Leave the Postal Code field blank<br>5. Click the Continue button | Form does not submit; user remains on Checkout - Information; an error banner and/or inline messages are displayed for each missing field with the exact messages: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required". No navigation to Checkout - Overview occurs. | high |
| TC-005 |  | Unauthenticated user attempts to access Checkout - Information | User is not authenticated | 1. As an unauthenticated user, navigate directly to the Checkout - Information URL | Access is blocked; user is redirected to the authentication/login page (Checkout - Information is not displayed). A login prompt is shown and no Checkout - Overview navigation occurs. | high |
| TC-006 | WF-001 | Attempt Continue when precondition fails (shopping cart is empty / checkout not initiated) | User is logged in but has an empty shopping cart (checkout not properly initiated) | 1. Log in as a user with an empty shopping cart<br>2. Navigate to the Checkout - Information page (e.g., via direct URL)<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid postal code> in the Postal Code field<br>6. Click the Continue button | Continue action is blocked; user remains on Checkout - Information; an error banner or inline message is displayed stating the checkout cannot proceed because the shopping cart is empty or checkout was not initiated (no navigation to Checkout - Overview occurs). The form is not submitted. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-001 | Leading/trailing whitespace in name is trimmed and allows continue | Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Enter leading and trailing spaces around the first name (e.g. "  <valid First Name>  ") into the First Name field<br>2. Enter a valid value into the Last Name field<br>3. Enter a valid value into the Postal Code field<br>4. Click Continue | Continue succeeds; navigates to Checkout - Overview. The First Name is saved/displayed without the leading or trailing whitespace (trimmed) on the subsequent page or form summary. | medium |
| TC-008 (input_edge) | WF-001 | Whitespace-only input in a required name field is treated as empty and blocked | Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Enter only whitespace characters (e.g. "   ") into the First Name field<br>2. Enter a valid value into the Last Name field<br>3. Enter a valid value into the Postal Code field<br>4. Click Continue | Submission is blocked; an error banner or inline message is shown with the exact text "Error: First Name is required" and the user remains on the Checkout - Information form. | medium |
| TC-009 (input_edge) | WF-001 | Very long text (200+ chars) in name fields | Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Enter a very long string (200+ characters) into the First Name field<br>2. Enter a very long string (200+ characters) into the Last Name field<br>3. Enter a valid value into the Postal Code field<br>4. Click Continue | Continue either succeeds or shows a clear inline/truncation indicator; if it succeeds, the app navigates to Checkout - Overview and the Overview displays the full entered First Name and Last Name (no silent data loss). If the UI truncates, a visible truncation indicator or message is shown before navigation. | low |
| TC-010 (interaction_edge) | WF-001 | Browser back after successful Continue does not re-submit and the form is blank | Logged in with at least one item in the shopping cart and checkout initiated from the Shopping Cart. | 1. Enter a valid value into the First Name field<br>2. Enter a valid value into the Last Name field<br>3. Enter a valid value into the Postal Code field<br>4. Click Continue<br>5. On the Checkout - Overview page, press the browser Back button | After using the browser Back button the Checkout - Information form is shown blank (not pre-filled) and no duplicate navigation or implicit re-submission occurs. The user must explicitly re-enter data and click Continue to navigate again. | low |

---
