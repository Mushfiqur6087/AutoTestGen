# Post-Verification Specifications

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page -> Clients list`
- **Observe**:
  - clients list does not contain a row for <First Name> <Last Name> with Office = <Office>
  - no pending client exists with identifier <Document Key>

**Post-Check**
- **Navigate To**: `Clients page -> Clients list (search for <First Name> <Last Name>) -> Open the newly created client detail`
- **Observe**:
  - clients list contains a new row for <First Name> <Last Name>
  - status badge for the new client shows 'Pending'
  - Office column for the new client equals <Office>
  - In client detail, Identifiers tab contains an entry with Document Type = <Document Type> and Document Key = <Document Key>

**Expected Change**: A new client record for <First Name> <Last Name> is present in the Clients list with status 'Pending' associated to <Office>, and the provided identifier (<Document Type>: <Document Key>) is saved and visible on the client's Identifiers tab.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Bulk Import / Import Jobs (Bulk Import page)`
- **Observe**:
  - import jobs list does not contain a job referencing the uploaded file name or batch id (e.g., '<valid client import file>')
  - no pending or running import job exists for the same filename

**Post-Check**
- **Navigate To**: `Clients -> Bulk Import / Import Jobs (Bulk Import page)`
- **Observe**:
  - import jobs list contains a new entry referencing the uploaded file name or batch id (e.g., '<valid client import file>')
  - status column shows 'Pending' or 'In Progress' (or similar indicating the job has started)
  - job row displays job id or started timestamp

**Expected Change**: A new import job entry is created for the uploaded client import file and its status is 'Pending' or 'In Progress', indicating the import job has been started by the upload.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page (find <target client>)`
- **Observe**:
  - client row for <target client> exists
  - status column for <target client> shows 'Pending'
  - client detail (if opened) shows status 'Pending' and no Activation Date set

**Post-Check**
- **Navigate To**: `Clients page -> Open Client Detail for <target client>`
- **Observe**:
  - client row for <target client> shows status 'Active' (green badge/chip)
  - client detail header shows status 'Active'
  - client detail displays Activation Date equal to <Activation Date>
  - any actions unavailable for Pending clients (e.g., 'Activate') are no longer present

**Expected Change**: The client status is updated from 'Pending' to 'Active' and the Activation Date on the client record is set to <Activation Date>; these changes are visible both on the Clients list and the Client Detail page.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> search for <target client> -> open Client Detail page`
- **Observe**:
  - Status badge is 'Pending'
  - Mobile Number field shows the current (pre-edit) value (not <new value>)

**Post-Check**
- **Navigate To**: `Clients -> search for <target client> -> open Client Detail page`
- **Observe**:
  - Mobile Number field shows '<new value>'
  - Client header/summary displays the updated mobile number
  - Clients list row for <target client> (if visible) shows the updated mobile number

**Expected Change**: The client's Mobile Number is updated to '<new value>' and persisted: the Client Detail page and Clients list reflect the new mobile number while the client remains in 'Pending' status.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page (use search/filter to locate <target client>)`
- **Observe**:
  - client row for <target client> exists
  - status column for <target client> shows 'Pending'

**Post-Check**
- **Navigate To**: `Clients page (search/filter for <target client>) and open Client Detail page for <target client>`
- **Observe**:
  - client row for <target client> shows status 'Rejected'
  - client appears under Rejected/Closed filter (if filter applied)
  - on Client Detail page the status badge reads 'Rejected'
  - the 'Reject' action is no longer available on the Client Detail page

**Expected Change**: The client's status changes from 'Pending' to 'Rejected'; the client appears in Rejected listings and the reject action is not available on the client detail.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Clients List (or open Client Detail for <target client>)`
- **Observe**:
  - clients list contains a row for <target client> with status badge 'Pending'
  - Client Detail header (if opened) shows status badge 'Pending'
  - Withdraw action is available on the Pending client (actions menu or detail page)

**Post-Check**
- **Navigate To**: `Clients -> Search for <target client> and open Client Detail page`
- **Observe**:
  - clients list row for <target client> shows status badge 'Withdrawn'
  - Client Detail header shows status badge 'Withdrawn'
  - Withdraw action is no longer available in the actions menu on the Client Detail page

**Expected Change**: The client's status has changed from 'Pending' to 'Withdrawn' and the Withdraw action is no longer offered; this change is visible both in the Clients list and on the Client Detail page.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Search for <target client> -> Open Client Detail`
- **Observe**:
  - Client status badge is 'Active'
  - Email field does not equal '<new value>' (shows current/old email)

**Post-Check**
- **Navigate To**: `Clients -> Search for <target client> -> Open Client Detail (or refresh page)`
- **Observe**:
  - Email field equals '<new value>'
  - Client status badge remains 'Active'
  - Client detail audit/last-modified metadata shows recent update by the current user (if available)

**Expected Change**: The client's Email Address field on the Client Detail page is updated to '<new value>' and the change is persisted in the backend (remains true after navigation or page refresh).

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Client Detail for <target client>`
- **Observe**:
  - status badge is 'Active'
  - office field displays '<Current Office>'

**Post-Check**
- **Navigate To**: `Clients -> Client Detail for <target client>`
- **Observe**:
  - office field displays '<Destination Office>'
  - Clients list row for <target client> (if viewed) shows Office column = '<Destination Office>'
  - client transfer/audit history contains an entry showing transfer from '<Current Office>' to '<Destination Office>'

**Expected Change**: The client's Office value is updated from '<Current Office>' to '<Destination Office>' and the client's transfer history/audit contains a record of the transfer.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Client List (or open Client Detail for <target client>)`
- **Observe**:
  - client row for <target client> shows status 'Active'
  - client detail page (if opened) displays status badge 'Active' and 'Close' action is available

**Post-Check**
- **Navigate To**: `Clients -> Client List (and open Client Detail for <target client>)`
- **Observe**:
  - client row for <target client> shows status 'Closed' (closed/gray chip) in the list
  - client detail page displays status badge 'Closed' and the 'Close' action is no longer available

**Expected Change**: The client's status changes from 'Active' to 'Closed': the client row and client detail page show status 'Closed', and actions requiring an active client (such as 'Close') are no longer available.

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Open <target client> -> Charges (or Client Charges) tab`
- **Observe**:
  - charges list does not contain the charge matching the <Charge details> to be added
  - no outstanding amount or pending charge row for the same charge type/date exists

**Post-Check**
- **Navigate To**: `Clients -> Open <target client> -> Charges (or Client Charges) tab`
- **Observe**:
  - charges list contains a new entry for the added charge showing the charge name (as entered in <Charge details>)
  - charge row displays the configured amount, charge type/timing, and a status indicating it is active/outstanding
  - outstanding amount equals the entered charge amount (or shows expected outstanding balance if partial payments are supported)

**Expected Change**: A new charge record is present in the client's Charges tab reflecting the entered charge details (name, amount, type/timing) and showing the correct outstanding amount and an active/outstanding status.

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Open Client Detail page for <target client>`
- **Observe**:
  - status badge displays 'Closed'
  - Client detail header shows client name and status 'Closed'

**Post-Check**
- **Navigate To**: `Clients -> Open Client Detail page for <target client'> and Clients list filtered by 'Active' status`
- **Observe**:
  - status badge displays 'Active' (green)
  - Client detail header shows client name and status 'Active'
  - When filtering Clients list by status 'Active', <target client> appears in the results

**Expected Change**: The client's status changes from 'Closed' to 'Active' — the Client Detail page shows 'Active' and the client appears in the Clients list when filtered by Active status.

---

### [TC-022] Create Data Table: leave representative text field (Data Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Data Table Name field blank
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Data Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> <target client> Detail -> Identifiers tab`
- **Observe**:
  - identifiers list does not contain an entry with Document Type '<Document Type>' and Document Key '<Document Key>'

**Post-Check**
- **Navigate To**: `Clients -> <target client> Detail -> Identifiers tab`
- **Observe**:
  - identifiers list contains an entry with Document Type '<Document Type>' and Document Key '<Document Key>'
  - attempting to add the same Document Type and Document Key again results in a validation error or duplicate-prevention message

**Expected Change**: A new identifier with the specified Document Type and Document Key is persisted for the client and is visible in the Identifiers list; the system prevents creating a duplicate identifier when the same values are submitted again.

---

### [TC-023] Create Data Table: leave representative dropdown (Application Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid name> in the Data Table Name field
2. 2. Leave the Application Table Name dropdown unselected
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Application Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Open <target client> detail -> Identifiers tab`
- **Observe**:
  - Identifiers list contains the target identifier row (Document Type: <type>, Document Key: <key>)
  - Identifier row shows expected metadata (created by, created on) if available

**Post-Check**
- **Navigate To**: `Clients -> Open <target client> detail -> Identifiers tab`
- **Observe**:
  - Identifiers list does not contain the removed identifier (Document Type: <type>, Document Key: <key>)
  - Total number of identifiers for the client has decreased by one compared to pre-check
  - No error or retry state shown for the identifier removal

**Expected Change**: The client's Identifiers list no longer includes the removed identifier and the total identifier count is reduced by one, confirming the removal persisted.

---

### [TC-024] Create Data Table: Column Definitions item with missing required column Name
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid name> in the Data Table Name field
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click Add to create a Column Definitions item
4. 4. Leave the Column 'Name' field blank in the new item
5. 5. Select <valid Type> in the new item's Type dropdown
6. 6. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Column Definitions item's Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Clients list`
- **Observe**:
  - clients list does not contain an entry for the client '<First Name> <Last Name>'

**Post-Check**
- **Navigate To**: `Clients -> search for '<First Name> <Last Name>' and open Client Detail page`
- **Observe**:
  - Address section displays '<Address line 1>' in Address Line 1
  - Address section displays '<City>' in City

**Expected Change**: A client record for '<First Name> <Last Name>' exists and the Client Detail page Address section shows the Address Line 1 and City values entered on Step 2 of the Create Client wizard.

---

### [TC-025] Inline edit CRON expression with invalid CRON format
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the CRON Expression cell for a job to edit inline
2. 2. Enter <invalid CRON expression> into the CRON Expression field
3. 3. Save the inline edit

**Original Expected Result:** Inline validation error appears on the CRON Expression field stating it must be a valid CRON expression; the change is rejected and the job's CRON expression remains unchanged.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Clients List (use search to locate the client)`
- **Observe**:
  - Search results do not contain a client with name '<First Name> <Last Name>'
  - No existing Client Detail record for '<First Name> <Last Name>' is open

**Post-Check**
- **Navigate To**: `Clients -> search for '<First Name> <Last Name>' -> open Client Detail -> Family Members tab`
- **Observe**:
  - Family Members tab is visible on the Client Detail page
  - Family members list contains an entry with name '<Family Member Name>'
  - The relationship column/value for the '<Family Member Name>' entry equals '<relationship>'

**Expected Change**: A new family member record is present on the client's Family Members tab showing the added member name '<Family Member Name>' with relationship '<relationship>', where previously no such client/family member existed.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups page (Groups list)`
- **Observe**:
  - Groups list does not contain a row with Name '<group name>' and Office '<office>'

**Post-Check**
- **Navigate To**: `Groups page -> Click the row for '<group name>' to open Group detail`
- **Observe**:
  - Groups list contains a row with Name '<group name>' and Office '<office>'
  - Group detail page lists '<client>' under Members/Selected Clients
  - Status badge shows 'Active' if Active checkbox was checked during creation, otherwise shows 'Pending' or 'Pending Approval'

**Expected Change**: A new group row for '<group name>' assigned to '<office>' appears in the Groups list and the group's detail contains the added client '<client>'; the status reflects whether the Active checkbox was selected at creation.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Bulk Import Groups page -> Import History`
- **Observe**:
  - Import History table does not contain an entry for the selected file name (the file about to be uploaded)
  - No recent success notification for that file is visible in the notifications area

**Post-Check**
- **Navigate To**: `Bulk Import Groups page -> Import History`
- **Observe**:
  - A new row exists in the Import History table for the uploaded file name
  - The new row shows a successful processing status (e.g., 'Success'/'Completed') in the status column
  - The new row displays an upload timestamp consistent with the test execution time
  - The uploader/initiator column shows the current user's username or identifier
  - A success notification is visible in the notifications area immediately after upload

**Expected Change**: A new import history entry is created for the uploaded groups file: the Import History table includes a row with the uploaded file name, a success/completed status, the uploader's username, and a timestamp reflecting the upload time; additionally a success notification is displayed.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Group Detail page for the target group (ensure page is loaded without refresh)`
- **Observe**:
  - status badge reads 'Pending'
  - Activate action/button is present in the Group Action Bar

**Post-Check**
- **Navigate To**: `Groups -> Group Detail page for the same group (refresh page) and Groups -> Groups List`
- **Observe**:
  - status badge reads 'Active' (green) on the refreshed Group Detail page
  - Activate action/button is no longer present in the Group Action Bar
  - Groups list shows the group row with status 'Active'

**Expected Change**: The group's status has been changed from 'Pending' to 'Active' in the backend; both the refreshed Group Detail page and the Groups list reflect the Active status and activation action is removed.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Group Detail page for the target group`
- **Observe**:
  - status badge shows 'Pending'
  - action bar contains 'Close' action

**Post-Check**
- **Navigate To**: `Groups -> Group Detail page for the same group (or Groups list filtered by status 'Closed')`
- **Observe**:
  - status badge shows 'Closed'
  - 'Close' action is no longer available in the action bar
  - group appears in Groups list when filtered by status 'Closed' (and is absent from 'Pending' filter)

**Expected Change**: The group's status has changed from 'Pending' to 'Closed' on the Group Detail page; the Close action is removed from the action bar and the group is discoverable under the 'Closed' status in the Groups list.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Group Detail page (target pending group)`
- **Observe**:
  - Group status is 'Pending'
  - Staff field does not display '<staff>' (no assignment or shows previous value)

**Post-Check**
- **Navigate To**: `Groups -> Group Detail page (target pending group)`
- **Observe**:
  - Staff field displays '<staff>'
  - Group status remains 'Pending' (unless business rules auto-change status)

**Expected Change**: The Staff field on the Group Detail page is updated to show '<staff>' after saving the Assign Staff dialog.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail -> Members tab for Source Group (Pending); optionally open Group Detail -> Members tab for Target Group`
- **Observe**:
  - Source group members list contains the selected client(s) to be transferred (identify by name or account number)
  - Target group members list does NOT contain the selected client(s) prior to transfer (if target group is accessible)

**Post-Check**
- **Navigate To**: `Group Detail -> Members tab for Source Group (Pending) and Group Detail -> Members tab for Target Group`
- **Observe**:
  - Source group members list does NOT contain the selected client(s) after the transfer
  - Target group members list contains the transferred client(s) (identify by name or account number)
  - Optional: Group activity/audit or recent history shows a Transfer Clients action with actor name and timestamp (if audit/history is available)

**Expected Change**: The selected client(s) are removed from the Pending source group's members list and appear as members of the chosen target group; the transfer action is reflected in group membership and (where available) audit/history.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Group Detail (target group)`
- **Observe**:
  - status badge shows 'Active'
  - group appears in Groups list when filtered by 'Active' (if filtering used)
  - no closure entry present in group activity/audit log

**Post-Check**
- **Navigate To**: `Groups -> Group Detail (same target group) and Groups -> Groups list (filter by 'Closed')`
- **Observe**:
  - status badge shows 'Closed' (closed/gray chip) on the Group Detail page
  - group appears in Groups list when filtered by 'Closed' or shows 'Closed' status column in list
  - group activity/audit log contains a closure entry with date and user who performed the action

**Expected Change**: The group's status has changed from 'Active' to 'Closed' and this is reflected on the Group Detail page, in the Groups list under the 'Closed' filter/status, and by a closure entry in the group's activity/audit log.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (Overview/General tab)`
- **Observe**:
  - Group status badge is 'Active'
  - Staff field does not display <staff> (shows previous staff or 'Unassigned')

**Post-Check**
- **Navigate To**: `Group Detail page for the same group (refresh page or navigate back to ensure backend state is loaded)`
- **Observe**:
  - Staff field displays <staff>
  - Activity/audit log or recent history contains an entry for assigning <staff> with current user's username or timestamp

**Expected Change**: The group's Staff field now shows the selected <staff>, and an assignment entry appears in the group's activity/audit log indicating the assignment performed by the acting user.

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the SOURCE group -> Members tab; and Group Detail page for the TARGET group -> Members tab`
- **Observe**:
  - SOURCE group members list contains the client(s) that will be transferred (identified by name or account no.)
  - SOURCE group members count shows the clients present prior to transfer
  - TARGET group members list does not contain the client(s) to be transferred

