# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Dashboard

### Functional Tests

| TC ID       | Test Case                      | Preconditions               | Steps                                                                | Expected Result                                                                                                   | Priority |
| ----------- | ------------------------------ | --------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| MF-DASH-001 | Dashboard loads from Home page | User logged in              | 1. Login with valid credentials<br>2. From Home page click Dashboard | Dashboard page displayed with summary cards for total clients, active loans, pending approvals, portfolio at risk | High     |
| MF-DASH-002 | Summary cards display metrics  | User logged in, data exists | 1. Navigate to Dashboard                                             | Summary cards show correct counts for clients, loans, approvals                                                   | High     |

### Negative Tests

| TC ID       | Test Case                           | Preconditions                    | Steps                                                                                       | Expected Result                                                | Priority |
| ----------- | ----------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- |
| MF-DASH-005 | Dashboard with no data              | Fresh instance, no clients/loans | 1. Login and open Dashboard from Home                                                       | Dashboard shows zero counts or empty state appropriately       | Medium   |
| MF-DASH-006 | Dashboard refresh after transaction | User logged in, data exists      | 1. View dashboard metrics<br>2. Create a client or post a repayment<br>3. Refresh dashboard | Summary metrics reflect latest committed data                  | Medium   |
| MF-DASH-007 | Search Activity on the Dashboard filters displayed activities | User logged in, Dashboard page is open | 1. Focus the Search Activity field at the top of the Dashboard page<br>2. Enter a search term in the Search Activity field<br>3. Press Enter to execute the search | Dashboard updates to show only activities matching the search term; the activity view and any related chart or list reflect the filtered set and unrelated activities are no longer visible | Medium   |
