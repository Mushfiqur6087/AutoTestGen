# Post-Verification Specifications

### [TC-003] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. After being redirected to the Login page, attempt to navigate to a protected page URL (e.g., open <protected page URL>)

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (with Edit mode enabled)`
- **Observe**:
  - Edit mode toggle is ON and 'Reset page to default' button is visible at top right
  - Current list and order of dashboard blocks (capture names and positions), e.g., [Block 1: Timeline, Block 2: Calendar, Block 3: <custom block A>, ...]
  - Presence of any custom-added blocks or layout changes (e.g., additional blocks, moved blocks, hidden default blocks)
  - Presence of block move icons and three-dot options menu on each block

**Post-Check**
- **Navigate To**: `Dashboard (still in Edit mode or reload Dashboard if Edit mode auto-toggles)`
- **Observe**:
  - Edit mode toggle state and visibility of 'Reset page to default' button
  - List and order of dashboard blocks (capture names and positions), specifically check for Timeline and Calendar blocks
  - Absence of previously observed custom-added blocks or user-added placements
  - Default block controls present (move icon and options) for default blocks only

**Expected Change**: Dashboard layout reverted to the default configuration: default blocks (Timeline and Calendar) are present in their default positions; any custom-added blocks or non-default block placements observed in the pre-check are no longer present; block order matches the platform's default Dashboard layout for the user.

---

### [TC-004] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Immediately click the "Log out" button again (second click occurs before the app finishes redirecting)

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Dashboard block order (left-to-right, top-to-bottom)
  - position/index of Timeline block (column and row or ordinal index)
  - presence of Timeline block title 'Timeline' and its move handle

**Post-Check**
- **Navigate To**: `Dashboard (Edit mode enabled) — after performing the move and after a page reload or navigating away and back`
- **Observe**:
  - Dashboard block order (left-to-right, top-to-bottom)
  - position/index of Timeline block (column and row or ordinal index)
  - presence of Timeline block title 'Timeline' and its move handle

**Expected Change**: The Timeline block's position/index matches the <new position> specified in the test steps (its ordinal location in the Dashboard block order has changed from the pre-check). The Timeline block is shown in the new location and this new position persists after a page reload or after navigating away from and back to the Dashboard.

---

### [TC-006] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. In Tab A, click the "Log out" button
2. 2. In Tab B, immediately reload the protected page or click a protected-action button (perform the action) without re-authenticating

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - current layout of dashboard blocks (identify columns and rows)
  - position/index of the Timeline block (e.g., Column X, Row Y or index N from top-left)
  - state of Edit mode toggle (should be enabled)

**Post-Check**
- **Navigate To**: `Dashboard after performing the move → then reload the page and/or navigate away (e.g., Home) and return to Dashboard`
- **Observe**:
  - position/index of the Timeline block (Column/Row or index as recorded in pre_check)
  - order of other blocks in the same column(s)
  - Edit mode toggle state after navigation/reload

**Expected Change**: The Timeline block's position/index has changed from the pre_check value to the new position specified during the move action (<new position>); this new position remains after a full page reload and after navigating away and returning to the Dashboard (i.e., the layout change is persisted for the current user).

---

### [TC-007] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. After redirect to the login page, enter the URL of a protected page in the browser address bar and press Enter

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Timeline block is present in the dashboard blocks area
  - Timeline block three-dot menu is visible

**Post-Check**
- **Navigate To**: `Dashboard (reload page; verify with Edit mode enabled and then disabled)`
- **Observe**:
  - Timeline block is NOT present in the dashboard blocks area
  - No Timeline widget or Timeline block placeholder appears in the previous Timeline block position
  - Other dashboard blocks and edit controls render normally (confirming page loaded correctly)

**Expected Change**: The Timeline block has been removed from the Dashboard and remains absent after reloading the page and after toggling Edit mode off and on.

---

### [TC-013] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. On <user B>'s Profile page, locate the Edit profile link
2. 2. Click the Edit profile link

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - current column and order/index of the Calendar block (e.g., left/center/right column and ordinal position within column)
  - current column and order/index of the Timeline block
  - presence of the Calendar block move handle (drag handle) and Edit mode toggle state

**Post-Check**
- **Navigate To**: `Dashboard (after page refresh, Edit mode enabled)`
- **Observe**:
  - column and order/index of the Calendar block
  - column and order/index of the Timeline block
  - presence of the Calendar block move handle

**Expected Change**: The Calendar block's column and order/index have changed from the pre-check values to the target <new position>; the Calendar block is visible in the new location on the dashboard and the layout change persists after a page refresh (other blocks' positions updated accordingly).

---

### [TC-015] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Clear the First name field (leave it blank)
2. 2. Enter <valid last name> in Last name
3. 3. Enter <valid email> in Email address
4. 4. Click the Update profile button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - column and row index of the Calendar block (e.g., Column 1, Row 2)
  - order/sequence of blocks in each dashboard column

**Post-Check**
- **Navigate To**: `Dashboard (after performing the move, then reload the page or navigate away and return)`
- **Observe**:
  - column and row index of the Calendar block (expected new position)
  - order/sequence of blocks in each dashboard column

**Expected Change**: The Calendar block's column and row index has changed from the pre_check value to the new position chosen during the move action, and this new position persists after a page reload or navigating away and back (i.e., the dashboard block order reflects the moved Calendar block).

---

### [TC-016] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Enter <invalid email format> in the Email address field
2. 2. Ensure other required fields contain <valid values>
3. 3. Click the Update profile button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Calendar block is present in the dashboard blocks area
  - Calendar block header shows current month and contains 'New event' button and month navigation arrows

**Post-Check**
- **Navigate To**: `Dashboard (reload the page or navigate to another page and return to Dashboard)`
- **Observe**:
  - Calendar block is not present in the dashboard blocks area
  - No Calendar block header, 'New event' button, or month navigation arrows are visible where the Calendar block previously appeared

**Expected Change**: The Calendar block is no longer present on the Dashboard after deletion; the absence persists after a page reload or navigating away and back, confirming the change was persisted.

---

### [TC-008] Unknown Title
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the Browser sessions link in the Reports card

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - verify at least two course cards are visible in the grid
  - record the current position/index of the <target course> card (e.g., position X from top)
  - verify the <target course> card does NOT display the Starred indicator (star icon not filled)
  - optionally record the identities (name or id) of the top 3 course cards

**Post-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - position/index of the <target course> card
  - Starred indicator on the <target course> card (star icon filled/marked)
  - identities (name or id) of the top 3 course cards
  - total count of course cards in the grid

**Expected Change**: The <target course> card is now at the top (position 1) of the My Courses grid and displays the Starred indicator; the total number of courses is unchanged; any course(s) previously above the target course are now listed below it.

---

### [TC-009] Unknown Title
**Category**: `positive` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the Grades overview link in the Reports card

---

#### Verification Plan

**Actor A (Role: `course participant (student or teacher)`)**
- **Action**: Execute the steps from the core test case: on My Courses page, open the three-dot menu for <target course> and select 'Remove from view'.

**Actor B (Role: `teacher (course instructor) or course manager`)**
- **Session**: `new_session`
- **Navigate To**: `Course page for <target course> -> Participants page (Participants Management view)`
- **Action**: 
- **Observe**:
  - Participants table rows
  - Row for the user who performed 'Remove from view' (by name or username)
  - Status/Role column for that row

**Expected Change**: The user who removed the course from view is still listed in the Participants table with an enrolled role/status (i.e., the user remains enrolled and is not absent), proving the action did not unenrol the user.

---

### [TC-005] Unknown Title
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case: open the Course page in Edit mode, click Add Row to create a new section row, inside that section click Add Row to create a new item, enter a valid name in the Name field for the new item, and ensure the section's 'Collapsed' checkbox is unchecked so the item is visible.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course page -> Course content (main course view, not Edit mode)`
- **Action**: 
- **Observe**:
  - the list of sections (section headers and their contained items)
  - presence of an item with name '<valid name>' inside one of the sections
  - that the new section is expanded so the item '<valid name>' is visible (not hidden under a collapsed header)

