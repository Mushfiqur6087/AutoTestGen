# Coverage Evaluation — SOP

## This document defines how to score \*_coverage_

## Core Principle

**Coverage is a measure of behavioral alignment, not textual similarity.**

The question for every GT scenario is: _did the generated (GEN) suite exercise the same underlying business rule or edge case, regardless of wording, field names, or fixture data used to trigger it?_

Never score by keyword overlap between the GT `Test Case` string and a GEN `test_case` string. Read both down to the behavior they assert and compare at that level.

**On close calls, lean generous.** If a GEN test genuinely exercises the same feature/flow as a GT scenario — even via a different (but related) precondition, a partially-overlapping boundary, or an outcome the GT scenario itself states loosely/alternatively — prefer the more generous verdict (Covered over Partially Covered, Partially Covered over Not Covered). Reserve **Not Covered** for scenarios where nothing in the GEN suite, even loosely, touches the behavior. Don't manufacture a match that isn't there, but don't withhold credit over a difference in precondition wording or an unisolated (rather than untested) boundary.

---

## Scope: One Module at a Time

This evaluation is run **per module**, not once across the whole system. Each pass takes one module's GT suite and that same module's GEN suite, and scores GT scenarios only against GEN tests from that module. Don't batch multiple modules into a single pass or match a GT scenario in one module against a GEN test from another — repeat the full procedure separately for each module.

## Verdict Scale

Score every GT scenario against the full GEN suite for that module (across `positive`, `negative`, and `edge` categories — the category label is not load-bearing for matching).

| Verdict               | Meaning                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Covered**           | Some GEN test (or combination of GEN tests) exercises the identical behavior/boundary the GT scenario requires.                                                     |
| **Partially Covered** | GEN exercises the general feature or a broader/generic version of it, but misses the specific boundary, negative assertion, or condition the GT scenario calls out. |
| **Not Covered**       | No GEN test — even generically — touches this behavior.                                                                                                             |

---

## Evaluation Rules

### 1. Semantic Equivalence, Not Keyword Matching

If GT and GEN test the identical technical behavior in different words, it's **Covered**.

> GT: "Empty username rejected" · GEN: "Submit form with blank user ID" → **Covered**

### 2. Core Boundaries vs. Generic Tests

A generic/happy-adjacent test does not, by itself, fully substitute for a specific boundary or edge condition — but it earns at least **Partially Covered** if it exercises the same field/flow/feature, rather than defaulting straight to Not Covered. Reserve **Not Covered** for when the feature area itself is untouched.

> GT: "Submit with invalid username format containing special characters" · GEN: "Submit with invalid credentials" → **Partially Covered** — GEN tests the invalid-username path generically, but the special-character boundary itself isn't isolated. (Only **Not Covered** if no GEN test touches invalid-username submission at all.)

### 3. Fixture and Data Agnosticism

Ignore specific data/fixture names as long as they exercise the same logical path.

> GT: clicks "Course 101" · GEN: clicks "Math 102" → same logical outcome, evaluate as if identical.

### 4. Combined vs. Split Scenarios

Match at the behavior level, not 1:1 at the test-case level. Mapping is many-to-many, not one-to-one.

- One GEN test asserting both "empty username" and "empty password" → covers **two** GT scenarios.
- Two separate GEN tests together covering all clauses of one combined GT scenario → that GT scenario is **Covered**.
- One GT scenario can legitimately be satisfied by several GEN tests jointly, even when the GT scenario itself is not a combined/multi-clause one — e.g., GEN-013 exercises the field-level rejection and GEN-021 exercises the resulting error message the GT scenario expects; list both as matches. Don't force a single tc_id when the behavior is only fully asserted across more than one GEN test.

### 5. Negative Assertions & State Checks

A GT scenario requiring an absence ("X is not possible", "Y is not visible") is **Covered** if GEN explicitly asserts the absence, or asserts a directly-blocking consequence of it (e.g., the action fails/is rejected as a result). It is **not** Covered merely because GEN asserts an adjacent, unrelated positive state.

> GT: "Student cannot access Settings" · GEN: "Course tabs are visible" (no mention of Settings) → **Not Covered**. GEN must assert the Settings tab/action is absent or blocked — an unrelated positive assertion doesn't imply it.

### 6. Equivalence Classes

The specific field/entity under test can differ if it belongs to the same functional equivalence class as the GT scenario.

> GT: required-field validation tested via "First Name" blank · GEN: same validation tested via "Email" blank → same equivalence class (required-field validation) → **Covered**.

