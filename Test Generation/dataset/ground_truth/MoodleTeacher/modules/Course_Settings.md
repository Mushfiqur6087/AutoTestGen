# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Course Settings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-001 | Save required course settings | Teacher opens Course Settings | 1. Change full name to `QA Automation 101 - Ground Truth`<br>2. Keep short name and category populated<br>3. Click "Save and display" | Course page opens with heading `QA Automation 101 - Ground Truth`; the original course name is restored during cleanup | High |
| MT-CSET-002 | Configure visibility and date fields | Course Settings is open | 1. Set Course visibility to Hide<br>2. Enable start/end date fields<br>3. Set start before end<br>4. Save and reopen settings | Visibility is Hide and the saved start/end date values are still populated after reopening settings | Medium |
| MT-CSET-003 | Configure course summary and image | Course Settings is open | 1. Set summary to `Ground truth course summary`<br>2. Upload `course-banner-ground-truth.png`<br>3. Save and reopen settings | Summary text and uploaded image filename are visible after reopening Course Settings | Medium |
| MT-CSET-004 | Configure format, completion, groups, and tags | Course Settings is open | 1. Set format to Topics format<br>2. Enable completion tracking<br>3. Set group mode to Separate groups<br>4. Add tag `ground-truth`<br>5. Save and reopen settings | Topics format, completion tracking, Separate groups, and tag `ground-truth` remain selected after reopening settings | Medium |

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
| MT-CSET-009 | End date earlier than start date | Course Settings is open | 1. Enable end date<br>2. Set end date before course start date<br>3. Save | Save is blocked with a date-range validation message and the previous course dates remain unchanged | Medium |
| MT-CSET-010 | Maximum upload size option | Course Settings is open | 1. Select `10 MB` in Maximum upload size<br>2. Save and reopen settings | Maximum upload size remains `10 MB` after reopening Course Settings | Low |
| MT-CSET-011 | Course end date exactly equals start date | Course Settings is open | 1. Enable end date<br>2. Set end date to the exact same day/time as start date<br>3. Save and display | Form saves successfully and the course dates are updated | Medium |
| MT-CSET-012 | Course end date one day before start date | Course Settings is open | 1. Enable end date<br>2. Set end date to exactly one day before start date<br>3. Save | Save is blocked by date-range validation and settings are not updated | Medium |
| MT-CSET-013 | Very long Course Full Name (200+ chars) | Course Settings is open | 1. Enter a 200+ character string in Course full name<br>2. Save | Name is saved and visible, possibly truncated at system limit, but does not crash the page | Low |
| MT-CSET-014 | Special characters and emoji in Course Short Name | Course Settings is open | 1. Enter a short name containing emoji and special characters<br>2. Save and reopen settings | Form saves successfully and the exact emoji/characters are preserved | Low |
| MT-CSET-015 | Leading/trailing whitespace in Course Short Name trimmed | Course Settings is open | 1. Enter a short name with leading and trailing spaces<br>2. Save and reopen settings | Whitespace is automatically trimmed from the saved short name | Low |
| MT-CSET-016 | Non-numeric value in Appearance News Items | Course Settings is open | 1. Expand Appearance section<br>2. Enter a non-numeric string in "Number of announcements"<br>3. Save | Save is blocked by numeric validation on the field | Medium |
| MT-CSET-017 | Rapid re-submission via browser Back | Course Settings is open | 1. Save settings successfully<br>2. Press browser Back to return to form<br>3. Click save again | Second save succeeds without creating duplicate courses or configurations | Medium |
| MT-CSET-018 | Dropdown visibility toggle state preservation | Course Settings is open | 1. Set Group mode to Separate groups<br>2. Select a Grouping<br>3. Change Group mode to No groups (Grouping field hides)<br>4. Change Group mode back to Separate groups | The previously selected Grouping value is restored when the field becomes visible again | Low |
