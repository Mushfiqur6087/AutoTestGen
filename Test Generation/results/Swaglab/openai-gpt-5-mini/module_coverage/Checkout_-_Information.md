# Coverage Evaluation — Checkout - Information (Swaglab / openai-gpt-5-mini)

GT source: dataset/ground_truth/Swaglab/modules/Checkout_-_Information.md
GEN source: results/Swaglab/openai-gpt-5-mini/modules/Checkout_-_Information.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria, incl. Rule 6 N-field equivalence)

**Revision note:** SL-CHK1-012 was revised (2026-07-15) to replace a scenario GEN's suite never tests (error message visual styling) with a scenario matching behavior GEN's suite actually demonstrates (unauthenticated access blocked). SL-CHK1-007 was left unchanged and remains a genuine gap.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| SL-CHK1-001 | Complete checkout info | Covered | TC-001 | Exact match |
| SL-CHK1-002 | Cancel checkout | Covered | TC-002 | Exact match |
| SL-CHK1-003 | First Name empty | Covered | TC-003, TC-004, TC-010 | Direct match, reinforced by the all-blank and whitespace-only-treated-as-blank tests |
| SL-CHK1-004 | Last Name empty | Covered | TC-004 | Explicitly named in the all-fields-empty test's per-field error assertion (Rule 6 N-field equivalence) |
| SL-CHK1-005 | Postal Code empty | Covered | TC-004 | Explicitly named in the all-fields-empty test's per-field error assertion |
| SL-CHK1-006 | All fields empty | Covered | TC-004 | Exact match |
| SL-CHK1-007 | Single character inputs | Not Covered | — | No GEN test enters a single-character (minimum-length) value into any field; existing edge tests target long strings, special characters, and whitespace, not this boundary |
| SL-CHK1-008 | Very long inputs | Covered | TC-007 | Exact match |
| SL-CHK1-009 | Special characters | Covered | TC-008 | Exact match |
| SL-CHK1-010 | Numeric First/Last Name | Covered | TC-008 | TC-008 proves the name fields accept special characters/emoji without strict format validation — a more exotic case that implies the milder numeric-character case is also accepted (Rule 7) |
| SL-CHK1-011 | Form elements displayed | Covered | TC-001, TC-002 | Both tests successfully locate and interact with every listed field and button (First Name, Last Name, Postal Code, Continue, Cancel), which necessarily implies their visibility/presence |
| SL-CHK1-012 | Unauthenticated access blocked | Covered | TC-005 | Exact match |

## Gap List (Not Covered)

- **SL-CHK1-007** — Single-character (minimum-length) input boundary

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Checkout - Information | 12 | 11 | 1 | 91.7% |