This generalizes to any number of fields, not just two. If a form has N fields that GT scores as N separate "field X is empty/required" scenarios, and GEN demonstrates that *same* validation mechanism (e.g., blank-submit triggers an inline required-field error) on even one of those fields, credit every GT scenario in that set as **Covered** — don't require a discrete GEN test per field. The rationale: once the pattern (client-side required-field validation exists and behaves consistently) is established for one field, re-proving it field-by-field tests the same code path, not new behavior. This still requires GEN to have actually exercised that validation mechanism on at least one field in the set — it does not extend to a set where no field's blank/required case was tested at all, and it does not let a *different* validation type (e.g., a format or matching check) stand in for the untested required/blank check (see Rule 2's per-boundary guidance).

### 7. Implied and Partial Coverage (Specific Implies General)

A GEN test that exercises a specific, complex edge case of a feature implicitly satisfies the GT scenario for the basic/general version of that same feature.

> GEN: "Search with special characters returns filtered results" → implicitly covers GT: "Standard search returns matching results" → **Covered**.

Note this only runs one direction: a specific edge case implies its general case, but a generic test does **not** imply a specific boundary (see Rule 2).

---

## Evaluation Procedure

For each module, work GT-scenario-first (not GEN-test-first) so nothing in the human suite gets silently skipped:

1. Take one GT scenario row (its `Test Case` + `Steps` + `Expected Result` define the behavior under test).
2. Scan the _entire_ GEN suite for that module — all categories — for any test(s) whose steps + expected result assert the same behavior, applying Rules 1–7.
3. Assign a verdict: `Covered`, `Partially Covered`, or `Not Covered`.
4. Record which GEN `tc_id`(s), if any, produced the match, and a one-line justification (cite the specific boundary/assertion that was or wasn't matched — don't just restate the rule name).
5. Repeat for every GT row in the module, then roll up:
   - `coverage_pct = Covered / total_GT_scenarios` (report Partially Covered separately, don't fold it into either bucket)
   - A gap list of `Not Covered` and `Partially Covered` scenarios, grouped by GT section (Functional / Negative / Boundary / Additional Coverage).
6. Produce the module summary report (see Module Summary Report below). This requires collapsing the three verdicts down to two buckets, so resolve every `Partially Covered` scenario individually:
   - Re-read the specific gap noted in its justification and judge, case by case, whether what's missing is minor/incidental (→ counts as **Covered**) or touches a real, distinct behavior a tester would flag as untested (→ counts as **Not Covered**).
   - Default to **Covered** unless the gap is a concrete, separately-testable behavior a tester would explicitly call out as missing (a distinct boundary value, a distinct error path, a distinct UI-state assertion). A difference in precondition framing, fixture setup, or wording is not, by itself, grounds to withhold Covered.
   - Note the reclassification reasoning inline next to the gap list so the judgment call is auditable.

## Output Template

| GT TC ID     | GT Scenario      | Verdict           | Matching GEN tc_id(s) | Justification                                                                                        |
| ------------ | ---------------- | ----------------- | --------------------- | ---------------------------------------------------------------------------------------------------- |
| MF-LOGIN-007 | Empty username   | Covered           | TC-014                | GEN submits blank username field, asserts inline validation error — same behavior, different wording |
| MF-LOGIN-005 | Invalid username | Partially Covered | TC-013                | GEN only tests generic "invalid credentials"; special-character/format boundary not isolated         |
| MF-LOGIN-009 | Lockout after 3 failed attempts | Covered | TC-016, TC-017 | TC-016 triggers the three failed logins, TC-017 asserts the resulting lockout message — together they satisfy the full GT scenario |

`Matching GEN tc_id(s)` is a list, not a single value — record every GEN test that contributes to the verdict. A GT scenario is frequently satisfied by more than one GEN tc_id even when it isn't itself a combined/multi-clause scenario (see Rule 4).

---

## Module Summary Report

One row per module — produced after the detailed per-scenario table above, once every `Partially Covered` row has been resolved to `Covered` or `Not Covered` per step 6.

| Module               | GT Cases | Covered | Not Covered | Coverage % |
| --------------------- | -------- | ------- | ----------- | ---------- |
| Home Page And Search | 9        | 8       | 1           | 88.9%      |

- `GT Cases` = total GT scenarios for the module.
- `Covered` = scenarios scored `Covered`, plus any `Partially Covered` scenarios reclassified as `Covered` in step 6.
- `Not Covered` = scenarios scored `Not Covered`, plus any `Partially Covered` scenarios reclassified as `Not Covered` in step 6.
- `Coverage % = Covered / GT Cases`.
- This table is generated per module — one row per module run, not one table spanning the whole system (see Scope above).

---

## Anti-Patterns to Avoid When Judging

- Don't reject a match because the GT and GEN test-case titles don't share words.
- Don't accept a match because titles share words but the underlying assertion differs (e.g., both say "invalid" but test different fields).
- Don't require GEN's `category` (`positive`/`negative`/`edge`) to match the GT section — a GT "Negative Test" can legitimately be covered by a GEN test filed under `edge`.
- Don't count a passing precondition or setup step as coverage of the behavior it's a precondition _for_.
- Don't let one strong generic test silently absorb multiple distinct GT boundaries — apply Rule 2 per boundary, not per feature.
