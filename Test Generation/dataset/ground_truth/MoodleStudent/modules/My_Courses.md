# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-001 | Student course cards displayed | Student is enrolled in courses | 1. Open My Courses | Course cards show image, course name, and category | High |
| MS-COURSES-002 | Filter, search, sort, and layout controls | `student1` is enrolled in `QA Automation 101` and at least one other course | 1. Select All status filter<br>2. Search for `QA Automation`<br>3. Sort by course name<br>4. Switch to list layout | Only matching course cards/rows remain visible, order follows the sort selection, and list layout persists after refresh | High |
| MS-COURSES-003 | Open course from course card | At least one course is visible | 1. Click course name | Student opens course main page | High |
| MS-COURSES-004 | Star course from course card | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Star this course"<br>3. Refresh My Courses | `QA Automation 101` appears in the Starred filter and `student1` remains enrolled | Medium |
| MS-COURSES-009 | Remove course from view without unenrolling | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Select Hidden filter<br>4. Open the hidden course card | `QA Automation 101` appears under Hidden, opens successfully, and `student1` remains enrolled as student | Medium |
| MS-COURSES-013 | Remove from view then immediately verify course appears in Hidden filter | `QA Automation 101` course card is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Immediately switch to the Hidden filter without refreshing | `QA Automation 101` appears in the Hidden filter list immediately after the action; no page refresh is required | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-005 | My Courses blocked while unauthenticated | User is logged out | 1. Navigate directly to My Courses URL | User is redirected to login | High |
| MS-COURSES-006 | Search no matching course | Student is logged in | 1. Search for non-existent course | Empty/no-results state is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-007 | Hidden-course filter | `QA Automation 101` was removed from view | 1. Select Hidden filter<br>2. Search for `QA Automation` | `QA Automation 101` is listed in Hidden with its course name and category; non-hidden courses are absent from the filtered list | Medium |
| MS-COURSES-008 | Long symbol search | My Courses is visible | 1. Search with `QA Automation @@@ ### 1234567890 long-search-token` | Search field retains the entered string, no matching-error dialog appears, and the course list shows matching or no-results content in the same layout | Low |
| MS-COURSES-010 | Very long search query (200+ chars) accepted without error | My Courses is visible | 1. Enter a 200+ character string into the course search field<br>2. Submit the search | Search field accepts and retains the long string; no error dialog appears; a matching or empty-results list is displayed without page crash | Low |
| MS-COURSES-011 | Search with special characters and emoji accepted | My Courses is visible | 1. Enter `@@##🎓 courses` into the search field<br>2. Submit the search | Search field accepts the input; no crash or validation error appears; list shows matching or empty-results content | Low |
| MS-COURSES-012 | Rapid star action on same course card is idempotent | `QA Automation 101` course card is visible and not starred | 1. Click "Star this course" on the `QA Automation 101` card menu<br>2. Immediately repeat the star action | Course is starred once; the Starred filter shows `QA Automation 101` exactly once with no duplicate entries | Medium |
