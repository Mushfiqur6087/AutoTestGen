# Workflow Critique — Moodleteacher

Generated: 2026-07-04T16:52:18.727894Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all required submit and action/button actions in the AST (Log in, Access as a guest, Cookies notice); no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actionable AST items (buttons and links) and there are no missing or phantom critical workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all submit_actions and row_actions in the AST, conditional branches reference the existing Edit_Mode field, and there are no missing or phantom workflows or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

The workflows cover the card link and both card row actions declared in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all actionable elements defined in the AST (Collapse_All, Toggle_Section, Activity_Name) with correct conditional handling and on_success behavior.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The workflow list fully and correctly covers all actionable items declared in the AST (section/activity menus, bulk actions, add buttons, and the Activity Chooser), with no missing or phantom workflows and no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Creation

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list omits required submit-action workflows for some conditional visibility combinations (Save and display is missing for File-only and Group-only conditions).

**Missing workflows:**

- {'path': "Assignment_Creation_Form: visible_when combination File_Submissions == true × submit_action 'Save and display'", 'severity': 'critical', 'reason': "The form has fields visible_when File_Submissions == true; the submit_action 'Save and display' must have a workflow covering the condition where File_Submissions is true but Group_Submissions is not."}
- {'path': "Assignment_Creation_Form: visible_when combination Group_Submissions == true × submit_action 'Save and display'", 'severity': 'critical', 'reason': "The form has fields visible_when Group_Submissions == true; the submit_action 'Save and display' must have a workflow covering the condition where Group_Submissions is true but File_Submissions is not."}

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Assignment_Creation_Form with conditional_branch 'File_Submissions == true && Group_Submissions == false' (or 'File_Submissions == true' if mutually exclusive branches aren't modeled) and terminal_action 'Save and display' with the matching on_success 'creates the assignment and opens the new assignment page'.
- Add a workflow for Assignment_Creation_Form with conditional_branch 'Group_Submissions == true && File_Submissions == false' (or 'Group_Submissions == true') and terminal_action 'Save and display' with the matching on_success 'creates the assignment and opens the new assignment page'.

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form's submit actions and the visible_when condition for Course_Format; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all required form submit actions, data table row and bulk actions, and dialog submit actions in the AST; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The single workflow matches the action_bar's 'Grade' action and there are no forms, state-bound actions, or data tables requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all row actions and the Quick Grading toggle referenced in the AST and description; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the data table's submit action and the listed cell/column actions; no critical gaps or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

All actionable AST nodes have matching workflows and there are no structural errors or phantoms.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

Workflows correctly cover all form submit actions (Update profile, Cancel) with matching on_success values; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the single Log out action from the top navigation menu and matches the AST and module context; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---