**Post-Check**
- **Navigate To**: `Group Detail page for the SOURCE group -> Members tab; then Group Detail page for the TARGET group -> Members tab`
- **Observe**:
  - SOURCE group members list does not contain the transferred client(s) (by name or account no.)
  - SOURCE group members count has decreased by the number of transferred client(s)
  - TARGET group members list contains the transferred client(s) (by name or account no.)
  - TARGET group members count has increased by the number of transferred client(s)

**Expected Change**: The selected client(s) are removed from the source group's members list and appear in the target group's members list; member counts for both groups are updated accordingly.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (currently Closed)`
- **Observe**:
  - status badge shows 'Closed'
  - Activate action is available in the Group Action Bar

**Post-Check**
- **Navigate To**: `Group Detail page for the same group (refresh or reopen)`
- **Observe**:
  - status badge shows 'Active' (green/active chip)
  - Activate action is no longer available or is disabled
  - Group appears in Groups list when filtering by status = 'Active'

**Expected Change**: The group's status is changed from 'Closed' to 'Active' in the backend; the Group Detail page shows the 'Active' status and the group is visible in the Active filter/list.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Open the target Group Detail page (the group with status 'Closed')`
- **Observe**:
  - status badge is 'Closed'
  - staff field does not display '<staff>' (is empty or shows a different staff)
  - if available, recent audit/history does not contain an assignment of '<staff>'

**Post-Check**
- **Navigate To**: `Groups -> Open the same Group Detail page (refresh the page or re-open the record)`
- **Observe**:
  - staff field displays '<staff>'
  - status badge remains 'Closed'
  - if available, audit/history contains a new entry recording the staff assignment and the current user's username or ID

**Expected Change**: The Group Detail record now shows the assigned staff as '<staff>' (previously not present), and the group remains in 'Closed' status; an audit/history entry for the assignment is present if the UI exposes it.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page -> Members tab for the Closed (source) group`
- **Observe**:
  - group status is 'Closed' (closed badge/chip visible)
  - members list contains the client(s) intended for transfer (identify by name and/or account number)

**Post-Check**
- **Navigate To**: `Group Detail page -> Members tab for the source group, then navigate to Group Detail page -> Members tab for the target group`
- **Observe**:
  - source group's members list does not contain the transferred client(s) (by name/account number)
  - target group's members list contains the transferred client(s) (by name/account number)

**Expected Change**: The selected client(s) have been removed from the Closed (source) group's Members list and appear in the destination (target) group's Members list after confirming the transfer.

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab`
- **Observe**:
  - meetings list/calendar does not contain an entry with topic '<meeting topic>' on '<meeting date>' at '<meeting time>'
  - no calendar event exists on '<meeting date>' matching '<meeting time>' and '<meeting topic>'

**Post-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab`
- **Observe**:
  - meetings list/calendar contains a new entry with topic '<meeting topic>'
  - the new meeting is shown on '<meeting date>' at '<meeting time>' in calendar or meeting list
  - meeting entry displays the entered topic, scheduled date, and scheduled time

**Expected Change**: A new meeting entry for the group is created and visible in the group's meeting list/calendar showing the scheduled date '<meeting date>', time '<meeting time>', and topic '<meeting topic>'.

---

### [TC-022] Create Data Table: leave representative text field (Data Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Data Table Name field blank
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Data Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab`
- **Observe**:
  - meeting list does not contain an entry with the meeting notes and attendance values to be recorded
  - meeting history/notes does not include an entry matching the new meeting's date, notes, or attendee list

**Post-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab (or Group Detail -> Meetings/History)`
- **Observe**:
  - meeting list contains a new entry with the meeting notes exactly as entered in the Record Meeting dialog
  - the attendance/participant count or listed attendees match the values entered in the Record Meeting dialog
  - the meeting row shows the meeting date matching the recorded meeting (or today's/entered date)
  - corresponding entry appears in the group's meeting history/notes with the entered details

**Expected Change**: A new meeting record is present in the group's meetings list and history containing the provided meeting notes, the recorded attendance/participant details, and the correct meeting date.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page (Administration -> Centers)`
- **Observe**:
  - centers table does not contain a row with Name = <center name> and Office = <office>

**Post-Check**
- **Navigate To**: `Centers page (Administration -> Centers)`
- **Observe**:
  - centers table contains a row with Name = <center name>
  - the same row shows Office = <office>
  - status badge reads 'Active' if Active checkbox was selected during creation, otherwise shows the default pending/status used by the application

**Expected Change**: A new Center entry is persisted and displayed in the Centers table with the submitted Name and Office; its status reflects the Active checkbox selection (Active) or the system's default pending state.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Home -> Centers (Centers list page)`
- **Observe**:
  - centers table does not contain a row with the new Center Name
  - if a center with the same name exists, its Groups tab does not already list the Group being added

**Post-Check**
- **Navigate To**: `Home -> Centers (Centers list page) -> Click the created Center Name -> Center Detail -> Groups tab`
- **Observe**:
  - centers table contains a new row with the created Center Name and the selected Office value
  - on the Center Detail Groups tab, the Member Groups table contains a row for the added Group with the expected group name
  - status or membership columns (if present) reflect the membership (e.g., Active or Member)

**Expected Change**: A new Center row is present in the Centers table showing the entered Name and Office, and the Center Detail's Groups tab lists the added Group in the Member Groups table.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - centers table does not contain rows for the centers included in the import file (no entries matching the import file names)
  - current count of centers (note the value to compare after import)

**Post-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - centers table contains rows for each center from the uploaded import file (matching center name)
  - imported rows display expected metadata such as Office and Submitted On date
  - status column for imported centers is present (e.g., 'Pending' or other expected import status)
  - total count of centers has increased by the number of imported rows

**Expected Change**: For each center in the uploaded file, a corresponding row appears in the Centers table with matching name and expected metadata (Office, Submitted On date) and the overall centers count increases by the number of imported entries; imported centers show the expected import status.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers -> Open Center Detail for the target center (before activation)`
- **Observe**:
  - status badge reads 'Inactive' on the Center Detail page
  - center row in Centers list (if opened) shows status 'Inactive'

**Post-Check**
- **Navigate To**: `Refresh Center Detail page for the same center; then navigate to Centers -> Centers list and locate the center row`
- **Observe**:
  - status badge reads 'Active' on the Center Detail page
  - center row in Centers list shows status 'Active'

**Expected Change**: The center's status changes from 'Inactive' to 'Active' — the Center Detail page displays an 'Active' status badge and the Centers list reflects the same 'Active' status for that center, confirming the activation was persisted.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page for the target center (ensure page is open and showing current status)`
- **Observe**:
  - status badge shows the center is Active (not 'Closed')
  - center name and identifier match the expected target center

**Post-Check**
- **Navigate To**: `Centers -> Centers List, then reopen the same Center Detail page for the target center`
- **Observe**:
  - Center Detail page shows status badge 'Closed'
  - Centers list contains the center row with status column showing 'Closed'

**Expected Change**: The center's status has changed from Active (or previous state) to 'Closed' and this Closed status is persisted and visible both in the Centers list and on the Center Detail page after navigation.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page (Products list)`
- **Observe**:
  - product list does not contain a product with name '<Product Name>'
  - no product row exists with short name '<Short Name>'

**Post-Check**
- **Navigate To**: `Loan Products page -> locate the newly created product by searching for '<Product Name>' -> open the product detail page`
- **Observe**:
  - product list contains a new product row with Product Name '<Product Name>' and Short Name '<Short Name>'
  - product detail page shows Product Name field/value as '<Product Name>'
  - product detail page shows Short Name field/value as '<Short Name>'
  - any other Details-step fields entered during creation are displayed on the product detail page (e.g., fund, currency, principal configuration) matching the values submitted

**Expected Change**: A new Loan Product record is persisted: it appears in the Loan Products list and its product detail page displays the Product Name '<Product Name>', Short Name '<Short Name>', and all values entered in the Details step.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page (list)`
- **Observe**:
  - Loan Products list does not contain a product with the submitted name '<Product Name>'

**Post-Check**
- **Navigate To**: `Loan Products page -> locate the newly created product by '<Product Name>' -> open Product Detail`
- **Observe**:
  - Product detail header shows product name '<Product Name>'
  - Currency field / label shows '<Currency>'
  - Principal Amount Default field shows '<Principal Default>'

**Expected Change**: A new Loan Product record for '<Product Name>' is present and its detail page displays Currency '<Currency>' and Principal Amount Default '<Principal Default>' as entered during creation.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products -> Loan Products list`
- **Observe**:
  - Loan products list does not contain a product with name '<Product Name>'

**Post-Check**
- **Navigate To**: `Loan Products -> Open product detail for '<Product Name>' (use list search or global search to locate the product)`
- **Observe**:
  - Amortization Method displayed as '<Amortization Method>'
  - Interest Method displayed as '<Interest Method>'
  - Days in Year displayed as '<Days in Year>'
  - Days in Month displayed as '<Days in Month>'

**Expected Change**: The newly created Loan Product's detail page shows the selected Amortization Method and Interest Method and the configured Days in Year and Days in Month values exactly as entered in the Settings step.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Products -> Loan Products (list view)`
- **Observe**:
  - loan products list does not contain product with name '<Product Name>'

**Post-Check**
- **Navigate To**: `Products -> Loan Products -> Open product detail for '<Product Name>' (or use global search to locate it)`
- **Observe**:
  - product detail page header shows product name '<Product Name>'
  - terms section displays 'Number of Repayments Default' as '<Number of Repayments Default>'
  - terms section displays 'Repaid Every' as '<Frequency> <Unit>'
  - terms section displays 'Nominal Interest Rate Default' as '<Nominal Interest Rate Default>'

**Expected Change**: A new Loan Product record for '<Product Name>' exists and its Product Detail shows Number of Repayments Default as '<Number of Repayments Default>', Repaid Every as '<Frequency> <Unit>', and Nominal Interest Rate Default as '<Nominal Interest Rate Default>'.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products -> Products list`
- **Observe**:
  - products list does not contain the product with name '<Product Name>' and short name '<Short Name>'
  - no product detail exists for '<Product Name>' in the Products list

**Post-Check**
- **Navigate To**: `Loan Products -> Products list -> Open product detail for '<Product Name>'`
- **Observe**:
  - product detail header shows product name '<Product Name>' and short name '<Short Name>'
  - Charges section lists '<selected charge>'

**Expected Change**: A new Loan Product record for '<Product Name>' is created and its Product Detail page shows the Charges section containing the configured charge '<selected charge>'.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products`
- **Observe**:
  - products list does not contain <Product Name> (or no existing product detail for <Product Name>)

**Post-Check**
- **Navigate To**: `Loan Products -> Open the newly created <Product Name> detail page`
- **Observe**:
  - Accounting Method displays '<Accounting Method other than None>'
  - Fund Source GL Account displays '<Fund Source GL Account>'
  - Loan Portfolio GL Account displays '<Loan Portfolio GL Account>'
  - Interest on Loans GL Account displays '<Interest on Loans GL Account>'
  - Income from Fees GL Account displays '<Income from Fees GL Account>'
  - Income from Penalties GL Account displays '<Income from Penalties GL Account>'
  - Losses Written Off GL Account displays '<Losses Written Off GL Account>'
  - Overpayment Liability GL Account displays '<Overpayment Liability GL Account>'

**Expected Change**: A new Loan Product entry for <Product Name> is created and its Accounting configuration persists: the Accounting Method is set to '<Accounting Method other than None>' and each GL mapping (Fund Source, Loan Portfolio, Interest on Loans, Income from Fees, Income from Penalties, Losses Written Off, Overpayment Liability) matches the selected values.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products list page`
- **Observe**:
  - Savings Products list does not contain a product with the Product Name entered during the test
  - Savings Products list does not contain a product with the Short Name entered during the test

**Post-Check**
- **Navigate To**: `Savings Products list -> refresh and open the newly created product's detail page`
- **Observe**:
  - Savings Products list contains an entry with the Product Name entered during the test
  - The product row displays the Short Name entered during the test
  - Product detail page displays the Nominal Annual Interest Rate and selected Interest Compounding/Posting/Calculation/Days settings as entered
  - Settings show Minimum Opening Balance and Minimum Required Balance values as entered
  - Overdraft is enabled and Maximum Overdraft Amount and Overdraft Interest Rate match the values entered
  - The added charge appears under the product's Charges section
  - Accounting section shows Accounting Method set to 'Cash-based' and required GL account mappings are populated

**Expected Change**: A new Savings Product record is created and visible: it appears in the Savings Products list and its detail page reflects the Product Name and Short Name entered, the configured interest/term settings, minimum balance and overdraft settings, the added charge, and Cash-based accounting mappings.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - table contains a row with product name '<target product>'

**Post-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - table does not contain a row with product name '<target product>'
  - searching/filtering the Share Products list for '<target product>' returns no results

**Expected Change**: The Share Product entry for '<target product>' is removed from the Share Products table and no longer appears in list or search results.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products List`
- **Observe**:
  - share products list contains a row with product name '<target product>'
  - filters are set to show active/available products (no archived/inactive filter applied)

**Post-Check**
- **Navigate To**: `Share Products -> Share Products List`
- **Observe**:
  - share products list does not contain a row with product name '<target product>'
  - total number of rows in the list is reduced by one compared to pre_check

**Expected Change**: The Share Products list no longer shows an entry for '<target product>' after deletion; the product row is removed from the active products list.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - share products table does not contain a row with Product Name: <Product Name> and Short Name: <Short Name>

**Post-Check**
- **Navigate To**: `Share Products -> Share Products list; then open the created product detail page for <Product Name>`
- **Observe**:
  - share products table contains a row with Product Name: <Product Name> and Short Name: <Short Name>
  - on the created product detail page the 'Accounting Method' field/value is 'None'
  - no GL mapping/accounting fields (e.g., Asset GL, Liability GL, Income GL, Expense GL) are visible in the Accounting section
  - Terms section shows 'Capital Value' equal to Total Number of Shares × Nominal/Unit Price (matches entered Total Number of Shares and Nominal/Unit Price)

**Expected Change**: A new Share Product record is created and appears in the Share Products list and detail; its Accounting Method is set to 'None' and the Accounting section does not display any GL mapping fields, and the Terms section displays Capital Value computed as Total Number of Shares × Nominal/Unit Price.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - share products table does not contain a row with the new Product Name
  - share products table does not contain a row with the new Short Name

**Post-Check**
- **Navigate To**: `Share Products -> Share Products list (or open created product from list)`
- **Observe**:
  - share products table contains a new row with the entered Product Name and Short Name
  - product detail page shows Accounting Method as 'Cash-based'
  - product detail page displays GL mapping fields populated: GL Share Reference, GL Share Suspense, GL Equity in Shares, GL Income from Fees, GL Share Equity with the selected accounts

**Expected Change**: A new Share Product record is present in the Share Products list and its detail shows Accounting Method set to 'Cash-based' with all configured GL mapping fields populated with the selected GL accounts.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> List`
- **Observe**:
  - share product list does not contain <Product Name>

**Post-Check**
- **Navigate To**: `Share Products -> Open created product detail for <Product Name>`
- **Observe**:
  - Currency displays '<Currency>'
  - Decimal places displays '<Decimal Places>'
  - Currency In Multiples Of displays '<Currency In Multiples Of>'

**Expected Change**: The product detail page shows the Currency set to <Currency>, and the Decimal Places and Currency In Multiples Of fields reflect the values entered on the Currency (Step 2) of the Create Share Product wizard.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> List`
- **Observe**:
  - No existing share product row with the same <Product Name>
  - Create Share Product wizard not already open

**Post-Check**
- **Navigate To**: `Share Products -> Open the created product detail page for <Product Name> (via list or global search)`
- **Observe**:
  - Share Product appears in the list with name <Product Name>
  - Terms section displays 'Total Number of Shares' equal to the value entered during creation
  - Terms section displays 'Nominal/Unit Price' equal to the value entered during creation
  - Terms section displays 'Capital Value' equal to Total Number of Shares × Nominal/Unit Price (numeric value and formatting match the value shown on the Terms step of the wizard)

**Expected Change**: A new Share Product record is created and the Terms.Capital Value on the product detail page equals the calculated value (Total Number of Shares × Nominal/Unit Price) that was displayed on the Terms step during creation.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - Share Products list does not contain <Product Name>

**Post-Check**
- **Navigate To**: `Share Products -> Open created product detail for <Product Name>`
- **Observe**:
  - Settings section is visible
  - Checkbox 'Allow Dividends for Inactive Clients' is checked
  - Minimum Shares per Client displays value '<Minimum_Shares_per_Client>'
  - Maximum Shares per Client displays value '<Maximum_Shares_per_Client>'

**Expected Change**: The created Share Product's Settings section has 'Allow Dividends for Inactive Clients' enabled and shows the entered Minimum and Maximum Shares per Client values.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products list`
- **Observe**:
  - Share Products list does not contain a product with name '<Product Name>'

