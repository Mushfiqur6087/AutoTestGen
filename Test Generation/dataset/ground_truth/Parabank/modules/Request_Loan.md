# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Request Loan

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-RL-001 | Personal loan approved | User logged in, sufficient collateral | 1. Select Personal Loan card<br>2. Enter amount $1,000-$50,000<br>3. Enter down payment (>= 10% of loan)<br>4. Select collateral account<br>5. Click submit | "Loan approved and created successfully!" with account details | High |
| MW-RL-002 | Auto loan approved | User logged in, sufficient collateral | 1. Select Auto Loan<br>2. Enter amount $5,000-$75,000<br>3. Enter down payment<br>4. Select collateral<br>5. Submit | Loan approved | High |
| MW-RL-003 | Home loan approved | User logged in, sufficient collateral | 1. Select Home Loan<br>2. Enter amount $50,000-$500,000<br>3. Enter down payment<br>4. Select collateral<br>5. Submit | Loan approved | High |
| MW-RL-004 | Loan type cards | User logged in | 1. View loan selection | Cards show: Personal (7.5% APR), Auto (4.5% APR), Home (3.5% APR) with ranges | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-RL-005 | Personal loan below minimum | User logged in | 1. Select Personal<br>2. Enter $500 (below $1,000 min)<br>3. Submit | Validation error: minimum $1,000 | High |
| MW-RL-006 | Personal loan above maximum | User logged in | 1. Select Personal<br>2. Enter $60,000 (above $50,000 max)<br>3. Submit | Validation error: maximum $50,000 | High |
| MW-RL-007 | Auto loan below minimum | User logged in | 1. Select Auto<br>2. Enter $3,000<br>3. Submit | Validation error: minimum $5,000 | High |
| MW-RL-008 | Auto loan above maximum | User logged in | 1. Select Auto<br>2. Enter $80,000<br>3. Submit | Validation error: maximum $75,000 | High |
| MW-RL-009 | Home loan below minimum | User logged in | 1. Select Home<br>2. Enter $40,000<br>3. Submit | Validation error: minimum $50,000 | High |
| MW-RL-010 | Home loan above maximum | User logged in | 1. Select Home<br>2. Enter $600,000<br>3. Submit | Validation error: maximum $500,000 | High |
| MW-RL-011 | Down payment >= loan | User logged in | 1. Enter down payment equal to or greater than loan amount<br>2. Submit | Validation error: down payment must be less than loan | High |
| MW-RL-012 | Insufficient collateral (< 20%) | User logged in | 1. Enter loan where collateral account < 20% of loan<br>2. Submit | Denial: "Inadequate collateral value" | High |
| MW-RL-013 | Down payment < 10% | User logged in | 1. Enter down payment < 10% of loan<br>2. Submit | Denial or validation error | High |
| MW-RL-014 | No loan type selected | User logged in | 1. Don't select loan type<br>2. Submit | Validation error | High |
| MW-RL-015 | No collateral account | User logged in | 1. Don't select collateral<br>2. Submit | Validation error | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-RL-016 | Exact minimum Personal ($1,000) | User logged in | 1. Enter exactly $1,000<br>2. Valid down payment<br>3. Submit | Loan processed | Medium |
| MW-RL-017 | Exact maximum Personal ($50,000) | User logged in | 1. Enter exactly $50,000<br>2. Valid down payment<br>3. Submit | Loan processed | Medium |
| MW-RL-018 | Exactly 10% down payment | User logged in | 1. Enter loan amount<br>2. Enter exactly 10% as down payment<br>3. Submit | Loan processed | Medium |
| MW-RL-019 | Non-numeric loan amount | User logged in | 1. Enter "abc" in loan amount | Validation error | High |
| MW-RL-020 | Down payment exactly one cent below 10% | User logged in | 1. Enter down payment = 9.99% | Denial or validation error | Medium |