**Expected Change**: A new section row is present in the course content and contains an item with the name '<valid name>'; the item is visible in the section because the section is not collapsed.

---

### [TC-002] Unknown Title
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Open the application home page (or a page that would normally show the Log out control)
2. 2. Verify whether a 'Log out' button is present in the UI
3. 3. Navigate directly to the logout endpoint (e.g., click a /logout link or enter the logout URL)

---

#### Verification Plan

**Actor A (Role: `student`)**
- **Action**: Execute the steps from the core test case (open Add submission, enter online text, upload a valid file, click Submit).

**Actor B (Role: `teacher`)**
- **Session**: `new_session`
- **Navigate To**: `Course -> Assignment page -> Submissions tab (Assignment Submissions view)`
- **Action**: 
- **Observe**:
  - row for the student (name/initials) in the Submissions table
  - Submission status column for that row
  - Grading status column for that row
  - Submission date/time column for that row
  - Online text preview (or Online text preview column/cell) for that row
  - File submission column showing uploaded filename(s) and download links
  - Grading summary panel values (Number of participants, Number of submissions, Needs grading)

**Expected Change**: A submission record exists for the student with Submission status 'Submitted for grading', Grading status 'Not graded', a submission date/time corresponding to the action, the entered online text visible in the online text preview, the uploaded file listed with the correct filename and an accessible download link, and the Grading summary reflecting the new submission (Number of submissions incremented).

---

