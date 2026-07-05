# Workflow Critique — Moodlestudent

Generated: 2026-07-04T16:43:47.254937Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and matches the AST: all form submit actions and visible action buttons have corresponding workflows, with no structural errors or phantoms.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the module's actionable controls except for one minor missing filter action (All_Courses dropdown); no structural errors or phantoms found.

**Missing workflows:**

- {'path': 'Calendar_Block.fields.All_Courses (change course filter)', 'severity': 'minor', 'reason': 'The AST defines an All_Courses dropdown used to filter calendar events by course, but there is no workflow covering changing that dropdown/filter.'}

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover each actionable terminal defined in the AST (card link 'Open Course' and the two card_actions), and there are no structural errors or phantom workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actions present in the AST (tab navigation, collapse all, section toggle/open, and activity open); no missing or phantom workflows or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants

**Verdict:** yes  
**Forced ship:** no  

All form submit_actions and data_table row_actions from the AST are represented by workflows; no missing or phantom workflows or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Grades

**Verdict:** yes  
**Forced ship:** no  

The single workflow is acceptable; it is a minor phantom (viewing the report is implied by the page) but there are no critical or structural issues and no required missing workflows.

**Missing workflows:** none

**Phantom workflows:**

- {'path': 'WF-001 terminal_action=View Grades', 'severity': 'minor', 'reason': "The terminal_action 'View Grades' does not appear in any AST node's row_actions, bulk_actions, or submit_actions; it is only implied by the page description ('view their own grades'), so it's a minor phantom rather than a critical mismatch."}

---

## Assignment

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action and all state-bound actions; only one minor form-condition combination variant is not explicitly represented.

**Missing workflows:**

- {'path': 'Assignment_Submission_Form: Submit when Online_Text is visible AND File_Upload is visible', 'severity': 'minor', 'reason': 'The form has visible_when conditions for Online_Text and File_Upload; the AST requires one workflow per unique condition combination × submit action. Workflows exist for Online_Text-only, File_Upload-only, and a base submit, but there is no explicit workflow covering the combination where both fields are visible.'}

**Phantom workflows:** none

---

## Activities

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all row_actions defined in the data tables and the expandable section interactions described in the AST and description; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers all form submit actions and all actionable items in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the Log out button action defined in the AST, matches its on_success text, and there are no other form/state/table actions requiring workflows.

**Missing workflows:** none

**Phantom workflows:** none

---
