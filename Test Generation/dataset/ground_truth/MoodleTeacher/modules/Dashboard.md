# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-001 | Personalized dashboard greeting | Teacher is logged in | 1. Open Dashboard | Greeting for the logged-in teacher is displayed | High |
| MT-DASH-002 | Timeline block displays teaching actions | `Essay Draft` has a due date within the selected timeline range | 1. Log in as `teacher1`<br>2. Open Dashboard<br>3. Inspect Timeline block | Timeline lists `Essay Draft` with its course name and due date; no unrelated course item appears when the course filter is active | High |
| MT-DASH-003 | Timeline search filters to matching activities | Timeline contains `Essay Draft` and at least one non-matching activity | 1. Enter a search term matching `Essay Draft` in the Timeline search field | Timeline displays only activities matching the search term; unrelated activities are no longer visible | High |
| MT-DASH-004 | Calendar block navigation | Calendar block is visible and has at least one event for `QA Automation 101` | 1. Select `QA Automation 101` in the course filter<br>2. Record the month heading<br>3. Click previous month<br>4. Click next month | Month heading changes on navigation, returns to the original month after the second click, and only selected-course events are shown | High |
| MT-DASH-005 | Calendar links open destination pages | Calendar block is visible | 1. Click "Full calendar"<br>2. Return<br>3. Click "Import or export calendars" | Full calendar and calendar data management pages open | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-006 | Dashboard blocked while unauthenticated | User is logged out | 1. Navigate directly to Dashboard URL | User is redirected to login and dashboard blocks are not exposed | High |
| MT-DASH-007 | Timeline search with no matches | Teacher is logged in | 1. Search for `zz-no-teaching-item` in the Timeline block | Timeline shows the no-results state, keeps the search term in the field, and leaves range/sort controls enabled | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-008 | Calendar year boundary | Calendar displays January | 1. Click previous-month arrow | Calendar shows December of the previous year | Medium |
| MT-DASH-009 | Very long timeline search | Timeline block is visible | 1. Enter a 200+ character search term ending in `Essay` | Search field retains the full entered term, Timeline displays the no-results state, and the Calendar block remains visible beside it | Low |
| MT-DASH-010 | Timeline empty state when selected range has zero activities | `teacher1` is on Dashboard; a date range with no activities is known | 1. Select the date range that contains no scheduled activities | Timeline block displays its empty-state message and no activity rows are rendered | Low |
| MT-DASH-011 | Timeline search with leading/trailing whitespace is trimmed | `teacher1` is on Dashboard and a known timeline item exists | 1. Enter the exact name of the timeline item with leading and trailing spaces into the Timeline search field | Search input is trimmed; the matching item appears in the Timeline with its normal name, no leading/trailing spaces displayed | Low |
| MT-DASH-012 | Navigate calendar to previous month removes current-date highlight | Calendar block is visible and shows the current month | 1. Click the previous-month arrow on the Calendar block | Calendar advances to the previous month; the current-date highlight is absent on the previous month view | Low |
| MT-DASH-013 | Rapid double-click New event does not open duplicate interfaces | Calendar block is visible | 1. Click the Calendar block's "New event" button<br>2. Immediately click "New event" again | Second click is blocked; only one New event creation interface is displayed; no duplicate modal/page instances appear | Medium |
