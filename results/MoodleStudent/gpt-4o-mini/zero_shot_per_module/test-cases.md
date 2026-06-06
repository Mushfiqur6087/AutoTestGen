# Test Cases — MoodleStudent

Generated: 2026-06-04T15:12:00.170898Z  
Model: gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 67 | 21 | 21 | 25 | 28 | 28 | 11 |

## Login

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Successful login with valid credentials | User has a valid username and password. | 1. Navigate to the login page.<br>2. Enter valid username.<br>3. Enter valid password.<br>4. Click on the 'Log in' button. | User is redirected to the Dashboard. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Login attempt with invalid username | User is on the login page. | 1. Enter an invalid username.<br>2. Enter a valid password.<br>3. Click on the 'Log in' button. | An inline error message is displayed, password field is cleared, and username is retained. | high |
| TC-003 |  | Login attempt with invalid password | User is on the login page. | 1. Enter a valid username.<br>2. Enter an invalid password.<br>3. Click on the 'Log in' button. | An inline error message is displayed, password field is cleared, and username is retained. | high |
| TC-004 |  | Login attempt with empty fields | User is on the login page. | 1. Leave the username field empty.<br>2. Leave the password field empty.<br>3. Click on the 'Log in' button. | An inline error message is displayed for both fields. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Login attempt with maximum length username and password | User is on the login page. | 1. Enter a username with maximum allowed length.<br>2. Enter a password with maximum allowed length.<br>3. Click on the 'Log in' button. | User is redirected to the Dashboard if credentials are valid. | medium |
| TC-006 |  | Login attempt with special characters in username and password | User is on the login page. | 1. Enter a username with special characters.<br>2. Enter a password with special characters.<br>3. Click on the 'Log in' button. | An inline error message is displayed if credentials are invalid. | medium |
| TC-007 |  | Login attempt with whitespace in username and password | User is on the login page. | 1. Enter a username with leading and trailing whitespace.<br>2. Enter a password with leading and trailing whitespace.<br>3. Click on the 'Log in' button. | An inline error message is displayed if credentials are invalid. | medium |

---

## Dashboard

