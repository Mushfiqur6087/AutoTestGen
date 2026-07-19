# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Activities

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-001 | Add new Activity Type row | User logged in | 1. Open Activities tab<br>2. Click "Add Row" in Additional Activity Types<br>3. Enter activity type name<br>4. Save | New collapsible Additional Activity Type section appears in the accordion | High |
| MS-ACT-002 | Assignment activity table | Assignments exist | 1. Inspect Assignments section | Name, due date, and submission status columns are visible | High |
| MS-ACT-003 | Expand collapsed activity type | Forums or Resources section is collapsed | 1. Click section arrow | Section expands and displays activities | Medium |
| MS-ACT-004 | Open activity from overview | Activity row exists | 1. Click activity name | Activity page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-005 | Activities blocked while unauthenticated | User is logged out | 1. Navigate directly to Activities URL | User is redirected to the login page before activity groups render | High |
| MS-ACT-006 | Not-enrolled user cannot view Assignments | User logged in but not enrolled in course | 1. Navigate to course page<br>2. Open Activities tab<br>3. Attempt to view/click an assignment | Access restriction notice shown; Activities accordion and assignment content not available | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-007 | Expanding Forums with zero activities shows empty state | Forums section collapsed, course has zero Forum activities | 1. Click the Forums expand arrow | Forums section expands showing empty-state content area; no error appears | Low |
| MS-ACT-008 | Many activity types | Course has Assignments, Forums, Resources, and one additional activity group | 1. Open Activities tab<br>2. Expand Forums<br>3. Expand Resources<br>4. Collapse Forums | Resources remains expanded while Forums collapses, proving activity groups toggle independently | Low |
| MS-ACT-009 | Rapid double-click on assignment name causes only one navigation | Activities tab is open; at least one assignment row is visible | 1. Double-click the assignment name link rapidly | Browser navigates to the assignment page exactly once; no duplicate page-load or error page appears | Medium |
| MS-ACT-010 | Expand collapsed Forums section then immediately click first activity — succeeds | Activities tab is open; Forums section is collapsed | 1. Click the Forums section arrow to expand it<br>2. Immediately click the first forum activity name | Forums section expands and the forum activity page opens successfully; no stale-state error appears | Medium |
| MS-ACT-011 | Activity name with 200+ chars and special characters is displayed and clickable | An activity with a 200+ character name containing special characters exists in `QA Automation 101` | 1. Open Activities tab<br>2. Locate the long-name activity row<br>3. Click the activity name | Activity name is displayed (possibly truncated) without overflow breaking the table layout; clicking the name opens the activity page | Low |
| MS-ACT-012 | Rapidly toggling multiple collapsible sections each ends in its final state | Activities tab shows Assignments, Forums, and Resources sections | 1. Rapidly click the toggle for Assignments, then Forums, then Resources in quick succession | Each section ends in the state corresponding to its own last click; no section is permanently stuck in a transitional state | Medium |
| MS-ACT-013 | Cannot click activity name in collapsed additional activity type section | Activities tab is open; at least one additional activity type section is collapsed | 1. Locate a collapsed activity section<br>2. Attempt to click an activity name inside that collapsed section | Activity names inside the collapsed section are not visible or not clickable; no navigation occurs until the section is expanded | Medium |
