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
| MF-LOGOUT-005 | Unauthenticated user cannot reach the Log Out control | User is not authenticated | 1. Open the application landing URL as an unauthenticated user<br>2. Observe the top-right corner of the navigation bar | The User Profile icon and Log Out option are not visible/available; the Login page is displayed | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                   | Preconditions                              | Steps                                   | Expected Result                                                         | Priority |
| ------------- | ------------------------------------------- | ------------------------------------------ | --------------------------------------- | ----------------------------------------------------------------------- | -------- |
| MF-LOGOUT-006 | Rapid double-click of Log Out does not create a duplicate or broken session | User is authenticated | 1. Open the profile dropdown and click Log Out<br>2. Immediately click Log Out again before the redirect completes | Log out succeeds once; the Login page is displayed and no visible error or second active session is created | Medium   |
| MF-LOGOUT-007 | Clicking Profile Settings immediately after initiating Log Out is blocked | User is authenticated | 1. Open the profile dropdown and click Log Out<br>2. Immediately click Profile Settings in the same dropdown | Log out succeeds and navigation to Profile Settings is blocked; the Login page is displayed | Medium   |
