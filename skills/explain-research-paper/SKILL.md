---
name: explain-research-paper
description: Read a local research-paper PDF and create clear Markdown learning material, including a comprehensive paper explanation and/or a second step-by-step input/output walkthrough with concrete examples. Use when the user asks to understand, study, summarize in depth, explain methodology, identify inputs and outputs, trace a pipeline, reproduce prompts, or turn a technical or scientific PDF into beginner-friendly notes.
---

# Explain Research Paper

Create accurate, self-contained learning documents from a research-paper PDF. Explain both what the paper claims and how its method transforms inputs into outputs.

## Select the deliverables

Infer the requested deliverables from the user. Unless the user specifies different names, write next to the PDF:

- `<paper-stem>-explained.md` for the comprehensive learning guide.
- `<paper-stem>-step-by-step-input-output.md` for the operational walkthrough.

If the user requests both, create both. If they request only one, do not create the other. Preserve an existing document's useful content when revising it.

## Read and inspect the paper

1. Locate the exact PDF requested by the user. If "first paper" is ambiguous, use the first paper in their stated order or open tabs; otherwise ask.
2. Read the complete relevant paper, including appendices when they affect the method or results.
3. Extract title, authors, version/date, abstract, headings, equations, algorithms, figures, tables, footnotes, sample sizes, metrics, limitations, and artifact links.
4. Visually inspect pages containing architecture diagrams, algorithms, prompt screenshots, and important tables. Text extraction alone can lose arrows, grouping, formatting, subscripts, and table structure.
5. Cross-check all quoted numbers and central claims against the PDF before writing.
6. Do not browse for outside explanations unless the user requests it or a claim requires current verification. Keep paper claims separate from external context.

## Track evidence while reading

Build a scratch map before drafting:

```text
Problem:
External inputs:
Intermediate artifacts:
Final outputs:
Pipeline steps:
Who performs each step (LLM/code/parser/solver/human):
Training-time behavior:
Inference-time behavior:
Prompts actually printed:
Prompts only described:
Datasets and sample sizes:
Metrics:
Main results:
Limitations and failure modes:
```

Resolve contradictions between prose, figures, and tables. If the paper is ambiguous, state the ambiguity rather than silently choosing an interpretation.

## Create the comprehensive learning guide

Make the guide useful without reopening the PDF. Prefer this structure when applicable:

1. Paper at a glance
2. Problem and motivation
3. Exact external inputs, intermediate artifacts, and final outputs
4. System architecture or conceptual model
5. Methodology in execution order
6. Training versus inference behavior
7. Worked example from the paper
8. Dataset and experimental setup
9. Metrics, including plain-language interpretations
10. Results and what they mean
11. Contributions
12. Assumptions, limitations, threats to validity, and failure modes
13. Reproduction outline
14. Compact mental model
15. Glossary

Adapt the headings to the paper. Do not force irrelevant sections.

### Explain technical content

- Define every important symbol before using it.
- Explain equations in words and state what each quantity measures.
- Distinguish a proposed method from an evaluation-only procedure.
- Distinguish ground-truth or oracle components from deployable components.
- State whether the work trains/fine-tunes a model or orchestrates existing models at inference time.
- Explain why each component exists, not merely what it is named.
- Interpret results rather than copying tables without commentary.

### Use Markdown-safe notation

Assume a standard Markdown preview without MathJax unless the user requests LaTeX. Avoid raw constructs such as `\[...\]` and `\(...\)`.

Use readable text blocks instead:

```text
Precision = correctly predicted positive cases / all predicted positive cases
```

Use inline code for symbols such as `s`, `R1`, and `D_sat`.

## Create the step-by-step input/output guide

Use one running example grounded in the paper. Prefer an actual example, input, or case study used by the authors.

At the beginning, state which parts are:

- directly shown in the paper;
- faithfully paraphrased from the paper;
- pedagogical reconstructions created to make the workflow concrete.

For every pipeline step, include these subsections:

```markdown
## Step N - Descriptive name

### Who performs this step
LLM, normal program code, parser, solver, model, human, or a combination.

### Input
Concrete input using the running example.

### How this step is done, simply
Numbered explanation of the mechanism.

### Prompt used
Only when an LLM performs the step. State prompt provenance.

### Output
Concrete output passed to the next step.

### Failure or alternate branch
Include when it changes downstream behavior.
```

Do not merely repeat "input" and "output." Explain the transformation connecting them.

### Identify the actor precisely

Use accurate language:

- **LLM:** interprets natural language, generates code, proposes data, or produces a classification.
- **Normal program code:** groups inputs, fills templates, routes results, counts attempts, saves state, and merges artifacts.
- **Parser/interpreter:** checks syntax or executes generated code.
- **Formal solver:** searches for a model, proves unsatisfiability, or returns unknown.
- **Human:** constructs labels, reference implementations, annotations, or evaluation samples.

Do not attribute deterministic list operations or arithmetic to an LLM.

### Cover all terminal paths

Trace every final state supported by the method, such as:

- successful positive result plus generated artifact;
- successful negative result;
- validation failure followed by feedback and retry;
- timeout or unknown result;
- retry-budget exhaustion and fallback selection.

Finish with a compact component contract table:

| Component | Actor | Input | Transformation | Output |
|---|---|---|---|---|

## Handle prompts accurately

For each LLM step, determine which of these cases applies.

### Exact prompt printed

If the paper prints a complete prompt, reproduce it accurately and identify its figure, table, appendix, or section. Preserve placeholders and explain how they are filled.

### Prompt-template excerpt printed

If the paper shows only an excerpt, label it **prompt-template excerpt**. Preserve visible omissions or ellipses. Do not call it the complete prompt.

### Prompt structure described only

If the authors describe ingredients but do not print the prompt, list those ingredients. An example reconstruction may be useful, but label it **illustrative reconstruction**.

### No prompt information

Say that the paper does not provide the prompt. Do not invent one unless a reconstruction clearly improves learning, and never present the reconstruction as author-provided text.

### System/user role distinction

Do not call text a "system prompt" unless the paper explicitly assigns it to the system role. Papers often use "prompt" to mean the complete request without revealing API message roles. State this limitation clearly.

For reconstructed prompts:

- use only details supported by the method description;
- mark invented role wording and output schemas;
- avoid implying experimental use;
- separate the reconstruction visually from actual paper text.

## Use examples responsibly

- Prefer exact examples and values printed in the paper.
- State when code or a trace is reconstructed for teaching.
- Make reconstructed examples logically consistent with the method.
- Do not claim a reconstructed trace was observed in the experiment.
- When demonstrating code, keep interfaces faithful to the paper even if implementation details are simplified.
- When presenting formal expressions, mention whether they are exact paper expressions or pedagogical equivalents.

## Report experiments accurately

- Preserve dataset sizes, class distributions, timeouts, retry budgets, temperature settings, and model names when relevant.
- Define each metric before reporting it.
- Separate baseline, oracle/ground-truth, and end-to-end results.
- Do not infer exact values from a plot when only approximate values are visible; label approximations.
- Explain class imbalance and why the authors chose separate metrics when applicable.
- Report threats to internal, external, and construct validity when the paper discusses them.

## Quality checks

Before delivery:

1. Confirm every created link resolves.
2. Confirm Markdown code fences are balanced.
3. Search for unsupported LaTeX delimiters, unfinished drafting markers, unresolved placeholders, and tool tokens.
4. Confirm every major pipeline step states actor, input, mechanism, and output.
5. Confirm every LLM step states prompt provenance.
6. Confirm reconstructed material is labeled.
7. Confirm numerical claims against the source PDF.
8. Run `git diff --check` when working in a Git repository.
9. Keep temporary extraction or rendering files out of the final deliverables.

## Final response

Link each created Markdown file with an absolute clickable path. Briefly state what each contains and disclose important source limitations, such as unavailable complete prompts. Cite the source PDF according to the active PDF-handling instructions.
