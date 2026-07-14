# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Assignment Teacher View

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-001 | Assignment metadata visible | Teacher opens assignment | 1. Open an assignment page | Opened date, due date, description, and attached files are visible | High |
| MT-ATVIEW-002 | Grading summary visible | Assignment has enrolled participants | 1. Open assignment page | Number of participants, submissions, needs grading, visibility, and time remaining are displayed | High |
| MT-ATVIEW-003 | Grade button opens grading interface | Assignment has submissions or enrolled students | 1. Click "Grade" | Individual grading interface opens | High |
| MT-ATVIEW-004 | Assignment tabs navigate | Assignment page is open | 1. Click Assignment, Settings, Submissions, Advanced grading, and More tabs | Each selected tab becomes active and displays its matching heading or form before the next tab is clicked | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-005 | Assignment blocked while unauthenticated | User is logged out | 1. Navigate directly to assignment URL | User is redirected to the login page before assignment metadata or grading controls render | High |
| MT-ATVIEW-006 | Grade unavailable without permission | User lacks grading permission | 1. Open assignment page<br>2. Navigate directly to the grading URL | Grade button is not rendered and the direct grading URL displays access denied before the grading form renders | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-007 | Assignment with zero submissions | Assignment exists with no submissions | 1. Open assignment page | Grading summary shows Number of submissions `0` and Needs grading `0`; Grade button and assignment tab bar remain visible | Medium |
| MT-ATVIEW-008 | Expired due date | Assignment due date has passed | 1. Open assignment page | Time remaining clearly indicates overdue/closed state | Low |
| MT-ATVIEW-009 | Rapid multiple clicks on Grade button | Assignment view is visible | 1. Rapidly double-click "Grade" | Grading interface modal opens exactly once; no duplicate modal or background load issues occur | Medium |
| MT-ATVIEW-010 | Very long assignment description does not break layout | Assignment view is visible | 1. View an assignment with a 10,000+ character description | Description renders fully and the grading summary table below it remains accessible and correctly aligned | Low |
