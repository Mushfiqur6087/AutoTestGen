# Test Cases — MoodleTeacher

Generated: 2026-06-04T15:09:03.832037Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 69 | 23 | 23 | 23 | 41 | 28 | 0 |

## Login

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Log in with valid credentials | User is on the login page, User has valid username and password | 1. Enter valid <username> in the Username field<br>2. Enter valid <password> in the Password field<br>3. Click 'Log in' button | User is redirected to the Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Attempt to log in with invalid credentials | User is on the login page | 1. Enter invalid <username> in the Username field<br>2. Enter invalid <password> in the Password field<br>3. Click 'Log in' button | An inline error message is displayed; the password field is cleared and the username remains for correction | high |
| TC-003 |  | Attempt to log in with empty fields | User is on the login page | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click 'Log in' button | An inline error message is displayed for both fields; both fields remain empty | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Log in with a very long username and password | User is on the login page | 1. Enter a username with maximum allowed length in the Username field<br>2. Enter a password with maximum allowed length in the Password field<br>3. Click 'Log in' button | User is redirected to the Dashboard if credentials are valid; otherwise, an error message is displayed | medium |
| TC-005 |  | Log in with a username containing special characters | User is on the login page | 1. Enter a username with special characters (e.g., !@#$%^&*) in the Username field<br>2. Enter a valid <password> in the Password field<br>3. Click 'Log in' button | User is redirected to the Dashboard if credentials are valid; otherwise, an error message is displayed | medium |

---

## Dashboard

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | View the Dashboard with all elements displayed correctly | User logged in, User has enrolled in at least one course | 1. Navigate to the Dashboard<br>2. Observe the personalized greeting at the top<br>3. Check that the Timeline block is displayed with the upcoming teaching actions<br>4. Verify that the Calendar block is displayed with the current month and year | The Dashboard displays a personalized greeting, the Timeline block shows upcoming actions, and the Calendar block shows the current month and year | high |
| TC-009 |  | Create a new event in the Calendar block | User logged in, User has access to the Calendar block | 1. Navigate to the Dashboard<br>2. Click the 'New event' button in the Calendar block<br>3. Fill in the event details (title, date, time)<br>4. Click 'Save' | The new event appears in the Calendar block on the selected date | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Attempt to use the search field in the Timeline block without entering a search term | User logged in, User has enrolled in at least one course | 1. Navigate to the Dashboard<br>2. Locate the search field in the Timeline block<br>3. Leave the search field empty<br>4. Click the search button | An error message is displayed indicating that a search term must be entered; no search results are shown | high |
| TC-010 |  | Attempt to create a new event without filling in required fields | User logged in, User has access to the Calendar block | 1. Navigate to the Dashboard<br>2. Click the 'New event' button in the Calendar block<br>3. Leave all required fields empty<br>4. Click 'Save' | An error message is displayed indicating that required fields must be filled; the event is not created | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Select a time range in the Timeline block that has no upcoming actions | User logged in, User has enrolled in at least one course | 1. Navigate to the Dashboard<br>2. Locate the time range dropdown in the Timeline block<br>3. Select 'Next 7 days' (assuming no actions are scheduled in this range)<br>4. Observe the Timeline block | The Timeline block displays an empty state message indicating no upcoming actions are available for the selected time range | medium |
| TC-011 |  | Navigate to the previous month in the Calendar block | User logged in, User has access to the Calendar block | 1. Navigate to the Dashboard<br>2. Locate the Calendar block<br>3. Click the left arrow to navigate to the previous month | The Calendar block updates to display the previous month with the correct month and year heading | medium |

---

## Dashboard — Edit Mode

Total: **5** (positive: 2, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Add a block to the Dashboard in Edit mode | User logged in, Edit mode is toggled on | 1. Click '+ Add a block' below the Dashboard heading<br>2. Select 'Course overview' from the list of available block types<br>3. Click 'Add' to add the block to the Dashboard | The 'Course overview' block appears on the Dashboard | high |
| TC-015 |  | Open the options menu for a block | User logged in, Edit mode is toggled on, At least one block is present on the Dashboard | 1. Click the three-dot options menu on an existing block<br>2. Select 'Configure' from the menu | The configuration settings for the selected block are displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | Attempt to add a block when Edit mode is off | User logged in, Edit mode is toggled off | 1. Click '+ Add a block' below the Dashboard heading | The '+ Add a block' button is not clickable; no action is performed | high |
| TC-016 |  | Attempt to reset the Dashboard without any blocks added | User logged in, Edit mode is toggled on, No blocks are added to the Dashboard | 1. Click 'Reset page to default' at the top right<br>2. Confirm the reset action | A message indicates that there are no changes to revert; the Dashboard remains unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 |  | Reset the Dashboard to default after adding multiple blocks | User logged in, Edit mode is toggled on, Multiple blocks are added to the Dashboard | 1. Click 'Reset page to default' at the top right<br>2. Confirm the reset action | All blocks are removed and the Dashboard returns to its default state | medium |

---

## My Courses

Total: **7** (positive: 3, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | View all courses displayed as visual cards | User logged in as Teacher | 1. Navigate to the My Courses page | All courses the teacher has access to are displayed as visual cards with course banner images, names, and category names | high |
| TC-018 |  | Search for a specific course by name | User logged in as Teacher, At least one course exists | 1. Navigate to the My Courses page<br>2. Enter <course name> in the search field<br>3. Click the search button | Only the course matching <course name> is displayed in the course cards | high |
| TC-021 |  | Star a course to pin it to the top | User logged in as Teacher, At least one course exists | 1. Navigate to the My Courses page<br>2. Click the three-dot menu on a course card<br>3. Select 'Star this course' | The starred course is pinned to the top of the course list | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | Attempt to search for a course with an empty search field | User logged in as Teacher | 1. Navigate to the My Courses page<br>2. Leave the search field empty<br>3. Click the search button | All courses are displayed as visual cards; no error is shown | medium |
| TC-022 |  | Attempt to star a course that is already starred | User logged in as Teacher, At least one course is already starred | 1. Navigate to the My Courses page<br>2. Click the three-dot menu on a starred course card<br>3. Select 'Star this course' | A message indicates that the course is already starred; no changes are made | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Sort courses with maximum number of courses displayed | User logged in as Teacher, More than 100 courses exist | 1. Navigate to the My Courses page<br>2. Select the sort dropdown and choose <sorting criteria><br>3. Observe the displayed courses | Courses are sorted according to the selected criteria, and all courses are displayed correctly | medium |
| TC-023 |  | Remove a course from view and check the remaining courses | User logged in as Teacher, At least one course exists | 1. Navigate to the My Courses page<br>2. Click the three-dot menu on a course card<br>3. Select 'Remove from view'<br>4. Refresh the My Courses page | The removed course no longer appears in the course list; other courses remain visible | medium |

---

## Course Page

Total: **5** (positive: 2, negative: 2, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 |  | View course content with all sections expanded | User logged in as Teacher, A course exists with multiple sections | 1. Navigate to the Course page<br>2. Ensure all sections are expanded | All sections are visible with activities and resources listed under each section | high |
| TC-027 |  | Collapse a specific section of the course | User logged in as Teacher, A course exists with multiple sections | 1. Navigate to the Course page<br>2. Expand a specific section<br>3. Click on the collapsible chevron of that section | The specific section collapses, hiding its activities and resources | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Attempt to view course content without being logged in |  | 1. Navigate to the Course page | User is redirected to the login page with an appropriate error message | high |
| TC-028 |  | Attempt to collapse a section that does not exist | User logged in as Teacher, A course exists | 1. Navigate to the Course page<br>2. Click on a non-existent section's collapsible chevron | No action is performed; a message indicates the section does not exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Collapse all sections when no sections are expanded | User logged in as Teacher, A course exists with all sections collapsed | 1. Navigate to the Course page<br>2. Click on the 'Collapse all' link | No change occurs; all sections remain collapsed and no error is displayed | medium |

---

## Course Edit Mode and Activity Chooser

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Enable Edit mode and access Activity Chooser | User logged in as Teacher, A course exists | 1. Navigate to the Course page<br>2. Click the 'Turn editing on' button<br>3. Click '+ Add an activity or resource' in a section | The Activity Chooser modal opens, displaying categories and activity/resource tiles | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | Attempt to add an activity without enabling Edit mode | User logged in as Teacher, A course exists | 1. Navigate to the Course page<br>2. Click '+ Add an activity or resource' in a section | An error message appears indicating that Edit mode must be enabled to add activities | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | Add multiple activities using bulk actions | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Navigate to the Course page<br>2. Click '+ Add an activity or resource' in a section<br>3. Select multiple activities from the Activity Chooser<br>4. Click 'Add' to add all selected activities | All selected activities are added to the course section successfully | medium |

---

## Assignment Creation

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Create an assignment with all required fields filled | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Navigate to the Course page<br>2. Click '+ Add an activity or resource' in the target section<br>3. Select Assignment from the Activity Chooser and click Add<br>4. Enter <assignment name> in the Assignment name field<br>5. Enter <description> in the Description field<br>6. Enable the Due date toggle and select <due date><br>7. Click 'Save and return to course' | The assignment appears in the course section with a link; the Grading summary panel shows 0 submissions | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Attempt to save an assignment without filling the required fields | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Navigate to the Course page and click '+ Add an activity or resource'<br>2. Select Assignment and click Add<br>3. Leave the Assignment name field empty<br>4. Click 'Save and return to course' | An inline validation error highlights the Assignment name field; the form is not submitted and remains open | high |
| TC-035 |  | Attempt to save an assignment with invalid file types in File submissions | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Navigate to the Course page and click '+ Add an activity or resource'<br>2. Select Assignment and click Add<br>3. Enter <assignment name><br>4. Enable File submissions and set invalid file types<br>5. Click 'Save and return to course' | An error message indicates that the file types are not accepted; the form is not submitted and remains open | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Set both Due date and Cut-off date to the same time in the past | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Open the Assignment creation form<br>2. Enter <assignment name><br>3. Enable Due date toggle and set it to <specific past date and time><br>4. Enable Cut-off date toggle and set it to the exact same past date and time as the due date<br>5. Click 'Save and return to course' | Assignment is saved successfully and appears in the course; both due and cut-off dates are identical in the assignment metadata | medium |
| TC-036 |  | Set maximum submission size to the system's maximum limit | User logged in as Teacher, A course exists and Edit mode is enabled | 1. Open the Assignment creation form<br>2. Enter <assignment name><br>3. Enable File submissions and set maximum submission size to <system maximum size><br>4. Click 'Save and return to course' | Assignment is saved successfully and appears in the course; maximum submission size is set correctly in the assignment metadata | medium |

---

## Course Settings

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | Save course settings with all required fields filled correctly | User logged in as Teacher, A course exists | 1. Navigate to the Course Settings page<br>2. Enter <course full name> in the Course full name field<br>3. Enter <course short name> in the Course short name field<br>4. Select <course category> from the Course category dropdown<br>5. Set Course visibility to <Show/Hide><br>6. Optionally set Course start date and Course end date<br>7. Click 'Save and display' | The course settings are saved successfully and the user is redirected to the course page with updated settings | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Attempt to save course settings without filling required fields | User logged in as Teacher, A course exists | 1. Navigate to the Course Settings page<br>2. Leave the Course full name field empty<br>3. Leave the Course short name field empty<br>4. Click 'Save and display' | Inline validation errors highlight the Course full name and Course short name fields; the form is not submitted and remains open | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Set maximum upload size to the system's maximum limit | User logged in as Teacher, A course exists | 1. Navigate to the Course Settings page<br>2. Enter <course full name> in the Course full name field<br>3. Enter <course short name> in the Course short name field<br>4. Select <course category> from the Course category dropdown<br>5. Set Maximum upload size to the maximum allowed value<br>6. Click 'Save and display' | The course settings are saved successfully with the maximum upload size set; the user is redirected to the course page | medium |

---

## Participants Management

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Enroll a user in the course successfully | User logged in as Teacher, A course exists with users enrolled | 1. Navigate to the Participants page of the course<br>2. Click the 'Enrol users' button<br>3. Enter a valid username in the user search field<br>4. Select a Role from the Role dropdown<br>5. Optionally set an Enrollment duration<br>6. Click 'Enrol selected users' | The user is added to the course with the specified role; the participants list updates to include the new user | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | Attempt to enroll a user without selecting a role | User logged in as Teacher, A course exists with users enrolled | 1. Navigate to the Participants page of the course<br>2. Click the 'Enrol users' button<br>3. Enter a valid username in the user search field<br>4. Leave the Role dropdown unselected<br>5. Click 'Enrol selected users' | An error message indicates that a role must be selected; the user is not enrolled | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Filter participants using multiple conditions | User logged in as Teacher, A course exists with multiple enrolled users | 1. Navigate to the Participants page of the course<br>2. Click the '+ Add condition' link<br>3. Select 'First name' from the Select attribute dropdown<br>4. Set the condition to 'Contains' and enter a common substring<br>5. Click 'Apply filters' | The participants list updates to show only users whose first names contain the specified substring; the filter conditions are displayed | medium |
| TC-043 |  | Use alphabetical filter for Last name with no results | User logged in as Teacher, A course exists with users enrolled | 1. Navigate to the Participants page of the course<br>2. Click the 'Last name' alphabetical filter button for 'Z'<br>3. Observe the participants list | The participants list shows no users; a message indicates that no users match the filter criteria | medium |

---

## Assignment — Teacher View

Total: **4** (positive: 2, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-044 |  | View assignment metadata including dates and description | User logged in as Teacher, An assignment exists in the course | 1. Navigate to the Course page<br>2. Click on the assignment link to open the Assignment page | The assignment's metadata including Opened date, Due date, full Description, and any attached files is displayed correctly | high |
| TC-045 |  | Access grading interface for an assignment | User logged in as Teacher, An assignment exists with submissions | 1. Navigate to the Course page<br>2. Click on the assignment link to open the Assignment page<br>3. Click the 'Grade' button | The grading interface opens, displaying a list of students and their submissions | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-046 |  | Attempt to view assignment metadata when no assignment exists | User logged in as Teacher, No assignments exist in the course | 1. Navigate to the Course page<br>2. Attempt to click on a non-existent assignment link | An error message is displayed indicating that the assignment does not exist | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | View assignment with maximum length description | User logged in as Teacher, An assignment exists with a description at maximum character limit | 1. Navigate to the Course page<br>2. Click on the assignment link to open the Assignment page | The assignment's metadata is displayed correctly, and the full description is visible without truncation | medium |

---

## Assignment Submissions

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | View all student submissions with default filters | User logged in as Teacher, An assignment with student submissions exists | 1. Navigate to the Assignment Submissions view<br>2. Observe the table displaying all student submission records | The table displays all student submissions with correct details in each column | high |
| TC-051 |  | Enable quick grading mode and enter grades | User logged in as Teacher, An assignment with student submissions exists | 1. Navigate to the Assignment Submissions view<br>2. Enable 'Quick grading' mode<br>3. Enter grades for multiple students directly in the table<br>4. Click 'Save changes' | Grades are saved successfully, and the table reflects the updated grades for each student | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Attempt to filter submissions with invalid student name | User logged in as Teacher, An assignment with student submissions exists | 1. Navigate to the Assignment Submissions view<br>2. Enter an invalid student name in the search field<br>3. Click the 'Search' button | The table shows no results found; a message indicates that no submissions match the search criteria | high |
| TC-052 |  | Attempt to enter invalid grade in quick grading mode | User logged in as Teacher, An assignment with student submissions exists | 1. Navigate to the Assignment Submissions view<br>2. Enable 'Quick grading' mode<br>3. Enter an invalid grade (e.g., a negative number) for a student<br>4. Click 'Save changes' | An error message appears indicating that the grade is invalid; the grade is not saved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-050 |  | Filter submissions by grading status with no submissions | User logged in as Teacher, An assignment exists with no submissions | 1. Navigate to the Assignment Submissions view<br>2. Select 'Not graded' from the grading status filter<br>3. Click the 'Filter' button | The table remains empty, and a message indicates that there are no submissions to display | medium |
| TC-053 |  | Filter submissions by submission status with maximum entries | User logged in as Teacher, An assignment exists with maximum allowed submissions | 1. Navigate to the Assignment Submissions view<br>2. Select 'Submitted for grading' from the submission status filter<br>3. Click the 'Filter' button | The table displays all submissions that match the filter criteria, even if the number is at the system's maximum limit | medium |

---

## Gradebook — Grader Report

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Switch from Grader report to User report | User logged in as Teacher, A course with enrolled students exists | 1. Navigate to the Gradebook section<br>2. Locate the report-type selector dropdown at the top left<br>3. Select 'User report' from the dropdown | The page refreshes to display the User report with the list of students and their grades | high |
| TC-057 |  | Filter students by name in the Gradebook | User logged in as Teacher, A course with enrolled students exists | 1. Navigate to the Gradebook section<br>2. Locate the user search and filter controls above the grade table<br>3. Enter a student's name in the search field<br>4. Press Enter or click the search button | The grade table updates to display only the rows corresponding to the filtered student | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-055 |  | Attempt to save a grade entry with a value outside the configured grade range | User logged in as Teacher, Edit mode is enabled, A grade entry exists | 1. Navigate to the Gradebook section<br>2. Locate the grade cell for a specific student and activity<br>3. Enter a grade value that exceeds the maximum configured grade range<br>4. Click 'Save changes' | An inline validation error highlights the grade cell; the form is not submitted and remains open | high |
| TC-058 |  | Attempt to save changes without enabling Edit mode | User logged in as Teacher, A grade entry exists | 1. Navigate to the Gradebook section<br>2. Locate the grade cell for a specific student and activity<br>3. Change the grade entry<br>4. Click 'Save changes' | An error message indicates that Edit mode must be enabled to save changes; no changes are saved | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Edit a grade entry to the minimum boundary value | User logged in as Teacher, Edit mode is enabled, A grade entry exists | 1. Navigate to the Gradebook section<br>2. Locate the grade cell for a specific student and activity<br>3. Change the grade entry to the minimum allowed value (e.g., 0)<br>4. Click 'Save changes' | The grade entry is saved successfully, and the updated value is displayed in the grade cell | medium |
| TC-059 |  | Edit multiple grade entries in quick succession | User logged in as Teacher, Edit mode is enabled, Multiple grade entries exist | 1. Navigate to the Gradebook section<br>2. Quickly change several grade entries for different students<br>3. Click 'Save changes' after editing multiple entries | All changes are saved successfully, and the updated values are displayed in the grade cells | medium |

---

## Profile

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-060 |  | View teacher's profile with all details displayed | User logged in as Teacher | 1. Navigate to the Profile page<br>2. Observe the circular initials icon, full name, and 'Message' button<br>3. Check for the presence of the profile description (if provided)<br>4. Verify the information cards for User details, Privacy and policies, Course details, Miscellaneous, Reports, and Login activity | All profile elements are displayed correctly, including the initials icon, full name, and all information cards | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Attempt to access profile without being logged in |  | 1. Navigate to the Profile page | User is redirected to the login page with an appropriate error message | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-062 |  | Profile page displays with a very long profile description | User logged in as Teacher, Profile description is set to a very long text | 1. Navigate to the Profile page<br>2. Observe the profile description section | The profile description is displayed correctly without breaking the layout; scrolling may be required to view the entire text | medium |

---

## Profile Edit

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | Update profile with all required fields filled correctly | User logged in, User is on the Edit profile page | 1. Enter 'John' in the First name field<br>2. Enter 'Doe' in the Last name field<br>3. Enter 'john.doe@example.com' in the Email address field<br>4. Select 'Show my email address' from the Email visibility dropdown<br>5. Enter '12345' in the MoodleNet profile ID field<br>6. Enter 'New York' in the City/town field<br>7. Select 'United States' from the Country dropdown<br>8. Select 'America/New_York' from the Timezone dropdown<br>9. Enter a description in the rich text editor<br>10. Click 'Update profile' | The profile is updated successfully; the user sees a confirmation message and the updated profile information. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-064 |  | Attempt to update profile without filling required fields | User logged in, User is on the Edit profile page | 1. Leave the First name field empty<br>2. Leave the Last name field empty<br>3. Leave the Email address field empty<br>4. Click 'Update profile' | Validation errors are displayed for First name, Last name, and Email address fields; the form is not submitted. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Upload a user picture with maximum file size limit | User logged in, User is on the Edit profile page | 1. Prepare a user picture file that is at the maximum allowed size<br>2. Drag and drop the picture file into the upload area<br>3. Enter a description in the Picture description field<br>4. Click 'Update profile' | The profile is updated successfully; the new picture is displayed with the provided description. | medium |
| TC-066 |  | Enter a very long description in the rich text editor | User logged in, User is on the Edit profile page | 1. Enter 'John' in the First name field<br>2. Enter 'Doe' in the Last name field<br>3. Enter 'john.doe@example.com' in the Email address field<br>4. Enter a very long text (exceeding typical limits) in the Description field<br>5. Click 'Update profile' | The profile is updated successfully; the long description is saved and displayed correctly. | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Successfully log out of the system | User logged in as Teacher | 1. Click on the 'Log out' button in the user menu<br>2. Wait for the page to redirect | User is redirected to the login page; the session is terminated and the user is no longer authenticated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Attempt to access a protected page after logging out | User logged in as Teacher, User has logged out | 1. Try to navigate to a protected page (e.g., Course page)<br>2. Observe the response | User is redirected to the login page; access to the protected page is denied | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-069 |  | Log out while performing an action | User logged in as Teacher, User is in the middle of creating an assignment | 1. Start creating an assignment<br>2. Click on the 'Log out' button in the user menu<br>3. Wait for the page to redirect | User is redirected to the login page; the assignment creation process is terminated and no data is saved | medium |

---
