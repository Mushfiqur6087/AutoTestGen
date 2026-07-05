# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Checkout - Information

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete required fields and continue to Overview | User logged in as <Buyer>, Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Ensure the Checkout - Information page is open (first step of the checkout flow).<br>2. Enter <first name> in the First Name field<br>3. Enter <last name> in the Last Name field<br>4. Enter <postal code> in the Postal Code field<br>5. Click the Continue button | The Checkout - Overview page is displayed with the page heading 'Checkout - Overview' | high |
| TC-002 | WF-002 | Click Cancel returns to Shopping Cart | User logged in as <Buyer>, Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Ensure the Checkout - Information page is open (first step of the checkout flow).<br>2. Click the Cancel button | The Shopping Cart page is displayed; the cart listing shows the previously added item(s) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave required text field (First Name) blank and submit | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Navigate to Checkout - Information as a logged-in user with at least one item in the Shopping Cart.<br>2. Leave the First Name field blank.<br>3. Enter <valid Last Name> in the Last Name field.<br>4. Enter <valid Postal Code> in the Postal Code field.<br>5. Click the Continue button. | An error banner is shown on the page: "Error: First Name is required"; the form does not navigate to Checkout - Overview and the user remains on the Checkout - Information page. | high |
| TC-004 | WF-001 | Submit with all required fields empty | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Navigate to Checkout - Information as a logged-in user with at least one item in the Shopping Cart.<br>2. Leave the First Name field blank.<br>3. Leave the Last Name field blank.<br>4. Leave the Postal Code field blank.<br>5. Click the Continue button. | Error banners are shown for each missing field: "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required"; the form does not submit and the user remains on the Checkout - Information page. | high |
| TC-005 |  | Access Checkout - Information while unauthenticated | User is not authenticated (no active session). | 1. From a browser with no authenticated session, navigate to the Checkout - Information URL or attempt to start checkout from the Shopping Cart. | Access is blocked: the user is redirected to the Login page (Checkout - Information form is not displayed) and cannot proceed to Checkout - Overview without authenticating. | high |
| TC-006 |  | Attempt to open Checkout - Information with an empty Shopping Cart | Logged in with an active session and the Shopping Cart contains no items. | 1. Log in as a Buyer with an active session.<br>2. Ensure the Shopping Cart has no items.<br>3. From the Shopping Cart, click the control to begin checkout or navigate directly to Checkout - Information. | Access is blocked: the Checkout - Information form is not displayed and the user remains on the Shopping Cart (cannot proceed to Checkout - Overview without at least one item in the cart). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-001 | Very long First and Last Name accepted and carried to Overview | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <very long string 200+ characters> in the First Name field<br>2. Enter <very long string 200+ characters> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the entered First Name and Last Name (the full long text) without truncation errors | medium |
| TC-008 (input_edge) | WF-001 | Names containing special characters and emoji accepted | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <string containing special characters and emoji> in the First Name field<br>2. Enter <string containing special characters and emoji> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the entered First Name and Last Name including the special characters/emoji | medium |
| TC-009 (input_edge) | WF-001 | Leading and trailing whitespace is trimmed before validation | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <string with leading and trailing spaces> in the First Name field<br>2. Enter <string with leading and trailing spaces> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Form submit succeeds; navigates to Checkout - Overview and the Checkout - Overview page visibly displays the First Name and Last Name with leading and trailing whitespace removed (trimmed) | medium |
| TC-010 (boundary) | WF-001 | Whitespace-only First Name is treated as missing and blocks continue | Logged in with an active session and at least one item in the Shopping Cart initiating the checkout flow. | 1. Enter <spaces-only string> in the First Name field<br>2. Enter <valid Last Name> in the Last Name field<br>3. Enter <valid Postal Code> in the Postal Code field<br>4. Click the Continue button | Continue is blocked; the page displays the error banner 'Error: First Name is required' (visible to the user) | medium |

---
