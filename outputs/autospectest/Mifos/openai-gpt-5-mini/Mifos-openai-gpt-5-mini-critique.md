# Semantic Critique — Mifos

Generated: 2026-05-21T14:25:39.131257Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST includes all required interactive elements and behaviors; only a minor detail (Username input type unspecified) is missing.

**Missing:**

- Login_Form.fields.Username.type

**Phantoms:** none

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

AST accurately includes the search input and Dashboard button and matches the described precondition; no missing or extraneous interactive elements found.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The AST includes the Home page 'Dashboard' button and the 'Search Activity' search field on the Dashboard page, with no extraneous interactive elements.

**Missing:** none

**Phantoms:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements: search icon button, search input (visible on click), live search across Clients/Groups/Loans/Savings, grouped results with entity name/identifier/status, selection navigation, and no-results message.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately and completely represents the interactive elements, steps, actions, constraints, and tabs described.

**Missing:** none

**Phantoms:** none

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST is mostly complete but missing interactive account and notes lists in Group Detail tabs and includes one inferred field not present in the description.

**Missing:**

- Group_Detail_Page.components.Detail_Tabs.tabs[1].components.Loan_Accounts_Table (data_table listing group loans and GLIM accounts with links and row actions)
- Group_Detail_Page.components.Detail_Tabs.tabs[2].components.Savings_Accounts_Table (data_table listing group savings and GSIM accounts with links and row actions)
- Group_Detail_Page.components.Detail_Tabs.tabs[3].components.Notes_List and Group_Detail_Page.components.Detail_Tabs.tabs[3].components.Add_Note_Form (interactive notes list and add-note form with text input and submit)

**Phantoms (hallucinations):**

- Create_Group_Form.fields.Associated_Clients_List (display_list not explicitly described)

**Fixes applied:**

- Add Loan accounts table: create Group_Detail_Page.components.Detail_Tabs.tabs[1].components.Loan_Accounts_Table as a data_table with columns such as Account Number (link), Product, Type (e.g., GLIM flag), Status, and row_actions for opening the loan — include interactive links to loan detail pages.
- Add Savings accounts table: create Group_Detail_Page.components.Detail_Tabs.tabs[2].components.Savings_Accounts_Table as a data_table with columns such as Account Number (link), Product, Type (e.g., GSIM flag), Status, and row_actions for opening the savings account.
- Add Notes UI: create Group_Detail_Page.components.Detail_Tabs.tabs[3].components.Notes_List as a data_table or list of notes (date, author, text) and Group_Detail_Page.components.Detail_Tabs.tabs[3].components.Add_Note_Form with a Note_Text field (textarea) and a Submit action that saves a note.
- Remove the inferred Associated_Clients_List: delete Create_Group_Form.fields.Associated_Clients_List unless the description is updated to explicitly require a separate persisted display list; otherwise keep only the described Add_Clients_Search search-and-add interface (Create_Group_Form.fields.Add_Clients_Search).

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (centers table, create/import flows, create form fields, bulk import template/upload, detail actions, tabs, and collection sheet) with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the described UI (filter bar, table with row link, 6-step wizard with specified fields, accounting conditional GL mappings, and detail view with Edit); only minor inferred items present.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Loan_Product_Wizard.submit_actions[0] (Create button text not explicitly named in description)
- Create_Loan_Product_Wizard.submit_actions[0].on_success (success action text inferred rather than specified)

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST largely matches the description but contains multiple inferred elements (phantoms) that were not explicitly specified; please remove or adjust those before reuse.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Savings_Product_Wizard.steps[5].fields.Charge_Search_Results.row_actions[0] (Add_Charge button not in description)
- Create_Savings_Product_Wizard.steps[5].fields.Selected_Charges.item_fields.Amount (Amount field for selected charge not specified in description)
- Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Charge_Search_Results.row_actions[0] (Add_Charge button not in description)
- Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Selected_Charges.item_fields.Amount (Amount field for selected charge not specified in description)
- Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Interest_Rate_Chart.min (min property inferred, not in description)
- Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Interest_Rate_Chart.item_fields.Amount_Range_Slabs.min (min property inferred, not in description)
- Create_Recurring_Deposit_Product_Wizard.steps[5].fields.Charge_Search_Results.row_actions[0] (Add_Charge button not in description)
- Create_Recurring_Deposit_Product_Wizard.steps[5].fields.Selected_Charges.item_fields.Amount (Amount field for selected charge not specified in description)

**Fixes applied:**

