# Test Cases — MoodleTeacher

Generated: 2026-06-04T15:09:05.207313Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 97 | 27 | 31 | 39 | 43 | 39 | 15 |

## Login

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User has a valid username and password. | 1. Navigate to the login page.<br>2. Enter valid username.<br>3. Enter valid password.<br>4. Click on the 'Log in' button. | User is redirected to the Dashboard. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login attempt with invalid username | User is on the login page. | 1. Enter an invalid username.<br>2. Enter a valid password.<br>3. Click on the 'Log in' button. | Inline error message is displayed, password field is cleared, and username is retained. | high |
| TC-003 |  | Login attempt with invalid password | User is on the login page. | 1. Enter a valid username.<br>2. Enter an invalid password.<br>3. Click on the 'Log in' button. | Inline error message is displayed, password field is cleared, and username is retained. | high |
| TC-004 |  | Login attempt with empty fields | User is on the login page. | 1. Leave the username field empty.<br>2. Leave the password field empty.<br>3. Click on the 'Log in' button. | Inline error message is displayed for both fields, and both fields remain empty. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Login attempt with maximum length username and password | User is on the login page. | 1. Enter a username with maximum allowed length.<br>2. Enter a password with maximum allowed length.<br>3. Click on the 'Log in' button. | User is redirected to the Dashboard if credentials are valid. | medium |
| TC-006 |  | Login attempt with special characters in username and password | User is on the login page. | 1. Enter a username with special characters.<br>2. Enter a password with special characters.<br>3. Click on the 'Log in' button. | User is redirected to the Dashboard if credentials are valid. | medium |
| TC-007 |  | Login attempt with whitespace in username and password | User is on the login page. | 1. Enter a username with leading and trailing whitespace.<br>2. Enter a password with leading and trailing whitespace.<br>3. Click on the 'Log in' button. | User is redirected to the Dashboard if credentials are valid after trimming whitespace. | medium |

---

## Dashboard

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Display personalized greeting | User is logged in | 1. Navigate to the Dashboard. | The personalized greeting is displayed at the top of the Dashboard. | high |
| TC-009 |  | View upcoming teaching actions in Timeline block | User is logged in, User is enrolled in courses | 1. Navigate to the Dashboard.<br>2. Select a time range from the dropdown. | The Timeline block displays upcoming teaching actions for the selected time range. | high |
| TC-014 |  | Create a new calendar event | User is logged in | 1. Navigate to the Dashboard.<br>2. Click on the 'New event' button.<br>3. Fill in the event details.<br>4. Save the event. | The new event is created and displayed in the Calendar block. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | No items in selected time range | User is logged in, User is enrolled in courses | 1. Navigate to the Dashboard.<br>2. Select a time range with no upcoming actions. | An empty state message is shown in the Timeline block. | medium |
| TC-011 |  | Search for non-existent activity | User is logged in, User is enrolled in courses | 1. Navigate to the Dashboard.<br>2. Enter a non-existent activity name in the search field.<br>3. Click the search button. | No results found message is displayed. | medium |
| TC-015 |  | Attempt to create a calendar event with missing details | User is logged in | 1. Navigate to the Dashboard.<br>2. Click on the 'New event' button.<br>3. Leave required fields empty.<br>4. Attempt to save the event. | An error message is displayed indicating that required fields must be filled. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Select maximum time range | User is logged in, User is enrolled in courses | 1. Navigate to the Dashboard.<br>2. Select the maximum time range from the dropdown. | The Timeline block displays all upcoming teaching actions within the maximum time range. | low |
| TC-013 |  | Navigate to previous month in Calendar block | User is logged in | 1. Navigate to the Dashboard.<br>2. Click the left arrow to go to the previous month. | The Calendar block updates to show the previous month with the correct events highlighted. | low |
| TC-016 |  | Filter events by course with no events | User is logged in, User is enrolled in courses | 1. Navigate to the Dashboard.<br>2. Select a course from the 'All courses' dropdown that has no events. | The Calendar block shows no events for the selected course. | low |

---

