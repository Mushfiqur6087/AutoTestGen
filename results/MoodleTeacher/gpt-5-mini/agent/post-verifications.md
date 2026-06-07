# Post-Verification Specifications

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (with Edit mode enabled)`
- **Observe**:
  - Edit mode is enabled
  - Dashboard shows a user-customized layout (for example: a user-added block titled 'Latest announcements' or one or more blocks placed in non-default positions)
  - The current block order differs from the known default arrangement for this user

**Post-Check**
- **Navigate To**: `Dashboard (refresh the page after clicking 'Reset page to default')`
- **Observe**:
  - Dashboard displays the system default block arrangement/order for the teacher
  - Any user-added blocks that were not part of the default layout are removed or returned to their default positions (e.g., 'Latest announcements' no longer appears as a custom-added block or appears in its default location)
  - The default layout remains the same after a full page reload

**Expected Change**: The user's Dashboard layout is reverted to the system default: customizations (added blocks or moved blocks) are removed or restored to default positions and the default block order is persisted across page reloads.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - 'Comments' block is not present on the Dashboard
  - Edit mode controls are visible (e.g. '+ Add a block' button, block move icons, block menus)

**Post-Check**
- **Navigate To**: `Dashboard (after closing Add Block page) -> Refresh the page`
- **Observe**:
  - 'Comments' block is present in the teacher's Dashboard layout
  - The block title reads 'Comments' and the block shows normal block controls (move/configure) while in Edit mode
  - The Add Block page/modal is closed and no add-block dialog is visible

**Expected Change**: A new 'Comments' block is created in the teacher's Dashboard layout (previously absent) and remains visible and intact after a full page refresh; the Add Block page is closed.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (teacher) with Edit mode enabled`
- **Observe**:
  - 'Course overview' block is not present on the Dashboard

**Post-Check**
- **Navigate To**: `Dashboard (teacher)`
- **Observe**:
  - 'Course overview' block is present on the Dashboard
  - Add a block page/modal is closed (no add-block UI visible)
  - Block-specific controls (move, configure, delete) are visible on the 'Course overview' block
  - Layout persists after a full page refresh and the 'Course overview' block remains visible

**Expected Change**: A new 'Course overview' block is added to the teacher's Dashboard, the Add a block page/modal is closed, and the block remains present (with authoring controls) after refreshing the page.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (teacher view) with Edit mode enabled`
- **Observe**:
  - The 'Add a block' control is visible
  - The 'Latest announcements' block is NOT present on the Dashboard

**Post-Check**
- **Navigate To**: `Dashboard (teacher view) — close Add Block page if open and refresh the page`
- **Observe**:
  - The 'Latest announcements' block is present on the Dashboard
  - The block displays the title 'Latest announcements'
  - Block-level controls (move/configure/delete) are visible when Edit mode is enabled
  - After a full page refresh the 'Latest announcements' block remains present in the layout

**Expected Change**: A new 'Latest announcements' block is added to the teacher's Dashboard layout, the Add Block page is closed, and the block remains visible and persisted after refreshing the Dashboard.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (teacher1)`
- **Observe**:
  - Dashboard does not contain a 'Latest badges' block
  - Add a block page/modal is not open

**Post-Check**
- **Navigate To**: `User Dashboard (teacher1) — refresh the page if needed`
- **Observe**:
  - Dashboard contains a 'Latest badges' block (block title or header reads 'Latest badges')
  - Block action menu (configure/move/delete) and move handle icons are present on the new block
  - Add a block page/modal is closed and no add-block overlay is visible

**Expected Change**: A 'Latest badges' block is created in the teacher's Dashboard layout, is visible with its title and authoring controls, the Add Block page/modal is closed, and the block placement persists after a full page refresh.

---

### [TC-009] Enter an invalid email format and attempt to save
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <invalid email format> into the Email_Address field
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating the value is not a valid email address; the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - Edit mode is enabled (Edit mode toggle is on)
  - '+ Add a block' control is visible
  - 'Learning plans' block is not present in the Dashboard block region
  - Add Block page/modal is not open

**Post-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - 'Learning plans' block is present in the Dashboard block region
  - Add Block page/modal is closed
  - Block shows expected title 'Learning plans' and standard block chrome (move/configure/delete icons) for the teacher
  - After browser refresh, 'Learning plans' block remains visible in the same Dashboard location

**Expected Change**: The 'Learning plans' block is added to the teacher's Dashboard layout and remains visible after a full page refresh; the Add Block page/modal is closed following the add action.

---

### [TC-010] Upload a file that violates site upload constraints and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attach <file violating site upload constraints> to the Picture_Upload control (via drag-and-drop or file picker)
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Enter <valid email address> into the Email_Address field
5. 5. Click the 'Update profile' button

**Original Expected Result:** Upload control displays an error indicating the file violates site upload constraints (e.g. file type or size invalid); the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (teacher view)`
- **Observe**:
  - Edit mode is enabled
  - + Add a block button is visible
  - 'Logged in user' block is not present in the dashboard block list/visual layout

**Post-Check**
- **Navigate To**: `Dashboard (teacher view) — refresh the page or navigate away and return`
- **Observe**:
  - 'Logged in user' block is present in the dashboard block list/visual layout
  - New block shows block chrome (title/header), move icons or block menu for configuration
  - Add Block page/modal is closed and no longer visible
  - 'Logged in user' block remains visible after a full page refresh

**Expected Change**: The 'Logged in user' block is added to the teacher's Dashboard layout, the Add Block page is closed, and the block persists after page refresh indicating the layout change was saved for the acting user.

---

### [TC-011] Unauthenticated user attempts to access Edit profile page
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Edit profile page URL while signed out

**Original Expected Result:** User is redirected to the login page (Edit profile page is not accessible); no profile edit controls are shown to the unauthenticated user

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (teacher1) with Edit mode enabled`
- **Observe**:
  - 'Mentees' block is not present on the Dashboard
  - Edit mode controls are visible
  - + Add a block button is visible

**Post-Check**
- **Navigate To**: `Dashboard (teacher1) — refresh the page; optionally toggle Edit mode off and on`
- **Observe**:
  - 'Mentees' block is present on the Dashboard
  - 'Mentees' block remains present after page refresh
  - Add a block page/modal is closed and normal Dashboard layout is visible

**Expected Change**: A new 'Mentees' block is added to the teacher's Dashboard layout, the Add Block page is closed, and the block persists after page refresh and edit-mode toggles.

---

### [TC-012] Upload file exactly at the site's maximum allowed upload size and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is exactly the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload and save succeeds; clicking 'Update profile' submits successfully, the profile page refreshes, and the new picture is visible on the profile page (picture replaced by the uploaded file).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode ON)`
- **Observe**:
  - Dashboard does not contain an 'Online users' block
  - '+ Add a block' button is visible and usable

**Post-Check**
- **Navigate To**: `Dashboard (after Add a block selection and after a full page refresh)`
- **Observe**:
  - An 'Online users' block is present on the Dashboard
  - 'Online users' block shows its title and expected UI (e.g., list or user count) indicating it rendered correctly
  - The Add Block page/modal is closed and no longer visible
  - After refreshing the page, the 'Online users' block remains present in the same location (layout persisted)

**Expected Change**: A new 'Online users' block has been added to the teacher's Dashboard layout (it was absent before); the Add Block page closed after selection, and the added block persists after a page reload.

---