- Remove the explicit row action objects named 'Add_Charge' from Charge_Search_Results.row_actions in all three wizards; JSON paths to change: Create_Savings_Product_Wizard.steps[5].fields.Charge_Search_Results.row_actions, Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Charge_Search_Results.row_actions, Create_Recurring_Deposit_Product_Wizard.steps[5].fields.Charge_Search_Results.row_actions — either remove the row_actions array or leave it empty, because the description only states a generic search-and-add interface without naming the action.
- Remove the inferred 'Amount' field from Selected_Charges.item_fields in all three wizards since the description did not specify an Amount field for selected charges: paths to change: Create_Savings_Product_Wizard.steps[5].fields.Selected_Charges.item_fields, Create_Fixed_Deposit_Product_Wizard.steps[8].fields.Selected_Charges.item_fields (note step index for Fixed Deposit Charges is 8 in the AST), Create_Recurring_Deposit_Product_Wizard.steps[5].fields.Selected_Charges.item_fields — delete the 'Amount' entry or confirm the description explicitly if amount should exist.
- Remove the inferred 'min' properties on the Interest_Rate_Chart repeating groups in Fixed Deposit wizard because the description only said 'optional Amount Range slabs' (no min constraint): paths to change: Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Interest_Rate_Chart.min and Create_Fixed_Deposit_Product_Wizard.steps[7].fields.Interest_Rate_Chart.item_fields.Amount_Range_Slabs.min — delete these 'min' properties.
- If you intend to keep any inferred action/field names (e.g., Add_Charge or Selected_Charges.Amount), update the raw description to explicitly include those names and behaviors so they are no longer treated as phantoms; otherwise remove them per the paths above.

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

AST is mostly complete with one minor missing field (Capital Value) and two small phantoms (inline table row actions); acceptable to use.

**Missing:**

- Create_Share_Product_Wizard.steps[3].fields.Capital_Value

**Phantoms (hallucinations):**

- Share_Products_Table.row_actions[0] (Edit button not specified in description as a table row action)
- Share_Products_Table.row_actions[1] (Delete button not specified in description as a table row action)

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (table with clickable Name, Create flow with required fields and conditional Charge Time Type options, submit action, and detail view with Edit/Delete).

**Missing:** none

**Phantoms:** none

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (table with link, create button and form, repeating rate periods, detail view and edit) with only minor non-critical extras.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Floating_Rate_Form.submit_actions[1] (Cancel button not mentioned in description)
- Edit_Floating_Rate_Form.submit_actions[1] (Cancel button not mentioned in description)

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST mostly covers pages, tables, and forms, but it includes several elements not explicitly specified in the description (named buttons/row actions/submit labels) and omits an explicit UI element for linking buckets to loan products which the description calls out.

**Missing:**

- Create_Delinquency_Bucket_Form.fields.Linked_Loan_Products (UI for linking buckets to Loan Products — description states buckets are linked to loan products but AST does not provide a field/interface for this)

**Phantoms (hallucinations):**

- Delinquency_Ranges_Page.page_actions[0] (Create Delinquency Range button name and presence not explicitly stated in description)
- Delinquency_Buckets_Page.page_actions[0] (Create Delinquency Bucket button name and presence not explicitly stated in description)
- Delinquency_Ranges_Page.row_actions[0] (action_name 'Open Range' label invented; description only states Classification is a clickable link)
- Delinquency_Buckets_Page.row_actions[0] (action_name 'Open Bucket' label invented; description only states Bucket Name is a clickable link)
- Create_Delinquency_Range_Form.submit_actions[0] (submit button label 'Create' and on_success text not specified in description)
- Create_Delinquency_Bucket_Form.submit_actions[0] (submit button label 'Create' and detailed on_success text not specified in description)

**Fixes applied:**

- Add explicit Loan Product linkage UI: Create_Delinquency_Bucket_Form.fields.Linked_Loan_Products — add either a multi-select or association field (type: multi_select_reference) allowing selection of one or more Loan Products so buckets can be linked to loan products.
- If buttons/row action labels are not intended to be prescriptive, remove or replace explicit labels: change Delinquency_Ranges_Page.page_actions[0] and Delinquency_Buckets_Page.page_actions[0] to a generic 'open_form' action without a hard-coded element_name, or annotate them as 'implied' rather than named; update JSON paths: components.Delinquency_Ranges_Page.page_actions[0] and components.Delinquency_Buckets_Page.page_actions[0].
- Replace explicit row action names with inferred behavior: components.Delinquency_Ranges_Page.row_actions[0] and components.Delinquency_Buckets_Page.row_actions[0] should reference the clickable column (Classification / Bucket Name) without inventing an 'action_name' label, or change action_name to 'open_linked_detail' to avoid inventing wording.
- Remove or neutralize unstated submit labels and success messages if they are not specified: components.Create_Delinquency_Range_Form.submit_actions[0] and components.Create_Delinquency_Bucket_Form.submit_actions[0] should be simplified to indicate 'submit' action_type with optional generic on_success behavior, unless the description provides the label and success consequences to be included.

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements from the description; only one minor inferred component (Add_Charge_Form) was added.

