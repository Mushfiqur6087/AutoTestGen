# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Logout from user dropdown | User is logged in | 1. Open user menu<br>2. Click "Logout" | Session ends and the home page shows Login and Signup links again | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-002 | Access protected page after logout | User has logged out | 1. Attempt to open dashboard or booking-management URL | User is redirected to login page and cannot access protected content | High |
