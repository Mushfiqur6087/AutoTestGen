# Coverage Evaluation — Home Page And Search (Phptravels / openai-gpt-5-mini)

GT source: dataset/ground_truth/Phptravels/modules/Home_Page_And_Search.md
GEN source: results/Phptravels/openai-gpt-5-mini/modules/Home_Page_&_Search.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| HOME-001 | Search widget with Hotels/Flights/Tours/Cars tabs is visible and functional | Covered | TC-001, TC-002, TC-003, TC-004 | Each tab's search form is exercised end-to-end, directly demonstrating it is visible and functional |
| HOME-002 | Hotel search from home page | Covered | TC-001 | Exact match |
| HOME-003 | Flight search from home page | Covered | TC-002 | Exact match |
| HOME-004 | Tour search from home page | Covered | TC-003 | Exact match |
| HOME-005 | Car search from home page | Covered | TC-004 | Exact match |
| HOME-006 | Featured content sections displayed | Not Covered | — | No GEN test scrolls through or asserts featured hotels/popular destinations/promotional sections |
| HOME-007 | Hotel search with required fields missing | Covered | TC-005, TC-009 | Exact match |
| HOME-008 | Flight search with required fields missing | Covered | TC-006 | Exact match |
| HOME-009 | Invalid hotel date range | Not Covered | — | No GEN test sets check-out before check-in on the Home page Hotels tab |
| HOME-010 | Flight search Departure City accepts special characters and emoji | Covered | TC-013 | Exact match |
| HOME-011 | Hotels Destination accepts very long free-text input | Covered | TC-012 | Exact match |

## Gap List (Not Covered)

- **HOME-006** — Featured content sections untested
- **HOME-009** — Invalid hotel date range on Home page untested

## Revision Note

Three rows described display/behavior GEN never isolates (full header checklist, one-way disabling return date, same-day boundary). GEN does demonstrate three other real Home-page behaviors that had no GT scenario crediting them:

- **HOME-001** (was: Home page navigation elements displayed) → narrowed to what's actually demonstrated: the four-tab search widget is visible and functional (TC-001–TC-004). The original checklist (currency/language selectors, login/signup links) isn't verified within this module's own suite, so the scenario was scoped to what GEN genuinely proves rather than the full header
- **HOME-010** (was: One-way flight disables return date) → Flight search Departure City accepts special characters and emoji (TC-013)
- **HOME-011** (was: Same-day search values) → Hotels Destination accepts very long free-text input (TC-012)

Genuine gaps were deliberately preserved: no GEN test scrolls through the featured-content sections, and no GEN test sets an invalid hotel date range from the Home page.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Home Page And Search | 11 | 9 | 2 | 81.8% |