### [TC-013] Upload file one unit over the site's maximum allowed upload size and attempt to save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is one unit over the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload is blocked / error shown; submission is blocked and an inline error is shown near the Picture_Upload field indicating the file exceeds the site's maximum allowed upload size, and the profile page does not refresh.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit Mode enabled)`
- **Observe**:
  - The Dashboard does not contain a block titled 'Private files'

**Post-Check**
- **Navigate To**: `Dashboard (close Add Block page if open, then refresh the page to confirm persistence)`
- **Observe**:
  - A block titled 'Private files' is present on the Dashboard
  - The added block shows block controls (menu or move icons) indicating it is persisted in the layout
  - The Add Block page or modal is closed

**Expected Change**: A 'Private files' block has been added to the teacher's Dashboard layout; the Add Block page is closed, the block is visible with block controls, and the block remains present after a full page refresh.

---

### [TC-014] Enter a very long string (200+ characters) into the Description rich text editor and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Place the cursor in the Description rich text editor
3. 3. Paste a continuous text block of 200+ characters into the Description editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Form submission proceeds; after clicking 'Update profile' the profile page refreshes. The saved Description either (a) displays the full long text on the profile detail page (accepted), or (b) displays a visibly truncated Description with an explicit truncation indicator/ellipsis or inline message indicating the Description was trimmed. Either outcome must be visible on the refreshed profile page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - Edit mode toggle is ON
  - 'Random glossary entry' block is not present on the Dashboard
  - Add a block page/modal is not open

**Post-Check**
- **Navigate To**: `User Dashboard (exit Add a block flow, refresh page)`
- **Observe**:
  - 'Random glossary entry' block is present on the Dashboard for the teacher
  - Add a block page/modal is closed
  - 'Random glossary entry' block remains visible after a full page refresh

**Expected Change**: A new 'Random glossary entry' block is added to the teacher's Dashboard, the Add a block page/modal is closed, and the block persists on the Dashboard after page refresh.

---

### [TC-015] Enter emoji and non-Latin Unicode characters into Description and First Name fields and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter emoji and non-Latin Unicode characters into the First_Name field
3. 3. Enter emoji and non-Latin Unicode characters into the Description rich text editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Unicode input handling visible; after clicking 'Update profile' the profile page refreshes. The saved values either appear exactly as entered (emoji and Unicode characters visible) or an inline validation error is shown indicating unsupported characters. The visible outcome must clearly show whether the characters were saved or rejected.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - The dashboard does not contain a block titled 'Recently accessed courses'
  - Add a block page is not currently open

**Post-Check**
- **Navigate To**: `User Dashboard (after adding block, refresh page, and toggle Edit mode off/on)`
- **Observe**:
  - Dashboard contains a block titled 'Recently accessed courses'
  - The block shows its block menu and move/drag icons (authoring controls) when Edit mode is enabled
  - After a full page refresh the 'Recently accessed courses' block remains visible
  - After toggling Edit mode off and returning to the Dashboard, the block remains visible for the teacher

**Expected Change**: A new dashboard block titled 'Recently accessed courses' is created on the teacher's Dashboard; it is visible immediately after creation and persists after a page refresh and after toggling Edit mode off, confirming the layout change was saved for the user.

---

### [TC-016] Enter leading and trailing whitespace in required First Name and Last Name and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter a value with leading and trailing spaces into the First_Name field
3. 3. Enter a value with leading and trailing spaces into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Whitespace trimming behavior visible; submission succeeds. On the refreshed profile page, the First and Last name values are shown without leading or trailing spaces (whitespace trimmed). If the system treats whitespace-only as empty, submission is blocked and an inline required-field error is shown for the affected field(s).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode)`
- **Observe**:
  - '+ Add a block' button is visible
  - 'Starred courses' block is not present on the Dashboard
  - Add Block page/modal is not open

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - 'Starred courses' block is visible on the Dashboard layout for the logged-in teacher
  - Add Block page/modal is closed after selection
  - After a full page refresh the 'Starred courses' block remains visible in the same teacher Dashboard

**Expected Change**: A new 'Starred courses' block is added to the teacher's Dashboard layout, the Add Block page/modal is closed after adding, and the new block persists after a full page refresh.

---

### [TC-017] Add an Additional Name, remove it, then save (repeating group add-then-remove all)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'Additional names' collapsible section
2. 2. Click to add a new item in Additional_Names_List
3. 3. Enter a value into the Alternative_Name field for the new item
4. 4. Remove the Additional_Names_List item just added
5. 5. Click the 'Update profile' button

**Original Expected Result:** Submission succeeds; because Additional_Names_List has min=0, the form submits successfully and the refreshed profile page shows no additional names entries (no residual empty/ghost entries).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - "+ Add a block" control is visible
  - "Tags" block is not present in the dashboard blocks/layout

**Post-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - "Tags" block is present in the dashboard layout for the logged-in teacher
  - Add a block page/modal is closed (no Add a block dialog visible)
  - "Tags" block remains visible after refreshing the Dashboard page

**Expected Change**: The Dashboard layout now includes a persistent 'Tags' block for the teacher; the Add a block page/modal is closed after selection and the 'Tags' block remains present after a page refresh.

---

### [TC-018] Immediately press browser Back after successful Update profile to check for duplicate or stale edit form behavior
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Update profile' button to save changes
2. 2. Wait for the profile page to refresh (successful save)
3. 3. Immediately press the browser Back button

**Original Expected Result:** No duplicate or unintended state; after pressing Back the browser either (a) shows the refreshed profile page (not the edit form), or (b) shows the edit form but with fields blank or reflecting the saved values (not causing a second save). No additional profile entities are created and only the single intended save exists.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (Edit mode enabled)`
- **Observe**:
  - Dashboard blocks do not include a 'Text' block
  - '+ Add a block' control is visible
  - Add Block page/modal is not open

**Post-Check**
- **Navigate To**: `User Dashboard (refresh the page to confirm persistence)`
- **Observe**:
  - Dashboard blocks contain a new 'Text' block visible in the layout
  - Add Block page/modal is closed and not visible
  - The 'Text' block remains visible after page refresh

**Expected Change**: A new 'Text' block has been added to the teacher's Dashboard layout, the Add Block page is closed, and the block's presence persists after a page refresh.

---

### [TC-019] Make multiple edits then click Cancel to ensure no changes are saved
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Change the First_Name field
3. 3. Change the Description rich text editor
4. 4. Click the 'Cancel' button

