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
| PREF-007 | Authenticated preference persists after relogin | Logged in as user | 1. Change language or currency<br>2. Log out and log back in | Stored preference remains applied if profile persistence is supported | Low |