**Post-Check**
- **Navigate To**: `Share Products -> Share Product detail for '<Product Name>' (open from list if not auto-redirected)`
- **Observe**:
  - Share Products list contains a new product row with name '<Product Name>'
  - On the Share Product detail page, the Market Price table lists rows with the entered From Date(s) and Share Value(s)

**Expected Change**: A new Share Product with name '<Product Name>' is created and its Market Price table contains the one or more rows added during the wizard, each showing the correct From Date and corresponding Share Value.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> List`
- **Observe**:
  - Share Products list does not contain a product with name <Product Name>

**Post-Check**
- **Navigate To**: `Share Products -> Search for <Product Name> -> Open created Product Detail`
- **Observe**:
  - Product header shows name <Product Name>
  - Charges section lists an entry matching <charge search term>
  - Listed charge shows the expected charge name (matching <charge search term>) and is present in the product's Selected Charges

**Expected Change**: A new Share Product with name <Product Name> is created and its Charges section includes the charge that was added in the wizard (matching <charge search term>).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - charges table does not contain a row with Name '<Charge Name>'
  - no existing charge row with Charge Applies To = 'Loan' and Name '<Charge Name>'

**Post-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - charges table contains a row with Name '<Charge Name>'
  - Charge Applies To column for that row is 'Loan'
  - Charge Time Type column for that row shows '<Charge_Time_Type>' (e.g., Disbursement, Specified Due Date, Installment Fee, Overdue Fees, Tranche Disbursement)
  - Currency column for that row shows '<Currency>'
  - Amount column for that row shows '<Amount>'
  - Payment Mode column for that row shows '<Payment_Mode>'
  - Status/Active column indicates 'Active' if Is Active was toggled on

**Expected Change**: A new charge definition is persisted and appears in the Charges list: a row with the supplied Name and Charge Applies To = 'Loan', the selected Charge Time Type, currency, amount, payment mode, and active status (if Is Active was set).

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Charges List`
- **Observe**:
  - charges list does not contain the new charge with name '<Charge Name>'
  - Charge Time Type dropdown (when creating a charge with 'Charge Applies To' = 'Savings Account') displays savings-specific options: 'Specified Due Date', 'Savings Activation', 'Withdrawal Fee', 'Annual Fee', 'Monthly Fee', 'Overdraft Fee'

**Post-Check**
- **Navigate To**: `Charges -> Charges List`
- **Observe**:
  - charges list contains a row with Name = '<Charge Name>'
  - the 'Charge Applies To' column for the new row shows 'Savings Account'
  - the 'Charge Time Type' column for the new row shows '<Charge_Time_Type>'
  - the 'Amount' column for the new row shows '<Amount>' (or matches the entered amount and currency)
  - status/active indicator reflects the 'Is Active' toggle selected during creation
  - the new charge row is selectable/openable to view detail showing Payment Mode = '<Payment_Mode>' and Calculation Type = '<Charge_Calculation_Type>'

**Expected Change**: A new Charge definition has been persisted and appears in the Charges list with the specified Name, Charge Applies To = 'Savings Account', the selected Charge Time Type, calculation type, amount/currency, payment mode, and active status.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Charges list`
- **Observe**:
  - charges table does not contain a row with Name '<Charge Name>' and Charge Applies To 'Client'
  - optionally: use list search/filter by Name '<Charge Name>' to confirm no existing entry

**Post-Check**
- **Navigate To**: `Charges -> Charges list`
- **Observe**:
  - charges table contains a row with Name '<Charge Name>'
  - the 'Charge Applies To' column for that row is 'Client'
  - the row shows Currency '<Currency>' (if currency column visible)
  - the row shows Amount '<Amount>' (if amount column visible)
  - the row shows Charge Time Type '<Charge Time Type>' and Charge Calculation Type '<Charge_Calculation_Type>' or these details are visible on the charge detail drill-down
  - Payment Mode '<Payment_Mode>' is present in the row or visible on the charge detail

**Expected Change**: A new charge definition is persisted in the backend and appears in the Charges list: a new row exists with Name '<Charge Name>' and Charge Applies To set to 'Client', and associated configured attributes (Currency '<Currency>', Amount '<Amount>', Charge Time Type '<Charge Time Type>', Charge Calculation Type '<Charge_Calculation_Type>', Payment Mode '<Payment_Mode>') are displayed in the list or the charge detail view.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Charges (Charges list)`
- **Observe**:
  - the specific charge row to be deleted is present in the list (identifyable by Name or ID)
  - count of charges in the visible list or matching filter that includes the target charge

**Post-Check**
- **Navigate To**: `Administration -> Charges (Charges list)`
- **Observe**:
  - the specific charge row is no longer present in the active charges list
  - the visible count of charges has decreased by one for the same filter/criteria used in pre_check
  - attempting to open the deleted charge by its previous Name/ID does not open a detail view (not found)

**Expected Change**: The deleted Charge entry is removed from the primary active Charges list (no longer listed or openable) and the visible list count for the same filter/criteria has decreased accordingly.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Charges list (locate the target charge by Name)`
- **Observe**:
  - A row exists for the target Charge in the Charges list
  - Displayed Amount for that Charge is the current (pre-edit) value and is not '<new Amount>'
  - Displayed Charge Time Type for that Charge is the current (pre-edit) value and is not '<Charge Time Type>'
  - Is Penalty and Is Active toggles (or status) reflect the pre-edit states

**Post-Check**
- **Navigate To**: `Charges -> Click the edited Charge Name to open Charge Detail`
- **Observe**:
  - Amount field shows '<new Amount>'
  - Charge Time Type shows the selected loan option '<Charge Time Type>'
  - Is Penalty toggle reflects the state chosen during edit (on/off)
  - Is Active toggle (or status) reflects the state chosen during edit (active/inactive)
  - Charges list row for the same Charge shows the updated Amount and updated Charge Time Type

**Expected Change**: The Charge record's Amount is updated to '<new Amount>' and its Charge Time Type is updated to '<Charge Time Type>'; these changes are visible both on the Charge detail page and in the Charges list, proving the backend persisted the edits.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Charges (Charges list)`
- **Observe**:
  - The target charge entry exists in the Charges table (the charge to be edited is present)
  - Record shows current Amount different from '<new Amount>' (or note current amount value)
  - Record shows current Charge Time Type different from '<Charge Time Type>' (or note current time type)
  - If applicable, Is Active / Is Penalty flags are shown with their current states

**Post-Check**
- **Navigate To**: `Administration -> Charges -> open the same charge detail (click Name) or search and open the edited charge from Charges list`
- **Observe**:
  - Charge detail Amount field shows '<new Amount>'
  - Charge detail Charge Time Type shows the selected '<Charge Time Type>' option
  - Charges list (when refreshed) shows the updated Amount and Charge Time Type for the charge row
  - If Is Active or Is Penalty were toggled during edit, the detail view shows the new toggled states

**Expected Change**: The persisted charge record now reflects the edits: the Amount is updated to '<new Amount>' and the Charge Time Type is updated to '<Charge Time Type>' (and any toggled Is Active / Is Penalty flags reflect their new values) in both the charge detail view and the refreshed charges list.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Charges list`
- **Observe**:
  - Locate the target Charge row by Name (or ID) that will be edited and note its identifier
  - Record the current 'Amount' value for that Charge (and record any other fields you plan to change, e.g., Payment Mode)

**Post-Check**
- **Navigate To**: `Charges -> Charges list (then open the edited Charge detail page)`
- **Observe**:
  - Charges list row for the target Charge shows 'Amount' as '<new Amount>'
  - Charge detail view shows the 'Amount' field with value '<new Amount>'
  - Any other changed fields (e.g., Payment Mode) display the updated selections on the Charge detail view

**Expected Change**: The target Charge's Amount (and any other edited fields) is persisted on the backend and is visible in the Charges list row and on the Charge detail page showing the new values after Save.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Creation and base-flag of the Floating Rate can be fully verified in-app. Automatic adjustment of linked loan products depends on those products being configured to reference this floating rate and may be asynchronous — verifying propagation to all linked products requires identifying one or more specific loan products to inspect and may not be observable immediately.*

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates -> List`
- **Observe**:
  - floating rates list does not contain the test Floating Rate named '<floating rate name>'
  - current base lending rate (if any) is noted so tester can confirm intended initial base state

**Post-Check**
- **Navigate To**: `Floating Rates -> List (then open the newly created Floating Rate record)`
- **Observe**:
  - floating rates list contains a new entry with name '<floating rate name>'
  - the new Floating Rate detail shows 'Is Base Lending Rate' indicator/checkbox as true or a 'Base' badge
  - the Rate Period row exists with From Date equal to '<from date>' and Interest Rate equal to '<interest rate percentage>'
  - Is Differential Rate is unchecked for the added period
  - If applicable: navigate to Loan Products -> open a Loan Product configured to use this Floating Rate and observe its configured interest rate or effective rate display (shows updated rate resolved from the new Rate Period)

**Expected Change**: A new Floating Rate record with the given name is persisted and marked as the Base Lending Rate; the specified rate period is saved. Where loan products are configured to reference this floating rate, those products' effective interest values reflect the new base lending rate according to the rate period (subject to any asynchronous propagation).

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Creation of the Floating Rate and its rate-period rows can be verified in-app via the Floating Rates list/detail. Verification that linked loan products' effective interest rates have been recalculated may be delayed or require inspecting each loan product detail (and may depend on backend recalculation jobs), so that aspect is only partially verifiable from the UI.*

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates -> Floating Rates List and Loan Products -> relevant Loan Product detail(s)`
- **Observe**:
  - Floating Rates list does NOT contain an entry named '<floating rate name>' (record absence)
  - If applicable/known, open each loan product expected to link to the floating rate and note the current interest rate / interest rate configuration (record '<pre-existing rate>' for comparison)

**Post-Check**
- **Navigate To**: `Floating Rates -> Floating Rates List; open the newly created Floating Rate detail -> Rate Periods section; then Loan Products -> relevant Loan Product detail(s)`
- **Observe**:
  - Floating Rates list contains an entry named '<floating rate name>'
  - Floating Rate detail shows two Rate Period rows with the supplied From Dates and Interest Rates
  - The second Rate Period row shows 'Is Differential' checked or is labelled/marked as 'Differential'
  - Linked loan product detail(s) show updated interest rate configuration or a computed interest rate/value that reflects application of the new floating rate period(s) (or show the floating rate linkage in the product settings)

**Expected Change**: A persistent Floating Rate record is created with two rate-period rows; the second period is stored as a differential rate. Loan product(s) that are linked to this floating rate should display updated interest rate configuration or computed interest rate that reflects the new applicable rate period(s).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The Floating Rate record and the newly added Rate Period can be verified in-app. However, automatic adjustment or recalculation of interest for already-existing loan accounts may be performed by background jobs or business processes and might not be immediately reflected in the UI; verifying full propagation to loan schedules/posted transactions may require additional backend checks or running scheduled jobs.*

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates -> Open detail for <existing floating rate>`
- **Observe**:
  - Floating Rate Name shows current value (matches pre-edit)
  - Rate Periods list does not contain a period with From Date '<from date>' and Interest Rate '<interest rate percentage>'
  - Linked Loan Products (if shown) list linked products and display their currently-applied effective rate/period

**Post-Check**
- **Navigate To**: `Floating Rates -> Open detail for <existing floating rate>`
- **Observe**:
  - Floating Rate Name shows '<updated floating rate name>' if it was changed (or unchanged if left as-is)
  - Rate Periods list contains a new period with From Date '<from date>' and Interest Rate '<interest rate percentage>' and correct 'Is Differential Rate' flag
  - Linked Loan Products section/reference shows the new period as the applicable period for products whose effective date is on/after '<from date>' (or the loan product detail resolves to the new rate/period)

**Expected Change**: A new Rate Period has been added to the Floating Rate with the specified From Date, Interest Rate, and differential flag; the Floating Rate name is updated if edited. Linked loan products should reference the new period as the applicable floating rate period for the relevant effective dates (note: propagation to existing loan account schedules or posted interest amounts may require background processing).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Delinquency Management -> Delinquency Ranges`
- **Observe**:
  - Delinquency Ranges table is visible
  - No row exists with Classification = <classification> and Minimum Age Days = <minimum age days>

**Post-Check**
- **Navigate To**: `Organization Settings -> Delinquency Management -> Delinquency Ranges`
- **Observe**:
  - Delinquency Ranges table contains a row with Classification = <classification>
  - The row shows Minimum Age Days = <minimum age days>
  - The Maximum Age Days cell for that row is blank (or displays an explicit empty/—/N/A indicator) showing it applies beyond the minimum

**Expected Change**: A new delinquency range row is created in the Delinquency Ranges table with the provided Classification and Minimum Age Days, and its Maximum Age Days cell is empty indicating the range applies to all days beyond the minimum.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Buckets`
- **Observe**:
  - Delinquency Buckets table does not contain a row with Bucket Name = <bucket name>

**Post-Check**
- **Navigate To**: `Delinquency Management -> Delinquency Buckets`
- **Observe**:
  - Delinquency Buckets table contains a row with Bucket Name = <bucket name>
  - The bucket row displays associated ranges: 'Minimum Age Days: <minimum age days 1> - Maximum Age Days: <maximum age days 1>' and 'Minimum Age Days: <minimum age days 2> - Maximum Age Days: (blank/open-ended)'
  - The bucket row or detail view shows the linked loan products: <linked loan products>
  - Opening the created bucket's detail displays the two ranges as entered and lists the linked loan products

**Expected Change**: A new Delinquency Bucket with name <bucket name> is present in the Delinquency Buckets list; it contains the two configured ranges (first with the specified minimum and maximum, second with the specified minimum and open-ended maximum) and the selected loan products are shown as linked to the bucket.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Accounts -> Loans tab`
- **Observe**:
  - loans list does not contain a loan entry matching the application to be submitted (no row with the selected Product Name and the entered Principal)
  - no loan with status 'Submitted and Pending Approval' exists for this client

**Post-Check**
- **Navigate To**: `Client Detail -> Accounts -> Loans tab (or Global Search -> Loan Account by account number if created)`
- **Observe**:
  - loans list contains a new loan application row with the selected Product Name and the entered Principal
  - the new loan row shows a status badge 'Submitted and Pending Approval' (yellow)
  - opening the new loan row navigates to the Loan Detail page which displays the status badge 'Submitted and Pending Approval'

**Expected Change**: A new loan account record is created for the client with the chosen Product and Principal and its workflow status is 'Submitted and Pending Approval' (visible in the loans list and on the Loan Detail page).

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page -> New Loan Application Wizard -> Step 3 (Charges)`
- **Observe**:
  - Charges repeating group does not contain <charge_name>
  - No existing charge row with amount <amount> in the Charges step

**Post-Check**
- **Navigate To**: `Client Detail page -> Loans/Accounts -> Loan Applications (Submitted / Pending) -> Open the newly created Loan Application`
- **Observe**:
  - Charges repeating group contains a row with Charge Name equal to <charge_name>
  - The charge row displays Amount equal to <amount>
  - If visible, the loan application status is 'Submitted' or 'Pending Approval'