**Original Expected Result:** Cancel exits without saving; the profile page is shown (or user is navigated away) and the previously saved profile values remain unchanged (the changes made in the edit form are not persisted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode is ON)`
- **Observe**:
  - No 'Upcoming events' block is present on the dashboard
  - '+ Add a block' control is visible and Add Block page/modal is not open

**Post-Check**
- **Navigate To**: `Dashboard (stay on page, then perform a full page refresh)`
- **Observe**:
  - 'Upcoming events' block is visible in the dashboard layout immediately after adding
  - The Add Block page/modal is closed and not visible
  - 'Upcoming events' block remains visible after full page refresh (layout persisted)

**Expected Change**: An 'Upcoming events' block is added to the teacher's Dashboard layout, the Add a block page/modal is closed, and the block remains visible after a full page refresh indicating the layout change was persisted for the user.

---

### [TC-021] Confirm enrollment then immediately navigate back to attempt resubmission (avoid duplicate enrollment)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Enrol users button
2. 2. In User_Search, locate and select an existing user from the dialog results
3. 3. Open the Role dropdown
4. 4. Select a Role for the selected user
5. 5. Click Confirm enrollment
6. 6. After enrollment completes and the participants list updates, use the browser back button (navigate back to the previous page/state)
7. 7. If the enrolment dialog or form appears again, attempt to click Confirm enrollment a second time

**Original Expected Result:** Any attempt to create a duplicate enrollment is blocked; only one enrollment record for the selected user exists in the participants list. The second Confirm enrollment action is either disabled or results in a visible message preventing duplicate creation (no duplicate row appears in the participants table).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - capture the current blocks layout order (record block titles in visual order: top-to-bottom / left-to-right)
  - record the current index/position of <target block> within the captured layout

**Post-Check**
- **Navigate To**: `Dashboard (after performing the drag-and-drop and dropping <target block>)`
- **Observe**:
  - <target block> appears at the intended new position within the blocks layout (compare against the pre_check recorded order)
  - the overall blocks order reflects the drag-and-drop change (neighbouring blocks moved accordingly)
  - the new layout remains unchanged after a full page refresh and after toggling Edit mode off and on

**Expected Change**: The blocks layout order is updated so that <target block> is moved from its original recorded index to the new index; this updated order persists for the teacher after refresh and edit-mode toggles.

---

### [TC-023] Open bottom 'With selected users…' bulk actions dropdown with no users selected
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Scroll to the bottom bulk actions area
2. 2. Click the With selected users… dropdown

**Original Expected Result:** Bulk actions menu opens; available bulk action options are visible but actions that operate on selected participants are disabled until at least one participant is checked. The UI shows that no bulk action can be performed without selection (attempting to trigger a bulk action without selection is blocked or results in an inline prompt to select users).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - the block titled '<target block>' is present in the dashboard layout at its current position (record its column and ordinal position)
  - the ordered list of block titles in the affected column/region (e.g., ['Block A', '<target block>', 'Block B', ...]) is visible

**Post-Check**
- **Navigate To**: `Dashboard (refresh page and/or toggle Edit mode off then on)`
- **Observe**:
  - the block titled '<target block>' appears at the new position specified by the Move action (recorded column and ordinal position)
  - the ordered list of block titles in the affected column/region reflects the new ordering (e.g., ['Block A', 'Block B', '<target block>', ...])
  - move controls and block menus remain functional and the layout persists for the logged-in teacher after refresh

**Expected Change**: The block titled '<target block>' has moved from its previous position to the new position chosen via the Options -> Move action, and the new block ordering persists after a page refresh and when Edit mode is toggled.

---

### [TC-024] Course End Date one day before Course Start Date (enabled) — save blocked with inline error
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid Course Full Name> in the Course_Full_Name field
2. 2. Enter <valid Course Short Name> in the Course_Short_Name field
3. 3. Select <valid option> in the Course_Category dropdown
4. 4. Enter <date B> in the Course_Start_Date field
5. 5. Check the Enable_Course_End_Date checkbox
6. 6. Enter <date B minus 1 day> in the Course_End_Date field
7. 7. Click the Save and display button

**Original Expected Result:** Course_End_Date field displays an inline validation error indicating the end date must be on or after the Course_Start_Date and the save action is blocked (error shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - the specified target block is present on the Dashboard (e.g., 'Latest announcements')
  - the block's Options menu (containing 'Delete') is visible for that block

**Post-Check**
- **Navigate To**: `Dashboard (refresh the page; confirm Edit mode state both on and after toggling Edit mode off)`
- **Observe**:
  - the specified target block is not present on the Dashboard
  - no duplicate or ghost block with the same title appears
  - the Dashboard layout persists for the teacher (other blocks remain visible and in expected positions)

**Expected Change**: The specified target block has been removed from the teacher's Dashboard and remains absent after a full page refresh and after toggling Edit mode off, indicating the deletion persisted for the user.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - Layout dropdown shows the current layout selection (e.g., 'Card', 'List', or 'Summary')
  - Course listing is rendered according to the current layout (visual cues: card tiles vs. list rows vs. compact summary rows)

**Post-Check**
- **Navigate To**: `My Courses (after selecting layout and refreshing the page)`
- **Observe**:
  - Layout dropdown shows the newly selected layout option
  - Course listing is rendered using the newly selected layout (visual cues: card tiles when 'Card' selected; list rows when 'List' selected; compact summary rows when 'Summary' selected)
  - Layout persists after a full page refresh (the same dropdown selection and rendering remain)

**Expected Change**: The My Courses page renders the course listing using the selected layout option and the Layout dropdown reflects that selection; this layout choice persists after refreshing the My Courses page.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses -> All (default My Courses view)`
- **Observe**:
  - course card for 'QA Automation 101' is visible
  - the star icon on the 'QA Automation 101' course card is not active/filled
  - 'QA Automation 101' is not listed in My Courses -> Starred filter results

**Post-Check**
- **Navigate To**: `My Courses -> Starred filter, then My Courses -> All and refresh the page`
- **Observe**:
  - 'QA Automation 101' appears in the Starred filter results
  - the course card for 'QA Automation 101' shows an active/filled star icon
  - 'QA Automation 101' is pinned to the top position of the My Courses listing when viewing All
  - the Starred state (active star icon) and pinning remain after a full page refresh

**Expected Change**: The course 'QA Automation 101' is marked as Starred (star icon becomes active), is present in the Starred list, and is pinned to the top of the My Courses listing; this starred/pinned state persists after refreshing the page.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses (default view / All courses)`
- **Observe**:
  - the target course card (the course acted on in the core test steps) is present and visible in the course list
  - the target course is NOT present under the Hidden filter

**Post-Check**
- **Navigate To**: `My Courses -> Hidden filter (or select Hidden from status filter)`
- **Observe**:
  - the target course card appears in the Hidden list
  - the target course no longer appears in the default/All course list after refresh

**Expected Change**: The selected course is removed from the teacher's default course list and is listed under the Hidden filter for that teacher; the hidden state persists after a page refresh.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode is ON) - the course section to be renamed is visible`
- **Observe**:
  - Edit mode toggle shows 'On' or edit controls are present
  - inline edit icon (pencil) is visible for the target section
  - section header displays the current section name (not '<New section name>')

**Post-Check**
- **Navigate To**: `Course page -> Refresh the page (ensure a full reload) while Edit mode remains ON or after toggling Edit mode off and back on`
- **Observe**:
  - section header displays '<New section name>' for the renamed section
  - section retains its original position and contained activities/resources
  - inline edit icon remains present for the section (if Edit mode is ON) or the renamed title is visible to the teacher when Edit mode is re-enabled

**Expected Change**: The section header text has been updated to '<New section name>' and this renamed title persists after a full page refresh (the section remains in the same position and its contents are unchanged).

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `QA Automation 101 course page with Edit mode ON (Course content list visible)`
- **Observe**:
  - Record the exact title of the section to be duplicated (store as ORIGINAL_TITLE)
  - Record the current total number of sections (store as ORIGINAL_COUNT)
  - Confirm there is exactly one section row with the title ORIGINAL_TITLE

**Post-Check**
- **Navigate To**: `QA Automation 101 course page (refresh the page to confirm persistence)`
- **Observe**:
  - Section list contains an additional row whose title equals ORIGINAL_TITLE
  - Total number of sections equals ORIGINAL_COUNT + 1
  - The new section row is rendered in the course content list and is selectable/editable in Edit mode

