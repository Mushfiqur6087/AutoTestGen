# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Home

### Functional Tests

| TC ID       | Test Case                                                   | Preconditions                                 | Steps                                                    | Expected Result                                                                                                   | Priority |
| ----------- | ----------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| MF-HOME-001 | User lands on Home page after successful login              | Valid user credentials                        | 1. Login with valid tenant, username, and password       | Home page is displayed as the first authenticated page                                                            | High     |
| MF-HOME-002 | Home page widgets and navigation tiles load successfully    | User logged in                                | 1. Login<br>2. Observe Home page                         | Home page loads without blank state or route error and shows configured landing content/cards/navigation elements | High     |
| MF-HOME-003 | Top toolbar is visible on Home page                         | User logged in                                | 1. Login<br>2. Observe top header area                   | Toolbar displays application header, global search access, profile/user menu, and other permitted header actions  | High     |
| MF-HOME-005 | Home page route is accessible directly after authentication | User logged in                                | 1. Login<br>2. Enter Home route URL directly             | Home page opens successfully without redirect loop                                                                | Medium   |
| MF-HOME-006 | Home page navigation to Dashboard                           | User logged in, user has dashboard permission | 1. Open Home page<br>2. Click Dashboard navigation entry | Dashboard page opens successfully                                                                                 | High     |
