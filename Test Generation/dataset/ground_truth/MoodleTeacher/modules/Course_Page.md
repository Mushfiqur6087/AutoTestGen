# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-001 | Teacher course tabs displayed | `teacher1` is enrolled as teacher in `QA Automation 101` | 1. Open the `QA Automation 101` course page | Course, Settings, Participants, Grades, Activities, and Competencies tabs are visible; Settings is visible for the teacher | High |
| MT-COURSE-002 | Sections and activities displayed | Course contains sections | 1. Inspect course content | Sections, activity icons, and activity/resource names are visible | High |
| MT-COURSE-003 | Collapse all sections | Sections are expanded | 1. Click "Collapse all" | All visible sections collapse | Medium |
| MT-COURSE-004 | Open an activity from an expanded section | An expanded section contains an activity/resource | 1. Locate the activity/resource in the expanded section<br>2. Click the activity/resource name link | The activity/resource page opens; the page heading displays the activity name | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-005 | Course page blocked while unauthenticated | User is logged out | 1. Navigate directly to the `QA Automation 101` course URL | User is redirected to the Moodle login page before course content is rendered | High |
| MT-COURSE-006 | Open hidden activity as teacher and student | `Essay Draft` is hidden from students in `QA Automation 101` | 1. Open the course as `teacher1` and inspect `Essay Draft`<br>2. Open the same activity URL as `student1` | `teacher1` sees `Essay Draft` with a hidden/restricted indicator; `student1` sees an access restriction page and no assignment submission form | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-007 | Hide Course Index sidebar | Course Index is open | 1. Click Course Index close button | Sidebar is hidden, course heading remains visible, and the tab bar remains clickable | Low |
| MT-COURSE-008 | Rapid section toggles | Section `Week 1` is visible | 1. Expand/collapse `Week 1` three times | `Week 1` ends in the final clicked state and each activity row appears once | Medium |
| MT-COURSE-009 | Activity link is blocked when its section is collapsed | Course page is visible and a section showing activities is then collapsed | 1. Collapse the section containing an activity<br>2. Attempt to click the activity's name link | The activity link is not visible or clickable while its section is collapsed; no navigation occurs and the section remains collapsed | Medium |
