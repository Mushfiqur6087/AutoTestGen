# Zero-Shot Baseline (stub)

Zero-shot baseline: one LLM call, full functional specification in the prompt,
JSON test cases out. No agents, no decomposition, no graph.

## Planned interface

```bash
python -m baselines.zero_shot \
  --input dataset/functional_descriptions/Parabank/Parabank.md \
  --api-key "$OPENAI_API_KEY" \
  --provider openai \
  --model gpt-4o
```

Writes to `outputs/zero_shot/<project>/<model>/test-cases.json`.

## Implementation notes

- Reuse `autotestgenx.framework.agents.base.BaseAgent` for the HTTP call so
  provider/model handling stays consistent across systems.
- The prompt should ask the LLM for the same `TestSuiteOutput` schema the
  framework emits, so existing exporters round-trip without modification.
- No retry / repair loop. The point of the baseline is to expose what a single
  unsupervised call gives you.

**Status:** stub. Implementation deferred — the directory exists so paths and
README references are stable while the framework is exercised first.
