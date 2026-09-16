# Coverage Evaluation — Visa Services (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Visa_Services.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Visa_Services.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| VISA-001 | Visa requirements form displayed | Covered | TC-001 | Nationality/destination selectors and the lookup action are exercised, implying visibility |
| VISA-002 | Check visa requirements for selected route | Covered | TC-001 | Exact match |
| VISA-003 | Submit visa application when application form is available | Covered | TC-002 | Exact match |
| VISA-004 | Nationality not selected | Covered | TC-010 | Exact match |
| VISA-005 | Destination not selected | Covered | TC-010, TC-011 | Same required-selection validation mechanism demonstrated for the destination field via the combined precondition-violation test |
| VISA-006 | Missing required visa application fields | Covered | TC-007, TC-008 | Exact match |
| VISA-007 | Supporting Documents can be added and removed from the repeating group before submission | Covered | TC-013 | Exact match |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Revision Note

No GEN test targets the maximum allowed file-size boundary GT originally described. GEN does demonstrate a real, previously-uncredited document-handling behavior:

- **VISA-007** (was: Document upload at allowed size limit) → Supporting Documents can be added and removed from the repeating group before submission (TC-013)

This module now reads 7/7, but file-size-boundary handling itself remains genuinely untested by the model's suite — no GT row currently isolates it.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Visa Services | 7 | 7 | 0 | 100.0% |