**Missing:** none

**Phantoms (hallucinations):**

- Add_Charge_Form (inferred form component opened by Add Charge button — the description only named the Add Charge button, not the form)

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements (creation form fields, charges repeating group, submit action, state-bound actions with Deposit/Withdraw forms and constraints, and the tabbed Transactions table) and matches the description.

**Missing:** none

**Phantoms:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the form fields, submit behavior, state-bound actions, and the three detail tabs; only a minor inferred control (selection of savings account for redeem) is added but not critical.

**Missing:** none

**Phantoms (hallucinations):**

- components.Share_Account_Detail_Actions.states.Active.available_actions[1].fields.Savings_Account_for_Credit (dropdown for selecting savings account to credit on Redeem — description only states redemption is credited to the linked savings account, not that the user selects one)

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains several inferred/phantom items (named submit buttons, explicit state machines, extra fields/constraints) and is missing the fact that FD/RD creation is initiated from the Client Detail page.

**Missing:**

- Client_Detail.create_actions.Create_FD (button/link to open FD creation form from Client Detail page)
- Client_Detail.create_actions.Create_RD (button/link to open RD creation form from Client Detail page)

**Phantoms (hallucinations):**

- FD_Account_Creation_Form.submit_actions[0] (Create Fixed Deposit button not named in description)
- RD_Account_Creation_Form.submit_actions[0] (Create Recurring Deposit button not named in description)
- RD_Account_Creation_Form.fields.Deposit_Period_Unit (deposit period unit options were not specified for RD in the description)
- FD_Account_Detail_Actions.states (explicit state names and per-state preconditions were not specified — description only listed available action buttons)
- RD_Account_Detail_Actions.states (explicit state names and per-state preconditions were not specified — description only listed available action buttons)
- FD_Account_Detail_Actions.states.Active.available_actions[1].constraints[0] ("maturity date must be reached" constraint is an inferred rule not stated in the description)
- FD_Account_Creation_Form.fields.*.required (required flags for form fields are inferred but not specified in the description)
- RD_Account_Creation_Form.fields.*.required (required flags for form fields are inferred but not specified in the description)

**Fixes applied:**

- Add explicit creation actions on the Client Detail page: create a component at Client_Detail.create_actions with two actions: {"action_name":"Create Fixed Deposit","target":"FD_Account_Creation_Form"} and {"action_name":"Create Recurring Deposit","target":"RD_Account_Creation_Form"}.
- Remove the named submit_actions entries that were not in the description: delete FD_Account_Creation_Form.submit_actions[0] and RD_Account_Creation_Form.submit_actions[0]; if a submit action is required, leave a generic unlabeled submit placeholder (e.g., form.submit_action: true) rather than a named button.
- Remove the Deposit_Period_Unit field from RD_Account_Creation_Form.fields (RD description only specified Deposit Period and Deposit Frequency; do not add extra unit dropdown unless the description mentions it). Path: delete RD_Account_Creation_Form.fields.Deposit_Period_Unit.
- Replace the inferred state machines with simple action listings on the detail pages: delete FD_Account_Detail_Actions.states and RD_Account_Detail_Actions.states and instead provide FD_Account_Detail_Actions.available_actions: ["Approve","Activate","Premature Close","Close on Maturity"] and RD_Account_Detail_Actions.available_actions: ["Approve","Activate","Deposit","Premature Close","Close on Maturity"] (do not invent per-state preconditions or status names unless explicitly described).
- Remove inferred constraints that are not in the description: delete FD_Account_Detail_Actions.states.Active.available_actions[1].constraints[0] (the "maturity date must be reached" constraint) and any other inferred constraints not explicitly stated.
- Remove 'required' properties from form fields unless the description explicitly states they are required. Specifically, remove the 'required' keys under FD_Account_Creation_Form.fields.* and RD_Account_Creation_Form.fields.* so the regenerated AST only marks required when described.

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only minor inferred submit button labels are present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Create_GL_Account_Form.submit_actions[0] (Create button not named in description)
- components.Edit_GL_Account_Form.submit_actions[0] (Save button not named in description)

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is mostly complete but is missing the repeating-group 'Add Row' action and the running-total display fields (debit, credit, difference); it also adds a per-line 'Type' field that is not stated in the description.

**Missing:**

- components.Add_Journal_Entry_Form.fields.Entry_Lines.actions[0] (Add Row button to add additional entry lines)
- components.Add_Journal_Entry_Form.display_fields.Debit_Total (running total display for debit total)
- components.Add_Journal_Entry_Form.display_fields.Credit_Total (running total display for credit total)
- components.Add_Journal_Entry_Form.display_fields.Difference (running total display for debit/credit difference)

**Phantoms (hallucinations):**

- components.Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Type (per-line Debit/Credit Type was not specified in the description — only GL Account and Amount were described)

