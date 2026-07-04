# Test Cases — Moodleteacher

Generated: 2026-07-04T15:16:12.934753Z  
Model: openai/gpt-5-mini  

## My Courses

Total: **10** (positive: 5, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open a course by clicking the course name link | User logged in as <Teacher> with access to one or more courses | 1. Click 'My Courses' in the top navigation to open the My Courses page<br>2. Click the course name link for <target course> in the Courses grid | Navigates to Course Main Page | high |
| TC-002 | WF-002 | Open a course by clicking the course card body | User logged in as <Teacher> with access to one or more courses | 1. Click 'My Courses' in the top navigation to open the My Courses page<br>2. Click the body of the course card for <target course> (not the three-dot menu or course name link) | Navigates to Course Main Page | high |
| TC-003 | WF-003 | Star a course from the card actions and verify it is pinned to the top | User logged in as <Teacher> with access to one or more courses | 1. Click 'My Courses' in the top navigation to open the My Courses page<br>2. Open the three-dot menu on the card for <target course><br>3. Click 'Star this course' in the card actions menu | pins the course to the top of the list | medium |
| TC-004 | WF-004 | Remove a course from view via card actions and verify it is hidden | User logged in as <Teacher> with access to one or more courses | 1. Click 'My Courses' in the top navigation to open the My Courses page<br>2. Open the three-dot menu on the card for <target course><br>3. Click 'Remove from view' in the card actions menu | hides the course from the user's view without affecting enrollment | medium |
| TC-005 |  | Filter, search and change layout to List view and verify filtered results and layout | User logged in as <Teacher> with access to one or more courses | 1. Click 'My Courses' in the top navigation to open the My Courses page<br>2. Select <Status> from the Status dropdown<br>3. Enter <search term> in the Search field and execute the search<br>4. Select <Sort option> from the Sort dropdown<br>5. Select 'List' from the Layout dropdown | Courses grid displays only courses matching <search term> and Status = <Status>; unrelated courses are no longer visible. The Courses view is presented in the List layout. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Unauthenticated user cannot access My Courses page | User is not logged in | 1. As an unauthenticated user (no session), navigate to <My Courses URL> | Navigation is blocked: user is redirected to the Login page; the Login form is visible and the Courses Grid is not displayed or accessible | high |
| TC-007 |  | Logged-in user without any course access cannot view course cards | User is logged in but has access to zero courses (no enrollments) | 1. Log in as <user account with no course access><br>2. Navigate to <My Courses URL> | Access precondition fails: the page shows an empty-state/access message and the Courses Grid is not populated; no course cards are shown and navigation to any Course Main Page is not possible from this view | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Search field accepts a very long query (>200 chars) | User is logged in with access to one or more courses, My Courses page is open | 1. Click the Search_Field<br>2. Type a very long string (greater than 200 characters) into the Search_Field<br>3. Press Enter or click the search icon | Search accepts the very long string and the search executes successfully; Courses_Grid updates (displays matching courses if any; otherwise shows the 'no results' / empty state). No UI error or crash is shown — operation succeeds. | low |
| TC-009 (input_edge) |  | Search with emoji, non-Latin unicode, and punctuation characters | User is logged in with access to one or more courses, My Courses page is open | 1. Click the Search_Field<br>2. Type a string containing emoji, non-Latin unicode characters, and punctuation (e.g., quotes, percent signs) into the Search_Field<br>3. Press Enter or click the search icon | Search accepts the special/unicode characters and executes successfully; Courses_Grid updates accordingly (shows matches or the 'no results' state). No input-related error is shown and the Search_Field preserves the entered characters — operation succeeds. | low |
| TC-010 (interaction_edge) |  | Remove from view then verify course appears under Status = Hidden | User is logged in with access to one or more courses, At least one course is visible in the default Courses_Grid (Status = All) | 1. Locate a visible course card in the Courses_Grid<br>2. Click the card's three-dot menu<br>3. Click the 'Remove from view' action<br>4. Observe the Courses_Grid immediately after the action<br>5. Open the Status_Filter dropdown<br>6. Select the 'Hidden' option in the Status_Filter | 'Remove from view' action succeeds: the course card is removed from the current (All) grid view (no longer visible). When Status_Filter is set to 'Hidden', the previously removed course appears in the Courses_Grid. The hide action does not affect enrollment and no error is shown — operation succeeds. | medium |

---