**Expected Change**: A new charge entry is persisted on the loan application: the Charges section shows a row with the specified <charge_name> and <amount> (visible on the application detail in Submitted or Pending state).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Accounts -> Loans`
- **Observe**:
  - loans list does not contain a loan with Repayment Strategy: <repayment_strategy> and Amortization: <amortization>
  - no recently created loan entry exists for this client with the target terms

**Post-Check**
- **Navigate To**: `Client Detail -> Accounts -> Loans (open the newly created loan) OR use the Loan Detail page opened after submission`
- **Observe**:
  - loan appears in client's Loans list (new row) with correct account number and status
  - Terms section on the Loan Detail page shows Repayment Strategy: <repayment_strategy>
  - Terms section on the Loan Detail page shows Amortization: <amortization>

**Expected Change**: A new loan account for the client is created and its Terms section displays Repayment Strategy set to <repayment_strategy> and Amortization set to <amortization> as submitted in Step 2 of the wizard.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (currently Submitted / Pending Approval)`
- **Observe**:
  - status badge displays 'Submitted' or 'Pending Approval'
  - Approved Amount field is empty or not set
  - Approved On Date field is empty or not set
  - Approval activity/log does not contain an approval entry for this loan

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (after confirming Approve dialog)`
- **Observe**:
  - status badge displays 'Approved' (blue)
  - Approved Amount equals the <approved_amount> entered in the Approve dialog
  - Approved On Date equals the <approved_on_date> entered in the Approve dialog
  - Approval activity/log contains an entry showing approval with approver username and note
  - Loan is no longer listed among 'Pending Approval' items in any approvals dashboard or pending list (if a pending list is visible)

**Expected Change**: The loan's lifecycle state changes from Submitted/Pending Approval to Approved; the approved amount and approved-on date are recorded on the loan record, and an approval entry appears in the loan activity/log showing the approver and note.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (Submitted / Pending Approval)`
- **Observe**:
  - status badge displays 'Submitted' or 'Pending Approval'
  - no 'Rejected' status is present on the loan
  - loan does not appear in any 'Rejected' or 'Closed' lists/views

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (and optionally Loans list / Pending Approvals view)`
- **Observe**:
  - status badge displays 'Rejected' (or explicit rejection state label)
  - the 'Submitted' / 'Pending Approval' badge is no longer displayed on the loan
  - activity/audit log on the loan shows a rejection entry (with timestamp and current user as actor) or a rejection note
  - loan no longer appears in Pending Approvals list or checker inbox (if such list/view is available) and appears in lists filtered by 'Rejected' where supported

**Expected Change**: The loan's persisted state changes from Submitted/Pending Approval to Rejected: the Detail page shows a 'Rejected' status, the Submitted/Pending Approval badge is removed, an audit entry records the rejection, and the loan is removed from pending-approval queues.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (Submitted and Pending Approval)`
- **Observe**:
  - status badge displays 'Submitted' or 'Submitted and Pending Approval'
  - Withdraw action/button is visible in the state action bar

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh page or re-open after action)`
- **Observe**:
  - status badge displays 'Withdrawn'
  - the 'Submitted' / 'Submitted and Pending Approval' status badge is not present
  - Withdraw action/button is no longer available in the state action bar

**Expected Change**: The loan's status changes from Submitted/Pending Approval to Withdrawn; the Submitted/Pending Approval status badge is removed and the Withdraw action is no longer available on the loan detail page.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page -> Loans tab (or Client Detail -> Accounts -> Loans)`
- **Observe**:
  - Loan application row for the target loan (by account number or application id) is present in the list
  - Status badge for the loan reads 'Submitted' or 'Pending Approval'
  - Loan detail can be opened from the list (loan detail page is reachable)

**Post-Check**
- **Navigate To**: `Client Detail page -> Loans tab (or Client Detail -> Accounts -> Loans)`
- **Observe**:
  - Loan application row for the target loan is no longer present in the client's loan list
  - No link or action is available to open the deleted loan from the client record
  - Global Search for the loan account number / application id returns no results or indicates the loan is not found

**Expected Change**: The Submitted loan application has been removed from the client's loan list and is no longer accessible from the client profile or global search; attempting to open the deleted loan should fail or show no results.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the Approved loan`
- **Observe**:
  - status badge is 'Approved' (e.g., yellow/orange as per UI)
  - transactions list does not contain a disbursement transaction for the loan
  - loan outstanding principal equals expected pre-disbursement balance

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh if necessary)`
- **Observe**:
  - status badge is 'Active' (green)
  - transactions list contains a Disbursement transaction with amount = <transaction_amount> and date = <disbursed_on_date>
  - Disbursement transaction shows Payment Type = <payment_type> and any provided payment details are recorded
  - repayment schedule and outstanding balances updated to reflect the disbursed amount
  - if 'Disburse to Savings' was toggled: linked Savings account shows a deposit/receipt transaction for amount = <transaction_amount> and the savings balance is increased accordingly

**Expected Change**: The loan's workflow status changes from 'Approved' to 'Active' and a disbursement transaction is recorded with the entered amount, date, and payment type; if Disburse to Savings was used, the target savings account receives a corresponding deposit transaction and balance update.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (currently in Approved state)`
- **Observe**:
  - status badge is 'Approved' (green)
  - state action bar contains 'Undo Approval' action

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh page or navigate back to the loan after performing Undo Approval)`
- **Observe**:
  - status badge is 'Submitted and Pending Approval' (yellow)
  - state action bar no longer shows 'Undo Approval' and shows actions appropriate for a pending approval (e.g., 'Approve')

**Expected Change**: The loan's status changes from 'Approved' to 'Submitted and Pending Approval' and the loan detail page reflects this with a yellow status badge and pending-approval actions.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Active state`
- **Observe**:
  - status badge reads 'Active'
  - outstanding principal/total due is greater than 0
  - no 'Closed obligations met' status is shown
  - transactions list does not contain a repayment equal to the expected full settlement amount

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan`
- **Observe**:
  - status badge reads 'Closed obligations met'
  - outstanding principal/total due is 0 (or shows fully settled)
  - a repayment transaction exists in the transactions list with the full settlement amount and the provided transaction date
  - loan summary shows paid amounts updated (paid principal/interest/fees reflect the settlement)

**Expected Change**: The loan status is updated from 'Active' to 'Closed obligations met', the outstanding amount is cleared to zero, and a repayment transaction for the full settlement amount is recorded on the loan with the specified transaction date.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page -> Charges / Transactions tab for the active loan`
- **Observe**:
  - loan status is 'Active'
  - Charges summary contains an interest charge row with an outstanding amount greater than 0
  - no existing 'Waive Interest' transaction present for the current interest due in the transactions list

**Post-Check**
- **Navigate To**: `Loan Detail page -> Charges / Transactions tab for the same loan`
- **Observe**:
  - Charges summary shows the interest charge marked as waived or shows a reduced/outstanding amount reflecting the waiver
  - Transaction history contains a 'Waive Interest' transaction or entry with the waived amount and date
  - Loan overview/summary reflects the updated interest due and outstanding balance after the waiver

**Expected Change**: The previously outstanding interest charge is recorded as waived (or its outstanding amount is reduced by the waived amount); a 'Waive Interest' transaction appears in the transaction history with waiver details; and the loan's charges/overview reflect the reduced interest due and updated outstanding balance.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan`
- **Observe**:
  - status badge is 'Active'
  - no 'Written Off' status badge present

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (or refresh current loan detail)`
- **Observe**:
  - status badge is 'Written Off' (red)
  - a write-off transaction appears in the Transactions/Activity list with write-off date and amount
  - outstanding principal/interest is marked or annotated as written off (or outstanding balance reflects the write-off)

**Expected Change**: The loan's status is updated to 'Written Off'; a corresponding write-off transaction is recorded in the loan transactions and the outstanding balance/annotations reflect the write-off.

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the specific Active loan (and optionally Loans list)`
- **Observe**:
  - status badge on Loan Detail shows 'Active'
  - loan row in Loans list displays status 'Active' (if present)

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan and Loans list`
- **Observe**:
  - status badge on Loan Detail shows 'Closed' (gray)
  - loan row in Loans list displays status 'Closed' (gray) where applicable
  - closure date or closure audit entry is present on Loan Detail (if UI shows closure metadata)

**Expected Change**: The loan's status is changed from 'Active' to 'Closed' and both the Loan Detail page and the Loans list (where visible) reflect the closed state with a gray 'Closed' status badge and associated closure metadata.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the Active loan -> Reschedule / Requests section`
- **Observe**:
  - reschedule requests list does not contain a pending reschedule entry for this loan
  - no 'Reschedule Request Pending' banner or pending indicator is shown on the Loan Detail page

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan -> Reschedule / Requests section`
- **Observe**:
  - reschedule requests list contains a new entry with status 'Pending Approval' or 'Pending'
  - the new reschedule entry displays Reschedule From Date: <reschedule_from_date>
  - the new reschedule entry displays Adjusted Due Date: <adjusted_due_date>
  - the new reschedule entry displays Reason: <reason>
  - loan status badge remains 'Active' and a pending reschedule indicator is visible on the page

**Expected Change**: A new reschedule request record is created and visible on the Loan Detail page's reschedule/requests section with status 'Pending Approval' and shows the submitted Reschedule From Date (<reschedule_from_date>), Adjusted Due Date (<adjusted_due_date>), and Reason (<reason>).

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page -> Transactions tab (for the Active loan)`
- **Observe**:
  - transactions list does not contain a row with transaction type 'Prepayment' for the intended/prepay amount
  - outstanding principal / loan balance shown before performing the prepayment

**Post-Check**
- **Navigate To**: `Loan Detail page -> Transactions tab (refresh if necessary)`
- **Observe**:
  - transactions list contains a new row with transaction type 'Prepayment' and the submitted prepayment amount
  - transaction row shows the prepayment date equal to the submitted transaction date
  - outstanding principal / loan balance is reduced by the prepayment amount compared to the pre-check value

**Expected Change**: A new prepayment transaction row is created in the Transactions tab for the loan and the outstanding principal/loan balance is decreased by the prepayment amount.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (open by account number or via client profile)`
- **Observe**:
  - status badge is 'Active'
  - no activity entry describing a foreclosure exists in the activity/notes feed
  - outstanding principal and repayment schedule show pre-foreclosure balances

**Post-Check**
- **Navigate To**: `Loan Detail page -> Activity / Transactions tab (refresh the page if already open)`
- **Observe**:
  - activity feed contains a new entry describing the Foreclosure action with date and performing user
  - status badge indicates a foreclosed/closed state (e.g., 'Foreclosed' or 'Closed')
  - transactions or account entries reflect the foreclosure (e.g., write-off or settlement entries) and outstanding balance is updated accordingly

**Expected Change**: A foreclosure activity entry is recorded and the loan status transitions from Active to a foreclosed/closed state; transaction history and outstanding balances reflect the executed foreclosure.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan`
- **Observe**:
  - status badge shows 'Active'
  - transactions/activity list does not contain a 'Charge Off' entry
  - outstanding principal and arrears balances reflect pre-charge-off amounts

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh if necessary)`
- **Observe**:
  - status badge shows 'Charged Off' or an equivalent closed status indicating charge-off
  - transactions/activity list contains a 'Charge Off' entry with date, amount, and user who performed the action
  - outstanding principal and arrears balances have been adjusted according to the charge-off (e.g., reduced to zero or reduced by charged-off amount)
  - audit/activity feed includes an entry describing the charge-off action

**Expected Change**: The loan status changes from Active to a Charged Off/closed status and the loan's transactions/activity list contains a Charge Off entry; outstanding balances are adjusted to reflect the charge-off.

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target Active loan`
- **Observe**:
  - Loan Detail header shows 'Loan Officer' field is empty or 'Unassigned'
  - Or 'Loan Officer' value is not equal to '<loan_officer>'

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh page or navigate back to ensure data loaded from backend)`
- **Observe**:
  - Loan Detail header displays 'Loan Officer' = '<loan_officer>'
  - Loan summary/header badge shows the assigned loan officer name as '<loan_officer>'

**Expected Change**: The loan's assigned Loan Officer is persisted and displayed in the Loan Detail header as '<loan_officer>' (previously unassigned or different).

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail -> Transactions tab for the target loan`
- **Observe**:
  - transactions list contains the target transaction row (identify by transaction ID, date, amount and transaction type)
  - visible transaction count for the loan (or page total) is recorded
  - loan outstanding balance / account balance shown on loan summary or transactions header (record current value)

**Post-Check**
- **Navigate To**: `Loan Detail -> Transactions tab for the same loan (after performing Undo and confirming)`
- **Observe**:
  - transactions list does not contain the original target transaction row OR the original transaction is marked as 'Reversed/Voided' and a new reversal transaction row exists referencing the original transaction ID
  - visible transaction count for the loan has decreased by one compared to pre_check (or shows reversal marker instead of original row)
  - loan outstanding balance / account balance updated to reflect the undo (pre_check balance adjusted by the transaction amount in the expected direction)

**Expected Change**: The original transaction is no longer active in the loan's Transactions tab: either it is removed or marked reversed and a reversal entry is present; the transactions count is reduced (or reversal marker shown) and the loan balance is updated to reflect the undone transaction.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Accounts (Savings) tab`
- **Observe**:
  - accounts list does not contain a savings account row for product '<product>' with submission date '<Submitted On date>'
  - no account with status 'Submitted and Pending Approval' exists for the target client

**Post-Check**
- **Navigate To**: `Client Detail -> Accounts (Savings) tab`
- **Observe**:
  - accounts list contains a new savings account row for product '<product>'
  - status badge for the new account is 'Submitted and Pending Approval'
  - submitted on date column shows '<Submitted On date>' for the new account
  - minimum opening balance column shows '<minimum opening amount>'
  - field officer column shows '<Field Officer>'
  - overdraft indicator reflects the selected toggle state ('Allowed' when on, 'Not allowed' when off)
  - if charge was added: charges column/row shows '<charge>' on the new account

**Expected Change**: A new Savings Account record for the selected product is created for the client and appears in the Accounts list with status 'Submitted and Pending Approval' and the entered metadata (Submitted On date, Field Officer, Minimum Opening Balance, overdraft setting, and any added charges).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the target account`
- **Observe**:
  - status badge shows 'Submitted' or 'Pending Approval'
  - no 'Approved' status or approval date present in account header/audit trail

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account (refresh if necessary)`
- **Observe**:
  - status badge shows 'Approved'
  - approval metadata present (approval date and approver username) in audit/history or account header
  - account appears as 'Approved' in Savings Accounts list or search results

**Expected Change**: The savings account status transitions from Submitted/Pending Approval to Approved; the detail page status badge displays 'Approved' and an approval audit entry (approver and approval date) is recorded and visible in the account history/list.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Accounts -> Open the specific Submitted/Pending Approval account detail`
- **Observe**:
  - status badge shows 'Submitted' or 'Pending Approval'
  - no 'Rejected' status badge or rejection indicator is present on the account detail page
  - action buttons include 'Approve' and 'Reject' (Reject is enabled)

**Post-Check**
- **Navigate To**: `Savings Accounts -> Open the same account detail (or refresh the account detail page)`
- **Observe**:
  - status badge shows 'Rejected'
  - a rejection indicator is present (e.g., rejection badge, timeline entry or rejection reason with date)
  - approval actions (Approve/Reject) are no longer available or are disabled for this account
  - the account no longer appears in Pending Approval / Submitted lists (if viewing lists)

**Expected Change**: The savings account status changes from 'Submitted'/'Pending Approval' to 'Rejected' and the account detail displays an explicit rejection indicator (status badge and timeline entry); approval actions are removed or disabled and the account is removed from pending-approval lists.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Accounts -> Open the target Savings Account Detail page (the account to be withdrawn)`
- **Observe**:
  - status badge displays 'Submitted' or 'Pending Approval' (application pending)
  - no 'Withdrawn' status indicator present on the account
  - account appears in any pending approvals / submitted accounts list (if applicable)

**Post-Check**
- **Navigate To**: `Savings Accounts -> Open the same Savings Account Detail page (or refresh and revisit the account)`
- **Observe**:
  - status badge displays 'Withdrawn' on the account detail
  - 'Withdrawn' status indicator is present in the account header/summary
  - the account is removed from Pending Approvals or Submitted lists (if applicable)

**Expected Change**: The account application status changes from 'Submitted'/'Pending Approval' to 'Withdrawn' and the UI shows a persistent 'Withdrawn' status indicator on the Savings Account detail (and the account no longer appears in pending/submitted lists).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the Approved account`
- **Observe**:
  - status badge is 'Approved'
  - Activate action button is visible and enabled
  - Account operations (Deposit/Withdraw) are disabled or not available while in Approved state

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account`
- **Observe**:
  - status badge is 'Active'
  - Activate action button is not visible
  - Account operations (Deposit/Withdraw) are enabled

**Expected Change**: The savings account status changes from 'Approved' to 'Active'. The status badge displays 'Active', the 'Activate' action is removed, and account operations become available.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the target account`
- **Observe**:
  - status badge is 'Approved'
  - approval metadata shows approval date and approver (if available)
  - account appears under 'Approved' when filtering Savings Accounts list by status

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account`
- **Observe**:
  - status badge displays 'Submitted and Pending Approval'
  - approval metadata (approval date/approver) is absent or cleared
  - account appears under 'Submitted and Pending Approval' when filtering Savings Accounts list by status

