# Workflow Critique — Phptravels

Generated: 2026-07-04T15:28:55.428010Z

## Home Page & Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows cover the four tab-specific Search submit paths but include conditional_branch expressions that reference a field not present in the AST (structural error), so regeneration/fix is required.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Add a field to the AST at components.Search_Widget.named 'selected_tab' (or 'active_tab') with possible values ["Hotels","Flights","Tours","Cars"] so the existing conditional_branch expressions are valid (path: components.Search_Widget.selected_tab).
- OR, if the AST intentionally models tabs without a selected_tab field, remove or update each workflow's conditional_branch to reference an actual AST-visible condition (for example replace conditional_branch with a visible_when/required_when entry in the AST for each tab form and then reference that condition), e.g. define visible_when conditions under each tab and change workflows to conditional_branch matching those visible_when expressions.

---

## User Registration

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the form's single submit action 'Register' and matches the AST's success/failure outcomes; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## User Login

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the form submit paths (with and without CAPTCHA), social logins, and the forgot-password link; no required or phantom workflows found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Forgot Password

**Verdict:** yes  
**Forced ship:** no  

All form submit actions in the AST have matching workflows, no state/data-table actions are present or missing, and there are no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Hotels Search & Listing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Several workflows use terminal_action names (filter field names and the sort field) that cannot be traced to the AST's canonical action lists, producing multiple minor phantom workflows — regenerate with terminal_action values that match AST action entries or add corresponding action entries to the AST.

**Missing workflows:** none

**Phantom workflows:**

- {'path': 'WF-002 terminal_action=Min_Price', 'severity': 'minor', 'reason': "Min_Price is a field name under Left_Sidebar_Filters.item_fields, but it is not present in the AST's submit_actions[], available_actions[], row_actions[], or bulk_actions[] arrays or in the description as an explicit action verb."}
- {'path': 'WF-003 terminal_action=Max_Price', 'severity': 'minor', 'reason': "Max_Price is a field name under Left_Sidebar_Filters.item_fields, but it is not present in the AST's canonical action arrays or described as an explicit action verb."}
- {'path': 'WF-004 terminal_action=Star_Rating', 'severity': 'minor', 'reason': "Star_Rating is a filter key in the AST but not listed in submit_actions[], available_actions[], row_actions[], or bulk_actions[], so the workflow's terminal_action cannot be traced to a canonical AST action entry."}
- {'path': 'WF-005 terminal_action=Facilities_Amenities', 'severity': 'minor', 'reason': "Facilities_Amenities is a filter key (on_change present) but not an action entry in the AST's submit/available/row/bulk action lists, so the workflow is not anchored to an AST action."}
- {'path': 'WF-006 terminal_action=Hotel_Type', 'severity': 'minor', 'reason': "Hotel_Type is a filter key in the AST but not present in the AST's canonical action lists, making this terminal_action untraceable per the phantom definition."}
- {'path': 'WF-007 terminal_action=Board_Basis', 'severity': 'minor', 'reason': 'Board_Basis is a filter key with on_change in the AST but is not present in submit_actions[], available_actions[], row_actions[], or bulk_actions[], so the workflow is a minor phantom.'}
- {'path': 'WF-010 terminal_action=Sort_By', 'severity': 'minor', 'reason': "Sort_By is the Sort_Control.field_name in the AST (with on_change), but it is not listed in the AST's submit/available/row/bulk action arrays nor explicitly named as an action verb in the description; the workflow's terminal_action is therefore unanchored."}

**Fixes applied:**

- Replace terminal_action values that refer to filter field names or control field names (Min_Price, Max_Price, Star_Rating, Facilities_Amenities, Hotel_Type, Board_Basis, Sort_By) with action names that appear in the AST action lists (e.g., add corresponding action entries to the AST such as submit_actions/available_actions/row_actions where appropriate) OR update the AST to include these field-change events in a recognized action array (e.g., add an actions/on_change list for Left_Sidebar_Filters and Sort_Control).
- Ensure terminal_action strings exactly match the AST action entries after the AST is updated (for example, change WF-002 terminal_action from 'Min_Price' to an AST action_name like 'Change Price Range (Min)' or add 'Min_Price' to an actions array in the AST).
- If field-level on_change events are intended to be valid terminal actions, add them to the AST under a canonical actions array (submit_actions, available_actions, row_actions, or bulk_actions) or make them explicit in the description so workflows can be unambiguously anchored.

