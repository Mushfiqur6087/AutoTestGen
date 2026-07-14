# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-001 | Course cards displayed | Teacher is enrolled in courses | 1. Open My Courses | Course cards show image, course name, and category | High |
| MT-COURSES-002 | Filter, search, sort, and layout controls | `teacher1` has access to `QA Automation 101` and at least one other course | 1. Select All status filter<br>2. Search for `QA Automation`<br>3. Sort by course name<br>4. Switch to list layout | Only matching courses remain visible, order follows the sort selection, and list layout persists after refresh | High |
| MT-COURSES-003 | Open course from course card | At least one course is visible | 1. Click a course name | Teacher opens the course main page | High |
| MT-COURSES-004 | Star course from course card | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Star this course"<br>3. Refresh My Courses | `QA Automation 101` appears in the Starred filter and teacher enrollment remains unchanged | Medium |
| MT-COURSES-009 | Remove course from view without unenrolling | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Select Hidden filter<br>4. Open the hidden course card | `QA Automation 101` appears under Hidden, opens successfully, and `teacher1` remains enrolled as teacher | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-005 | My Courses blocked while unauthenticated | User is logged out | 1. Navigate directly to My Courses URL | User is redirected to login | High |
| MT-COURSES-006 | Search with no matching course | Teacher is logged in | 1. Search for a non-existent course | Empty/no-results state is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-007 | Hidden-course filter | `QA Automation 101` was removed from view | 1. Select Hidden filter<br>2. Search for `QA Automation` | `QA Automation 101` is listed in Hidden with its course name and category; non-hidden courses are absent from the filtered list | Medium |
| MT-COURSES-008 | Special-character search | Courses page is visible | 1. Search with `@@@` | No matching course cards are displayed, no validation error appears, and the search field remains editable | Low |
| MT-COURSES-010 | Very long search query (200+ chars) accepted without error | My Courses is visible | 1. Enter a 200+ character string into the course search field<br>2. Submit the search | Search field accepts and retains the long string; no error dialog appears; a matching or empty-results list is displayed | Low |
| MT-COURSES-011 | Search with leading and trailing whitespace is trimmed | My Courses is visible and `QA Automation 101` exists | 1. Search for `   QA Automation   ` (with spaces) | Course `QA Automation 101` is displayed successfully; whitespace is ignored for the search match | Low |
