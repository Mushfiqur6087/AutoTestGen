# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Home

### Functional Tests

| TC ID       | Test Case                                                   | Preconditions                                 | Steps                                                    | Expected Result                                                                                                   | Priority |
| ----------- | ----------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| MF-HOME-001 | Dashboard button on Home page is blocked when no application context is loaded | Authenticated user session, no application context (Institution) loaded | 1. Log in as a valid user with no Institution context selected<br>2. Navigate to the Home Page<br>3. Click the Dashboard button<br>4. Also attempt to navigate directly to the Dashboard URL in the browser address bar | Both attempts are blocked: the Dashboard button click does not navigate away (button disabled or a blocking indicator is shown) and the user remains on the Home Page; direct navigation to the Dashboard URL is also blocked, either redirecting back to Home or showing a blocking notice, with Home Page content remaining visible | High     |
| MF-HOME-002 | Home page widgets and navigation tiles load successfully    | User logged in                                | 1. Login<br>2. Observe Home page                         | Home page loads without blank state or route error and shows configured landing content/cards/navigation elements | High     |
| MF-HOME-003 | Search Activity on the Home page filters the Recent Activities list | Authenticated user session with application context loaded | 1. Navigate to the Home Page<br>2. Enter a search term in the Search Activity input<br>3. Submit the search (press Enter or click the search control) | Recent Activities list displays only entries matching the search term; unrelated activities are no longer visible | High     |
| MF-HOME-005 | Accessing the Home Page while unauthenticated redirects to Login | User is not authenticated                     | 1. In a new browser session with no authentication, navigate to the Home Page URL<br>2. Observe the resulting page | Access is blocked due to missing authenticated session: browser is redirected to the Login page (login prompt displayed); Home Page content (welcome card and Search Activity input) is not visible | Medium   |
| MF-HOME-006 | Home page navigation to Dashboard                           | User logged in, user has dashboard permission | 1. Open Home page<br>2. Click Dashboard navigation entry | Dashboard page opens successfully                                                                                 | High     |
