# Test Generation

> Convert natural-language functional specifications into structured, machine-readable Structural Models, enumerate every executable workflow path, and generate comprehensive positive, negative, and edge test cases — fully automatically.

---

## How It Works

A functional spec markdown file goes in; structured JSON and human-readable markdown reports come out.

```
spec.md  (## Module sections)
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Test Generation Pipeline  (--generate)                             │
│                                                                     │
│  [0/4] extract_module_context (all modules run concurrently)        │
│  │                                                                  │
│  │  For each module:                                                │
│  │    ModuleContextExtractorAgent ──► context block                 │
│  │                           ↓                                      │
│  [1/4] generate_and_critique  (all modules run concurrently)        │
│  │                                                                  │
│  │  For each module:                                                │
│  │    attempt 1: StructuralModelGeneratorAgent ──► StructuralModelValidatorAgent  │
│  │      verdict=yes  ────────────────────────────────────► done    │
│  │      verdict=retry → fixes[] fed back                           │
│  │      verdict=needs_clarification ─────────────────────► abort   │
│  │    attempt 2: StructuralModelGeneratorAgent(fixes) ──► Validator │
│  │      verdict=yes  ────────────────────────────────────► done    │
│  │    attempt 3: StructuralModelGeneratorAgent(fixes) ──► escalate │
│  │                           ↓                                     │
│  [2/4] extract_workflows  (all modules run concurrently)            │
│  │                                                                  │
│  │  For each module:                                                │
│  │    attempt 1: WorkflowExtractorAgent ──► WorkflowValidatorAgent  │
│  │      verdict=yes  ────────────────────────────────────► done    │
│  │    attempt 2/3: same retry loop (max 3)                         │
│  │                           ↓                                     │
│  [3/4] generate_tests  (all modules run concurrently)               │
│  │                                                                  │
│  │  For each module (three agents in parallel per module):          │
│  │    PositiveTestCaseGeneratorAgent  ┐                             │
│  │    NegativeTestCaseGeneratorAgent  ├── parallel ──► merge        │
│  │    EdgeTestCaseGeneratorAgent      ┘                             │
│  │    (each receives the approved workflow list)                    │
│  │                           ↓                                     │
│  [4/4] finalize  ──► write JSON + markdown reports                  │
└─────────────────────────────────────────────────────────────────────┘
```

**Stage 0 — ModuleContextExtractorAgent** — For each module, synthesizes a global context block using the application navigation overview and the full module list to prevent precondition hallucination in later stages.

**Stage 1 — StructuralModelGeneratorAgent + StructuralModelValidatorAgent** — For each module, the generator emits a UI component tree and the validator audits it with a `yes`, `retry`, or `needs_clarification` verdict. On retry, the validator's `fixes[]` array is injected directly into the generator's system prompt for the next attempt. Maximum 3 attempts per module, escalating with a severity-tagged report if exhausted.

**Stage 2 — WorkflowExtractorAgent + WorkflowValidatorAgent** — For each module, the extractor enumerates every distinct executable path through the module (one workflow per submit action, per state × action pair, per table row/bulk action, per conditional branch). The validator audits for missing paths, phantom workflows, and wrong terminal actions — with the same `yes/retry/needs_clarification` verdict rules and 3-attempt retry loop.

**Stage 3 — Three test agents** — For each module, three agents run in parallel against both the approved Structural Model and the workflow list: positive tests (must cover every workflow), negative tests (workflow-aware failure injection), and edge/boundary tests (workflow-aware boundary scoping). Each test case carries a `wf_ref` linking it back to the workflow it covers. Results are merged into a single per-module test suite with sequential TC IDs.

All modules run concurrently across all stages.

---

## Installation

**Requirements:** Python 3.9+

```bash
git clone https://github.com/Mushfiqur6087/AutoTestGenX
cd "AutoTestGenX/Test Generation"
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -e .
```

---

## Configuration

Copy `.env.example` to `.env` and fill in your keys:

```env
# LLM API Keys (used by LiteLLM — provide the key matching your chosen --model)
OPENAI_API_KEY="sk-..."
ANTHROPIC_API_KEY="sk-ant-..."
GEMINI_API_KEY="..."

# Optional: local model base URL (e.g. Ollama, vLLM)
# OPENAI_API_BASE="http://localhost:11434/v1"

# Enable debug logging by default
DEBUG=True

# Default model for baseline scripts
MODEL="openai/gpt-4o"
```

