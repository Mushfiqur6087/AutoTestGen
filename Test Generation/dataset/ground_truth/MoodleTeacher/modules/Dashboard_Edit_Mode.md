# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Dashboard Edit Mode

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-001 | Enable dashboard edit mode | Teacher is on Dashboard | 1. Toggle Edit mode on | Reset button, Add a block button, block move icons, and block menus are visible | High |
| MT-DEDIT-002 | Add a dashboard block | Edit mode is on and `Latest announcements` block is not already present | 1. Click "+ Add a block"<br>2. Select `Latest announcements` | `Latest announcements` block appears on the teacher Dashboard and remains visible after page refresh | High |
| MT-DEDIT-003 | Configure a dashboard block | Edit mode is on and `Latest announcements` block is visible | 1. Open the block menu<br>2. Select configure<br>3. Change a non-destructive block setting<br>4. Save and refresh Dashboard | Updated block configuration is preserved for `teacher1` and does not change the student's dashboard | Medium |
| MT-DEDIT-004 | Reset dashboard to default | Edit mode is on and layout was customized | 1. Click "Reset page to default" | Dashboard returns to default block arrangement | High |
| MT-DEDIT-010 | Move a block via drag and drop | Edit mode is on and Dashboard contains at least two blocks | 1. Click and hold the Move icon for a block<br>2. Drag the block to a new position in the layout<br>3. Release to drop the block | The block is moved to the new position and the layout persists for the teacher | High |
| MT-DEDIT-011 | Move a block via the block options menu | Edit mode is on and Dashboard contains at least two blocks | 1. Open the block menu for a block<br>2. Select the Move action | The block is moved to the selected position and the layout persists for the teacher | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-005 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect dashboard controls | "+ Add a block" is not rendered and no add-block URL is exposed from the Dashboard controls | High |
| MT-DEDIT-006 | Block menu unavailable outside edit mode | Edit mode is off | 1. Inspect existing dashboard blocks | Configure, move, and delete options are not rendered on dashboard blocks | High |
| MT-DEDIT-007 | Cancel add-block flow | Add-block page is open | 1. Click "Cancel" | No block is added and teacher returns to Dashboard | Medium |
| MT-DEDIT-012 | Add block blocked when block type is not selected | Edit mode is on and Add a block page is open | 1. Leave the Block Type dropdown empty<br>2. Click to submit or add | Submission is blocked by required-field validation and no block is added | High |
| MT-DEDIT-013 | Move handle is hidden when edit mode is off | Edit mode is off and Dashboard contains blocks | 1. Inspect existing blocks on the Dashboard | Move handles (drag icons) are absent and blocks cannot be dragged | High |
| MT-DEDIT-014 | Reset dashboard button hidden when edit mode is off | Edit mode is off | 1. Inspect Dashboard controls | "Reset page to default" button is absent | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-008 | Rapid edit-mode toggle | Dashboard is visible | 1. Toggle Edit mode on and off several times quickly | Final UI state matches the final toggle state | Medium |
| MT-DEDIT-009 | Delete all optional blocks | Edit mode is on and blocks exist | 1. Delete available optional blocks<br>2. Reload Dashboard | Layout persists without duplicate or ghost blocks | Medium |
| MT-DEDIT-015 | Toggle edit mode off closes Add block page | Add a block page is open in Edit mode | 1. Click the Edit mode toggle to turn it off | Add a block page closes, teacher is returned to the standard Dashboard, and no block is added | Medium |
| MT-DEDIT-016 | Reset to default immediately after adding a block | Edit mode is on and layout was customized | 1. Add a new block<br>2. Immediately click "Reset page to default" | Dashboard reverts to the default block arrangement and the newly added block is removed if it was not part of the default layout | Medium |
| MT-DEDIT-017 | Rapid Add block double-click | Edit mode is on | 1. Click "+ Add a block" rapidly twice | Add a block page opens only once; no duplicate modal or error state occurs | Low |
