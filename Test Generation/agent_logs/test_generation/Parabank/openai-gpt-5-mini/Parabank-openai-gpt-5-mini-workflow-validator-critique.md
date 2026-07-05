# Workflow Critique — Parabank

Generated: 2026-07-04T16:25:15.081852Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The workflows cover the form submit action 'Sign In' and the 'Forgot Password?' link; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's 'Register' submit action and matches the AST's on_success behavior; no required workflows or structural errors are missing.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

All required workflows for the data_table row action and action_bar available actions are present and correctly mapped to the AST; no structural errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's submit_action 'Open Account' and matches the AST's on_success behavior; no missing or phantom workflows or structural errors were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action and both conditional branches for internal and external transfers; no missing or phantom workflows or structural errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover the form's submit action (successful submission and the two explicit failure modes from the AST) and there are no missing or phantom workflows or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form's Apply submit action including Loan_Type-specific branches and match the AST's on_success text; no critical or structural issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the form's submit_action with matching on_success text and there are no missing, phantom, or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

Workflows cover each form submit action and there are no missing, phantom, or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

The provided workflows cover all submit actions and conditional branches in the AST and contain no structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and conditional combinations in the AST are covered by workflows; no missing or phantom workflows or structural errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the form's submit action with the correct success path and on_success text; no required workflows or phantoms were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

All form submit actions in the AST are covered by workflows and there are no missing, phantom, or structural errors.

**Missing workflows:** none

**Phantom workflows:** none

---
