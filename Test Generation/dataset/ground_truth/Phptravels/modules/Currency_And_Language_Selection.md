# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Currency And Language Selection

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-001 | Currency selector updates displayed prices | None | 1. Change currency from the top navigation | Prices across the current page update to the selected currency | High |
| PREF-002 | Language selector updates interface text | None | 1. Change language from the top navigation | Interface text updates to the selected language | High |
| PREF-003 | Arabic or RTL language applies RTL layout | RTL language option is available | 1. Select Arabic or another RTL language | Page layout and text direction switch to RTL where applicable | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-005 | Unsupported preference value cannot be applied | None | 1. Attempt to select unavailable currency or language option | Invalid selection is not applied | Low |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-006 | Currency preference persists across page navigation | None | 1. Change currency<br>2. Navigate to another page | Selected currency remains active across navigation | Medium |
| PREF-007 | Authenticated language selection persists to profile preferences | User is authenticated and on any page with an active session; Account/Preferences page is available | 1. Open the Language selector<br>2. Select a language different from the current site language<br>3. Navigate to the Account or Preferences page | The Account/Preferences page visibly shows the newly selected language as the saved preference; the site continues to display the chosen language across pages | Low |
