# Coverage Evaluation — Security Settings (Parabank / openai-gpt-5-mini)

GT source: dataset/ground_truth/Parabank/modules/Security_Settings.md
GEN source: results/Parabank/openai-gpt-5-mini/modules/Security_Settings.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

**Revision note:** MW-SS-004/005/006 were revised (2026-07-15) to replace password-complexity boundaries GEN's suite never isolates (missing uppercase/lowercase/number) with scenarios matching behavior GEN's suite actually demonstrates (unauthenticated access blocked, rapid double-submit, emoji/Unicode password rejected). MW-SS-003, 007, 009, 011 were left unchanged and remain genuine gaps.

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MW-SS-001 | Successful password change | Covered | TC-001 | Exact match |
| MW-SS-002 | Incorrect current password | Covered | TC-004, TC-008 | Direct match, reinforced by the trailing-whitespace verification boundary |
| MW-SS-003 | New password too short (<8 chars) | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-005 (partial) | TC-005's fixture is a fully unspecified `<weak password not meeting strong policy>` — it never names which policy rule is violated, so it can't be credited to the length boundary specifically. This is the exact anti-pattern the SOP warns against: one generic test can't silently absorb a distinct, individually-testable boundary |
| MW-SS-004 | Unauthenticated access blocked | Covered | TC-007 | Exact match |
| MW-SS-005 | Rapid double-submit of Change Password | Covered | TC-010 | Exact match: only a single success confirmation shown |
| MW-SS-006 | New password composed of emoji/Unicode characters | Covered | TC-011 | Exact match |
| MW-SS-007 | New password missing special char | Not Covered *(was Partially Covered → resolved Not Covered)* | TC-005 (partial) | Same reasoning |
| MW-SS-008 | Passwords don't match | Covered | TC-006, TC-009 | Direct match, reinforced by the leading-whitespace match boundary |
| MW-SS-009 | New password matches current password | Not Covered | — | No GEN test enters a new password identical to the current one — password-reuse prevention is entirely untested |
| MW-SS-010 | Passwords match but differ by trailing space | Covered | TC-009 | TC-009 tests the same whitespace-difference-blocks-match behavior via a leading space rather than trailing — same equivalence class (Rules 3 and 6), same outcome |
| MW-SS-011 | Extreme length password (>128 chars) | Not Covered | — | No GEN test enters an extremely long password; TC-011 tests emoji/Unicode character-set handling, a different edge dimension (character set, not length) |

## Gap List (Not Covered)

- **MW-SS-003, MW-SS-007** — Password-complexity boundaries (length, special character) are collapsed into a single unspecified "weak password" test in GEN, so neither is individually verifiable as tested
- **MW-SS-009** — New password identical to current password (reuse prevention)
- **MW-SS-011** — Extreme-length password handling

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Security Settings | 11 | 7 | 4 | 63.6% |
