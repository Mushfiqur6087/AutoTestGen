# Mifos Banking System Test Cases — Ground Truth

Source: dataset/ground_truth/Mifos/Mifos.md

## Global Search

### Functional Tests

| TC ID         | Test Case                                | Preconditions          | Steps                                                                     | Expected Result                                                                         | Priority |
| ------------- | ---------------------------------------- | ---------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------- |
| MF-SEARCH-001 | Global search bar visible in toolbar     | User logged in         | 1. Observe top toolbar/header                                             | Search input is visible and accessible from authenticated pages                         | High     |
| MF-SEARCH-002 | Search active client by name             | Active client exists   | 1. Enter full or partial client name in global search<br>2. Submit search | Matching client appears in results with link to client detail page                      | High     |
| MF-SEARCH-003 | Search loan account by account number    | Loan account exists    | 1. Enter exact loan account number<br>2. Submit                           | Matching loan account appears in results and opens loan detail page when selected       | High     |
| MF-SEARCH-004 | Search savings account by account number | Savings account exists | 1. Enter exact savings account number<br>2. Submit                        | Matching savings account appears in results and opens savings detail page when selected | High     |

### Negative Tests

| TC ID         | Test Case                | Preconditions  | Steps                                                        | Expected Result                                                       | Priority |
| ------------- | ------------------------ | -------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- | -------- |
| MF-SEARCH-009 | Search non-existent term | User logged in | 1. Enter random string not mapped to any entity<br>2. Submit | "No results found" or equivalent empty-state message displayed        | Medium   |
| MF-SEARCH-010 | Unauthenticated user cannot open Global Search | User is not authenticated | 1. Open the application root URL as an unauthenticated user<br>2. Attempt to click the top-bar search icon | Search input does not open; the user is redirected to the login page and no search UI is focused or usable | Low      |

### Boundary Tests

| TC ID         | Test Case                                                  | Preconditions                                                    | Steps                                  | Expected Result                                                               | Priority |
| ------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------- | -------- |
| MF-SEARCH-013 | Partial prefix match                                       | Multiple entities with similar prefixes exist                    | 1. Enter partial prefix of entity name | Relevant matching results are returned according to supported search behavior | Medium   |
| MF-SEARCH-014 | Opening an entity detail from search results is blocked when the user lacks detail-view permission | User can invoke search but lacks permission to view the matched entity's detail page | 1. Search for a term matching an entity the user lacks detail-view permission for<br>2. Click the matching item in the results dropdown | Navigation to the entity's detail page is blocked; an access-denied indicator is shown and the user remains on the current page | Medium   |

### Additional Coverage Tests

| TC ID         | Test Case                                                         | Preconditions                                | Steps                                     | Expected Result                                                          | Priority |
| ------------- | ----------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------ | -------- |
| MF-SEARCH-016 | Search result click navigates to correct entity detail page       | Searchable entity exists                     | 1. Run search<br>2. Click matching result | Correct entity profile/account page opens                                | High     |
| MF-SEARCH-017 | Search supports case-insensitive text matching                    | Searchable entity exists                     | 1. Search using different case variation  | Matching entity is returned regardless of letter case                    | Medium   |
| MF-SEARCH-018 | Search results update correctly across entity types for same term | Client/group/center with similar names exist | 1. Search shared term                     | Results include all authorized matching entity types without duplication | Medium   |
