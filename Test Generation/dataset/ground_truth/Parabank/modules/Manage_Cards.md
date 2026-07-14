# ParaBank Test Cases — Ground Truth

Source: dataset/ground_truth/Parabank/Parabank.md

## Manage Cards

### Card Request Form Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-MC-001 | Request Debit card | User logged in | 1. Select Card Type: Debit<br>2. Select account to link<br>3. Enter complete shipping address<br>4. Click "Request Card" | "Card request submitted successfully." with tracking ID | High |
| MW-MC-002 | Request Credit card | User logged in | 1. Select Card Type: Credit<br>2. Select account<br>3. Enter address<br>4. Submit | Card request submitted | High |
| MW-MC-003 | Incomplete address | User logged in | 1. Leave shipping address incomplete<br>2. Submit | Validation error: address required | High |
| MW-MC-004 | No account selected | User logged in | 1. Don't select account to link<br>2. Submit | Validation error | High |

### Card Controls Form Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MW-MC-005 | Update spending limit | Existing card | 1. Select existing card<br>2. Enter new spending limit<br>3. Click "Update Controls" | "Card controls updated successfully." | High |
| MW-MC-006 | Add travel notice | Existing card | 1. Select card<br>2. Enter travel dates and destination<br>3. Submit | Controls updated | Medium |
| MW-MC-007 | Freeze card | Existing card, Active | 1. Select card<br>2. Change status to Frozen<br>3. Submit | Card frozen successfully | High |
| MW-MC-008 | Unfreeze card | Existing card, Frozen | 1. Select frozen card<br>2. Change status to Active<br>3. Submit | Card activated | High |
| MW-MC-009 | Invalid spending limit | Existing card | 1. Enter limit above policy maximum<br>2. Submit | Validation error displayed inline | High |
| MW-MC-010 | Invalid date range | Existing card | 1. Enter end date before start date<br>2. Submit | Validation error | Medium |
| MW-MC-011 | Spending limit exactly at policy maximum | Existing card | 1. Enter limit exactly at policy max | Accepted | Medium |
| MW-MC-012 | Travel notice for same day | Existing card | 1. Enter start date = today | Accepted | Medium |
| MW-MC-013 | Rapid status toggle | Existing card | 1. Rapidly toggle Frozen/Active | Handled without state corruption | Low |
