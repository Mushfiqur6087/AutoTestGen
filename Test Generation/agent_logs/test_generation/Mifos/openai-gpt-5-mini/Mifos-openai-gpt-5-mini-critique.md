# Structural Model Critique — Mifos

Generated: 2026-07-04T17:13:41.268090Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST correctly models all interactive elements (Tenant, Username, Password, Remember Me, Language selector, Login button, Forgot Password link), required-field validation, enablement condition, and success/error behaviors; no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models the interactive elements described (Search Activity input and Dashboard button); passive items like the welcome card and system version info are appropriately omitted.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST matches the description: the Dashboard button and Search Activity input are present; chart and summary cards are passive displays (out of scope) and correctly omitted as interactive elements.

**Missing:** none

**Phantoms:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (search toggle, input with live search, grouped results, item navigation, and no-results message) and contains no critical omissions or structural errors.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

AST matches the description with one minor interactive element omitted (download action on import history); no structural errors or critical gaps found.

**Missing:**

- {'path': 'Bulk_Import_Page.components.Import_History_Table.Download_Action', 'severity': 'minor', 'reason': "Description lists an Import History table with a 'Download' column implying a per-row download action; the AST provides only a descriptive table entry and does not model the downloadable action."}

**Phantoms:** none

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements and actions described (groups table with row navigation, create/import buttons and forms, bulk import panels and history, detail-page actions, tabs, member links, meeting scheduling/recording, and collection-sheet generation); no critical items are missing.

**Missing:** none

**Phantoms:** none

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only a minor redundant component was added but no critical items are missing.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Collection_Sheet', 'severity': 'minor', 'reason': 'The description refers to a Collection Sheet feature (an action) accessible from the Calendar/Meeting tab, but does not define a standalone Collection_Sheet form component; the AST adds a separate Collection_Sheet component in addition to the Generate button under Calendar/Meeting.'}

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements and wizard steps described for Loan Products; no critical elements or structural errors found.

**Missing:** none

**Phantoms:** none

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements, wizards, steps, fields, and conditionals for Savings, Fixed Deposit, and Recurring Deposit product creation.

**Missing:** none

**Phantoms:** none

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements, wizard steps, required fields, repeating market-price rows, charges search, accounting radio with conditional GL mappings, and table actions described.

**Missing:** none

**Phantoms:** none

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (data table with clickable row, Create form with required fields, conditional Charge Time options, submit action, and detail view actions); only a minor non-essential metadata note is present.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Create_Charge_Form.fields.Charge_Time_Type.options_note', 'severity': 'minor', 'reason': 'This explanatory metadata string is not anchored in the description and is not an interactive element.'}

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described: the table with a clickable row action, the Create button and creation/edit forms (including required name, base/active checkboxes, and repeating Rate Periods with differential behavior), and the detail view with Edit.

**Missing:** none

**Phantoms:** none

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

The AST includes the expected tables, row actions, forms, required fields, repeating ranges, optional maximum-day semantics, and submit actions matching the description.

**Missing:** none

**Phantoms:** none

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

The AST captures the interactive elements, wizard steps, state-bound actions, and tabbed actions described; no critical elements or structural errors are missing.

**Missing:** none

**Phantoms:** none

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements, actions, state-bound behaviors, and conditionals described; no critical mismatches found.

**Missing:** none

**Phantoms:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The AST includes all expected interactive elements (application form fields and submit action, state-bound actions with required fields, and the three detail tabs) and contains no critical missing items or structural errors.

**Missing:** none

**Phantoms:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST invents passive/display-only Interest_Rate fields on the create forms that are not anchored in the description and must be removed or re-anchored; otherwise the structure matches the described interactive elements.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Fixed_Deposit_Create_Form.fields.Interest_Rate', 'severity': 'critical', 'reason': 'The description does not state that an Interest Rate field is shown on the FD creation form; this is a passive/display value derived from product/config and thus should not be modeled as an interactive field in the AST.'}
- {'path': 'components.Recurring_Deposit_Create_Form.fields.Interest_Rate', 'severity': 'critical', 'reason': 'The description does not state that an Interest Rate field is shown on the RD creation form; this is a passive/display value derived from product/config and thus should not be modeled as an interactive field in the AST.'}

**Fixes applied:**

- Remove components.Fixed_Deposit_Create_Form.fields.Interest_Rate from the AST (or convert it to an explicitly-described interactive element with a textual anchor if the spec intends it to be an input/action).
- Remove components.Recurring_Deposit_Create_Form.fields.Interest_Rate from the AST (or convert it to an explicitly-described interactive element with a textual anchor if the spec intends it to be an input/action).

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

The AST includes the hierarchical accounts table, the + Create GL Account action and form with required fields and uniqueness constraint, and the account detail Edit/Delete actions — matching the described interactive elements.

**Missing:** none

**Phantoms:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

AST accurately models the interactive elements from the description; only a small optional interactive item (filtering on the Closures table) was added without textual anchor.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Closing_Entries_Table.filterable_columns', 'severity': 'minor', 'reason': "The description only mentions the Closing Entries table's columns (Office, Closing Date, Created Date, Comments) but does not state that the table has filter controls; making those columns filterable is an extra interactive feature not anchored in the text."}

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements described (tables, create buttons, forms, required fields, constraints, and rule detail actions); no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described; only a couple of minor, unsurprising actions are present that have no explicit textual anchor.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Provisioning_Criteria_Table.row_actions.Edit', 'severity': 'minor', 'reason': "The description states the Criteria Name is a clickable link (to open the criteria) but does not explicitly name an 'Edit' row action; an Edit action is a reasonable inferred interaction but is not textually anchored."}
- {'path': 'components.Provisioning_Criteria_Form.fields.Definitions.actions.[1]', 'severity': 'minor', 'reason': "The AST includes a 'Remove Row' row_action for Definitions rows; the description mentions adding multiple rows but does not explicitly state a remove/delete action. Removal is a plausible inferred action but is not explicitly described."}

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

