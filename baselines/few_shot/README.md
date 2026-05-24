# Few-Shot Baseline (stub)

Same shape as the zero-shot baseline, but with **k in-context exemplars**
sourced from `dataset/ground_truth_test_cases/`. Tests how much of the gap between
zero-shot and AutoTestGenX is closed simply by giving the model concrete
examples of well-formed test cases.

## Planned interface

```bash
python -m baselines.few_shot \
  --input dataset/functional_descriptions/Parabank/Parabank.md \
  --shots dataset/ground_truth_test_cases/Mifos.md dataset/ground_truth_test_cases/Parabank.md \
  --k 3 \
  --api-key "$OPENAI_API_KEY" \
  --provider openai \
  --model gpt-4o
```

Writes to `outputs/few_shot/<project>/<model>/test-cases.json`.

## Implementation notes

- Sample exemplars from `dataset/ground_truth_test_cases/` excluding the project under
  test (no train/test leakage).
- Document `k` and the exemplar selection method in the paper — both matter for
  reproducibility.
- Reuse `autotestgenx.framework.agents.base.BaseAgent` for the LLM call.

**Status:** stub.