### [TC-003] Unknown Title
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. After being redirected to the Login page, attempt to navigate to a protected page URL (e.g., open <protected page URL>)

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page for the assignment under test`
- **Observe**:
  - Submission status row (e.g., 'No submissions have been made yet' or similar)
  - Submission summary: online text preview (should be empty or not present)
  - Submission summary: list of file attachments (should be empty)

**Post-Check**
- **Navigate To**: `Assignment page for the assignment under test`
- **Observe**:
  - Submission status row text
  - Submission summary: online text preview content
  - Submission summary: list of file attachments

**Expected Change**: Submission status row shows 'Submitted for grading'; the submission summary displays an online text preview that exactly matches the submitted <online text>; there are no file attachments listed in the submission summary.

---

### [TC-004] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Immediately click the "Log out" button again (second click occurs before the app finishes redirecting)

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page -> Submission status section`
- **Observe**:
  - Submission status row (e.g., 'No submissions have been made yet' or current status)
  - Submission summary uploaded files list (expected empty)
  - Online text preview area (expected absent or empty)
  - Last modified field (timestamp of last change, if any)

**Post-Check**
- **Navigate To**: `Assignment page -> Submission status section (refresh page or navigate away and return)`
- **Observe**:
  - Submission status row
  - Submission summary uploaded files list
  - Online text preview area
  - Last modified field

**Expected Change**: Submission status row shows 'Submitted for grading'; Submission summary lists the uploaded file <uploaded file>; Online text preview is absent or empty (no online text present); Last modified timestamp updated to reflect the new submission.

---

### [TC-005] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment page -> Submission status section`
- **Observe**:
  - Submission status (e.g. 'No submissions have been made yet' or 'No submission')
  - Grading status
  - Uploaded files list (should be empty)
  - Online text preview (should be absent)
  - Last modified (may be empty or show previous timestamp)

**Post-Check**
- **Navigate To**: `Assignment page -> Submission status section`
- **Observe**:
  - Submission status
  - Grading status
  - Uploaded files list
  - Online text preview
  - Last modified timestamp

**Expected Change**: Submission status shows 'Submitted for grading'; uploaded files list remains empty and no online text preview is present; grading status reflects that the submission is not yet graded (e.g. 'Not graded'); Last modified timestamp is updated to the time of this submission.

---

### [TC-005] Unknown Title
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Click the "Log out" button
2. 2. Wait for redirect to the login page (login form visible)
3. 3. Press the browser Back button once

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course -> Activities page`
- **Observe**:
  - count of 'Additional Activity Type' rows
  - presence/absence of activity with name '<new activity>' in any Additional Activity Type row

**Post-Check**
- **Navigate To**: `Course -> Activities page`
- **Observe**:
  - count of 'Additional Activity Type' rows
  - presence of activity link with name '<new activity>' in a new Additional Activity Type row
  - expanded/collapsed state of the new Additional Activity Type row
  - on clicking the '<new activity>' link, the activity page loads (page heading matches activity name or activity-type specific heading)

**Expected Change**: The number of 'Additional Activity Type' rows has increased by one; a row containing an activity link named '<new activity>' is present. Expanding that row reveals the activity link, and clicking the link navigates to the activity's page (activity page heading or URL indicates the newly created activity).

---

### [TC-011] Unknown Title
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

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

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile page -> User Details card`
- **Observe**:
  - Full name (First and Last name)
  - Email address
  - Email visibility
  - Country
  - Timezone
  - Description

**Post-Check**
- **Navigate To**: `Profile page -> User Details card`
- **Observe**:
  - Full name (First and Last name)
  - Email address
  - Email visibility
  - Country
  - Timezone
  - Description

**Expected Change**: Full name is updated to '<First name> <Last name>'; Email address is updated to '<valid email>'; Email visibility is set to '<Email visibility>'; Country is set to '<Country>'; Timezone is set to '<Timezone>'; Description is updated to '<description>'. The Profile page is displayed after saving and shows these persisted values.

---

### [TC-001] Unknown Title
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Test Case Description:**
> No description available.

**Original Steps:**
1. 1. Locate the 'Log out' button in the application header or navigation
2. 2. Click the 'Log out' button

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (protected authenticated area)`
- **Observe**:
  - user initials / user menu visible in header
  - personalized greeting on Dashboard
  - Timeline block present
  - Calendar block present

**Post-Check**
- **Navigate To**: `Attempt to access Dashboard (same browser session) or reload protected URL after clicking 'Log out'`
- **Observe**:
  - Login page authentication form visible (Username and Password fields and Log in button)
  - no user initials / user menu visible in header
  - protected Dashboard content (personalized greeting, Timeline, Calendar) not visible
  - browser URL indicates Login page (not Dashboard)

**Expected Change**: After clicking 'Log out', attempts to access a protected page (Dashboard) redirect to the Login page showing the authentication form; personalized/protected UI elements (user initials/menu, Dashboard greeting, Timeline/Calendar) are no longer visible, demonstrating the authenticated session was terminated and re-authentication is required.

---
