# Test Cases — Mifos

Generated: 2026-07-04T17:13:41.270116Z  
Model: openai/gpt-5-mini  

## Home Page

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search recent system activity filters the Recent Activities list | Authenticated user session (successful login) with application context loaded | 1. Navigate to the Home Page (open the application's landing view)<br>2. Enter <search term> in the Search Activity input<br>3. Submit the search (press Enter or click the search control) | Recent Activities list displays only entries matching <search term>; unrelated activities are no longer visible | high |
| TC-002 | WF-002 | Clicking Dashboard opens the Dashboard page | Authenticated user session (successful login) with application context loaded | 1. Navigate to the Home Page (open the application's landing view)<br>2. Click the Dashboard button | The Dashboard page opens; the page heading 'Dashboard' is visible | high |
| TC-003 |  | Welcome card and system version information are visible on Home Page | Authenticated user session (successful login) with application context loaded | 1. Navigate to the Home Page (open the application's landing view)<br>2. Observe the main content area and the bottom of the page | The welcome card displays the text "Welcome, mifos!"; system version information for Mifos and Fineract is visible at the bottom of the page | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Access Home Page while unauthenticated (requires authenticated session) | User is not authenticated | 1. In a new browser session with no authentication, navigate to the Home Page URL<br>2. Observe the resulting page | Access is blocked due to missing authenticated session: browser is redirected to the Login page (login prompt displayed); Home Page content (welcome card and Search Activity input) is not visible | high |
| TC-005 | WF-002 | Click Dashboard button when application context is not loaded (precondition failure) | Authenticated user session, No application context loaded (no Institution selected) | 1. Log in as a valid user<br>2. Ensure no application context (Institution) is selected for the session<br>3. Navigate to the Home Page<br>4. Click the Dashboard button | Action is blocked due to missing application context: click does not navigate to the Dashboard; user remains on the Home Page; the Dashboard button is disabled or an inline blocking indicator is shown near the Dashboard control indicating application context is required | high |
| TC-006 | WF-002 | Directly navigate to Dashboard URL when application context is not loaded | Authenticated user session, No application context loaded (no Institution selected) | 1. Log in as a valid user<br>2. Ensure no application context (Institution) is selected for the session<br>3. In the browser address bar, navigate directly to the Dashboard URL<br>4. Observe the resulting page | Navigation is blocked due to missing application context: the Dashboard view is not displayed; the user is either redirected back to the Home Page or shown a blocking notice indicating application context is required; Home Page content remains visible | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (input_edge) | WF-001 | Search input accepts very long string (200+ characters) | Authenticated user session; Home Page is visible with Search_Activity input | 1. Focus the Search_Activity input<br>2. Type a string of 200+ characters into the Search_Activity input<br>3. Press Enter (submit the search) | Search executes successfully; the Search_Activity input displays the full 200+ character string and the Recent Activity area updates to show filtered results or a visible 'no results' / empty-state message | medium |
| TC-008 (input_edge) | WF-001 | Search input with special characters and emoji | Authenticated user session; Home Page is visible with Search_Activity input | 1. Focus the Search_Activity input<br>2. Type a string containing special characters and emoji into the Search_Activity input<br>3. Click the search control or press Enter to submit | Search executes successfully; the Search_Activity input displays the exact special characters and emoji entered and the Recent Activity area updates to reflect the search (showing matching items or a visible 'no results' message) | medium |
| TC-009 (input_edge) | WF-001 | Search input handles leading and trailing whitespace | Authenticated user session; Home Page is visible with Search_Activity input | 1. Focus the Search_Activity input<br>2. Type a search term with leading and trailing whitespace into the Search_Activity input<br>3. Press Enter (submit the search) | Search executes successfully; the Search_Activity input displays the entered value with leading and trailing whitespace trimmed and the Recent Activity area updates to show filtered results or a visible 'no results' message | low |
| TC-010 (interaction_edge) | WF-002 | Rapid double-click of Dashboard button | Authenticated user session; Home Page is visible with Dashboard button | 1. Click the Dashboard button<br>2. Immediately click the Dashboard button again within a short interval (e.g., two clicks within 300ms) | Single navigation to the Dashboard occurs (action succeeds); the Dashboard view is displayed and no duplicate navigations or duplicate visible dashboard pages are produced | medium |

---
