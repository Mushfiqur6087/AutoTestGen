# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Logout

### Functional Tests

| TC ID         | Test Case                                                           | Preconditions                        | Steps                                                  | Expected Result                                        | Priority |
| ------------- | ------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | -------- |
| MF-LOGOUT-001 | Logout from user menu                                               | User logged in                       | 1. Open user/profile menu<br>2. Click Logout           | User session is terminated and login page is displayed | High     |
| MF-LOGOUT-002 | Protected routes inaccessible after logout                          | User logged out after active session | 1. Logout<br>2. Attempt to navigate to protected route | User is redirected to login page or access is denied   | High     |
| MF-LOGOUT-003 | Browser refresh after logout does not restore authenticated session | User has logged out                  | 1. Logout<br>2. Refresh page                           | User remains logged out                                | High     |

### Negative Tests

| TC ID         | Test Case                                                           | Preconditions                                   | Steps                                           | Expected Result                                                           | Priority |
| ------------- | ------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------- | -------- |
| MF-LOGOUT-004 | Browser back after logout does not reopen active authenticated page | User logged out                                 | 1. Logout<br>2. Press browser back              | Previously visited protected page is not usable without re-authentication | High     |
| MF-LOGOUT-005 | Expired session behaves consistently with explicit logout           | Session timeout configured or token invalidated | 1. Allow session to expire<br>2. Perform action | User is redirected to login or prompted to re-authenticate                | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                   | Preconditions                              | Steps                                   | Expected Result                                                         | Priority |
| ------------- | ------------------------------------------- | ------------------------------------------ | --------------------------------------- | ----------------------------------------------------------------------- | -------- |
| MF-LOGOUT-006 | Logout clears user-specific UI state        | User logged in and navigation state exists | 1. Logout<br>2. Login as different user | New user does not inherit previous user's UI state in unauthorized ways | Medium   |
| MF-LOGOUT-007 | Logout from any module behaves consistently | User logged in on non-home route           | 1. Logout from multiple pages/modules   | Logout always invalidates session and returns to login page             | Medium   |
