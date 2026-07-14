# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Assignment

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-001 | Assignment details displayed | Assignment is available | 1. Open assignment page | Opened date, due date, description, and submission status are visible | High |
| MS-ASGN-002 | Submit online text | `Essay Draft` accepts online text and is open for submissions | 1. Click "Add submission"<br>2. Enter `My essay draft text` in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission status shows Submitted for grading and `My essay draft text` is visible in the submission preview | High |
| MS-ASGN-003 | Submit file upload | `Essay Draft` accepts file submissions and is open for submissions | 1. Click "Add submission"<br>2. Upload `essay-draft.pdf` within the allowed size/type<br>3. Save/submit the submission<br>4. Reopen the assignment page | Submission status includes `essay-draft.pdf` as a downloadable file link | High |
| MS-ASGN-004 | Edit submission before deadline | Editable submission exists before due date | 1. Click "Edit submission"<br>2. Replace text with `Updated essay draft text`<br>3. Save changes<br>4. Reopen the assignment page | Updated text is shown and the previous text is no longer the active submission content | Medium |
| MS-ASGN-005 | Remove submission when allowed | Removable submission exists before due date | 1. Click "Remove submission"<br>2. Confirm removal<br>3. Reopen the assignment page | Submission file/text is removed and submission status returns to not submitted or draft-empty state | Medium |
| MS-ASGN-006 | View grade and feedback | Teacher has graded submission | 1. Open assignment page | Earned grade and teacher feedback are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-007 | Required online text missing | Assignment requires online text | 1. Add submission<br>2. Leave online text empty<br>3. Submit | Submission is blocked with validation feedback | High |
| MS-ASGN-008 | Required file missing | Assignment requires file upload | 1. Add submission<br>2. Do not attach file<br>3. Submit | Submission is blocked with validation feedback | High |
| MS-ASGN-009 | Late submission blocked when closed | Due/cut-off date has passed and late submissions are disabled | 1. Open assignment<br>2. Inspect submission controls<br>3. Navigate directly to the submission edit URL | Add/Edit submission controls are not rendered and direct submission edit URL shows the assignment-closed message before an editor appears | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-010 | File at allowed upload limit | Assignment accepts files with 10 MB maximum upload size | 1. Upload `essay-limit-10mb.pdf`<br>2. Click "Save changes"<br>3. Reopen assignment page | `essay-limit-10mb.pdf` appears in the submission file list after reopening the assignment page | Low |
| MS-ASGN-011 | Long online text submission | Assignment accepts online text | 1. Enter boundary text starting `GT-LONG-TEXT-START` and ending `GT-LONG-TEXT-END`<br>2. Click "Save changes"<br>3. Reopen assignment page | Submission preview contains both `GT-LONG-TEXT-START` and `GT-LONG-TEXT-END`, proving the saved text kept its beginning and ending sentinels | Low |
| MS-ASGN-012 | Resubmit after grading not allowed | Assignment is graded and resubmission disabled | 1. Open assignment page | Edit/resubmit controls are absent or disabled | Medium |
| MS-ASGN-013 | Submit when no input areas are enabled still succeeds | `Essay Draft` is configured with no online text and no file submission enabled | 1. Open the assignment page<br>2. Click "Add submission"<br>3. Click "Save changes" without entering any content | Submission status changes to Submitted for grading; no validation error is raised for an empty submission when no input types are enabled | Medium |
| MS-ASGN-014 | Edit submission allowed when due date is exactly today and teacher permits resubmission | `Essay Draft` due date is set to today; teacher has enabled resubmission | 1. Open assignment page<br>2. Click "Edit submission" | Edit submission form opens without a late-submission or access-denied message | Medium |
| MS-ASGN-015 | Edit submission blocked when due date passed by one day even if teacher permits resubmission | `Essay Draft` due date was yesterday; teacher has enabled resubmission but late submissions are disabled | 1. Open assignment page<br>2. Inspect submission controls | Edit/resubmit controls are absent or show an assignment-closed message; submission form does not render | High |
| MS-ASGN-016 | Online text with leading/trailing whitespace is trimmed on save | `Essay Draft` is open for online text submission | 1. Click "Add submission"<br>2. Enter `   Trimmed essay text   ` (with leading and trailing spaces) in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission preview shows `Trimmed essay text` without the surrounding whitespace | Low |
| MS-ASGN-017 | File with special-character/emoji filename uploads and filename is preserved | `Essay Draft` accepts file submissions | 1. Click "Add submission"<br>2. Upload a file whose name contains special characters and emoji (e.g., `essay_🎓_draft.pdf`)<br>3. Click "Save changes"<br>4. Reopen the assignment page | The file appears in the submission file list with its original filename preserved including the special characters and emoji | Low |
| MS-ASGN-018 | Rapid re-submission via browser Back does not create duplicate submission | `student1` has just saved an `Essay Draft` submission | 1. Immediately after saving, press browser Back<br>2. Resubmit the form if prompted<br>3. Reopen the assignment page | Only one submission record exists for `student1`; no duplicate submission entry or duplicate file appears | Medium |
