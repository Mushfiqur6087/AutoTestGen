# Baselines

Comparator approaches used as **ablations** in the AutoTestGenX evaluation.
Each subdirectory implements one prompting strategy that does **not** use the
multi-agent orchestration pipeline, so we can quantify how much of
AutoTestGenX's quality comes from agent decomposition vs. raw LLM capacity.

All baselines must:
1. Read a functional specification from
   `dataset/functional_descriptions/<project>/<spec>.md`.
2. Produce a `test-cases.json` matching the pipeline output schema used by
   AutoTestGenX so downstream evaluation stays consistent.
3. Write outputs under
   `outputs/<system>/<dataset>/<model>/test-cases.json` where `<system>` is the
   slug of the baseline directory (e.g. `zero_shot`, `few_shot`).

## Slugs

| Subdir              | System slug      | Status |
|---------------------|------------------|--------|
| `zero_shot/`        | `zero_shot`      | stub   |
| `few_shot/`         | `few_shot`       | stub   |