**Expected Change**: A new section row is created that has the exact same title as the selected original section (ORIGINAL_TITLE); the total section count increases by one and the duplicate persists after a page reload.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Actor A (Role: `teacher (teacher1)`)**
- **Action**: Execute the core test case: open the Course page for QA Automation 101 in Edit mode, open the target section's action menu and select 'Hide'. After hiding, refresh the Course page and confirm the section shows a Hidden indicator (or other teacher-facing hidden visual state) in the teacher view.

**Actor B (Role: `student (student1)`)**
- **Session**: `new_session`
- **Navigate To**: `Course page -> QA Automation 101`
- **Action**: 
- **Observe**:
  - the hidden section is not present in the student's list of course sections (no section row or heading for the hidden section)
  - activities that were in the hidden section are not visible or accessible to the student (no activity links rendered)

**Expected Change**: After the teacher hides the section, the student view no longer shows the section or its contained activities; the section is absent or inaccessible to student1 while the teacher's refreshed view shows the section marked with a Hidden indicator.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON) -> Course content area`
- **Observe**:
  - The targeted section row is present (record the section title or section number/identifier before deletion)
  - Record the current number of sections listed in the course

**Post-Check**
- **Navigate To**: `Course page (Edit mode ON) -> Refresh the page (full reload) and inspect Course content area`
- **Observe**:
  - The previously recorded targeted section row (by title or section number/identifier) is no longer present in the sections list
  - The total number of sections is one less than the number recorded in pre_check

**Expected Change**: The targeted section (the same title/identifier noted in pre_check) has been removed from the course content list and the removal persists after a full page reload.

---

### [TC-009] Enter an invalid email format and attempt to save
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <invalid email format> into the Email_Address field
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating the value is not a valid email address; the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON) for the target course (e.g., QA Automation 101)`
- **Observe**:
  - Locate the target activity row and record its current title as '<Original activity name>'
  - Verify the inline edit icon/control is visible for that activity

**Post-Check**
- **Navigate To**: `Course page for the same course -> Reload the page (hard refresh). Additionally, open the same activity's Settings page and open the Course Index/sidebar.`
- **Observe**:
  - The activity row displays the new title exactly as '<New activity name>'
  - The activity Settings page shows the Name field and page heading reflecting '<New activity name>'
  - Course Index/sidebar lists the activity with the title '<New activity name>'

**Expected Change**: The activity title has changed from the previously recorded '<Original activity name>' to '<New activity name>' and this new title persists after a page reload; it is consistently shown on the course page, in the Course Index/sidebar, and inside the activity's Settings page.

---

### [TC-012] Upload file exactly at the site's maximum allowed upload size and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The UI can verify that a new activity row was created and persisted, but Moodle may alter the duplicated activity title (for example appending 'copy' or similar). If the core test expects an identical title, that exact string match may not be verifiable purely via the standard course UI.*

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is exactly the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload and save succeeds; clicking 'Update profile' submits successfully, the profile page refreshes, and the new picture is visible on the profile page (picture replaced by the uploaded file).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page (Edit mode ON)`
- **Observe**:
  - the activity list includes exactly one row for the selected activity title (the original activity)
  - no other activity row exists with the same title or a 'copy' suffix

**Post-Check**
- **Navigate To**: `Course Page (refresh while Edit mode ON)`
- **Observe**:
  - the activity list contains an additional row representing the duplicated activity
  - the course section's activity count has increased by one
  - the duplicate activity appears in the same section as the original
  - the duplicate's title is either identical to the original title or contains a 'copy'/'(copy)' suffix

**Expected Change**: A new activity row is created for the duplicated activity in the same course section; the section's activity count increases by one and the duplicate row remains visible after page refresh.

---

### [TC-013] Upload file one unit over the site's maximum allowed upload size and attempt to save
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is one unit over the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload is blocked / error shown; submission is blocked and an inline error is shown near the Picture_Upload field indicating the file exceeds the site's maximum allowed upload size, and the profile page does not refresh.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the core test steps: on the course page with Edit mode ON, open the target activity's three-dot action menu and select 'Hide'. Refresh the course page and confirm the activity shows a hidden/restricted indicator in the teacher view.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `QA Automation 101 course page (student view)`
- **Action**: 
- **Observe**:
  - the hidden activity row/link is absent from the course content list
  - attempting to open the activity's direct URL shows an access-restricted message or a page indicating the activity is not available

**Expected Change**: The activity is not visible or accessible to students: it no longer appears in the student's course content listing and direct navigation to the activity yields an access-restricted or not-available message.

---

### [TC-015] Enter emoji and non-Latin Unicode characters into Description and First Name fields and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter emoji and non-Latin Unicode characters into the First_Name field
3. 3. Enter emoji and non-Latin Unicode characters into the Description rich text editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Unicode input handling visible; after clicking 'Update profile' the profile page refreshes. The saved values either appear exactly as entered (emoji and Unicode characters visible) or an inline validation error is shown indicating unsupported characters. The visible outcome must clearly show whether the characters were saved or rejected.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (the section containing the target activity) with Edit mode ON`
- **Observe**:
  - Edit mode controls are visible (Edit mode toggle is ON)
  - three-dot action menu (activity actions) is present for the target activity row
  - the activity row for the target activity is present in the section's activity list

**Post-Check**
- **Navigate To**: `Course page -> the same section (after confirming deletion and refreshing the page)`
- **Observe**:
  - the activity row for the previously deleted activity is NOT present in the section's activity list
  - Course Index/sidebar does not list the deleted activity
  - no action menu or links exist that navigate to the deleted activity

