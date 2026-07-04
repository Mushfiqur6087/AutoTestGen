# Structural Model Critique — Parabank

Generated: 2026-07-04T15:05:28.327021Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST includes the required form, both input fields with their validation constraints, the Sign In submit action with success/failure behavior, and the Forgot Password link, matching the description.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the registration form, required fields, validation constraints, auto-formatting, and submit action with success/failure behavior.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

The AST includes the single interactive element (clickable Account Number row action) described and contains no critical missing items, phantoms, or structural errors.

**Missing:** none

**Phantoms:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements (account type selection, deposit amount, funding source, open button), required validations (minimums per account type, numeric deposit, funding balance), real-time validation flags, and the success redirect, matching the description.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements, conditionals, validations, and success/failure behaviors described for the Transfer Funds form.

**Missing:** none

**Phantoms:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive form fields, the Pay action, the account-number match constraint, funds-availability constraint, and success/failure behaviors described.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST includes all expected interactive elements (loan type selection, amount, down payment, collateral account), the conditional amount ranges, validation rules, submission simulation, and success/failure outcomes described; no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST includes the form, all seven editable fields marked required with format constraints, the Update Profile submit action, and the described precondition, success, and failure behaviors — matching the description.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

AST includes both forms, all interactive fields, submit actions, validations, and success/failure behaviors described; no critical elements or structural errors found.

**Missing:** none

**Phantoms:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

The AST includes the expected interactive forms, fields, conditional validations, submit actions, preconditions, and success/error behaviors from the description; no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

The AST includes both forms, their interactive fields, conditionals, validations, preconditions, and submit actions as described; no critical issues found.

**Missing:** none

**Phantoms:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the collapsible panel, form, three password fields, submit action, verification and validation behaviors described.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

All expected interactive elements and submit actions are present; only small type-specific details are missing.

**Missing:**

- {'path': 'components.Secure_Message_Form.fields.Message_Body.type', 'severity': 'minor', 'reason': "Description specifies the message body is rich-text; the AST lists Message_Body but its type is 'unspecified'."}
- {'path': 'components.Secure_Message_Form.fields.Subject.type', 'severity': 'minor', 'reason': "Description references Subject with a length validation (a text input); the AST includes Subject but its type is 'unspecified'."}
- {'path': 'components.Schedule_Callback_Form.fields.Phone_Number.type', 'severity': 'minor', 'reason': "Description indicates Phone Number is pre-filled and editable with format validation (a phone input); the AST marks it prefilled but leaves type 'unspecified'."}

**Phantoms:** none

---
