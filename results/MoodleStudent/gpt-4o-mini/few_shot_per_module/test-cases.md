# Test Cases — MoodleStudent

Generated: 2026-06-04T15:11:53.185615Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 45 | 13 | 15 | 17 | 24 | 21 | 0 |

## Login

Total: **6** (positive: 1, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Log in with valid credentials | A registered student account exists with valid credentials | 1. Navigate to the Moodle login page<br>2. Enter <valid username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | User is redirected to the Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Log in with an empty username and password |  | 1. Navigate to the Moodle login page<br>2. Leave the Username field empty<br>3. Leave the Password field empty<br>4. Click 'Log in' | An inline error message is displayed; both fields are cleared | high |
| TC-003 |  | Log in with an invalid username |  | 1. Navigate to the Moodle login page<br>2. Enter <invalid username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | An inline error message is displayed; the Password field is cleared; the Username field retains the entered value | high |
| TC-004 |  | Log in with an invalid password | A registered student account exists | 1. Navigate to the Moodle login page<br>2. Enter <valid username> in the Username field<br>3. Enter <invalid password> in the Password field<br>4. Click 'Log in' | An inline error message is displayed; the Password field is cleared; the Username field retains the entered value | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Log in with a username at maximum length | A registered student account exists with maximum length username | 1. Navigate to the Moodle login page<br>2. Enter <maximum length username> in the Username field<br>3. Enter <valid password> in the Password field<br>4. Click 'Log in' | User is redirected to the Dashboard | medium |
| TC-006 |  | Log in with a password at maximum length | A registered student account exists with maximum length password | 1. Navigate to the Moodle login page<br>2. Enter <valid username> in the Username field<br>3. Enter <maximum length password> in the Password field<br>4. Click 'Log in' | User is redirected to the Dashboard | medium |

---

## Dashboard

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | View the Dashboard with upcoming activities displayed | User logged in as Student, User is enrolled in courses with upcoming activities | 1. Navigate to the Dashboard | The Dashboard displays a personalized greeting, and the Timeline block shows upcoming activities and deadlines. | high |
| TC-010 |  | Create a new event in the Calendar block | User logged in as Student | 1. Navigate to the Dashboard<br>2. In the Calendar block, click on the 'New event' button<br>3. Fill in the event details and save | The new event appears in the Calendar block for the selected date. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Attempt to filter the Timeline block with an invalid course selection | User logged in as Student, User is enrolled in courses | 1. Navigate to the Dashboard<br>2. In the Timeline block, select an invalid course from the 'All courses' dropdown | An inline error message is displayed indicating the course selection is invalid; the Timeline block does not update. | high |
| TC-011 |  | Attempt to create a new event without filling in required fields | User logged in as Student | 1. Navigate to the Dashboard<br>2. In the Calendar block, click on the 'New event' button<br>3. Leave required fields empty and click 'Save' | An inline error message is displayed indicating required fields must be filled. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Filter the Timeline block with a date range that contains no upcoming activities | User logged in as Student, No activities are due within the next 7 days | 1. Navigate to the Dashboard<br>2. In the Timeline block, select 'Next 7 days' from the time range dropdown | The Timeline block displays an empty state message indicating no upcoming activities within the selected range. | medium |
| TC-012 |  | Navigate to the Calendar block using left/right arrows at month boundaries | User logged in as Student | 1. Navigate to the Dashboard<br>2. In the Calendar block, click the left arrow to go to the previous month<br>3. Click the right arrow to return to the current month | The Calendar block updates to show the previous month and then returns to the current month correctly. | medium |

---

## My Courses

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 |  | View all enrolled courses as visual cards | User logged in as Student, User is enrolled in multiple courses | 1. Navigate to the My Courses page | All enrolled courses are displayed as visual cards with course banner images, names, and category names | high |
| TC-014 |  | Click on a course name to navigate to the course page | User logged in as Student, At least one course is displayed on the My Courses page | 1. Navigate to the My Courses page<br>2. Click on the course name of any displayed course | User is navigated to the main page of the selected course | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 |  | Attempt to use the search field with an empty input | User logged in as Student, Multiple courses are displayed on the My Courses page | 1. Navigate to the My Courses page<br>2. Leave the search field empty<br>3. Click the search button | All courses remain displayed without any filtering applied | medium |
| TC-016 |  | Attempt to star a course that is already starred | User logged in as Student, At least one course is starred | 1. Navigate to the My Courses page<br>2. Click the three-dot menu on a starred course<br>3. Select 'Star this course' again | No change occurs; the course remains starred and a message indicates it is already starred | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 |  | Filter courses using the status dropdown with 'Hidden' | User logged in as Student, At least one course is hidden | 1. Navigate to the My Courses page<br>2. Select 'Hidden' from the status dropdown | Only hidden courses are displayed, or a message indicates no hidden courses if none exist | medium |
| TC-018 |  | Sort courses by name when there are multiple courses with similar names | User logged in as Student, Multiple courses with similar names are displayed | 1. Navigate to the My Courses page<br>2. Select 'Sort by name' from the sort dropdown | Courses are displayed in alphabetical order, with similar names grouped together | medium |

---

## Course Page

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 |  | View course content on the Course page | User logged in as Student, User is enrolled in a course | 1. Navigate to the Course page from the Dashboard<br>2. Observe the course name displayed as the page heading<br>3. Check the navigation tab bar is present<br>4. Expand a section by clicking the chevron next to the section name | The section expands to show the activities and resources listed within it | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | Attempt to enable Edit mode on the Course page | User logged in as Student, User is on the Course page | 1. Look for an 'Edit' button or link on the Course page | No 'Edit' button or link is present; the user cannot enable Edit mode | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 |  | Collapse all sections on the Course page | User logged in as Student, Multiple sections are expanded on the Course page | 1. Navigate to the Course page<br>2. Click the 'Collapse all' link at the top right | All sections collapse, and only section names are visible without any activities or resources displayed | medium |
| TC-022 |  | View a section with no activities or resources | User logged in as Student, User is enrolled in a course with at least one section that has no activities or resources | 1. Navigate to the Course page<br>2. Expand the section that contains no activities or resources | The section expands but displays a message indicating that there are no activities or resources available | medium |

---

## Participants

Total: **5** (positive: 2, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-023 |  | View the Participants page with all enrolled users | User logged in as Student, User is enrolled in a course | 1. Navigate to the Participants page from the Course page | The Participants page displays a list of all enrolled users with their First/Last names, Roles, Groups, and Last access information | high |
| TC-024 |  | Filter participants by First name using alphabetical filter | User logged in as Student, Participants page is open | 1. Click on the 'A' button in the First name alphabetical filter | The Participants table displays only users whose First names start with 'A' | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-025 |  | Attempt to apply filters without selecting any conditions | User logged in as Student, Participants page is open | 1. Click 'Apply filters' without adding any conditions | An error message is displayed indicating that at least one condition must be selected to apply filters | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | Apply filters with the 'Any' toggle and no specific conditions | User logged in as Student, Participants page is open | 1. Toggle the 'Any' option<br>2. Click 'Apply filters' | The Participants table displays all enrolled users as no specific conditions were applied | medium |
| TC-027 |  | Sort participants by Last name in descending order | User logged in as Student, Participants page is open | 1. Click on the Last name column header to sort in descending order | The Participants table displays users sorted by Last name in descending order | medium |

---

## Grades

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-028 |  | View own grades on the Grades page | User logged in as Student, At least one graded activity exists in the course | 1. Navigate to the Grades page from the Course page<br>2. Observe the grade table displaying the Grade items, Calculated weight, Grade, Range, Percentage, Feedback, and Contribution to course total | The Grades page displays the student's own grades correctly with all relevant columns populated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Attempt to access another student's grades | User logged in as Student, Another student has grades in the course | 1. Navigate to the Grades page<br>2. Attempt to access the full gradebook or another student's grades | An error message is displayed indicating that the user does not have permission to view other students' grades | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | View grades when no graded activities exist | User logged in as Student, No graded activities exist in the course | 1. Navigate to the Grades page | The Grades page displays a message indicating that there are no grades available for the student | medium |
| TC-031 |  | View grades with maximum number of graded activities | User logged in as Student, The maximum number of graded activities is present in the course | 1. Navigate to the Grades page | The Grades page displays all graded activities correctly without any layout issues or truncation | medium |

---

## Assignment

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Submit an assignment with both online text and file upload | User logged in as Student, An assignment with online text and file submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <submission text> in the online text editor<br>4. Upload a valid file in the file upload area<br>5. Click 'Save changes' | Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the submission time | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-033 |  | Attempt to submit an assignment after the due date | User logged in as Student, An assignment is past its due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <submission text> in the online text editor<br>4. Click 'Save changes' | An error message is displayed indicating that submissions are no longer accepted | high |
| TC-035 |  | Attempt to submit an assignment without any content | User logged in as Student, An assignment with online text submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Leave the online text editor empty<br>4. Click 'Save changes' | An error message is displayed indicating that submission cannot be empty | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Submit an assignment with maximum length text in the online text editor | User logged in as Student, An assignment with online text submission is open and within the due date | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <maximum length submission text> in the online text editor<br>4. Click 'Save changes' | Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the submission time | medium |
| TC-036 |  | View submission status after editing submission just before due date | User logged in as Student, An assignment is open and due in 1 minute | 1. Navigate to the Assignment page from the Course page<br>2. Click 'Add submission'<br>3. Enter <initial submission text> in the online text editor<br>4. Click 'Save changes'<br>5. Quickly edit the submission to <edited submission text><br>6. Click 'Save changes' | Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the latest submission time | medium |

---

## Activities

Total: **4** (positive: 2, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-037 |  | View the Activities page with all sections displayed correctly | User logged in as Student, User is enrolled in a course with activities | 1. Navigate to the Activities page from the Course page | The Activities page displays the Assignments section expanded with a table showing Name, Due date, and Submission status; Forums and Resources sections are collapsed. | high |
| TC-038 |  | Expand the Forums section to view its activities | User logged in as Student, User is enrolled in a course with forum activities | 1. Navigate to the Activities page from the Course page<br>2. Click the arrow to expand the Forums section | The Forums section expands to display a list of forum activities available in the course. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | Attempt to access an activity that does not exist | User logged in as Student, User is enrolled in a course | 1. Navigate to the Activities page from the Course page<br>2. Click on a non-existent activity link | An error message is displayed indicating that the activity does not exist or is unavailable. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Check the Activities page with no activities available | User logged in as Student, User is enrolled in a course with no activities | 1. Navigate to the Activities page from the Course page | The Activities page displays a message indicating that there are no activities available in the course. | medium |

---

## Profile

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | Update profile with valid information | User logged in as Student, User is on the Profile page | 1. Click 'Edit profile'<br>2. Fill in all required fields with valid data<br>3. Click 'Update profile' | Profile is updated successfully; a confirmation message is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-042 |  | Attempt to update profile with missing required fields | User logged in as Student, User is on the Profile page | 1. Click 'Edit profile'<br>2. Leave required fields empty<br>3. Click 'Update profile' | Error messages are displayed for each missing required field; profile is not updated | high |
| TC-045 |  | Attempt to update profile with invalid email format | User logged in as Student, User is on the Profile page | 1. Click 'Edit profile'<br>2. Enter an invalid email format in the Email address field<br>3. Click 'Update profile' | An error message is displayed indicating the email format is invalid; profile is not updated | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-043 |  | Update profile with maximum length description | User logged in as Student, User is on the Profile page | 1. Click 'Edit profile'<br>2. Fill in the Description field with maximum allowed characters<br>3. Click 'Update profile' | Profile is updated successfully; the description displays correctly with maximum length | medium |
| TC-044 |  | Upload a profile picture with maximum file size | User logged in as Student, User is on the Profile page | 1. Click 'Edit profile'<br>2. Upload a profile picture that is at the maximum allowed file size<br>3. Click 'Update profile' | Profile picture is updated successfully; the new picture displays on the profile | medium |

---

## Logout

Total: **0** (positive: 0, negative: 0, edge: 0)

---
