# PHPTravels Test Cases — Ground Truth

Source: dataset/ground_truth/Phptravels/Phptravels.md

## Home Page And Search

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-001 | Home page navigation elements displayed | None | 1. Navigate to the PHPTravels home page | Top navigation, currency selector, language selector, login/signup links, and search widget are visible | High |
| HOME-002 | Hotel search from home page | None | 1. Select the Hotels tab<br>2. Enter destination<br>3. Select valid check-in and check-out dates<br>4. Set guests and rooms<br>5. Click "Search" | User is redirected to the hotel listing page with matching search criteria summary | High |
| HOME-003 | Flight search from home page | None | 1. Select the Flights tab<br>2. Enter origin and destination<br>3. Select valid dates and class<br>4. Click "Search" | User is redirected to the flight listing page with results matching the search criteria | High |
| HOME-004 | Tour search from home page | None | 1. Select the Tours tab<br>2. Enter destination<br>3. Select travel date<br>4. Click "Search" | User is redirected to the tour listing page with matching results | Medium |
| HOME-005 | Car search from home page | None | 1. Select the Cars tab<br>2. Enter pick-up and drop-off data<br>3. Select valid date and time values<br>4. Click "Search" | User is redirected to the car listing page with matching results | Medium |
| HOME-006 | Featured content sections displayed | None | 1. Scroll through the home page | Featured hotels, popular destinations, and promotional sections are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-007 | Hotel search with required fields missing | None | 1. Select Hotels tab<br>2. Leave destination or required dates empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-008 | Flight search with required fields missing | None | 1. Select Flights tab<br>2. Leave origin or destination empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-009 | Invalid hotel date range | None | 1. Select Hotels tab<br>2. Choose check-out before check-in<br>3. Click "Search" | Search is blocked or date validation feedback is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-010 | One-way flight disables return date | None | 1. Select Flights tab<br>2. Choose "One Way" | Return date field becomes disabled or inactive | Medium |
| HOME-011 | Same-day search values | None | 1. Perform search using the earliest allowed same-day date values | Search handles the earliest valid date boundary consistently | Low |
