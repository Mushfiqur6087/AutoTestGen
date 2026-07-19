# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Assignment

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-001 | Add submission form opens when no submissions exist | No submissions made yet | 1. Open assignment page<br>2. Click "Add submission" | Submission form displays online text editor and/or file upload area as configured | High |
| MS-ASGN-002 | Submit online text | `Essay Draft` accepts online text and is open for submissions | 1. Click "Add submission"<br>2. Enter `My essay draft text` in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission status shows Submitted for grading and `My essay draft text` is visible in the submission preview | High |
| MS-ASGN-003 | Submit file upload | `Essay Draft` accepts file submissions and is open for submissions | 1. Click "Add submission"<br>2. Upload `essay-draft.pdf` within the allowed size/type<br>3. Save/submit the submission<br>4. Reopen the assignment page | Submission status includes `essay-draft.pdf` as a downloadable file link | High |
| MS-ASGN-004 | Edit submission before deadline | Editable submission exists before due date | 1. Click "Edit submission"<br>2. Replace text with `Updated essay draft text`<br>3. Save changes<br>4. Reopen the assignment page | Updated text is shown and the previous text is no longer the active submission content | Medium |
| MS-ASGN-005 | Unauthenticated user cannot open Add submission | User not logged in | 1. Navigate to Assignment page URL<br>2. Attempt to open Add submission | Access is blocked; redirected to login page; submission form not opened | High |
| MS-ASGN-006 | View grade and feedback | Teacher has graded submission | 1. Open assignment page | Earned grade and teacher feedback are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-007 | Not-enrolled user cannot submit | Logged in but not enrolled in course | 1. Navigate to Assignment page<br>2. Look for Add submission button | Add submission button is not present; submission form cannot be opened | High |
| MS-ASGN-008 | View/Edit submission unavailable when no submissions made | Assignment status is "No submissions have been made yet" | 1. Open Assignment page<br>2. Inspect action bar | View submission and Edit submission buttons are not visible; status remains "No submissions have been made yet" | High |
| MS-ASGN-009 | Late submission blocked when closed | Due/cut-off date has passed and late submissions are disabled | 1. Open assignment<br>2. Inspect submission controls<br>3. Navigate directly to the submission edit URL | Add/Edit submission controls are not rendered and direct submission edit URL shows the assignment-closed message before an editor appears | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-010 | Submit online text with emoji and Unicode characters | Assignment allows online text | 1. Add submission<br>2. Enter text with emoji and Unicode characters<br>3. Submit | Submission created; emoji/Unicode rendered correctly in submission content | Low |
| MS-ASGN-011 | Long online text submission | Assignment accepts online text | 1. Enter boundary text starting `GT-LONG-TEXT-START` and ending `GT-LONG-TEXT-END`<br>2. Click "Save changes"<br>3. Reopen assignment page | Submission preview contains both `GT-LONG-TEXT-START` and `GT-LONG-TEXT-END`, proving the saved text kept its beginning and ending sentinels | Low |
| MS-ASGN-012 | Resubmit after grading not allowed | Assignment is graded and resubmission disabled | 1. Open assignment page | Edit/resubmit controls are absent or disabled | Medium |
| MS-ASGN-013 | View submission shows submitted content and status | Submission exists, status is Submitted for grading | 1. Open assignment page<br>2. Click "View submission" | Submission details panel shows submitted content, status "Submitted for grading", and last modified timestamp | Medium |
| MS-ASGN-014 | Edit submission allowed when due date is exactly today and teacher permits resubmission | `Essay Draft` due date is set to today; teacher has enabled resubmission | 1. Open assignment page<br>2. Click "Edit submission" | Edit submission form opens without a late-submission or access-denied message | Medium |
| MS-ASGN-015 | Edit submission blocked when due date passed by one day even if teacher permits resubmission | `Essay Draft` due date was yesterday; teacher has enabled resubmission but late submissions are disabled | 1. Open assignment page<br>2. Inspect submission controls | Edit/resubmit controls are absent or show an assignment-closed message; submission form does not render | High |
| MS-ASGN-016 | Online text with leading/trailing whitespace is trimmed on save | `Essay Draft` is open for online text submission | 1. Click "Add submission"<br>2. Enter `   Trimmed essay text   ` (with leading and trailing spaces) in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission preview shows `Trimmed essay text` without the surrounding whitespace | Low |
| MS-ASGN-017 | File with special-character/emoji filename uploads and filename is preserved | `Essay Draft` accepts file submissions | 1. Click "Add submission"<br>2. Upload a file whose name contains special characters and emoji (e.g., `essay_🎓_draft.pdf`)<br>3. Click "Save changes"<br>4. Reopen the assignment page | The file appears in the submission file list with its original filename preserved including the special characters and emoji | Low |
| MS-ASGN-018 | Rapid double-click Submit results in single submission | Add submission form open with required field filled | 1. Click "Submit"<br>2. Immediately click "Submit" again | Only one submission record created; duplicate submit prevented | Medium |
