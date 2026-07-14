# Moodle Student Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleStudent/MoodleStudent.md

## Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-001 | Personalized dashboard greeting | Student is logged in | 1. Open Dashboard | Greeting for the logged-in student is displayed | High |
| MS-DASH-002 | Timeline shows upcoming activities | `Essay Draft` has a due date within the selected timeline range | 1. Log in as `student1`<br>2. Open Dashboard<br>3. Inspect Timeline block | Timeline lists `Essay Draft` with course name, due date, and direct activity link | High |
| MS-DASH-003 | Timeline controls update content | Timeline contains `Essay Draft` and at least one non-matching activity | 1. Select a range containing `Essay Draft`<br>2. Sort by date<br>3. Search for `Essay` | Timeline shows `Essay Draft`, hides non-matching activities, and preserves the selected controls | High |
| MS-DASH-004 | Calendar block supports personal event flow | Calendar block is visible | 1. Click "New event" | Personal calendar event form or modal opens with event title, date, and save/cancel controls | Medium |
| MS-DASH-005 | Calendar navigation and links | Calendar block is visible | 1. Select `QA Automation 101` in the course filter<br>2. Navigate to next month and back<br>3. Click Full calendar | Calendar heading changes then returns to the original month; Full calendar opens with `QA Automation 101` filter context visible | Medium |
| MS-DASH-006 | Add student dashboard block | Student is on Dashboard and Edit mode is enabled | 1. Click "+ Add a block"<br>2. Add `Latest announcements`<br>3. Refresh Dashboard | `Latest announcements` appears on `student1` Dashboard after refresh and is not added to `teacher1` Dashboard | Medium |
| MS-DASH-013 | Delete student dashboard block | `Latest announcements` is visible on `student1` Dashboard in Edit mode | 1. Open the block menu<br>2. Delete `Latest announcements`<br>3. Refresh Dashboard | `Latest announcements` is removed from `student1` Dashboard after refresh | Medium |
| MS-DASH-016 | Reset dashboard to default in edit mode reverts layout | `student1` is on Dashboard with Edit mode enabled and at least one block repositioned or added | 1. Click the "Reset page to default" option in Edit mode<br>2. Confirm the reset | Dashboard layout reverts to the default block arrangement and any added or repositioned blocks return to their original positions | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-007 | Dashboard blocked while unauthenticated | User is logged out | 1. Navigate directly to Dashboard URL | User is redirected to login | High |
| MS-DASH-008 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect Dashboard controls | "+ Add a block", configure, move, and delete controls are not rendered on the Dashboard | High |
| MS-DASH-009 | Timeline search with no matches | Student is logged in | 1. Search for non-existent activity | Empty/no-results state is displayed | Medium |
| MS-DASH-017 | Delete Timeline block via block menu removes it from dashboard | `student1` is on Dashboard with Edit mode enabled and Timeline block visible | 1. Open the block action menu on the Timeline block<br>2. Click "Delete Timeline" and confirm<br>3. Refresh Dashboard | Timeline block is absent from the Dashboard after refresh; no error message is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-010 | Dashboard with no upcoming work | Student has no pending activities | 1. Open Dashboard | Timeline shows its no-activity empty state and Calendar block remains visible | Low |
| MS-DASH-011 | Calendar year boundary | Calendar displays January | 1. Click previous-month arrow | Calendar shows December of previous year | Medium |
| MS-DASH-012 | Rapid edit-mode toggle | Dashboard is visible | 1. Toggle Edit mode repeatedly | Final UI state matches final toggle | Medium |
| MS-DASH-014 | Timeline empty state when selected range has zero activities | `student1` is on Dashboard; a date range with no activities is known | 1. Select the date range that contains no scheduled activities | Timeline block displays its empty-state message and no activity rows are rendered | Low |
| MS-DASH-015 | Timeline search with special characters and emoji accepted | `student1` is on Dashboard | 1. Type `@@##🎓` into the Timeline search field | Search field accepts the input without error; timeline shows empty-results state or matching items; no crash or validation dialog appears | Low |
| MS-DASH-018 | Navigate calendar to previous month removes current-date highlight | Calendar block is visible and shows the current month | 1. Click the previous-month arrow on the Calendar block | Calendar advances to the previous month; the current-date highlight is absent on the previous month view | Low |