**Expected Change**: The account's status changes from 'Approved' to 'Submitted and Pending Approval'; any approval timestamp/approver information is cleared and the account is returned to the pending-approval workflow.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab`
- **Observe**:
  - record current account balance as <Pre-Transaction Balance>
  - verify transactions table does not contain a row with Type 'Deposit' and Amount <Transaction Amount> dated <Transaction Date>

**Post-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (refresh page if necessary)`
- **Observe**:
  - transactions table contains a new row with Type 'Deposit', Amount <Transaction Amount>, Payment Type 'Cash', and Transaction Date <Transaction Date>
  - account balance equals <Pre-Transaction Balance> + <Transaction Amount>
  - the new transaction row appears as the most recent entry and shows posted/confirmed status

**Expected Change**: A Deposit transaction is persisted for the account with Amount <Transaction Amount>, Payment Type 'Cash' and Transaction Date <Transaction Date>, and the Account balance increases by <Transaction Amount> compared to the pre-check balance.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for <the account>`
- **Observe**:
  - Account balance shown on the detail page (record the pre-withdrawal balance)
  - Transactions table does not contain a Withdrawal row with Date <Transaction Date>, Amount <Transaction Amount>, and Payment Type 'Cash'
  - Note the current transaction count in the Transactions table (pre-withdrawal count)

**Post-Check**
- **Navigate To**: `Savings Account Detail page for <the account>`
- **Observe**:
  - Transactions table contains a new row with Type 'Withdrawal', Date <Transaction Date>, Amount <Transaction Amount>, and Payment Type 'Cash'
  - Account balance on the detail page equals (pre-withdrawal balance - <Transaction Amount>)
  - Transactions table transaction count has increased by 1 compared to the pre-withdrawal count

**Expected Change**: A new persisted Withdrawal transaction is present for the account with the specified date, amount, and payment type 'Cash', and the displayed account balance is reduced by <Transaction Amount> relative to the pre-withdrawal balance.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab`
- **Observe**:
  - record the current account balance as 'preBalance' (displayed on account header/summary)
  - transactions list does not contain a recent row with Type 'Interest Posting' for the intended posting date
  - if available, note the latest transaction id/date to identify new entry position

**Post-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (refresh view if necessary)`
- **Observe**:
  - transactions list contains a new row with Type 'Interest Posting'
  - the new 'Interest Posting' row shows an Amount equal to the calculated interest expected from the action
  - account balance (displayed on account header/summary) equals preBalance + posted interest amount
  - new transaction appears at or near the top of the transactions list with a transaction date matching the post action

**Expected Change**: A new transaction of type 'Interest Posting' is created for the account with the calculated interest amount, and the displayed account balance increases by that posted interest amount compared to the pre-check balance.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the target account (or Savings Accounts -> open the specific account)`
- **Observe**:
  - status badge is 'Active'
  - Close action button is visible on the account detail page
  - (Optional) In Savings Accounts list the account row shows Status = 'Active'

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account (or Savings Accounts -> open the specific account)`
- **Observe**:
  - status badge is 'Closed'
  - Close action button is no longer present or is disabled
  - Account no longer permits deposit/withdraw actions from the UI
  - (Optional) In Savings Accounts list the account row shows Status = 'Closed'

**Expected Change**: The savings account's status changes from 'Active' to 'Closed' and the account detail UI reflects the closed state (status badge displays 'Closed' and transaction/close action controls are removed or disabled).

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Savings Accounts tab -> Open the target Savings Account detail (or Savings Accounts list -> open account)`
- **Observe**:
  - status badge shows 'Active'
  - no 'Blocked' badge/chip is present on the account header or summary
  - account does not appear in Savings Accounts list when filtered by status = 'Blocked'

**Post-Check**
- **Navigate To**: `Refresh or re-open the same Savings Account detail (or navigate to Savings Accounts list and open the account); optionally apply status filter 'Blocked' in Savings Accounts list`
- **Observe**:
  - status badge shows 'Blocked' on the account detail header
  - a 'Blocked' tag/chip is visible in account summary or header areas
  - account appears in the Savings Accounts list when filtered by status = 'Blocked'

**Expected Change**: The savings account status has changed from 'Active' to 'Blocked' and the 'Blocked' status is persisted and visible on the account detail header and when listing/filtering accounts by status.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Accounts -> Savings Account Detail (target account)`
- **Observe**:
  - Account status is 'Active'
  - No 'Debit Blocked' indicator (badge or status line) is visible
  - Debit/Withdraw action/button is present and enabled

**Post-Check**
- **Navigate To**: `Client Profile -> Accounts -> Savings Account Detail (target account)`
- **Observe**:
  - A visible 'Debit Blocked' indicator (badge or status line) is present on the account header
  - Debit/Withdraw action/button is disabled or not available
  - Attempting to create a debit/withdrawal transaction is blocked and shows an error message or prevention UI (e.g., 'Debit blocked')

**Expected Change**: The account displays a persistent 'Debit Blocked' indicator and debit transactions are prevented — the debit action is disabled/removed and any attempted debit submission is rejected with an explanatory error.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the target account`
- **Observe**:
  - No 'Credit Blocked' indicator (badge or status line) is present on the account header
  - Account status shows 'Active' (or expected active state)
  - Credit/deposit action/button on the account is available/enabled

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account (refresh page or reopen account)`
- **Observe**:
  - 'Credit Blocked' indicator (badge or status line) is present and clearly visible on the account header
  - Credit/deposit action/button on the account is disabled or hidden
  - Attempting to create a credit/deposit transaction results in the UI preventing the action or showing an error message such as 'Credits are blocked for this account'
  - The 'Credit Blocked' indicator persists after a full page refresh (proves backend persistence)

**Expected Change**: The account shows a persistent 'Credit Blocked' indicator and the UI prevents posting credit/deposit transactions (credit action is disabled/hidden and attempts to post credits are rejected with a clear error), demonstrating the credit-block state was saved.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Share Accounts tab for the target client`
- **Observe**:
  - share accounts list does not contain an entry matching the new application (product: <share product>, requested shares: <valid number within product bounds>, submitted on: <valid date>, external id: <external id> if provided)

**Post-Check**
- **Navigate To**: `Client Detail -> Share Accounts tab for the target client`
- **Observe**:
  - share accounts list contains a new entry with Share Product = <share product>
  - the new entry shows Requested Shares = <valid number within product bounds>
  - Submitted On date equals <valid date>
  - status badge for the new entry is 'Submitted and Pending Approval'
  - external id column shows <external id> when provided
  - linked Savings Account for Charges is shown when selected (if applicable)

**Expected Change**: A new Share Account application row is created in the client's Share Accounts list showing the selected share product, requested shares amount, submitted on date, any provided external id, and a status badge of 'Submitted and Pending Approval'; any selected savings account for charges is linked in the application row.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open Share Account detail for <share account> (status: Submitted / Pending Approval)`
- **Observe**:
  - status badge is 'Submitted' or indicates 'Pending Approval'
  - Approved Shares field is empty or not populated
  - Approved Date field is empty or not populated
  - no approval audit entry or approval note exists on the account timeline

**Post-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open Share Account detail for <share account> (after approval)`
- **Observe**:
  - status badge is 'Approved' (visible on the Share Account detail header)
  - Approved Shares field displays the number entered during approval
  - Approved Date shows the date entered during approval
  - account activity / audit timeline contains an entry indicating the approval action and approving user

**Expected Change**: The Share Account's status changes from 'Submitted'/'Pending Approval' to 'Approved', and the Approved Shares and Approved Date fields are populated with the values entered during the approval. The approval is persisted and visible on the account detail view (including an approval audit entry).

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open the Share Account detail page for the target account`
- **Observe**:
  - status badge is 'Submitted and Pending Approval'

**Post-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open the same Share Account detail page`
- **Observe**:
  - status badge is 'Rejected'
  - action buttons related to approval (e.g., Approve/Reject) are disabled or no longer present as applicable

**Expected Change**: The Share Account's status changes from 'Submitted and Pending Approval' to 'Rejected' on the detail page, reflecting the backend state update.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share -> Share Accounts -> Open <share account> detail page`
- **Observe**:
  - status badge is 'Approved'
  - Activate action/button is available

**Post-Check**
- **Navigate To**: `Share -> Share Accounts -> Open <share account> detail page`
- **Observe**:
  - status badge is 'Active'
  - Activate action/button is no longer available (or replaced by actions allowed for an active account)

**Expected Change**: The Share Account status transitions from 'Approved' to 'Active' and the detail page displays an 'Active' status badge.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Accounts -> Open the target Share Account detail page`
- **Observe**:
  - status badge displays 'Approved'
  - an 'Undo Approval' action/button is visible and enabled

**Post-Check**
- **Navigate To**: `Share Accounts -> Open the same Share Account detail page`
- **Observe**:
  - status badge displays 'Submitted and Pending Approval'
  - an 'Approve' action/button (or equivalent submit-for-approval action) is available
  - 'Undo Approval' action/button is no longer present or is disabled

**Expected Change**: The Share Account status changes from 'Approved' to 'Submitted and Pending Approval' and the available actions update accordingly (approval action re-appears and undo-approval is removed/disabled).

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open the target Share Account -> Purchased Shares tab`
- **Observe**:
  - Capture current count of rows where Type = 'Purchase' in the Purchased Shares table
  - Confirm there is no existing 'Purchase' row with Status = 'Pending' that would match this new action

**Post-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> Open the target Share Account -> Purchased Shares tab`
- **Observe**:
  - Purchased Shares table contains a new row with Type = 'Purchase' and Status = 'Pending'
  - The count of rows where Type = 'Purchase' has increased by 1 compared to the pre-check capture
  - The new row shows expected metadata (transaction date near action time and reference or created-by user matching the actor) where available

**Expected Change**: A new entry is created in the Purchased Shares table for the account: there is an added row with Type 'Purchase' and Status 'Pending' (the total number of Purchase rows increases by one), indicating the purchase request was persisted in the backend.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> <share account> (Active) -> Purchased Shares / Transactions`
- **Observe**:
  - Purchased Shares table does not contain a 'Redemption' row for the pending redemption being executed
  - Current unit price is visible on the Share Account page (used to compute redemption amount)
  - Navigate to Savings Accounts -> <linked_savings_account> -> Transactions
  - Selected savings account transaction list does not contain a credit for the redemption amount and available balance = <balance_before>

**Post-Check**
- **Navigate To**: `Client Profile -> Share Accounts -> <share account> (Active) -> Purchased Shares / Transactions; then navigate to Savings Accounts -> <linked_savings_account> -> Transactions`
- **Observe**:
  - Purchased Shares table contains a new row with type 'Redemption' and Number of Shares = <number of shares to redeem>
  - Redemption row shows Amount = <number of shares to redeem> * current unit price (matches calculation displayed on Share Account page)
  - Selected savings account transaction list contains a credit/deposit transaction for the redemption Amount
  - Selected savings account available balance has increased by the redemption Amount compared to <balance_before>

**Expected Change**: A 'Redemption' transaction row is recorded on the Share Account Purchased Shares table showing the redeemed number of shares and the correctly calculated Amount (shares × unit price), and the chosen savings account has a corresponding credit transaction and an increased available balance equal to that Amount.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account detail page for the target <share account> (or Client Profile -> Share Accounts -> open the account)`
- **Observe**:
  - status badge shows 'Active'
  - account summary/holding values visible (sanity check that correct account opened)

**Post-Check**
- **Navigate To**: `Share Account detail page for the same <share account> (or return to Client Profile -> Share Accounts -> open the account)`
- **Observe**:
  - status badge shows 'Closed' (closed/gray chip)
  - Close action is no longer available in actions menu

**Expected Change**: The share account's status changes from 'Active' to 'Closed' and the account detail page displays a 'Closed' status badge; close action is no longer offered.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Accounts -> Fixed & Recurring Deposit Accounts (or Fixed Deposits list)`
- **Observe**:
  - no account row exists for the target <Fixed_Deposit_Product> with deposit amount <Deposit_Amount> and status 'Pending' / 'Awaiting Approval'
  - no recent account detail for the same deposit amount and submission timestamp

**Post-Check**
- **Navigate To**: `Client Profile -> Accounts -> Fixed & Recurring Deposit Accounts -> Open the newly created Fixed Deposit account detail`
- **Observe**:
  - account row exists for <Fixed_Deposit_Product> with displayed Deposit Amount equal to <Deposit_Amount>
  - status badge shows 'Awaiting Approval' or 'Pending Approval'
  - Maturity Date is visible and populated
  - Interest Rate or calculated rate value is displayed and corresponds to the product's configured interest chart
  - Account number or reference identifier for the newly created Fixed Deposit is present in the header/detail

**Expected Change**: A new Fixed Deposit account record is persisted for the client: the Fixed & Recurring Deposit accounts list contains a new row for the selected product and deposit amount, and the account's detail page shows the entered Deposit Amount, a populated Maturity Date, an Interest Rate calculated from the product configuration, and a status indicating the account is awaiting approval.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Accounts -> Recurring Deposits`
- **Observe**:
  - recurring deposits list does not contain an entry for <Recurring_Deposit_Product> (no pending/awaiting approval account exists for this product and client)

**Post-Check**
- **Navigate To**: `Client Profile -> Accounts -> Recurring Deposits (or open the newly created Recurring Deposit Account detail page)`
- **Observe**:
  - recurring deposits list contains a new entry for <Recurring_Deposit_Product>
  - account detail page shows the deposit schedule with installments and dates
  - Total deposits made displayed as 0 or the current total
  - Maturity details (maturity date and maturity amount) are present
  - Interest Rate field displays a calculated value derived from the product's Interest Rate Chart
  - status badge displays 'Awaiting Approval' or equivalent pending-approval state

**Expected Change**: A new Recurring Deposit account for the target client is persisted and visible in the client's Recurring Deposits list and on its detail page, showing the generated deposit schedule, maturity details, an interest rate computed from the product's Interest Rate Chart, 'Total deposits made' initially zero (or current total), and a status indicating the account is awaiting approval.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed & Recurring Deposit Accounts -> Accounts list (or open the Fixed Deposit Account detail page)`
- **Observe**:
  - Fixed Deposit Account detail page shows status badge 'Pending Approval'
  - Accounts list (with status filter 'Pending' or search by account number/client) contains the account row with status 'Pending Approval'

**Post-Check**
- **Navigate To**: `Fixed & Recurring Deposit Accounts -> Accounts list; search for the same Fixed Deposit Account and open its detail page`
- **Observe**:
  - Accounts list row for the target Fixed Deposit Account shows status 'Approved' (no longer listed as 'Pending')
  - Fixed Deposit Account detail page shows status badge 'Approved'

**Expected Change**: The Fixed Deposit Account transitions from 'Pending Approval' to 'Approved' — the account appears with an 'Approved' status in the Accounts list and its detail page reflects the 'Approved' status badge, proving the approval was persisted in the backend.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account -> Account Detail page (approved account)`
- **Observe**:
  - status badge shows 'Approved'
  - 'Activate' action button is present and enabled
  - no activation date is displayed in account header/summary
  - recent transactions do not include an activation/disbursement entry

**Post-Check**
- **Navigate To**: `Fixed Deposit Account -> Account Detail page (same account)`
- **Observe**:
  - status badge shows 'Active' (visual change from 'Approved')
  - activation date is displayed in account header/summary
  - account transactions include an activation transaction or system entry for activation

**Expected Change**: The Fixed Deposit Account status changes from 'Approved' to 'Active'; an activation date appears on the account summary and an activation transaction/entry is recorded in the account transactions.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account detail page (target account)`
- **Observe**:
  - status badge is 'Active'
  - 'Premature Close' action button is present in the action bar
  - transactions list does not contain a 'Premature Close' or 'Account Closure' transaction for the account
  - account appears under Active Fixed Deposits when filtered by status

**Post-Check**
- **Navigate To**: `Fixed Deposit Account detail page (same account) or Fixed Deposits list then open the account`
- **Observe**:
  - status badge is 'Prematurely Closed' (or equivalent closed-with-premature label)
  - 'Premature Close' action button is no longer present in the action bar
  - transactions list contains a closure transaction with type/name indicating premature closure and shows closing balance/date
  - account no longer appears under Active Fixed Deposits when filtered by status and appears under Closed/Prematurely Closed listings

**Expected Change**: The Fixed Deposit Account status is updated from 'Active' to 'Prematurely Closed', the premature-close action is removed, and a closure transaction/record is created showing the closure date and resulting balances.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account detail page for the matured account`
- **Observe**:
  - status badge is 'Matured'
  - no 'Closed on Maturity' status visible on the page

