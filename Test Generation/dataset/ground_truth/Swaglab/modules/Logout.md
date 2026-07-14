# Swaglab — Ground Truth

Source: dataset/ground_truth/Swaglab/Swaglab.md

## Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGOUT-001 | Successful logout | User logged in | 1. Open hamburger menu<br>2. Click "Logout" | User redirected to login page | High |
| SL-LOGOUT-002 | Session cleared | Logged out | 1. Try to access inventory directly | Redirected to login | High |
| SL-LOGOUT-003 | Cart cleared on logout | Items in cart, logged out | 1. Log back in<br>2. Check cart | Cart is empty (session reset) | High |
| SL-LOGOUT-004 | Back button after logout | Logged out | 1. Click browser back button | Cannot access protected pages | High |
