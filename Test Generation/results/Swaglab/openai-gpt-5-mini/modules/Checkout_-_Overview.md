# Test Cases — Swaglab

Generated: 2026-07-04T16:57:18.453082Z  
Model: openai/gpt-5-mini  

## Checkout - Overview

Total: **8** (positive: 2, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout and navigate to Confirmation | User logged in, Cart contains one or more items, Checkout contact/payment/shipping information has been entered on the Checkout - Information step | 1. Open the Checkout - Overview page<br>2. Verify the Order summary is visible and displays Item total, Tax, and Total; verify Payment information and Shipping information sections are visible<br>3. Click the Finish button | The Checkout - Confirmation page is displayed with a confirmation heading; the page shows an order summary listing Item total, Tax, and Total that match the Overview and a visible order confirmation section | high |
| TC-002 | WF-002 | Cancel checkout and return to Shopping Cart | User logged in, Cart contains one or more items, Checkout contact/payment/shipping information has been entered on the Checkout - Information step | 1. Open the Checkout - Overview page<br>2. Click the Cancel button | The Shopping Cart page is displayed showing the cart items list; the Checkout - Overview page is no longer visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Access Overview while not authenticated | User is not logged in, Cart may contain items or be empty | 1. In a browser session where the user is logged out, navigate to the Checkout - Overview page URL (or click Checkout from the Cart)<br>2. Observe the resulting page | User is not shown the Checkout - Overview; the UI redirects to or displays the login screen (or an authentication prompt). The checkout is not accessible and no Finish/Cancel actions are performed. | high |
| TC-004 | WF-001 | Click Finish when cart is empty | User is logged in, Cart contains no items, Checkout contact/payment/shipping information may or may not be present | 1. Navigate to the Checkout - Overview page while signed in and with an empty cart<br>2. Click the Finish button | Finish does not complete; the page does not navigate to Checkout - Confirmation. An inline validation/error indicator is shown in or near the order summary indicating the cart is empty or that items are required. The order is not created and the user remains on Checkout - Overview. | high |
| TC-005 | WF-001 | Click Finish with missing payment or shipping information | User is logged in, Cart contains one or more items, Checkout contact/payment/shipping information has NOT been provided on the previous information step | 1. Navigate to the Checkout - Overview page while signed in and with items in the cart but without entering payment/shipping/contact information<br>2. Click the Finish button | Finish does not complete; the page does not navigate to Checkout - Confirmation. Inline validation errors appear on the missing information area(s) (for example, Payment information and/or Shipping information) indicating those details are required. The order is not created and the user remains on Checkout - Overview. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click of Finish (duplicate submit) | User is logged in, cart contains one or more items, and checkout contact/payment/shipping information has been entered on the Checkout - Information step., User is on the Checkout - Overview page showing order summary and Finish button. | 1. Click the Finish button once.<br>2. Immediately click the Finish button a second time (while the first submission is still processing).<br>3. Observe the UI after the clicks. | Second submission attempt is blocked: after the first click the Finish button becomes disabled or shows an in-progress indicator and the second click does not navigate again; the user is taken to the Checkout - Confirmation page once and no duplicate confirmation UI is shown. | medium |
| TC-007 (interaction_edge) | WF-001 | Browser Back after successful Finish (prevent duplicate order) | User is logged in, cart contains one or more items, and checkout contact/payment/shipping information has been entered on the Checkout - Information step., User is on the Checkout - Overview page. | 1. Click the Finish button and wait until the Checkout - Confirmation page is shown.<br>2. Use the browser Back button once to return to the Checkout - Overview page.<br>3. Observe the Overview page and the state of the cart and Finish/Cancel controls. | Visible outcome: returning to Checkout - Overview shows the cart as emptied or the page in a non-submittable state (Finish disabled) indicating the order was completed; the page does not produce a second confirmation or allow an immediate duplicate submission. | medium |
| TC-008 (input_edge) |  | Very long / special-character shipping address entered on prior step is displayed in Overview | User is logged in and cart contains one or more items., User is on the Checkout - Information step. | 1. Enter a shipping address value of 200+ characters containing a mix of special characters and emoji into the Shipping Address field on the Checkout - Information step.<br>2. Click Continue to navigate to Checkout - Overview.<br>3. Observe how the Checkout - Overview displays the shipping address in the summary view (layout, truncation indicator, or visible full value). | Visible outcome: the Overview either shows the full long shipping address without layout-breaking overflow or shows a visibly truncated address with a truncation/overflow indicator (e.g., ellipsis or 'show more') — the page remains usable and no rendering errors are shown. | low |

---
