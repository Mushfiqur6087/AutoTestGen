# Structural Model Critique — Moodleteacher

Generated: 2026-07-04T15:16:12.927275Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST matches the description: all interactive elements, submit behavior, error handling, and preconditions are present and no structural errors detected.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements described (Timeline dropdowns and search; Calendar dropdown, navigation buttons, New Event button, and links) and has no structural errors or unexpected phantoms.

**Missing:** none

**Phantoms:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements described (Reset button, +Add a block button linking to the Add page with block options and Cancel link, per-block move icon and three-dot menu with Configure/Move/Delete) and models the Edit-mode visibility precondition correctly.

**Missing:** none

**Phantoms:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only a minor structural naming omission (the per-card three-dot menu) is not explicitly modeled but its actions are present.

**Missing:**

- {'path': 'components.Courses_Grid.item_fields.Three_Dot_Menu', 'severity': 'minor', 'reason': "The description explicitly names a three-dot menu on each course card containing the actions 'Star this course' and 'Remove from view'. The AST includes the actions under components.Courses_Grid.item_actions but does not model a named menu container for them."}

**Phantoms:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

The AST includes the tab bar, course index sidebar, repeating course sections with collapse toggles, 'Collapse all' action, and activity/resource links as described; no critical elements are missing and there are no structural errors.

**Missing:** none

**Phantoms:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements, menus, bulk actions, modal controls, tile favourites, and conditionals described; no critical or structural issues found.

**Missing:** none

**Phantoms:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

The AST includes all described interactive fields, panels, conditionals, and submit actions with matching preconditions and inline validation.

**Missing:** none

**Phantoms:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive fields, panels, conditionals, and submit actions described for the Course Settings form.

**Missing:** none

**Phantoms:** none

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

AST includes all interactive elements described (scope dropdown, enrol button/dialog, filter form and controls, alphabetical filters, table with selectable rows and row actions, and bulk actions); no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The AST correctly includes the interactive Grade button (with precondition and on_success) and the tab bar, and appropriately omits passive display-only metadata and read-only metrics.

**Missing:** none

**Phantoms:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (search/filters, quick-grading toggle, row action, inline editable grade with conditional enabling, and interactive preview/file/comment links); no critical omissions or phantoms found.

**Missing:** none

**Phantoms:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

The AST includes all required interactive elements and constraints from the description; only minor, expected inferred properties are present.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.User_Filters.fields.Edit_Mode_Toggle', 'severity': 'minor', 'reason': "The description refers to 'Edit mode is enabled' but does not explicitly name or place an 'Edit mode' control; the toggle is a reasonable implied UI control."}
- {'path': 'components.Gradebook_Table.searchable', 'severity': 'minor', 'reason': "The AST marks the table as 'searchable', which is an inferred property (the description mentions user search controls above the table but does not explicitly set a table-level 'searchable' flag)."}

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements described (Message button, Edit profile link, data retention link, course links, miscellaneous and report links), contains no structural errors, and omits passive display-only fields as expected.

**Missing:** none

**Phantoms:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements, required flags, collapsible sections, upload support, tag input, site-defined custom fields, and submit/cancel actions as described; no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models the single interactive Log out button with its precondition, success consequence, and locations; no missing or phantom elements detected.

**Missing:** none

**Phantoms:** none

---
