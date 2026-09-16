# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Course Edit Mode and Activity Chooser

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-001 | Enable course edit mode | Teacher is on course page | 1. Toggle edit mode on | Section, activity, bulk action, and add controls become visible | High |
| MT-CEDIT-002 | Rename a course section inline | Edit mode is on and section `Week 1` exists | 1. Click the section inline edit icon<br>2. Rename `Week 1` to `Week 1 - Orientation`<br>3. Save and refresh course page | The renamed section title persists after refresh and the old title is no longer shown | High |
| MT-CEDIT-003 | Hide an activity shows a hidden indicator | Edit mode is on and `Essay Draft` is visible | 1. Open the `Essay Draft` activity menu<br>2. Select Hide<br>3. If a confirmation appears, click Confirm | The `Essay Draft` row shows a visible hidden/visibility indicator confirming it is not visible to students | High |
| MT-CEDIT-004 | Bulk hide selected activities | Edit mode is on and at least two visible activities exist | 1. Select `Essay Draft` and one other activity<br>2. Use the bulk action toolbar to hide selected activities<br>3. Refresh course page | Only the selected activities are hidden; unselected activities remain visible | Medium |
| MT-CEDIT-005 | Open Activity Chooser | Edit mode is on | 1. Click "+ Add an activity or resource" | Activity Chooser modal opens with categories, search, and activity/resource tiles | High |
| MT-CEDIT-006 | Select Assignment from Activity Chooser | Activity Chooser is open | 1. Select Assignment<br>2. Click "Add" | Assignment creation form opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-007 | Edit controls hidden when edit mode is off | Teacher is on course page with edit mode off | 1. Inspect sections and activities | Authoring controls are hidden | High |
| MT-CEDIT-008 | Add action with no tile selected | Activity Chooser is open | 1. Click Add without selecting an activity/resource | No activity is created and user is prompted to select an item | Medium |
| MT-CEDIT-009 | Delete action removes the item after confirmation | Edit mode is on | 1. Delete a section or activity<br>2. Confirm the deletion dialog | The deleted section/activity is no longer present in the course listing | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-010 | Activity chooser search no results | Activity Chooser is open | 1. Search for non-existent activity type | Empty/no-results state is displayed | Low |
| MT-CEDIT-011 | Nested subsection creation | Edit mode is on in section `Week 1` | 1. Click "+ Add a subsection"<br>2. Name it `Ground Truth Subsection`<br>3. Save and refresh course page | `Ground Truth Subsection` appears nested under `Week 1` after refresh and can be removed during cleanup | Medium |
| MT-CEDIT-012 | Rename section inline trims leading/trailing whitespace | Edit mode is on | 1. Click inline edit for a section<br>2. Enter a title with leading and trailing whitespace<br>3. Press Enter | The section title is saved and displayed with the intended text; leading/trailing whitespace is removed | High |
| MT-CEDIT-013 | Open section edit interface from three-dot menu | Edit mode is on | 1. Click the section's three-dot menu<br>2. Click "Edit" | The section edit panel is displayed, showing section settings controls and the section's title | Low |
| MT-CEDIT-014 | Initiate moving an activity via the three-dot menu | Edit mode is on and course has activities | 1. Open the three-dot menu for an activity<br>2. Select "Move" | A move UI is displayed allowing selection of a new location for the activity | High |
| MT-CEDIT-015 | Initiate moving a section via the three-dot menu | Edit mode is on and course has multiple sections | 1. Open the three-dot menu for a section<br>2. Select "Move" | A move UI is displayed allowing selection of a new position for the section | High |
| MT-CEDIT-016 | Rapid consecutive clicks on hide/show activity toggle | Edit mode is on and an activity is visible | 1. Open activity action menu<br>2. Rapidly toggle Hide/Show multiple times | Activity ends in the visibility state corresponding to the final toggle action; no intermediate locked state | Medium |
| MT-CEDIT-017 | Duplicate an activity | Edit mode is on and `Essay Draft` exists | 1. Open action menu for `Essay Draft`<br>2. Select Duplicate | A copy of the activity appears with "copy" in the title; original activity remains unchanged | High |
| MT-CEDIT-018 | Bulk delete selected activities | Edit mode is on and multiple activities are present | 1. Select checkboxes for two activities<br>2. Click the Bulk Actions toolbar and select "Delete Selected"<br>3. Confirm the bulk deletion dialog | The selected activity rows are no longer present in the section's activity list | High |
| MT-CEDIT-019 | Bulk move selected activities to another section | Edit mode is on and multiple activities are present across sections | 1. Select checkboxes for two activities<br>2. Click the Bulk Actions toolbar and select "Move Selected"<br>3. Choose a target section and confirm | The moved activities are visible in the target section and no longer listed in their original section | Low |
| MT-CEDIT-020 | Activity chooser search with special characters | Activity Chooser is open | 1. Search for `@@##🎓` | Search field accepts input without error and displays the no-results state | Low |
| MT-CEDIT-021 | Bulk 'Set Access Restrictions' opens editor for selected activities | Edit mode is on and bulk action bar is visible | 1. Select checkboxes for two activities<br>2. Click the Bulk Actions toolbar and select "Set Access Restrictions Selected" | The access restrictions editor opens and lists the selected activities with controls to configure restrictions | Medium |
| MT-CEDIT-022 | Edit settings action opens activity form | Edit mode is on and an activity exists | 1. Open action menu for the activity<br>2. Select Edit settings | Activity configuration form opens successfully | High |