---

## Hotel Details & Booking

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the room selection and the Book Now submit paths, matches AST actions and conditional visibility, and has no missing or phantom critical workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Flights Search & Listing

**Verdict:** yes  
**Forced ship:** no  

All required workflows for the form submit and data-table row actions are present; no missing or phantom workflows or structural errors were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Flight Booking

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's sole submit_action (Continue) with matching on_success and there are no missing, phantom, or structural issues.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tours Search & Listing

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the only submit_action declared in the AST (Search) and there are no other form submit_actions, state-bound actions, or table actions requiring workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tour Details & Booking

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers each form submit action in the AST (Book Now and Confirm Booking), with matching on_success behaviors; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Cars Search & Listing

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the form submit, all filter on_change actions, and each group's Book Now item_action with matching on_success handlers; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Car Booking

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the form's submit action (Confirm Booking) with the required condition Accept_Terms == true and matches the AST's on_success behavior; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Visa Services

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the form submit action for the Visa Application and the search/view action for visa requirements; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## User Dashboard

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all actions defined in the AST (data_table row_actions and panel/form actions), with no missing or phantom workflows and no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Booking Management

**Verdict:** yes  
**Forced ship:** no  

All submit actions in the AST have matching workflows and conditional branches align with defined fields; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payment Processing

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover every form submit_action (with one workflow per Payment_Method visibility variant), include the Retry Payment path and both confirmation-page download actions, and contain no phantom or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Currency & Language Selection

**Verdict:** yes  
**Forced ship:** no  

Workflows cover each on_change action in the AST (currency persistence for authenticated/unauthenticated; language apply and persistence for both user states) with matching conditional branches and concrete on_success outcomes.

**Missing workflows:** none

**Phantom workflows:** none

---

## Search & Filters

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly and completely covers all interactive fields and actions defined in the AST (no missing or phantom workflows and no structural errors).

**Missing workflows:** none

**Phantom workflows:** none

---

## Reviews & Ratings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Three workflows use conditional_branch expressions that reference a non-existent conditional field ('source_component') in the AST, which is a structural error and requires correction.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- For WF-003: either remove the conditional_branch (set to null) so the workflow is unconditional, OR add a visible_when entry to the Review_Submission_Form component in the AST that defines source_component (e.g., add visible_when: { "source_component": "Review_Submission_Form" }) so the condition references a declared field.
- For WF-004: either remove the conditional_branch (set to null) OR add a visible_when entry to the Review_Submission_Form component (or to the Dashboard_Submit_Review component if appropriate) so 'source_component' is a declared conditional field; e.g., add visible_when: { "source_component": "Dashboard_Submit_Review" }.
- For WF-005: either remove the conditional_branch (set to null) OR add a visible_when entry to the Review_Submission_Form component (or to the Email_Submit_Link component if appropriate) so 'source_component' is a declared conditional field; e.g., add visible_when: { "source_component": "Email_Submit_Link" }.

---

## Offers & Deals

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Two workflows contain conditional_branch expressions that reference form fields which are not declared under visible_when/required_when or as state keys in the AST, a structural error requiring regeneration or AST/workflow fixes.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- For WF-007 (Book Now — no filters selected): either remove the conditional_branch or update the AST to declare these fields under visible_when/required_when (e.g., add visible_when/required_when entries that expose 'Service_Type', 'Destination', and 'Travel_Dates') so the condition references valid AST field names.
- For WF-008 (Terms and Conditions (Offers List) — no filters selected): either remove the conditional_branch or update the AST to declare these fields under visible_when/required_when (e.g., add visible_when/required_when entries that expose 'Service_Type', 'Destination', and 'Travel_Dates') so the condition references valid AST field names.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the Logout button action and its on_success behavior; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---
