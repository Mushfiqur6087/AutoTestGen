# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Participants Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-001 | Participants management controls displayed | Teacher opens Participants page | 1. Open Participants tab | Scope dropdown, Enrol users button, filters, alphabetical filters, table, row menus, and bulk dropdown are visible | High |
| MT-PART-002 | Filter participants by student name | Participants include `student1` | 1. Add a First name filter for the seeded student<br>2. Apply filters | Participants table shows `student1` and hides unrelated participant rows | High |
| MT-PART-003 | Alphabetical filtering | Participants exist | 1. Select First name or Last name initial | Participants table filters by selected initial | Medium |
| MT-PART-004 | Enrol user dialog | A non-enrolled fixture user exists | 1. Click "Enrol users"<br>2. Search for the fixture user<br>3. Select Student role and enrollment duration<br>4. Confirm<br>5. Search the participants table for that user | User appears in the participants table with Student role and active enrollment status | High |
| MT-PART-005 | Row action menu targets selected participant | Participants table includes `student1` | 1. Open the row action menu for `student1`<br>2. Select view profile | `student1` profile opens and the page does not navigate to any other participant profile | Medium |
| MT-PART-012 | Bulk action requires explicit checked rows | Participants table includes `student1` and another user | 1. Check only `student1`<br>2. Open "With selected users..." dropdown | Bulk action context is limited to the checked row; unchecked participant rows remain unselected | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-006 | Participants blocked while unauthenticated | User is logged out | 1. Navigate directly to Participants URL | User is redirected to the login page before the participants table is rendered | High |
| MT-PART-007 | Enrol dialog with no selected user | Enrol users dialog is open | 1. Leave user search empty<br>2. Confirm | Enrollment is blocked with validation feedback | High |
| MT-PART-008 | Filter with no matches | Participants page is visible | 1. Apply filter that matches no users | Empty/no-results state is displayed | Medium |
| MT-PART-009 | Clear filters resets conditions | Filters are active | 1. Click "Clear filters" | Filters are removed and full list returns | Medium |
| MT-PART-013 | Confirm enrollment with no user selected | Enrol users dialog is open | 1. Leave User search blank<br>2. Select `Student` role<br>3. Click "Enrol users" | Save is blocked by a required-field validation error on the user search field | High |
| MT-PART-014 | Confirm enrollment with no role selected | Enrol users dialog is open | 1. Select a valid user<br>2. Leave Role dropdown blank<br>3. Click "Enrol users" | Save is blocked by a required-field validation error on the role field | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-010 | Multiple filter conditions | Participants include `student1` and `teacher1` | 1. Add a Role filter for Student<br>2. Add a name filter for `student1`<br>3. Apply filters | Table shows `student1`; `teacher1` and non-matching users are absent from the filtered table | Medium |
| MT-PART-011 | Bulk action with no users selected | Participants page is visible | 1. Leave all checkboxes empty<br>2. Open "With selected users..." dropdown | Bulk action cannot be submitted and the participants table remains unchanged | Medium |
| MT-PART-015 | Confirm enrollment then immediately navigate back | Enrol users dialog is open | 1. Complete enrollment<br>2. Click browser Back | Duplicate enrollment is blocked; no duplicate row appears in the participants table | Medium |
| MT-PART-016 | User search with very long string and emoji | Enrol users dialog is open | 1. Search for a 200+ character string containing emoji<br>2. Submit | Dialog does not crash; UI displays "No results" safely without layout breaking | Low |
| MT-PART-017 | Alphabet filter with no matching participants | Participants list is visible | 1. Select First name `Z`<br>2. Assume no users start with `Z` | Table updates to display the empty state "Nothing to display" without error | Low |
