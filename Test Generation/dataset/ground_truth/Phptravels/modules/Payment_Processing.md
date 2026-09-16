# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Payment Processing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-001 | Payment summary displayed | User is on payment page | 1. Review payment page | Booking summary, price breakdown, payment methods, and terms checkbox are visible | High |
| PAY-002 | Apply valid promo code | Valid promo code exists | 1. Enter valid promo code<br>2. Click "Apply" | Discount is applied and total updates | Medium |
| PAY-003 | Successful card payment | User is on payment page and uses valid card | 1. Select card payment<br>2. Enter valid cardholder, card number, expiry, and CVV<br>3. Accept terms<br>4. Click "Pay Now" | Payment succeeds and booking confirmation page is displayed | High |
| PAY-004 | Successful wallet payment | User has enough wallet balance | 1. Select wallet or credits payment<br>2. Confirm payment | Payment succeeds and booking confirmation page is displayed | Medium |
| PAY-005 | Confirmation page displayed after successful payment | Payment was successful | 1. Review confirmation page | Booking reference and follow-up actions such as invoice or voucher download are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-006 | Invalid card number | User is on payment page | 1. Enter invalid card number<br>2. Submit payment | Card validation error is displayed | High |
| PAY-007 | Expired card | User is on payment page | 1. Enter past expiry date<br>2. Submit payment | Expiry validation error is displayed | High |
| PAY-008 | Invalid CVV | User is on payment page | 1. Enter invalid CVV length or format<br>2. Submit payment | CVV validation error is displayed | High |
| PAY-009 | Terms unchecked | User is on payment page | 1. Fill valid payment data<br>2. Leave terms unchecked<br>3. Submit payment | Payment does not proceed and terms validation is displayed | High |
| PAY-010 | Payment declined or insufficient funds | User is on payment page | 1. Submit payment with failing payment source | Error message is displayed with retry or alternate-payment options | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-011 | Retry Payment action is not available when previous attempt did not fail | A completed booking/reservation is present; payment intent is initiated; Payment_Last_Attempt is not Failed | 1. Open the Payment page for a booking where the previous attempt did not fail<br>2. Attempt to locate a Retry Payment button or control | Retry Payment control is not visible on the Payment page; user cannot initiate a retry action from this state | Medium |
| PAY-012 | Download Invoice/Voucher actions are not available before successful booking confirmation | User is on the Payment page or pre-confirmation state (payment not successful) | 1. Open the Payment page for a booking before completing payment<br>2. Attempt to locate the Download Invoice and Download Voucher actions | Download Invoice and Download Voucher actions are not visible prior to a successful booking confirmation; no download is initiated | Low |
