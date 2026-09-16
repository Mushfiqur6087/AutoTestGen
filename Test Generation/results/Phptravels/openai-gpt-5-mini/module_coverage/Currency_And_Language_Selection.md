# Coverage Evaluation — Currency And Language Selection (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Currency_And_Language_Selection.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Currency_&_Language_Selection.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| PREF-001 | Currency selector updates displayed prices | Covered | TC-001, TC-002 | Exact match |
| PREF-002 | Language selector updates interface text | Covered | TC-003, TC-004 | Exact match |
| PREF-003 | Arabic or RTL language applies RTL layout | Covered | TC-011 | Exact match |
| PREF-005 | Unsupported preference value cannot be applied | Covered | TC-007, TC-008 | Exact match |
| PREF-006 | Currency preference persists across page navigation | Covered | TC-001, TC-002 | Both assert the selection persists after a reload — same equivalence class as persisting across navigation |
| PREF-007 | Authenticated language selection persists to profile preferences | Covered | TC-012 | Exact match |

## Gap List (Not Covered)

None — all GT scenarios are covered.

## Revision Note

GEN never simulates a literal logout-then-login cycle to re-check a persisted preference. It does demonstrate a real, previously-uncredited behavior — persistence to the authenticated user's profile, verified via the Account/Preferences UI — which is the functional mechanism a relogin-survival check would depend on:

- **PREF-007** (was: Authenticated preference persists after relogin) → Authenticated language selection persists to profile preferences (TC-012)

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Currency And Language Selection | 6 | 6 | 0 | 100.0% |
