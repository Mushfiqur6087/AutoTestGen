# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Assignment Submissions

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-001 | Submission table displayed | Assignment has enrolled students | 1. Open Submissions tab | Student identity, status, grading status, date, online text, files, comments, feedback, and final grade columns are visible | High |
| MT-ASUB-002 | Search and filter submissions | Submissions tab includes `student1` | 1. Search for `student1`<br>2. Filter by submission status Submitted for grading | Table shows `student1` submitted row and hides rows that do not match the selected status | High |
| MT-ASUB-003 | Open row grading workflow | Submission row exists | 1. Open row action menu<br>2. Select grade action | Grading workflow opens for selected student | High |
| MT-ASUB-004 | Enable quick grading | Quick grading is available and `student1` has a submission | 1. Enable quick grading<br>2. Enter grade `85` and feedback `Meets rubric` for `student1`<br>3. Save changes<br>4. Refresh Submissions tab | Grade `85` and feedback `Meets rubric` persist for `student1` | High |
| MT-ASUB-005 | Download submitted file | `student1` submitted `essay-draft.pdf` | 1. Click `essay-draft.pdf` in the File submission column | Browser receives the `essay-draft.pdf` file response and no access-denied page is shown | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-006 | Submissions blocked while unauthenticated | User is logged out | 1. Navigate directly to submissions URL | User is redirected to the login page before the submissions table renders | High |
| MT-ASUB-007 | Invalid quick grade | Quick grading is enabled | 1. Enter grade `101` for `student1`<br>2. Save | Save is blocked, `101` is marked invalid, and the previous grade value for `student1` remains unchanged after refresh | High |
| MT-ASUB-008 | Search no matching student | Submissions tab is open | 1. Search for non-existent student | Empty/no-results state is displayed | Medium |
| MT-ASUB-011 | Attempt inline Final Grade edit when Quick Grading disabled | Assignment Submissions table is visible and Quick grading is off | 1. Click a student's Final Grade cell | Cell remains read-only; no inline input field appears | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-009 | Maximum valid grade | Quick grading is enabled | 1. Enter grade `100` for `student1`<br>2. Save and refresh Submissions tab | Grade `100` remains visible for `student1` after refresh | Medium |
| MT-ASUB-010 | Late submission row | Assignment has late submission | 1. Open Submissions tab | Late timing/status is shown accurately | Medium |
| MT-ASUB-012 | Rapidly toggle Quick Grading on and off | Assignment Submissions table is visible | 1. Rapidly toggle Quick grading multiple times | Table stabilizes in the state matching the final toggle action; no duplicate inline inputs appear | Medium |
| MT-ASUB-013 | Rapid double-click "Grade" in action menu | Assignment Submissions table is visible | 1. Open action menu for a student<br>2. Rapidly double-click "Grade" | Grading interface opens exactly once without triggering multiple browser navigation requests | Medium |
| MT-ASUB-014 | Student Name search with leading and trailing whitespace is trimmed | Assignment Submissions table is visible | 1. Search for `   student1   ` | Table filters to show `student1`; surrounding whitespace is safely ignored | Low |
| MT-ASUB-015 | Student profile link is navigable from submissions | Assignment Submissions table is visible | 1. Click the student's name in a submission row | Browser navigates directly to the student's Moodle profile | Medium |
