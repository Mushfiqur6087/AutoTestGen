# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Assignment Creation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-001 | Create assignment and return to course | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft - Ground Truth`<br>2. Enter a short description<br>3. Enable online text and file submissions<br>4. Click "Save and return to course" | Assignment is created, course page opens, and `Essay Draft - Ground Truth` appears in the selected section after refresh | High |
| MT-ACREATE-002 | Create assignment and display it | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft Display Check`<br>2. Configure required fields<br>3. Click "Save and display" | Assignment page opens with the new assignment name, description, due date/status panel, and teacher tabs | High |
| MT-ACREATE-003 | Configure group submissions | Assignment form is open | 1. Check the Group submissions checkbox<br>2. Configure Require all group members to submit and select a Grouping<br>3. Click "Save and return to course" | Assignment is created with Group submissions configured as set in the creation form; course page opens | Medium |
| MT-ACREATE-004 | Configure File submissions and limits | Assignment form is open | 1. Check the File submissions checkbox<br>2. Set maximum number of files, maximum submission size, and accepted file types<br>3. Click "Save and return to course" | Assignment is created with File submissions enabled and the configured limits as set in the creation form | High |
| MT-ACREATE-005 | Save and display shows configured submission settings | Assignment form is open | 1. Enable File submissions and Group submissions with configured limits and grouping<br>2. Click "Save and display" | The new assignment page opens showing File submissions enabled with the configured maximum files/size, and the Group submissions configuration showing the selected grouping and requirement | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-006 | Assignment name empty | Assignment form is open | 1. Leave Assignment name empty<br>2. Click save | Inline required-field validation is shown and assignment is not created | High |
| MT-ACREATE-007 | Oversized additional file | Assignment form is open | 1. Upload `oversize-11mb.pdf` to Additional files | Upload is blocked, file-size validation is displayed, and `oversize-11mb.pdf` is not listed in Additional files | Medium |
| MT-ACREATE-008 | Non-numeric value in maximum file count blocked | File submissions are enabled | 1. Enter a non-numeric value in "Maximum number of uploaded files"<br>2. Save | Save is blocked, inline validation indicates a numeric value is required, and no assignment is created from the invalid configuration | Medium |
| MT-ACREATE-009 | Cancel discards assignment creation | Assignment form has unsaved changes | 1. Click "Cancel" | No assignment is created and teacher returns to previous page | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-010 | Enable File and Group submissions together | Assignment form is open | 1. Enable File submissions with configured limits and accepted file types<br>2. Enable Group submissions with a selected grouping and requirement<br>3. Click "Save and return to course" | Assignment is created with both File and Group submissions configured as set in the creation form | Low |
| MT-ACREATE-011 | Assignment Creation blocked without edit permission | User is logged in without course-edit permission (e.g., Student role) | 1. Open the Activity Chooser while logged in without edit permissions<br>2. Attempt to select Assignment | The Activity Chooser does not open the Assignment Creation form for this user; the Assignment option is unavailable or selecting it has no effect; the user remains on the Course page | Low |
| MT-ACREATE-012 | Invalid due date format rejected | Assignment form is open | 1. Enable Due date<br>2. Enter an invalid date format into Due date<br>3. Save | Save is blocked with an inline validation error indicating the date/time is invalid; no assignment is created | High |
| MT-ACREATE-013 | Cut-off date earlier than Due date | Assignment form is open | 1. Set Cut-off date to a time earlier than Due date<br>2. Save | Save is blocked with an inline date-validation error | High |
| MT-ACREATE-014 | Repeating completion conditions can be added and removed before save | Assignment form is open | 1. Add multiple Activity completion required conditions<br>2. Remove all of them so none remain<br>3. Click "Save and display" | The new assignment page opens and the Activity completion section shows zero required conditions; save succeeds even after all repeating entries were removed | Low |
| MT-ACREATE-015 | File submissions save with optional limits left blank | Assignment form is open | 1. Enable File submissions<br>2. Leave the maximum-files and maximum-size fields blank<br>3. Click "Save and return to course" | Save succeeds; the course page is shown and the new assignment appears in the Course Index; no inline error about the missing optional limits is shown | Low |
| MT-ACREATE-016 | Extremely long assignment name blocked | Assignment form is open | 1. Enter a 200+ character string in Assignment name<br>2. Attempt to save | Inline validation indicates the value exceeds the maximum allowed length; Save is blocked until the value is shortened | Medium |
| MT-ACREATE-017 | Assignment Creation blocked while unauthenticated | User is not authenticated; course page is reachable | 1. Navigate to the Course page while not logged in<br>2. Open the Activity Chooser<br>3. Select Assignment | Access to the Assignment Creation form is blocked: the user is redirected to the login page and the form is not displayed | High |
| MT-ACREATE-018 | Additional file with emoji filename | Assignment form is open | 1. Upload a file named `assignment_🎓_reqs.pdf`<br>2. Save and display | File uploads successfully and the emoji filename is preserved on the assignment page | Low |
| MT-ACREATE-019 | Maximum points boundary value | Assignment form is open with Point grading | 1. Set Maximum points to the highest allowed system value (e.g., 1000000)<br>2. Save and reopen settings | High point value is saved and displayed without causing a system overflow error | Low |
