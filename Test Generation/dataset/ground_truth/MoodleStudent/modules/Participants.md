# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Participants

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-001 | Participants table displayed | Student opens Participants tab | 1. Open Participants | Filters, alphabetical filters, and participant table are visible | High |
| MS-PART-002 | Filter participants by teacher name | Participants include `teacher1` | 1. Add a First name filter for the seeded teacher<br>2. Apply filters | Participants table shows `teacher1` and hides unrelated participant rows | High |
| MS-PART-003 | Alphabetical filters | Participants exist | 1. Select first-name or last-name initial | Table filters by selected initial | Medium |
| MS-PART-004 | Open participant profile | Participant row exists | 1. Click participant name | Participant profile page opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-005 | Student cannot enrol users | Student is on Participants page | 1. Inspect page toolbar | Enrol users button, role dropdown, and enrollment duration controls are not rendered | High |
| MS-PART-006 | Student cannot edit/remove roles | Student is on Participants page | 1. Inspect row menus<br>2. Navigate directly to a role-management URL | Role edit and remove actions are not rendered; direct role-management URL shows access denied before any role form renders | High |
| MS-PART-007 | Participants blocked while unauthenticated | User is logged out | 1. Navigate directly to Participants URL | User is redirected to the login page before the participants table renders | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-008 | Filter no matching users | Participants page is visible | 1. Apply filter with no matches | Empty/no-results state is displayed | Medium |
| MS-PART-009 | Multiple filter conditions | Participants include `student1` and `teacher1` | 1. Add a Role filter for Teacher<br>2. Add a name filter for `teacher1`<br>3. Apply filters | Table shows `teacher1`; `student1` and non-matching users are absent from the filtered table | Medium |
| MS-PART-010 | Apply filters with empty condition row — participants list updates without error | Participants page is visible with the filter panel open | 1. Add a filter condition row but leave its value empty<br>2. Click "Apply filters" | Participants list updates or shows all participants without a JavaScript error; no page crash occurs | Low |
| MS-PART-011 | Rapid First Name initial changes resolve to final selection only | Participants page is visible | 1. Click alphabetical initial "A"<br>2. Immediately click initial "B"<br>3. Immediately click initial "C" | Table reflects the last-clicked initial ("C") only; no stale intermediate filter result is permanently shown | Medium |
| MS-PART-012 | Row checkbox selection persists after navigating to participant profile and pressing Back | Participants page is visible; at least two participant rows exist | 1. Check the checkbox for `student1` row<br>2. Click `student1` name to open profile<br>3. Press browser Back | Participants page reloads; the previously checked row checkbox for `student1` is no longer checked (fresh page state) and no JavaScript error appears | Low |
| MS-PART-013 | Student role enrollment management features not visible or interactive | `student1` is on the Participants page | 1. Inspect each participant row for role-edit controls<br>2. Inspect the toolbar for enrollment management buttons | Role-edit icons, "Enrol users" button, and enrollment duration controls are not rendered for any row | High |