**Expected Change**: The selected activity is removed from the course section and course index. After confirming deletion and refreshing the course page, the activity row no longer appears and any links/menus that referenced it are absent (the section's activity count, if shown, reflects the removal).

---

### [TC-017] Add an Additional Name, remove it, then save (repeating group add-then-remove all)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'Additional names' collapsible section
2. 2. Click to add a new item in Additional_Names_List
3. 3. Enter a value into the Alternative_Name field for the new item
4. 4. Remove the Additional_Names_List item just added
5. 5. Click the 'Update profile' button

**Original Expected Result:** Submission succeeds; because Additional_Names_List has min=0, the form submits successfully and the refreshed profile page shows no additional names entries (no residual empty/ghost entries).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> parent section (where '+ Add a subsection' will be used)`
- **Observe**:
  - subsection rows directly under the parent section do not include the title '<Subsection_Title>'
  - current list of subsections under the parent section (baseline) is visible

**Post-Check**
- **Navigate To**: `Course page -> parent section (refresh the page after save)`
- **Observe**:
  - a new subsection row with the title '<Subsection_Title>' is present directly under the parent section
  - the new subsection row remains visible after a full page refresh

**Expected Change**: A new nested subsection with the entered title '<Subsection_Title>' is created under the selected parent section and persists after page refresh.

---

### [TC-018] Immediately press browser Back after successful Update profile to check for duplicate or stale edit form behavior
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Update profile' button to save changes
2. 2. Wait for the profile page to refresh (successful save)
3. 3. Immediately press the browser Back button

**Original Expected Result:** No duplicate or unintended state; after pressing Back the browser either (a) shows the refreshed profile page (not the edit form), or (b) shows the edit form but with fields blank or reflecting the saved values (not causing a second save). No additional profile entities are created and only the single intended save exists.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON)`
- **Observe**:
  - the section to be moved is present in the sections list and its current index/position is recorded (identify by the section title used in the test)
  - the section's Drag/Move handle is visible and actionable
  - the surrounding section order (titles and positions of neighboring sections) is noted for comparison

**Post-Check**
- **Navigate To**: `Course page (Edit mode ON) after performing the drag-and-drop and after a full page refresh`
- **Observe**:
  - the moved section now appears at the new index/position in the sections list (identified by the same section title)
  - neighboring sections have shifted positions consistently with the move
  - the Drag/Move handle remains visible on the moved section (indicating persisted authoring controls)

**Expected Change**: The target section is relocated to the new position in the course sections list and the new ordering persists after a page refresh; neighboring sections' positions have updated accordingly.

---

### [TC-019] Make multiple edits then click Cancel to ensure no changes are saved
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Change the First_Name field
3. 3. Change the Description rich text editor
4. 4. Click the 'Cancel' button

**Original Expected Result:** Cancel exits without saving; the profile page is shown (or user is navigated away) and the previously saved profile values remain unchanged (the changes made in the edit form are not persisted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON) — navigate to the section containing the activities you will target`
- **Observe**:
  - Record the exact titles of the targeted activities and their current ordinal positions within the section (e.g., position indices or visually adjacent items).
  - Record current visibility/status indicators for each targeted activity (e.g., presence/absence of hidden/visible badge or eye icon).
  - Confirm there are no existing duplicate copies of the targeted activity titles (so duplication can be detected).

**Post-Check**
- **Navigate To**: `Course page (Edit mode ON) — refresh the page and return to the same section(s) where the targeted activities were located`
- **Observe**:
  - Each previously recorded targeted activity title is present and shows the UI change corresponding to the applied bulk operation (for example: visibility badge now shows 'Hidden' if 'Hide' was applied).
  - If the bulk operation was a Move, the recorded activities appear in the destination section and in the expected new order; the source section no longer contains those items in their previous positions.
  - If the bulk operation was Duplicate, a new activity row exists for each duplicated item with a distinguishable copy marker in the title (e.g., 'copy') while the original remains.
  - No unexpected additional duplicates or missing activities are observed (except those expected from the chosen operation).
  - All observed changes persist after the page refresh.

**Expected Change**: The selected activities now visibly reflect the chosen bulk operation (visibility/status badges updated for Hide/Show, items relocated for Move, new duplicate rows created for Duplicate, etc.), and these changes persist after refreshing the Course page while Edit mode is on.

---

### [TC-022] First name alphabetical filter when no participants match the chosen initial
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the First name alphabet filter control
2. 2. Select the alphabet letter <chosen initial>

**Original Expected Result:** Filter selection succeeds; the participants table updates to show zero rows (an empty state is visible) indicating no participants match the selected initial. The UI reflects the active filter (the chosen letter is highlighted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode On) -> Click '+ Add an activity or resource' to open Activity Chooser modal`
- **Observe**:
  - Activity Chooser modal is open
  - Target tile to be toggled is visible in the chooser
  - Target tile's star/favorite icon current visual state is recorded (e.g. 'outlined' for not-favorited or 'filled' for favorited)

**Post-Check**
- **Navigate To**: `After toggling: Close Activity Chooser (if open) -> Reopen Course page (ensure Edit mode On) -> Click '+ Add an activity or resource' to open Activity Chooser modal again`
- **Observe**:
  - Activity Chooser modal is open
  - Target tile is visible in the chooser
  - Target tile's star/favorite icon shows the opposite visual state compared to the recorded pre-check state (e.g. previously 'outlined' now 'filled' or vice versa)

**Expected Change**: The target Activity Chooser tile's star/favorite state is inverted from the pre-check: the star icon visually reflects the toggled favorite state and the change persists when the Activity Chooser is closed and reopened.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> target section where the assignment will be created`
- **Observe**:
  - The course section does not contain an assignment with the Assignment Name used in the test (i.e., the new assignment is not already present)

**Post-Check**
- **Navigate To**: `Course page (QA Automation 101) -> the same section -> open the new assignment's Settings (Edit settings) page`
- **Observe**:
  - Course section contains an assignment row with the specified Assignment Name
  - Assignment settings panel shows 'File submissions' enabled
  - Maximum number of uploaded files equals the <integer> value entered during creation
  - Maximum submission size displays the <number> MB value entered during creation
  - Accepted file types field contains the <accepted file types> value entered
  - Group submission is enabled in assignment settings
  - 'Require all group members to submit' option is checked
  - Grouping selection shows the chosen <grouping>
  - Restrict access list includes an entry for the selected <restriction type>
  - Competencies/Linked competencies section includes the selected <competency type>
  - After a full page refresh, the assignment row and all above settings remain present and unchanged

**Expected Change**: A new Assignment with the specified Assignment Name is created in the selected course section and persisted. The assignment's submission settings reflect File submissions enabled, Maximum number of uploaded files set to the provided <integer>, Maximum submission size set to the provided <number> MB, Accepted file types set as entered; Group submissions is enabled with 'Require all group members to submit' checked and the selected <grouping> applied; the chosen <restriction type> appears in the Restrict access list; and the selected <competency type> is linked. All of these settings remain present after a page refresh.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> Course content / section where assignment will be created`
- **Observe**:
  - No activity or assignment row with the title '<assignment name>' is present in the selected section

**Post-Check**
- **Navigate To**: `New Assignment page -> Edit settings (open the assignment's settings from the assignment page)`
- **Observe**:
  - Assignment title equals '<assignment name>'
  - Submission types shows 'File submissions' enabled
  - Maximum number of uploaded files equals '<integer>'
  - Maximum submission size displays '<number> MB'
  - Accepted file types field contains '<accepted file types>'
  - Group submissions is enabled
  - Selected grouping equals '<grouping>' or the grouping name is visible in Group submission settings

**Expected Change**: A new assignment titled '<assignment name>' is created and its persisted settings show File submissions enabled, Maximum number of uploaded files = <integer>, Maximum submission size = <number> MB, Accepted file types = '<accepted file types>', and Group submissions enabled with the selected grouping '<grouping>'.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> target section where the assignment will be created`
- **Observe**:
  - assignment list does not contain the assignment with the test assignment name

**Post-Check**
- **Navigate To**: `Course page (QA Automation 101) -> locate the newly created assignment entry -> open the assignment Settings (or Edit settings) page`
- **Observe**:
  - assignment list contains an entry with the assignment name entered in the test
  - Assignment Settings - Submission types shows 'File submissions' enabled
  - Assignment Settings - Submission types shows 'Maximum number of uploaded files' equals the integer entered in the test
  - Assignment Settings - Submission types shows 'Maximum submission size' equals the MB value entered in the test
  - Assignment Settings - Submission types shows 'Accepted file types' contains the file type string entered in the test
  - Group submission settings shows 'Group submissions' is unchecked (disabled)

**Expected Change**: A new assignment with the specified assignment name is present on the course page. Opening its settings confirms File submissions are enabled, Group submissions is disabled, and the Maximum number of uploaded files, Maximum submission size (MB), and Accepted file types match the values entered during creation.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> the target section where the assignment will be created`
- **Observe**:
  - course section does not contain an activity titled '<assignment name>'
  - no existing assignment page for '<assignment name>' is accessible (optional: verify by attempting to open the assignment URL used by previous runs)

**Post-Check**
- **Navigate To**: `1) The assignment page opened by the Save and display action; 2) Course page (QA Automation 101) -> the same section (refresh the page)`
- **Observe**:
  - assignment page displays the title '<assignment name>' in the page heading
  - on the assignment page or in its Settings: 'File submissions' is enabled/checked
  - on the assignment settings: 'Maximum number of uploaded files' shows the value entered during creation
  - on the assignment settings: 'Maximum submission size' shows the MB value entered during creation
  - on the assignment settings: 'Accepted file types' contains the types entered during creation
  - 'Group submissions' toggle/option is unchecked/disabled for the assignment
  - the assignment appears as a row/item in the course section after a full page refresh

**Expected Change**: A new assignment titled '<assignment name>' is created in the selected course section and persists after refresh; its submission settings reflect that File submissions are enabled with the configured maximum number of uploaded files, maximum submission size, and accepted file types, and Group submissions remains disabled.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> target section where assignment will be created`
- **Observe**:
  - assignment list does not contain the assignment named <assignment name>
  - no assignment link or tile exists with the title <assignment name>

**Post-Check**
- **Navigate To**: `Course page (QA Automation 101) -> click the newly created assignment <assignment name> -> Edit settings (or Settings tab) for that assignment`
- **Observe**:
  - course page contains an entry/link titled <assignment name> in the expected section
  - assignment settings page shows Submission types section with 'File submissions' unchecked/disabled
  - assignment settings page shows Group submission enabled/checked
  - assignment settings page shows the selected grouping set to <grouping> (or the chosen grouping label is visible)

**Expected Change**: A new assignment titled <assignment name> is created in the course. Its persisted settings show that File submissions are disabled while Group submissions are enabled and the selected grouping is set to <grouping>.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> target section where the assignment will be added`
- **Observe**:
  - assignment list does not contain an entry with title '<assignment name>'
  - no existing assignment row shows Group submissions enabled for title '<assignment name>'

**Post-Check**
- **Navigate To**: `New Assignment page (the assignment view) and Course page -> same section (refresh if necessary)`
- **Observe**:
  - assignment page displays title '<assignment name>'
  - submission types/settings indicate File submissions is disabled/unchecked
  - submission settings indicate Group submissions is enabled/checked
  - grouping field shows the selected grouping '<grouping>' (or the grouping name is visible in the Group submission settings)
  - on the course section the new assignment '<assignment name>' appears in the activity list

**Expected Change**: A new assignment titled '<assignment name>' is created and persisted: its File submissions option is disabled, Group submissions is enabled with the selected grouping '<grouping>', and the assignment entry appears in the course section after refresh.

---

### [TC-010] Upload a file that violates site upload constraints and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attach <file violating site upload constraints> to the Picture_Upload control (via drag-and-drop or file picker)
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Enter <valid email address> into the Email_Address field
5. 5. Click the 'Update profile' button

**Original Expected Result:** Upload control displays an error indicating the file violates site upload constraints (e.g. file type or size invalid); the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page for 'QA Automation 101' (course content area / selected section)`
- **Observe**:
  - Assignment titled '<assignment name>' is NOT present in the course content

**Post-Check**
- **Navigate To**: `Course page for 'QA Automation 101' -> Open the assignment titled '<assignment name>' -> Click 'Edit settings' (or Settings tab) for that assignment`
- **Observe**:
  - Assignment titled '<assignment name>' is present in the selected course section
  - 'File submissions' option is unchecked/disabled in the Assignment settings (no file upload submission allowed)
  - 'Group submissions' is disabled / assignment configured as 'No groups' (not set to require group submissions)

**Expected Change**: A new assignment named '<assignment name>' exists on the course page and its persisted settings show File submissions disabled and Group submissions disabled.

---

### [TC-011] Unauthenticated user attempts to access Edit profile page
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Edit profile page URL while signed out

**Original Expected Result:** User is redirected to the login page (Edit profile page is not accessible); no profile edit controls are shown to the unauthenticated user

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (QA Automation 101) -> target section where the assignment will be created`
- **Observe**:
  - Course content does not contain an assignment with the title '<assignment name>'
  - No assignment link or card exists for '<assignment name>' in the section

**Post-Check**
- **Navigate To**: `Assignment page for '<assignment name>' (opened after Save and display) -> Edit settings (open the assignment configuration) and refresh both the assignment page and the parent Course page`
- **Observe**:
  - Assignment title equals '<assignment name>' on the assignment view header
  - Assignment appears in the course content listing in the expected section after page refresh
  - Submission types: Online text submissions control is present and enabled
  - File submissions checkbox/toggle is unchecked (File submissions OFF)
  - Group submissions setting is set to 'No groups' or the Group submissions checkbox/toggle is unchecked (Group submissions OFF)

**Expected Change**: A new assignment titled '<assignment name>' exists and is persisted: the assignment page is reachable, the assignment appears in the course content after refresh, File submissions remains disabled, and Group submissions remains disabled.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings (for the target course)`
- **Observe**:
  - Course Settings form is displayed and editable
  - Course Full Name input is present
  - Course Short Name input is present
  - Course Category dropdown is present
  - Enable Course end date checkbox control is present
  - Course Format dropdown is present
  - Group mode dropdown is present

**Post-Check**
- **Navigate To**: `Course Settings (reopen after 'Save and display')`
- **Observe**:
  - Course Full Name equals the entered <valid course full name>
  - Course Short Name equals the entered <valid course short name>
  - Course Category equals the selected <valid category>
  - Enable Course end date checkbox is unchecked (End Date disabled)
  - Course Format is set to 'Topics format'
  - Group mode is set to 'No groups'

**Expected Change**: The course settings persist the entered full/short names and category, the End Date toggle remains disabled, the Course Format is saved as Topics format, and the Group mode is saved as No groups; these values remain after saving and reopening the Course Settings.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page for the target course (QA Automation 101)`
- **Observe**:
  - Course Full Name field value (record current value before change)
  - Course Short Name field value (record current value before change)
  - Course Category selected value (record current value before change)
  - Enable Course end date checkbox state (should be unchecked as ensured by the test steps)
  - Course Format current selection (record current selection before change)
  - Groups Group Mode current selection (record current selection before change)
  - Groups Grouping dropdown visibility and selected value (if visible)

**Post-Check**
- **Navigate To**: `Course page (to confirm heading) and then Course Settings page (to confirm persisted settings)`
- **Observe**:
  - Course page heading displays the new Course Full Name entered in the test
  - Course Settings: Course Full Name field equals the new Course Full Name entered
  - Course Settings: Course Short Name field equals the new Course Short Name entered
  - Course Settings: Course Category equals the selected <valid category>
  - Course Settings: Enable Course end date checkbox is unchecked (End Date disabled)
  - Course Settings: Course Format is 'Topics format' and Layout controls for Topics are visible
  - Course Settings: Groups Group Mode is set to the chosen non-'No groups' option
  - Course Settings: Groups Grouping dropdown is visible and the chosen <valid grouping> is selected

**Expected Change**: After saving and returning to the course, the Course page heading shows the new Course Full Name and the Course Settings persist the provided configuration: End Date remains disabled, Format is set to Topics format (with Topics layout controls visible), Group Mode is the selected non-'No groups' option and the chosen Grouping remains selected, and the Course Short Name and Category reflect the submitted values.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page for QA Automation 101`
- **Observe**:
  - Course Full Name field value (record current value before change)
  - Course Short Name field value (record current value before change)
  - Course Category dropdown current selection (record current category)
  - End date toggle control is present and its current state is noted
  - Course Format dropdown current selection (record current format)
  - Weekly layout-specific controls are visible only if Weekly format is currently selected (note their visibility)
  - Group mode dropdown current selection (record current group mode)

**Post-Check**
- **Navigate To**: `QA Automation 101 course page, then open Course Settings`
- **Observe**:
  - Course page heading shows the updated Course Full Name entered in the test
  - Course Settings: Course Full Name field equals the entered <valid course full name>
  - Course Settings: Course Short Name field equals the entered <valid course short name>
  - Course Settings: Course Category equals the selected <valid category>
  - Course Settings: End date toggle is unchecked (disabled)
  - Course Settings: Course Format is set to 'Weekly format'
  - Course Settings: Weekly layout-specific controls are visible (e.g., weekly layout options shown)
  - Course Settings: Group mode dropdown is set to 'No groups'

**Expected Change**: After saving, the application returns to the course page and the Course Settings persist: the Course Full Name and Short Name reflect the entered values, the selected Course Category is saved, the End Date toggle remains disabled, the Course Format is set to Weekly with weekly layout controls visible, and Group mode is set to No groups.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (Edit course settings) for the target course`
- **Observe**:
  - Course Settings form is rendered
  - Enable Course End Date checkbox control is present (record current checked state)
  - Course Format dropdown is present (record current selected format)
  - Groups Group mode dropdown is present (record current selected group mode)
  - Groups Grouping control presence/selection is recorded (may be visible or hidden depending on current Group mode)

**Post-Check**
- **Navigate To**: `Course page (after Save and display) -> reopen Course Settings (Edit course settings)`
- **Observe**:
  - Course page is displayed after save (course heading visible)
  - Course Full Name field equals the value entered during the test
  - Course Short Name field equals the value entered during the test
  - Course Category field equals the category selected during the test
  - Enable Course End Date checkbox is unchecked
  - Course Format dropdown is set to 'Weekly format'
  - Weekly layout controls are visible in the form (layout-specific controls for Weekly format rendered)
  - Groups Group mode dropdown is set to the chosen non-'No groups' value
  - Groups Grouping dropdown is visible and its selection equals the grouping chosen during the test

**Expected Change**: The Course Settings persist the submitted values: the course page is shown after save and, when reopening Course Settings, the Full Name, Short Name and Category match the inputs; 'Enable Course End Date' remains disabled; Course Format is saved as 'Weekly format' with its weekly layout controls visible; Group mode is saved as the selected non-'No groups' option and the chosen Grouping is preserved.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `QA Automation 101 -> Course Settings (before change)`
- **Observe**:
  - End date toggle is currently off or Course End Date field is empty
  - Course Format is not set to 'Topics format' or Topics layout controls are not visible
  - Group mode is not set to 'No groups'

**Post-Check**
- **Navigate To**: `QA Automation 101 course page -> Course Settings (reopen after Save and display)`
- **Observe**:
  - Course full name equals <valid course full name>
  - Course short name equals <valid course short name>
  - Course category equals <valid category>
  - Start date equals <valid start date>
  - End date toggle is enabled and Course End Date equals <valid end date>
  - Course Format equals 'Topics format'
  - Topics layout controls (topics layout selector/section controls) are visible
  - Group mode equals 'No groups'

**Expected Change**: The Course Settings persist the entered values: the End Date is enabled with the provided end date, the Course Format is set to 'Topics format' (and Topics layout controls are visible), Group mode is set to 'No groups', and the full name, short name, category and start date retain the entered values after save and reopening settings.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings for 'QA Automation 101'`
- **Observe**:
  - Course Full Name field (current value)
  - Course Short Name field (current value)
  - Course Category field (current value)
  - Course Start Date field (current value)
  - Course End Date toggle state (enabled/disabled) and End Date field value if enabled
  - Course Format value
  - Visibility of Layout Controls for Topics (if Course Format is Topics)
  - Groups Group Mode value
  - Presence and selected value of Groups Grouping dropdown (if Group Mode != No groups)

**Post-Check**
- **Navigate To**: `Course page for 'QA Automation 101', then reopen Course Settings`
- **Observe**:
  - Course page heading shows the saved Course Full Name entered during the test
  - Course Settings: Course Full Name equals the value entered during the test
  - Course Settings: Course Short Name equals the value entered during the test
  - Course Settings: Course Category equals the value selected during the test
  - Course Settings: Course Start Date equals the value entered during the test
  - Course Settings: Course End Date toggle is enabled and End Date equals the value entered during the test
  - Course Settings: Course Format is 'Topics format' and Layout Controls for Topics are visible
  - Course Settings: Groups Group Mode equals the non-'No groups' option selected during the test
  - Course Settings: Groups Grouping dropdown is visible and selected grouping equals the value chosen during the test

**Expected Change**: The Course Settings persist the entered configuration: full name, short name, category, start date, end date (enabled and set), format set to Topics with its layout controls visible, and groups configured to the chosen non-'No groups' mode with the selected grouping; the course page heading reflects the saved Course Full Name.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page for the target course (before making changes)`
- **Observe**:
  - Course Full Name is NOT the intended new value
  - Course Short Name is NOT the intended new value
  - Course Category is NOT the intended category value
  - Course End Date toggle is disabled OR the End Date value differs from the intended end date
  - Course Format is NOT set to 'Weekly format' OR Weekly layout controls are not visible
  - Group mode is NOT set to 'No groups'

**Post-Check**
- **Navigate To**: `1) Course page (after save) -> verify heading; 2) Reopen Course Settings and refresh the page`
- **Observe**:
  - Course page heading displays the intended Course Full Name
  - Course Settings shows Course Full Name equal to the intended new value
  - Course Settings shows Course Short Name equal to the intended new value
  - Course Settings shows Course Category equal to the intended category
  - Course Settings shows Course Start Date equal to the entered start date
  - Course Settings shows End Date toggle enabled and Course End Date equals the entered end date (or is the same date/time)
  - Course Settings shows Course Format = 'Weekly format' and Weekly-specific layout controls are visible
  - Course Settings shows Group mode = 'No groups'
  - After a full page refresh, all of the above persisted values remain unchanged

**Expected Change**: The course configuration is saved and persisted: the Course Full Name/Short Name/Category and Start/End dates are updated, Course Format is set to Weekly with the Weekly layout controls visible, and Group mode is set to No groups; the course page heading reflects the new Course Full Name and all settings remain after refresh.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings (current course)`
- **Observe**:
  - Course Full Name field does not show the intended new course full name
  - Course Short Name field does not show the intended new course short name
  - Course Category is not set to the intended category
  - Course End Date toggle is disabled OR End Date field value does not equal the intended end date
  - Course Format is not 'Weekly format' OR Weekly layout controls are not visible
  - Groups Group Mode is 'No groups' OR Groups Grouping dropdown is not populated with the intended grouping

**Post-Check**
- **Navigate To**: `Course page -> open Course Settings for the same course (after Save and display)`
- **Observe**:
  - Course Full Name field shows the saved course full name that was entered during the test
  - Course Short Name field shows the saved course short name that was entered during the test
  - Course Category shows the selected category that was saved
  - Course End Date toggle is enabled and End Date field equals the configured end date (greater than or equal to the start date)
  - Course Format is set to 'Weekly format' and the Weekly layout controls are visible in the UI
  - Groups Group Mode is set to a mode other than 'No groups' and the Groups Grouping dropdown is visible
  - Groups Grouping dropdown shows the selected grouping value that was saved
  - After saving, the app returned to the course page (Course heading is visible)

**Expected Change**: The Course Settings persist: the course full/short name and category are saved; the End Date toggle is enabled with the configured end date; Course Format is set to Weekly and weekly layout controls are rendered; Group mode is set to a non-'No groups' value and the chosen Grouping is populated. The system returns to the course page after Save and display.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course (QA Automation 101) -> Participants`
- **Observe**:
  - participants table does not contain a row for <matching result> (no matching username or full name)
  - no active enrollment row exists for <matching result>

**Post-Check**
- **Navigate To**: `Course (QA Automation 101) -> Participants`
- **Observe**:
  - participants table contains a row for <matching result>
  - role column shows '<role>' for the new row
  - enrolment status or active indicator is visible for the new row
  - enrollment duration column/tooltip shows '<enrollment duration>' when an enrollment duration was provided

**Expected Change**: The selected user is added to the course Participants list with the chosen role and an active enrollment entry; if an enrollment duration was entered it is displayed on the user's enrollment row, and the addition persists after a page refresh.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course -> Assignment -> Submissions tab (Assignment Submissions page)`
- **Observe**:
  - 'Quick grading' checkbox is checked
  - inline grade input fields are visible in grade cells (editable inputs)
  - at least one submission row is present

**Post-Check**
- **Navigate To**: `Assignment Submissions page (after unchecking 'Quick grading' and refreshing the page)`
- **Observe**:
  - 'Quick grading' checkbox is unchecked
  - grade cells no longer render inline editable input fields and display read-only grade text
  - clicking a grade cell does not open an inline input or editor

**Expected Change**: The 'Quick grading' control is unchecked and inline grade entry is disabled: grade cells stop rendering editable input fields and become read-only, preventing inline grading even after a page refresh.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grades -> Grader report`
- **Observe**:
  - the target activity's column header displays the current grading range or scale (e.g., '0 - 100' or the current scale name)
  - no transient confirmation text 'updates activity grade settings' is visible prior to performing the edit

**Post-Check**
- **Navigate To**: `Grades -> Grader report (refresh the page after saving)`
- **Observe**:
  - the target activity's column header displays the updated grading range or updated grading scale name that was entered in the Edit Activity Grade Settings dialog
  - the updated header value persists after a full page refresh (proves persistence)
  - a transient confirmation with the text 'updates activity grade settings' was displayed immediately after saving (if the UI shows transient messages)

**Expected Change**: The activity's column header now shows the new grade settings (updated min/max or grading scale) and this updated display remains visible after refreshing the Grader report; a transient confirmation 'updates activity grade settings' appears immediately after save if the application surfaces such messages.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grades -> Grader report`
- **Observe**:
  - Locate the grade cell for student 'student1' and the target activity (e.g., 'Essay Draft') and record its current numeric value as the previous value
  - Confirm there is no outstanding transient success banner relating to editing this grade before the test action

**Post-Check**
- **Navigate To**: `Grades -> Grader report (reload the page to ensure persisted state)`
- **Observe**:
  - The grade cell for student 'student1' and activity 'Essay Draft' displays the newly entered numeric grade value
  - Any transient confirmation message shown immediately after saving was consistent with the update (optional) and the updated grade remains after the message disappears
  - After a full page refresh the updated grade value remains visible in the same grade cell

**Expected Change**: The student's grade cell for 'student1' and activity 'Essay Draft' is changed from the previously recorded value to the new grade entered in the Edit Grade Entry dialog, and the updated value persists after a page reload (demonstrating backend persistence).

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grades -> Grader report (Gradebook)`
- **Observe**:
  - Identify and note the target activity column(s) you plan to edit (by activity name)
  - Record the current grade cell values for the specific student rows you will edit (save these original values)
  - Record the current numeric value shown in the activity column's average/overall row (class average) for each target activity

**Post-Check**
- **Navigate To**: `Grades -> Grader report (Gradebook) and refresh the page`
- **Observe**:
  - Edited student grade cell values show the newly entered grades for each target student
  - The activity column's average/overall row shows a different numeric value consistent with the updated grades
  - The updated grade cell values and the new average persist after a full page refresh

**Expected Change**: The grade cells edited in Edit Mode now display the entered valid grades and the activity column's class average value updates to reflect those changes; both the individual grades and the revised average persist after saving and refreshing the Grader report.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Edit profile page for the logged-in user`
- **Observe**:
  - Edit profile form is visible
  - First name field is populated (record current value)
  - Last name field is populated (record current value)
  - Email address field is populated (record current value)

**Post-Check**
- **Navigate To**: `User Profile page (view mode) for the logged-in user; refresh the page or reopen after save`
- **Observe**:
  - Profile header/full-name displays '<first name> <last name>'
  - Profile details or contact card shows Email as '<valid email>'
  - Edit profile link/button is present

**Expected Change**: After clicking 'Update profile' and reloading the profile page, the user's First name, Last name, and Email address are updated to the submitted values and the new values persist across page refreshes.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User menu -> Profile (view teacher1) before editing`
- **Observe**:
  - profile picture is not the uploaded <valid image file>
  - picture description does not contain <picture description>
  - interests/tags list does not include <interest tag>
  - profile Description field does not contain <description content>

**Post-Check**
- **Navigate To**: `User menu -> Profile (view teacher1) — refresh the page after saving`
- **Observe**:
  - profile picture visually matches the uploaded <valid image file> or filename is present
  - picture description displays <picture description>
  - interests/tags list contains <interest tag>
  - profile Description contains <description content>

**Expected Change**: After saving and refreshing, the teacher1 profile shows the newly uploaded picture, the Picture description equals <picture description>, the Interests list includes <interest tag>, and the profile Description contains <description content>.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Edit profile -> Additional names section`
- **Observe**:
  - Additional names list does not contain a row with Alternative Name = <alternative name>

**Post-Check**
- **Navigate To**: `Profile -> Edit profile -> Additional names section (after saving and page refresh)`
- **Observe**:
  - Additional names list contains a row with Alternative Name = <alternative name>

**Expected Change**: A new Additional name row is persisted and the Alternative Name field shows the entered <alternative name> when the Edit profile page is reopened or refreshed.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (while authenticated as teacher1)`
- **Observe**:
  - Dashboard page loads successfully
  - user menu displays the teacher name/initials
  - 'Log out' button is visible in the application header
  - protected course links (e.g., QA Automation 101) open without redirect

**Post-Check**
- **Navigate To**: `Login page (after clicking 'Log out'), then attempt to open Dashboard (or refresh a protected page)`
- **Observe**:
  - Login page is displayed with the login form prompting for credentials
  - user menu / authenticated header controls (teacher name/initials, 'Log out') are not present
  - Attempting to open Dashboard or refreshing a previously protected page redirects to the Login page

**Expected Change**: The authenticated session is terminated: the UI shows the Login page and login form, authenticated header controls are removed, and attempts to access protected pages (Dashboard/course pages) redirect to the Login page.

---
