# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Grades

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-001 | Student User report displayed | Student opens Grades | 1. Open Grades page | Grade item, calculated weight, grade, range, percentage, feedback, and contribution columns are visible | High |
| MS-GRADE-002 | Expand course group | Grades contain `QA Automation 101` course group with activities | 1. Collapse `QA Automation 101` group<br>2. Expand it again | Child grade items are hidden after collapse and visible again after expand | Medium |
| MS-GRADE-003 | Course total row displayed | Student has grade items | 1. Scroll to total row | AGGREGATION Course total displays cumulative grade | High |
| MS-GRADE-004 | Ungraded item displays placeholder | An activity is not graded | 1. Inspect ungraded row | Grade column shows `-` and no numeric grade is displayed for that item | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-005 | Student cannot access full gradebook | Student is logged in | 1. Navigate directly to Grader report/full gradebook URL | Access denied page is shown before grader report rows render; other students' names and grades are not visible | High |
| MS-GRADE-006 | Grades blocked while unauthenticated | User is logged out | 1. Navigate directly to Grades URL | User is redirected to login | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-007 | No graded activities yet | Student has no graded activities | 1. Open Grades | User report opens with empty grade placeholders for activity rows and no other students' grades | Low |
| MS-GRADE-008 | Decimal percentage display | Grade item has decimal percentage | 1. Inspect percentage column | Decimal precision is displayed consistently | Low |
| MS-GRADE-009 | Rapid consecutive course-group toggle ends in stable expanded/collapsed state | `student1` is on the Grades page; `QA Automation 101` course group is visible | 1. Click the course-group collapse control three times in rapid succession | Course group ends in the state corresponding to the final click; no intermediate state is locked and no JavaScript error appears | Medium |
| MS-GRADE-010 | Keyboard Space/Enter activates course-group collapse control | `student1` is on the Grades page; `QA Automation 101` course-group row is focused | 1. Tab to the course-group collapse control<br>2. Press Space or Enter | Course group expands or collapses in response to the keypress; the same toggle behavior as a mouse click is produced | Medium |
| MS-GRADE-011 | Long feedback text (200+ chars) truncated in cell; full text accessible on hover | Teacher has entered 200+ character feedback for `Essay Draft` | 1. Open Grades page<br>2. Locate the Feedback cell for `Essay Draft`<br>3. Hover over the cell | Feedback cell displays truncated text within the column width; full feedback text is accessible via tooltip or hover reveal | Low |
| MS-GRADE-012 | Unicode/emoji in Feedback column renders correctly without garbled display | Teacher has entered feedback containing Unicode and emoji for `Essay Draft` | 1. Open Grades page<br>2. Locate the Feedback cell for `Essay Draft` | Feedback cell renders Unicode characters and emoji as intended; no garbled or replacement characters are displayed | Low |
| MS-GRADE-013 | Whitespace-only feedback displays as empty placeholder not as visible whitespace | Teacher has entered whitespace-only feedback for a grade item | 1. Open Grades page<br>2. Inspect the Feedback cell for the whitespace-feedback item | Feedback cell shows the empty-placeholder indicator (dash or blank); no visible whitespace block occupies the cell | Low |