**Post-Check**
- **Navigate To**: `Fixed Deposit Accounts -> Accounts list (or use Global Search) -> open the same account detail page (or refresh the detail page)`
- **Observe**:
  - status badge is 'Closed on Maturity' on the account detail page
  - account activity/transactions list contains a closure entry (e.g., 'Closed on Maturity' or closure transaction)
  - accounts list shows the account with status 'Closed on Maturity' in the status column

**Expected Change**: The Fixed Deposit Account status is updated from 'Matured' to 'Closed on Maturity' and a closure transaction/event is recorded in the account activity/history, visible after refresh or by reopening the account.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page (the account under test)`
- **Observe**:
  - status badge displays 'Pending Approval'
  - action bar shows 'Approve' action available
  - audit/activities section does not yet contain an approval entry for this account (optional)

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page (refresh if necessary)`
- **Observe**:
  - status badge displays 'Approved'
  - action bar no longer shows 'Approve' (or shows approval-related actions as per workflow)
  - audit/activities section contains an approval entry showing current user and timestamp (if audit UI available)

**Expected Change**: The Recurring Deposit Account status is updated from 'Pending Approval' to 'Approved' on the detail page; the Approve action is no longer available and an approval audit entry is recorded in the account activity log where supported.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page (the account under test)`
- **Observe**:
  - status badge displays 'Approved'
  - action bar contains an 'Activate' button

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page (refresh or reopen the same account)`
- **Observe**:
  - status badge displays 'Active'
  - 'Activate' action is no longer present in the action bar
  - activation date is recorded on the account summary (if applicable)

**Expected Change**: The Recurring Deposit Account status changes from 'Approved' to 'Active' on the account detail page, the 'Activate' action is removed, and an activation date is recorded in the account summary.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page -> Transactions tab and Account Summary/Overview`
- **Observe**:
  - transactions list does not contain a Deposit transaction with the intended deposit amount and current/expected transaction date
  - Account Summary 'Total deposits made' value (record current displayed value before performing the deposit)

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page -> Transactions tab and Account Summary/Overview`
- **Observe**:
  - transactions list contains a new Deposit transaction row with the entered deposit amount, correct transaction date and type 'Deposit'
  - Account Summary 'Total deposits made' value increased by the deposited amount compared to the recorded pre-check value

**Expected Change**: A new Deposit transaction row is created in the Transactions list showing the entered amount and transaction date, and the Recurring Deposit account's 'Total deposits made' summary value increases by that deposit amount.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page`
- **Observe**:
  - status badge is 'Active'
  - account number or identifier matches the target Recurring Deposit Account

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page`
- **Observe**:
  - status badge is 'Prematurely Closed'
  - transactions list contains a closure entry (e.g., 'Premature Close' or 'Account Closure') with the expected date
  - account balance and summary reflect closure (e.g., balance adjusted or zeroed according to product rules)

**Expected Change**: The account status changes from 'Active' to 'Prematurely Closed' on the Recurring Deposit Account detail page and a corresponding premature closure transaction is recorded in the account transactions/history.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page`
- **Observe**:
  - status badge shows 'Matured'
  - account summary shows maturity date
  - transactions/history does not contain a 'Closure on Maturity' entry for the current date

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page (refresh if needed)`
- **Observe**:
  - status badge shows 'Closed on Maturity'
  - transactions/history contains a 'Closure on Maturity' transaction or closure event with the closure date
  - account summary displays a closure date and the available balance reflects closed state (zero or appropriately settled)

**Expected Change**: The account status changes from 'Matured' to 'Closed on Maturity', a closure transaction/event is recorded in the transactions/history with the closure date, and the account summary reflects the closed state (closure date shown and balance settled).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - Chart of Accounts tree displays the header account '<existing header account>' under '<Account_Type>'
  - Chart of Accounts tree does NOT contain a detail account row with GL Code '<unique GL Code>' and Account Name '<Account Name>'

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - Chart of Accounts tree contains a new detail account row under '<Account_Type>' -> '<existing header account>' with GL Code '<unique GL Code>' and Account Name '<Account Name>'
  - The new account row shows Account Usage = 'Detail' and the 'Manual Entries Allowed' indicator is enabled/checked (if displayed in UI)

**Expected Change**: A new Detail GL account with the specified GL Code and Account Name appears as a child of the chosen header account in the Chart of Accounts, with Account Usage set to 'Detail' and Manual Entries Allowed enabled.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - chart/tree contains a row for the account with name '<existing Account Name>'
  - the row shows GL Code '<existing GL Code>' (or GL Code column value matches)

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts (refresh the page or re-open the Chart of Accounts view)`
- **Observe**:
  - chart/tree does NOT contain a row for the account with name '<existing Account Name>'
  - no search result for '<existing Account Name>' or '<existing GL Code>' in the Chart of Accounts list

**Expected Change**: The account row for '<existing Account Name>' (GL Code '<existing GL Code>') is removed from the Chart of Accounts tree after deletion; the Chart of Accounts no longer lists that account.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts (open Account Detail for <existing Account Name>)`
- **Observe**:
  - Chart of Accounts tree contains a row with account name '<existing Account Name>' and GL Code '<existing GL Code>'
  - Account Detail view header (when opened) shows account name '<existing Account Name>' and GL Code '<existing GL Code>'

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts (open Account Detail for the edited account)`
- **Observe**:
  - Chart of Accounts tree row for GL Code '<existing GL Code>' displays account name '<new Account Name>'
  - Account Detail view header shows account name '<new Account Name>'
  - GL Code '<existing GL Code>' remains unchanged for the account

**Expected Change**: The account's display name is updated from '<existing Account Name>' to '<new Account Name>' in both the Account Detail view header and the Chart of Accounts tree row (GL Code '<existing GL Code>' remains the same).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Journal Entries`
- **Observe**:
  - journal entries list does not contain an entry with Office = <Office> and Transaction Date = <Transaction_Date> and (if provided) Reference Number = <Reference_Number>

**Post-Check**
- **Navigate To**: `Accounting -> Journal Entries`
- **Observe**:
  - journal entries list contains a new row with Office = <Office> and Transaction Date = <Transaction_Date>
  - the new row shows Debit Total equal to Credit Total and Difference = 0
  - open the new journal entry detail and verify Entry Lines include <GL_Account_1> and <GL_Account_2> with the entered amounts
  - in entry detail, Reference Number and Comments are present when they were provided during creation

**Expected Change**: A new journal entry record is created for the selected Office and Transaction Date; the entry is balanced (Debit total equals Credit total and Difference is zero) and includes the specified GL account lines and any provided reference/comments.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Accounting Closures (Closing Entries) page`
- **Observe**:
  - Closing Entries table does not contain a row with Office '<Office>' and Closing Date '<Closing_Date>'

**Post-Check**
- **Navigate To**: `Accounting -> Accounting Closures (Closing Entries) page`
- **Observe**:
  - Closing Entries table contains a new row with Office '<Office>' and Closing Date '<Closing_Date>'
  - The new closure row shows metadata such as created by (current username) and creation timestamp (if available)
  - Attempt to create a manual Journal Entry dated '<Closing_Date>' (Accounting -> Journal Entries -> Create Journal Entry) is blocked or rejected with a validation/error message preventing posting for dates on or before '<Closing_Date>'

**Expected Change**: A new accounting closure record appears in the Closing Entries table for the specified Office and Closing Date, and the system prevents posting journal entries dated on or before that closing date (creation of such journal entries is rejected with a validation/error message).

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules page (e.g., System Administration -> Accounting Rules)`
- **Observe**:
  - Accounting Rules table does not contain a row with Rule Name '<Rule Name>'
  - No existing row with matching Debit Account(s) and Credit Account(s) for '<Rule Name>'

**Post-Check**
- **Navigate To**: `Accounting Rules page (e.g., System Administration -> Accounting Rules)`
- **Observe**:
  - Accounting Rules table contains a row with Rule Name '<Rule Name>'
  - Office column shows the selected Office or is blank indicating rule applies to all offices
  - Debit Accounts column lists the configured Debit Account(s) selected during creation
  - Credit Accounts column lists the configured Credit Account(s) selected during creation
  - Allow Multiple Debit/Credit Entries flags reflect the choices made (if displayed)

**Expected Change**: A new accounting rule row for '<Rule Name>' is present in the Accounting Rules table showing the configured Office (or blank for all offices), the selected Debit Account(s), the selected Credit Account(s), and the configured allow-multiple flags.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Accounting Rules -> Open the existing Accounting Rule detail view for the rule being edited`
- **Observe**:
  - Rule Name displays the current/original rule name
  - Debit Account(s) list shows currently assigned debit GL account(s)
  - Allow Multiple Debit Entries checkbox shows current state (checked/unchecked)
  - Credit Account(s) list shows currently assigned credit GL account(s)
  - Allow Multiple Credit Entries checkbox shows current state (checked/unchecked)

**Post-Check**
- **Navigate To**: `Administration -> Accounting Rules -> Open the same Accounting Rule detail view (refresh page or re-open from list to confirm persistence)`
- **Observe**:
  - Rule Name displays the <new Rule Name>
  - Debit Account(s) list shows the newly selected Debit Account(s)
  - Allow Multiple Debit Entries checkbox reflects the toggled state performed during edit
  - Credit Account(s) list shows the newly selected Credit Account(s)
  - Allow Multiple Credit Entries checkbox reflects the toggled state performed during edit

**Expected Change**: The Accounting Rule detail view now persists and displays the updated values: Rule Name shows the <new Rule Name>, the Debit and Credit account selections match those chosen during edit, and the Allow Multiple Debit/Credit Entries checkboxes reflect the toggled choices.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules & Financial Activity Mappings -> Financial Activity Mappings (Accounting Rules) list`
- **Observe**:
  - the list contains a row for '<existing rule>' (rule name visible)
  - the rule is discoverable via list search/filter by name

**Post-Check**
- **Navigate To**: `Accounting Rules & Financial Activity Mappings -> Financial Activity Mappings (Accounting Rules) list`
- **Observe**:
  - the list does not contain a row for '<existing rule>'
  - search/filter for '<existing rule>' returns no results or shows 'No records found'

**Expected Change**: The Accounting Rules list no longer contains an entry for '<existing rule>'; the rule row that was present in the pre-check has been removed.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Accounting -> Financial Activity Mappings`
- **Observe**:
  - Financial Activity Mappings table does not contain an entry for <unmapped Financial Activity>

**Post-Check**
- **Navigate To**: `Administration -> Accounting -> Financial Activity Mappings`
- **Observe**:
  - Financial Activity Mappings table contains a new row with Financial Activity: <unmapped Financial Activity> and GL Account: <GL Account>
  - The new mapping row is visible in the table without error badges or pending status

**Expected Change**: A new mapping row for <unmapped Financial Activity> linked to <GL Account> appears in the Financial Activity Mappings table, confirming the mapping was created and will be used for automatic accounting postings.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning -> Provisioning Criteria`
- **Observe**:
  - Provisioning Criteria table does not contain an entry with Criteria Name '<criteria name>'
  - No recent Created Date entry exists matching the expected creation time for '<criteria name>'

**Post-Check**
- **Navigate To**: `Provisioning -> Provisioning Criteria`
- **Observe**:
  - Provisioning Criteria table contains a row with Criteria Name '<criteria name>'
  - Created Date column populated for the row with Criteria Name '<criteria name>'
  - Open the newly created Criteria detail and observe the Definitions repeating table contains a row with Loan Product '<loan product>'
  - In the Definitions row observe Category is 'STANDARD'
  - In the Definitions row observe Minimum_Age is '<minimum overdue days>' and Maximum_Age is '<maximum overdue days>'
  - In the Definitions row observe Provisioning_Percentage is '<provision percentage>'
  - In the Definitions row observe Liability Account is '<liability account>' and Expense Account is '<expense account>'

**Expected Change**: A new Provisioning Criteria entry with the specified Criteria Name is present in the Provisioning Criteria list with a populated Created Date; its detail view contains one Definitions row configured for the specified Loan Product with Category 'STANDARD', the provided minimum and maximum overdue days, the entered provisioning percentage, and the selected liability and expense GL accounts.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning -> Entries page`
- **Observe**:
  - Provisioning Entries table is visible
  - Record the current number of rows and the latest 'Entry Date' shown in the table
  - Note the 'Journal Entry Created' value for the latest row (e.g., journal id/link or status)

**Post-Check**
- **Navigate To**: `Provisioning -> Entries page`
- **Observe**:
  - Provisioning Entries table contains one additional row compared to pre-check
  - The new row displays an appropriate Entry Date corresponding to the provisioning run
  - The new row's 'Journal Entry Created' column shows a created journal entry (e.g., a journal entry ID/link or status 'Created')

**Expected Change**: A new provisioning entry row is added to the Provisioning Entries table for the generated run; its Entry Date corresponds to the generation event and the 'Journal Entry Created' column indicates a created journal entry (visible as an ID/link or a 'Created' status).

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning -> Entries`
- **Observe**:
  - Target provisioning entry exists in the table (identify by run name / reference / run id shown in row)
  - There is exactly one row matching the target provisioning run/reference before recreation
  - 'Journal Entry Created' column value for the existing row is shown (capture current value for comparison)

**Post-Check**
- **Navigate To**: `Provisioning -> Entries`
- **Observe**:
  - A new provisioning entry row appears for the recreated run (an additional row with the same run reference or clear 'recreated' indicator)
  - The new row shows an Entry Date corresponding to the recreation action (newer than the original entry date)
  - The new row's 'Journal Entry Created' column indicates a created journal entry (e.g., displays 'Yes' or shows a journal entry link/ID)
  - Total rows matching the provisioning run/reference has increased by 1

**Expected Change**: A new provisioning entry row is added to the Entries table for the recreated run with an updated Entry Date, and the new row's 'Journal Entry Created' column indicates that a journal entry was created (for example by showing 'Yes' or a journal entry link/ID).

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Offices`
- **Observe**:
  - Offices table does not contain a row with Office Name '<Office Name>'

**Post-Check**
- **Navigate To**: `Administration -> Offices`
- **Observe**:
  - Offices table contains a row with Office Name '<Office Name>'
  - Parent Office column for that row shows '<Parent Office>'
  - Opened On (or Opening Date) column for that row shows '<Opened On Date>'
  - External ID column shows '<External ID>' if an External ID was provided

**Expected Change**: A new office row is created in the Offices table for the entered Office Name and displays the selected Parent Office and the provided Opened On date (and External ID if supplied).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offices -> Click the existing Office Name to open the Office Detail page`
- **Observe**:
  - Office Detail header shows Office Name = <existing office>
  - Opened On date displays the current <Opened On Date>
  - External ID displays the current value (if present)

**Post-Check**
- **Navigate To**: `Offices -> Click the (same) Office Name to open the Office Detail page; optionally return to Offices list to verify listing`
- **Observe**:
  - Office Detail header shows Office Name = <new Office Name> (the value entered in the edit form)
  - Opened On date displays the updated <Opened On Date> (the value entered in the edit form)
  - External ID shows the updated value if it was changed
  - Offices list contains a row for the office with Office Name = <new Office Name>

**Expected Change**: The Office record is persisted: the Office Detail page (and the Offices list) display the updated Office Name and the updated Opened On Date; External ID is updated if provided.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Employees (Employees page/list)`
- **Observe**:
  - employees table does not contain a row with Name '<First Name> <Last Name>' and Office '<Office>'

**Post-Check**
- **Navigate To**: `Administration -> Employees (Employees page/list); refresh the list if necessary`
- **Observe**:
  - employees table contains a row with Name '<First Name> <Last Name>'
  - Office column shows '<Office>' for that row
  - Is Loan Officer column is unchecked for that row
  - Status column shows 'Active' for that row

**Expected Change**: A new employee row is created in the Employees table with the provided First and Last Name and Office; the Status is 'Active' and the Is Loan Officer flag is unset.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employees table does not contain a row with Name '<First Name> <Last Name>'
  - no row exists with Office '<Office>' and Name '<First Name> <Last Name>'

**Post-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - employees table contains a row with Name '<First Name> <Last Name>'
  - Office column for that row shows '<Office>'
  - Is Loan Officer column for that row is checked/true
  - Status column for that row shows 'Active'

**Expected Change**: A new employee record appears in the Employees table with full name '<First Name> <Last Name>', assigned to Office '<Office>', marked as a Loan Officer, and Status set to 'Active'.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees -> Open Staff Detail for '<First Name> <Last Name>'`
- **Observe**:
  - Mobile Number does not equal <new mobile number>
  - Is Loan Officer indicator is not checked on the Staff Detail page

