# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Investments

### Portfolio Snapshot Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-INV-001 | View portfolio snapshot | User logged in | 1. Navigate to Investments | Read-only panel shows fund holdings, market value, unrealized gain/loss | High |

### Trade Funds Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-INV-002 | Buy funds | User logged in, sufficient funds | 1. Select Action: Buy<br>2. Enter/select Fund Symbol<br>3. Enter Quantity > 0<br>4. Select Funding Account<br>5. Click "Execute Trade" | "Trade executed successfully." with order ID | High |
| MW-INV-003 | Sell funds | User logged in, has shares | 1. Select Action: Sell<br>2. Enter Fund Symbol<br>3. Enter Quantity <= shares owned<br>4. Select Destination Account<br>5. Submit | Trade executed successfully | High |
| MW-INV-004 | Fund symbol autocomplete | User logged in | 1. Start typing fund symbol | Autocomplete suggestions appear | Medium |
| MW-INV-005 | Invalid fund symbol | User logged in | 1. Enter non-existent symbol<br>2. Submit | Validation error: symbol not found | High |
| MW-INV-006 | Zero quantity | User logged in | 1. Enter 0 as quantity<br>2. Submit | Validation error: quantity must be > 0 | High |
| MW-INV-007 | Insufficient buying power | User logged in | 1. Try to buy more than account allows<br>2. Submit | Validation error: insufficient funds | High |
| MW-INV-008 | Sell more than owned | User logged in | 1. Try to sell more shares than owned<br>2. Submit | Validation error: insufficient shares | High |

### Recurring Investment Plan Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-INV-009 | Create weekly plan | User logged in | 1. Enter Fund Symbol<br>2. Enter Contribution Amount<br>3. Select Frequency: Weekly<br>4. Enter future Start Date<br>5. Select Funding Account<br>6. Click "Create Plan" | "Plan created successfully." | High |
| MW-INV-010 | Create monthly plan | User logged in | 1. Enter all fields<br>2. Select Monthly<br>3. Submit | Plan created | High |
| MW-INV-011 | Past start date | User logged in | 1. Enter start date in the past<br>2. Submit | Validation error: "Start date must be in the future" | High |
| MW-INV-012 | Below minimum contribution | User logged in | 1. Enter contribution below minimum<br>2. Submit | Validation error | High |
| MW-INV-013 | Insufficient funding balance | User logged in | 1. Select account with low balance<br>2. Submit | Validation error: inadequate balance | High |
| MW-INV-014 | Start date exactly today | User logged in | 1. Enter start date = today | Handled based on cutoff rules | Medium |
| MW-INV-015 | Sell exact total shares owned | User logged in | 1. Sell quantity = total shares | Success, balance goes to 0 | Medium |
