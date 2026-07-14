# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Assignment Creation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-001 | Create assignment and return to course | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft - Ground Truth`<br>2. Enter a short description<br>3. Enable online text and file submissions<br>4. Click "Save and return to course" | Assignment is created, course page opens, and `Essay Draft - Ground Truth` appears in the selected section after refresh | High |
| MT-ACREATE-002 | Create assignment and display it | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft Display Check`<br>2. Configure required fields<br>3. Click "Save and display" | Assignment page opens with the new assignment name, description, due date/status panel, and teacher tabs | High |
| MT-ACREATE-003 | Configure availability dates | Assignment form is open | 1. Enable submission/due/cut-off date controls<br>2. Set dates and times | Date settings are saved and visible after save | Medium |
| MT-ACREATE-004 | Configure submission and feedback types | Assignment form is open | 1. Enable online text and file submissions<br>2. Configure feedback comments/files/offline worksheet | Selected submission and feedback settings are saved | High |
| MT-ACREATE-005 | Configure grade and completion settings | Assignment form is open | 1. Set grade type to Point<br>2. Set maximum points to `100`<br>3. Enable activity completion tracking<br>4. Add tag `ground-truth`<br>5. Save and reopen settings | Grade type, maximum points, completion tracking, and `ground-truth` tag are persisted in the assignment settings | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-006 | Assignment name empty | Assignment form is open | 1. Leave Assignment name empty<br>2. Click save | Inline required-field validation is shown and assignment is not created | High |
| MT-ACREATE-007 | Oversized additional file | Assignment form is open | 1. Upload `oversize-11mb.pdf` to Additional files | Upload is blocked, file-size validation is displayed, and `oversize-11mb.pdf` is not listed in Additional files | Medium |
| MT-ACREATE-008 | Invalid accepted file type | File submissions are enabled | 1. Enter `not-an-extension` in accepted file types<br>2. Save | Save is blocked, the accepted file types field is marked invalid, and no assignment is created from the invalid configuration | Medium |
| MT-ACREATE-009 | Cancel discards assignment creation | Assignment form has unsaved changes | 1. Click "Cancel" | No assignment is created and teacher returns to previous page | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-010 | Disabled availability dates are not enforced | Assignment form is open | 1. Disable Allow submissions from, Due date, and Cut-off date toggles<br>2. Save and display assignment | Assignment page shows no enforced open, due, or cut-off date for the new assignment | Low |
| MT-ACREATE-011 | Maximum number of uploaded files | File submissions are enabled | 1. Select the highest value displayed in "Maximum number of uploaded files"<br>2. Save and reopen assignment settings | The same maximum-file count label remains selected after reopening settings | Low |
| MT-ACREATE-012 | Due date earlier than Allow submissions from date | Assignment form is open | 1. Set Due date to a time earlier than Allow submissions from date<br>2. Save | Save is blocked with an inline date-validation error | High |
| MT-ACREATE-013 | Cut-off date earlier than Due date | Assignment form is open | 1. Set Cut-off date to a time earlier than Due date<br>2. Save | Save is blocked with an inline date-validation error | High |
| MT-ACREATE-014 | Negative maximum points blocked | Assignment form is open with Point grading | 1. Set Maximum points to `-10`<br>2. Save | Save is blocked and a validation error requires points to be greater than 0 | High |
| MT-ACREATE-015 | Very long assignment description | Assignment form is open | 1. Enter a 10,000+ character description<br>2. Save and display | Assignment saves successfully and the full description is displayed on the assignment page | Low |
| MT-ACREATE-016 | Rapid double-click on Save and return to course | Assignment form is open and filled | 1. Rapidly double-click "Save and return to course" | Assignment is created exactly once and no duplicate entries appear on the course page | Medium |
| MT-ACREATE-017 | Disable all submission types | Assignment form is open | 1. Uncheck both Online text and File submissions<br>2. Save | Save is blocked with validation indicating at least one submission type must be enabled | High |
| MT-ACREATE-018 | Additional file with emoji filename | Assignment form is open | 1. Upload a file named `assignment_🎓_reqs.pdf`<br>2. Save and display | File uploads successfully and the emoji filename is preserved on the assignment page | Low |
| MT-ACREATE-019 | Maximum points boundary value | Assignment form is open with Point grading | 1. Set Maximum points to the highest allowed system value (e.g., 1000000)<br>2. Save and reopen settings | High point value is saved and displayed without causing a system overflow error | Low |