## Dashboard — Edit Mode

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Toggle Edit Mode and Add a Block | User is logged in, User is on the Dashboard | 1. Toggle Edit mode on.<br>2. Click on '+ Add a block' button.<br>3. Select 'Comments' from the list of available block types. | The 'Comments' block is added to the Dashboard. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | Attempt to Add a Block in View Mode | User is logged in, User is on the Dashboard, Edit mode is off | 1. Click on '+ Add a block' button. | The '+ Add a block' button is not visible or clickable. | high |
| TC-019 |  | Cancel Adding a Block | User is logged in, User is in Edit mode | 1. Click on '+ Add a block' button.<br>2. Click on 'Cancel' link. | User is returned to the Dashboard without adding a block. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Reset Page to Default | User is logged in, User has added multiple blocks in Edit mode | 1. Click on 'Reset page to default' button. | All blocks are removed and the Dashboard is reset to its default state. | high |
| TC-021 |  | Add Maximum Number of Blocks | User is logged in, User is in Edit mode | 1. Click on '+ Add a block' button.<br>2. Add blocks until the maximum limit is reached. | User is able to add blocks up to the maximum limit without errors. | medium |
| TC-022 |  | Check Move Icon and Options Menu | User is logged in, User is in Edit mode, At least one block is present | 1. Hover over an existing block.<br>2. Check for the presence of the move icon and three-dot options menu. | The move icon and options menu are visible for the block. | low |

---

## My Courses

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 |  | View all courses | User is logged in as a teacher, User has access to courses | 1. Navigate to the My Courses page.<br>2. Observe the displayed course cards. | All courses the teacher has access to are displayed as visual cards with course banner images, names, and categories. | high |
| TC-024 |  | Search for a specific course | User is on the My Courses page, At least one course exists | 1. Enter a valid course name in the search field.<br>2. Click the search button. | The course matching the search term is displayed in the course cards. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Search with an invalid course name | User is on the My Courses page | 1. Enter an invalid course name in the search field.<br>2. Click the search button. | No courses are displayed, and a message indicating no results found is shown. | high |
| TC-026 |  | Remove a course from view | User is on the My Courses page, At least one course is visible | 1. Click the three-dot menu on a course card.<br>2. Select 'Remove from view'. | The selected course is hidden from the view but remains enrolled. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 |  | Star a course | User is on the My Courses page, At least one course is visible | 1. Click the three-dot menu on a course card.<br>2. Select 'Star this course'. | The selected course is pinned to the top of the course list. | medium |
| TC-028 |  | Change layout to List | User is on the My Courses page | 1. Click on the layout dropdown.<br>2. Select 'List'. | The course cards are displayed in a list format. | low |
| TC-029 |  | Change layout to Summary | User is on the My Courses page | 1. Click on the layout dropdown.<br>2. Select 'Summary'. | The course cards are displayed in a summary format. | low |
| TC-030 |  | Select status filter | User is on the My Courses page, At least one course exists in each status category | 1. Click on the status dropdown.<br>2. Select 'In progress'. | Only courses that are currently in progress are displayed. | medium |

---

## Course Page

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-031 |  | View course content with all sections expanded | User is logged in, User has access to the course | 1. Navigate to the Course page.<br>2. Expand all sections. | All sections are expanded, displaying all activities and resources. | high |
| TC-032 |  | Collapse all sections | User is logged in, User has access to the course, At least one section is expanded | 1. Navigate to the Course page.<br>2. Click on the 'Collapse all' link. | All sections are collapsed. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Access course page without permission | User is logged out or does not have access | 1. Attempt to navigate to the Course page. | User is shown an error message indicating lack of access. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | View course page with maximum number of sections | User is logged in, User has access to the course with maximum sections | 1. Navigate to the Course page. | All sections are displayed correctly without performance issues. | medium |
| TC-035 |  | View course page with empty sections | User is logged in, User has access to the course with empty sections | 1. Navigate to the Course page. | Sections are displayed with appropriate messages indicating no content available. | low |

---

