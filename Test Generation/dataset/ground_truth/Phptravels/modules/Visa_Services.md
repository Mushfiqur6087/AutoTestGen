# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Visa Services

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-001 | Visa requirements form displayed | None | 1. Open the Visa page | Nationality selector, Destination selector, and requirement lookup action are visible | High |
| VISA-002 | Check visa requirements for selected route | None | 1. Select nationality<br>2. Select destination<br>3. Click "Check Requirements" or equivalent action | Visa requirement details, processing time, validity, required documents, and fees are displayed | High |
| VISA-003 | Submit visa application when application form is available | Visa application form is enabled and user has required documents | 1. Complete visa application fields<br>2. Upload required documents<br>3. Submit application | Visa application is submitted and application status or confirmation is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-004 | Nationality not selected | None | 1. Leave nationality empty<br>2. Select destination<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-005 | Destination not selected | None | 1. Select nationality<br>2. Leave destination empty<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-006 | Missing required visa application fields | Visa application form is enabled | 1. Leave one or more required applicant fields empty<br>2. Submit application | Validation errors are displayed and application is not submitted | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-007 | Document upload at allowed size limit | Visa application form is enabled | 1. Upload a supported document at the maximum allowed size<br>2. Submit application | Document is accepted at the allowed boundary | Low |
