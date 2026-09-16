# Mifos Banking System Test Cases

**Website URL:** <http://localhost:4200>
**Test Suite Version:** 2.0 (Revised)

## Test Credentials

| Field    | Value    |
| -------- | -------- |
| Tenant   | default  |
| Username | mifos    |
| Password | password |

---

## Table of Contents

1. [Login](#1-login)
2. [Home](#2-home)
3. [Dashboard](#3-dashboard)
4. [Global Search](#4-global-search)
5. [Client Management](#5-client-management)
6. [Group Management](#6-group-management)
7. [Center Management](#7-center-management)
8. [Loan Products](#8-loan-products)
9. [Savings Products](#9-savings-products)
10. [Charges](#10-charges)
11. [Loan Account](#11-loan-account)
12. [Savings Account](#12-savings-account)
13. [Accounting - Chart of Accounts](#13-accounting---chart-of-accounts)
14. [Accounting - Journal Entries](#14-accounting---journal-entries)
15. [Users & Roles](#15-users--roles)
16. [Offices](#16-offices)
17. [Employees](#17-employees)
18. [Reports](#18-reports)
19. [Organization Settings](#19-organization-settings)
20. [Share Products](#20-share-products)
21. [Floating Rates](#21-floating-rates)
22. [Delinquency Management](#22-delinquency-management)
23. [Share Account](#23-share-account)
24. [Fixed & Recurring Deposit Accounts](#24-fixed--recurring-deposit-accounts)
25. [Accounting - Closures](#25-accounting---closures)
26. [Accounting Rules & Financial Activity Mappings](#26-accounting-rules--financial-activity-mappings)
27. [Provisioning](#27-provisioning)
28. [Teller & Cashier Management](#28-teller--cashier-management)
29. [Account Transfers & Standing Instructions](#29-account-transfers--standing-instructions)
30. [Tax Management](#30-tax-management)
31. [System Administration](#31-system-administration)
32. [Logout](#32-logout)

---

## 1. Login

### Functional Tests

| TC ID        | Test Case                            | Preconditions          | Steps                                                                                                                                            | Expected Result                                                                                                 | Priority |
| ------------ | ------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | -------- |
| MF-LOGIN-001 | Valid login with correct credentials | Mifos instance running | 1. Navigate to login page<br>2. Enter "default" as Tenant<br>3. Enter "mifos" as Username<br>4. Enter "password" as Password<br>5. Click "Login" | User is redirected to Home page, toolbar shows username                                                         | High     |
| MF-LOGIN-002 | Login page elements displayed        | None                   | 1. Navigate to login page                                                                                                                        | Tenant Identifier field, Username field, Password field, and Login button are visible with application branding | Medium   |

### Negative Tests

| TC ID        | Test Case         | Preconditions | Steps                                                                                                    | Expected Result                                       | Priority |
| ------------ | ----------------- | ------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-LOGIN-005 | Invalid username  | None          | 1. Enter valid tenant<br>2. Enter invalid username<br>3. Enter any password<br>4. Click "Login"          | Error message for invalid authentication is displayed | High     |
| MF-LOGIN-006 | Invalid password  | None          | 1. Enter valid tenant<br>2. Enter "mifos" as username<br>3. Enter incorrect password<br>4. Click "Login" | Error message displayed, user remains on login page   | High     |
| MF-LOGIN-007 | Empty username    | None          | 1. Enter valid tenant<br>2. Leave username empty<br>3. Enter password<br>4. Click "Login"                | Inline validation error shown for username            | High     |
| MF-LOGIN-008 | Empty password    | None          | 1. Enter valid tenant<br>2. Enter username<br>3. Leave password empty<br>4. Click "Login"                | Inline validation error shown for password            | High     |
| MF-LOGIN-009 | Both fields empty | None          | 1. Leave Username and Password empty<br>2. Click "Login"                                                 | Validation errors shown for all mandatory fields      | Medium   |

### Boundary Tests

| TC ID        | Test Case                                               | Preconditions          | Steps                                                                             | Expected Result                                                | Priority |
| ------------ | ------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- |
| MF-LOGIN-015 | Rapid double-click of Login with valid credentials does not create duplicate sessions | Valid account exists for the selected tenant | 1. Enter valid Tenant, Username, and Password<br>2. Rapidly click the Login button twice in immediate succession | Login succeeds once; user is redirected to the landing page and no duplicate error messages or duplicate login forms are displayed | Medium   |
| MF-LOGIN-017 | Login button remains disabled until Tenant, Username, and Password are all filled | None                   | 1. Observe the Login button state before filling any fields<br>2. Enter Tenant, Username, and Password one at a time, observing the button state after each | The Login button becomes enabled and clickable only after Tenant, Username, and Password are all filled | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                          | Preconditions          | Steps                                                                                      | Expected Result                                                            | Priority |
| ------------ | ------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------- |
| MF-LOGIN-020 | Session persists on page refresh after successful login            | User logged in         | 1. Login successfully<br>2. Refresh browser tab                                            | User remains authenticated and current page reloads successfully           | High     |
| MF-LOGIN-021 | Forgot Password link navigates to the Forgot Password page | None | 1. On the Login page, click the 'Forgot Password?' link | The Forgot Password page is displayed showing its page title and an input to enter the account email or username | Medium   |
| MF-LOGIN-022 | Extremely long Username and Password inputs (200+ characters) are rejected | Tenant is selected or defaults to the default tenant | 1. Enter a very long string (200+ characters) into the Username field<br>2. Enter a very long string (200+ characters) into the Password field<br>3. Click Login | Login is blocked; an inline validation message or the invalid-credentials error is shown on the login form | High     |

---

## 2. Home

### Functional Tests

| TC ID       | Test Case                                                   | Preconditions                                 | Steps                                                    | Expected Result                                                                                                   | Priority |
| ----------- | ----------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| MF-HOME-001 | Dashboard button on Home page is blocked when no application context is loaded | Authenticated user session, no application context (Institution) loaded | 1. Log in as a valid user with no Institution context selected<br>2. Navigate to the Home Page<br>3. Click the Dashboard button<br>4. Also attempt to navigate directly to the Dashboard URL in the browser address bar | Both attempts are blocked: the Dashboard button click does not navigate away (button disabled or a blocking indicator is shown) and the user remains on the Home Page; direct navigation to the Dashboard URL is also blocked, either redirecting back to Home or showing a blocking notice, with Home Page content remaining visible | High     |
| MF-HOME-002 | Home page widgets and navigation tiles load successfully    | User logged in                                | 1. Login<br>2. Observe Home page                         | Home page loads without blank state or route error and shows configured landing content/cards/navigation elements | High     |
| MF-HOME-003 | Search Activity on the Home page filters the Recent Activities list | Authenticated user session with application context loaded | 1. Navigate to the Home Page<br>2. Enter a search term in the Search Activity input<br>3. Submit the search (press Enter or click the search control) | Recent Activities list displays only entries matching the search term; unrelated activities are no longer visible | High     |
| MF-HOME-005 | Accessing the Home Page while unauthenticated redirects to Login | User is not authenticated                     | 1. In a new browser session with no authentication, navigate to the Home Page URL<br>2. Observe the resulting page | Access is blocked due to missing authenticated session: browser is redirected to the Login page (login prompt displayed); Home Page content (welcome card and Search Activity input) is not visible | Medium   |
| MF-HOME-006 | Home page navigation to Dashboard                           | User logged in, user has dashboard permission | 1. Open Home page<br>2. Click Dashboard navigation entry | Dashboard page opens successfully                                                                                 | High     |

---

## 3. Dashboard

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

---

## 4. Global Search

### Functional Tests

| TC ID         | Test Case                                | Preconditions          | Steps                                                                     | Expected Result                                                                         | Priority |
| ------------- | ---------------------------------------- | ---------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------- |
| MF-SEARCH-001 | Global search bar visible in toolbar     | User logged in         | 1. Observe top toolbar/header                                             | Search input is visible and accessible from authenticated pages                         | High     |
| MF-SEARCH-002 | Search active client by name             | Active client exists   | 1. Enter full or partial client name in global search<br>2. Submit search | Matching client appears in results with link to client detail page                      | High     |
| MF-SEARCH-003 | Search loan account by account number    | Loan account exists    | 1. Enter exact loan account number<br>2. Submit                           | Matching loan account appears in results and opens loan detail page when selected       | High     |
| MF-SEARCH-004 | Search savings account by account number | Savings account exists | 1. Enter exact savings account number<br>2. Submit                        | Matching savings account appears in results and opens savings detail page when selected | High     |

### Negative Tests

| TC ID         | Test Case                | Preconditions  | Steps                                                        | Expected Result                                                       | Priority |
| ------------- | ------------------------ | -------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- | -------- |
| MF-SEARCH-009 | Search non-existent term | User logged in | 1. Enter random string not mapped to any entity<br>2. Submit | "No results found" or equivalent empty-state message displayed        | Medium   |
| MF-SEARCH-010 | Unauthenticated user cannot open Global Search | User is not authenticated | 1. Open the application root URL as an unauthenticated user<br>2. Attempt to click the top-bar search icon | Search input does not open; the user is redirected to the login page and no search UI is focused or usable | Low      |

### Boundary Tests

| TC ID         | Test Case                                                  | Preconditions                                                    | Steps                                  | Expected Result                                                               | Priority |
| ------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-SEARCH-013 | Partial prefix match                                       | Multiple entities with similar prefixes exist                    | 1. Enter partial prefix of entity name | Relevant matching results are returned according to supported search behavior | Medium   |
| MF-SEARCH-014 | Opening an entity detail from search results is blocked when the user lacks detail-view permission | User can invoke search but lacks permission to view the matched entity's detail page | 1. Search for a term matching an entity the user lacks detail-view permission for<br>2. Click the matching item in the results dropdown | Navigation to the entity's detail page is blocked; an access-denied indicator is shown and the user remains on the current page | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                         | Preconditions                                | Steps                                     | Expected Result                                                          | Priority |
| ------------- | ----------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------ | -------- |
| MF-SEARCH-016 | Search result click navigates to correct entity detail page       | Searchable entity exists                     | 1. Run search<br>2. Click matching result | Correct entity profile/account page opens                                | High     |
| MF-SEARCH-017 | Search supports case-insensitive text matching                    | Searchable entity exists                     | 1. Search using different case variation  | Matching entity is returned regardless of letter case                    | Medium   |
| MF-SEARCH-018 | Search results update correctly across entity types for same term | Client/group/center with similar names exist | 1. Search shared term                     | Results include all authorized matching entity types without duplication | Medium   |

---

## 5. Client Management

### Functional Tests

| TC ID         | Test Case                      | Preconditions                          | Steps                                                                                                                                  | Expected Result                                                                                                                                       | Priority |
| ------------- | ------------------------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| MF-CLIENT-001 | Unauthenticated access to Clients page is blocked | User is not authenticated | 1. Navigate directly to the Clients page URL without an authenticated session | Access is blocked: the login page or login prompt is displayed and the Clients list is not shown | High     |
| MF-CLIENT-002 | Create new client successfully | At least one office exists             | 1. Click "+" on Clients page<br>2. Select Office<br>3. Enter First Name and Last Name<br>4. Set Submitted On date<br>5. Click "Submit" | New client created and appears in client list with Pending status                                                                                     | High     |
| MF-CLIENT-003 | Activate pending client        | Client in Pending status               | 1. Open client detail page<br>2. Click "Activate"<br>3. Set Activation Date<br>4. Submit                                               | Client status changes to "Active" (green chip)                                                                                                        | High     |
| MF-CLIENT-004 | Client detail page elements    | Active client exists                   | 1. Click client name in list                                                                                                           | Header shows full name, account number, status badge, activation date, office. Tabs: General, Accounts, Identifiers, Family Members, Notes, Documents | High     |
| MF-CLIENT-005 | Create client with invalid email format is rejected | None | 1. Open Create Client form<br>2. Enter an invalid email format in the Email Address field<br>3. Fill other required fields with valid values<br>4. Submit | Inline validation error appears on the Email Address field indicating it must be a valid email address; the form does not submit and no client is created | Medium   |
| MF-CLIENT-006 | Search clients by name         | Multiple clients exist                 | 1. Type name in search bar on Clients page                                                                                             | Table filters to matching clients                                                                                                                     | Medium   |
| MF-CLIENT-007 | Transfer client                | Active client exists, multiple offices | 1. Open client detail<br>2. Click "Transfer Client"<br>3. Select destination office<br>4. Submit                                       | Client transferred to new office                                                                                                                      | Medium   |
| MF-CLIENT-008 | Close client                   | Active client, no active accounts      | 1. Open client detail<br>2. Click "Close"<br>3. Provide closure reason<br>4. Submit                                                    | Client status changes to "Closed" (gray chip)                                                                                                         | Medium   |
| MF-CLIENT-009 | Add client identifier          | Active client exists                   | 1. Go to Identifiers tab<br>2. Add Document Type (National ID), Document Key<br>3. Submit                                              | Identifier added and visible in list                                                                                                                  | Medium   |
| MF-CLIENT-010 | Add client note                | Active client exists                   | 1. Go to Notes tab<br>2. Click "Add Note"<br>3. Enter note text<br>4. Submit                                                           | Note appears in chronological list                                                                                                                    | Low      |
| MF-CLIENT-011 | Pagination on clients list     | Many clients exist                     | 1. View Clients page<br>2. Navigate pages                                                                                              | Pagination controls work correctly, showing total count and page navigation                                                                           | Medium   |

### Negative Tests

| TC ID         | Test Case                                                   | Preconditions                         | Steps                                                                                                        | Expected Result                                                              | Priority |
| ------------- | ----------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | -------- |
| MF-CLIENT-012 | Create client without Office                                | None                                  | 1. Open Create Client form<br>2. Fill name fields but leave Office empty<br>3. Submit                        | Validation error "Office is required"                                        | High     |
| MF-CLIENT-013 | Create client without First Name                            | None                                  | 1. Open Create Client form<br>2. Leave First Name empty<br>3. Fill other required fields<br>4. Submit        | Validation error "First name is required"                                    | High     |
| MF-CLIENT-014 | Create client without Last Name                             | None                                  | 1. Open Create Client form<br>2. Leave Last Name empty<br>3. Fill other required fields<br>4. Submit         | Validation error "Last name is required"                                     | High     |
| MF-CLIENT-015 | Close client with active accounts                           | Client has active loan/savings        | 1. Try to close client                                                                                       | Error: cannot close client with active accounts                              | High     |
| MF-CLIENT-016 | Edit client profile details                                 | Active client exists                  | 1. Open client detail<br>2. Click Edit<br>3. Update fields such as mobile number or external ID<br>4. Submit | Updated values are saved and displayed on client profile                     | Medium   |
| MF-CLIENT-017 | Add family member to client                                 | Active client exists                  | 1. Open Family Members tab<br>2. Click Add<br>3. Enter relationship and basic details<br>4. Submit           | Family member is added to the list                                           | Medium   |
| MF-CLIENT-018 | Upload client document                                      | Active client exists                  | 1. Open Documents tab<br>2. Upload a valid file with description<br>3. Submit                                | Document is uploaded and listed under client documents                       | Medium   |
| MF-CLIENT-019 | Search clients by account number                            | Multiple clients exist                | 1. Enter client account number in list search                                                                | Matching client row is returned                                              | Medium   |
| MF-CLIENT-020 | Activate client with activation date before submission date | Pending client exists                 | 1. Open Activate dialog<br>2. Enter date earlier than Submitted On date<br>3. Submit                         | Validation error or business rule prevents activation                        | High     |
| MF-CLIENT-021 | Duplicate identifier for same client document type          | Active client with identifier exists  | 1. Add another identifier with same document type and key where uniqueness is enforced<br>2. Submit          | Validation or server error prevents duplicate identifier                     | Medium   |
| MF-CLIENT-022 | Transfer client to same office                              | Active client exists                  | 1. Click Transfer Client<br>2. Select current office<br>3. Submit                                            | Validation blocks no-op transfer or system handles without duplicate history | Low      |
| MF-CLIENT-023 | Close client without closure reason                         | Active client with no active accounts | 1. Click Close<br>2. Leave reason empty<br>3. Submit                                                         | Validation error shown for closure reason                                    | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                          | Preconditions                                     | Steps                                                                                      | Expected Result                                                                      | Priority |
| ------------- | -------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------- |
| MF-CLIENT-024 | Reject pending client                              | Pending client exists                             | 1. Open client detail<br>2. Click Reject<br>3. Enter rejection date/reason<br>4. Submit    | Client status changes to Rejected and no activation actions remain available         | High     |
| MF-CLIENT-025 | Withdraw pending client application                | Pending client exists                             | 1. Open client detail<br>2. Click Withdraw<br>3. Enter withdrawal reason/date<br>4. Submit | Client status changes to Withdrawn                                                   | Medium   |
| MF-CLIENT-026 | Reactivate closed client when business rules allow | Closed client exists and reactivation allowed     | 1. Open client detail<br>2. Click Reactivate<br>3. Submit                                  | Client returns to Active state with audit history preserved                          | Medium   |
| MF-CLIENT-027 | Client Detail action-bar shortcuts redirect to New Loan, New Savings, and New Share Account creation | Active client exists | 1. Open the Active client's Detail page<br>2. Click the "New Loan" action<br>3. Return to the client Detail page and click the "New Savings" action<br>4. Return to the client Detail page and click the "New Share Account" action | Each action navigates the browser to its respective creation page (New Loan, New Savings, New Share Account) with the page header visible | Medium   |
| MF-CLIENT-028 | Client charges tab supports add charge action      | Active client exists and charge definition exists | 1. Open client detail<br>2. Add charge<br>3. Submit                                        | Charge appears under client-related charges and is available for collection workflow | Medium   |
| MF-CLIENT-029 | Duplicate client creation with same external ID    | External ID uniqueness enforced                   | 1. Create client with already-used external ID<br>2. Submit                                | Validation or server-side error prevents duplicate external ID                       | High     |

---

## 6. Group Management

### Functional Tests

| TC ID        | Test Case                        | Preconditions                             | Steps                                                                                                  | Expected Result                                                               | Priority |
| ------------ | -------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | -------- |
| MF-GROUP-001 | View groups list                 | User logged in                            | 1. Navigate to Groups page                                                                             | Groups list loads with group name, account number, office, staff, and status  | High     |
| MF-GROUP-002 | Create group successfully        | Office exists                             | 1. Click Create Group<br>2. Select office<br>3. Enter group name<br>4. Set submitted date<br>5. Submit | Group is created in pending status                                            | High     |
| MF-GROUP-003 | Activate group                   | Pending group exists                      | 1. Open group detail<br>2. Click Activate<br>3. Set activation date<br>4. Submit                       | Group status changes to Active                                                | High     |
| MF-GROUP-004 | View group details               | Group exists                              | 1. Open a group record                                                                                 | Group profile displays general details, members, accounts, notes, and actions | High     |
| MF-GROUP-005 | Add client members to group      | Active group and active clients exist     | 1. Open group<br>2. Add members<br>3. Select eligible clients<br>4. Submit                             | Selected clients become group members                                         | High     |
| MF-GROUP-006 | Assign staff to group            | Group and staff exist                     | 1. Edit group<br>2. Select staff member<br>3. Submit                                                   | Staff assignment is saved                                                     | Medium   |
| MF-GROUP-007 | Transfer Clients action is unavailable on a Closed group | Group exists with Status = Closed | 1. Open the Group Detail page for a group whose Status is Closed<br>2. Click the Transfer Clients action/button | Transfer Clients action is blocked; members remain unchanged and no transfer dialog/procedure is initiated; the control is disabled or an inline error is shown indicating the action cannot be performed in the Closed state | Medium   |
| MF-GROUP-008 | Close group                      | Group has no blocking active constraints  | 1. Open active group<br>2. Click Close<br>3. Provide closure details<br>4. Submit                      | Group status changes to Closed                                                | Medium   |

### Negative Tests

| TC ID        | Test Case                                                   | Preconditions                                        | Steps                                                                                    | Expected Result                                              | Priority |
| ------------ | ----------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------- |
| MF-GROUP-009 | Create group without office                                 | None                                                 | 1. Open Create Group form<br>2. Leave office empty<br>3. Enter other fields<br>4. Submit | Validation error is shown for office                         | High     |
| MF-GROUP-010 | Create group without group name                             | None                                                 | 1. Open Create Group form<br>2. Leave group name empty<br>3. Submit                      | Validation error is shown for group name                     | High     |
| MF-GROUP-011 | Activate action is unavailable on a group that is already Active | Group exists with Status = Active | 1. Open the Group Detail page for a group whose Status is Active<br>2. Click the Activate action/button | Activate action is blocked; the group's Status remains Active; either the Activate control is not available/disabled or an inline error is shown indicating the action cannot be performed in the current state; no state change occurs | High     |
| MF-GROUP-012 | Add ineligible client to group                              | Client not eligible due to status/office constraints | 1. Add member to group<br>2. Select ineligible client                                    | Selection is blocked or submission fails with proper message | Medium   |
| MF-GROUP-013 | Edit action is unavailable on a Closed group | Group exists with Status = Closed | 1. Open the Group Detail page for a group whose Status is Closed<br>2. Click the Edit action/button | Edit is blocked; the Create Group form does not open for the Closed group; user sees the control disabled or an inline message indicating Closed groups cannot be edited; no changes are permitted | High     |

### Additional Coverage Tests

| TC ID        | Test Case                                              | Preconditions                    | Steps                                                      | Expected Result                                  | Priority |
| ------------ | ------------------------------------------------------ | -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ | -------- |
| MF-GROUP-014 | Generate Collection Sheet action is unavailable for a Pending group | Group exists with Status = Pending | 1. Open the Group Detail page for a group whose Status is Pending<br>2. Go to the Calendar/Meeting tab<br>3. Click Generate Collection Sheet | Generate Collection Sheet action is blocked; no collection sheet is generated; the control is disabled or an inline message is shown indicating the sheet cannot be generated for a Pending group | Medium   |
| MF-GROUP-015 | Remove member from group                               | Active group with members exists | 1. Open group members tab<br>2. Remove member<br>3. Submit | Member is removed according to business rules    | Medium   |
| MF-GROUP-016 | Reject pending group application                       | Pending group exists             | 1. Open group<br>2. Click Reject<br>3. Submit              | Group status changes to Rejected                 | Medium   |
| MF-GROUP-017 | Withdraw pending group application                     | Pending group exists             | 1. Open group<br>2. Click Withdraw<br>3. Submit            | Group status changes to Withdrawn                | Medium   |
| MF-GROUP-018 | Scheduling and recording meetings creates chronological entries in the group's meeting history | Group exists | 1. Open the Group Detail page and go to the Calendar/Meeting tab<br>2. Click Schedule Meeting, enter meeting date and agenda, and save<br>3. Click Record Meeting, enter meeting notes and attendance, and save | A scheduled meeting entry with the entered date/agenda and a recorded meeting entry with the entered notes both appear in the group's meeting list/history | Low      |

---

## 7. Center Management

### Functional Tests

| TC ID         | Test Case                  | Preconditions                              | Steps                                                                                                     | Expected Result                                          | Priority |
| ------------- | -------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------- |
| MF-CENTER-001 | View centers list          | User logged in                             | 1. Navigate to Centers page                                                                               | Centers list loads with center information               | High     |
| MF-CENTER-002 | Create center successfully | Office exists                              | 1. Click Create Center<br>2. Select office<br>3. Enter center name<br>4. Set submission data<br>5. Submit | Center is created in pending state                       | High     |
| MF-CENTER-003 | Activate center            | Pending center exists                      | 1. Open center detail<br>2. Click Activate<br>3. Enter activation date<br>4. Submit                       | Center becomes Active                                    | High     |
| MF-CENTER-004 | View center detail         | Center exists                              | 1. Open center                                                                                            | Center profile shows details, groups, staff, and actions | High     |
| MF-CENTER-005 | View existing group associations in Edit Center form | Center exists with linked groups | 1. Open center detail<br>2. Click Edit action button | Edit Center form opens pre-populated with the center's current Name, Office, Staff, External Id, Submitted On, and selected Groups | Medium   |
| MF-CENTER-006 | Assign staff to center     | Center and staff exist                     | 1. Edit center<br>2. Select staff<br>3. Submit                                                            | Staff assignment is saved                                | Medium   |
| MF-CENTER-007 | Transfer center            | Active center and destination office exist | 1. Open center<br>2. Click Transfer<br>3. Select destination office<br>4. Submit                          | Center is transferred successfully                       | Medium   |
| MF-CENTER-008 | Close center               | Center eligible for closure                | 1. Open center<br>2. Click Close<br>3. Submit with closure details                                        | Center status changes to Closed                          | Medium   |

### Negative Tests

| TC ID         | Test Case                                         | Preconditions                                      | Steps                                                | Expected Result                                   | Priority |
| ------------- | ------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- | -------- |
| MF-CENTER-009 | Create center without office                      | None                                               | 1. Leave office empty in create form<br>2. Submit    | Validation error shown for office                 | High     |
| MF-CENTER-010 | Create center without center name                 | None                                               | 1. Leave name empty<br>2. Submit                     | Validation error shown for center name            | High     |
| MF-CENTER-011 | Activate center using date before submission date | Pending center exists                              | 1. Enter invalid activation date<br>2. Submit        | Activation is prevented                           | High     |
| MF-CENTER-012 | Create Center blocked when no Office exists in system | No Offices exist in the system | 1. Ensure zero Offices are available for selection<br>2. Navigate to Centers page<br>3. Attempt to click Create Center | Create Center control is disabled or not visible; if clicking is possible, the form shows no selectable Office and cannot be submitted; no center is created | Medium   |
| MF-CENTER-013 | Unauthenticated user cannot access Centers page   | User is not authenticated                          | 1. Ensure the user session is logged out<br>2. Attempt to navigate to the Centers page via the Institution menu or direct URL | User is redirected to the login page or shown an authentication-required UI; the Centers list is not displayed | High     |

### Additional Coverage Tests

| TC ID         | Test Case                           | Preconditions                           | Steps                                                 | Expected Result                              | Priority |
| ------------- | ----------------------------------- | --------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | -------- |
| MF-CENTER-014 | Download Centers import template from Import Center dialog | Centers page is accessible | 1. Navigate to Centers page<br>2. Click Import Center button to open the Bulk Import Centers dialog<br>3. Click Download Template button | The centers import template file is downloaded by the browser | Medium   |
| MF-CENTER-015 | Import centers via file upload (happy path) | A valid centers import file is available | 1. Navigate to Centers page<br>2. Click Import Center button<br>3. Upload valid centers import file<br>4. Click Import button | Success notification is displayed confirming the import and the Centers table shows rows for the imported centers | Medium   |
| MF-CENTER-016 | Bulk Import Centers blocked when File upload left blank | None | 1. Navigate to Centers page<br>2. Click Import Center button<br>3. Leave File upload blank<br>4. Click Import button | Inline validation error appears on the File field indicating it is required; the import does not proceed and no centers are imported | Medium   |
| MF-CENTER-017 | View Group detail from Center's Groups tab | Center has at least one Group member | 1. Open center detail<br>2. Click Groups tab<br>3. Click View Group action for target group | Group Detail page opens showing the group's title and member list | Medium   |
| MF-CENTER-018 | Generate Collection Sheet from Center's Calendar/Meeting tab | Center has one or more Groups with clients and account data | 1. Open center detail<br>2. Click Calendar/Meeting tab<br>3. Click Generate Collection Sheet button | Collection sheet is displayed showing all groups and their clients with loan repayment and savings deposit amounts for batch data entry | Low      |

---

## 8. Loan Products

### Functional Tests

| TC ID        | Test Case                                      | Preconditions                       | Steps                                                                                                                                                                           | Expected Result                                                                  | Priority |
| ------------ | ---------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------- |
| MF-LPROD-001 | View loan products list                        | User logged in with permission      | 1. Navigate to Loan Products                                                                                                                                                    | Loan products list displays available products and status                        | High     |
| MF-LPROD-002 | Create loan product successfully               | Required accounting setup exists    | 1. Click Create Loan Product<br>2. Fill mandatory details including name, short name, fund, currency, principal, interest, repayment settings, accounting mappings<br>3. Submit | Loan product is created and visible in list                                      | High     |
| MF-LPROD-003 | View loan product detail                       | Loan product exists                 | 1. Open product record                                                                                                                                                          | Product detail shows terms, charges, accounting, and configuration tabs/sections | High     |
| MF-LPROD-004 | Edit loan product                              | Loan product exists and is editable | 1. Open product<br>2. Click Edit<br>3. Update editable fields<br>4. Submit                                                                                                      | Product updates are saved successfully                                           | High     |
| MF-LPROD-005 | Create declining balance loan product          | Required accounting setup exists    | 1. Create product with declining balance interest method                                                                                                                        | Product saves with correct calculation configuration                             | High     |
| MF-LPROD-006 | Create flat interest loan product              | Required accounting setup exists    | 1. Create product with flat interest method                                                                                                                                     | Product saves with flat interest configuration                                   | High     |
| MF-LPROD-007 | Unauthenticated user cannot access Loan Products page | User is not authenticated | 1. Ensure the user is logged out<br>2. Attempt to navigate directly to the Loan Products page URL | User is redirected to the login page; the Loan Products listing is not accessible without authentication | High      |
| MF-LPROD-008 | Configure accounting mappings for loan product | GL accounts exist                   | 1. Define asset, income, expense, liability mappings<br>2. Submit                                                                                                               | Product accounting configuration is saved                                        | High     |

### Negative Tests

| TC ID        | Test Case                                                                            | Preconditions          | Steps                                                                                    | Expected Result                           | Priority |
| ------------ | ------------------------------------------------------------------------------------ | ---------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-LPROD-011 | Create product without product name                                                  | None                   | 1. Leave product name empty<br>2. Fill other fields<br>3. Submit                         | Validation error shown for product name   | High     |
| MF-LPROD-012 | Create product without short name                                                    | None                   | 1. Leave short name empty<br>2. Submit                                                   | Validation error shown for short name     | High     |
| MF-LPROD-013 | Principal Amount Default outside the configured minimum/maximum range is blocked | None | 1. Set Principal Amount Minimum to a value A<br>2. Set Principal Amount Maximum to a value B greater than A<br>3. Set Principal Amount Default to a value outside the A-B range<br>4. Click Save | Save is blocked; Principal Amount Default field displays an inline validation error indicating the default must be within the configured minimum and maximum range | High     |
| MF-LPROD-014 | Invalid Start Date format prevents progressing through the wizard | None | 1. Open the Loan Product Create Wizard and stay on Step 1 (Details)<br>2. Enter an invalid date format into the Start Date field<br>3. Click Next | Cannot proceed to the next step; Start Date field displays an inline validation error indicating the entered value is not a valid date | High     |
| MF-LPROD-015 | Create product with missing mandatory accounting mappings when accounting is enabled | GL accounts incomplete | 1. Select accounting rule requiring mappings<br>2. Omit mandatory GL values<br>3. Submit | Validation error shown and save blocked   | High     |
| MF-LPROD-017 | Cancelling the Create Loan Product wizard discards entered changes | None | 1. Open the Create Loan Product wizard<br>2. Enter Product Name and Short Name<br>3. Click Cancel | The wizard closes and the Loan Products listing is visible; no new row for the entered Product Name appears in the table | High     |

---

## 9. Savings Products

### Functional Tests

| TC ID        | Test Case                                             | Preconditions                    | Steps                                                                                                                                       | Expected Result                                                                      | Priority |
| ------------ | ----------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------- |
| MF-SPROD-001 | View savings products list                            | User logged in with permission   | 1. Navigate to Savings Products                                                                                                             | Savings product list displays configured products and status                         | High     |
| MF-SPROD-002 | Create savings product successfully                   | Required accounting setup exists | 1. Click Create Savings Product<br>2. Fill mandatory product details, interest settings, withdrawal rules, accounting mappings<br>3. Submit | Savings product is created successfully                                              | High     |
| MF-SPROD-003 | View savings product details                          | Savings product exists           | 1. Open product                                                                                                                             | Product details show terms, interest settings, fees/charges, and accounting mappings | High     |
| MF-SPROD-004 | Edit savings product                                  | Savings product exists           | 1. Open product<br>2. Click Edit<br>3. Update allowed fields<br>4. Submit                                                                   | Changes are saved successfully                                                       | High     |
| MF-SPROD-005 | Configure interest-bearing savings product            | Required setup exists            | 1. Create product with interest calculation and posting rules                                                                               | Product stores interest settings correctly                                           | High     |
| MF-SPROD-006 | Configure overdraft-enabled savings product           | Feature supported                | 1. Enable overdraft settings during product creation<br>2. Save                                                                             | Product is created with overdraft rules                                              | Medium   |
| MF-SPROD-007 | Configure withdrawal fee or charge on savings product | Charges exist                    | 1. Link charge(s) to product<br>2. Save                                                                                                     | Product stores linked charge configuration                                           | Medium   |
| MF-SPROD-008 | Configure accounting mappings for savings product     | GL accounts exist                | 1. Set liability, expense, income, and overdraft-related mappings<br>2. Submit                                                              | Accounting setup is saved successfully                                               | High     |
| MF-SPROD-009 | Create zero-interest savings product                  | Required setup exists            | 1. Create product with no interest                                                                                                          | Product is saved successfully with non-interest-bearing behavior                     | Medium   |

### Negative Tests

| TC ID        | Test Case                                                                                | Preconditions              | Steps                                                                                   | Expected Result                               | Priority |
| ------------ | ---------------------------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------- | -------- |
| MF-SPROD-010 | Create product without name                                                              | None                       | 1. Leave product name empty<br>2. Submit                                                | Validation error shown for product name       | High     |
| MF-SPROD-011 | Create product without short name                                                        | None                       | 1. Leave short name empty<br>2. Submit                                                  | Validation error shown for short name         | High     |
| MF-SPROD-012 | Enable Minimum Required Balance then leave amount blank and Save | User authenticated with product-management permissions, on Savings Products page | 1. Click '+ Create Savings Product' to open wizard<br>2. Navigate to Step 4 (Settings)<br>3. Check 'Enforce Minimum Required Balance' checkbox<br>4. Leave the 'Minimum Required Balance' field blank<br>5. Progress to final step and click Save | Form does not submit; Minimum Required Balance field displays an inline validation error indicating it is required when Enforce Minimum Required Balance is enabled; product is not created | High     |
| MF-SPROD-013 | Create product with missing accounting mappings when accounting rule requires them       | GL mappings incomplete     | 1. Select accounting option requiring mappings<br>2. Omit mandatory fields<br>3. Submit | Validation blocks save                        | High     |
| MF-SPROD-014 | Save is blocked for user without product-management permissions | User authenticated as a user without product-management permissions | 1. Log in as user without product-management permissions<br>2. Navigate directly to the Create Savings Product wizard<br>3. Fill all required fields to enable Save<br>4. Click Save | Save action is blocked; form does not submit and no product is created; user remains on the wizard (Save disabled or submission rejected due to missing permissions) | Medium   |
| MF-SPROD-015 | Enable Overdraft and enter Maximum Overdraft Amount with excessive decimal precision is blocked | User authenticated with product-management permissions, Savings Products page is open | 1. Click '+ Create Savings Product'<br>2. Navigate to Step 4 (Settings)<br>3. Check 'Is Overdraft Allowed' checkbox<br>4. Enter a Maximum Overdraft Amount with more decimal places than the field supports<br>5. Click Save | Save is blocked; an inline validation error is shown on Maximum Overdraft Amount indicating the value has too many decimal places | High     |

---

## 10. Charges

### Functional Tests

| TC ID         | Test Case                                   | Preconditions                          | Steps                                                                                                               | Expected Result                                                 | Priority |
| ------------- | ------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------- |
| MF-CHARGE-001 | View charges list                           | User logged in with permission         | 1. Navigate to Charges                                                                                              | Charges list displays configured charge definitions             | High     |
| MF-CHARGE-002 | Create flat charge successfully             | None                                   | 1. Click Create Charge<br>2. Enter name, currency, flat amount, applicable time/type and target entity<br>3. Submit | Charge is created successfully                                  | High     |
| MF-CHARGE-003 | Create percentage-based charge successfully | None                                   | 1. Create charge with percentage amount and valid basis                                                             | Charge is created successfully with percentage configuration    | High     |
| MF-CHARGE-004 | Edit charge definition                      | Existing charge exists and is editable | 1. Open charge<br>2. Click Edit<br>3. Update allowed fields<br>4. Submit                                            | Updated values are saved                                        | High     |
| MF-CHARGE-005 | Create loan disbursement charge             | Loan charge applicability supported    | 1. Create charge applicable to loans at disbursement                                                                | Charge is available for relevant loan product/account workflows | High     |
| MF-CHARGE-006 | Create savings withdrawal charge            | Savings applicability supported        | 1. Create charge applicable to savings withdrawals                                                                  | Charge can be linked to savings products/accounts               | Medium   |
| MF-CHARGE-007 | Create client-level charge                  | Client charges supported               | 1. Create charge applicable to clients                                                                              | Charge is available for client charge assignment                | Medium   |
| MF-CHARGE-008 | View charge details                         | Charge exists                          | 1. Open charge record                                                                                               | Detail page shows amount, type, applicability, and timing       | Medium   |

### Negative Tests

| TC ID         | Test Case                                                      | Preconditions | Steps                                                                     | Expected Result                           | Priority |
| ------------- | -------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-CHARGE-009 | Create charge without name                                     | None          | 1. Leave name empty<br>2. Submit                                          | Validation error shown for charge name    | High     |
| MF-CHARGE-010 | Create charge without amount or percentage                     | None          | 1. Omit required amount field<br>2. Submit                                | Validation error prevents save            | High     |
| MF-CHARGE-011 | Submit Create Charge form with all required fields empty       | None          | 1. Open the Create Charge form<br>2. Leave Charge Name, Charge Applies To, Currency, and Amount all empty<br>3. Click Submit | Inline validation errors appear on Charge Name, Charge Applies To, Currency, and Amount indicating they are required; the form does not submit and no charge definition is created | High     |
| MF-CHARGE-012 | Create charge with Charge Applies To left blank is rejected | None          | 1. Open the Create Charge form<br>2. Leave the Charge Applies To dropdown unselected<br>3. Enter valid Charge Name, Currency, and Amount<br>4. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required; the form does not submit and no charge definition is created | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                              | Preconditions                     | Steps                                                              | Expected Result                                                                    | Priority |
| ------------- | ---------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- |
| MF-CHARGE-014 | Unauthenticated user cannot access the Charges page                    | User is not logged in             | 1. Attempt to navigate directly to the Charges page URL or click the Products/Charges navigation link | The login page or login prompt is displayed and the Charges table is not accessible; the unauthenticated user cannot view the Charges page | Medium   |
| MF-CHARGE-015 | Charge linked to product appears during account lifecycle              | Product linked to charge exists   | 1. Create account from linked product<br>2. Trigger relevant event | Charge is assessed according to configuration                                      | High     |
| MF-CHARGE-016 | Charge creation is blocked when no active organization is selected     | User has permissions but no active organization is selected | 1. Ensure the user session has no active organization selected<br>2. Click Create Charge and fill Charge Name, Charge Applies To, Currency, and Amount with valid values<br>3. Click Submit | Submission is blocked; no charge definition is created; a visible error or blocking message indicates the action cannot proceed because no active organization is selected; the Create Charge form remains open | High     |
| MF-CHARGE-017 | Waive charge from applicable account                                   | Applied charge exists             | 1. Open charge on account<br>2. Waive charge                       | Charge outstanding amount is reduced according to waived amount                    | Medium   |

---

## 11. Loan Account

### Functional Tests

| TC ID       | Test Case                                               | Preconditions                                 | Steps                                                                                                                                             | Expected Result                                                                            | Priority |
| ----------- | ------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------- |
| MF-LOAN-001 | Create new loan application for client                  | Active client and loan product exist          | 1. Open client profile<br>2. Click New Loan<br>3. Select product<br>4. Enter principal, term, interest, disbursement/submission data<br>5. Submit | Loan account is created in Submitted and Pending Approval state                            | High     |
| MF-LOAN-002 | Approve loan application                                | Pending approval loan exists                  | 1. Open loan account<br>2. Click Approve<br>3. Enter approval details<br>4. Submit                                                                | Loan moves to Approved state                                                               | High     |
| MF-LOAN-003 | Disburse approved loan                                  | Approved loan exists                          | 1. Open approved loan<br>2. Click Disburse<br>3. Enter disbursement date and amount<br>4. Submit                                                  | Loan becomes Active and disbursement transaction is recorded                               | High     |
| MF-LOAN-004 | View repayment schedule                                 | Loan exists                                   | 1. Open loan account                                                                                                                              | Repayment schedule is displayed with installments, principal, interest, fees, and balances | High     |
| MF-LOAN-005 | Make repayment                                          | Active loan with amount due exists            | 1. Open loan<br>2. Click Repayment<br>3. Enter transaction date and amount<br>4. Submit                                                           | Repayment is posted and outstanding balances are updated                                   | High     |
| MF-LOAN-006 | Undo repayment or reverse transaction where supported   | Loan repayment exists and user has permission | 1. Open repayment transaction<br>2. Reverse or undo                                                                                               | Transaction is reversed according to business rules and balances are recalculated          | Medium   |
| MF-LOAN-007 | View loan transactions                                  | Loan with transactions exists                 | 1. Open loan transactions tab/section                                                                                                             | Full transaction history is displayed                                                      | High     |
| MF-LOAN-008 | Add loan charge                                         | Loan exists and charge definition exists      | 1. Open loan<br>2. Add charge<br>3. Submit                                                                                                        | Charge is added to the loan account                                                        | Medium   |
| MF-LOAN-009 | Waive loan charge                                       | Loan charge exists                            | 1. Open loan charge<br>2. Waive charge                                                                                                            | Charge amount is reduced appropriately                                                     | Medium   |
| MF-LOAN-010 | Reschedule loan where supported                         | Loan eligible for rescheduling                | 1. Open loan<br>2. Start reschedule workflow<br>3. Submit new schedule details                                                                    | Loan repayment schedule is updated after approval/process completion                       | Medium   |
| MF-LOAN-011 | Multi-disbursement loan additional tranche disbursement | Active multi-disbursement loan exists         | 1. Open loan<br>2. Disburse next tranche<br>3. Submit                                                                                             | Additional disbursement is recorded and schedule/balance updated                           | Medium   |
| MF-LOAN-012 | Foreclosure or close loan as closed obligations met     | Active loan eligible for closure              | 1. Open loan<br>2. Complete closure action                                                                                                        | Loan reaches appropriate closed status                                                     | High     |
| MF-LOAN-013 | Loan write-off                                          | Delinquent loan eligible for write-off        | 1. Open loan<br>2. Click Write Off<br>3. Enter date<br>4. Submit                                                                                  | Loan status changes to written-off and accounting entries are posted                       | High     |

### Negative Tests

| TC ID       | Test Case                                                  | Preconditions                | Steps                                                               | Expected Result                                 | Priority |
| ----------- | ---------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- | -------- |
| MF-LOAN-014 | Disburse action unavailable while loan is Submitted and Pending Approval | Loan exists in Submitted and Pending Approval state | 1. Open the loan account in Submitted and Pending Approval state<br>2. Inspect the action bar for a Disburse action | Disburse action/button is not visible in the action bar; disbursement cannot be initiated and no disbursement is recorded | High     |
| MF-LOAN-015 | Approve action unavailable when loan is already Approved | Loan exists in Approved state | 1. Open the loan account in Approved state<br>2. Inspect the action bar for an Approve action | Approve action/button is not visible in the action bar; no approve dialog can be opened and the loan remains in Approved state | High     |
| MF-LOAN-016 | No actions available when loan is Closed | Loan exists in Closed state | 1. Open the loan account in Closed state<br>2. Inspect the action bar for available actions | Action bar shows no actionable buttons for the Closed state; no action can be performed from the UI | High     |
| MF-LOAN-017 | Repayment equal to outstanding due closes the loan; one unit less keeps it Active | Active loan exists with a known outstanding amount due | 1. Make a repayment equal to the full outstanding amount due and submit<br>2. Observe the loan status<br>3. On a separate Active loan, make a repayment of one unit less than the amount due and submit<br>4. Observe the loan status | The repayment equal to the full amount due is posted and the loan status changes to Closed; the repayment of one unit less than the amount due is posted as a partial repayment, the balance is reduced accordingly, and the loan status remains Active | High     |
| MF-LOAN-018 | Repayment on non-active loan                               | Loan not in active state     | 1. Attempt repayment                                                | Action is blocked                               | High     |
| MF-LOAN-019 | Disbursement is blocked when required Transaction Amount is left blank | Approved loan exists | 1. Open the Disburse dialog for the approved loan<br>2. Leave the Transaction Amount field blank<br>3. Click Disburse/Submit | Disburse dialog does not submit; Transaction Amount field displays an inline validation error indicating it is required; loan remains in Approved state and no disbursement is recorded | High     |
| MF-LOAN-021 | Prepay an Active loan reduces the outstanding balance | Active loan exists | 1. Open the loan account<br>2. Click the Prepay Loan action<br>3. Enter prepayment amount and payment type<br>4. Submit | Transactions table shows a prepayment transaction for the entered amount and the Loan Balance decreases accordingly | Medium   |

### Additional Coverage Tests

| TC ID       | Test Case                                                            | Preconditions                                             | Steps                                                | Expected Result                                                                 | Priority |
| ----------- | -------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------- | -------- |
| MF-LOAN-022 | Reject loan application                                              | Pending approval loan exists                              | 1. Open loan<br>2. Reject application<br>3. Submit   | Loan status changes to Rejected                                                 | High     |
| MF-LOAN-023 | Withdraw loan application before approval                            | Submitted loan exists                                     | 1. Open loan<br>2. Withdraw application<br>3. Submit | Loan status changes to Withdrawn by client/officer as supported                 | Medium   |
| MF-LOAN-024 | Undo approval of loan where supported                                | Approved loan not yet disbursed                           | 1. Open approved loan<br>2. Undo approval            | Loan returns to prior workflow state                                            | Medium   |
| MF-LOAN-025 | Apply payment allocation rules correctly for mixed due amounts       | Active loan with principal, interest, fees, penalties due | 1. Make repayment                                    | Amount is allocated according to configured repayment strategy                  | High     |
| MF-LOAN-026 | Apply Charge Off action on an Active loan                            | Active loan exists and is eligible for charge off          | 1. Open the loan account<br>2. Click the Charge Off action<br>3. Confirm | A success notification is displayed on the Loan Detail page indicating the charge off action was applied | Medium   |
| MF-LOAN-027 | Loan schedule recalculates after transaction reversal                | Loan with repayment reversal exists                       | 1. Reverse repayment                                 | Outstanding balances and schedule-derived figures are recalculated consistently | High     |
| MF-LOAN-028 | Overpayment handling on loan                                         | Loan allows overpayment or prepayment                     | 1. Make repayment above due amount                   | Excess amount is handled according to business rules without corruption         | Medium   |
| MF-LOAN-029 | Loan notes and documents can be added                                | Loan exists                                               | 1. Add note or upload document                       | Supporting artifacts are stored and visible on loan profile                     | Low      |
| MF-LOAN-030 | Loan guarantor or collateral tab accessible where feature is enabled | Feature enabled and loan exists                           | 1. Open relevant tab                                 | Guarantor/collateral workflows are available and functional                     | Low      |

---

## 12. Savings Account

### Functional Tests

| TC ID      | Test Case                                                     | Preconditions                                                              | Steps                                                                                                               | Expected Result                                            | Priority |
| ---------- | ------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| MF-SAV-001 | Create savings account for client                             | Active client and savings product exist                                    | 1. Open client profile<br>2. Click New Savings Account<br>3. Select product<br>4. Fill required fields<br>5. Submit | Savings account is created in submitted/pending state      | High     |
| MF-SAV-002 | Approve savings account                                       | Pending savings account exists                                             | 1. Open account<br>2. Click Approve<br>3. Submit                                                                    | Savings account moves to approved state                    | High     |
| MF-SAV-003 | Activate savings account                                      | Approved savings account exists                                            | 1. Open account<br>2. Click Activate<br>3. Enter activation date<br>4. Submit                                       | Savings account becomes Active                             | High     |
| MF-SAV-004 | Deposit into active savings account                           | Active savings account exists                                              | 1. Open account<br>2. Click Deposit<br>3. Enter amount and date<br>4. Submit                                        | Deposit transaction is posted and balance increases        | High     |
| MF-SAV-005 | Withdraw from active savings account                          | Active savings account with sufficient balance or allowed overdraft exists | 1. Open account<br>2. Click Withdraw<br>3. Enter amount and date<br>4. Submit                                       | Withdrawal transaction is posted and balance decreases     | High     |
| MF-SAV-006 | View savings transactions                                     | Savings account with transactions exists                                   | 1. Open transactions section                                                                                        | Transaction history is displayed correctly                 | High     |
| MF-SAV-007 | Post interest to savings account                              | Interest-bearing savings account exists and posting is due                 | 1. Run posting event or inspect posted account                                                                      | Interest posting appears correctly in transactions/balance | Medium   |
| MF-SAV-008 | Add charge to savings account                                 | Active account and charge exist                                            | 1. Open account<br>2. Add charge<br>3. Submit                                                                       | Charge is added to the savings account                     | Medium   |
| MF-SAV-009 | Close savings account                                         | Active savings account eligible for closure                                | 1. Open account<br>2. Click Close<br>3. Submit closure details                                                      | Account status changes to Closed                           | High     |
| MF-SAV-010 | Reactivate or reopen eligible savings account where supported | Closed account and business rule allow                                     | 1. Open account<br>2. Use reactivation action                                                                       | Account returns to active workflow as supported            | Low      |

### Negative Tests

| TC ID      | Test Case                                                       | Preconditions                    | Steps                                                | Expected Result                                 | Priority |
| ---------- | --------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------- | ----------------------------------------------- | -------- |
| MF-SAV-011 | Create savings account without product                          | Active client exists             | 1. Start application<br>2. Omit product<br>3. Submit | Validation error shown                          | High     |
| MF-SAV-012 | Deposit rejected when an invalid Transaction Date is entered    | Active savings account exists    | 1. Open Deposit dialog<br>2. Enter invalid/impossible Transaction Date<br>3. Submit | Inline validation error shown on Transaction Date field; deposit is not recorded | High     |
| MF-SAV-013 | Withdraw more than available balance when overdraft not allowed | Active account exists            | 1. Attempt excessive withdrawal                      | Transaction is blocked with appropriate message | High     |
| MF-SAV-014 | Deposit negative or zero amount                                 | Active account exists            | 1. Enter invalid deposit amount<br>2. Submit         | Validation error shown                          | High     |
| MF-SAV-015 | Withdraw on non-active account                                  | Account not active               | 1. Attempt withdrawal                                | Action is blocked                               | High     |
| MF-SAV-016 | Close savings account with blocked pending conditions           | Account has holds or constraints | 1. Attempt closure                                   | Business rule prevents closure                  | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                                 | Preconditions                                       | Steps                                                                            | Expected Result                                                               | Priority |
| ---------- | ------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-SAV-017 | Reject savings account application                                        | Pending account exists                              | 1. Open account<br>2. Reject application<br>3. Submit                            | Account status changes to Rejected                                            | Medium   |
| MF-SAV-018 | Undo approval of savings account before activation where supported        | Approved account exists                             | 1. Open approved account<br>2. Undo approval                                     | Account returns to previous state                                             | Low      |
| MF-SAV-019 | Waive savings account charge                                              | Charge exists on account                            | 1. Open charge<br>2. Waive                                                       | Outstanding charge is reduced correctly                                       | Medium   |
| MF-SAV-020 | Overdraft-enabled account allows negative balance within configured limit | Active overdraft-enabled account exists             | 1. Withdraw amount exceeding current positive balance but within overdraft limit | Withdrawal succeeds and resulting balance respects configured overdraft rules | Medium   |
| MF-SAV-021 | Savings notes and documents can be maintained                             | Savings account exists                              | 1. Add note/upload document                                                      | Records are saved and visible                                                 | Low      |
| MF-SAV-022 | View interest calculation summary for an active savings account           | Active savings account exists with product settings that determine interest calculation | 1. Open account<br>2. Click Calculate Interest                                   | Interest calculation summary/preview is displayed showing the calculated interest amount according to product settings and the period selected | Medium   |

---

## 13. Accounting - Chart of Accounts

### Functional Tests

| TC ID      | Test Case                     | Preconditions                             | Steps                                                                  | Expected Result                                                                | Priority |
| ---------- | ----------------------------- | ----------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------- |
| MF-COA-001 | View chart of accounts        | User with accounting permission           | 1. Navigate to Chart of Accounts                                       | GL accounts tree/list is displayed grouped by account type                     | High     |
| MF-COA-002 | Create header account         | Accounting access available               | 1. Create new GL account as header<br>2. Submit                        | Header account is created successfully                                         | High     |
| MF-COA-003 | Create non-header account     | Parent/header account exists where needed | 1. Create new GL account with type, usage, classification<br>2. Submit | GL account is created and visible in chart                                     | High     |
| MF-COA-004 | Edit GL account               | Editable GL account exists                | 1. Open GL account<br>2. Edit details<br>3. Submit                     | Changes are saved successfully                                                 | High     |
| MF-COA-005 | Disable or close GL account   | Eligible account exists                   | 1. Open account<br>2. Disable/close                                    | Account status changes and account is unavailable for future use as configured | Medium   |
| MF-COA-006 | View GL account usage details | GL account exists                         | 1. Open GL account detail                                              | Details show account classification, usage type, and relationships             | Medium   |

### Negative Tests

| TC ID      | Test Case                                                | Preconditions               | Steps                                            | Expected Result                                   | Priority |
| ---------- | -------------------------------------------------------- | --------------------------- | ------------------------------------------------ | ------------------------------------------------- | -------- |
| MF-COA-007 | Create GL account without name                           | None                        | 1. Leave name empty<br>2. Submit                 | Validation error shown                            | High     |
| MF-COA-008 | Create GL account without account type                   | None                        | 1. Omit account type/classification<br>2. Submit | Validation error shown                            | High     |
| MF-COA-009 | Duplicate GL account code                                | Existing code exists        | 1. Create another GL account using same code     | Validation or server-side uniqueness error occurs | High     |
| MF-COA-010 | Disable GL account that is constrained by business rules | Account linked or protected | 1. Attempt disable/close action                  | Operation is blocked with correct error message   | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                        | Preconditions     | Steps                                                       | Expected Result                                       | Priority |
| ---------- | ---------------------------------------------------------------- | ----------------- | ----------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-COA-011 | Manual entries allowed only for accounts with correct usage type | GL account exists | 1. Attempt journal entry on restricted and allowed accounts | Only accounts eligible for manual posting can be used | High     |

---

## 14. Accounting - Journal Entries

### Functional Tests

| TC ID      | Test Case                                          | Preconditions                    | Steps                                                                                                        | Expected Result                                                                             | Priority |
| ---------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | -------- |
| MF-JRN-001 | View journal entries list                          | User with accounting permission  | 1. Navigate to Journal Entries                                                                               | Journal entries list is displayed with date, office, transaction ID, debit, and credit data | High     |
| MF-JRN-002 | Create manual journal entry                        | Eligible GL accounts exist       | 1. Click Create Journal Entry<br>2. Select office/date<br>3. Add balanced debit and credit rows<br>4. Submit | Journal entry is posted successfully                                                        | High     |
| MF-JRN-003 | Reverse manual journal entry where supported       | Existing reversible entry exists | 1. Open journal entry<br>2. Reverse it                                                                       | Reversal entry is created and reflected in list                                             | High     |
| MF-JRN-004 | Filter journal entries by Entry Type using dropdown filter | Journal entries exist with varying Entry Types; user has accounting permission | 1. Navigate to Journal Entries<br>2. In the filter bar, select an Entry Type from the Entry Type dropdown filter<br>3. Apply the filter | The Journal Entries table displays only rows matching the selected Entry Type; rows with other entry types are no longer visible in the results | Medium   |
| MF-JRN-005 | Filter journal entries by office or transaction ID | Journal entries exist            | 1. Apply office/ID filter                                                                                    | Matching entries are displayed                                                              | Medium   |

### Negative Tests

| TC ID      | Test Case                                          | Preconditions              | Steps                                                         | Expected Result                           | Priority |
| ---------- | -------------------------------------------------- | -------------------------- | ------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-JRN-006 | Submit unbalanced journal entry                    | Eligible GL accounts exist | 1. Add debit and credit rows with unequal totals<br>2. Submit | Validation prevents posting               | High     |
| MF-JRN-007 | Submit journal entry without mandatory office/date | None                       | 1. Omit required fields<br>2. Submit                          | Validation error shown                    | High     |
| MF-JRN-008 | Submit journal entry with Amount entered at excessive decimal precision | Eligible GL accounts exist | 1. Add Journal Entry form open<br>2. Select Office, Currency, Transaction Date<br>3. Add an entry line and select a GL Account<br>4. Enter an Amount with more decimal places than the currency's supported precision<br>5. Add balancing entry lines so totals would match if precision were accepted<br>6. Submit | Submission is blocked; inline validation indicates the Amount precision is unsupported and prevents the journal entry from being created | High     |
| MF-JRN-009 | Rapid double-submission of Create Journal Entry does not create duplicate entries | Eligible GL accounts exist | 1. Fill in Office, Currency, Transaction Date, and balanced entry lines in the Journal Entry form<br>2. Click 'Create Journal Entry' twice in rapid succession (double-click)<br>3. Return to the Journal Entries table or refresh | Only one journal entry is created; the Journal Entries table shows a single new entry and no duplicate rows after the rapid double-click | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                | Preconditions             | Steps                                    | Expected Result                                        | Priority |
| ---------- | -------------------------------------------------------- | ------------------------- | ---------------------------------------- | ------------------------------------------------------ | -------- |
| MF-JRN-010 | View journal entry detail showing Reference Number preserved exactly as entered | Entry exists with a Reference Number containing special characters/emoji | 1. Create (or open) a journal entry with a Reference Number that includes special characters and emoji<br>2. Open the journal entry detail view | The journal entry detail view displays the Reference Number exactly as entered, including special characters and emoji | Medium   |
| MF-JRN-011 | Backdated journal entry follows accounting closure rules | Closure exists for period | 1. Attempt manual entry in closed period | Operation is blocked if closure rules disallow posting | High     |

---

## 15. Users & Roles

### Functional Tests

| TC ID       | Test Case                      | Preconditions                   | Steps                                                                                                                           | Expected Result                                                    | Priority |
| ----------- | ------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------- |
| MF-USER-001 | View users list                | Admin user logged in            | 1. Navigate to Users                                                                                                            | Users list displays username, office, roles, and status            | High     |
| MF-USER-002 | Create new user successfully   | Office and role exist           | 1. Click Create User<br>2. Enter username, first name, last name, email if applicable, office, roles, and password<br>3. Submit | User is created successfully and appears in users list             | High     |
| MF-USER-003 | View user details              | User exists                     | 1. Open user record                                                                                                             | User profile displays office, assigned roles, status, and metadata | High     |
| MF-USER-004 | Edit user details              | Editable user exists            | 1. Open user<br>2. Click Edit<br>3. Update allowed fields<br>4. Submit                                                          | User details are updated successfully                              | High     |
| MF-USER-005 | Assign additional role to user | User and role exist             | 1. Edit user roles<br>2. Add role<br>3. Submit                                                                                  | New role is assigned successfully                                  | High     |
| MF-USER-006 | Remove role from user          | User with multiple roles exists | 1. Edit user roles<br>2. Remove role<br>3. Submit                                                                               | Role is removed successfully according to business rules           | Medium   |
| MF-USER-007 | Disable user                   | Active user exists              | 1. Open user<br>2. Disable/inactivate user                                                                                      | User becomes inactive and cannot authenticate                      | High     |
| MF-USER-008 | Re-enable disabled user        | Disabled user exists            | 1. Open disabled user<br>2. Enable user                                                                                         | User is restored to active status                                  | Medium   |
| MF-USER-009 | View roles list                | Admin user logged in            | 1. Navigate to Roles                                                                                                            | Roles list loads with role names and status                        | High     |
| MF-USER-010 | Create role successfully       | Admin permissions available     | 1. Click Create Role<br>2. Enter role name and permissions<br>3. Submit                                                         | Role is created successfully                                       | High     |
| MF-USER-011 | Edit role permissions          | Existing role exists            | 1. Open role<br>2. Update permission mappings<br>3. Submit                                                                      | Role permissions are updated successfully                          | High     |

### Negative Tests

| TC ID       | Test Case                                    | Preconditions                  | Steps                                  | Expected Result                                             | Priority |
| ----------- | -------------------------------------------- | ------------------------------ | -------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-USER-013 | Create user without username                 | None                           | 1. Leave username empty<br>2. Submit   | Validation error shown for username                         | High     |
| MF-USER-014 | Create user without office                   | None                           | 1. Omit office selection<br>2. Submit  | Validation error shown for office                           | High     |
| MF-USER-015 | Create user without password                 | None                           | 1. Leave password blank<br>2. Submit   | Validation error shown                                      | High     |
| MF-USER-016 | Duplicate username                           | Existing username exists       | 1. Create user using existing username | Validation or server-side uniqueness error occurs           | High     |
| MF-USER-018 | Unauthenticated user cannot access Users page | User is not authenticated | 1. Navigate to the Users & Roles page URL without logging in | User is redirected to the login page or shown an access-denied message; Users content is not accessible | High      |

### Additional Coverage Tests

| TC ID       | Test Case                                        | Preconditions         | Steps                                                                       | Expected Result                                                | Priority |
| ----------- | ------------------------------------------------ | --------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------- | -------- |
| MF-USER-019 | Non-administrator cannot open Manage Permissions for a role | Logged in as a user without administrative privileges | 1. Navigate to the Roles page<br>2. Attempt to click Manage Permissions for a role | Action is blocked: the Manage Permissions page does not open and a visible indication shows administrative privileges are required | High     |
| MF-USER-021 | Create User form is blocked when required Offices/Staff records are missing | No Offices exist in the system | 1. Ensure no Offices (and/or required Staff records) are configured<br>2. Click Create User | Create User form does not open; a visible message indicates Offices and Staff records are required and the action is blocked | Medium   |

---

## 16. Offices

### Functional Tests

| TC ID         | Test Case                  | Preconditions                       | Steps                                                                                    | Expected Result                                             | Priority |
| ------------- | -------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-OFFICE-001 | View offices list          | User with organization permission   | 1. Navigate to Offices                                                                   | Offices hierarchy/list is displayed                         | High     |
| MF-OFFICE-002 | Create office successfully | Parent office exists if required    | 1. Click Create Office<br>2. Enter office name, parent office, opening date<br>3. Submit | Office is created successfully                              | High     |
| MF-OFFICE-003 | Edit office details        | Office exists                       | 1. Open office<br>2. Edit details<br>3. Submit                                           | Office details are updated successfully                     | High     |
| MF-OFFICE-004 | Office creation is blocked when no Head Office (hierarchy root) exists | User authenticated with organization/manage-offices permission; Head Office does not exist in the system | 1. Navigate to Offices<br>2. Click '+ Create Office' | Create action is blocked: the Create Office form does not open; a visible indicator shows the action cannot proceed because a Head Office (root of the hierarchy) must exist; Offices list remains unchanged | Medium   |
| MF-OFFICE-005 | Close office               | Office eligible for closure         | 1. Open office<br>2. Close office with closure date and reason                           | Office status changes to closed/inactive according to rules | Medium   |

### Negative Tests

| TC ID         | Test Case                                              | Preconditions                                         | Steps                                                                   | Expected Result                           | Priority |
| ------------- | ------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-OFFICE-006 | Create office without name                             | None                                                  | 1. Leave office name blank<br>2. Submit                                 | Validation error shown                    | High     |
| MF-OFFICE-007 | Create office without opening date                     | None                                                  | 1. Omit opening date<br>2. Submit                                       | Validation error shown                    | High     |
| MF-OFFICE-008 | Create office with required Parent Office field left blank is blocked | Existing office hierarchy exists                      | 1. Open Create Office form<br>2. Leave Parent Office field blank<br>3. Fill Office Name and Opened On Date with valid values<br>4. Submit | Form does not submit; an inline validation error appears on the Parent Office field indicating it is required; no new office is created | High     |
| MF-OFFICE-009 | Close office with active dependencies blocking closure | Office has active clients/users or dependent entities | 1. Attempt to close office                                              | Operation is blocked with correct error   | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                         | Preconditions                        | Steps                                            | Expected Result                                      | Priority |
| ------------- | ------------------------------------------------- | ------------------------------------ | ------------------------------------------------ | ---------------------------------------------------- | -------- |
| MF-OFFICE-010 | Transfer dependent entities before office closure | Source and destination offices exist | 1. Move required dependencies<br>2. Close office | Closure succeeds only after dependencies are handled | Medium   |
| MF-OFFICE-011 | Search/filter offices list                        | Multiple offices exist               | 1. Search for office by name                     | Matching office is returned                          | Low      |

---

## 17. Employees

### Functional Tests

| TC ID      | Test Case                           | Preconditions                     | Steps                                                                                         | Expected Result                                               | Priority |
| ---------- | ----------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-EMP-001 | View employees list                 | User with organization permission | 1. Navigate to Employees                                                                      | Employees list is displayed with office and status            | High     |
| MF-EMP-002 | Create employee successfully        | Office exists                     | 1. Click Create Employee<br>2. Enter first name, last name, office, joining date<br>3. Submit | Employee is created successfully                              | High     |
| MF-EMP-003 | Edit employee details               | Employee exists                   | 1. Open employee<br>2. Edit allowed fields<br>3. Submit                                       | Employee updates are saved                                    | High     |
| MF-EMP-004 | View employee profile               | Employee exists                   | 1. Open employee record                                                                       | Employee detail page shows linked office and personal details | Medium   |
| MF-EMP-005 | Assign employee to office correctly | Offices and employee exist        | 1. Create or edit employee with office assignment                                             | Office linkage is saved successfully                          | Medium   |

### Negative Tests

| TC ID      | Test Case                          | Preconditions | Steps                                  | Expected Result        | Priority |
| ---------- | ---------------------------------- | ------------- | -------------------------------------- | ---------------------- | -------- |
| MF-EMP-006 | Create employee without first name | None          | 1. Leave first name blank<br>2. Submit | Validation error shown | High     |
| MF-EMP-007 | Create employee without office     | None          | 1. Omit office<br>2. Submit            | Validation error shown | High     |

---

## 18. Reports

### Functional Tests

| TC ID         | Test Case                                                      | Preconditions                    | Steps                                                    | Expected Result                                               | Priority |
| ------------- | -------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-REPORT-001 | View reports list                                              | User with reporting permission   | 1. Navigate to Reports                                   | Reports page displays available report definitions/categories | High     |
| MF-REPORT-002 | Run report with valid parameters                               | Parameterized report exists      | 1. Open report<br>2. Enter required parameters<br>3. Run | Report output is generated successfully                       | High     |
| MF-REPORT-003 | Run report without parameters when not required                | Non-parameterized report exists  | 1. Open report<br>2. Run report                          | Report output is generated                                    | Medium   |
| MF-REPORT-004 | Export report where supported                                  | Generated report exists          | 1. Run report<br>2. Export to available format           | Export file is generated successfully                         | Medium   |
| MF-REPORT-005 | View report data with large result set pagination or scrolling | Report with large dataset exists | 1. Run report                                            | Results remain readable and usable                            | Medium   |

### Negative Tests

| TC ID         | Test Case                                             | Preconditions                | Steps                                                         | Expected Result                                | Priority |
| ------------- | ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------- | ---------------------------------------------- | -------- |
| MF-REPORT-006 | Run parameterized report without mandatory parameters | Parameterized report exists  | 1. Open report<br>2. Leave required parameter blank<br>3. Run | Validation error shown                         | High     |
| MF-REPORT-007 | Run report with invalid date range                    | Date-parameter report exists | 1. Provide invalid date range<br>2. Run                       | Validation or backend error handled gracefully | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                            | Preconditions                        | Steps                                | Expected Result                                            | Priority |
| ------------- | -------------------------------------------------------------------- | ------------------------------------ | ------------------------------------ | ---------------------------------------------------------- | -------- |
| MF-REPORT-009 | Unauthenticated user cannot access the Reports page | User is not authenticated | 1. Navigate to the Reports page URL or click Reports in top navigation | Access is blocked; the user is redirected to the login screen; the Reports page is not displayed | Low      |
| MF-REPORT-010 | Export actions are unavailable before a report has been run | No report has been run in the current session | 1. Open a report's Parameters form<br>2. Do not click Run Report<br>3. Attempt to locate or click Export to Excel or other export buttons | Export actions are not visible or are disabled when no output table exists; no file download is initiated | Low      |
| MF-REPORT-011 | Run Report when system contains no relevant data shows an empty-result indicator | System contains no relevant transactional/master data for the selected parameters | 1. Open a report's Parameters form and fill valid values<br>2. Click Run Report | Report generation produces no rows; a visible message informs the user no data is available for the selected parameters | High     |

---

## 19. Organization Settings

### Functional Tests

| TC ID      | Test Case                          | Preconditions                    | Steps                                                                                 | Expected Result                              | Priority |
| ---------- | ---------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------- | -------- |
| MF-ORG-001 | View organization settings modules | User with admin permission       | 1. Navigate to Organization settings area                                             | Available configuration pages are displayed  | High     |
| MF-ORG-002 | Configure working days             | Organization settings accessible | 1. Open Working Days<br>2. Set business days and repayment reschedule rule<br>3. Save | Working day settings are saved successfully  | High     |
| MF-ORG-003 | Configure holidays                 | Organization settings accessible | 1. Open Holidays<br>2. Create holiday with office/date details<br>3. Save             | Holiday is created and visible in list       | High     |
| MF-ORG-004 | Configure currency settings        | Settings accessible              | 1. Open currency/configuration module<br>2. Update allowed settings<br>3. Save        | Currency-related settings are saved          | Medium   |
| MF-ORG-005 | Bulk Import - Download template for Clients | User logged in as Administrator, Organization context configured | 1. Navigate to Admin > Organization Settings and open the Bulk Import page<br>2. Under Clients, click the 'Download template' button | A file download is triggered in the browser for the Clients import template | Medium   |
| MF-ORG-006 | Manage payment types               | Payment types accessible         | 1. Open payment types<br>2. Create or edit payment type<br>3. Save                    | Payment type changes are saved               | Medium   |
| MF-ORG-007 | Configure fund definitions         | Fund configuration accessible    | 1. Open funds<br>2. Create/edit fund<br>3. Save                                       | Fund definition is saved                     | Medium   |
| MF-ORG-008 | Bulk Import - Upload Clients file and start import | User logged in as Administrator, Organization context configured, a valid Clients import file is available | 1. Navigate to Admin > Organization Settings and open the Bulk Import page<br>2. Under Clients, click the Upload/File control<br>3. Select valid Clients import file in the file chooser<br>4. Click the button to start the upload/import | A success notification is displayed confirming the Clients file was uploaded and the import has started | Medium   |

### Negative Tests

| TC ID      | Test Case                                         | Preconditions              | Steps                                              | Expected Result                           | Priority |
| ---------- | ------------------------------------------------- | -------------------------- | -------------------------------------------------- | ----------------------------------------- | -------- |
| MF-ORG-010 | Create holiday with invalid date range            | Settings accessible        | 1. Enter invalid holiday period<br>2. Save         | Validation error shown                    | High     |
| MF-ORG-011 | Unauthenticated user cannot access Organization Settings | User is not authenticated | 1. Open the application in a browser<br>2. Navigate to the Admin > Organization Settings URL directly | Access is blocked; user is redirected to the login page or shown a login prompt; Organization Settings content is not visible | High     |
| MF-ORG-012 | Bulk Import (Clients) - attempt Upload without selecting a file | Administrator logged in with existing organization context | 1. Navigate to Admin > Organization Settings > Bulk Import<br>2. In the Clients group, click the Upload control without choosing a file<br>3. Click the action that starts the upload/import | Upload is blocked; import does not start; Clients Upload/File field displays an inline validation error indicating a file must be selected | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                  | Preconditions                                          | Steps                                                    | Expected Result                                                               | Priority |
| ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-ORG-014 | Create Fund button blocked when organization context is not configured | Administrator logged in without an existing organization context configured | 1. Navigate to Admin > Organization Settings > Funds<br>2. Observe the top actions area where 'Create Fund' would appear<br>3. Attempt to click 'Create Fund' if visible | Create Fund action is not available; the button is either not visible or disabled and cannot be opened; no fund can be created | High     |
| MF-ORG-015 | Non-administrative user does not see Admin menu / Organization Settings link | Authenticated non-administrative user | 1. Login as a non-administrative user<br>2. Observe the top navigation | Admin menu is not present in the top navigation; the 'Organization Settings' link is not visible to the user | High     |
| MF-ORG-016 | Create Holiday - submit with all required fields empty | Administrator logged in with existing organization context | 1. Navigate to Admin > Organization Settings > Holidays<br>2. Click the '+ Create Holiday' button<br>3. Leave the Name field blank<br>4. Leave the From Date field blank<br>5. Leave the To Date field blank<br>6. Click Save | Form does not submit; holiday is not created; inline validation errors appear on the Name, From Date, and To Date fields indicating they are required | High     |
| MF-ORG-017 | Create Holiday - very long Name input is rejected at boundary | Administrator logged in with existing organization context, Holidays page is visible | 1. Click the '+ Create Holiday' button<br>2. In the Name field enter a very long string (>200 characters)<br>3. Enter a valid From Date<br>4. Enter a valid To Date (on or after the From Date)<br>5. Click Save | Save is blocked; the Name field shows an inline validation error indicating the value exceeds the maximum allowed length | Medium   |

---

## 20. Share Products

### Functional Tests

| TC ID         | Test Case                                    | Preconditions            | Steps                                                                                                                                                                                             | Expected Result                                             | Priority |
| ------------- | -------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------- |
| MF-SHPROD-001 | View share products list                     | Share module enabled     | 1. Navigate to Share Products                                                                                                                                                                     | Share products list displays configured products            | High     |
| MF-SHPROD-002 | Create share product successfully            | Required setup exists    | 1. Click Create Share Product<br>2. Fill mandatory fields including product name, short name, currency, total shares, nominal price, market price, accounting mappings if applicable<br>3. Submit | Share product is created successfully                       | High     |
| MF-SHPROD-003 | View share product detail                    | Share product exists     | 1. Open product                                                                                                                                                                                   | Product detail displays pricing, share limits, and settings | High     |
| MF-SHPROD-004 | Edit share product                           | Share product exists     | 1. Open product<br>2. Edit allowed fields<br>3. Submit                                                                                                                                            | Product changes are saved successfully                      | High     |
| MF-SHPROD-005 | Configure dividend settings on share product | Dividend feature enabled | 1. Create or edit product with dividend settings                                                                                                                                                  | Product retains dividend configuration                      | Medium   |
| MF-SHPROD-006 | Unauthenticated user cannot open the Create Share Product wizard | User is not authenticated | 1. Navigate to the Share Products listing page URL without being logged in<br>2. Click '+ Create Share Product' | User is redirected to the Login page; the Create Share Product wizard is not opened | Medium   |

### Negative Tests

| TC ID         | Test Case                                                      | Preconditions          | Steps                                                                             | Expected Result                | Priority |
| ------------- | -------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------- | ------------------------------ | -------- |
| MF-SHPROD-007 | Create share product without mandatory name                    | None                   | 1. Leave product name empty<br>2. Submit                                          | Validation error shown         | High     |
| MF-SHPROD-008 | Create button hidden for user without product-management privileges | Authenticated user without product-management privileges | 1. Login as a user account without product-management privileges<br>2. Navigate to the Share Products listing page | The '+ Create Share Product' button is not visible; Edit/Delete row actions are not available to this user role | High     |
| MF-SHPROD-009 | Missing accounting mappings when accounting rule requires them | GL accounts incomplete | 1. Configure accounting-requiring product without mandatory mappings<br>2. Submit | Validation blocks save         | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                                                     | Preconditions         | Steps                                                           | Expected Result                                            | Priority |
| ------------- | ----------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| MF-SHPROD-010 | Inactivate share product for future use                                       | Product exists        | 1. Disable/inactivate product                                   | Product is unavailable for new share accounts              | Medium   |
| MF-SHPROD-011 | Unauthenticated user cannot access Edit on an existing share product | User is not authenticated; an existing share product exists | 1. Navigate directly to an existing Share Product detail page URL while not logged in<br>2. Attempt to click the Edit action | User is redirected to the Login page; the edit action is blocked | Low      |
| MF-SHPROD-012 | Direct navigation to Step 7 without completing Step 1 is blocked | Authenticated user on Share Products listing page | 1. Click + Create Share Product<br>2. Click the Step 7 tab/header directly without entering data in Step 1 | Navigation to Step 7 is prevented; the stepper shows a validation indicator and Step 1 remains active | Medium   |

---

## 21. Floating Rates

### Functional Tests

| TC ID        | Test Case                         | Preconditions                              | Steps                                                                                | Expected Result                                            | Priority |
| ------------ | --------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------- | -------- |
| MF-FRATE-001 | View floating rates list          | Floating rate feature enabled              | 1. Navigate to Floating Rates                                                        | Existing floating rates and periods are displayed          | High     |
| MF-FRATE-002 | Create floating rate successfully | Feature enabled                            | 1. Click Create Floating Rate<br>2. Enter name and required details<br>3. Submit     | Floating rate is created successfully                      | High     |
| MF-FRATE-003 | Add floating rate period          | Floating rate exists                       | 1. Open floating rate<br>2. Add new period with effective date and rate<br>3. Submit | New floating rate period is saved                          | High     |
| MF-FRATE-004 | View floating rate history        | Floating rate with multiple periods exists | 1. Open floating rate details                                                        | Historical effective periods and rates are shown correctly | Medium   |
| MF-FRATE-005 | Edit floating rate metadata       | Floating rate exists                       | 1. Open floating rate<br>2. Edit metadata<br>3. Submit                               | Changes are saved successfully                             | Medium   |

### Negative Tests

| TC ID        | Test Case                                             | Preconditions        | Steps                                                            | Expected Result                           | Priority |
| ------------ | ----------------------------------------------------- | -------------------- | ---------------------------------------------------------------- | ----------------------------------------- | -------- |
| MF-FRATE-006 | Create floating rate without mandatory name           | None                 | 1. Leave required name field empty<br>2. Submit                  | Validation error shown                    | High     |
| MF-FRATE-007 | Add rate period with overlapping effective date range | Floating rate exists | 1. Add period overlapping existing effective period<br>2. Submit | Validation or business rule prevents save | High     |
| MF-FRATE-008 | Add rate period with invalid rate value               | Floating rate exists | 1. Enter invalid or out-of-range rate<br>2. Submit               | Validation error shown                    | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                                                                 | Preconditions                         | Steps                                                             | Expected Result                                                  | Priority |
| ------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- | -------- |
| MF-FRATE-009 | Loan product linked to floating rate uses latest applicable period                                        | Linked loan product exists            | 1. Configure product with floating rate<br>2. Create/inspect loan | Linked rate is resolved according to effective date rules        | High     |
| MF-FRATE-010 | Future-dated floating rate period does not affect current calculations before effective date              | Floating rate has future-dated period | 1. Add future period<br>2. Inspect current-linked calculations    | Current calculations remain unchanged until effective date       | High     |
| MF-FRATE-011 | Floating rate history remains immutable for already effective periods where business rules restrict edits | Existing period history exists        | 1. Attempt restricted update to historical period                 | System blocks invalid modification or handles according to rules | Medium   |

---

## 22. Delinquency Management

### Functional Tests

| TC ID         | Test Case                                                                   | Preconditions               | Steps                                                                                  | Expected Result                                       | Priority |
| ------------- | --------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------- |
| MF-DELINQ-001 | View delinquency buckets or ranges                                          | Delinquency feature enabled | 1. Navigate to Delinquency configuration                                               | Delinquency ranges/buckets are displayed              | High     |
| MF-DELINQ-002 | Create delinquency bucket successfully                                      | Feature enabled             | 1. Click Create Delinquency Bucket<br>2. Enter name and age/range details<br>3. Submit | Delinquency bucket is created successfully            | High     |
| MF-DELINQ-003 | Create a delinquency range independently of a bucket, specifying Minimum and Maximum Age Days | Feature enabled; user has configuration/admin privileges | 1. Navigate to Delinquency Ranges<br>2. Click Create Delinquency Range<br>3. Enter Classification, Minimum Age Days, and Maximum Age Days<br>4. Submit | A new row appears in the Delinquency Ranges table showing the entered Classification with the specified Minimum and Maximum Age Days | Medium   |
| MF-DELINQ-004 | View delinquent loans grouped by bucket                                     | Delinquent loans exist      | 1. Open delinquency view/report                                                        | Loans are categorized into correct delinquency ranges | High     |
| MF-DELINQ-005 | Delinquency bucket creation is blocked when no Loan Products exist to link to | User authenticated with configuration/admin privileges; no Loan Products exist in the system | 1. Navigate to Delinquency Buckets<br>2. Open Create Delinquency Bucket form<br>3. Fill Bucket Name and add at least one Bucket Range with valid values<br>4. Submit | Form submission is blocked; a visible error indicates creation is not allowed because no Loan Products are available to link the bucket to; no bucket is created | Medium   |

### Negative Tests

| TC ID         | Test Case                                               | Preconditions                         | Steps                                        | Expected Result                               | Priority |
| ------------- | ------------------------------------------------------- | ------------------------------------- | -------------------------------------------- | --------------------------------------------- | -------- |
| MF-DELINQ-006 | Create bucket with overlapping ranges                   | Existing bucket ranges exist          | 1. Create new overlapping range<br>2. Submit | Validation prevents overlapping configuration | High     |
| MF-DELINQ-007 | Create bucket with invalid min/max range                | None                                  | 1. Enter invalid boundaries<br>2. Submit     | Validation error shown                        | High     |
| MF-DELINQ-008 | Delinquency Bucket creation is blocked for users lacking configuration/admin privileges | User authenticated but does NOT have configuration/admin privileges; loan products exist | 1. Log in as a user without configuration/admin privileges<br>2. Navigate to Delinquency Buckets<br>3. Open Create Delinquency Bucket form<br>4. Fill all required fields with valid values<br>5. Submit | Creation is blocked; a visible authorization error indicates the user lacks sufficient privileges to create delinquency buckets; no bucket is created | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                                        | Preconditions                  | Steps                                                                         | Expected Result                                                                          | Priority |
| ------------- | -------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------- |
| MF-DELINQ-009 | Create delinquency range with boundary configurations: open-ended Maximum Age Days and single-day range where Maximum equals Minimum | User authenticated with configuration/admin privileges; Create Delinquency Range form accessible | 1. Create a range entering Classification and Minimum Age Days, leaving Maximum Age Days blank; submit<br>2. Create a second range entering Classification and the same numeric value for both Minimum and Maximum Age Days; submit | Both creations succeed; the first range's Maximum Age Days cell is shown empty/open-ended; the second range's Minimum and Maximum Age Days both display the same value (single-day range) | High     |
| MF-DELINQ-010 | Create delinquency range and bucket with very long text and special characters/emoji in name fields | User authenticated with configuration/admin privileges | 1. Open Create Delinquency Range form and enter a 200+ character string in Classification, a numeric Minimum Age Days, submit<br>2. Open Create Delinquency Bucket form and enter a Bucket Name containing special characters and emoji, add one Bucket Range, submit | Both creations succeed; the long Classification and Bucket Name strings display in full without truncation, and the special characters/emoji entered in Classification and Range Label appear verbatim in the Ranges and Bucket detail views | High     |

---

## 23. Share Account

### Functional Tests

| TC ID        | Test Case                               | Preconditions                                        | Steps                                                                                                 | Expected Result                                        | Priority |
| ------------ | --------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------- |
| MF-SHARE-001 | Create share account for client         | Active client and share product exist                | 1. Open client profile<br>2. Create new share account<br>3. Select product and submit required values | Share account is created successfully                  | High     |
| MF-SHARE-002 | Approve share account application       | Pending share account exists                         | 1. Open share account<br>2. Approve application                                                       | Share account moves to approved state                  | High     |
| MF-SHARE-003 | Activate share account                  | Approved share account exists                        | 1. Open account<br>2. Activate                                                                        | Share account becomes active                           | High     |
| MF-SHARE-004 | Purchase shares                         | Active share account exists                          | 1. Open share account<br>2. Purchase shares with quantity/date<br>3. Submit                           | Purchase transaction is posted and holdings increase   | High     |
| MF-SHARE-005 | Redeem shares                           | Active share account with sufficient holdings exists | 1. Open share account<br>2. Redeem shares<br>3. Submit                                                | Redemption transaction is posted and holdings decrease | High     |
| MF-SHARE-006 | View share transactions                 | Share account with activity exists                   | 1. Open transactions section                                                                          | Purchase/redemption/dividend history is displayed      | Medium   |
| MF-SHARE-007 | Post dividend to eligible share account | Dividend-capable share product/account exists        | 1. Trigger or post dividend action                                                                    | Dividend transaction is recorded correctly             | Medium   |
| MF-SHARE-008 | Close share account                     | Eligible account exists                              | 1. Open account<br>2. Close with required details                                                     | Share account status changes to closed                 | Medium   |

### Negative Tests

| TC ID        | Test Case                                      | Preconditions                 | Steps                                       | Expected Result                                | Priority |
| ------------ | ---------------------------------------------- | ----------------------------- | ------------------------------------------- | ---------------------------------------------- | -------- |
| MF-SHARE-009 | Purchase shares below minimum allowed quantity | Active share account exists   | 1. Attempt purchase below minimum threshold | Validation or business rule blocks transaction | High     |
| MF-SHARE-010 | Redeem blocked when client has no linked savings account for crediting redemption | Active share account exists; client has no active savings accounts linked for charges/crediting | 1. Open share account<br>2. Click Redeem Shares action<br>3. Enter valid number of Shares to Redeem<br>4. Click Redeem/Submit button | Dialog does not submit; a visible error/notice indicates there is no linked savings account to credit redemption (or Redeem button is disabled); no redemption is processed and holdings remain unchanged | High     |
| MF-SHARE-011 | Purchase or redeem on non-active share account | Account not active            | 1. Attempt transaction                      | Action is blocked                              | High     |
| MF-SHARE-012 | Undo Approval on an Approved share account reverts it to Pending | Approved share account exists | 1. Open share account<br>2. Click Undo Approval action<br>3. Confirm on the Undo Approval dialog | Share Account Detail page displays status badge 'Pending'; Approved-state fields such as Approved Date are no longer shown as current | Medium   |

### Additional Coverage Tests

| TC ID        | Test Case                                                                 | Preconditions                | Steps                                             | Expected Result                                              | Priority |
| ------------ | ------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------- | ------------------------------------------------------------ | -------- |
| MF-SHARE-013 | Reject share account application                                          | Pending share account exists | 1. Open account<br>2. Reject                      | Account status changes to Rejected                           | Medium   |
| MF-SHARE-014 | Share balance and nominal/market value display updates after transactions | Share account exists         | 1. Purchase or redeem shares<br>2. Reopen summary | Summary values reflect updated holdings and valuation inputs | Medium   |
| MF-SHARE-015 | Dividend posting respects eligible holdings and effective rules           | Dividend run configured      | 1. Post dividend                                  | Dividend amount aligns with eligible share holdings/rules    | Medium   |

---

## 24. Fixed & Recurring Deposit Accounts

### Functional Tests

| TC ID      | Test Case                                              | Preconditions                                      | Steps                                                                                                  | Expected Result                                                             | Priority |
| ---------- | ------------------------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | -------- |
| MF-DEP-001 | Fixed deposit account creation blocked when no deposit products or interest rate charts are configured | Active client selected on the Client Detail page; no relevant Fixed Deposit products or interest rate charts configured in the system | 1. Navigate to the Client Detail page for the selected client<br>2. Click Create Fixed Deposit (or the Create action) to initiate account creation | Create Fixed Deposit form does not open (or Create button is disabled); a visible message indicates product/interest rate chart configuration is required; no account is created | High     |
| MF-DEP-002 | Create recurring deposit product successfully          | Required setup exists                              | 1. Create recurring deposit product with mandatory details<br>2. Submit                                | Recurring deposit product is created successfully                           | High     |
| MF-DEP-003 | Open fixed deposit account for client                  | Active client and fixed deposit product exist      | 1. Open client profile<br>2. Create fixed deposit account<br>3. Fill required values<br>4. Submit      | Fixed deposit account is created successfully                               | High     |
| MF-DEP-004 | Open recurring deposit account for client              | Active client and recurring deposit product exist  | 1. Create recurring deposit account from client profile                                                | Recurring deposit account is created successfully                           | High     |
| MF-DEP-005 | Approve deposit account                                | Pending deposit account exists                     | 1. Open deposit account<br>2. Approve                                                                  | Account moves to approved state                                             | High     |
| MF-DEP-006 | Activate deposit account                               | Approved deposit account exists                    | 1. Open account<br>2. Activate with required date                                                      | Account becomes active                                                      | High     |
| MF-DEP-007 | Premature close fixed deposit account                  | Eligible fixed deposit account exists              | 1. Open account<br>2. Initiate premature closure<br>3. Submit                                          | Account closes with premature closure handling applied                      | Medium   |
| MF-DEP-008 | Mature and close fixed deposit account                 | Matured fixed deposit account exists               | 1. Open matured account<br>2. Close on maturity                                                        | Maturity proceeds are handled correctly and account closes                  | High     |
| MF-DEP-009 | Post installment to recurring deposit account          | Active RD account exists                           | 1. Open RD account<br>2. Post deposit installment                                                      | Installment transaction is recorded correctly                               | High     |
| MF-DEP-010 | View deposit account transactions and maturity details | Deposit account exists                             | 1. Open account                                                                                        | Transactions, interest accruals, and maturity information display correctly | Medium   |

### Negative Tests

| TC ID      | Test Case                                              | Preconditions                | Steps                                                     | Expected Result                | Priority |
| ---------- | ------------------------------------------------------ | ---------------------------- | --------------------------------------------------------- | ------------------------------ | -------- |
| MF-DEP-011 | Create deposit product without mandatory name          | None                         | 1. Leave name empty<br>2. Submit                          | Validation error shown         | High     |
| MF-DEP-012 | Create fixed deposit account with non-numeric deposit period value | Active client selected on the Client Detail page; relevant Fixed Deposit product and interest rate chart configured | 1. Navigate to the Client Detail page for the selected client<br>2. Click Create Fixed Deposit to open the Fixed Deposit creation form<br>3. Enter a non-numeric value into the Deposit Period Value field<br>4. Click Create Fixed Deposit | Form does not submit; Fixed Deposit account is not created; Deposit Period Value field displays an inline validation error indicating the value must be numeric | Medium   |
| MF-DEP-013 | Open deposit account without product                   | Active client exists         | 1. Start account creation<br>2. Omit product<br>3. Submit | Validation error shown         | High     |
| MF-DEP-014 | Activate action not available when Fixed Deposit account is in Pending status | Fixed Deposit account exists in Pending status on its Detail page | 1. Open the Fixed Deposit Detail page for the account in Pending status<br>2. Attempt to click Activate in the action bar | Activate button is not visible or is disabled; clicking it is not possible; account status remains Pending and no state transition occurs | High     |
| MF-DEP-015 | Deposit action not available on Recurring Deposit account in Pending status | Recurring Deposit account exists in Pending status on its Detail page | 1. Open the Recurring Deposit Detail page for the account in Pending status<br>2. Attempt to click Deposit in the action bar | Deposit button is not visible or is disabled; clicking it is not possible; account status remains Pending and no deposit is recorded | High     |
| MF-DEP-016 | Premature Close action not available when Fixed Deposit account is already Closed | Fixed Deposit account exists in Closed (matured) status on its Detail page | 1. Open the Fixed Deposit Detail page for the account in Closed (matured) status<br>2. Observe the action bar | No action buttons (Approve, Activate, Premature Close, Close on Maturity) are visible in the action bar; Premature Close cannot be invoked and account status remains Closed | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                              | Preconditions                            | Steps                                   | Expected Result                                                           | Priority |
| ---------- | ---------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------- | -------- |
| MF-DEP-017 | Reject deposit account application                                     | Pending deposit account exists           | 1. Open account<br>2. Reject            | Account status changes to Rejected                                        | Medium   |
| MF-DEP-018 | Interest posting or accrual updates deposit account balances correctly | Active deposit account exists            | 1. Trigger interest accrual/posting     | Balances and maturity details update correctly                            | High     |
| MF-DEP-019 | Maturity instructions transfer proceeds according to configured option | Matured account with instructions exists | 1. Process maturity                     | Proceeds are paid out, transferred, or renewed according to configuration | High     |
| MF-DEP-020 | Recurring deposit missed installment behavior follows product rules    | Active RD with missed schedule exists    | 1. Skip installment and inspect account | Penalties or status outcomes follow configured rules                      | Medium   |

---

## 25. Accounting - Closures

### Functional Tests

| TC ID        | Test Case                              | Preconditions                              | Steps                                                                     | Expected Result                                | Priority |
| ------------ | -------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------- | -------- |
| MF-CLOSE-001 | View accounting closures list          | Accounting admin logged in                 | 1. Navigate to Accounting Closures                                        | Existing closures are displayed by office/date | High     |
| MF-CLOSE-002 | Create accounting closure successfully | No conflicting closure for same scope/date | 1. Click Create Closure<br>2. Select office and closing date<br>3. Submit | Closure is created successfully                | High     |
| MF-CLOSE-003 | View closure details                   | Closure exists                             | 1. Open closure                                                           | Closure details display office/date metadata   | Medium   |

### Negative Tests

| TC ID        | Test Case                                                 | Preconditions                      | Steps                                                        | Expected Result                                  | Priority |
| ------------ | --------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------ | -------- |
| MF-CLOSE-004 | Create duplicate closure for same office/date constraints | Closure exists                     | 1. Attempt duplicate closure                                 | Validation or business rule prevents duplicate   | High     |
| MF-CLOSE-005 | Create closure without required office/date               | None                               | 1. Omit mandatory fields<br>2. Submit                        | Validation error shown                           | High     |
| MF-CLOSE-006 | Backdated transaction after closure is blocked            | Closure exists for relevant period | 1. Attempt transaction/manual journal entry in closed period | System blocks posting according to closure rules | High     |

### Additional Coverage Tests

| TC ID        | Test Case                                                              | Preconditions                             | Steps                                          | Expected Result                                  | Priority |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------- | ------------------------------------------------ | -------- |
| MF-CLOSE-007 | Closure impacts all relevant accounting transactions for scoped office | Closure exists and transactions attempted | 1. Try various posting workflows after closure | Restricted transactions are blocked consistently | High     |
| MF-CLOSE-008 | Closure list can be filtered or sorted where supported                 | Multiple closures exist                   | 1. Use available list controls                 | Expected closures are shown                      | Low      |

---

## 26. Accounting Rules & Financial Activity Mappings

### Functional Tests

| TC ID      | Test Case                                         | Preconditions                       | Steps                                                                 | Expected Result                          | Priority |
| ---------- | ------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------- | ---------------------------------------- | -------- |
| MF-FAM-001 | View financial activity mappings                  | Accounting configuration accessible | 1. Navigate to Financial Activity Mappings                            | Existing mappings are displayed          | High     |
| MF-FAM-002 | Create or update financial activity to GL mapping | GL accounts exist                   | 1. Open financial activity<br>2. Assign GL account mapping<br>3. Save | Mapping is saved successfully            | High     |
| MF-FAM-003 | View accounting rules configuration               | Accounting settings accessible      | 1. Navigate to accounting rules/settings                              | Configured rules are displayed correctly | Medium   |
| MF-FAM-004 | Edit accounting rule setting                      | Editable accounting setting exists  | 1. Update rule value<br>2. Save                                       | Rule change is persisted                 | Medium   |

### Negative Tests

| TC ID      | Test Case                                                    | Preconditions               | Steps                                      | Expected Result                         | Priority |
| ---------- | ------------------------------------------------------------ | --------------------------- | ------------------------------------------ | --------------------------------------- | -------- |
| MF-FAM-005 | Save mapping without required GL account                     | Financial activity selected | 1. Leave required account empty<br>2. Save | Validation error shown                  | High     |
| MF-FAM-006 | Map financial activity to invalid or incompatible GL account | GL account incompatible     | 1. Select invalid account type<br>2. Save  | Validation or business rule blocks save | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                          | Preconditions                           | Steps                                        | Expected Result                                                         | Priority |
| ---------- | ---------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- | -------- |
| MF-FAM-008 | Product/account posting uses configured financial activity mapping                 | Mapping exists and relevant txn occurs  | 1. Perform linked transaction                | Journal entries use configured mapped GL account                        | High     |
| MF-FAM-009 | Updating mapping affects future transactions without corrupting historical entries | Existing transactions and mapping exist | 1. Change mapping<br>2. Post new transaction | Historical entries remain unchanged and new entries use updated mapping | High     |
| MF-FAM-010 | Accounting rules visible state matches enabled features                            | Different features enabled/disabled     | 1. Review accounting settings                | Only relevant rules are displayed and editable                          | Low      |

---

## 27. Provisioning

### Functional Tests

| TC ID       | Test Case                     | Preconditions                     | Steps                                                                 | Expected Result                                        | Priority |
| ----------- | ----------------------------- | --------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ | -------- |
| MF-PROV-001 | View provisioning criteria    | Provisioning feature enabled      | 1. Navigate to Provisioning                                           | Provisioning criteria and history are displayed        | High     |
| MF-PROV-002 | Create provisioning criteria  | Feature enabled                   | 1. Create criteria with delinquency ranges and percentages<br>2. Save | Criteria are saved successfully                        | High     |
| MF-PROV-003 | Generate provisioning entries | Criteria and eligible loans exist | 1. Run provisioning process                                           | Provisioning entries/report are generated successfully | High     |
| MF-PROV-004 | View provisioning history     | Provisioning runs exist           | 1. Open provisioning history                                          | Past generated entries are displayed                   | Medium   |

### Negative Tests

| TC ID       | Test Case                                                        | Preconditions            | Steps                                        | Expected Result                       | Priority |
| ----------- | ---------------------------------------------------------------- | ------------------------ | -------------------------------------------- | ------------------------------------- | -------- |
| MF-PROV-005 | Non-privileged user cannot submit Provisioning Criteria | Logged in as a user without accounting/administrative privileges | 1. Open the Provisioning Criteria form<br>2. Fill Criteria Name and at least one Definitions row with valid values<br>3. Click Create | Create action is blocked; a visible permission/access error is shown and the form remains open; the criteria is not saved | High     |
| MF-PROV-006 | Create criteria with invalid percentage                          | None                     | 1. Enter invalid percentage value<br>2. Save | Validation error shown                | High     |
| MF-PROV-007 | Submitting Provisioning Criteria with zero Definitions rows is blocked | Provisioning Criteria creation form can be opened | 1. Enter a valid Criteria Name<br>2. Add then remove a Definitions row so zero rows remain<br>3. Click Create | Form submission is blocked; a visible inline error indicates at least one Definitions row is required; no new criteria appears in the listing | Medium   |

### Additional Coverage Tests

| TC ID       | Test Case                                                                  | Preconditions                  | Steps                                                                        | Expected Result                                  | Priority |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ | -------- |
| MF-PROV-008 | Unauthenticated user cannot create a Provisioning Entry | Not logged in (no authenticated session) | 1. Navigate to the Provisioning Entries page<br>2. Click the + Create Provisioning Entry button | Action is blocked; user is redirected to login or shown an authentication prompt; no provisioning entries are generated | High     |
| MF-PROV-009 | Generated provisioning creates expected accounting impact where configured | Accounting integration enabled | 1. Run provisioning                                                          | Related accounting entries are created correctly | High     |

---

## 28. Teller & Cashier Management

### Functional Tests

| TC ID         | Test Case                  | Preconditions                                  | Steps                                                                                                       | Expected Result                                                   | Priority |
| ------------- | -------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------- |
| MF-TELLER-001 | View tellers list          | Teller feature enabled and user has permission | 1. Navigate to Tellers                                                                                      | Teller list is displayed with office and status details           | High     |
| MF-TELLER-002 | Create teller successfully | Office and required setup exist                | 1. Click Create Teller<br>2. Enter teller details including office and cash limits if required<br>3. Submit | Teller is created successfully                                    | High     |
| MF-TELLER-003 | View cashier assignments   | Tellers and users exist                        | 1. Navigate to Cashiers or teller detail page                                                               | Cashier assignments are displayed correctly                       | High     |
| MF-TELLER-004 | Assign cashier to teller   | Teller and eligible user exist                 | 1. Open teller<br>2. Assign cashier/user with start and end time if required<br>3. Submit                   | Cashier assignment is saved successfully                          | High     |
| MF-TELLER-005 | Allocate cash to cashier   | Active teller and cashier assignment exist     | 1. Open cashier allocation workflow<br>2. Enter amount<br>3. Submit                                         | Cash allocation transaction is recorded successfully              | High     |
| MF-TELLER-006 | Settle cashier balance     | Active cashier with transactions exists        | 1. Open settle or close cashier workflow<br>2. Submit settlement                                            | Cashier is settled and balances are reconciled according to rules | High     |
| MF-TELLER-007 | View cashier transactions  | Cashier transaction history exists             | 1. Open cashier transactions/history                                                                        | Allocation, settlement, and cash transactions are displayed       | Medium   |
| MF-TELLER-008 | Close or deactivate teller | Teller eligible for closure                    | 1. Open teller<br>2. Deactivate or close                                                                    | Teller status is updated successfully                             | Medium   |

### Negative Tests

| TC ID         | Test Case                                        | Preconditions              | Steps                                                                                    | Expected Result                                         | Priority |
| ------------- | ------------------------------------------------ | -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------- |
| MF-TELLER-009 | Create teller without mandatory office           | None                       | 1. Omit office while creating teller<br>2. Submit                                        | Validation error shown                                  | High     |
| MF-TELLER-010 | Assign cashier with invalid overlapping schedule | Existing assignment exists | 1. Create overlapping cashier assignment for same user/teller if restricted<br>2. Submit | Validation or business rule prevents overlap            | High     |
| MF-TELLER-011 | Allocate Cash rejected when Transaction Date is invalid | Active cashier exists      | 1. Open Allocate Cash dialog<br>2. Enter invalid/impossible Transaction Date<br>3. Submit | Inline validation error shown on Transaction Date field; no allocation transaction is recorded | High     |
| MF-TELLER-012 | Settle cashier with inconsistent cash balance    | Cashier imbalance exists   | 1. Attempt settlement without resolving discrepancy if required                          | Process is blocked or discrepancy is surfaced correctly | High     |

### Additional Coverage Tests

| TC ID         | Test Case                                                                  | Preconditions                   | Steps                                                     | Expected Result                                                        | Priority |
| ------------- | -------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------- | -------- |
| MF-TELLER-014 | Cash allocation impacts cashier available balance immediately              | Active cashier exists           | 1. Allocate cash<br>2. Refresh cashier detail             | Available cash/balance reflects allocation                             | High     |
| MF-TELLER-015 | Settlement closes cashier session for further transactions where required  | Cashier settled                 | 1. Settle cashier<br>2. Attempt additional cashier action | Further cashier activity is blocked or requires new assignment/session | Medium   |
| MF-TELLER-016 | Teller and cashier list filters work                                       | Multiple tellers/cashiers exist | 1. Search/filter by office or status                      | Matching records are displayed                                         | Low      |
| MF-TELLER-017 | Cashier transaction audit trail shows maker/checker metadata where enabled | Maker-checker enabled           | 1. Perform teller workflow                                | Audit details are recorded correctly                                   | Medium   |

---

## 29. Account Transfers & Standing Instructions

### Functional Tests

| TC ID      | Test Case                                                       | Preconditions                                           | Steps                                                                                                                                       | Expected Result                                                   | Priority |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------- |
| MF-TRF-001 | Transfer funds between eligible own accounts                    | Client has eligible source and destination accounts     | 1. Open transfer workflow<br>2. Select source and destination accounts<br>3. Enter amount/date<br>4. Submit                                 | Transfer is completed and reflected in both accounts              | High     |
| MF-TRF-002 | Transfer from savings to loan repayment                         | Active savings and loan accounts exist                  | 1. Select savings as source and loan as destination<br>2. Submit transfer                                                                   | Savings is debited and loan repayment transaction is posted       | High     |
| MF-TRF-003 | Transfer between client accounts across supported account types | Eligible account types exist                            | 1. Perform supported transfer                                                                                                               | Transfer succeeds according to supported combinations             | Medium   |
| MF-TRF-004 | Create standing instruction successfully                        | Eligible source/destination accounts exist              | 1. Navigate to Standing Instructions<br>2. Create instruction with frequency, amount/rule, start date, source, and destination<br>3. Submit | Standing instruction is created successfully                      | High     |
| MF-TRF-005 | Execute due standing instruction                                | Active standing instruction exists and due date reached | 1. Trigger scheduled execution or inspect executed run                                                                                      | Transfer posts successfully according to standing instruction     | High     |
| MF-TRF-006 | View standing instructions list                                 | Standing instructions exist                             | 1. Navigate to Standing Instructions                                                                                                        | Standing instruction list displays status and rule details        | Medium   |
| MF-TRF-007 | Disable or delete standing instruction                          | Existing standing instruction exists                    | 1. Open instruction<br>2. Disable/delete                                                                                                    | Instruction status changes accordingly and future execution stops | Medium   |

### Negative Tests

| TC ID      | Test Case                                                                         | Preconditions                                  | Steps                                                                 | Expected Result                                                     | Priority |
| ---------- | --------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- |
| MF-TRF-008 | Transfer amount exceeds allowed source balance                                    | Eligible accounts exist but insufficient funds | 1. Enter excessive transfer amount<br>2. Submit                       | Transfer is blocked with proper validation or business-rule message | High     |
| MF-TRF-009 | Unauthenticated user cannot access the Account Transfers page | User is not authenticated | 1. Navigate to the Account Transfers page URL as an unauthenticated user | User is redirected to the login page (or shown the login screen) and cannot access the Account Transfers form | High     |
| MF-TRF-010 | Delete multiple standing instructions using the bulk Delete Selected action | Multiple standing instructions exist in the listing | 1. Select the checkboxes for two standing instructions in the table<br>2. Click 'Delete Selected' in the bulk actions toolbar<br>3. Confirm the bulk delete | Both selected standing instruction rows are no longer visible in the table | High     |
| MF-TRF-011 | Enable action is unavailable on a standing instruction that is already Active | A standing instruction exists with Status = Active | 1. Locate the row for the Active standing instruction<br>2. Attempt to click an Enable row action | Enable action is not available for the row; Status remains Active; no status change occurs | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                                         | Preconditions                   | Steps                                         | Expected Result                                | Priority |
| ---------- | --------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------- | ---------------------------------------------- | -------- |
| MF-TRF-013 | Toolbar Create button hidden for user without standing-instruction permissions | Authenticated user without permissions for account transfers and standing instruction management | 1. Navigate to the Standing Instructions page as a user lacking the required permissions | The + Create Standing Instruction toolbar button is not visible; user cannot open the Create form | High     |
| MF-TRF-014 | Standing instruction can be paused and resumed where supported                    | Instruction exists              | 1. Pause instruction<br>2. Resume instruction | Execution behavior follows updated status      | Medium   |
| MF-TRF-015 | Disable action is unavailable on a standing instruction that is already Disabled | A standing instruction exists with Status = Disabled | 1. Locate the row for the Disabled standing instruction<br>2. Attempt to click a Disable row action | Disable action is not available for the row; Status remains Disabled; no status change occurs | Low      |

---

## 30. Tax Management

### Functional Tests

| TC ID      | Test Case                                                   | Preconditions                         | Steps                                                               | Expected Result                                 | Priority |
| ---------- | ----------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- | -------- |
| MF-TAX-001 | View tax components list                                    | Tax feature enabled                   | 1. Navigate to tax management                                       | Tax components and groups are displayed         | High     |
| MF-TAX-002 | Create tax component successfully                           | Tax feature enabled                   | 1. Create tax component with name and percentage/value<br>2. Submit | Tax component is created successfully           | High     |
| MF-TAX-003 | Create tax group successfully                               | Tax components exist                  | 1. Create tax group and add components<br>2. Submit                 | Tax group is created successfully               | High     |
| MF-TAX-004 | Link tax group to applicable charge/product where supported | Charges/products and tax config exist | 1. Edit applicable configuration<br>2. Assign tax group<br>3. Save  | Tax configuration is saved successfully         | Medium   |
| MF-TAX-005 | View tax configuration details                              | Tax components/groups exist           | 1. Open tax component/group                                         | Details display correct rates and applicability | Medium   |

### Negative Tests

| TC ID      | Test Case                                                          | Preconditions | Steps                                  | Expected Result                           | Priority |
| ---------- | ------------------------------------------------------------------ | ------------- | -------------------------------------- | ----------------------------------------- | -------- |
| MF-TAX-006 | Create tax component without mandatory fields                      | None          | 1. Omit required fields<br>2. Submit   | Validation error shown                    | High     |
| MF-TAX-007 | Create tax component with invalid rate                             | None          | 1. Enter invalid tax rate<br>2. Submit | Validation error shown                    | High     |
| MF-TAX-008 | Create tax group without components where at least one is required | None          | 1. Leave group empty<br>2. Submit      | Validation or business rule prevents save | Medium   |

### Additional Coverage Tests

| TC ID      | Test Case                                                       | Preconditions                           | Steps                                            | Expected Result                                                                | Priority |
| ---------- | --------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------ | -------- |
| MF-TAX-010 | Tax is applied correctly on configured charge transaction       | Tax-linked charge exists                | 1. Trigger charge transaction                    | Tax amount is computed and posted according to configuration                   | High     |
| MF-TAX-011 | Updating tax rate affects future transactions only              | Tax component already used historically | 1. Update tax rate<br>2. Trigger new transaction | Historical transactions remain unchanged and new transactions use updated rate | High     |
| MF-TAX-012 | Tax breakdown is visible in transaction details where supported | Tax-applied transaction exists          | 1. Open transaction detail                       | Tax component breakdown is shown correctly                                     | Medium   |

---

## 31. System Administration

### Functional Tests

| TC ID      | Test Case                                                  | Preconditions                    | Steps                                                                              | Expected Result                             | Priority |
| ---------- | ---------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------- | -------- |
| MF-SYS-001 | System Administration area is blocked for unauthenticated and non-admin users | User is either not logged in, or logged in without administrative privileges | 1. Attempt to navigate to Admin > System Administration without an authenticated session (or as a non-admin user) | System Administration content (scheduler table, global configuration table, audit trails, admin controls) is not displayed; unauthenticated users are redirected to the Login page; non-admin users see an authorization/permission indicator and remain on a non-admin view | High     |
| MF-SYS-002 | Manage data tables                                         | Data table feature enabled       | 1. Navigate to Data Tables<br>2. View existing tables                              | Data tables list is displayed correctly     | Medium   |
| MF-SYS-003 | Create or register data table where supported              | Data table feature enabled       | 1. Create/register new data table configuration<br>2. Save                         | Data table is created successfully          | Medium   |
| MF-SYS-004 | Manage hooks/webhooks configuration                        | Hook feature enabled             | 1. Open hooks configuration<br>2. Create or edit hook endpoint/settings<br>3. Save | Hook configuration is saved successfully    | Medium   |
| MF-SYS-005 | View scheduler jobs                                        | Scheduler feature enabled        | 1. Navigate to Scheduler Jobs                                                      | Jobs list and status are displayed          | High     |
| MF-SYS-006 | Run a schedulable job manually where supported             | Eligible job exists              | 1. Trigger manual execution                                                        | Job execution starts/completes successfully | Medium   |
| MF-SYS-007 | Manage password preferences or security settings           | Security settings accessible     | 1. Open password/security preferences<br>2. Update policy settings<br>3. Save      | Security preferences are saved successfully | High     |
| MF-SYS-008 | Manage external services or configurations where supported | Feature enabled                  | 1. Open external service configuration<br>2. View/edit supported settings          | Changes are saved successfully              | Low      |
| MF-SYS-009 | Manage maker-checker settings                              | Maker-checker feature accessible | 1. Open maker-checker settings<br>2. Enable or configure                           | Configuration is saved successfully         | High     |
| MF-SYS-010 | View audit or application logs where supported             | Feature enabled                  | 1. Navigate to log/audit section                                                   | Available logs/audit metadata are displayed | Low      |

### Negative Tests

| TC ID      | Test Case                                | Preconditions                | Steps                                                                          | Expected Result                           | Priority |
| ---------- | ---------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------- | -------- |
| MF-SYS-012 | Save invalid hook endpoint configuration | Hook feature enabled         | 1. Enter invalid endpoint/config values<br>2. Save                             | Validation or connectivity error is shown | Medium   |
| MF-SYS-014 | Set invalid password policy values       | Security settings accessible | 1. Enter invalid values such as unsupported lengths or combinations<br>2. Save | Validation error shown                    | High     |

### Additional Coverage Tests

| TC ID      | Test Case                                                          | Preconditions                                      | Steps                                                                  | Expected Result                                               | Priority |
| ---------- | ------------------------------------------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------- | -------- |
| MF-SYS-015 | Scheduler job execution updates last-run status correctly          | Schedulable job exists                             | 1. Run job<br>2. Refresh job list                                      | Last run metadata and status reflect execution outcome        | Medium   |
| MF-SYS-016 | Maker-checker workflow holds pending action until checker approval | Maker-checker enabled and applicable action exists | 1. Perform maker action<br>2. Inspect pending approvals                | Action remains pending until checker approves                 | High     |
| MF-SYS-017 | Checker approval completes pending maker action                    | Pending maker-checker action exists                | 1. Login as checker<br>2. Approve action                               | Underlying business operation completes successfully          | High     |
| MF-SYS-018 | Checker rejection cancels pending maker action                     | Pending maker-checker action exists                | 1. Reject pending action                                               | Pending action is not executed and status updates accordingly | High     |
| MF-SYS-019 | Hook invocation occurs on configured business event                | Valid hook configured                              | 1. Trigger linked event such as client creation or repayment           | Hook is invoked according to event configuration              | Medium   |
| MF-SYS-020 | Password policy update affects subsequent user password operations | Password policy modified                           | 1. Update security policy<br>2. Create/reset password using new values | System enforces updated policy on future operations           | High     |

---

## 32. Logout

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

---

## Test Summary

| Module                                         | Total Tests | High Priority | Medium Priority | Low Priority |
| ---------------------------------------------- | ----------- | ------------- | --------------- | ------------ |
| Login                                          | 12          | 7             | 5               | 0            |
| Home                                           | 5           | 4             | 1               | 0            |
| Dashboard                                      | 5           | 2             | 3               | 0            |
| Global Search                                  | 11          | 5             | 5               | 1            |
| Client Management                              | 29          | 12            | 15              | 2            |
| Group Management                               | 18          | 9             | 8               | 1            |
| Center Management                              | 18          | 8             | 9               | 1            |
| Loan Products                                  | 14          | 13            | 1               | 0            |
| Savings Products                               | 15          | 11            | 4               | 0            |
| Charges                                        | 16          | 10            | 6               | 0            |
| Loan Account                                   | 29          | 17            | 10              | 2            |
| Savings Account                                | 22          | 12            | 7               | 3            |
| Accounting - Chart of Accounts                 | 11          | 8             | 3               | 0            |
| Accounting - Journal Entries                   | 11          | 7             | 4               | 0            |
| Users & Roles                                  | 18          | 14            | 4               | 0            |
| Offices                                        | 11          | 7             | 3               | 1            |
| Employees                                      | 7           | 5             | 2               | 0            |
| Reports                                        | 10          | 4             | 4               | 2            |
| Organization Settings                          | 15          | 6             | 9               | 0            |
| Share Products                                 | 12          | 7             | 4               | 1            |
| Floating Rates                                 | 11          | 7             | 4               | 0            |
| Delinquency Management                         | 10          | 7             | 3               | 0            |
| Share Account                                  | 15          | 8             | 7               | 0            |
| Fixed & Recurring Deposit Accounts             | 20          | 15            | 5               | 0            |
| Accounting - Closures                          | 8           | 6             | 1               | 1            |
| Accounting Rules & Financial Activity Mappings | 9           | 6             | 2               | 1            |
| Provisioning                                   | 9           | 7             | 2               | 0            |
| Teller & Cashier Management                    | 16          | 11            | 4               | 1            |
| Account Transfers & Standing Instructions      | 14          | 9             | 4               | 1            |
| Tax Management                                 | 11          | 7             | 4               | 0            |
| System Administration                          | 18          | 9             | 7               | 2            |
| Logout                                         | 7           | 5             | 2               | 0            |
| **TOTAL**                                      | **437**     | **265**       | **152**         | **20**       |