## Course Edit Mode and Activity Chooser

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Enable Edit Mode | User is logged in, User has permission to edit the course | 1. Navigate to the Course page.<br>2. Click on the 'Enable Edit Mode' button. | The Course page transforms into an authoring interface with inline controls visible. | high |
| TC-037 |  | Add an Activity | Edit Mode is enabled, User is on the Course page | 1. Click on '+ Add an activity or resource' button.<br>2. Select 'Assignment' from the Activity Chooser modal.<br>3. Click 'Add'. | The Assignment creation form opens. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-038 |  | Attempt to Add Activity without Edit Mode | User is logged in, User is on the Course page, Edit Mode is not enabled | 1. Click on '+ Add an activity or resource' button. | The system shows an error message indicating that Edit Mode must be enabled to add activities. | high |
| TC-039 |  | Add Activity with Empty Search | Edit Mode is enabled, User is on the Activity Chooser modal | 1. Leave the search field empty.<br>2. Click 'Search'. | The system displays all available activities/resources in the grid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Add Activity with Maximum Length Name | Edit Mode is enabled, User is on the Course page | 1. Click on '+ Add an activity or resource' button.<br>2. Select 'Page' from the Activity Chooser modal.<br>3. Enter a name with maximum allowed characters in the name field.<br>4. Click 'Add'. | The Page creation form opens with the name correctly displayed. | medium |
| TC-041 |  | Add Activity with Special Characters | Edit Mode is enabled, User is on the Course page | 1. Click on '+ Add an activity or resource' button.<br>2. Select 'Forum' from the Activity Chooser modal.<br>3. Enter a name with special characters (e.g., @#$%^&*) in the name field.<br>4. Click 'Add'. | The Forum creation form opens with the name correctly displayed. | low |

---

## Assignment Creation

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Create assignment with all valid fields | User is logged in, User has selected 'Assignment' from the Activity Chooser | 1. Enter a valid assignment name.<br>2. Fill in the description using the rich text editor.<br>3. Upload an additional file (optional).<br>4. Set the availability dates and enable them.<br>5. Select submission types and configure settings.<br>6. Set feedback types and submission settings.<br>7. Configure group submission settings.<br>8. Set notifications and grading options.<br>9. Add tags and competencies.<br>10. Click 'Save and return to course'. | The assignment is created successfully and the user is redirected to the course page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Create assignment without assignment name | User is logged in, User has selected 'Assignment' from the Activity Chooser | 1. Leave the assignment name field empty.<br>2. Fill in the description using the rich text editor.<br>3. Click 'Save and return to course'. | An error message is displayed indicating that the assignment name is required. | high |
| TC-044 |  | Create assignment with invalid file type | User is logged in, User has selected 'Assignment' from the Activity Chooser | 1. Enter a valid assignment name.<br>2. Upload a file with an unsupported file type.<br>3. Click 'Save and return to course'. | An error message is displayed indicating that the file type is not accepted. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Create assignment with maximum length assignment name | User is logged in, User has selected 'Assignment' from the Activity Chooser | 1. Enter an assignment name that is at the maximum allowed character length.<br>2. Fill in the description using the rich text editor.<br>3. Click 'Save and return to course'. | The assignment is created successfully and the user is redirected to the course page. | medium |
| TC-046 |  | Create assignment with no description and no additional files | User is logged in, User has selected 'Assignment' from the Activity Chooser | 1. Enter a valid assignment name.<br>2. Leave the description empty.<br>3. Do not upload any additional files.<br>4. Click 'Save and return to course'. | The assignment is created successfully with the assignment name only, and the user is redirected to the course page. | low |

---

## Course Settings

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Successfully save course settings with valid inputs | User is logged in, User has access to Course Settings | 1. Navigate to Course Settings.<br>2. Fill in the Course full name with 'Introduction to Testing'.<br>3. Fill in the Course short name with 'IT101'.<br>4. Select a Course category from the dropdown.<br>5. Set Course visibility to 'Show'.<br>6. Enter a Course start date.<br>7. Enter a Course end date.<br>8. Fill in the Course ID number with 'IT101-001'.<br>9. Enter a Course summary.<br>10. Upload a Course image.<br>11. Select a Course format.<br>12. Adjust appearance settings as needed.<br>13. Click on 'Save and display'. | The course settings are saved successfully, and the user is redirected to the course page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-048 |  | Fail to save course settings with missing required fields | User is logged in, User has access to Course Settings | 1. Navigate to Course Settings.<br>2. Leave the Course full name field empty.<br>3. Leave the Course short name field empty.<br>4. Click on 'Save and display'. | An error message is displayed indicating that the Course full name and Course short name are required. | high |
| TC-050 |  | Fail to save course settings with invalid date range | User is logged in, User has access to Course Settings | 1. Navigate to Course Settings.<br>2. Enter a Course start date that is after the Course end date.<br>3. Click on 'Save and display'. | An error message is displayed indicating that the Course start date must be before the Course end date. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Test maximum length for Course full name | User is logged in, User has access to Course Settings | 1. Navigate to Course Settings.<br>2. Fill in the Course full name with a string of 255 characters.<br>3. Fill in the Course short name with 'IT101'.<br>4. Select a Course category from the dropdown.<br>5. Set Course visibility to 'Show'.<br>6. Click on 'Save and display'. | The course settings are saved successfully, and the user is redirected to the course page. | medium |
| TC-051 |  | Test empty fields for optional inputs | User is logged in, User has access to Course Settings | 1. Navigate to Course Settings.<br>2. Fill in the Course full name with 'Introduction to Testing'.<br>3. Fill in the Course short name with 'IT101'.<br>4. Select a Course category from the dropdown.<br>5. Leave Course summary empty.<br>6. Leave Course image upload empty.<br>7. Click on 'Save and display'. | The course settings are saved successfully, and the user is redirected to the course page, with optional fields left empty. | medium |

---

## Participants Management

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | Filter participants by enrollment context | User is on the Participants page | 1. Select an enrollment context from the dropdown<br>2. Click 'Apply filters' | The participants list updates to show only users enrolled in the selected context | high |
| TC-053 |  | Enroll a user successfully | User is on the Participants page, User clicks 'Enrol users' | 1. Enter a valid user in the search field<br>2. Select a role from the Role dropdown<br>3. Click 'Confirm' | The user is added to the course with the specified role | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Attempt to enroll a user without selecting a role | User is on the Enrol users dialog | 1. Enter a valid user in the search field<br>2. Leave the Role dropdown unselected<br>3. Click 'Confirm' | An error message is displayed indicating that a role must be selected | high |
| TC-055 |  | Filter participants with no conditions | User is on the Participants page | 1. Click 'Apply filters' without adding any conditions | An error message is displayed indicating that at least one condition must be added | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Filter participants with maximum length name | User is on the Participants page | 1. Enter a name with maximum allowed characters in the filter<br>2. Click 'Apply filters' | The participants list updates correctly to show users matching the maximum length name | medium |
| TC-057 |  | Bulk action with no users selected | User is on the Participants page | 1. Click on the 'With selected users...' dropdown<br>2. Select an action | An error message is displayed indicating that no users are selected for the action | medium |
| TC-058 |  | Search for a user with special characters | User is on the Enrol users dialog | 1. Enter a user name with special characters in the search field<br>2. Click 'Search' | The search results display users matching the special character input | low |

---

## Assignment — Teacher View

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-059 |  | View assignment metadata | User is logged in as a teacher, An assignment exists | 1. Navigate to the Assignment page.<br>2. Observe the assignment's metadata. | The assignment's Opened date, Due date, Description, and attached files are displayed correctly. | high |
| TC-060 |  | Open grading interface | User is logged in as a teacher, An assignment exists | 1. Navigate to the Assignment page.<br>2. Click on the 'Grade' button. | The grading interface for individual students opens successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Attempt to view assignment without being logged in | User is not logged in | 1. Attempt to navigate to the Assignment page. | User is redirected to the login page with an appropriate error message. | high |
| TC-062 |  | Check grading interface without submissions | User is logged in as a teacher, An assignment exists with no submissions | 1. Navigate to the Assignment page.<br>2. Click on the 'Grade' button. | The grading interface opens, but indicates that there are no submissions to grade. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-063 |  | View assignment with maximum length description | User is logged in as a teacher, An assignment exists with a maximum length description | 1. Navigate to the Assignment page. | The assignment's metadata, including the maximum length description, is displayed correctly without truncation. | medium |
| TC-064 |  | View assignment with no attached files | User is logged in as a teacher, An assignment exists with no attached files | 1. Navigate to the Assignment page. | The assignment's metadata is displayed correctly, indicating that there are no attached files. | low |
| TC-065 |  | Check grading summary panel with zero submissions | User is logged in as a teacher, An assignment exists with zero submissions | 1. Navigate to the Assignment page. | The grading summary panel shows 'Number of submissions: 0' and other metrics are displayed correctly. | medium |

---

## Assignment Submissions

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-066 |  | Search by student name | User is logged in, There are submissions in the system | 1. Navigate to the Submissions view<br>2. Enter a valid student name in the search field<br>3. Click the search button | The table displays only the submissions for the specified student | high |
| TC-069 |  | Filter by submission status | User is logged in, There are submissions with various statuses | 1. Navigate to the Submissions view<br>2. Select a submission status from the filter dropdown<br>3. Click the filter button | The table displays only the submissions with the selected status | high |
| TC-072 |  | Enable Quick grading mode | User is logged in, User has grading permissions | 1. Navigate to the Submissions view<br>2. Click on the 'Enable Quick grading' toggle | The table allows inline grade entry for each submission | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Search with invalid student name | User is logged in | 1. Navigate to the Submissions view<br>2. Enter an invalid student name in the search field<br>3. Click the search button | An error message is displayed indicating no submissions found | high |
| TC-070 |  | Filter with no selection | User is logged in | 1. Navigate to the Submissions view<br>2. Do not select any submission status<br>3. Click the filter button | An error message is displayed indicating that a selection is required | medium |
| TC-073 |  | Attempt to grade without permissions | User is logged in, User does not have grading permissions | 1. Navigate to the Submissions view<br>2. Try to enable Quick grading mode | An error message is displayed indicating insufficient permissions | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-068 |  | Search with empty student name | User is logged in | 1. Navigate to the Submissions view<br>2. Leave the search field empty<br>3. Click the search button | The table displays all submissions without any filtering | medium |
| TC-071 |  | Filter with maximum length of submission status | User is logged in | 1. Navigate to the Submissions view<br>2. Enter a submission status with maximum allowed characters<br>3. Click the filter button | The table displays submissions matching the maximum length status | low |
| TC-074 |  | Inline grading with maximum grade value | User is logged in, Quick grading mode is enabled | 1. Navigate to the Submissions view<br>2. Enter the maximum grade value in the inline grading field<br>3. Save the changes | The grade is saved successfully and displayed correctly in the table | medium |

---

## Gradebook — Grader Report

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-075 |  | Switch to User report | User is logged in, User is on the Grader report page | 1. Click on the report-type selector dropdown<br>2. Select 'User report' from the dropdown | The page refreshes to display the User report view. | high |
| TC-076 |  | Edit a grade entry | User is logged in, User is in Edit mode, Grade cells are editable | 1. Locate a grade cell for a student<br>2. Click on the cell and enter a new valid grade<br>3. Click on 'Save changes' | The new grade is saved and displayed in the grade cell. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-077 |  | Attempt to save an invalid grade | User is logged in, User is in Edit mode, Grade cells are editable | 1. Locate a grade cell for a student<br>2. Click on the cell and enter an invalid grade (e.g., below minimum range)<br>3. Click on 'Save changes' | An error message is displayed indicating the grade is out of range and the grade is not saved. | high |
| TC-078 |  | Leave grade cell empty and save | User is logged in, User is in Edit mode, Grade cells are editable | 1. Locate a grade cell for a student<br>2. Click on the cell and delete the existing grade<br>3. Click on 'Save changes' | An error message is displayed indicating that the grade cannot be empty and the grade is not saved. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-079 |  | Enter maximum length grade | User is logged in, User is in Edit mode, Grade cells are editable | 1. Locate a grade cell for a student<br>2. Click on the cell and enter a grade at the maximum allowed length<br>3. Click on 'Save changes' | The grade is saved successfully and displayed in the grade cell. | medium |
| TC-080 |  | Filter by student name with no results | User is logged in, User is on the Grader report page | 1. Enter a non-existent student name in the user search field<br>2. Click on the filter button | The grade table displays no results found message. | medium |
| TC-081 |  | Switch to Overview report and back | User is logged in, User is on the Grader report page | 1. Click on the report-type selector dropdown<br>2. Select 'Overview report' from the dropdown<br>3. Click on the report-type selector dropdown again<br>4. Select 'Grader report' from the dropdown | The page refreshes to display the Grader report view again. | low |

---

## Profile

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-082 |  | View Profile with Complete Information | User is logged in, User has a complete profile | 1. Navigate to the Profile page.<br>2. Observe the displayed information. | The profile displays the teacher's initials icon, full name, message button, and complete profile description. | high |
| TC-085 |  | Access All Information Cards | User is logged in | 1. Navigate to the Profile page.<br>2. Click on each information card. | Each information card (User details, Privacy and policies, Course details, Miscellaneous, Reports, Login activity) is accessible and displays the correct information. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-083 |  | Attempt to View Profile When Not Logged In | User is not logged in | 1. Navigate to the Profile page. | The system redirects to the login page with an error message indicating that login is required. | high |
| TC-086 |  | Edit Profile with Invalid Email Format | User is logged in, User is on the Profile page | 1. Click on 'Edit profile' link.<br>2. Enter an invalid email format in the email field.<br>3. Save changes. | The system shows an error message indicating that the email format is invalid. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-084 |  | View Profile with No Profile Description | User is logged in, User has no profile description | 1. Navigate to the Profile page. | The profile displays the teacher's initials icon, full name, and a message button, but the profile description section is empty. | medium |
| TC-087 |  | View Profile with Maximum Length Description | User is logged in, User has a profile description at maximum length | 1. Navigate to the Profile page. | The profile displays the teacher's initials icon, full name, message button, and the profile description is fully visible without truncation. | medium |
| TC-088 |  | View Profile with No Login Activity | User is logged in, User has never accessed the site | 1. Navigate to the Profile page. | The Login activity section shows 'No login activity recorded.' | low |

---

## Profile Edit

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-089 |  | Successfully update profile with valid data | User is logged in, User is on the Edit Profile page | 1. Fill in First name with 'John'<br>2. Fill in Last name with 'Doe'<br>3. Fill in Email address with 'john.doe@example.com'<br>4. Select Email visibility as 'Public'<br>5. Fill in MoodleNet profile ID with '123456'<br>6. Fill in City/town with 'New York'<br>7. Select Country as 'United States'<br>8. Select Timezone as 'GMT-5'<br>9. Enter Description in the rich text editor<br>10. Upload a new user picture<br>11. Fill in Picture description with 'Profile picture'<br>12. Click on 'Update profile' | Profile is updated successfully and the profile page is refreshed with the new data. | high |
| TC-094 |  | Cancel profile edit without saving changes | User is logged in, User is on the Edit Profile page | 1. Make changes to the profile fields<br>2. Click on 'Cancel' | User is redirected to the profile page without any changes being saved. | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-090 |  | Fail to update profile with missing required fields | User is logged in, User is on the Edit Profile page | 1. Leave First name empty<br>2. Leave Last name empty<br>3. Leave Email address empty<br>4. Click on 'Update profile' | Error messages are displayed for First name, Last name, and Email address indicating they are required. | high |
| TC-091 |  | Fail to update profile with invalid email format | User is logged in, User is on the Edit Profile page | 1. Fill in First name with 'John'<br>2. Fill in Last name with 'Doe'<br>3. Fill in Email address with 'john.doe'<br>4. Click on 'Update profile' | An error message is displayed indicating the email format is invalid. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-092 |  | Update profile with maximum length fields | User is logged in, User is on the Edit Profile page | 1. Fill in First name with a string of 255 characters<br>2. Fill in Last name with a string of 255 characters<br>3. Fill in Email address with a valid email of 255 characters<br>4. Fill in Description with a string of 2000 characters<br>5. Click on 'Update profile' | Profile is updated successfully without any errors despite maximum length inputs. | medium |
| TC-093 |  | Upload a large image file | User is logged in, User is on the Edit Profile page | 1. Click on the upload area for user picture<br>2. Select an image file larger than the allowed limit<br>3. Click on 'Update profile' | An error message is displayed indicating the file size exceeds the limit. | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-095 |  | Successful logout | User is logged into the application. | 1. Click on the 'Log out' button.<br>2. Observe the redirection. | User is redirected to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-096 |  | Logout without being logged in | User is not logged into the application. | 1. Attempt to click on the 'Log out' button. | Logout button is disabled or not visible. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-097 |  | Session timeout before logout | User is logged into the application., User's session is set to timeout. | 1. Wait for the session to timeout.<br>2. Click on the 'Log out' button. | User is redirected to the login page with a session timeout message. | medium |

---
