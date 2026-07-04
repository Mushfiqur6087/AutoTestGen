# Workflow Critique — Parabank

Generated: 2026-07-04T15:05:28.347146Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the required Sign In submit_action and matches the AST on_success; no required workflows or structural errors are missing.

**Missing workflows:** none

**Phantom workflows:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's sole submit action and matches the AST's on_success; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: the data_table row action 'Account Number' is represented and there are no forms, state-bound actions, or bulk actions requiring additional workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

Workflows correctly cover the form's submit action for both Account_Type options and match the AST on_success behavior; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

Workflows cover each submit action for both conditional branches (internal and external transfers); no missing or phantom workflows or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's sole submit action 'Pay' with matching on_success and no conditional branches or state/table actions missing, so the workflow list is complete and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

All required workflows present: each Submit Application path for the three Loan_Type conditions is represented, with no missing or phantom workflows or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The workflow list includes the required submit workflow for the form's 'Update Profile' action with matching on_success; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

Workflows cover each form submit action and conditional variants present in the AST; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the Trade Funds form (both Buy and Sell branches) and the Recurring Investment Plan form submit action; no missing or phantom workflows or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and conditional branches in the AST are covered by corresponding workflows; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's submit action and matches the AST's on_success; no missing or phantom workflows or structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

Both form submit actions are represented with matching on_success texts; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---
