# Test Cases — Mifos

Generated: 2026-07-04T17:13:41.270116Z  
Model: openai/gpt-5-mini  

## Dashboard

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Dashboard and view Client Trends chart and summary cards | User logged in as <Authenticated user>, Authenticated user on the Home Page with an office context available (selected or default) | 1. Click the 'Dashboard' button on the Home page | Dashboard page is displayed; the 'Client Trends' chart is visible with legends for 'New Clients' and 'Closed Clients'; two summary cards titled 'Amount Pending / Disbursed' and 'Amount Collected' are visible for the selected office | high |
| TC-002 | WF-002 | Use Search Activity to filter dashboard activities | User logged in as <Authenticated user>, Authenticated user on the Home Page with an office context available (selected or default), Dashboard page is open | 1. Focus the 'Search Activity' field at the top of the Dashboard page<br>2. Enter <search term> in the 'Search Activity' field<br>3. Press Enter to execute the search | Dashboard updates to show only activities matching <search term>; the activity view and any related chart or list reflect the filtered set and unrelated activities are no longer visible | medium |
| TC-003 | WF-001 | Dashboard summary cards display 'No Data' when office has no financial information | User logged in as <Authenticated user>, Authenticated user on the Home Page with an office context available (selected or default), Selected office has no financial records for the summary period | 1. Click the 'Dashboard' button on the Home page | Both summary cards titled 'Amount Pending / Disbursed' and 'Amount Collected' display the text 'No Data' for the selected office; the 'Client Trends' chart is still visible (may show empty or zeroed series) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Unauthenticated user attempts to open Dashboard from Home page | User is not authenticated, Home Page is reachable | 1. Open the Home Page as an unauthenticated user<br>2. Click the Dashboard button/link in the top navigation | User is not taken to the Dashboard; the application redirects to the authentication/login screen or shows a login prompt. The Dashboard page is not displayed and Client Trends chart and summary cards are not visible. | high |
| TC-005 | WF-001 | Authenticated user with no office context attempts to open Dashboard | User is authenticated, No office context is selected or available for the user | 1. Sign in as an authenticated user who has no office context selected or assigned<br>2. From the Home Page, click the Dashboard button/link | Dashboard page does not load; the UI displays a visible error banner or inline message indicating an office context is required (office must be selected) and blocking access. The Client Trends chart and the summary cards (Amount Pending / Disbursed and Amount Collected) are not displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) | WF-002 | Very long search query is entered into Search Activity | Authenticated user on the Home Page with an office context available, Dashboard page is opened | 1. Focus the Search Activity field<br>2. Enter a very long search string (significantly longer than typical display width)<br>3. Press Enter or click the Search action | Search Activity input retains and displays the full entered string (no visible truncation in the input) and no inline validation error is shown for length | medium |
| TC-007 (input_edge) | WF-002 | Search query containing special characters and emoji | Authenticated user on the Home Page with an office context available, Dashboard page is opened | 1. Focus the Search Activity field<br>2. Enter a search string composed primarily of special characters and emoji<br>3. Press Enter or click the Search action | Search Activity input displays the exact entered special characters and emoji; no inline validation error is shown and the UI does not show an error state for the query | medium |
| TC-008 (input_edge) | WF-002 | Leading and trailing whitespace in search term is handled | Authenticated user on the Home Page with an office context available, Dashboard page is opened | 1. Focus the Search Activity field<br>2. Enter a search term that includes leading and trailing whitespace<br>3. Press Enter or click the Search action | After search executes, the Search Activity input displays the value without leading or trailing whitespace (visible trimmed value) and no inline validation error is shown | medium |
| TC-009 (data_edge) | WF-001 | Selected office has no available data — chart and summary cards show 'No Data' | Authenticated user on the Home Page with an office context available, The selected office has no client growth or financial data available | 1. Click the Dashboard button from the Home Page | Client Trends chart area displays a visible 'No Data' indicator and both summary cards ('Amount Pending / Disbursed' and 'Amount Collected') each display a visible 'No Data' label | medium |

---
