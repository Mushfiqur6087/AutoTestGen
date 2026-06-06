# Test Cases — MoodleStudent

Generated: 2026-06-04T15:14:00.902741Z  
Model: gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 161 | 76 | 38 | 47 | 76 | 65 | 20 |

## Login

Total: **11** (positive: 3, negative: 5, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User account exists with username 'student1' and known password, User is on the Login page | 1. Enter 'student1' into the Username field<br>2. Enter the correct password into the Password field<br>3. Click the 'Log in' button | User is redirected to the Dashboard page; no inline error is shown and user session is established | high |
| TC-007 |  | Access as a guest navigates to unauthenticated browsing | User is on the Login page | 1. Click the 'Access as a guest' button | User is taken to the guest/unauthenticated browsing area (limited-access Dashboard or landing page) without requiring credentials | high |
| TC-009 |  | Cookies notice displays cookie usage information | User is on the Login page | 1. Click the 'Cookies notice' button | A cookies notice (modal, panel, or message) is displayed containing information about cookie usage and an option to close/dismiss the notice | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login fails with incorrect password — password cleared, username retained | User account exists with username 'student1' and known password, User is on the Login page | 1. Enter 'student1' into the Username field<br>2. Enter an incorrect password into the Password field<br>3. Click the 'Log in' button | An inline error message is displayed indicating login failed; the Password field is cleared; the Username field remains populated with 'student1' for correction | high |
| TC-003 |  | Login fails with non-existing username | No account exists for username 'no_such_user', User is on the Login page | 1. Enter 'no_such_user' into the Username field<br>2. Enter any password into the Password field<br>3. Click the 'Log in' button | An inline error message is displayed indicating login failed; the Password field is cleared; the Username field remains populated with 'no_such_user' | high |
| TC-004 |  | Login with both fields empty | User is on the Login page | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the 'Log in' button | An inline error message is displayed indicating credentials are required; Password field remains empty; Username field remains empty; no redirect occurs | high |
| TC-005 |  | Login with empty password (username provided) | User account exists with username 'student1', User is on the Login page | 1. Enter 'student1' into the Username field<br>2. Leave the Password field empty<br>3. Click the 'Log in' button | An inline error message is displayed indicating password is required; the Password field is empty (cleared); the Username field remains populated with 'student1'; no redirect occurs | high |
| TC-008 |  | Lost password? link is present but disabled | User is on the Login page, This test site has the 'Lost password?' feature disabled | 1. Attempt to click the 'Lost password?' link | 'Lost password?' link does not navigate; link is visibly disabled or inactive and no password recovery flow is started | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Login attempt with very long username and password | User is on the Login page | 1. Enter a very long string (e.g., 500 characters) into the Username field<br>2. Enter a very long string (e.g., 500 characters) into the Password field<br>3. Click the 'Log in' button | The application handles the input without crashing; either a validation inline error or authentication failure message is shown; the Password field is cleared; the Username field remains populated (or visibly truncated to UI max length); no unexpected behavior occurs | medium |
| TC-010 |  | Attempt login with SQL-injection-like input | User is on the Login page | 1. Enter "' OR '1'='1" into the Username field<br>2. Enter "' OR '1'='1" into the Password field<br>3. Click the 'Log in' button | Authentication fails and an inline error message is shown; the Password field is cleared; the Username field remains populated; the application does not expose database errors or crash | medium |
| TC-011 |  | Login page UI elements presence and required indicators | User is on the Login page | 1. Inspect the Login form | Username and Password fields are visible and marked as required; 'Log in' button is present; 'Lost password?' link is visible (disabled on this site); 'Access as a guest' and 'Cookies notice' buttons are visible | low |

---

## Dashboard

Total: **20** (positive: 15, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Personalized greeting shows user's display name | User is logged in, User has a display name set in profile | 1. Navigate to the Dashboard page | A greeting is visible at the top of the Dashboard and contains the logged-in user's display name (e.g., 'Welcome, <User>') | high |
| TC-013 |  | Timeline displays upcoming activities for default time range (Next 7 days) | User is logged in, There are activities with deadlines within the next 7 days across enrolled courses | 1. Navigate to the Dashboard<br>2. Locate the Timeline block<br>3. Ensure the time range dropdown is set to 'Next 7 days' | Timeline lists the upcoming activities that fall within the next 7 days, each showing name, course, and date/time; items are visible in the current sort order | high |
| TC-014 |  | Changing sort order in Timeline updates item ordering | User is logged in, Timeline contains multiple activities with different dates/times | 1. Open the Dashboard<br>2. In the Timeline block, open the sort order dropdown<br>3. Select an alternate sort order (e.g., 'Newest first' or 'Oldest first') | Timeline items re-order according to the selected sort option (e.g., newest items appear first when 'Newest first' is selected) | medium |
| TC-015 |  | Timeline search finds activities by full name | User is logged in, There is at least one activity with unique name 'Assignment X' in the current time range | 1. Navigate to Dashboard<br>2. In the Timeline block, enter 'Assignment X' into the search field and submit/search | Search results show the activity named 'Assignment X'; non-matching items are not shown | high |
| TC-017 |  | Calendar displays current month/year heading and highlights current date | User is logged in, Dashboard Calendar block is visible | 1. Navigate to the Dashboard | Calendar header shows the current month and year (e.g., 'June 2026') and the cell representing today's date is visually highlighted | high |
| TC-018 |  | Filtering calendar by 'All courses' dropdown shows only events for selected course | User is logged in, Calendar contains events from at least two different courses | 1. Open Dashboard<br>2. In the Calendar block, open the 'All courses' dropdown<br>3. Select a single course (Course A) | Calendar updates to display only events that belong to Course A; events from other courses are hidden | high |
| TC-019 |  | Creating a new personal calendar event saves and appears on calendar and timeline if in range | User is logged in, User has permission to create personal events, Selected date for event is within timeline time range if verifying timeline | 1. In the Calendar block click 'New event'<br>2. Fill in valid event details (Title, Date, Time, optional description)<br>3. Click Save/Create<br>4. Observe the Calendar and (optionally) the Timeline if the event date falls in the selected Timeline range | Event is created successfully; the new event appears on the calendar cell for the chosen date (showing the title inline) and appears in the Timeline if the date is within the timeline's range | high |
| TC-021 |  | Calendar month navigation arrows move calendar to previous/next month | User is logged in, Calendar block is visible | 1. Open Dashboard<br>2. Note the month/year in the Calendar header<br>3. Click the right arrow once<br>4. Click the left arrow once (to return) | After clicking right arrow the calendar header advances by one month; clicking left arrow returns to the original month; calendar cells update to show dates and events for the displayed month | medium |
| TC-023 |  | Dates with events display event names inline in the calendar month view | User is logged in, There is at least one event scheduled on a date in the current month | 1. Open Dashboard<br>2. View the current month in the Calendar block | Cells for dates that have events show the event name(s) inline within the date cell | high |
| TC-024 |  | 'Full calendar' link opens the dedicated calendar view | User is logged in, Dashboard is displayed | 1. Scroll to the bottom of the Calendar block<br>2. Click the 'Full calendar' link | The application navigates to or opens the dedicated calendar view (full calendar page) and the calendar view is displayed | medium |
| TC-025 |  | 'Import or export calendars' link opens calendar data management page | User is logged in, Dashboard is displayed | 1. Scroll to the bottom of the Calendar block<br>2. Click the 'Import or export calendars' link | The calendar import/export or data management page opens (or navigates to the appropriate UI) allowing the user to import or export calendar data | medium |
| TC-026 |  | Toggling Edit mode on reveals Reset and Add a block controls | User is logged in with page edit permissions, Dashboard is visible | 1. Click the Edit mode toggle to turn Edit mode on | A 'Reset page to default' button appears at the top right of the Dashboard and a '+ Add a block' button appears below the Dashboard heading | high |
| TC-027 |  | + Add a block opens list of available block types | User is logged in with edit permissions, Edit mode is ON | 1. In Edit mode, click the '+ Add a block' button below the Dashboard heading | The application opens a page or panel listing all available block types that can be added to the Dashboard | medium |
| TC-028 |  | In Edit mode each block shows move icon and three-dot menu with configure/move/delete actions | User is logged in with edit permissions, Edit mode is ON, Dashboard contains at least one block (Timeline and Calendar) | 1. Turn Edit mode ON<br>2. Inspect each block on the Dashboard | Each existing block displays a move icon and a three-dot menu; opening the menu shows options for Configure, Move, and Delete (or equivalent actions) | high |
| TC-029 |  | Reset page to default restores original layout | User is logged in with edit permissions, Edit mode is ON, Dashboard layout has been modified (blocks moved/added/removed) | 1. In Edit mode click 'Reset page to default'<br>2. Confirm the reset when prompted | Dashboard reverts to the default page layout; added blocks are removed, moved blocks return to default positions, and a confirmation or success message is shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 |  | Creating a new personal event without required Title shows validation error | User is logged in, User is on the Dashboard, User has permission to create personal events | 1. In the Calendar block, click 'New event'<br>2. In the New Event form leave the Title field empty and fill other required fields if any<br>3. Click Save/Create | The system prevents saving and displays a validation error indicating the Title is required (e.g., 'Please enter a title') and the event is not created | high |
| TC-030 |  | Attempt to enter Edit mode without permissions is blocked and edit controls are not shown | User is logged in without page edit permissions | 1. Attempt to toggle Edit mode ON from the Dashboard | The system prevents entering Edit mode; Edit-specific controls (Reset, + Add a block, move icons, three-dot menus) are not displayed and an appropriate error or permission message is shown if applicable (e.g., 'You do not have permission to edit this page') | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Create event on Feb 29 (leap year) and verify invalid date selection on non-leap year | User is logged in, Date picker supports selecting year/month/day | 1. Click 'New event' in Calendar<br>2. Use date picker to select Feb 29, 2024 (leap year) and save the event<br>3. Verify event is created<br>4. Attempt to select Feb 29, 2023 (non-leap year) in date picker | Event for Feb 29, 2024 is created successfully. For 2023 the date picker prevents selection of Feb 29 or the system shows a validation error if a user attempts to submit that invalid date | medium |
| TC-022 |  | Navigate many months forward/back to verify calendar stability (large range navigation) | User is logged in, Calendar navigation is enabled | 1. Open Dashboard<br>2. Click the right arrow repeatedly (e.g., 120 times) to move many months into the future<br>3. Click the left arrow repeatedly to move back to current month | Calendar continues to respond without crashing; month/year heading updates correctly for each navigation step; eventually returns to the expected month when navigating back. If the system imposes a navigation limit it shows a graceful message or prevents further navigation without crashing | low |
| TC-031 |  | Timeline shows empty state when no items exist within the selected time range | User is logged in, No activities exist within a selected timeline range (e.g., 'Next 30 days') | 1. Open Dashboard<br>2. In the Timeline block set the time range to a range with no activities (e.g., 'Next 30 days' when there are none) | Timeline displays the empty state UI (informational message and/or illustration) indicating there are no upcoming activities within the selected time range | medium |

---

## My Courses

Total: **16** (positive: 9, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Click course name navigates to course main page | User is logged in as a student, My Courses page is accessible, At least one enrolled course exists with a visible course card | 1. Open the My Courses page<br>2. Identify a course card and click the course name link | Browser navigates to the selected course's main page; the URL and page header/course title correspond to the clicked course and course content loads without error | high |
| TC-033 |  | Status filter shows only 'In progress' courses | User is logged in, My Courses contains courses with various statuses including 'In progress' and other statuses | 1. Open the My Courses page<br>2. Click the Status dropdown<br>3. Select 'In progress' from the dropdown | Only course cards whose status is 'In progress' are visible in the grid; courses with other statuses are not shown | high |
| TC-034 |  | Search by partial course name returns matching cards | User is logged in, There is at least one course whose name contains a specific recognizable substring (e.g., 'Intro') | 1. Open the My Courses page<br>2. Enter the substring (e.g., 'Intro') into the search field<br>3. Press Enter or click the search icon | Only course cards whose name includes the substring are displayed; other courses are filtered out | medium |
| TC-035 |  | Sort by Name A-Z orders courses alphabetically | User is logged in, My Courses contains multiple courses with distinct names, Sort dropdown contains a 'Name A-Z' option | 1. Open the My Courses page<br>2. Click the Sort dropdown<br>3. Select 'Name A-Z' (or equivalent) option | Course cards are reordered so that their names appear in ascending alphabetical order (A to Z) | medium |
| TC-036 |  | Change layout to List view | User is logged in, Layout dropdown is visible with options Card, List, Summary | 1. Open the My Courses page<br>2. Click the Layout dropdown<br>3. Select 'List' layout option | The page switches to List layout: course presentations change from card grid to vertical list format showing course image, name (link), and category in list rows | medium |
| TC-037 |  | Star a course pins it to the top | User is logged in, At least one course card is available, The three-dot menu is present on each course card and includes 'Star this course' | 1. Open the My Courses page<br>2. On a non-top course card, click the three-dot menu<br>3. Select 'Star this course' | The selected course shows a star indicator and is moved/pinned to the top position of the course list/grid (above non-starred courses) | high |
| TC-038 |  | Remove a course from view hides it without unenrolling | User is logged in, At least one course card is visible, Three-dot menu includes 'Remove from view' | 1. Open the My Courses page<br>2. On a visible course card, click the three-dot menu<br>3. Select 'Remove from view' | The selected course card is removed/hidden from the My Courses view; user remains enrolled in the course (no unenroll action occurs). The course should be possible to view again via the 'Hidden' status filter or undo if provided | high |
| TC-039 |  | Status filter 'Starred' shows starred/pinned courses | User is logged in, At least one course has been starred/pinned, Status dropdown contains 'Starred' option | 1. Open the My Courses page<br>2. Click the Status dropdown<br>3. Select 'Starred' | Only courses that were starred/pinned are displayed; non-starred courses are not shown | medium |
| TC-040 |  | Status filter 'Hidden' shows courses removed from view | User is logged in, At least one course has been removed from view (hidden), Status dropdown contains 'Hidden' option | 1. Open the My Courses page<br>2. Click the Status dropdown<br>3. Select 'Hidden' | Courses previously removed from view are displayed in the list; they remain hidden from other status views until unhidden | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | Search input with SQL-like special characters does not expose data or crash | User is logged in, My Courses page is open | 1. Open the My Courses page<br>2. Enter a SQL-like string such as "' OR '1'='1' --" into the search field<br>3. Press Enter or click the search icon | The application remains responsive and does not return unintended courses or crash; either no results or only correctly sanitized filtering results are shown and no error stack trace is displayed | medium |
| TC-042 |  | Search input exceeding maximum length is rejected or truncated | User is logged in, My Courses search field is available, There is a client or server-defined maximum input length (test with a very long string) | 1. Open the My Courses page<br>2. Paste a very long string (e.g., 5000 characters) into the search field<br>3. Press Enter or click search | The system prevents the excessively long input from causing errors: either the input is truncated client-side, a validation message like 'Search term too long' is shown, or the server returns a handled response (no crash). | low |
| TC-047 |  | Clicking course link while offline shows network error and does not crash | User is logged in and on the My Courses page, A course card is present, Test environment can simulate offline/network loss | 1. Simulate network offline mode (browser/network tooling)<br>2. Click the course name link on a course card | Navigation fails gracefully with a clear network/error message (e.g., 'You are offline' or 'Unable to load course'); the application does not crash or display an unhandled error | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Search is case-insensitive (matching different case) | User is logged in, There is a course whose name is 'Biology 101' or similar | 1. Open the My Courses page<br>2. Enter 'biology 101' (lowercase) into search and execute<br>3. Observe results | Course 'Biology 101' is returned despite case differences, confirming case-insensitive search behavior | medium |
| TC-044 |  | Star multiple courses and verify pinned order | User is logged in, At least three courses are available | 1. Open the My Courses page<br>2. For Course A, open its three-dot menu and select 'Star this course'<br>3. For Course B, open its menu and select 'Star this course'<br>4. Observe the order of starred courses at the top | Both Course A and Course B appear above unstarred courses; order is consistent with defined behavior (e.g., most recently starred first) and both show a star indicator | medium |
| TC-045 |  | Hidden course remains hidden after page refresh (persistence) | User is logged in, At least one course has been removed from view (hidden) | 1. Open the My Courses page and confirm the course is hidden (not visible in default All view)<br>2. Refresh the browser page<br>3. Re-open the My Courses page or confirm current state | The previously hidden course remains hidden after refresh; it is still visible when the 'Hidden' status filter is selected, demonstrating persistence of the hidden state | low |
| TC-046 |  | Rapidly toggle layout options to check UI stability | User is logged in, Layout dropdown contains Card, List, Summary | 1. Open the My Courses page<br>2. Repeatedly change the layout selection between Card, List, and Summary (e.g., 20 rapid changes)<br>3. Observe the UI behavior and responsiveness | The UI remains responsive without visual glitches or crashes; each selected layout is rendered correctly after change | low |

---

## Course Page

Total: **13** (positive: 5, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Course heading and navigation tab bar are displayed | User is logged in as a student, User is enrolled in the course | 1. Navigate to the Course page for the enrolled course | Course name is displayed as the page heading and the navigation tab bar is visible below the heading | high |
| TC-049 |  | Expand and collapse individual section using chevron | User is logged in as a student, Course has at least one collapsed section with activities | 1. Open the Course page<br>2. Click the chevron icon for a section to expand it<br>3. Click the chevron icon again to collapse the section | Section expands to show the activities/resources on first click and collapses to hide them on second click; chevron orientation updates accordingly | high |
| TC-050 |  | Open an activity/resource by clicking its name | User is logged in as a student, Course has at least one expanded section containing activities/resources | 1. Open the Course page and expand the section that contains an activity/resource<br>2. Click the clickable name of an activity/resource | The selected activity/resource opens (navigates to the correct activity page or downloads/displays the resource) | high |
| TC-051 |  | "Collapse all" collapses all expanded sections | User is logged in as a student, Course contains multiple sections and at least two sections are expanded | 1. Open the Course page with multiple expanded sections<br>2. Click the "Collapse all" link at the top right of the section list | All sections collapse and no section content (activities/resources) is visible; chevrons show collapsed state | high |
| TC-058 |  | Activity/resource type icons are displayed and correspond to item type | User is logged in as a student, Course contains activities/resources of different types (e.g., PDF, Quiz, Forum) | 1. Open the Course page and expand sections to view activities/resources<br>2. Verify the icon next to each activity/resource corresponds to its type | Each activity/resource displays an appropriate type icon next to its name (icons match the expected types) and icons are visible | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Student cannot enable Edit mode on course page | User is logged in as a student | 1. Open the Course page<br>2. Attempt to locate and enable any Edit mode toggle or link | Edit mode option is not available to the student, or attempt to enable it is blocked with a permission error/message | high |
| TC-053 |  | Clicking a broken activity link displays an error | User is logged in as a student, Course contains an activity/resource with a broken URL or missing target | 1. Open the Course page and expand the section containing the broken activity<br>2. Click the activity/resource name that points to the broken link | An error page or user-friendly error message is displayed (e.g., 404 or 'Resource not found') and the system does not crash | medium |
| TC-057 |  | Expand a section that contains no activities/resources | User is logged in as a student, Course has at least one section with zero activities/resources | 1. Open the Course page<br>2. Click the chevron to expand the section that contains no activities | Expanded section displays an appropriate empty state (e.g., 'No activities in this section' or no items), and no errors occur | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Display of extremely long section names | User is logged in as a student, Course contains a section with an extremely long name (e.g., 500+ characters) | 1. Open the Course page that includes the long-named section<br>2. Observe the layout of the section list and, if available, hover over the truncated name | Long section name does not break the layout; name is truncated with ellipsis if necessary and full name is available via tooltip or accessible method (no overflow causing UI distortion) | medium |
| TC-055 |  | Course page with a very large number of sections (performance and Collapse all) | User is logged in as a student, Course contains a very large number of sections (e.g., 200+) | 1. Open the Course page with many sections<br>2. Observe page load time and responsiveness<br>3. Click "Collapse all" and observe behavior | Page loads within acceptable time (no hang); UI remains responsive and "Collapse all" collapses all sections without UI errors | medium |
| TC-056 |  | Course page when there are no sections | User is logged in as a student, Course has zero sections configured | 1. Open the Course page for the empty course | Page shows an appropriate empty state (e.g., message like 'No sections available' or simply no section list); "Collapse all" link is not shown or is disabled and no errors appear | medium |
| TC-059 |  | Keyboard accessibility for collapsing/expanding sections (Enter/Space) | User is logged in as a student, Course page is open with focusable chevron controls | 1. Focus the chevron control for a section using keyboard (Tab key)<br>2. Press Enter (or Space) to toggle the section | Section toggles (expands/collapses) when the chevron is activated via keyboard; focus outline is visible and no JS errors occur | low |
| TC-060 |  | "Collapse all" when all sections are already collapsed | User is logged in as a student, All course sections are in collapsed state | 1. Open the Course page ensuring all sections are collapsed<br>2. Click the "Collapse all" link | No visual change occurs, no errors are shown, and the page remains stable ("Collapse all" can be a no-op or remain available) | low |

---

## Participants

Total: **18** (positive: 9, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Participants page shows list and expected columns | User is logged in as a Student, User has access to the course with enrolled participants | 1. Navigate to the course Participants page | Participants table is displayed with columns: selection checkbox, First/Last name (sortable and linked), Roles, Groups, Last access to course, and filter controls are visible at the top | high |
| TC-062 |  | Click a participant name opens their profile | User is logged in as a Student, At least one participant exists with a profile | 1. Open the Participants page<br>2. Click on a participant's First/Last name link in the table | Participant's profile page/modal opens showing participant details; Student can view but does not see enrol/unenrol or role-edit controls | high |
| TC-063 |  | Alphabetical filter by First name (A) filters results | User is logged in as a Student, Participants list contains names starting with 'A' and other letters | 1. Open the Participants page<br>2. In the First name alphabetical filter, click the 'A' button | Table shows only participants whose first name begins with 'A'; other rows are hidden | high |
| TC-064 |  | Alphabetical filter by Last name (Z) filters results | User is logged in as a Student, Participants list contains last names beginning with 'Z' and others | 1. Open the Participants page<br>2. In the Last name alphabetical filter, click the 'Z' button | Table shows only participants whose last name begins with 'Z'; other rows are hidden | medium |
| TC-065 |  | Sort participants by First/Last name ascending and descending | User is logged in as a Student, Participants list has multiple distinct first and last names | 1. Open the Participants page<br>2. Click the First/Last name column header once to sort ascending<br>3. Click the same header again to sort descending | Clicking toggles the sort order; rows reorder accordingly (ascending then descending) and visible ordering matches expected sort | medium |
| TC-066 |  | Apply a single filter condition (Role = Student) | User is logged in as a Student, Some participants have Role = Student | 1. Open the Participants page<br>2. In the filter area, select the attribute 'Role' from the Select attribute dropdown<br>3. Choose value 'Student'<br>4. Click 'Apply filters' | Table displays only participants with Role = Student; filter indicator shows active filter | high |
| TC-067 |  | Use '+ Add condition' with 'Any' toggle to create OR filter across attributes | User is logged in as a Student, Participants exist matching either Role = Teacher or Group = Group1 | 1. Open the Participants page<br>2. Ensure the 'Any' toggle is enabled (OR behavior)<br>3. Select attribute 'Role' = 'Teacher'<br>4. Click '+ Add condition' and select attribute 'Group' = 'Group1'<br>5. Click 'Apply filters' | Table shows participants who satisfy either Role = Teacher OR Group = Group1 (union of matches); both conditions are visible in the filter UI | high |
| TC-073 |  | Clear filters returns to full participants list and resets UI | User is logged in as a Student, Filters currently applied showing a subset of participants | 1. On the Participants page, ensure a filter is active<br>2. Click the 'Clear filters' button | All active filters are cleared, filter UI fields reset to defaults (Any toggle, Select attribute empty), and the table displays the full list of participants | high |
| TC-076 |  | Select multiple participant checkboxes but no bulk enrollment actions available to Student | User is logged in as a Student, Participants table shows selectable checkboxes | 1. Open the Participants page<br>2. Click checkboxes for multiple participants<br>3. Look for bulk action toolbar or buttons (e.g., Enrol/Unenrol/Edit roles) | Checkboxes can be selected/unselected, but no bulk enrol/unenrol or role-edit actions are available to the Student; if any bulk controls exist they are disabled or hidden | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Attempt to apply filters without selecting attribute/value | User is logged in as a Student, Open Participants page | 1. Open the filter area<br>2. Click '+ Add condition' but do not select an attribute or value<br>3. Click 'Apply filters' | Filter validation prevents application: an inline validation message is displayed (e.g., 'Please select an attribute and value') or no filter is applied and user is prompted to complete the condition | medium |
| TC-071 |  | Student cannot enrol or unenrol users (no enrollment controls present) | User is logged in as a Student, Open Participants page | 1. Open the Participants page<br>2. Inspect participant rows, profile pages, and any context menus for enrol/unenrol controls<br>3. If checkboxes are present, attempt any bulk action that would enrol/unenrol | No enrol/unenrol buttons or links are visible to the Student; bulk enrol/unenrol actions are not available or are disabled and produce no access to enrollment management | high |
| TC-072 |  | Student cannot edit roles or access role-editing features | User is logged in as a Student, Open Participants page | 1. Open the Participants page<br>2. Inspect Roles column and any actions/context menus for edit role controls<br>3. Attempt to access any role-edit UI if visible | Role edit controls are not visible or are disabled for Student; any attempt to access role management is blocked or shows a permission error | high |
| TC-077 |  | Applying filters that produce zero matches shows empty results message | User is logged in as a Student, Filter inputs exist that will produce no matches | 1. Open the Participants page<br>2. Enter filter criteria guaranteed to match no participants (e.g., Role = NonexistentRole)<br>3. Click 'Apply filters' | Table shows no rows and a clear 'No results' or similar message; filters remain visible for adjustment | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-069 |  | Add conditions repeatedly until UI limit (max conditions) is reached | User is logged in as a Student, Open Participants page | 1. Open the filter area<br>2. Repeatedly click '+ Add condition' and choose an attribute/value for each until the link is disabled or the system prevents adding more<br>3. Observe system behavior when the presumed limit is reached | System either allows a reasonable number of conditions and then disables 'Add condition' or shows a clear message about condition limit; UI remains stable and responsive | low |
| TC-070 |  | Filter using special characters and unicode in values (e.g., O'Connor, 漢字) | User is logged in as a Student, Participants include names/groups/attributes with special characters or unicode | 1. Open the Participants page<br>2. In the filter area select attribute 'Last name' and enter a value containing special characters/unicode (e.g., "O'Connor" or "漢字")<br>3. Click 'Apply filters' | Filter correctly returns participants with matching special-character/unicode values (no errors or mis-encoding); matches appear in the table | medium |
| TC-074 |  | Empty participants list displays appropriate empty state | User is logged in as a Student, Course has zero enrolled participants | 1. Open the Participants page | Participants table shows an empty state message (e.g., 'No participants found') and filter controls remain available and usable; page does not error | medium |
| TC-075 |  | Very long participant names render safely (truncated/displayed) and profile link works | User is logged in as a Student, At least one participant has an extremely long first/last name (e.g., 256+ characters) | 1. Open the Participants page<br>2. Locate the row with the very long name<br>3. Verify visual rendering and click the name link | Long names are visually handled (truncated with ellipsis or wrapped without breaking layout), UI remains usable, and clicking the name opens the participant profile | low |
| TC-078 |  | Sorting with duplicate names maintains stable behavior and does not crash | User is logged in as a Student, There are multiple participants with identical first and/or last names | 1. Open the Participants page<br>2. Click the name column header to sort ascending or descending<br>3. Observe ordering of duplicate-name rows and attempt additional sorts | Sorting completes without error; rows with identical names are grouped consistently and UI remains responsive (secondary ordering may be by last access or other stable criterion) | low |

---

## Grades

Total: **16** (positive: 6, negative: 3, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Grades page shows correct columns and AGGREGATION row | Student is logged in, Student is enrolled in the course, At least one graded activity exists in the course | 1. Navigate to the course Grades page (User report) from the course menu<br>2. Observe the grade table and bottom rows | Grade table displays columns: Grade item, Calculated weight, Grade, Range, Percentage, Feedback, Contribution to course total. An 'AGGREGATION Course total' row is present at the bottom showing the cumulative grade. | high |
| TC-080 |  | Graded activity displays numeric grade, range and percentage correctly | Student is logged in and enrolled, One graded activity exists with earned value 18 and range max 20 | 1. Open the Grades page for the course<br>2. Locate the graded activity row | Grade column shows '18' (or configured format), Range shows '0–20' (or '20'), Percentage shows '90%' (18/20), and Contribution to course total shows the calculated contribution based on weight. | high |
| TC-081 |  | Course header collapses and expands to show/hide graded activities | Student is logged in and enrolled, Course header contains multiple graded activities | 1. Open the Grades page<br>2. Click the course name collapsible header<br>3. Click the header again to collapse | Clicking header expands to show indented graded activities; clicking again collapses them. The state persists while on the page. | medium |
| TC-082 |  | Contribution to course total reflects calculated weight | Student is logged in and enrolled, Graded activity has a configured weight (e.g., 30%) and grade is available | 1. Open the Grades page<br>2. Identify the activity with configured weight<br>3. Verify Contribution to course total value for that activity | Contribution equals (earned grade / range) * weight and is displayed in the Contribution to course total column. Values match expected calculation. | high |
| TC-089 |  | Percentage calculation is correct for fractional grades | Student is logged in, An activity exists with earned value 7.5 and maximum 10 | 1. Open the Grades page<br>2. Locate the activity and check the Percentage column | Percentage displays '75%' (or '75.0%' depending on formatting). Calculation equals (7.5 / 10) * 100 and matches displayed value. | high |
| TC-093 |  | Feedback column displays instructor feedback for graded item | Student is logged in, Instructor has provided feedback for at least one graded activity | 1. Open the Grades page<br>2. Locate the activity with feedback and view the Feedback column | Feedback column shows the instructor's feedback text. If feedback is long it follows UI behavior (truncated with expansion or fully visible). | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-084 |  | Student cannot view another student's grades via direct URL manipulation | Student A is logged in and enrolled in course, Student B exists and has grades in the same course, Tester knows the URL or parameters that reference Student B's grade report | 1. While logged in as Student A, attempt to open the grade report URL referencing Student B (e.g., change user id parameter)<br>2. Observe the response | System denies access (403/Access denied/redirect to own grades). Student A only sees their own grades; no other student's grades are shown. | high |
| TC-085 |  | Student cannot access full gradebook or list of students | Student is logged in, Course has a gradebook accessible to instructors/TAs | 1. Navigate to any link/button that would normally access the full gradebook (if visible)<br>2. Attempt to open gradebook via direct URL if link not shown | Student cannot access the full gradebook or list of students. The UI either does not show links, or the system returns an access denied message/redirects to student's own grades. | high |
| TC-091 |  | Grade fields are read-only for students (attempt to edit fails) | Student is logged in and viewing Grades page | 1. Attempt to click into Grade, Range, Percentage or Contribution fields to edit<br>2. Attempt to use browser dev tools to change displayed grade value and submit (if UI offers any submit)<br>3. Attempt to find edit controls for grades on the page | No edit controls are available. Fields are read-only. Any client-side changes do not persist; the server rejects unauthorized grade changes. Student cannot modify grades. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-083 |  | Ungraded activity shows dash '–' in Grade column | Student is logged in and enrolled, At least one activity exists with no grade yet | 1. Open the Grades page<br>2. Locate the activity that has not been graded | Grade column displays '–' (dash) for ungraded activity, Percentage and Contribution show appropriate placeholders or zero values per spec, and no error is thrown. | medium |
| TC-086 |  | Zero-weight activity shows zero contribution and does not affect course total | Student is logged in and enrolled, An activity exists with weight = 0 and has a grade | 1. Open the Grades page<br>2. Locate the zero-weight activity and note Contribution and Course total | Contribution to course total for the zero-weight activity shows '0' (or 0.00). The AGGREGATION Course total excludes the zero-weight item and remains unchanged by this item's grade. | high |
| TC-087 |  | Very long feedback text displayed without layout break | Student is logged in, Instructor has entered very long feedback (e.g., 5000 characters) for an activity | 1. Open the Grades page<br>2. Locate the activity with long feedback and view the Feedback column<br>3. Attempt to scroll or expand the feedback if UI offers truncation/tooltip | Long feedback is displayed or truncated with a visible expansion/tooltip. The page layout remains intact (no overflow breaking other columns) and text is readable or accessible via expansion. | low |
| TC-088 |  | Page handles very large number of graded items (performance and visibility) | Student is logged in, Course contains many graded items (e.g., 200+) | 1. Open the Grades page<br>2. Scroll through the list to the bottom<br>3. Verify AGGREGATION Course total remains visible or reachable | Page loads within acceptable time, scrollbar or pagination appears if necessary, and AGGREGATION Course total is present and correct. No UI rendering errors occur. | medium |
| TC-090 |  | Boundary grades 0 and maximum produce 0% and 100% | Student is logged in, Two activities exist: one with grade 0/20, one with 20/20 | 1. Open the Grades page<br>2. Verify Percentage values for both boundary activities | Activity with 0/20 shows '0%'; activity with 20/20 shows '100%'. Contributions to course total reflect these percentages and weights. | medium |
| TC-092 |  | Missing range value handled gracefully (no crash) | Student is logged in, An activity exists with a missing or null maximum range value | 1. Open the Grades page<br>2. Locate the activity with missing range | UI displays a placeholder for Range (e.g., '—' or 'N/A'), Percentage is shown as '—' or appropriate message. The page does not crash and other rows render normally. | medium |
| TC-094 |  | Contributions and AGGREGATION total rounding consistent and sums to expected total | Student is logged in, Multiple graded activities with weights lead to fractional contributions requiring rounding | 1. Open the Grades page<br>2. Note individual Contribution to course total values and the AGGREGATION Course total<br>3. Sum individual displayed contributions and compare to AGGREGATION value | Displayed individual contributions are rounded per UI spec (e.g., two decimals) and the AGGREGATION Course total equals the sum of contributions within acceptable rounding tolerance. No significant discrepancy is present. | medium |

---

## Assignment

Total: **20** (positive: 9, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-095 |  | Assignment page displays Opened date, Due date, and full Description | User is a student enrolled in the course, An assignment exists with Opened date, Due date, and Description populated | 1. Log in as the student<br>2. Navigate to the Assignment page | Opened date, Due date, and the full Description are visible and match the assignment data | high |
| TC-096 |  | Add submission button opens submission form with online text editor | Assignment is configured with an online text editor, Current time is between Opened date and Due date (submissions allowed) | 1. Open the Assignment page<br>2. Click the 'Add submission' button | Submission form opens and contains an online text editor input area | high |
| TC-097 |  | Add submission form displays file upload area when configured | Assignment is configured to allow file uploads, Student is on the Assignment page | 1. Click 'Add submission'<br>2. Observe the submission form | Submission form includes a file upload area with controls to select files | high |
| TC-098 |  | Successful submission using online text editor | Assignment accepts online text submissions, Submission period is open | 1. Click 'Add submission'<br>2. Enter valid text into the online editor<br>3. Click 'Save changes' or 'Submit' (as provided by UI) | Submission is saved; Submission status shows 'Submitted for grading' (or appropriate), Last modified shows current timestamp, and submission content is viewable | high |
| TC-099 |  | Successful file upload submission | Assignment accepts file uploads, Student has a valid file within allowed size and type, Submission period is open | 1. Click 'Add submission'<br>2. Use the file upload area to attach the valid file<br>3. Click 'Save changes' or 'Submit' | File is uploaded and listed in the submission preview; Submission status updates to 'Submitted for grading' and Last modified shows current timestamp | high |
| TC-100 |  | Successful submission with both text and file when assignment allows both | Assignment configured to allow both online text and file upload, Submission window is open | 1. Click 'Add submission'<br>2. Enter text into the text editor and attach a valid file<br>3. Click 'Submit' | Both text and file are saved in the submission; Submission status shows submitted and Last modified updated | high |
| TC-101 |  | Student can view and edit their submission before due date when resubmission permitted | Student has already submitted, Current time is before Due date, Teacher allows resubmission | 1. Open Assignment page<br>2. Click 'View/edit submission' or similar control<br>3. Modify submission (edit text or replace file) and save | Edits are saved; Last modified updates; Submission status remains or updates accordingly | high |
| TC-102 |  | Graded submission displays earned grade and written feedback | Student submitted an assignment, Teacher has graded the submission and provided written feedback | 1. Student opens the Assignment page after grading is completed | Earned grade and teacher's written feedback are displayed on the page in the grading section | high |
| TC-112 |  | Submission status summary shows correct Grading status before and after grading | Student has submitted the assignment, Teacher has or has not graded the submission (test both states) | 1. After student submission, open Assignment page and note Grading status<br>2. After teacher grades, reopen the page | Before grading, Grading status shows 'Not graded' (or similar); after grading, Grading status shows 'Graded' and grade/feedback appear | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-103 |  | Submitting empty required online text shows validation error | Assignment requires online text or non-empty submission, Submission window is open | 1. Click 'Add submission'<br>2. Leave the online text editor empty<br>3. Click 'Submit' | System prevents submission and shows an error indicating the submission cannot be empty or that required content is missing | high |
| TC-104 |  | Uploading disallowed file type is rejected with error | Assignment allows file uploads but restricts file types (e.g., only .pdf, .docx), Student has a disallowed file type (e.g., .exe) | 1. Click 'Add submission'<br>2. Attempt to attach a disallowed file type<br>3. Click 'Submit' | Upload is rejected; an error message explains the disallowed file type and submission is not accepted | high |
| TC-105 |  | Uploading file exceeding size limit shows error and prevents submission | Assignment has a maximum allowed file size (e.g., 20 MB), Student attempts to upload a file larger than limit | 1. Click 'Add submission'<br>2. Attach an oversized file<br>3. Click 'Submit' | System rejects the file and shows an error indicating the file exceeds the allowed size; submission not saved | high |
| TC-106 |  | Attempt to submit after due date when resubmission is not permitted is rejected | Current time is after Due date, Teacher does not permit submissions past due date (no late submissions/resubmissions), Student has not yet submitted or tries to resubmit | 1. Open Assignment page after due date<br>2. Click 'Add submission' (if present) or attempt to submit | System prevents new submissions or resubmissions and shows an appropriate message indicating submission window has closed | high |
| TC-111 |  | Submission comments field rejects excessively long comment input if a limit exists | Submission comments field is present, A comment length limit is configured | 1. Click 'Add submission' or 'Edit submission'<br>2. Enter a comment that exceeds the configured limit<br>3. Click 'Submit' or 'Save changes' | System prevents submission of the overly long comment and displays an error indicating the comment exceeds the allowed length | medium |
| TC-114 |  | Attempt to edit submission after due date when resubmission not allowed shows blocked action | Student has a prior submission, Current time is after Due date, Teacher has not allowed resubmission after due date | 1. Open the Assignment page after the due date<br>2. Click 'View/edit submission' or attempt to modify submission | Editing is blocked or disabled; system displays a message that resubmission is not permitted after the due date | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-107 |  | Submit a file at the exact maximum allowed size | Assignment has a known file size limit (e.g., 20 MB), Student has a file exactly at the limit | 1. Click 'Add submission'<br>2. Attach the file that is exactly the maximum size<br>3. Click 'Submit' | File is accepted and submission succeeds; submission listed and Last modified updated | medium |
| TC-108 |  | Submit extremely long text (boundary length) in online editor | Assignment accepts online text, There is a maximum character limit enforced (or not stated) — test uses very large but valid length | 1. Click 'Add submission'<br>2. Paste or type a very large body of text at the expected maximum or slightly below (boundary)<br>3. Click 'Submit' | If within allowed limits, submission is accepted and text is stored/displayed; if limits exist, an informative validation error is shown that explains the limit | medium |
| TC-109 |  | Filename with special/unicode characters is accepted and displayed correctly | Assignment accepts file uploads, Student has a file with special characters/unicode in filename | 1. Click 'Add submission'<br>2. Attach the special-character filename file<br>3. Click 'Submit' | File uploads successfully and filename is displayed correctly in the submission preview and summary | medium |
| TC-110 |  | Time remaining shows 0 or negative when due date equals current time or has just passed | Current time is exactly at or just after the Due date, Assignment page is open | 1. Refresh or open the Assignment page at the boundary time<br>2. Observe the Time remaining field in the Submission status section | Time remaining displays '0' or an appropriate 'time has passed' message; UI does not crash and displays clear status (e.g., 'Due date passed') | medium |
| TC-113 |  | No Due date configured (open-ended assignment) displays appropriate Time remaining or message | Assignment has no Due date (open-ended), Student opens the Assignment page | 1. Open the Assignment page for an assignment without a Due date<br>2. Observe the Time remaining and Submission status section | The page displays an appropriate message (e.g., 'No due date' or 'Open until closed by teacher') and Time remaining either hidden or shows 'N/A' without errors | low |

---

## Activities

Total: **18** (positive: 8, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-115 |  | Assignments section expanded by default and table columns visible | User is logged in, Course contains at least one assignment | 1. Navigate to the course Activities page | The Assignments section is expanded by default and displays a table with columns: Name (clickable link), Due date, and Submission status. | high |
| TC-116 |  | Clicking an activity name navigates to that activity's page | User is logged in, At least one assignment exists in the course | 1. Open the Activities page<br>2. Click on an assignment Name link in the Assignments table | Browser navigates to the selected activity's page (URL changes and activity page content loads). | high |
| TC-117 |  | Activity Name shows parent section displayed below it in the table | User is logged in, An assignment exists and is part of a parent section | 1. Open the Activities page<br>2. Inspect the Name cell for the assignment | The Name cell contains a clickable link for the activity and the parent section name is displayed below the activity name (visible in the same row/cell). | medium |
| TC-118 |  | Forums and Resources sections are collapsed by default | User is logged in, Course contains forums and resources | 1. Navigate to the Activities page | Forum and Resources sections appear collapsed by default and display an expand/collapse arrow indicator. | high |
| TC-119 |  | Expanding a collapsed section (Forums) displays its activities | User is logged in, Course contains at least one forum activity | 1. Open the Activities page<br>2. Click the expand arrow on the Forums section | The Forums section expands and lists the forum activities (each activity name shown, clickable). | medium |
| TC-120 |  | Clicking an activity name in a non-Assignments section navigates to that activity | User is logged in, At least one activity exists in Forums or Resources | 1. Open the Activities page<br>2. Expand the relevant section (e.g., Forums)<br>3. Click an activity name in that section | The application navigates to the selected activity's page and the activity page content loads. | medium |
| TC-121 |  | Additional activity types appear as their own collapsible sections | User is logged in, Course contains at least one additional activity type (e.g., Quizzes, Workshops) | 1. Navigate to the Activities page | Each additional activity type appears as its own section on the page and is collapsed by default with an expand arrow. | medium |
| TC-122 |  | Assignments table shows correct submission statuses | User is logged in, Course contains assignments with different submission statuses (e.g., Submitted, Not submitted, Late) | 1. Open the Activities page<br>2. Inspect the Submission status column in the Assignments table | Each assignment row displays the correct submission status corresponding to the backend data. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-123 |  | User without permission attempts to open an activity -> access denied | User is logged in with insufficient permissions to view a specific activity, That activity is listed on the Activities page | 1. Open the Activities page<br>2. Click the activity Name the user should not have access to | The system prevents access and displays an access denied message or redirects to an appropriate error/permission page. | high |
| TC-124 |  | Clicking a listed activity whose backend record was deleted results in 404 or not-found error | User is logged in, An activity is listed on the Activities page but its backend record has been deleted | 1. Open the Activities page<br>2. Click the deleted activity's Name link | The application shows a 404 / "Activity not found" page or an appropriate error message indicating the activity no longer exists. | medium |
| TC-125 |  | Navigating directly to an invalid activity id in the URL shows an error | User is logged in | 1. Enter an activity URL with an invalid/non-numeric or nonexistent activity id (e.g., /mod/activity/view.php?id=INVALID) in the browser address bar<br>2. Press Enter to navigate | The system displays an error message (e.g., "Activity not found" or 404) and does not display an activity page. | medium |
| TC-126 |  | Network/server failure when loading Activities page shows error banner | User is logged in, Simulate network outage or server returns 5xx response for activities list | 1. Attempt to open the Activities page while the network/server is failing | A visible error banner or message appears (e.g., "Failed to load activities"), and the UI provides a retry option or guidance. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-127 |  | Course with no activities shows appropriate empty states | User is logged in, Course contains zero activities of any type | 1. Open the Activities page | The page shows empty state messaging where appropriate (e.g., Assignments table shows "No activities" or similar) and no activity rows are listed. | medium |
| TC-128 |  | Extremely long activity name is displayed truncated with full text available | User is logged in, An activity exists with a very long name (> 255 characters) | 1. Open the Activities page<br>2. Locate the long activity name in the table<br>3. Hover over the truncated name | The name is truncated in the table (ellipses) to maintain layout; the full name is available via tooltip/hover or by clicking into the activity page. | low |
| TC-129 |  | Activity names with special characters and Unicode render correctly | User is logged in, An activity exists with special characters and Unicode (e.g., emojis, non-Latin scripts) | 1. Open the Activities page<br>2. Inspect the activity name rendering | The activity name displays correctly without garbled characters or layout breaks (Unicode and special characters render properly). | low |
| TC-130 |  | Large number of activities loads and is scrollable (performance) | User is logged in, Course contains a very large number of activities (e.g., hundreds or thousands) | 1. Open the Activities page<br>2. Measure load time and scroll through the list/sections | The Activities page loads within acceptable performance limits, sections remain responsive, and users can scroll through activities (UI may use pagination or lazy loading). | medium |
| TC-131 |  | Assignments with missing due date display 'No due date' or appropriate placeholder | User is logged in, At least one assignment exists with no due date set (null) | 1. Open the Activities page<br>2. Locate the assignment row with no due date | The Due date column for that assignment shows a clear placeholder such as "No due date" (not an error or invalid date). | medium |
| TC-132 |  | Clicking an activity name opens the activity in the same tab | User is logged in, At least one activity exists | 1. Open the Activities page<br>2. Click an activity Name link | The activity opens in the same browser tab (the current tab navigates to the activity page rather than opening a new tab), consistent with expected navigation behavior. | low |

---

## Profile

Total: **20** (positive: 9, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-133 |  | Profile page displays core elements | User is logged in as a student, User navigates to own Profile page | 1. Open the Profile page<br>2. Observe the page header and main area | Student's circular initials icon, full name, Message button, optional profile description (if any), and information cards (User details, Privacy and policies, Course details, Miscellaneous, Reports, Login activity) are visible and correctly labeled | high |
| TC-134 |  | Message button opens messaging interface | User is logged in as a student, On their own Profile page or another student's profile that allows messaging | 1. Click the Message button on the Profile page | System opens the messaging interface (modal or new page) prefilled with the recipient; user can compose a message | medium |
| TC-135 |  | Edit profile link opens profile form with collapsible panels | User is logged in as a student, Viewing own Profile page | 1. Click the 'Edit profile' link in the User details card | Profile form opens with collapsible panels: General, User picture, Additional names, Interests, Optional fields; form fields are visible within each expanded panel | high |
| TC-136 |  | Update profile with valid inputs saves changes | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Modify First name, Last name, and Description with valid text<br>3. Choose a Country and Timezone from dropdowns<br>4. Click 'Update profile' | Form validates inputs, saves changes, returns to Profile page showing updated name and description | high |
| TC-137 |  | Course details links open enrolled course profiles | User is logged in as a student, User is enrolled in at least one course, On Profile page | 1. In the Course details card, click a linked course profile | Clicked course profile opens in the same tab or a new tab (depending on implementation) and displays the course's profile page | medium |
| TC-138 |  | Login activity shows exact dates and relative times | User is logged in as a student, Profile page has both first and last access recorded | 1. Open the Profile page and locate Login activity card | First and Last access show exact date/time (e.g., 2026-06-01 14:23) and a relative time indicator (e.g., '2 days ago') next to each | high |
| TC-139 |  | Data retention summary link opens policy page | User is logged in, On Profile page | 1. In Privacy and policies card, click the Data retention summary link | Data retention summary page opens and displays relevant policy information | medium |
| TC-140 |  | Upload a valid profile picture succeeds | User is logged in as a student, Profile edit form open, Valid image file available (supported format, within size limit) | 1. Open User picture panel<br>2. Click to upload a new picture and select a valid image file<br>3. Optionally add picture description<br>4. Click 'Update profile' | Image uploads successfully, thumbnail updates on Profile page to show the new picture | high |
| TC-141 |  | Cancel in edit form discards changes | User is logged in as a student, Profile edit form open, Some fields modified but not saved | 1. Modify one or more fields in the edit form<br>2. Click 'Cancel' | Form closes and Profile page remains unchanged (no modified values saved) | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-142 |  | Cannot edit another student's profile | User is logged in as a student, Viewing another student's Profile page | 1. Open another student's Profile page<br>2. Look for 'Edit profile' link or attempt to navigate to edit URL directly | 'Edit profile' link is not available or disabled; direct navigation to edit URL is blocked and an authorization error or access denied message is shown | high |
| TC-143 |  | Missing required field (Email) causes validation error | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Clear the Email address field<br>3. Click 'Update profile' | Form prevents submission and shows an inline error message indicating that Email address is required | high |
| TC-144 |  | Invalid email format is rejected | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Enter 'invalid-email' into Email address field<br>3. Click 'Update profile' | Form prevents submission and shows an inline error message indicating invalid email format | high |
| TC-145 |  | Uploading unsupported image format is rejected | User is logged in as a student, Profile edit form open, File of unsupported format (e.g., .exe) available | 1. Open User picture panel<br>2. Attempt to upload an unsupported file format<br>3. Click 'Update profile' if needed | Upload is rejected with an error message indicating unsupported file type; picture is not changed | medium |
| TC-146 |  | Uploading oversized image is rejected | User is logged in as a student, Profile edit form open, Image file larger than allowed limit available | 1. Open User picture panel<br>2. Attempt to upload an image exceeding the size limit<br>3. Click 'Update profile' if needed | Upload is rejected with an error message indicating file size exceeds limit; picture is not changed | medium |
| TC-147 |  | Attempt to set empty First name triggers validation error | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Clear the First name field<br>3. Click 'Update profile' | Form prevents submission and displays an inline error indicating First name is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-148 |  | Very long names and description are accepted/truncated appropriately | User is logged in as a student, Profile edit form open, Strings at or above expected maximum lengths prepared | 1. Expand General panel<br>2. Enter a 500-character First name and Last name each and a 2000-character Description<br>3. Click 'Update profile' | System either accepts and saves long values (displaying them appropriately) or enforces and displays a clear validation/truncation message; no crash occurs | medium |
| TC-149 |  | Special characters and non-Latin scripts in names | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Enter names using special characters and non-Latin scripts (e.g., emojis, Cyrillic, Chinese)<br>3. Click 'Update profile' | System saves and displays names correctly (or provides a validation message if characters are disallowed); no layout breakage | low |
| TC-150 |  | Timezone dropdown boundary values selectable | User is logged in as a student, Profile edit form open | 1. Expand General panel<br>2. Select extreme timezone values (e.g., UTC-12 and UTC+14) from the Timezone dropdown<br>3. Click 'Update profile' | Selected timezone is saved and reflected in Profile and any displayed timestamps; no error shown | low |
| TC-151 |  | Set email visibility to 'Hide my email address' and confirm effect | User is logged in as a student, Another test account available to view profile | 1. Open Profile edit form and set Email visibility dropdown to 'Hide my email address'<br>2. Click 'Update profile'<br>3. Log out and log in as another test user, then view original user's Profile page | Email address is not visible to other users per visibility setting; original user can still see their own email | medium |
| TC-152 |  | Upload image exactly at maximum allowed size | User is logged in as a student, Profile edit form open, Image exactly at size limit available | 1. Open User picture panel<br>2. Upload the image file that equals the maximum allowed size<br>3. Click 'Update profile' | Image is accepted and saved if system allows boundary size; no error thrown and thumbnail updates | medium |

---

## Logout

Total: **9** (positive: 3, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-153 |  | Basic logout via UI menu | User is authenticated, User is on a protected page (e.g., dashboard) | 1. Click the user/profile menu or hamburger menu where the 'Log out' control is located<br>2. Click 'Log out' or 'Sign out' | User is redirected to the login page (login form visible). Current session is terminated (session cookie removed or invalidated) and attempting to navigate to a protected page redirects to the login page requiring re-authentication. | high |
| TC-154 |  | Logout via direct /logout endpoint | User is authenticated, User can access application URL bar | 1. Enter the application's logout endpoint URL (e.g., /logout) and navigate<br>2. Observe application response | User is redirected to the login page and the authenticated session is terminated; protected pages require re-login. | high |
| TC-155 |  | Logout from a deep/protected page (settings) | User is authenticated, User is on a deep protected page (e.g., Settings > Account) | 1. Click the 'Log out' control from the page header/footer/menu<br>2. Observe post-logout behavior | User is redirected to the login page and session is terminated; attempting to reload or navigate back to the deep page requires authentication. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-157 |  | Network failure during logout action | User is authenticated, Test environment allows simulating network failure (e.g., offline mode or blocked request) | 1. Simulate network failure or block the logout request<br>2. Click 'Log out'<br>3. Observe UI/error handling | Application displays an error or retry prompt indicating logout failed (or informs the user of connectivity issue). The client may remain on the current page and should not assume the session was terminated until confirmation. | medium |
| TC-161 |  | Logout request rejected due to missing/invalid CSRF token | User is authenticated, Test environment allows tampering with outgoing requests (e.g., proxy) | 1. Intercept and remove or modify the CSRF token/header from the logout request<br>2. Send the modified logout request<br>3. Observe server and client response | Server rejects the logout request (e.g., 403) and client indicates the action failed; the user remains authenticated until a valid logout request succeeds. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-156 |  | Click logout when no active session (not authenticated) | User is not authenticated (no valid session) | 1. Navigate to the application or click a visible 'Log out' link/button (if present)<br>2. Observe response | Application redirects to the login page or shows the login screen without error; user remains unauthenticated and no server error is shown. | low |
| TC-158 |  | Use browser back button after successful logout | User is authenticated and on a protected page | 1. Click 'Log out' and confirm redirection to login page<br>2. Click the browser Back button<br>3. Observe whether the protected page is accessible | Protected page is not accessible; the app redirects to the login page or shows the login form. Content from the protected page must not be available without re-authentication. | high |
| TC-159 |  | Logout in one tab invalidates session in another tab | User is authenticated in two separate browser tabs/windows using the same account | 1. In Tab A, click 'Log out' and confirm redirected to login page<br>2. In Tab B, refresh a protected page or try to perform an authenticated action<br>3. Observe authentication state in Tab B | Tab B is required to re-authenticate: refresh leads to login page or shows authentication error; protected actions are blocked until login. | high |
| TC-160 |  | Double-click or rapidly click logout control | User is authenticated, Logout control is visible and clickable | 1. Rapidly click or double-click the 'Log out' control<br>2. Observe application behavior and any messages | Logout is processed once without causing duplicate actions or errors; user ends up on the login page and session is terminated cleanly. | low |

---
