# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-001 | Student course tabs displayed | `student1` is enrolled in `QA Automation 101` | 1. Open the `QA Automation 101` course page | Course, Participants, Grades, Activities, and Competencies tabs are visible; Settings tab and edit controls are not visible | High |
| MS-COURSE-002 | Course sections and activities displayed | Course contains sections | 1. Inspect course content | Sections, activity icons, and activity/resource names are visible | High |
| MS-COURSE-003 | Collapse all sections | Sections are expanded | 1. Click "Collapse all" | Sections collapse | Medium |
| MS-COURSE-004 | Toggle section with very long name (200+ chars) | Course contains a section with a 200+ character name | 1. Click chevron to expand the long-named section<br>2. Click section name to collapse it | Long name renders without breaking layout; expand/collapse both succeed | Low |
| MS-COURSE-005 | Open activity from course page | Activity link is visible | 1. Click assignment, forum, page, or resource link | Activity/resource page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-006 | Not-enrolled user cannot use Collapse all | User logged in, not enrolled in course | 1. Navigate to Course Page<br>2. Attempt to click "Collapse all" | Collapse all link not visible/actionable; section states unchanged | High |
| MS-COURSE-007 | Student cannot enable course edit mode | Student is on course page | 1. Inspect page controls<br>2. Navigate directly to the edit-mode course URL | Edit toggle is absent; direct edit-mode URL returns to read-only course view or access denied without authoring controls | High |
| MS-COURSE-008 | Course page blocked while unauthenticated | User is logged out | 1. Navigate directly to course URL | User is redirected to the login page before course sections render | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-009 | Open activity with emoji/Unicode name | Course contains an activity with emoji/Unicode in its name | 1. Expand the section if collapsed<br>2. Click the activity's clickable name | Activity opens; the activity title shows the same emoji/Unicode characters; no error | Low |
| MS-COURSE-010 | Rapid double-click "Collapse all" while sections expanded | At least one section expanded | 1. Click "Collapse all"<br>2. Immediately click "Collapse all" again | All sections end collapsed; no duplicate action, error, or visual corruption | Medium |
| MS-COURSE-011 | Collapse all when all sections already collapsed | Every section is in the collapsed state | 1. Click "Collapse all" | All sections remain collapsed; no error or visual glitch appears | Low |
| MS-COURSE-012 | Collapse all when some sections already collapsed — all end collapsed | `QA Automation 101` course page shows a mix of expanded and collapsed sections | 1. Click "Collapse all" | All sections are collapsed regardless of their prior state; no section headers show expanded content | Medium |
| MS-COURSE-013 | Rapid single-section toggle ends in final clicked state | Section `Week 1` is visible | 1. Click the `Week 1` toggle arrow rapidly three times in quick succession | `Week 1` ends in the state corresponding to the final click (expanded or collapsed); no intermediate state is permanently locked | Medium |
| MS-COURSE-014 | Collapse all after adding then removing all sections succeeds silently | Course page is open; all sections were added then removed so the course has zero sections | 1. Click "Collapse all" | Collapse all completes silently; no error is displayed and the empty course page remains rendered | Low |