Total: **10** (positive: 4, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 |  | Display personalized greeting | User is logged in | 1. Navigate to the Dashboard. | The personalized greeting is displayed at the top of the Dashboard. | high |
| TC-009 |  | View upcoming activities in Timeline block | User is logged in, User has upcoming activities | 1. Navigate to the Dashboard.<br>2. Check the Timeline block. | Upcoming activities are listed in the Timeline block. | high |
| TC-014 |  | Create a new calendar event | User is logged in, User is in Calendar block | 1. Click on the 'New event' button.<br>2. Fill in the event details.<br>3. Save the event. | The new event is displayed in the Calendar block. | high |
| TC-017 |  | Access full calendar and import/export options | User is logged in | 1. Navigate to the Dashboard.<br>2. Click on 'Full calendar' link.<br>3. Click on 'Import or export calendars' link. | The respective pages for full calendar view and calendar data management are opened. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | No activities in selected time range | User is logged in, User has no activities in the selected range | 1. Navigate to the Dashboard.<br>2. Set the time range to 'Next 7 days'. | An empty state message is displayed in the Timeline block. | medium |
| TC-011 |  | Search for non-existent activity | User is logged in, User has activities | 1. Navigate to the Dashboard.<br>2. Enter a non-existent activity name in the search field.<br>3. Click on the search button. | No results found message is displayed. | medium |
| TC-015 |  | Attempt to create a calendar event with missing details | User is logged in, User is in Calendar block | 1. Click on the 'New event' button.<br>2. Leave required fields empty.<br>3. Attempt to save the event. | An error message is displayed indicating required fields are missing. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Select maximum time range | User is logged in | 1. Navigate to the Dashboard.<br>2. Select the maximum time range available from the dropdown. | The Timeline block updates to show activities for the selected maximum time range. | low |
| TC-013 |  | Navigate to previous month in Calendar block | User is logged in | 1. Navigate to the Dashboard.<br>2. Click the left arrow to navigate to the previous month. | The Calendar block updates to display the previous month. | low |
| TC-016 |  | Toggle Edit mode and check for additional buttons | User is logged in | 1. Navigate to the Dashboard.<br>2. Toggle Edit mode on. | The 'Reset page to default' and '+ Add a block' buttons are displayed. | low |

---

## My Courses

Total: **8** (positive: 4, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 |  | View all enrolled courses | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Observe the displayed course cards. | All enrolled courses are displayed as visual cards with course banner images, names, and categories. | high |
| TC-019 |  | Click on course name to navigate | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Click on a course name. | User is navigated to the main page of the selected course. | high |
| TC-024 |  | Star a course | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Click on the three-dot menu of a course card.<br>3. Select 'Star this course'. | The course is pinned to the top of the list of courses. | medium |
| TC-025 |  | Remove a course from view | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Click on the three-dot menu of a course card.<br>3. Select 'Remove from view'. | The course is hidden from the list without unenrolling the user. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 |  | No courses displayed when not enrolled | User is logged in, User has no enrolled courses | 1. Navigate to the My Courses page. | A message indicating that the user is not enrolled in any courses is displayed. | medium |
| TC-021 |  | Search with empty input | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Leave the search field empty and click search. | All courses are displayed as no specific search term was provided. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 |  | Status dropdown with all options | User is logged in, User has enrolled courses | 1. Navigate to the My Courses page.<br>2. Select each status option from the dropdown (All, In progress, Future, Past, Starred, Hidden). | The course cards displayed correspond to the selected status option. | low |
| TC-023 |  | Sort dropdown with maximum length course names | User is logged in, User has courses with maximum length names | 1. Navigate to the My Courses page.<br>2. Select a sort option from the dropdown. | Courses are sorted correctly regardless of the length of their names. | low |

---

## Course Page

Total: **6** (positive: 3, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-026 |  | View course content | User is logged in, User has access to the course | 1. Navigate to the Course page.<br>2. Observe the course name and sections. | The course name is displayed as the page heading, and all sections are visible. | high |
| TC-027 |  | Collapse a section | User is on the Course page, At least one section is expanded | 1. Click on the chevron icon of a section.<br>2. Observe the section content. | The section collapses, hiding its content. | medium |
| TC-028 |  | Collapse all sections | User is on the Course page, At least one section is expanded | 1. Click on the 'Collapse all' link.<br>2. Observe the sections. | All sections collapse, hiding their content. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-029 |  | Attempt to enable Edit mode | User is on the Course page | 1. Look for an option to enable Edit mode.<br>2. Attempt to click on it. | The option to enable Edit mode is not available or clickable. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-030 |  | View course with maximum sections | User is logged in, Course has the maximum allowed sections | 1. Navigate to the Course page.<br>2. Observe the sections listed. | All sections are displayed correctly without layout issues. | low |
| TC-031 |  | View course with empty sections | User is logged in, Course has sections with no activities or resources | 1. Navigate to the Course page.<br>2. Observe the sections with no content. | Sections are displayed with appropriate messages indicating no content available. | low |

---

## Participants

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-032 |  | Filter participants by First name using 'A–Z' button | User is logged in and on the Participants page. | 1. Click on the 'A–Z' button for First name.<br>2. Observe the filtered list of participants. | The participants list displays only those whose first names start with the selected letter. | high |
| TC-033 |  | Apply multiple filters successfully | User is logged in and on the Participants page. | 1. Select an attribute from the Select attribute dropdown.<br>2. Toggle 'Any' to true.<br>3. Click on '+ Add condition' and select another attribute.<br>4. Click on 'Apply filters'. | The participants list updates to show only those matching the applied filters. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-034 |  | Attempt to apply filters without selecting any attributes | User is logged in and on the Participants page. | 1. Click on 'Apply filters' without selecting any attributes. | An error message is displayed indicating that at least one filter must be selected. | high |
| TC-035 |  | Click on a participant's name without permission to edit roles | User is logged in and on the Participants page. | 1. Click on a participant's name. | The participant's profile is displayed, but no options to edit roles or manage enrollment are available. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-036 |  | Apply filters with maximum length of input | User is logged in and on the Participants page. | 1. Enter a string of maximum allowed length in the filter input.<br>2. Click on 'Apply filters'. | The participants list updates correctly without any errors, showing participants matching the maximum length input. | medium |
| TC-037 |  | Clear filters after applying them | User is logged in and has applied filters. | 1. Click on 'Clear filters'. | The participants list resets to show all participants without any filters applied. | low |
| TC-038 |  | Check participants list with no participants enrolled | User is logged in and there are no participants in the course. | 1. Navigate to the Participants page. | A message indicating that there are no participants enrolled is displayed. | low |

---

## Grades

Total: **6** (positive: 1, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-039 |  | View own grades successfully | User is logged in, User has grades recorded | 1. Navigate to the Grades page.<br>2. Observe the grades displayed. | The user sees their own grades with all columns populated correctly. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-040 |  | Access another student's grades | User is logged in, User has no grades for the course | 1. Attempt to access the grades of another student. | The system displays an error message indicating access is denied. | high |
| TC-043 |  | Access Grades page without being logged in | User is not logged in | 1. Attempt to navigate to the Grades page. | The system redirects the user to the login page. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-041 |  | View grades with no recorded grades | User is logged in, User has no grades recorded | 1. Navigate to the Grades page. | The user sees a message indicating there are no grades available. | medium |
| TC-042 |  | View grades with maximum length feedback | User is logged in, User has grades with maximum length feedback | 1. Navigate to the Grades page.<br>2. Observe the feedback column. | The feedback is displayed correctly without truncation or errors. | medium |
| TC-044 |  | View grades with empty fields | User is logged in, User has grades with some empty fields | 1. Navigate to the Grades page. | The user sees the grades with empty fields represented as '–'. | medium |

---

## Assignment

Total: **7** (positive: 2, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-045 |  | Successful submission with text editor | User is logged in, Assignment is open for submission | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Enter text in the online text editor<br>4. Click on 'Submit' | Submission is successful, and a confirmation message is displayed. | high |
| TC-046 |  | Successful submission with file upload | User is logged in, Assignment is open for submission | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Upload a valid file<br>4. Click on 'Submit' | Submission is successful, and a confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-047 |  | Submission after due date | User is logged in, Assignment is past due date | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Enter text in the online text editor<br>4. Click on 'Submit' | Error message is displayed indicating that submission is not allowed after the due date. | high |
| TC-048 |  | Submission without any input | User is logged in, Assignment is open for submission | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Click on 'Submit' without entering any data | Error message is displayed indicating that submission cannot be empty. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-049 |  | Submission with maximum file size | User is logged in, Assignment is open for submission, File size limit is known | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Upload a file that is exactly at the maximum size limit<br>4. Click on 'Submit' | Submission is successful, and a confirmation message is displayed. | medium |
| TC-050 |  | Submission with maximum character limit in text editor | User is logged in, Assignment is open for submission | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Enter text that reaches the maximum character limit<br>4. Click on 'Submit' | Submission is successful, and a confirmation message is displayed. | medium |
| TC-051 |  | Submission with special characters | User is logged in, Assignment is open for submission | 1. Navigate to the Assignment page<br>2. Click on 'Add submission'<br>3. Enter text with special characters (e.g., @, #, $, %) in the text editor<br>4. Click on 'Submit' | Submission is successful, and a confirmation message is displayed. | medium |

---

## Activities

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-052 |  | View expanded Assignments section | User is logged in, User is on the Activities page | 1. Observe the Assignments section<br>2. Verify that it is expanded by default | The Assignments section is visible with a table showing Name, Due date, and Submission status. | high |
| TC-053 |  | Click on an activity name | User is logged in, User is on the Activities page, Assignments section is expanded | 1. Click on an activity name in the Assignments section | User is navigated to the corresponding activity's page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-054 |  | Attempt to access Activities page without logging in | User is not logged in | 1. Navigate to the Activities page | User is redirected to the login page with an error message. | high |
| TC-055 |  | Click on a non-existent activity name | User is logged in, User is on the Activities page, Assignments section is expanded | 1. Click on a non-existent activity name | An error message is displayed indicating the activity does not exist. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-056 |  | Check behavior with maximum length activity name | User is logged in, User is on the Activities page | 1. Add an activity with the maximum allowed length for the name<br>2. Verify the display in the Assignments section | The activity name is displayed correctly without truncation. | medium |
| TC-057 |  | Check behavior with empty sections | User is logged in, User is on the Activities page | 1. Verify the Forums and Resources sections are collapsed by default | The Forums and Resources sections are collapsed and not visible until expanded. | low |

---

## Profile

Total: **7** (positive: 1, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-058 |  | Update profile with valid data | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Fill in all required fields with valid data<br>3. Click on 'Update profile' | Profile is updated successfully and a confirmation message is displayed. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-059 |  | Attempt to update profile with missing required fields | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Leave required fields empty<br>3. Click on 'Update profile' | Error messages are displayed for the missing required fields. | high |
| TC-060 |  | Attempt to update profile with invalid email format | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Enter an invalid email format in the email field<br>3. Click on 'Update profile' | An error message is displayed indicating the email format is invalid. | high |
| TC-063 |  | Cancel profile update | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Make changes to the profile<br>3. Click on 'Cancel' | User is returned to the Profile page without any changes being saved. | low |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-061 |  | Update profile with maximum length fields | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Fill in all fields with maximum allowed characters<br>3. Click on 'Update profile' | Profile is updated successfully without any errors. | medium |
| TC-062 |  | Update profile with special characters in name fields | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Enter special characters in the First name and Last name fields<br>3. Click on 'Update profile' | Profile is updated successfully without any errors. | medium |
| TC-064 |  | Update profile with empty description | User is logged in, User is on the Profile page | 1. Click on 'Edit profile'<br>2. Leave the Description field empty<br>3. Click on 'Update profile' | Profile is updated successfully, as the description is optional. | medium |

---

## Logout

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-065 |  | Successful logout | User is logged into the application. | 1. Click on the 'Log out' button.<br>2. Wait for the redirection. | User is redirected to the login page. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-066 |  | Logout without being logged in | User is not logged into the application. | 1. Attempt to click on the 'Log out' button. | No action is taken, and the user remains on the current page. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-067 |  | Logout after session timeout | User is logged in and session has timed out. | 1. Click on the 'Log out' button after session timeout. | User is redirected to the login page with a session timeout message. | medium |

---
