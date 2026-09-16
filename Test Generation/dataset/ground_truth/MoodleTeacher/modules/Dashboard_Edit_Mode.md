# Moodle Teacher Test Cases — Ground Truth

Source: dataset/ground_truth/MoodleTeacher/MoodleTeacher.md

## Dashboard Edit Mode

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-001 | Enable dashboard edit mode | Teacher is on Dashboard | 1. Toggle Edit mode on | Reset button, Add a block button, block move icons, and block menus are visible | High |
| MT-DEDIT-002 | Opening Add a block page lists available block types | Edit mode is on | 1. Click "+ Add a block" | The Add a block page opens and lists the available block types, including `Latest announcements` | High |
| MT-DEDIT-003 | Opening a block's Configure UI displays the configuration panel | Edit mode is on and an existing block is visible | 1. Open the block's options menu<br>2. Click "Configure" | The block configuration UI is displayed for the block (a configuration panel or modal with controls to edit the block is visible) | Medium |
| MT-DEDIT-004 | Reset dashboard to default | Edit mode is on and layout was customized | 1. Click "Reset page to default" | Dashboard returns to default block arrangement | High |
| MT-DEDIT-010 | Move a block via drag and drop | Edit mode is on and Dashboard contains at least two blocks | 1. Click and hold the Move icon for a block<br>2. Drag the block to a new position in the layout<br>3. Release to drop the block | The block is moved to the new position and the layout persists for the teacher | High |
| MT-DEDIT-011 | Move a block via the block options menu | Edit mode is on and Dashboard contains at least two blocks | 1. Open the block menu for a block<br>2. Select the Move action | The block is moved to the selected position and the layout persists for the teacher | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-005 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect dashboard controls | "+ Add a block" is not rendered and no add-block URL is exposed from the Dashboard controls | High |
| MT-DEDIT-006 | Configure action blocked for users without dashboard edit permission | Edit mode is on but the user lacks dashboard edit permission | 1. Open the options menu for an existing block<br>2. Attempt to click "Configure" | "Configure" is not present or not actionable for this user; clicking does not open the block configuration UI and the block remains unchanged | High |
| MT-DEDIT-007 | Cancel add-block flow | Add-block page is open | 1. Click "Cancel" | No block is added and teacher returns to Dashboard | Medium |
| MT-DEDIT-012 | Add block blocked when block type is not selected | Edit mode is on and Add a block page is open | 1. Leave the Block Type dropdown empty<br>2. Click to submit or add | Submission is blocked by required-field validation and no block is added | High |
| MT-DEDIT-013 | Move handle is hidden when edit mode is off | Edit mode is off and Dashboard contains blocks | 1. Inspect existing blocks on the Dashboard | Move handles (drag icons) are absent and blocks cannot be dragged | High |
| MT-DEDIT-014 | Reset dashboard button hidden when edit mode is off | Edit mode is off | 1. Inspect Dashboard controls | "Reset page to default" button is absent | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-008 | Toggling Edit Mode off closes an open block options menu | Edit mode is on and a block's options menu is open | 1. Open the options menu for a block<br>2. Toggle Edit Mode off while the menu is open | The options menu and move handles are no longer visible and the menu closes immediately; the Dashboard returns to view mode without error | Medium |
| MT-DEDIT-009 | Delete all optional blocks | Edit mode is on and blocks exist | 1. Delete available optional blocks<br>2. Reload Dashboard | Layout persists without duplicate or ghost blocks | Medium |
| MT-DEDIT-015 | Toggle edit mode off closes Add block page | Add a block page is open in Edit mode | 1. Click the Edit mode toggle to turn it off | Add a block page closes, teacher is returned to the standard Dashboard, and no block is added | Medium |
| MT-DEDIT-016 | Reset immediately after moving a block reverts its position | Edit mode is on and Dashboard contains at least one block in a known position | 1. Use the move handle to drag a block to a different position<br>2. Immediately click "Reset page to default" | Dashboard visibly reverts to the default layout; the moved block returns to its original default position with no error shown | Medium |
| MT-DEDIT-017 | Reset when layout is already default succeeds with no error | Edit mode is on and the Dashboard layout already matches the system default | 1. Click "Reset page to default" | Reset succeeds: the Dashboard remains in the default layout with no visible change and no error is shown; Edit Mode remains active | Low |