Keys in `.env` are picked up automatically; you can also pass `--api-key` directly on the command line.

---

## Quick Start

### Minimal command

```bash
test-generation --generate \
  --input dataset/raw_specifications/Mifos/Mifos.md \
  --api-key "$OPENAI_API_KEY" \
  --model "openai/gpt-4o"
```

Output is written to `outputs/test_generation/Mifos/openai-gpt-4o/`.

### Full command with all options

```bash
test-generation --generate \
  --input dataset/raw_specifications/Mifos/Mifos.md \
  --api-key "$OPENAI_API_KEY" \
  --model "openai/gpt-4o" \
  --output outputs/my-run \
  --type positive negative edge \
  --max-concurrency 10 \
  --debug
```

## CLI Reference

### Test Generation

```
test-generation --generate --input SPEC --api-key KEY [options]
test-generation --resume RUN_ID --api-key KEY
```

| Flag | Default | Description |
|------|---------|-------------|
| `--input` / `-i` | — | Path to `.md` spec file (required for `--generate`) |
| `--api-key` | — | API key for the LLM provider |
| `--model` | `openai/gpt-4o` | LiteLLM model string with provider prefix |
| `--output` / `-o` | `outputs/test_generation/<project>/<model>/` | Output directory |
| `--type` | all | Subset of test types: `positive`, `negative`, `edge` |
| `--max-concurrency` | `10` | Max concurrent in-flight LLM calls |
| `--debug` | off | Write per-stage LLM logs to `<output>/debug/` |
| `--resume RUN_ID` | — | Resume an interrupted run from its checkpoint |
| `--version` | — | Print version and exit |

## LLM Providers

