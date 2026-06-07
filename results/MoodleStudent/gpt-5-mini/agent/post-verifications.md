# Post-Verification Specifications

### [TC-003] After logging out, accessing a protected page is blocked (requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. After being redirected to the Login page, attempt to navigate to a protected page URL (e.g., open <protected page URL>)

**Original Expected Result:** Logout is enforced and access is blocked: After clicking 'Log out' the user is redirected to the Login page. When attempting to open <protected page URL>, the system redirects to the Login page and does not display protected content (the Login form is shown). The session state remains Unauthenticated and protected resources require re-authentication.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - 'Latest announcements' block is present on the Dashboard in a non-default position (indicating a custom block placement)
  - Dashboard shows Edit mode controls (move, configure, delete) indicating Edit mode is active

**Post-Check**
- **Navigate To**: `Dashboard (refresh the page or navigate away and return) `
- **Observe**:
  - 'Latest announcements' block is not present on the Dashboard in the custom location
  - Default blocks and their default positions are visible (Dashboard block arrangement matches the known default for the student dashboard)
  - Edit mode controls remain available or the UI shows the Dashboard in the expected post-reset state

**Expected Change**: Any custom block placements (for example the 'Latest announcements' block added or moved earlier) have been removed or returned to their original default positions and the Dashboard block arrangement matches the default student dashboard layout after refresh.

---

### [TC-004] Double-click / rapid repeat of Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Immediately click the "Log out" button again (second click occurs before the app finishes redirecting)