**Fixes applied:**

- Remove the phantom field: delete components.Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Type unless the functional spec is updated to explicitly require a per-line Debit/Credit selector.
- Add the missing 'Add Row' action for the repeating entry lines: add components.Add_Journal_Entry_Form.fields.Entry_Lines.actions[0] with { "element_name": "Add Row", "type": "button", "behavior": "adds another item to the repeating_group" }
- Expose running totals in the form UI: add components.Add_Journal_Entry_Form.display_fields with entries Debit_Total, Credit_Total, and Difference, each typed (number/currency) and updated live; e.g. add components.Add_Journal_Entry_Form.display_fields.Debit_Total { "type": "number" } (and similarly for Credit_Total and Difference).
- Ensure the equality validation remains and is tied to these running totals: keep components.Add_Journal_Entry_Form.constraints entry 'total debits must equal total credits (blocks submission)' and make it reference the new display fields.

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements described (tables, clickable rule name, create/edit/delete flows, forms with specified fields and constraints, and mapping uniqueness), with no missing or extraneous interactive items.

**Missing:** none

**Phantoms:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements: Criteria list and create flow with repeating Definitions rows and required fields, and Provisioning Entries list with create, review, and recreate actions.

**Missing:** none

**Phantoms:** none

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains reasonable structure but includes multiple invented UI element labels/actions that are not present in the description and should be removed or made explicit.

**Missing:** none

**Phantoms (hallucinations):**

- components.Offices_Table.row_actions[0] (action_name: 'View Details' — the description only states the Office Name is a clickable link; it does not name a 'View Details' action)
- components.Create_Office_Form.submit_actions[0] (element_name: 'Create' — the submit button label is not specified in the description)
- components.Edit_Office_Form.submit_actions[0] (element_name: 'Save' — the submit button label is not specified in the description)

**Fixes applied:**

- components.Offices_Table.row_actions[0]: Remove or neutralize the explicit action_name 'View Details' and instead represent the trigger as the Office Name link (e.g., replace action_name with a textual trigger field: "trigger": "Office Name link"), because the description does not name the action.
- components.Create_Office_Form.submit_actions[0]: Remove the explicit element_name 'Create' or set it to 'unspecified' (e.g., "element_name": "unspecified") so the AST does not invent a label not present in the description; keep the on_success behavior if needed.
- components.Edit_Office_Form.submit_actions[0]: Remove the explicit element_name 'Save' or set it to 'unspecified' (e.g., "element_name": "unspecified") so the AST does not invent a label not present in the description; keep the on_success behavior if needed.

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (employees table with Name link, + Create Employee button and form with required fields, Employee Detail page with Edit action); only minor phantom is that the Edit form's fields are detailed though the description only mentioned an Edit option.

**Missing:** none

**Phantoms (hallucinations):**

- components.Edit_Employee_Form.fields (detailed editable fields are specified though description only states there is an Edit option on the Staff Detail page)

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements described (tables, buttons, forms, required fields, actions, and transaction list) with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

The AST accurately includes all interactive elements (tables, buttons, forms, fields, validation constraints, and permissions matrix) described in the specification.

**Missing:** none

**Phantoms:** none

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the pages, tabs, report list, parameter form fields, Run Report action, result table with sorting/pagination, export options, and common reports; only minor inferred items identified.

**Missing:** none

**Phantoms (hallucinations):**

- Report_Parameters_Form.fields.Output_Format.required (required flag not specified in description)
- Report_Parameters_Form.submit_actions[0].on_success (contains explicit conditional 'when Output_Format == On screen...' which is an inferred behavior rather than verbatim in the description)

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements; only minor extras (a Cancel action and an explicit state_bound_action_bar component) are present but non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Standing_Instruction_Form.submit_actions[1] (Cancel button not mentioned in the description)
- Standing_Instruction_Actions (explicit state_bound_action_bar component not named in the description; actions were described on the listing)

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (tables, create buttons, forms, fields, repeating group, and product/charge settings); only minor inferred submit buttons are present.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Tax_Component_Form.submit_actions[0] (Save button not explicitly named in description)
- Create_Tax_Group_Form.submit_actions[0] (Save button not explicitly named in description)

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive pages and forms with only a minor omission (currency activation control).

**Missing:**

- Currencies_Page.active_selection_control (missing row-level control to select/activate currencies, e.g., checkbox or toggle per currency)

**Phantoms:** none

---

## System Administration

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (scheduler jobs toggles and CRON editing, global scheduler toggle, global config flags, code list management, data table create/edit form with repeating column definitions, and audit trail filters/actions) with no critical omissions or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (profile icon button, dropdown with Profile Settings and Log Out, and the post-logout navigation guard) and their behaviors.

**Missing:** none

**Phantoms:** none

---