**Post-Check**
- **Navigate To**: `Employees -> Open Staff Detail for '<First Name> <Last Name>'`
- **Observe**:
  - Mobile Number equals <new mobile number>
  - Is Loan Officer indicator is shown as checked on the Staff Detail page

**Expected Change**: The employee's Mobile Number is updated to <new mobile number> and the Is Loan Officer flag is set (checked) on the Staff Detail page, reflecting the persisted backend change.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - tellers table does not contain a row with the <Teller Name> to be created
  - if available, search/filter for <Teller Name> returns no results

**Post-Check**
- **Navigate To**: `Tellers page (refresh list or use search/filter for <Teller Name>)`
- **Observe**:
  - tellers table contains a new row with the created <Teller Name>
  - the Office column for that row shows the selected <Office>
  - the Status column shows the selected status (e.g., 'Active')
  - the Description cell displays the entered <Description> (if provided)

**Expected Change**: A new teller entry is present in the Tellers list matching the submitted Teller Name and Office, with the Status and Description fields reflecting the values entered in the Create Teller form.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers -> Open Teller Detail for <existing teller>`
- **Observe**:
  - Cashiers table is visible on the Teller Detail page
  - Cashiers table does not contain a row with Staff = <Staff> and Start Date = <Start Date>

**Post-Check**
- **Navigate To**: `Tellers -> Open Teller Detail for <existing teller>`
- **Observe**:
  - Cashiers table contains a new row with Staff = <Staff>
  - Start Date column for the new row shows <Start Date>
  - End Date column for the new row shows <End Date> (if End Date was provided)
  - Is Full Day column for the new row shows 'Yes' when checked and 'No' when unchecked
  - Description column for the new row shows <Description> (if Description was provided)

**Expected Change**: A new cashier assignment row is created in the Teller's Cashiers table reflecting the entered Staff, Start Date, optional End Date, the Is Full Day selection, and optional Description.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers -> Click the teller row -> Cashiers table -> Click the cashier row to open Cashier Detail page`
- **Observe**:
  - Cashier Transactions table current row count or last transaction identifier (record snapshot)
  - Cash In Hand numeric value
  - Running Balance numeric value

**Post-Check**
- **Navigate To**: `Tellers -> Click the teller row -> Cashiers table -> Click the cashier row to open Cashier Detail page`
- **Observe**:
  - Cashier Transactions table contains a new transaction row for the allocation (new row compared to pre-check snapshot)
  - New transaction row shows transaction type indicating cash allocation and displays the allocated amount
  - Cash In Hand numeric value increased by the allocated amount compared to pre-check
  - Running Balance numeric value increased by the allocated amount compared to pre-check

**Expected Change**: A new allocation transaction row is added to the Cashier Transactions table and both Cash In Hand and Running Balance values increase by the allocated cash amount relative to their pre-check values.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers -> Click <existing teller> -> Cashiers table -> Click <existing cashier> (Cashier Detail page)`
- **Observe**:
  - Cashier Transactions table: note current rows and ensure there is no settlement row matching Amount: <Amount> and Transaction Date: <Transaction_Date>
  - UI shows current Running Balance value for the cashier (record this value)
  - UI shows current Cash In Hand value for the cashier (record this value)

**Post-Check**
- **Navigate To**: `Tellers -> Click <existing teller> -> Cashiers table -> Click <existing cashier> (Cashier Detail page) -> Transactions / Cashier Transactions table`
- **Observe**:
  - Cashier Transactions table contains a new settlement transaction row with Amount: <Amount>, Currency: <Currency>, Transaction Date: <Transaction_Date>, and a transaction type or description indicating 'Settle Cash' or 'Settlement'
  - Running Balance value has decreased by <Amount> compared to the pre-check recorded Running Balance
  - Cash In Hand value has decreased by <Amount> compared to the pre-check recorded Cash In Hand

**Expected Change**: A new settlement transaction is present for the submitted Amount/Currency/Transaction Date and both the Running Balance and Cash In Hand values have decreased by the settlement Amount to reflect the posted settlement.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Users (Users page)`
- **Observe**:
  - Users table does not contain a row with Username '<new username>'
  - No user detail exists for '<new username>' (search returns no results)

**Post-Check**
- **Navigate To**: `Administration -> Users (Users page) and open the created user's detail`
- **Observe**:
  - Users table contains a new row with Username '<new username>' and Email '<email address>'
  - Created user's detail page displays First Name '<first name>', Last Name '<last name>', Office '<office>' and the selected Roles
  - If 'Send Password to Email' was checked, UI shows confirmation that password/email was sent (if present)

**Expected Change**: A persistent user record for '<new username>' is created in the backend: the Users list shows the new row with the entered email and the user's detail page reflects the supplied profile fields and assigned roles.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Users & Roles -> Roles`
- **Observe**:
  - roles list does not contain a role named '<role name>'
  - no Role Permissions page is open for '<role name>'

**Post-Check**
- **Navigate To**: `Users & Roles -> Roles`
- **Observe**:
  - roles list contains a row for the new role with name '<role name>' and description '<description>'
  - clicking the new role opens the Role Permissions page for '<role name>'
  - Role Permissions page displays a permissions matrix with categories: 'User Management', 'Portfolio', 'Organization', 'Accounting', 'Reports', and 'Other_Permissions'
  - each listed category shows its permission checkboxes (visible and interactable)

**Expected Change**: A new Role record with the specified name and description is persisted and the Role Permissions page for that role displays the permissions matrix containing the categories User Management, Portfolio, Organization, Accounting, Reports, and Other_Permissions with their permission checkboxes.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Users & Roles -> Roles -> <role name> -> Permissions tab`
- **Observe**:
  - User Management permission group is visible
  - The checkbox for <specific permission> is currently unchecked (or not selected)

**Post-Check**
- **Navigate To**: `Users & Roles -> Roles -> <role name> -> Permissions tab (after saving / page refresh or navigating away and back)`
- **Observe**:
  - The checkbox for <specific permission> under User Management is checked
  - Role last-modified metadata or audit indicator shows a recent change (if available)

**Expected Change**: The specific permission checkbox for <specific permission> is persisted as checked on the role's Permissions tab after refresh or re-opening the role, demonstrating the backend stored the permission change.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Profile -> Accounts -> <From_Account> -> Transactions AND Client Profile -> Accounts -> <To_Account> -> Transactions`
- **Observe**:
  - From account current balance shown (record as <from_balance_before>)
  - From account transactions list does NOT contain a debit transaction for <transfer amount> on <transfer date> referencing transfer to <To_Account>
  - To account current balance shown (record as <to_balance_before>)
  - To account transactions list does NOT contain a credit transaction for <transfer amount> on <transfer date> referencing transfer from <From_Account>

**Post-Check**
- **Navigate To**: `Client Profile -> Accounts -> <From_Account> -> Transactions AND Client Profile -> Accounts -> <To_Account> -> Transactions`
- **Observe**:
  - From account transactions list contains a new DEBIT transaction with amount <transfer amount>, date <transfer date>, description contains <description> (if provided), and counterparty reference to <To_Account>
  - From account current balance equals <from_balance_before> - <transfer amount>
  - To account transactions list contains a new CREDIT transaction with amount <transfer amount>, date <transfer date>, description contains <description> (if provided), and counterparty reference to <From_Account>
  - To account current balance equals <to_balance_before> + <transfer amount>
  - UI shows a success notification confirming the transfer (message includes transfer processed or similar)

**Expected Change**: A debit transaction for <transfer amount> is recorded on the source account dated <transfer date> and the source account balance is reduced by <transfer amount>; simultaneously a credit transaction for <transfer amount> is recorded on the destination account dated <transfer date> and the destination account balance is increased by <transfer amount>.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Standing Instructions page (Standing Instructions list)`
- **Observe**:
  - standing instructions table does not contain a row with Name = <Name>

**Post-Check**
- **Navigate To**: `Standing Instructions page (Standing Instructions list)`
- **Observe**:
  - success notification is displayed with text indicating the standing instruction was created
  - standing instructions table contains a row with Name = <Name>
  - the new row displays configured details when provided: From Account = <From_Account>, To Account = <To_Account>, Instruction Type = <Instruction_Type>, Amount = <Amount> (if entered), Validity From = <validity from date> (if entered), Validity Till = <validity till date> (if entered), Recurrence = <Recurrence_Type> / frequency details (if configured)

**Expected Change**: A new Standing Instruction record is present in the Standing Instructions table with Name = <Name>, and the displayed fields (From Account, To Account, Instruction Type, Amount, Validity dates, and Recurrence details) match the values entered in the Create form.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Standing Instructions -> Listing`
- **Observe**:
  - a row exists with Name = <Name>
  - Status column for that row shows 'Disabled'

**Post-Check**
- **Navigate To**: `Standing Instructions -> Listing (refresh or navigate away and return) and optionally open the detail for <Name>`
- **Observe**:
  - a row exists with Name = <Name>
  - Status column for that row shows 'Active'
  - when opening the detail for <Name>, the Status field shows 'Active' (verifies persistence)

**Expected Change**: The Standing Instruction with Name = <Name> changes status from 'Disabled' to 'Active' in the listing and the Active status persists after refreshing the list or viewing the instruction detail.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Standing Instructions -> Listing`
- **Observe**:
  - a table row exists with Name = <Name>
  - the Status column for that row shows 'Active'
  - the row shows a 'Disable' action/button available

**Post-Check**
- **Navigate To**: `Standing Instructions -> Listing (refresh if necessary)`
- **Observe**:
  - the table row with Name = <Name> is present
  - the Status column for that row shows 'Disabled'
  - the 'Disable' action/button is no longer shown for that row (or an 'Enable' action is shown if toggle exists)

**Expected Change**: The standing instruction with Name = <Name> now displays Status = 'Disabled' in the listing, and the prior 'Disable' action is removed (or replaced by an 'Enable' action), indicating the backend state was updated.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Navigation -> Account Transfers & Standing Instructions -> Standing Instructions`
- **Observe**:
  - standing instructions table contains a row with Name = <Name>
  - row shows expected details (source account, destination account, amount, frequency) for Name = <Name>

**Post-Check**
- **Navigate To**: `Navigation -> Account Transfers & Standing Instructions -> Standing Instructions`
- **Observe**:
  - standing instructions table does not contain a row with Name = <Name>
  - a transient success notification is shown with text: 'removes standing instruction from listing' or equivalent confirmation message

**Expected Change**: The standing instruction entry with Name = <Name> is removed from the Standing Instructions listing and a success notification confirming deletion is displayed.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tax Management -> Tax Components`
- **Observe**:
  - tax components table does not contain a row with Name '<valid name>'
  - no entry exists with Percentage '<valid percentage>' for Name '<valid name>'

**Post-Check**
- **Navigate To**: `Tax Management -> Tax Components`
- **Observe**:
  - tax components table contains a row with Name '<valid name>'
  - Percentage column for the row shows '<valid percentage>'
  - Debit and Credit GL account columns (if displayed) show the selected <matching GL account> values

**Expected Change**: A new Tax Component has been created and is listed in the Tax Components table: a row appears with the entered Name and Percentage (and the selected debit/credit GL accounts where those columns are shown).

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - Tax Groups table does not contain a row with Name = <valid name>
  - No existing Tax Group row lists <matching Tax Component> in Associated Components for the same name

**Post-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - Tax Groups table contains a row with Name = <valid name>
  - Associated Components column for the new row includes <matching Tax Component>
  - Component effective dates (Start Date / End Date) are visible in the group's component details or hover/expand view for the new row

**Expected Change**: A new Tax Group record is present in the Tax Groups table with the specified Name and its Associated Components listing includes the selected Tax Component; the component row shows the configured start and end dates.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Creation and the holiday record (name, dates, rescheduling type) can be verified in the Holidays UI. Actual effect on installments (that installments falling on holidays were rescheduled) cannot be fully verified here — that requires inspecting affected loan/savings repayment schedules or running/observing scheduled background jobs.*

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Holidays`
- **Observe**:
  - Holidays table is accessible
  - Holidays table does not contain a row with Name = <holiday name> (the holiday to be created)

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Holidays`
- **Observe**:
  - Success notification is displayed with text containing 'creates holiday; installments falling on holidays are rescheduled per configured type' (or equivalent confirmation)
  - Holidays table contains a new row with Name = <holiday name>
  - The new row's Start Date column equals <from date>
  - The new row's To Date column equals <to date>
  - The new row displays the selected Rescheduling Type = <rescheduling type>
  - Applicable Offices column shows one or more of the selected <applicable offices> (where the table exposes office info)

**Expected Change**: A new holiday entry is present in the Holidays table with the provided Name, From/To dates, selected Rescheduling Type, and applicable offices; a success notification confirming holiday creation is shown. (Note: downstream rescheduling of installments is not validated here.)

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Funds`
- **Observe**:
  - funds table does not contain row with Fund Name = <fund name> and External ID = <external id>

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Funds`
- **Observe**:
  - funds table contains row with Fund Name = <fund name> and External ID = <external id>
  - success notification with text containing 'creates fund' is visible

**Expected Change**: A new Fund row with the specified Fund Name and External ID is present in the Funds table and a success notification confirming the creation was displayed.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Payment Types (also open a representative transaction form such as Savings Deposit or Loan Repayment)`
- **Observe**:
  - Payment Types table does not contain '<payment type name>'
  - Representative transaction form payment type dropdown does not contain '<payment type name>'

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Payment Types (then open a representative transaction form such as Savings Deposit or Loan Repayment)`
- **Observe**:
  - Payment Types table contains a row with Name = '<payment type name>' and Is Cash Payment = <chosen state>
  - Representative transaction form payment type dropdown includes '<payment type name>' as a selectable option

**Expected Change**: A new Payment Type record with the specified name and Is Cash Payment flag is persisted in the Payment Types table and is available as a selectable option in transaction forms (e.g., deposit or repayment forms).

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Currencies`
- **Observe**:
  - Target currency rows intended for activation are not marked active (row checkbox unchecked or active indicator/badge absent)
  - No 'Active' state or selected styling present for those currency rows

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Currencies (refresh page or navigate away and return)`
- **Observe**:
  - Previously selected currency rows show active/selected state (row checkbox checked and/or 'Active' indicator/badge visible)
  - Active state persists after navigation/refresh and is reflected in the table (including any Active column or filters)

**Expected Change**: The currency rows that were selected in the core test case are now persisted and displayed as active in the Currencies table (checked/active indicator present), and this active state remains after navigation or page refresh.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import (Clients import card); Clients -> Clients list / Search`
- **Observe**:
  - Import History does not contain an entry for '<import_file_name>' or for a recent upload timestamp matching this test run
  - Clients list does not contain any rows for External ID(s) referenced in the import file (e.g., '<external_id_1>', '<external_id_2>')

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import -> Import History; then Clients -> Clients list / Search`
- **Observe**:
  - Import History contains an entry for '<import_file_name>' (or matching upload timestamp) with status 'Completed' or 'Import Completed'
  - A transient success notification is visible stating 'file uploaded; Clients imported per template' (if notifications are shown)
  - Clients list contains new client rows matching the imported entries by Name and/or External ID (e.g., '<external_id_1>')

**Expected Change**: A new Import History record exists showing the uploaded Clients file has completed successfully, and the client records referenced in that import file are present in the Clients list (discoverable by the imported names and/or External IDs).

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import; then Groups -> Groups List`
- **Observe**:
  - Bulk Import history does not contain an entry for '<import_filename>' (the file you will upload)
  - Groups list does not contain any of the group names present in '<import_file>'

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import; then Groups -> Groups List`
- **Observe**:
  - Bulk Import history contains an entry for '<import_filename>' with a status of 'Completed' or 'Success' and a timestamp after upload
  - Application displays a success notification with text 'file uploaded; Groups imported per template' (or equivalent success message)
  - Groups list contains new rows for each group name from '<import_file>'
  - Imported group rows show expected attributes from the file (e.g., office, staff assignment, and status as provided by the import template)

**Expected Change**: A new import history entry for the uploaded Groups file appears with status 'Completed'/'Success' and the Groups referenced in the import file are created and visible in the Groups list with attributes matching the import file.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import; Organization -> Centers (record baseline before upload)`
- **Observe**:
  - Bulk import history contains no entry for the intended import file name or timestamp
  - Centers list does not contain any rows matching the center names/identifiers present in the import file

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import (Centers import history) and Organization -> Centers`
- **Observe**:
  - Bulk import history contains a new entry for the uploaded Centers file
  - Import entry status is 'Completed' (or similar success status) and shows imported record counts and any error summary
  - Centers list contains new center rows matching the names/identifiers from the import file and shows expected attributes (office, status)

**Expected Change**: A new Bulk Import record for the uploaded Centers file is present with status 'Completed' and the Centers from the file are created and visible in the Centers list with the expected attributes.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Organization -> Offices (Offices list page)`
- **Observe**:
  - Offices list does not contain entries matching the office names present in the import file
  - Total Offices count shown in header does not include the offices from the import file

