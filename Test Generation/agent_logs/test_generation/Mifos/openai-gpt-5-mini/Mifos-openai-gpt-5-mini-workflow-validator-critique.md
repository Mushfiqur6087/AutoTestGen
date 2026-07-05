# Workflow Critique — Mifos

Generated: 2026-07-04T17:13:41.304379Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action and the Forgot Password link as required by the AST; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

The provided workflows correctly cover the AST's interactive elements (Search_Activity submit and Dashboard button) with no missing or phantom workflows and no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the Dashboard link and the Search Activity field present in the AST and description; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Global Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows contain 2 critical phantom terminal_actions (Search_Input) and structural errors in conditional_branch usage for result-selection workflows; regenerate to correct terminal_action names and remove/replace invalid conditional_branch expressions.

**Missing workflows:** none

**Phantom workflows:**

- {'path': 'WF-002 terminal_action=Search_Input', 'severity': 'critical', 'reason': "Terminal_action 'Search_Input' is a field name, not an action listed in the AST; the AST defines an on_input handler 'perform_search_and_update_results_dropdown' but no action named 'Search_Input', so this workflow's terminal_action cannot be traced to the AST or description."}
- {'path': 'WF-003 terminal_action=Search_Input', 'severity': 'critical', 'reason': "Terminal_action 'Search_Input' is not an action or submit_action in the AST; the AST provides an on_input handler and a no_results_message but no action named 'Search_Input', so this workflow is a phantom."}

**Fixes applied:**

- WF-002: Replace terminal_action 'Search_Input' with a terminal_action that matches the AST action name — use 'perform_search_and_update_results_dropdown' (the field's on_input handler) or add an explicit action 'Perform Search' to the AST and use that; do not use the field name as terminal_action.
- WF-003: Replace terminal_action 'Search_Input' with 'perform_search_and_update_results_dropdown' (matching AST on_input) and, if you need a separate workflow for the empty-results case, add a conditional expression that references a real AST-exposed field (e.g., add a boolean/results_count visible field to the AST) such as 'Results.count == 0'; otherwise remove the conditional_branch and keep on_success = 'No results found'.
- WF-004, WF-005, WF-006, WF-007: Remove the free-text conditional_branch values (e.g., 'Selected result from Clients group') or replace them with conditional expressions that reference real AST fields/states; if the AST will not expose such fields/states, set conditional_branch to null because the item_action 'Open Detail' with params (Entity_Type, Entity_Id) already distinguishes which entity was selected.

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

The provided workflow list fully and correctly covers the AST-defined forms, wizard submit, data table row/page actions, and all state-bound actions with appropriate conditional branches and concrete on_success outcomes.

**Missing workflows:** none

**Phantom workflows:** none

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions, data-table row actions, buttons, and action-bar items present in the AST; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all required form submits, data-table row actions, and action-bar actions; two minor UI-open actions on the Centers page have no explicit terminal workflows but are non-critical.

**Missing workflows:**

- {'path': 'Centers_Page.action=Create Center', 'severity': 'minor', 'reason': "The AST defines a 'Create Center' action that opens Create_Center_Form, but there is no workflow whose terminal_action is 'Create Center' (only the Submit of the form is present)."}
- {'path': 'Centers_Page.action=Import Center', 'severity': 'minor', 'reason': "The AST defines an 'Import Center' action on the Centers page that would open the Bulk_Import_Centers form, but there is no workflow with terminal_action 'Import Center' (only the Download Template and Import submit actions within the import form are represented)."}

**Phantom workflows:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers all required submit actions (Save, Cancel) including conditional variations for Accounting_Method, and includes the data-table row action; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the data table row action and each wizard Submit action including workflows for each distinct visible_when condition present in the AST; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the Create wizard (both Accounting_Method branches), all data-table row actions (Open/Edit/Delete), and detail action bar actions; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the data table view action, create action, form submit, edit, and delete actions and match the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

All required workflows for form submits and data-table actions are present, no phantom or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions and data-table row actions in the AST; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the wizard submit action, every state×action in the state_bound_action_bar, and the data-table row action; there are no missing critical workflows, phantoms, or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit and every state-bound action in the AST with correct conditional branches and non-generic on_success values; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all form submit actions and state-bound actions in the AST with matching conditional branches and on_success behavior; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all form submit_actions and all action_bar available_actions present in the AST; no critical or structural issues detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all required form submit actions, the data-table row view action, and the detail actions (Edit/Save and Delete); no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

All required workflows for the forms and table actions in the AST are present and correctly mapped; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all form submit actions, data-table row actions, and available action-bar actions defined in the AST; no critical or structural gaps found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all form submit actions, data table actions, and row actions present in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers all form submits, data-table row actions, and action-bar actions in the AST with matching on_success outcomes; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the form submit actions (Create Employee, Save) and the data table row action (View); no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit_actions and data table row actions present in the AST; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions and data-table row actions present in the AST; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: all data-table row actions (Open Parameters for each tab), the form submit action (Run Report), and the report output actions (View and Export to Excel/CSV/PDF) are represented with no missing or phantom workflows and no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions, table row/bulk/toolbar actions, and on_success texts match the AST—no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

Workflows fully cover all form submit actions (including conditional Save paths), data table row actions, and contain no phantoms or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all form submit actions and the Bulk Import download/upload interactions listed in the AST; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## System Administration

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit_actions and all data_table row/bulk actions defined in the AST; conditional branches match preconditions and no structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all actions in the AST (Open Profile Menu, Profile Settings, Log Out) and include the logout precondition and concrete on_success behaviors.

**Missing workflows:** none

**Phantom workflows:** none

---