All LLM calls go through [LiteLLM](https://github.com/BerriAI/litellm). The `--model` flag accepts any LiteLLM model string with a provider prefix:

```bash
# OpenAI
--model openai/gpt-4o
--model openai/gpt-4o-mini

# Anthropic
--model anthropic/claude-3-5-sonnet-20241022

# Google Gemini
--model gemini/gemini-2.0-flash

# OpenRouter (proxies 100+ models)
--model openrouter/anthropic/claude-3.5-sonnet
--model openrouter/openai/gpt-4o

# GitHub Models
--model github/gpt-4o
```

The `--api-key` value is passed directly to LiteLLM and must match the provider. Parameters unsupported by a given model (e.g. `temperature` on `o`-series models) are silently dropped — no manual per-model configuration needed.

---

## Input Format

The input is a markdown file. Each `## ` heading becomes one module. A `## Navigation` section is extracted as metadata and not processed as a module.

```markdown
# My Application

## Navigation
Sidebar with links to Clients, Reports, Settings.

## Clients
The Clients page is a data table with columns Name, Status, Account Number.
Rows have a three-dot menu with View and Deactivate (only when Status is Active).
A checkbox column enables bulk Export. The table is sortable by Name and Status.

## Create Client
A wizard with 3 steps: Basic Info, Contact, Review.
Step 1 collects First Name (required), Last Name (required), Email (required, must be valid email).
Step 2 collects Phone, Address (required).
Step 3 is read-only review. Submit creates the client in Pending status.
```

The file stem (e.g. `my-app-spec`) becomes the project name in the output.

---


---

## Resumability

Every `--generate` run gets a unique run ID (`<project>-YYYYMMDD-HHmmss-<6char>`). If a run is interrupted mid-pipeline, resume it with:

```bash
test-generation --resume mifos-20260503-120000-abc123 --api-key "sk-..."
```

The run ID is printed at the start of every `--generate` invocation. Checkpoints are stored in `outputs/.checkpoints/test_generation.sqlite`; sidecar metadata (original inputs) lives in `outputs/.checkpoints/<run-id>.json`.

---

## Debug Mode

```bash
test-generation --generate \
  --input spec.md \
  --api-key "..." \
  --model openai/gpt-4o \
  --output outputs/debug-run \
  --debug
```

With `--debug`, per-module log files are written to `outputs/debug-run/debug/<Module_Name>/`:

| File | Contents |
|------|----------|
| `01_structural_model.log` | System prompt, user prompt, and raw LLM response for every `StructuralModelGeneratorAgent` call |
| `02_structural_model_validator.log` | Same for every `StructuralModelValidatorAgent` call |
| `02b_workflow_extractor.log` | Same for every `WorkflowExtractorAgent` call |
| `02c_workflow_validator.log` | Same for every `WorkflowValidatorAgent` call |
| `03_positive_test_case_generator.log` | Same for every `PositiveTestCaseGeneratorAgent` call |
| `04_negative_test_case_generator.log` | Same for every `NegativeTestCaseGeneratorAgent` call |
| `05_edge_test_case_generator.log` | Same for every `EdgeTestCaseGeneratorAgent` call |

Useful for diagnosing why a validator keeps retrying, why a workflow is missing, or why a test case lacks a `wf_ref`.

---

## Project Structure

```
AutoTestGenX/
├── test_generation/              # Installable Python package
│   ├── cli.py                         # CLI entry point (argparse)
│   ├── __main__.py                    # Enables python -m test_generation
│   ├── framework/
│   │   ├── agents/
│   │   │   ├── base.py                # BaseAgent — LiteLLM wrapper, semaphore, debug logging
│   │   │   ├── utils.py               # Shared build_test_prompt() utility (Stage 3)
│   │   │   ├── structural_model_generator.py
│   │   │   ├── structural_model_validator.py
│   │   │   ├── workflow_extractor.py
│   │   │   ├── workflow_validator.py
│   │   │   ├── positive_test_case_generator.py
│   │   │   ├── negative_test_case_generator.py
│   │   │   ├── edge_test_case_generator.py
│   │   └── orchestrator/
│   │       ├── generator.py           # TestGenerationPipeline — drives LangGraph
│   │       ├── graph.py               # LangGraph node wiring
│   │       ├── nodes.py               # Node implementations (async fan-out per module)
│   │       ├── state.py               # PipelineState TypedDict
│   │       ├── reporters.py           # Markdown report renderers
│   │       └── runs.py                # Run-ID generation, sidecar, checkpoint helpers
│   └── prompts/                       # System prompt markdown files (one per agent)
│       ├── structural_model_generator.md
│       ├── structural_model_validator.md
│       ├── workflow_extractor.md
│       ├── workflow_validator.md
│       ├── positive_test_case_generator.md
│       ├── negative_test_case_generator.md
│       ├── edge_test_case_generator.md
│
├── dataset/
│   ├── raw_specifications/            # Input markdown spec files
│   │   ├── Mifos/
│   │   ├── Moodle/
│   │   ├── Parabank/
│   │   ├── SwagLab/
│   │   └── PHPTravels/
│   └── ground_truth/                  # Manually curated gold-standard test suites
│       ├── Mifos.md
│       ├── MoodleStudent.md
│       ├── MoodleTeacher.md
│       ├── Parabank.md
│       ├── Phptravels.md
│       └── Swaglab.md
│
├── baselines/                         # Zero-shot and few-shot baseline runners
│   ├── zero_shot/
│   └── few_shot/
│
├── outputs/                           # Generated artifacts (git-ignored)
│   ├── test_generation/
│   └── .checkpoints/                  # SQLite checkpoint DB + run sidecars
│
├── docs/
│   ├── architecture.md                # System design, state management, concurrency model
│   ├── agents.md                      # Per-agent input/output/param reference
│   ├── pipeline.md                    # Step-by-step walkthrough of a real execution
│   └── data_models.md                 # Full JSON schemas for all output files
│
├── .env.example                       # Environment variable template
├── pyproject.toml                     # Package metadata and dependencies
└── README.md                          # This file
```

---

## Dataset and Baselines

The `dataset/` directory contains five real-world open-source web applications used for evaluation:

| Application | Domain | Modules | Ground Truth TCs |
|-------------|--------|---------|-----------------|
| **Mifos** | Microfinance / core banking (Apache Fineract) | 6 | ~200 |
| **Moodle (Teacher)** | Learning management — teacher role | 8 | ~130 |
| **Moodle (Student)** | Learning management — student role | 7 | ~136 |
| **Parabank** | Online banking demo | 5 | ~70 |
| **PHPTravels** | Travel booking platform | 6 | ~80 |
| **SwagLab** | E-commerce demo (Sauce Labs) | 4 | ~45 |

Ground truth test suites in `dataset/ground_truth/` are manually curated and serve as the reference for evaluating agent-generated test suite coverage and precision.

`baselines/` contains single-prompt (zero-shot) and few-shot reference implementations for ablation studies. See `baselines/README.md` for usage.

---

## Structural Model Schema

The AST captures **interactive elements only**. The validator enforces this — passive display labels produce no AST nodes.

| Component type | Used for |
|---|---|
| `form` | Single-page forms with `fields{}` |
| `wizard` | Multi-step forms with `steps[]`, each step has `fields{}` |
| `tab_container` | Pages with `tabs[]`, each tab has `fields{}` and can nest more `tabs[]` |
| `data_table` | Tables with `row_actions[]`, `bulk_actions[]`, `sortable_columns[]` |
| `state_bound_action_bar` | Action buttons that change by entity state (Pending/Active/Closed) with `states{}` |
| `repeating_group` | Add-row patterns; has `item_fields{}`, optional `min`/`max` |

Field-level attributes: `type`, `required`, `required_when`, `visible_when`, `enabled_when`, `options[]`, `constraints[]`

Action-level attributes: `on_success`, `preconditions[]`, `fields{}` (for modal/inline forms triggered by the action)

---

## Workflow Extraction

The workflow extractor enumerates distinct paths based on AST node type:

| AST node type | What is enumerated |
|---|---|
| `form` with no conditionals | One workflow per `submit_actions[]` entry |
| `form` with `visible_when` fields | One workflow per unique conditional branch × submit action |
| `wizard` | One workflow per distinct step sequence or `submit_actions[]` entry |
| `state_bound_action_bar` | One workflow per state × available action |
| `data_table` | One workflow per `row_actions[]` entry + one per `bulk_actions[]` entry |
| `tab_container` | One workflow per tab containing a form with a submit action |
| `repeating_group` | Not a standalone source — part of the form workflow that activates it |

The `WorkflowValidatorAgent` checks for: missing form submit paths, missing state × action pairs, missing table row/bulk actions, phantom workflows, wrong terminal action names, bad conditional field references, and zero-workflow failures.

---

## Test Agent Workflow Obligations

Each Stage 3 agent receives the approved workflow list as a compact `<workflows>` block appended to its prompt.

**PositiveTestCaseGeneratorAgent** — must collectively cover every workflow: at least one TC per `wf_id` that activates its `conditional_branch` and asserts its `on_success`.

**NegativeTestCaseGeneratorAgent** — for each workflow with a form interaction, identifies the most critical blocking failure for that workflow's branch. Adds one negative TC only when it catches a bug not covered by any other workflow's negative test.

**EdgeTestCaseGeneratorAgent** — for each workflow where `conditional_branch` activates a numeric or date field with a boundary, generates or confirms a boundary edge TC for it.

---

## Concurrency Tuning

`--max-concurrency` controls how many LLM calls can be in-flight simultaneously across all modules and stages. The default of 10 is safe for most providers. Lower it if you hit rate limits; raise it for providers with high per-minute token quotas.

### Test Generation pipeline

A single module can make up to **10 LLM calls** at peak:
- Stage 1: up to 3 `StructuralModelGeneratorAgent` + 3 `StructuralModelValidatorAgent` calls (if all retries are used)
- Stage 2: up to 3 `WorkflowExtractorAgent` + 3 `WorkflowValidatorAgent` calls
- Stage 3: 3 test agent calls (positive, negative, edge) in parallel

With `--max-concurrency 10` and 5 modules, peak concurrency is bounded at 10 regardless of how many modules are retrying simultaneously.

## Further Reading

| Document | Contents |
|----------|----------|
| [docs/architecture.md](docs/architecture.md) | System design, LangGraph node graph, concurrency model, state management, error handling, and resumability |
| [docs/agents.md](docs/agents.md) | Per-agent role, input context, expected output schema, and LLM parameters |
| [docs/pipeline.md](docs/pipeline.md) | Step-by-step walkthrough of a real run using the Mifos "Client Management" module |
| [docs/data_models.md](docs/data_models.md) | Full JSON schemas for all output files and internal data structures |