**Post-Check**
- **Navigate To**: `1) Administration -> Organization -> Bulk Import (Offices import history)
2) Administration -> Organization -> Offices (Offices list page)`
- **Observe**:
  - Bulk Import history shows the uploaded Offices import job with status 'Completed' or 'Import completed' and a successful record count matching the file
  - Offices list contains new rows for each Office defined in the uploaded import file (names, office codes or other identifying fields match the file)
  - Total Offices count shown in header increased by the number of imported offices
  - No import error entries present for the completed import job

**Expected Change**: The Offices defined in the uploaded import file are created in the system: the Bulk Import history shows the Offices import job as completed/successful, and the Offices list contains new entries corresponding to the offices from the file (with matching names/codes).

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Organization -> Employees (Employees list)`
- **Observe**:
  - employees list does not contain rows for identifiers present in the import file (e.g., email addresses, external IDs, or unique usernames)
  - count of employees matching import criteria is zero or unchanged prior to import

**Post-Check**
- **Navigate To**: `Administration -> Organization -> Employees (Employees list)`
- **Observe**:
  - employees list contains one row per entry in the uploaded import file (matched by email, external ID, or username)
  - new employee rows display expected fields: First Name, Last Name, Office, Email, Status
  - import audit/status indicator or import job reference is present (e.g., 'Imported' or import job id) where the UI shows import details

**Expected Change**: Employee/staff records corresponding to each row in the uploaded Staff import file are created in the system and are visible in the Employees list with matching identifying data (first/last name, office, email) and an import/completion status.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Users  (and optionally Admin -> Organization -> Bulk Import -> Import History)`
- **Observe**:
  - Users list does not contain entries matching the records in the import file (by username or email)
  - Bulk Import -> Import History does not contain a completed entry for the import file name or expected upload timestamp

**Post-Check**
- **Navigate To**: `Admin -> Users and Admin -> Organization -> Bulk Import -> Import History`
- **Observe**:
  - Users list contains rows for each user from the uploaded import file (matching username and/or email and external ID where provided)
  - Bulk Import Import History shows an entry for the uploaded file with status 'Completed' or 'Imported'
  - Imported user detail pages (open at least one) show expected imported attributes such as office, roles or active/invited status as provided in the file

**Expected Change**: All user records defined in the uploaded import file are created and visible in the Users list; the Bulk Import history records the upload as completed/imported and individual user records reflect imported attributes.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import -> Loans (Import History)`
- **Observe**:
  - note current latest import entries (timestamp, uploader, status) to establish baseline
  - confirm there is no existing import history entry for the test file (by filename/timestamp) being uploaded
  - navigate to Loans -> All Loans and record current total loan count or confirm that sample loan identifiers from the import file are not present

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Bulk Import -> Loans (Import History) and Loans -> All Loans`
- **Observe**:
  - a new import history entry exists for the uploaded file with uploader equal to the current user
  - the import history entry shows status 'Completed' (or equivalent success state) and any processing summary (rows processed/success/failures) if available
  - Loans list contains new loan accounts created from the import (matching account numbers or external IDs from the import file) or the total loan count increased by the expected number

**Expected Change**: A new Loans import history entry is recorded for the uploaded file with status 'Completed', and the loan accounts specified in the import file are created and visible in the Loans list (matching account numbers/external IDs or reflected in the loans count).

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Savings import history; then navigate to Savings -> Accounts (or Savings Accounts list/search)`
- **Observe**:
  - No existing import history entry for the target import file (search by filename or recent uploaded timestamp) — note current count of Completed imports for comparison
  - Savings Accounts list does not contain the account numbers or external IDs that are expected to be created by the import (if known) or does not show new accounts created at the intended upload timestamp

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Savings import history; open the new import's details; then navigate to Savings -> Accounts and search by account numbers or import timestamp`
- **Observe**:
  - A new import history row exists for the uploaded file (filename or uploaded timestamp matches) with status 'Completed' (or 'Imported') and a success indicator/notification
  - Import details show counts of processed/created records and list of created Savings account numbers or identifiers (or a downloadable result/report)
  - The Savings Accounts list/search returns the account numbers or external IDs shown in the import details (accounts are present and Active/Approved as applicable)

**Expected Change**: A new Bulk Import history entry for the uploaded Savings file is present with status 'Completed' and the Savings accounts listed in the import details are visible in the Savings Accounts list, proving the backend has created the imported Savings records.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The UI can verify the Global Scheduler checkbox state and scheduler-job metadata (Next Run / Last Run / job status). Proving the scheduler engine actually started/stopped (i.e., background job execution) may require waiting for scheduled executions or inspecting server logs, so backend execution is only partially verifiable in the UI.*

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Scheduler Control and System Administration -> Scheduler Jobs`
- **Observe**:
  - value/state of the 'Scheduler Enabled' checkbox on Global Scheduler Control (record current state as 'pre-state')
  - Scheduler Jobs list rows including for at least one known scheduled job: observe 'Last Run' timestamp, 'Next Run' timestamp (if shown), and any job-level status/indicator

**Post-Check**
- **Navigate To**: `System Administration -> Global Scheduler Control and System Administration -> Scheduler Jobs`
- **Observe**:
  - value/state of the 'Scheduler Enabled' checkbox on Global Scheduler Control (should be inverted from pre-state)
  - Scheduler Jobs list rows for the same job(s) inspected in pre_check: observe 'Last Run' and 'Next Run' timestamps and job-level status/indicator
  - If scheduler was disabled by the toggle: job-level 'Next Run' entries should be removed/cleared or job status should indicate disabled and 'Last Run' timestamps should not advance during an observation window
  - If scheduler was enabled by the toggle: job-level 'Next Run' entries should appear/update or subsequent 'Last Run' timestamps should advance after scheduled execution(s) (may require waiting for next scheduled run)

**Expected Change**: The 'Scheduler Enabled' checkbox state is inverted compared to pre_check, and the Scheduler Jobs view reflects that global state: disabling the scheduler removes/upgrades job next-run scheduling or marks jobs as disabled and prevents new 'Last Run' updates; enabling the scheduler restores next-run scheduling and allows jobs to execute (observable as 'Next Run' entries and later updated 'Last Run' timestamps).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - Table contains a row for <Job Name>
  - Record the current state shown by the 'Is Active' toggle for the <Job Name> row (either 'ON' or 'OFF')
  - Note the 'Last Modified' or 'Updated At' timestamp/value for the <Job Name> row if available

**Post-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs (after toggling, then refresh the page or navigate away and return)`
- **Observe**:
  - Table still contains a row for <Job Name>
  - The 'Is Active' toggle for the <Job Name> row reflects the new state (the opposite of the pre-check recorded value)
  - The 'Last Modified' or 'Updated At' timestamp/value for the <Job Name> row is more recent than the pre-check value (if available)
  - No transient UI-only success banner should be the only indicator — the persisted toggle state remains after page refresh/navigation

**Expected Change**: The 'Is Active' value for <Job Name> has been updated and persists in the Manage Scheduler Jobs table (visible after a page refresh or after navigating away and back), and the row's last-modified timestamp is updated accordingly.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - job row for <Job Name> exists in the jobs table
  - CRON Expression cell for <Job Name> does not contain <valid CRON expression> (i.e., the new expression is not yet present)

**Post-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs (refresh or reopen the page to confirm persistence)`
- **Observe**:
  - CRON Expression cell for <Job Name> contains <valid CRON expression>
  - After a full page refresh or reopening Manage Scheduler Jobs, the CRON Expression cell for <Job Name> still contains <valid CRON expression> (proves backend persistence)
  - Optional: job row's Last Updated / Audit metadata reflects a recent update (if column available)

**Expected Change**: The CRON Expression column for the <Job Name> row now displays the provided <valid CRON expression>, replacing the previous expression, and the value remains after a page refresh or reopening the Manage Scheduler Jobs page.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - Job row for <Job Name> exists in the jobs table
  - CRON Expression column value for <Job Name> is not <valid CRON expression>

**Post-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - Job row for <Job Name> exists in the jobs table
  - CRON Expression column value for <Job Name> equals <valid CRON expression>

**Expected Change**: The CRON Expression for the scheduler job named <Job Name> is updated to <valid CRON expression> in the Manage Scheduler Jobs table.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - Locate the row for <Configuration_Name>
  - Record the current Enabled checkbox state for <Configuration_Name> as PRE_STATE (either 'Checked' or 'Unchecked')

**Post-Check**
- **Navigate To**: `System Administration -> Global Configuration (refresh page or navigate away and return to ensure reload)`
- **Observe**:
  - Locate the row for <Configuration_Name>
  - Enabled checkbox state for <Configuration_Name> is present and persisted (should be the opposite of PRE_STATE)
  - Optional: any success/toast message confirming update is shown (e.g., 'Configuration updated' or similar)

**Expected Change**: The Enabled checkbox for <Configuration_Name> is toggled to the opposite state compared to PRE_STATE and remains in that new state after refreshing/navigating back to the Global Configuration list, proving the change was persisted.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - configuration row for <Configuration_Name> is present in the list
  - Value cell for <Configuration_Name> shows the current/previous value (not <valid configuration value>)

**Post-Check**
- **Navigate To**: `System Administration -> Global Configuration (refresh page or navigate away and back if needed)`
- **Observe**:
  - Value cell for <Configuration_Name> displays <valid configuration value>
  - Updated value remains visible after page refresh or after navigating away and returning to the Global Configuration page

**Expected Change**: The Value column for the <Configuration_Name> row is updated to and persists as <valid configuration value>, indicating the configuration change was saved in the backend.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - configuration row for <Configuration_Name> is present
  - record the current 'Enabled' state and current 'Value' for <Configuration_Name> before editing

**Post-Check**
- **Navigate To**: `System Administration -> Global Configuration (refresh page or re-open to confirm persistence)`
- **Observe**:
  - configuration row for <Configuration_Name> is present
  - Enabled state equals <enabled state>
  - Value equals <valid configuration value>

**Expected Change**: The Global Configuration entry for <Configuration_Name> now shows Enabled = <enabled state> and Value = <valid configuration value>, confirming the updated configuration was persisted.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Code Values -> Code Values Editor for <Code List Name>`
- **Observe**:
  - Code values list does not contain an entry with Value = <new entry value>
  - No row exists where Value equals <new entry value> (confirm by scanning visible pages/filter)

**Post-Check**
- **Navigate To**: `Organization Settings -> Code Values -> Code Values Editor for <Code List Name>`
- **Observe**:
  - Code values list contains a row with Value = <new entry value>
  - The 'Is Active' column for that row reflects the state chosen during creation (e.g. 'Active' or 'Inactive')
  - Row appears in the expected sort/filter context (visible without additional unknown filters applied)

**Expected Change**: A new code value row is present in the Code Values Editor for <Code List Name> with Value set to <new entry value> and the Is Active flag matching the selection made during creation.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Code Values Editor -> <Code List Name>`
- **Observe**:
  - code values table contains a row with Value = <existing value>
  - Is Active column shows current state for that row (Active or Inactive)
  - no row exists with Value = <updated value> (if different from <existing value>)

**Post-Check**
- **Navigate To**: `Organization Settings -> Code Values Editor -> <Code List Name> (refresh list if necessary)`
- **Observe**:
  - code values table contains a row with Value = <updated value>
  - Is Active column for that row reflects the change made (Active or Inactive)
  - the original row with Value = <existing value> is no longer present if Value was changed

**Expected Change**: The code value entry that previously had Value = <existing value> now displays Value = <updated value>, and its Is Active flag reflects the updated state made during the edit.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Code Tables (Code Values Editor) -> <Code List Name>`
- **Observe**:
  - a row with Value = <existing value> is present in the list
  - Is Active column shows checked/active indicator for that row

**Post-Check**
- **Navigate To**: `Organization Settings -> Code Tables (Code Values Editor) -> <Code List Name>`
- **Observe**:
  - the row with Value = <existing value> is still present
  - Is Active column shows unchecked/inactive indicator for that row
  - row may be visually styled as inactive (grayed out) or show an 'Inactive' badge

**Expected Change**: The code value row for <existing value> is marked inactive: its 'Is Active' checkbox/indicator is unchecked or an inactive status indicator is displayed (previously it was active).

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Manage Code Values -> <Code List Name>`
- **Observe**:
  - The code values list displays rows in current ordering
  - <entry B> row appears above <entry A> row
  - If present, the positional/index column shows <entry A> at a lower priority/greater index than <entry B>

**Post-Check**
- **Navigate To**: `Organization Settings -> Manage Code Values -> <Code List Name>`
- **Observe**:
  - <entry A> row now appears above <entry B> row in the code values list
  - The positional/index column (if displayed) reflects <entry A> with a higher priority/lower index than before
  - Ordering persists after refreshing the Code Values page or reopening the Code List

**Expected Change**: The selected code value <entry A> has moved up one position in the persisted code list ordering and is now displayed above <entry B>.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Code Tables -> <Code List Name> -> Code Values Editor`
- **Observe**:
  - Code values list displays <entry B> above <entry C>
  - Ordering/index positions show <entry B> immediately preceding <entry C>

**Post-Check**
- **Navigate To**: `Organization Settings -> Code Tables -> <Code List Name> -> Code Values Editor (refresh or navigate away and back)`
- **Observe**:
  - Code values list displays <entry B> below <entry C>
  - Ordering/index positions show <entry B> immediately following <entry C>

**Expected Change**: The code value ordering is persisted so that <entry B> now appears after <entry C> in the Code Values Editor list even after navigating away or refreshing the page.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Data Tables`
- **Observe**:
  - custom data table row for <Data_Table_Name> is present in the list
  - option/button 'Delete' visible for the <Data_Table_Name> row

**Post-Check**
- **Navigate To**: `System Administration -> Manage Data Tables`
- **Observe**:
  - custom data table row for <Data_Table_Name> is not present in the list
  - no search/filter result returns <Data_Table_Name>
  - optional: success toast or banner confirming deletion is displayed (if UI shows transient message)

**Expected Change**: The custom data table named <Data_Table_Name> is removed from the Manage Data Tables list and cannot be found by name via the list or search/filter.

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Data Tables (Manage Data Tables)`
- **Observe**:
  - Manage Data Tables list does not contain an entry with Data Table Name = <data table name>
  - No existing row with Application Table Name = <application table> for the same Data Table Name

**Post-Check**
- **Navigate To**: `System Administration -> Data Tables (Manage Data Tables) and refresh list`
- **Observe**:
  - Manage Data Tables list contains a row with Data Table Name = <data table name>
  - The row shows Application Table Name = <application table>
  - If 'Multi Row' was checked during creation, the row shows Multi Row = true (or corresponding indicator)
  - Open the newly created Data Table detail and observe Column Definitions contains a column with Name = <column name>, Type = <column type> and the configured Length/Is Mandatory/Is Unique flags

**Expected Change**: A new Data Table record is present in the Manage Data Tables list with the specified Data Table Name and Application Table Name; its detail view contains the configured column definition(s) and the Create Data Table form is closed.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Audit Trails`
- **Observe**:
  - an audit row for <Action_Name> exists
  - Processing Result column for that row displays 'Pending'

**Post-Check**
- **Navigate To**: `System Administration -> Audit Trails`
- **Observe**:
  - the same audit row for <Action_Name> is present
  - Processing Result column for that row displays 'Approved'
  - Processing/Approved By column shows the approver username (if available)
  - Processing/Approved Date column shows a recent timestamp (if available)

**Expected Change**: The audit row's Processing Result changes from 'Pending' to 'Approved' after clicking Approve; the row reflects the approver (username) and approval timestamp where the UI exposes those fields.

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Audit Trails`
- **Observe**:
  - audit row for <Action_Name> with Processing Result = 'Pending'
  - audit row identifier (e.g., transaction id / timestamp / actor) to uniquely identify the row

**Post-Check**
- **Navigate To**: `System Administration -> Audit Trails`
- **Observe**:
  - the previously identified audit row now shows Processing Result = 'Rejected'
  - the rejection reason entered is visible in the audit row (if a Rejection Reason column exists) or inside the audit entry detail panel when the row is opened

**Expected Change**: The Processing Result for the selected audit trail entry changes from 'Pending' to 'Rejected', and the provided rejection reason is persisted and viewable in the audit row or its detail view.

---
