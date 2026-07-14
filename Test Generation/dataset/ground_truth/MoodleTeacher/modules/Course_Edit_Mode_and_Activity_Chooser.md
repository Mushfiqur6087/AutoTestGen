# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Course Edit Mode and Activity Chooser

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-001 | Enable course edit mode | Teacher is on course page | 1. Toggle edit mode on | Section, activity, bulk action, and add controls become visible | High |
| MT-CEDIT-002 | Rename a course section inline | Edit mode is on and section `Week 1` exists | 1. Click the section inline edit icon<br>2. Rename `Week 1` to `Week 1 - Orientation`<br>3. Save and refresh course page | The renamed section title persists after refresh and the old title is no longer shown | High |
| MT-CEDIT-003 | Hide an activity from students | Edit mode is on and `Essay Draft` is visible | 1. Open the `Essay Draft` activity menu<br>2. Select Hide<br>3. Open the course as `student1` | `Essay Draft` is hidden from the student view while remaining visible to `teacher1` with a hidden indicator | High |
| MT-CEDIT-004 | Bulk hide selected activities | Edit mode is on and at least two visible activities exist | 1. Select `Essay Draft` and one other activity<br>2. Use the bulk action toolbar to hide selected activities<br>3. Refresh course page | Only the selected activities are hidden; unselected activities remain visible | Medium |
| MT-CEDIT-005 | Open Activity Chooser | Edit mode is on | 1. Click "+ Add an activity or resource" | Activity Chooser modal opens with categories, search, and activity/resource tiles | High |
| MT-CEDIT-006 | Select Assignment from Activity Chooser | Activity Chooser is open | 1. Select Assignment<br>2. Click "Add" | Assignment creation form opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-007 | Edit controls hidden when edit mode is off | Teacher is on course page with edit mode off | 1. Inspect sections and activities | Authoring controls are hidden | High |
| MT-CEDIT-008 | Add action with no tile selected | Activity Chooser is open | 1. Click Add without selecting an activity/resource | No activity is created and user is prompted to select an item | Medium |
| MT-CEDIT-009 | Delete action requires confirmation | Edit mode is on | 1. Delete a section or activity<br>2. Cancel confirmation | Item remains unchanged | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-010 | Activity chooser search no results | Activity Chooser is open | 1. Search for non-existent activity type | Empty/no-results state is displayed | Low |
| MT-CEDIT-011 | Nested subsection creation | Edit mode is on in section `Week 1` | 1. Click "+ Add a subsection"<br>2. Name it `Ground Truth Subsection`<br>3. Save and refresh course page | `Ground Truth Subsection` appears nested under `Week 1` after refresh and can be removed during cleanup | Medium |
| MT-CEDIT-012 | Rename section inline with empty text | Edit mode is on | 1. Click inline edit for a section<br>2. Clear the text and press Enter | Section name reverts to its previous value or displays a required-field error; no unnamed section is created | High |
| MT-CEDIT-013 | Rename section inline with very long text | Edit mode is on | 1. Click inline edit for a section<br>2. Enter a 200+ character string and press Enter | Long text is saved and visible, wrapping correctly without breaking the page layout | Low |
| MT-CEDIT-014 | Drag and drop an activity to reorder | Edit mode is on and course has activities | 1. Click and hold the move handle for an activity<br>2. Drag it to a new position<br>3. Release | Activity appears in the new position and layout persists | High |
| MT-CEDIT-015 | Drag and drop a section to reorder | Edit mode is on and course has multiple sections | 1. Click and hold the move handle for a section<br>2. Drag it above another section<br>3. Release | Section appears in the new position with its contents intact and layout persists | High |
| MT-CEDIT-016 | Rapid consecutive clicks on hide/show activity toggle | Edit mode is on and an activity is visible | 1. Open activity action menu<br>2. Rapidly toggle Hide/Show multiple times | Activity ends in the visibility state corresponding to the final toggle action; no intermediate locked state | Medium |
| MT-CEDIT-017 | Duplicate an activity | Edit mode is on and `Essay Draft` exists | 1. Open action menu for `Essay Draft`<br>2. Select Duplicate | A copy of the activity appears with "copy" in the title; original activity remains unchanged | High |
| MT-CEDIT-018 | Delete section containing activities warns of cascading delete | Edit mode is on and section contains activities | 1. Open action menu for the section<br>2. Select Delete | A confirmation dialog explicitly warns that deleting the section will also delete its contained activities | High |
| MT-CEDIT-019 | Rapid double-click on Add activity button | Edit mode is on | 1. Rapidly double-click "+ Add an activity or resource" | Activity Chooser modal opens exactly once | Low |
| MT-CEDIT-020 | Activity chooser search with special characters | Activity Chooser is open | 1. Search for `@@##🎓` | Search field accepts input without error and displays the no-results state | Low |
| MT-CEDIT-021 | Bulk action bar clears selection when closed | Edit mode is on and bulk action bar is visible | 1. Select multiple activities<br>2. Click the 'X' to close the bulk action bar | Bulk action bar closes and all activity checkboxes are deselected | Medium |
| MT-CEDIT-022 | Edit settings action opens activity form | Edit mode is on and an activity exists | 1. Open action menu for the activity<br>2. Select Edit settings | Activity configuration form opens successfully | High |