The AST supplies the interactive elements described (hierarchical offices table with a navigation row action, Create Office flow with required fields and submit, Office Detail with Edit and Edit form), with no critical omissions or structural errors.

**Missing:** none

**Phantoms:** none

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

AST includes the Create and Edit forms with required fields, the Create button, table row action to view details, and the Edit action — matches the described interactive elements.

**Missing:** none

**Phantoms:** none

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (tables, forms, actions) with no critical omissions or structural errors.

**Missing:** none

**Phantoms:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements and constraints; only two minor, unsurprising UI action names are present that were not verbatim in the description.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Users_Table.row_actions[0].action_name', 'severity': 'minor', 'reason': "The description specifies that the Username is a clickable link (no explicit action name). The AST includes a 'View' row action which is a reasonable inferred action but not explicitly named in the description."}
- {'path': 'components.Roles_Table.row_actions[0].action_name', 'severity': 'minor', 'reason': "The description states that after role creation a permissions page is displayed; it does not name a 'Manage Permissions' row action. Including a 'Manage Permissions' action is a plausible UI affordance but is not explicitly anchored in the text."}

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (tabs, clickable report rows, parameters form, Run Report action, output table with sorting/pagination, and export options); only small optional details are underspecified.

**Missing:**

- {'path': 'Report_Parameters_Form.fields.(Office,Branch,Currency,Loan_Product,Loan_Officer)', 'severity': 'minor', 'reason': 'The description names these parameter fields but does not specify input control types in the AST (only Date_Range and Fund have types); type details are optional/unspecified in the description.'}

**Phantoms (hallucinations):**

- {'path': 'Reports_Catalog_Tabs.tabs[].fields.Reports_List.bulk_actions', 'severity': 'minor', 'reason': 'bulk_actions is present (empty) in each Reports_List but the description does not mention bulk actions; this is a minor implied/extra element.'}

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements and constraints; only a minor unanchored bulk-action was added.

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Standing_Instructions_Table.bulk_actions[0]', 'severity': 'minor', 'reason': "The AST includes a 'Delete Selected' bulk action which is not mentioned in the description; bulk table columns and passive display fields are out of scope."}

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST covers Tax Components, Tax Groups, and Savings Product references but is missing the Charge definitions integration and includes minor unexpected row actions.

**Missing:**

- {'path': 'components.Charge_Definition_Form', 'severity': 'critical', 'reason': 'The description explicitly states that Tax Groups are referenced by Charge definitions; an interactive element (e.g., a Tax Group selector or equivalent control on the Charge definition form) is expected but is not present in the AST.'}
- {'path': 'components.Tax_Components_Table.row_actions.Name_Link', 'severity': 'minor', 'reason': 'The description specifies the Name column is a clickable link; the AST provides generic row actions (View/Edit) but does not explicitly model the Name-as-link action.'}

**Phantoms (hallucinations):**

- {'path': 'components.Tax_Components_Table.row_actions[0]', 'severity': 'minor', 'reason': "A 'View' row action is not mentioned in the description; the description only names a clickable Name link (no explicit 'View' action)."}
- {'path': 'components.Tax_Components_Table.row_actions[1]', 'severity': 'minor', 'reason': "An 'Edit' row action is not mentioned in the description; no Edit action was described for rows."}

**Fixes applied:**

- Add a new form component at components.Charge_Definition_Form with type 'form', appropriate preconditions (e.g., Logged in with Accounting/Admin privileges), and a field 'Tax_Group' of type 'tax_group_selector' with options_source 'Tax_Groups' so Charge definitions can reference Tax Groups: components.Charge_Definition_Form = { "type": "form", "preconditions": ["Logged in with Accounting/Admin privileges"], "fields": { "Tax_Group": { "type": "tax_group_selector", "options_source": "Tax_Groups" } }, "submit_actions": [ { "action_name": "Save" } ] }.
- Explicitly model the clickable Name link in the Tax Components table row actions: insert an action object into components.Tax_Components_Table.row_actions with action_name 'Name' (or 'Open' with a clear note that it represents the clickable Name link) and 'opens_component' pointing to the detail/view component, e.g. components.Tax_Components_Table.row_actions.unshift({ "action_name": "Name", "opens_component": "Tax_Component_Detail_View" }).

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

The AST captures all interactive elements described (forms, buttons, checkboxes, dropdowns, file uploads) with correct required flags and preconditions; no critical omissions or phantom elements were found.

**Missing:** none

**Phantoms:** none

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST largely matches the description but it adds a required 'Reason' constraint for Audit Trails Reject that has no textual anchor in the description (critical phantom).

**Missing:** none

**Phantoms (hallucinations):**

- {'path': 'components.Audit_Trails.row_actions[2].fields.Reason', 'severity': 'critical', 'reason': 'The description states Approve and Reject buttons appear when maker-checker is enabled but does not state that Reject must require a Reason; the AST adds a required constraint with no textual anchor.'}

**Fixes applied:**

- Remove the 'required': true constraint at components.Audit_Trails.row_actions[2].fields.Reason or change it to optional, unless the description is updated to explicitly state that Rejections must capture a required reason.
- If the product expects a rejection reason, update the description to include: 'Reject action requires entering a Reason (required) that is recorded with the rejection.' so the AST may keep required:true.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements (profile icon, dropdown, Profile Settings link, and Log Out button) and their behaviors described in the module.

**Missing:** none

**Phantoms:** none

---