**Original Expected Result:** First click succeeds: the current authenticated session is terminated and the user is redirected to the login page with the login form visible. The second click is blocked / has no additional effect: no duplicate session termination occurs, no duplicate redirects occur, and no error is shown to the user; the login page remains visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Timeline block is present at its current/original location (record the block's column and order index or a visual landmark such as 'left column, position 2')
  - Dashboard shows Edit mode controls and move handles for blocks

**Post-Check**
- **Navigate To**: `Dashboard (exit Edit mode if required, then refresh the page)`
- **Observe**:
  - Timeline block is displayed at the new location (the column and order index match the target position noted in the test step)
  - Dashboard layout persists after a full page refresh and the Timeline block remains in the new location

**Expected Change**: The Timeline block is relocated from its original column/index to the specified new column/index and that new position is persisted after refreshing the Dashboard.

---

### [TC-006] Logout in one tab, then attempt action/reload in another authenticated tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the "Log out" button
2. 2. In Tab B, immediately reload the protected page or click a protected-action button (perform the action) without re-authenticating

**Original Expected Result:** Logout in Tab A succeeds: the session is terminated and Tab A is redirected to the login page. The attempt in Tab B is blocked / error shown in the sense that the protected request is not allowed: the reload or protected action redirects Tab B to the login page (login form visible) and the protected action does not complete under an authenticated session.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Timeline block is present on the Dashboard
  - Timeline block is not at <new position> (record its current position index or relative placement among other blocks)
  - Block move controls are not active (no drag overlay visible before the move)

**Post-Check**
- **Navigate To**: `Dashboard (after reposition action, then refresh the page)`
- **Observe**:
  - A drag overlay/handle was shown during the move action and is no longer visible after release
  - Timeline block is displayed at <new position> relative to the other dashboard blocks
  - After refreshing the Dashboard, the Timeline block remains at <new position> (layout persisted for the logged-in user)

**Expected Change**: The Timeline block is relocated to <new position> on the student's Dashboard; the reposition is reflected in the block order immediately after the move and remains in place after a full page refresh (persisted user dashboard layout).

---

### [TC-007] Manually navigate to a protected URL after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. After redirect to the login page, enter the URL of a protected page in the browser address bar and press Enter

**Original Expected Result:** Logout succeeds: the session is terminated and the user is on the login page. The manual navigation to the protected URL is blocked: the app prevents access and redirects to the login page (login form visible). The protected page content is not accessible without re-authentication.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - Timeline block is visible on the Dashboard
  - Timeline block header and three-dot block action menu are present

**Post-Check**
- **Navigate To**: `User Dashboard (after confirming deletion and performing a full page refresh)`
- **Observe**:
  - Timeline block header is not present anywhere on the Dashboard
  - Timeline block three-dot menu and any timeline rows are not visible

**Expected Change**: The Timeline block is removed from the student's Dashboard and remains absent after a page refresh, proving the deletion persisted for the current user.

---

### [TC-013] Open Edit profile when not the profile owner (precondition violation)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. On <user B>'s Profile page, locate the Edit profile link
2. 2. Click the Edit profile link

**Original Expected Result:** Edit_Profile_Form does not open; a visible permission/authorization notification or inline error is shown on the Profile page indicating the action is not allowed; no navigation to the edit form occurs

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Calendar block is present on the Dashboard
  - Record the Calendar block's current column (e.g., left/middle/right) and its index position among blocks in that column (e.g., 1st, 2nd, 3rd).
  - Take note that only one Calendar block exists for this user.

**Post-Check**
- **Navigate To**: `Dashboard (after performing the drag-and-drop) -> Refresh the page while keeping Edit mode enabled`
- **Observe**:
  - Calendar block is present on the Dashboard
  - Calendar block is located in the target column and at the target index position recorded during the drag operation
  - No duplicate Calendar block is present and other blocks' ordering reflects the move

**Expected Change**: The Calendar block's column and ordinal index differ from the values recorded in pre_check and match the intended new position; the moved position persists after a full page refresh.

---

### [TC-015] Leave First name blank and attempt to Update profile (required text field)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Clear the First name field (leave it blank)
2. 2. Enter <valid last name> in Last name
3. 3. Enter <valid email> in Email address
4. 4. Click the Update profile button

**Original Expected Result:** First name field displays an inline validation error indicating it is required; form does not submit; profile is not saved; Edit_Profile_Form remains open

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Dashboard block list / layout is visible
  - Calendar block is present
  - Record the current Dashboard block order (e.g., list of block titles or the Calendar block's position index and its immediate neighbor blocks) before performing the move

**Post-Check**
- **Navigate To**: `Dashboard (Edit mode enabled) after performing the Move action and refreshing the page`
- **Observe**:
  - Calendar block is present at the target/new position in the recorded Dashboard block order
  - Calendar block's new neighbors (blocks immediately before and after) match the expected placement after the move
  - No duplicate Calendar block exists and Edit mode remains enabled

**Expected Change**: The Calendar block's position in the dashboard block order has changed from the previously recorded original position to the specified new position and this new position persists after a page refresh.

---

### [TC-016] Enter invalid format in Email address and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <invalid email format> in the Email address field
2. 2. Ensure other required fields contain <valid values>
3. 3. Click the Update profile button

**Original Expected Result:** Email address field displays an inline validation error indicating the email format is invalid; form does not submit; profile is not saved; Edit_Profile_Form remains open

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - Calendar block is visible on the Dashboard
  - Calendar block shows its header and three-dot block action menu

**Post-Check**
- **Navigate To**: `User Dashboard (refresh the page to confirm persistence)`
- **Observe**:
  - Calendar block is not present on the Dashboard
  - No Calendar block header or block action menu is visible in any block column or region

**Expected Change**: The Calendar block has been removed from the student's Dashboard and remains absent after a full page refresh, indicating the deletion persisted.

---

### [TC-008] Open Browser sessions report from Reports card
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Browser sessions link in the Reports card

**Original Expected Result:** opens Browser_sessions — The Browser sessions report is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - QA Automation 101 course card is present in the course list
  - QA Automation 101 does not show a Starred indicator/icon
  - QA Automation 101 is not the first (top) course card in the current sort/filter order

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - QA Automation 101 course card appears as the first (top) course card in the list
  - QA Automation 101 displays a Starred indicator/icon on its card
  - When applying the Starred filter, QA Automation 101 is listed in the Starred results
  - After performing a full page refresh, QA Automation 101 remains starred and stays at the top position

**Expected Change**: The QA Automation 101 course card is pinned to the top of My Courses and displays the Starred indicator; this pinned/starred state persists after a page refresh.

---

### [TC-009] Open Grades overview from Reports card
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Grades overview link in the Reports card

**Original Expected Result:** opens Grades_overview — The Grades overview page is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses (All/default filter)`
- **Observe**:
  - 'QA Automation 101' course card is present in the All/default list
  - 'QA Automation 101' is not listed under the Hidden filter (confirm by switching to Hidden filter)

**Post-Check**
- **Navigate To**: `My Courses -> Hidden filter (then optionally switch back to All/default)`
- **Observe**:
  - 'QA Automation 101' course card is present in the Hidden list
  - 'QA Automation 101' is absent from the All/default list after the action
  - Clicking the 'QA Automation 101' card in Hidden opens the course page and the Course, Participants, Grades, and Activities tabs render

**Expected Change**: The 'QA Automation 101' course card is removed from the All/default My Courses view and appears under the Hidden filter; the student can still open the hidden course page, indicating the user remains enrolled and access is preserved.

---

### [TC-005] Browser Back navigation after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

**Original Expected Result:** Pressing Back is blocked from restoring protected content: the protected page is not returned to. The user remains unauthenticated and the login page (login form) is shown (either the browser stays on the login page or the protected page immediately redirects back to the login page).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page -> Sections list for 'QA Automation 101'`
- **Observe**:
  - No section contains an item named '<valid name>'
  - 'Add Row' (or equivalent course edit/add controls) is visible, indicating the current user has editing permission

**Post-Check**
- **Navigate To**: `Course Page -> Sections list for 'QA Automation 101' (after saving the new section and performing a full page refresh)`
- **Observe**:
  - Sections list contains a new section row that includes an item named '<valid name>'
  - The new section is expanded (its content is visible), indicating the 'Collapsed' checkbox was unchecked
  - The item named '<valid name>' is rendered as an activity/resource entry (clickable link or named row) within that new section

**Expected Change**: A new section row is persisted in the Course Page Sections list and contains an item with the exact name '<valid name>'; the section is expanded (not collapsed) and both the section and its item remain present after a full page refresh.

---

### [TC-002] Attempt to use Log out when not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page (or a page that would normally show the Log out control)
2. 2. Verify whether a 'Log out' button is present in the UI
3. 3. Navigate directly to the logout endpoint (e.g., click a /logout link or enter the logout URL)

**Original Expected Result:** Precondition enforced: The 'Log out' control is not available to unauthenticated users (the Log out button is not visible). Navigating directly to the logout endpoint redirects to the Login page and displays the Login form; no logout success action is performed because there was no active session (session remains unauthenticated). Protected content is not accessible without authentication.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for 'Essay Draft' -> Submission status / Submission summary`
- **Observe**:
  - submission status is not 'Submitted for grading' (e.g., shows 'No submission' or 'Draft')
  - submission preview does not contain the online text '<online text>'
  - no uploaded file entry named '<uploaded file>' is present in the submission summary

**Post-Check**
- **Navigate To**: `Assignment page for 'Essay Draft' -> Submission summary (refresh the page to verify persistence)`
- **Observe**:
  - submission status is 'Submitted for grading'
  - submission preview displays the entered online text '<online text>' (visible in the preview area or submission confirmation)
  - uploaded file '<uploaded file>' appears in the submission file list as a downloadable link

**Expected Change**: The Assignment submission status changes to 'Submitted for grading', the submission preview contains the entered online text '<online text>', and the uploaded file named '<uploaded file>' is present as a downloadable entry in the submission summary; these items persist after a page refresh.

---

### [TC-003] After logging out, accessing a protected page is blocked (requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. After being redirected to the Login page, attempt to navigate to a protected page URL (e.g., open <protected page URL>)

**Original Expected Result:** Logout is enforced and access is blocked: After clicking 'Log out' the user is redirected to the Login page. When attempting to open <protected page URL>, the system redirects to the Login page and does not display protected content (the Login form is shown). The session state remains Unauthenticated and protected resources require re-authentication.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course 'QA Automation 101' -> Assignment 'Essay Draft' (Submission section)`
- **Observe**:
  - Submission status is not 'Submitted for grading' (e.g., shows 'No submission' or 'Draft')
  - Submission summary does not contain the online text to be submitted
  - No files are listed in the submission files/attachments area

**Post-Check**
- **Navigate To**: `Course 'QA Automation 101' -> Assignment 'Essay Draft' (Submission section) — refresh page or reopen assignment to confirm persistence`
- **Observe**:
  - Submission status row displays 'Submitted for grading'
  - Submission summary displays the exact online text that was entered during the test
  - No file attachments are listed in the submission files/attachments area
  - Submission timestamp or 'last modified' reflects the recent submission action (optional but recommended)

**Expected Change**: After submitting the online text, the assignment's submission state is persisted: the Submission status reads 'Submitted for grading', the submitted online text appears in the submission summary, and there are no file attachments listed.

---

### [TC-004] Double-click / rapid repeat of Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Immediately click the "Log out" button again (second click occurs before the app finishes redirecting)

**Original Expected Result:** First click succeeds: the current authenticated session is terminated and the user is redirected to the login page with the login form visible. The second click is blocked / has no additional effect: no duplicate session termination occurs, no duplicate redirects occur, and no error is shown to the user; the login page remains visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page -> Essay Draft (Submission details area)`
- **Observe**:
  - File upload area is visible and accepts file attachments
  - Online text editor / online text preview area is not present (assignment_allows_online_text == false)
  - Submission summary does not list the file named <uploaded file>
  - Submission status row does not show 'Submitted for grading' (e.g., shows 'No submission' or 'Draft')

**Post-Check**
- **Navigate To**: `Assignment page -> Essay Draft (after submitting and refreshing the page)`
- **Observe**:
  - Submission status row shows 'Submitted for grading'
  - Submission summary lists the uploaded file with the filename <uploaded file> as a downloadable link
  - No online text preview or online text content is shown in the submission summary or preview area

**Expected Change**: After uploading the file and clicking Submit, the assignment's submission status updates to 'Submitted for grading' and the submission summary persistently includes the uploaded file named <uploaded file>; there is no online text content displayed.

---

### [TC-005] Browser Back navigation after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

**Original Expected Result:** Pressing Back is blocked from restoring protected content: the protected page is not returned to. The user remains unauthenticated and the login page (login form) is shown (either the browser stays on the login page or the protected page immediately redirects back to the login page).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for 'Essay Draft' (before submitting)`
- **Observe**:
  - 'Add submission' button is visible
  - Submission status is not 'Submitted for grading' (e.g., shows 'No submission' or 'Not submitted')
  - Submission summary shows no uploaded files and no online text preview

**Post-Check**
- **Navigate To**: `Assignment page for 'Essay Draft' (refresh the page or reopen after clicking Submit)`
- **Observe**:
  - Submission status row shows 'Submitted for grading'
  - Submission summary shows no uploaded files (no file links are listed)
  - Submission preview area shows no online text content/preview

**Expected Change**: The submission record for student1 now exists and the Submission status changed from not-submitted to 'Submitted for grading' while the persisted submission contains no uploaded files and no online-text content.

---

### [TC-005] Browser Back navigation after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

**Original Expected Result:** Pressing Back is blocked from restoring protected content: the protected page is not returned to. The user remains unauthenticated and the login page (login form) is shown (either the browser stays on the login page or the protected page immediately redirects back to the login page).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course -> Activities tab`
- **Observe**:
  - No Additional Activity Type section exists for the to-be-created row (no section header or table for the new Additional Activity Type)
  - No activity row with the name '<new activity>' is present in any activity group or table

**Post-Check**
- **Navigate To**: `Course -> Activities tab (refresh the page to confirm persistence)`
- **Observe**:
  - A new 'Additional Activity Type' section header is present with the created row listed under it
  - The new Additional Activity Type section is expanded and shows a table row for the activity named '<new activity>'
  - The activity name '<new activity>' is a clickable link
  - After clicking the '<new activity>' link, the browser navigates to the activity page whose title/header or main heading equals '<new activity>' or clearly identifies the opened activity

**Expected Change**: A new Additional Activity Type section containing an activity row named '<new activity>' appears in the Activities list; the activity row is expandable, the activity name is a clickable link, and clicking it navigates to the activity page showing the activity title '<new activity>'. The new section and activity remain present after a page refresh, proving persistence.

---

### [TC-011] Update profile: edit General fields and save
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Edit profile' link on the User Details card to open the Edit Profile form
2. 2. In the 'General' panel enter <First name> in First_name
3. 3. Enter <Last name> in Last_name
4. 4. Enter <valid email> in Email_address
5. 5. Select <Email visibility> from Email_visibility
6. 6. Select <Country> from Country
7. 7. Select <Timezone> from Timezone
8. 8. Enter <description> in Description
9. 9. Click the 'Update profile' button

**Original Expected Result:** saves profile and returns to Profile page — The Profile page is displayed and the User Details card shows the updated name as <First name> <Last name>, Email address as <valid email>, and Timezone as <Timezone>

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile page -> User Details card`
- **Observe**:
  - Full name displayed (note current value before change)
  - Email address displayed (note current value before change)
  - Timezone displayed (note current value before change)
  - 'Edit profile' link/button is visible

**Post-Check**
- **Navigate To**: `Profile page -> User Details card (after clicking 'Update profile' and refreshing the page)`
- **Observe**:
  - Full name equals '<First name> <Last name>'
  - Email address equals '<valid email>'
  - Timezone equals '<Timezone>'
  - Description contains '<description>'
  - User is returned to the Profile page after saving (Profile page is displayed)

**Expected Change**: The User Details card displays the updated full name as '<First name> <Last name>', the Email address as '<valid email>', the Timezone as '<Timezone>', and the Description contains '<description>'; these updated values persist after a page refresh and the application returns to the Profile page after saving.

---

### [TC-001] Click Log out terminates session and returns to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Locate the 'Log out' button in the application header or navigation
2. 2. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page. The Login page is displayed with the authentication form (prompting for credentials) — the authenticated area is no longer visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (while authenticated as student1)`
- **Observe**:
  - Personalized greeting visible (e.g., 'Welcome, student1' or student initials/name)
  - User menu contains 'Log out' option
  - Protected dashboard content is rendered (e.g., course card for 'QA Automation 101')

**Post-Check**
- **Navigate To**: `Attempt to open Dashboard URL / refresh the Dashboard after clicking 'Log out'`
- **Observe**:
  - Login page is displayed with Username and Password input fields and a 'Log in' button
  - No authenticated dashboard content is visible (course cards, personalized greeting absent)
  - Authenticated user menu and 'Log out' option are not rendered

**Expected Change**: The authenticated session is terminated: after clicking 'Log out', attempts to view the Dashboard (or refreshing the protected page) redirect to the Login page and show the authentication form; protected content and authenticated user controls are no longer accessible.

---
