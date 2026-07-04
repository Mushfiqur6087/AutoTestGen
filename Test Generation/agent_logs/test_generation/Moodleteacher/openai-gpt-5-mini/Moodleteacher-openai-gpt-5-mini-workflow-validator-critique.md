# Workflow Critique — Moodleteacher

Generated: 2026-07-04T15:16:13.004569Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all required submit and action button paths; one minor non-critical UI link (disabled 'Lost password?') is not represented as a workflow.

**Missing workflows:**

- {'path': "components.Login_Form.fields.Lost_Password (link 'Lost password?')", 'severity': 'minor', 'reason': "The AST defines a 'Lost password?' link in the login form (disabled on this test site) but there is no workflow covering the user clicking this link; omission is non-critical since it does not affect form submission or state transitions."}

**Phantom workflows:** none

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows mostly match the AST, but several workflows use a conditional_branch that references a non-existent state/field (structural errors) and must be fixed.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- For WF-007 (Create a new calendar event): either remove the conditional_branch 'user_logged_in == true' (since actor is already 'Authenticated user'), or add a corresponding state key to the AST (e.g., a state_bound_action_bar state 'user_logged_in') and reference that exact state name in the workflow conditional_branch.
- For WF-008 (Open full calendar view): either remove the conditional_branch 'user_logged_in == true' (actor already 'Authenticated user'), or add a corresponding state key to the AST (e.g., 'user_logged_in') and update the workflow to use that state name.
- For WF-009 (Open calendar import/export management): either remove the conditional_branch 'user_logged_in == true' (actor already 'Authenticated user'), or add a corresponding state key to the AST (e.g., 'user_logged_in') and update the workflow to use that state name.

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all actions and conditional branches expressed in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actionable items defined in the AST (card click, course-name link, and both card item actions); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all actionable AST nodes (index link, section toggle, collapse-all, activity and resource links) and no structural errors or phantoms were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all AST actions (section/activity menus, quick rename, bulk actions, activity chooser Add per tile, and favorite toggle); no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers all form submit actions across the visible_when condition combinations (File_Submissions, Group_Submissions, Add_Restriction_Button_Clicked), with no missing or phantom workflows and no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the form's submit actions across the conditional combinations implied by Course_End_Date_Enable and Course_Format; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

Workflows comprehensively cover all submit_actions, data_table row and bulk actions, and dialog submissions in the AST; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The workflow list includes the Grade button path required by the AST; no required workflows are missing and there are no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actionable fields, table row actions, and the conditional quick-grading path; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the data_table submit action and the listed column and cell actions in the AST, with no missing critical paths or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

All actionable elements in the AST (links and buttons) have corresponding workflows; no missing or phantom workflows detected and no structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all required form submit actions (Update profile, Cancel); no missing or phantom critical paths detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the Logout action defined in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---
