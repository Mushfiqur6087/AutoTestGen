# Structural Model Critique — Parabank

Generated: 2026-07-04T16:25:15.026751Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST includes the two required fields, validation constraints, the Sign In submit action with success/failure behavior, and the Forgot Password link — matching the description.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The AST includes all required form fields, validation constraints, state dropdown options, submit action with precondition, success message and redirect — matching the description.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

The AST captures the single interactive element (clickable Account Number as a row action) and includes appropriate preconditions; no critical elements or structural errors were found.

**Missing:** none

**Phantoms:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

AST is usable; it captures the required interactive fields, validations, preconditions, and submit behavior, with one minor omission in the Account_Type field type.

**Missing:**

- {'path': 'components.Open_New_Account_Form.fields.Account_Type.type', 'severity': 'minor', 'reason': "The description specifies interactive account-type selection cards (Checking or Savings); the AST includes Account_Type and options but leaves its type as 'unspecified' instead of a selector/card type (e.g., 'card_selector' or 'radio_card')."}

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the described interactive elements, conditionals, validations, and submit behavior for the Transfer Funds form.

**Missing:** none

**Phantoms:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST includes the form, all named interactive fields (including dropdown and number), the Pay submit action, the account-number match and funds-check constraints, and the precondition/on_success/on_failure behavior, so it is acceptable to use as-is.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements, conditionals, validations, preconditions, and simulated outcomes described for the Request Loan page.

**Missing:** none

**Phantoms:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the editable fields, validation, submit action, and success/failure behavior; only minor metadata about pre-filled initial values is missing.

**Missing:**

- {'path': 'components.Update_Contact_Info_Form.fields', 'severity': 'minor', 'reason': 'The description states the form is pre-filled with First Name, Last Name, Street Address, City, State, ZIP Code, and Phone Number; the AST does not include initial_value/prefilled metadata for these fields.'}

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the two forms, their interactive fields, validations, submit actions, preconditions, and success/failure behaviors described; no critical elements are missing.

**Missing:** none

**Phantoms:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive fields, conditional validations, submit actions, and on_success behavior described for both forms; no critical elements or structural errors were found.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

AST includes both forms, all interactive fields, conditionals, validations, and submit actions described in the specification; no critical gaps found.

**Missing:** none

**Phantoms:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements and constraints; only a minor omission of explicit failure handling for validation feedback.

**Missing:**

- {'path': 'components.Change_Password_Panel.fields.Change_Password_Form.submit_actions[0].on_failure', 'severity': 'minor', 'reason': 'The description states that validation errors highlight the appropriate fields (a failure consequence), but the AST does not include an on_failure or validation_error handling entry mapping failures to field-level feedback.'}

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

The AST includes both forms, all interactive fields, specified constraints, submit actions with on_success/on_failure behavior, and matches the described preconditions and validation rules.

**Missing:** none

**Phantoms:** none

---
