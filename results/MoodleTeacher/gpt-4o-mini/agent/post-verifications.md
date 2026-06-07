# Post-Verification Specifications

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Calendar`
- **Observe**:
  - calendar does not contain the new event

**Post-Check**
- **Navigate To**: `Calendar`
- **Observe**:
  - calendar contains the new event
  - event details are correct

**Expected Change**: A new calendar entry is created with the correct details visible in the calendar.

---

### [TC-005] Leave the Email Address field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Email Address field blank
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - block is in its original position

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - block is in the new position

**Expected Change**: The block has been successfully moved to a new position on the Dashboard.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - existing block is visible

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - existing block is not visible

**Expected Change**: The block is successfully deleted from the Dashboard and no longer appears.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - Course list does not show the starred course at the top

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - Starred course is pinned to the top of the course list

**Expected Change**: The starred course appears at the top of the My Courses page.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - Course card for the selected course is visible

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - Course card for the selected course is not visible

**Expected Change**: The course is removed from view and does not appear in the My Courses list.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - subsection list does not contain the new subsection

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - subsection list contains the new subsection

**Expected Change**: A new subsection is added to the course and is visible in the subsection list.

---

### [TC-003] User attempts to log out after being authenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page; session is terminated successfully.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - Activity chooser modal is open

**Post-Check**
- **Navigate To**: `Activity Creation Form`
- **Observe**:
  - Activity creation form is displayed
  - Assignment title field is present
  - Submission settings are visible

**Expected Change**: The activity creation form opens, allowing the teacher to configure the new assignment.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity settings are displayed with previous configurations

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity settings reflect the updated configurations

**Expected Change**: The activity settings are updated to reflect the changes made in the edit settings action.

---

### [TC-005] Leave the Email Address field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Email Address field blank
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity is in its original position

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity is in the new position

**Expected Change**: The activity has been successfully moved to the new position in the course layout.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity list does not contain the duplicated activity

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity list contains the duplicated activity
  - activity name includes 'copy' or similar identifier

**Expected Change**: A new activity entry is created that is a duplicate of the original activity, identifiable by its name.

---

### [TC-007] Submit with all required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave all required fields blank
2. 2. Click Update Profile

**Original Expected Result:** Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - Activity is visible in the activity list

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - Activity is not visible in the activity list
  - Activity status is marked as hidden

**Expected Change**: The selected activity is no longer displayed in the activity list, confirming it has been successfully hidden.

---

### [TC-008] Upload a file exactly at the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is exactly at the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Profile is updated successfully; the profile page refreshes.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page -> Activity List`
- **Observe**:
  - activity access restrictions are not set

**Post-Check**
- **Navigate To**: `Course Page -> Activity List`
- **Observe**:
  - activity access restrictions are set
  - access restriction indicator is visible

**Expected Change**: The activity now displays an access restriction indicator, confirming that access restrictions have been successfully applied.

---

### [TC-009] Upload a file one byte over the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is one byte over the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Upload is blocked; an error message is displayed indicating the file exceeds the size limit.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity list contains the deleted activity

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity list does not contain the deleted activity

**Expected Change**: The activity is no longer present in the activity list on the course page.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `QA Automation 101 course page`
- **Observe**:
  - Assignment list does not contain the new assignment

**Post-Check**
- **Navigate To**: `QA Automation 101 course page`
- **Observe**:
  - Assignment list contains the new assignment
  - Assignment name is '<valid assignment name>'

**Expected Change**: A new assignment entry is created with the specified name and is visible on the course page.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `QA Automation 101 course page`
- **Observe**:
  - Assignment list does not contain the new assignment

**Post-Check**
- **Navigate To**: `QA Automation 101 course page`
- **Observe**:
  - Assignment list contains the new assignment
  - assignment name is '<valid assignment name>'

**Expected Change**: A new assignment entry is created with the name '<valid assignment name>' and is visible on the course page.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page`
- **Observe**:
  - Course Full Name field is empty
  - Course Short Name field is empty
  - Course Category dropdown is unselected
  - Course Visibility dropdown is unselected
  - Course Start Date field is empty

**Post-Check**
- **Navigate To**: `Course page`
- **Observe**:
  - Course Full Name displays the entered value
  - Course Short Name displays the entered value
  - Course Category shows the selected category
  - Course Visibility reflects the selected option
  - Course Start Date shows the entered date

**Expected Change**: The course settings are saved and displayed correctly on the course page.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Confirm enrollment of a user by entering a valid user and selecting 'Student' role.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Participants Management`
- **Action**: 
- **Observe**:
  - participants table
  - student name
  - student role

**Expected Change**: The participants table shows the newly enrolled user with the role 'Student' under the course managed by the teacher.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Participants Management`
- **Observe**:
  - user role is 'Student' for the selected user

**Post-Check**
- **Navigate To**: `Participants Management`
- **Observe**:
  - user role is updated to 'Teacher' for the selected user

**Expected Change**: The user role for the selected participant is changed from 'Student' to 'Teacher'.

---

### [TC-007] Submit with all required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave all required fields blank
2. 2. Click Update Profile

**Original Expected Result:** Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Participants page`
- **Observe**:
  - message history does not contain the new message

**Post-Check**
- **Navigate To**: `Messages page`
- **Observe**:
  - new message appears in the conversation with the recipient
  - message content matches <message>

**Expected Change**: The message sent to the user is visible in the conversation history.

---

### [TC-008] Upload a file exactly at the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is exactly at the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Profile is updated successfully; the profile page refreshes.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Bulk enroll selected users from the Participants table.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Participants page`
- **Action**: 
- **Observe**:
  - student enrollment status
  - teacher name in participant list

**Expected Change**: The selected students are now enrolled in the course and their enrollment status reflects the change.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment Submissions tab`
- **Observe**:
  - Final grade column shows previous grade for the submission

**Post-Check**
- **Navigate To**: `Assignment Submissions tab`
- **Observe**:
  - Final grade column updates to reflect the entered grade

**Expected Change**: The Final grade column now displays the new grade entered for the submission.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grader Report`
- **Observe**:
  - grade cell for <valid student name> shows previous grade value

**Post-Check**
- **Navigate To**: `Grader Report`
- **Observe**:
  - grade cell for <valid student name> shows updated grade value

**Expected Change**: The grade cell for <valid student name> reflects the new valid grade value after saving changes.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grader report`
- **Observe**:
  - grade cell shows previous grade value

**Post-Check**
- **Navigate To**: `Grader report`
- **Observe**:
  - grade cell shows updated grade value

**Expected Change**: The grade cell reflects the new valid grade value entered by the teacher.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - initials icon
  - full name
  - message button
  - profile description area is visible

**Post-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - initials icon
  - full name
  - message button
  - profile description area is visible
  - updated profile details

**Expected Change**: The profile details reflect the recent updates made during the edit process.

---

### [TC-013] Send a message
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Message' button

**Original Expected Result:** Message sent successfully

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> Messages`
- **Observe**:
  - no recent messages or notifications indicating a sent message

**Post-Check**
- **Navigate To**: `Dashboard -> Messages`
- **Observe**:
  - recent messages list contains the new message
  - message status is 'Sent'

**Expected Change**: A new message entry appears in the messages list indicating that the message was sent successfully.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile page`
- **Observe**:
  - initial first name
  - initial last name
  - initial email
  - initial profile picture

**Post-Check**
- **Navigate To**: `Profile page`
- **Observe**:
  - <valid first name>
  - <valid last name>
  - <valid email>
  - updated profile picture

**Expected Change**: The profile page displays the updated first name, last name, email address, and the new profile picture.

---
