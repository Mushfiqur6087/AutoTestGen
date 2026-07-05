# Test Cases — Moodlestudent

Generated: 2026-07-04T16:43:47.211887Z  
Model: openai/gpt-5-mini  

## Course Page

Total: **18** (positive: 11, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Navigate to Course tab from Course Page tab bar | User logged in as <Enrolled user> and has the <Course Page> open | 1. Click the 'Course' tab in the horizontal tab bar | Navigated to Course tab; course tab content displayed | high |
| TC-002 | WF-002 | Navigate to Participants tab from Course Page tab bar | User logged in as <Enrolled user> and has the <Course Page> open | 1. Click the 'Participants' tab in the horizontal tab bar | Navigated to Participants tab; participants list displayed | high |
| TC-003 | WF-003 | Navigate to Grades tab from Course Page tab bar | User logged in as <Enrolled user> and has the <Course Page> open | 1. Click the 'Grades' tab in the horizontal tab bar | Navigated to Grades tab; grades content displayed | high |
| TC-004 | WF-004 | Navigate to Activities tab from Course Page tab bar | User logged in as <Enrolled user> and has the <Course Page> open | 1. Click the 'Activities' tab in the horizontal tab bar | Navigated to Activities tab; activities content displayed | high |
| TC-005 | WF-005 | Navigate to Competencies tab from Course Page tab bar | User logged in as <Enrolled user> and has the <Course Page> open | 1. Click the 'Competencies' tab in the horizontal tab bar | Navigated to Competencies tab; competencies content displayed | high |
| TC-006 | WF-006 | Collapse all sections using the 'Collapse all' link | User logged in as <Enrolled user> and has the <Course Page> open, <Course Page> has multiple sections expanded | 1. Click the 'Collapse all' link in the course action bar | All sections are collapsed; section contents are hidden and only section headers with collapsed chevrons are visible | medium |
| TC-007 | WF-007 | Expand a collapsed section by clicking its chevron toggle | User logged in as <Enrolled user> and has the <Course Page> open, The <Section> is currently collapsed | 1. Click the chevron toggle for the <Section> | The <Section> expands, showing its list of activities and resources with type icons and clickable names | medium |
| TC-008 | WF-008 | Toggle a section open by clicking its section name link | User logged in as <Enrolled user> and has the <Course Page> open, The <Section> is currently collapsed | 1. Click the <Section> name link in the section header | The <Section> expands, showing its list of activities and resources with type icons and clickable names | medium |
| TC-009 | WF-009 | Open an activity from an expanded section by clicking the activity name | User logged in as <Enrolled user> and has the <Course Page> open, The <Section> is expanded and contains at least one <Activity> | 1. Click the activity name <Activity> listed inside the <Section> | The <Activity> page opens, showing its title and content | high |
| TC-010 | WF-010 | Open an activity via its clickable name (alternate repeating-group item) | User logged in as <Enrolled user> and has the <Course Page> open, The <Section> is expanded and contains at least one <Activity> | 1. Click the activity name link for the alternate <Activity> item inside the <Section> | The <Activity> page opens, showing its title and content | high |
| TC-011 |  | Verify students cannot enable Edit mode on the Course Page | User logged in as <Student> and has the <Course Page> open | 1. Inspect the course action bar / top-right action area on the Course Page | No 'Edit mode' toggle is present in the course action bar for the student | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 |  | Unauthenticated user cannot access Course Page | User is not logged in | 1. In a browser session where the user is not authenticated, navigate directly to the Course Page URL for a specific course | User is redirected to the login page or shown a login prompt; the Course page heading, tab bar, and course content are not displayed (the Course Page is not accessible while unauthenticated). | high |
| TC-013 | WF-006 | Logged-in user who is not enrolled cannot use 'Collapse all' action | User is logged in, User is NOT enrolled in the target course | 1. Log in as a user account that is not enrolled in the course<br>2. Navigate to the Course Page URL for that course<br>3. Attempt to locate and click the 'Collapse all' link in the course header | The 'Collapse all' link is not visible or is not actionable for a non-enrolled user; clicking does not collapse sections and the section expanded/collapsed states remain unchanged (the 'Collapse all' action is blocked because the user is not enrolled). | high |
| TC-014 |  | Enrolled student cannot enable Edit mode on Course Page | User is logged in, User is enrolled in the course, User has the Student role | 1. Log in as an enrolled user with the Student role<br>2. Open the Course Page for the course<br>3. Attempt to enable Edit mode (attempt to locate and toggle any 'Edit mode' / 'Turn editing on' control) | No Edit mode control is available or it is disabled for the Student role; the Course Page remains in view-only mode and no editing controls or editable fields are revealed (students cannot enable Edit mode). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (interaction_edge) | WF-006 | Click 'Collapse all' when all sections are already collapsed | User is logged in, enrolled in the course, and the Course Page is open, Every section on the Course Page is in the collapsed state | 1. Click the 'Collapse all' link in the Course Page action bar | succeeds: The UI remains with every section shown in the collapsed state; no error or warning is displayed and no visual glitch appears (each section header shows the collapsed indicator) | medium |
| TC-016 (interaction_edge) | WF-006 | Rapid double-click of 'Collapse all' while sections are expanded | User is logged in, enrolled in the course, and the Course Page is open, At least one section on the Course Page is currently expanded | 1. Click the 'Collapse all' link<br>2. Immediately click the 'Collapse all' link a second time | succeeds: After the second click the UI shows all sections collapsed; no duplicate action, error message, or visual corruption occurs and section headers show collapsed state | medium |
| TC-017 (input_edge) | WF-007 | Toggle a section whose name is a very long string (200+ characters) | User is logged in, enrolled in the course, and the Course Page is open, The course contains a section whose displayed name is a very long string (e.g., 200+ characters) | 1. Locate the section header with the very long name<br>2. Click the section's chevron toggle to expand the section<br>3. Click the section name link to collapse the section | succeeds: The very long section name is rendered (may wrap across lines) without breaking the page layout; clicking the chevron expands and displays that section's activities, and clicking the section name collapses it back; no error or visual overflow occurs | low |
| TC-018 (input_edge) | WF-009 | Open an activity whose displayed name contains emoji and special Unicode characters | User is logged in, enrolled in the course, and the Course Page is open, The course contains an activity whose displayed name includes emoji and non-ASCII Unicode characters | 1. Expand the section containing the activity if it is collapsed<br>2. Click the activity's clickable name | succeeds: Clicking the activity name navigates to the activity (or displays the activity content) and the activity title shown on the target view contains the same emoji and Unicode characters; no error is displayed | low |

---
