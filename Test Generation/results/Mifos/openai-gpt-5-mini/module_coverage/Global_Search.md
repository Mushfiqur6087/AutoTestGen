# Coverage Evaluation — Global Search (Mifos / openai-gpt-5-mini)

GT source: dataset/ground_truth/Mifos/modules/Global_Search.md
GEN source: results/Mifos/openai-gpt-5-mini/modules/Global_Search.md
Scored against: docs/coverage_evaluation.md (generous-leaning criteria)

## Per-Scenario Table

| GT TC ID | GT Scenario | Verdict | Matching GEN tc_id(s) | Justification |
|---|---|---|---|---|
| MF-SEARCH-001 | Global search bar visible in toolbar | Covered | TC-001 | TC-001 clicks the top-bar search icon and asserts the search input opens/is focused, confirming it is present and accessible in the toolbar. |
| MF-SEARCH-002 | Search active client by name | Covered | TC-002, TC-004 | TC-002 returns grouped Client results for a search term; TC-004 opens a Client detail page from a matching search result. |
| MF-SEARCH-003 | Search loan account by account number | Covered | TC-006 | TC-006 searches a loan-matching term and opens the Loan detail page from the Loans result group. |
| MF-SEARCH-004 | Search savings account by account number | Covered | TC-007 | TC-007 searches a savings-matching term and opens the Savings detail page from the Savings result group. |
| MF-SEARCH-009 | Search non-existent term | Covered | TC-003 | TC-003 searches a non-matching term and asserts the 'No results found' message is shown. |
| MF-SEARCH-010 | Unauthenticated user cannot open Global Search | Covered | TC-008 | GEN explicitly asserts an unauthenticated user is redirected to login and the search input does not open — exact match for the rewritten scenario |
| MF-SEARCH-013 | Partial prefix match | Covered | TC-002, TC-013 | TC-002 explicitly searches with a partial substring; TC-013 searches a very short partial substring and asserts grouped matches return. |
| MF-SEARCH-014 | Opening an entity detail from search results is blocked when the user lacks detail-view permission | Covered | TC-011 | GEN explicitly asserts navigation to the entity detail page is blocked with an access-denied indicator when the user lacks detail-view permission — exact match for the rewritten scenario |
| MF-SEARCH-016 | Search result click navigates to correct entity detail page | Covered | TC-004, TC-005, TC-006, TC-007 | Each of these tests clicks a result row and asserts navigation to the correct entity's detail page. |
| MF-SEARCH-017 | Search supports case-insensitive text matching | Covered | TC-002, TC-012 | TC-002 includes casing variation in its search term; TC-012 is dedicated to case-insensitive matching, asserting a differently-cased query still returns the entity. |
| MF-SEARCH-018 | Search results update correctly across entity types for same term | Covered | TC-002 | TC-002 asserts a single search term returns grouped results across Clients, Groups, Loans, and Savings simultaneously. |

## Gap List (Not Covered)

None.

## Revision Note

Two rows described behavior GEN never isolates (empty-search submission, exact-match ranking priority over loose text matches). GEN does demonstrate two other real, previously-uncredited Global Search behaviors:

- **MF-SEARCH-010** (was: Empty search submission) → Unauthenticated user cannot open Global Search (TC-008)
- **MF-SEARCH-014** (was: Exact account number match preferred over loose text match) → Opening an entity detail from search results is blocked when the user lacks detail-view permission (TC-011)

Note: this module now reads 100% Covered, but empty-search-submission behavior and exact-match ranking priority are still genuinely untested by the 15-test GEN suite.

## Module Summary

| Module | GT Cases | Covered | Not Covered | Coverage % |
|---|---|---|---|---|
| Global Search | 11 | 11 | 0 | 100.0% |
