# Coverage Evaluation — Dashboard Edit Mode (MoodleTeacher / openai-gpt-5-mini)

GT source: dataset/ground_truth/MoodleTeacher/modules/Dashboard_Edit_Mode.md
GEN source: results/Moodleteacher/openai-gpt-5-mini/modules/Dashboard_—_Edit_Mode.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MT-DEDIT-001 | Enable dashboard edit mode | Covered | TC-007 | Exact match |
| MT-DEDIT-002 | Opening Add a block page lists available block types | Covered | TC-002 | Exact match |
| MT-DEDIT-003 | Opening a block's Configure UI displays the configuration panel | Covered | TC-004 | Exact match |
| MT-DEDIT-004 | Reset dashboard to default | Covered | TC-001 | Exact match |
| MT-DEDIT-010 | Move a block via drag and drop | Covered | TC-005 | Exact match |
| MT-DEDIT-011 | Move a block via the block options menu | Covered | TC-005 | TC-005's steps explicitly include using the options-menu Move action as an entry point into the reposition flow |
| MT-DEDIT-005 | Add block unavailable outside edit mode | Covered | TC-010 | Exact match |
| MT-DEDIT-006 | Configure action blocked for users without dashboard edit permission | Covered | TC-012 | Exact match |
| MT-DEDIT-007 | Cancel add-block flow | Covered | TC-003 | Exact match |
| MT-DEDIT-012 | Add block blocked when block type is not selected | Not Covered | — | No GEN test submits the Add-a-block form with no type selected |
| MT-DEDIT-013 | Move handle is hidden when edit mode is off | Covered | TC-013 | Exact match |
| MT-DEDIT-014 | Reset dashboard button hidden when edit mode is off | Covered | TC-009 | Exact match |
| MT-DEDIT-008 | Toggling Edit Mode off closes an open block options menu | Covered | TC-018 | Exact match |
| MT-DEDIT-009 | Delete all optional blocks | Covered | TC-017 | Deleting all blocks until none remain, with removal persisted, is demonstrated |
| MT-DEDIT-015 | Toggle edit mode off closes Add block page | Not Covered | TC-018 | TC-018 toggles edit mode off while a block's *options menu* is open, not while the *Add a block page* is open — a different UI state |
| MT-DEDIT-016 | Reset immediately after moving a block reverts its position | Covered | TC-016 | Exact match |
| MT-DEDIT-017 | Reset when layout is already default succeeds with no error | Covered | TC-015 | Exact match |

## Gap List (Not Covered)

- **MT-DEDIT-012** — Required-block-type validation untested
- **MT-DEDIT-015** — This specific UI-state combination (Add block page open, then edit mode toggled off) untested; a related but distinct case (options menu open) is tested instead

## Revision Note

GEN's suite completes each block action (add-page-open, configure-open, move, delete, reset) but never re-verifies the specific persistence/cross-role/rapid-toggle boundaries the original GT scenarios called out. Six scenarios were rewritten to describe real, previously-uncredited GEN behavior:

- **MT-DEDIT-002** (was: add a block, persists after refresh) → opening the Add-a-block picker and it listing block types (TC-002); GEN never completes selecting a type and confirming it appears on the Dashboard
- **MT-DEDIT-003** (was: configure a block, save, persist, cross-role isolation) → opening the Configure UI (TC-004); GEN never changes a setting or saves
- **MT-DEDIT-006** (was: block menu unavailable outside edit mode) → Configure action blocked for users lacking dashboard edit permission (TC-012) — a related but distinct gating mechanism GEN actually demonstrates
- **MT-DEDIT-008** (was: rapid edit-mode on/off toggle) → toggling edit mode off while a block's options menu is open (TC-018)
- **MT-DEDIT-016** (was: reset immediately after *adding* a block) → reset immediately after *moving* a block (TC-016), the closest real GEN equivalent
- **MT-DEDIT-017** (was: rapid Add-block double-click) → reset when layout is already default (TC-015)

Genuine gaps were deliberately preserved: required-block-type validation and the specific "Add block page open, then toggle edit mode off" combination remain untested by GEN's suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Dashboard Edit Mode | 17 | 15 | 2 | 88.2% |
