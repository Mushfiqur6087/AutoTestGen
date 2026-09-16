# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Course Settings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-001 | Save required course settings | Teacher opens Course Settings | 1. Change full name to `QA Automation 101 - Ground Truth`<br>2. Keep short name and category populated<br>3. Click "Save and display" | Course page opens with heading `QA Automation 101 - Ground Truth`; the original course name is restored during cleanup | High |
| MT-CSET-002 | Course Start Date invalid format is rejected | Course Settings is open | 1. Enter an invalid date format into Course Start Date<br>2. Click Save and display | Save is blocked; inline validation error appears on the Course Start Date field indicating it must be a valid date; settings are not persisted | Medium |
| MT-CSET-003 | Course summary with emoji is saved and preserved | Course Settings is open | 1. Paste a rich-text course summary containing emoji and special Unicode characters<br>2. Save and reopen settings | Form saves successfully and the full summary content, including emoji/special characters, is preserved after reopening Course Settings | Medium |
| MT-CSET-004 | Course format selection reveals and persists Layout Controls | Course Settings is open | 1. Select a Course Format to trigger Layout Controls visibility<br>2. Enter a long value into Layout Controls<br>3. Save and reopen settings | Form saves successfully and the Layout Controls field displays the full saved value with no truncation after reopening | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-005 | Course full name empty | Course Settings is open | 1. Clear Course full name<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-006 | Course short name empty | Course Settings is open | 1. Clear Course short name<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-007 | Course category empty | Course Settings is open | 1. Remove or leave category empty<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-008 | Cancel leaves settings unchanged | Course Settings has unsaved edits | 1. Click "Cancel" | Unsaved changes are discarded | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-009 | Conditional Course End Date enabled but invalid is rejected | Course Settings is open | 1. Check the Enable Course End Date checkbox<br>2. Enter an invalid date format into Course End Date<br>3. Click Save and display | Save is blocked; inline validation error appears on the Course End Date field indicating it must be a valid date; settings are not persisted | Medium |
| MT-CSET-010 | Maximum upload size option | Course Settings is open | 1. Select `10 MB` in Maximum upload size<br>2. Save and reopen settings | Maximum upload size remains `10 MB` after reopening Course Settings | Low |
| MT-CSET-011 | Enabling Course End Date reveals the field and saves successfully | Course Settings is open | 1. Check the Enable Course End Date checkbox<br>2. Verify the Course End Date field becomes visible<br>3. Enter a valid date and click Save and display | Form submits successfully and returns to the course page; the course heading shows the updated course name | Medium |
| MT-CSET-012 | Course end date one day before start date | Course Settings is open | 1. Enable end date<br>2. Set end date to exactly one day before start date<br>3. Save | Save is blocked by date-range validation and settings are not updated | Medium |
| MT-CSET-013 | Very long Course Full Name (200+ chars) | Course Settings is open | 1. Enter a 200+ character string in Course full name<br>2. Save | Name is saved and visible, possibly truncated at system limit, but does not crash the page | Low |
| MT-CSET-014 | Special characters and emoji in Course Short Name | Course Settings is open | 1. Enter a short name containing emoji and special characters<br>2. Save and reopen settings | Form saves successfully and the exact emoji/characters are preserved | Low |
| MT-CSET-015 | Leading/trailing whitespace in Course Short Name trimmed | Course Settings is open | 1. Enter a short name with leading and trailing spaces<br>2. Save and reopen settings | Whitespace is automatically trimmed from the saved short name | Low |
| MT-CSET-016 | Non-numeric value in Appearance News Items | Course Settings is open | 1. Expand Appearance section<br>2. Enter a non-numeric string in "Number of announcements"<br>3. Save | Save is blocked by numeric validation on the field | Medium |
| MT-CSET-017 | Course Settings blocked while unauthenticated | User is not logged in | 1. Open the Course Settings URL for an existing course while logged out | User is redirected to the login page or shown an access-denied page; the Course Settings form and Save button are not accessible | Medium |
| MT-CSET-018 | Settings tab not present for non-teacher role | User is logged in as a non-teacher role (e.g., student) | 1. Log in as a user without teacher/editing permissions<br>2. Navigate to the course page | The Settings tab is not present on the course's tab bar for this user role; the Course Settings form is not visible or accessible | Low |
