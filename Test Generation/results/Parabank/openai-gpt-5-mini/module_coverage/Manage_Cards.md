# Coverage Evaluation — Manage Cards (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Manage_Cards.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Manage_Cards.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MW-MC-012/013 were revised (2026-07-15) to replace scenarios GEN's suite never tests (today-start travel notice, rapid Frozen/Active toggle) with scenarios matching behavior GEN's suite actually demonstrates (non-numeric spending limit rejected, unauthenticated access blocked). MW-MC-008 and 011 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-MC-001 | Request Debit card | Covered | TC-001 | TC-001 parameterizes `<Card Type>` over the same request flow — same equivalence class (Rule 6) as the Debit-specific case |
| MW-MC-002 | Request Credit card | Covered | TC-001 | Same reasoning as MW-MC-001 |
| MW-MC-003 | Incomplete address | Covered | TC-009 | Exact match: incomplete address rejected with inline validation error |
| MW-MC-004 | No account selected | Covered | TC-007 | Exact match: Account_To_Link left blank → inline validation error |
| MW-MC-005 | Update spending limit | Covered | TC-002 | Exact match |
| MW-MC-006 | Add travel notice | Covered | TC-003 | Exact match, and more thorough (multiple destinations) |
| MW-MC-007 | Freeze card | Covered | TC-004 | Exact match: Active → Frozen transition succeeds |
| MW-MC-008 | Unfreeze card | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-004, TC-014 (partial) | GEN only exercises the Active→Frozen direction (TC-004) and a rejected Active→Active no-op (TC-014); the reverse Frozen→Active transition is never attempted — a distinct, separately-testable direction |
| MW-MC-009 | Invalid spending limit (above max) | Covered | TC-011 | Exact match |
| MW-MC-010 | Invalid date range | Covered | TC-012, TC-016 | TC-012 direct match; TC-016 reinforces with the one-day-before boundary |
| MW-MC-011 | Spending limit exactly at policy maximum | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-002, TC-011 (partial) | TC-002 tests a generic within-policy limit and TC-011 tests exceeding the max, but the exact-boundary value itself is never entered — a distinct boundary value per the SOP's explicit carve-out |
| MW-MC-012 | Non-numeric spending limit | Covered | TC-010 | Exact match |
| MW-MC-013 | Unauthenticated access blocked | Covered | TC-005 | Exact match |

## Gap List (Not Covered)

- **MW-MC-008** — Frozen → Active (unfreeze) transition never tested, only the reverse direction
- **MW-MC-011** — Spending limit exactly at policy maximum boundary value

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Manage Cards | 13 | 11 | 2 | 84.6% |
