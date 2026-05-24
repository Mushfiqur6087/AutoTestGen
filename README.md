# AutoTestGenX

![Python](https://img.shields.io/badge/python-3.9%2B-blue)

AutoTestGenX converts natural-language functional specifications into a deterministic UI Abstract Syntax Tree (UI-AST) and a structured test suite. It captures interactive elements only and produces machine-readable JSON for automated validation, coverage analysis, and test generation workflows.

## Highlights

- Deterministic UI-AST schema focused on interactive elements
- Critic-guided retries to reduce omissions and hallucinations
- Parallelized test generation for positive, negative, and edge cases
- Resumable runs with checkpointing and optional debug logs
- Provider-agnostic LLM routing via LiteLLM

## Architecture overview

```text
spec.md (## Module sections)
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│  AutoTestGenX Pipeline                                   │
│                                                          │
│  ┌─────────────────────────────────────────────────┐     │
│  │  [1/3] generate_and_critique (parallel)         │     │
│  │                                                 │     │
│  │  For each module (concurrent):                  │     │
│  │    attempt 1: UIASTAgent → SemanticCritic       │     │
│  │      verdict=yes  ───────────────────► done     │     │
│  │      verdict=retry → fixes[] fed back           │     │
│  │    attempt 2: UIASTAgent(fixes) → Critic        │     │
│  │      verdict=yes  ───────────────────► done     │     │
│  │      verdict=retry → fixes[] fed back           │     │
│  │    attempt 3: UIASTAgent(fixes) → ship as-is   │     │
│  └─────────────────────────────────────────────────┘     │
│                          ↓                               │
│  ┌─────────────────────────────────────────────────┐     │
│  │  [2/3] generate_tests (parallel, 3 calls each)  │     │
│  │                                                 │     │
│  │  For each module (concurrent):                  │     │
│  │    TestPositiveAgent  ┐                         │     │
│  │    TestNegativeAgent  ├─ parallel → merge       │     │
│  │    TestEdgeAgent      ┘                         │     │
│  └─────────────────────────────────────────────────┘     │
│                          ↓                               │
│  ┌──────────────────────────┐                            │
│  │  [3/3] finalize          │ → ui-ast.json              │
│  │                          │ → semantic-critique.json   │
│  │                          │ → test-cases.json          │
│  └──────────────────────────┘                            │
└──────────────────────────────────────────────────────────┘
```

**Stage 1 — UIASTAgent + SemanticCriticAgent** — For each module, the generator emits a UI component tree and the critic audits it with a binary `yes/retry` verdict. On retry, the critic's `fixes[]` array is fed directly back to the generator. Maximum 3 attempts per module.

**Stage 2 — Three test agents** — For each module, three agents run in parallel against the approved AST: positive tests (happy paths, state transitions, lifecycle flows), negative tests (validation failures, constraint violations, precondition violations), and edge/boundary tests (threshold boundaries, unusual interaction paths). Results are merged into a single per-module test suite with sequential TC IDs.

Modules run concurrently across all stages.

---

## Installation

```bash
git clone https://github.com/your-org/AutoTestGenX
cd AutoTestGenX
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Quick start

```bash
autotestgenx --generate \
  --input dataset/functional_descriptions/my-app-spec.md \
  --api-key "sk-..." \
  --model "openai/gpt-4o" \
  --output outputs/my-run
```

Outputs are written to `outputs/my-run/`:

- `ui-ast.json`
- `semantic-critique.json`
- `test-cases.json`

## Input format

The input is a markdown file. Each `##` heading becomes one module. A `## Navigation` section is extracted as metadata and not processed as a module.

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

## CLI reference

```bash
autotestgenx --generate --input SPEC --api-key KEY [options]
autotestgenx --resume RUN_ID --api-key KEY
```

| Flag | Default | Description |
| --- | --- | --- |
| `--input` / `-i` | - | Path to `.md` spec file (required for `--generate`) |
| `--api-key` | - | API key for the LLM provider |
| `--model` | `openai/gpt-4o` | LiteLLM model string with provider prefix |
| `--output` / `-o` | `outputs/autotestgenx/<project>/<model>/` | Output directory |
| `--baseline` | - | Write outputs to `outputs/baselines/<baseline>/<project>/<model>/` (`zero_shot` or `few_shot`) |
| `--max-concurrency` | `10` | Max concurrent in-flight LLM calls |
| `--debug` | off | Write per-stage debug logs to `<output>/debug/` |
| `--resume RUN_ID` | - | Resume an interrupted run from its checkpoint |
| `--version` | - | Print version and exit |

## LLM providers

All LLM calls go through [LiteLLM](https://github.com/BerriAI/litellm). The `--model` flag accepts any LiteLLM model string with a provider prefix:

```bash
# OpenAI
--model openai/gpt-4o
--model openai/gpt-4o-mini

# Anthropic
--model anthropic/claude-3-5-sonnet-20241022

# OpenRouter
--model openrouter/anthropic/claude-3.5-sonnet
--model openrouter/openai/gpt-4o

# GitHub Models
--model github/gpt-4o
```

The `--api-key` value is passed directly to LiteLLM and must match the provider.

## Output files

### ui-ast.json

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "modules": [
    {
      "module_id": 1,
      "module_title": "Clients",
      "ast": {
        "module_name": "Clients",
        "components": {
          "Clients_Table": {
            "type": "data_table",
            "sortable_columns": ["Name", "Status"],
            "row_actions": [
              { "action_name": "View" },
              { "action_name": "Deactivate", "preconditions": ["status must be Active"] }
            ],
            "bulk_actions": [{ "action_name": "Export" }]
          }
        }
      },
      "attempts": 1
    }
  ]
}
```

### semantic-critique.json

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "modules": [
    {
      "module_id": 1,
      "module_title": "Clients",
      "critique": {
        "verdict": "yes",
        "summary": "All interactive elements captured correctly.",
        "missing": [],
        "phantoms": [],
        "fixes": []
      },
      "forced_ship": false
    }
  ]
}
```

`forced_ship: true` means the module hit the 3-attempt cap and the final attempt was emitted. Check `critique.missing` and `critique.fixes` to guide prompt or spec refinements.

### test-cases.json

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "model": "openai/gpt-4o",
  "modules": [
    {
      "module": "Clients",
      "test_cases": [
        {
          "tc_id": "TC-001",
          "category": "positive",
          "test_case": "View client with all fields filled",
          "preconditions": ["User logged in", "At least one client exists"],
          "steps": ["Navigate to Clients page", "Click View on any row"],
          "expected_result": "Client detail page opens showing all client information",
          "priority": "high"
        },
        {
          "tc_id": "TC-010",
          "category": "negative",
          "test_case": "Attempt Deactivate on already Inactive client",
          "preconditions": ["User logged in", "Client in Inactive status"],
          "steps": ["Open client detail page", "Observe action bar"],
          "expected_result": "Deactivate action is not available",
          "priority": "high"
        },
        {
          "tc_id": "TC-015",
          "category": "edge",
          "subcategory": "interaction_edge",
          "test_case": "Double-click Export button on bulk selection",
          "preconditions": ["User logged in", "Multiple clients exist"],
          "steps": ["Select 3 clients via checkbox", "Double-click Export"],
          "expected_result": "Export triggered once, not twice",
          "priority": "low"
        }
      ],
      "summary": {
        "total": 18,
        "positive": 8,
        "negative": 6,
        "boundary": 2,
        "edge": 2,
        "high_priority": 10,
        "medium_priority": 6,
        "low_priority": 2
      }
    }
  ],
  "total_summary": {
    "total_modules": 1,
    "total_tests": 18,
    "positive": 8,
    "negative": 6,
    "boundary": 2,
    "edge": 2,
    "high_priority": 10,
    "medium_priority": 6,
    "low_priority": 2
  }
}
```

Each test case has `category` (`positive | negative | edge`) set automatically during merge. Edge test cases also carry `subcategory` (`boundary | input_edge | interaction_edge | state_edge | data_edge`). TC IDs are renumbered sequentially across all categories within each module.

---

## UI-AST schema

The AST captures **interactive elements only**. The critic enforces this — passive display labels ("the page shows the client name") produce zero expected items and are not emitted.

| Component type | Used for |
| --- | --- |
| `form` | Single-page forms with `fields` |
| `wizard` | Multi-step forms with `steps[]`, each step has `fields` |
| `tab_container` | Pages with `tabs[]`, each tab has `fields` and can nest more `tabs[]` |
| `data_table` | Tables with `row_actions[]`, `bulk_actions[]`, `sortable_columns[]` |
| `state_bound_action_bar` | Action buttons that change by entity state (Pending/Active/Closed) with `states{}` |
| `repeating_group` | Add-row patterns; has `item_fields{}`, optional `min`/`max` |

Field-level attributes: `type`, `required`, `required_when`, `visible_when`, `enabled_when`, `options[]`, `constraints[]`.

Action-level attributes: `on_success`, `preconditions[]`, `fields{}` (for modal/inline forms triggered by the action).

---

## Resumability

Every run gets a unique run ID (`<project>-YYYYMMDD-HHmmss-<6char>`). If a run is interrupted, resume it with:

```bash
autotestgenx --resume my-app-20260503-120000-abc123 --api-key "sk-..."
```

Checkpoints are stored in `outputs/.checkpoints/autotestgenx.sqlite`, with a sidecar file at `outputs/.checkpoints/<run-id>.json`.

## Debug logging

```bash
autotestgenx --generate --input spec.md --api-key "..." --model openai/gpt-4o \
  --output outputs/debug-run --debug
```

Log files are written to `<output>/debug/`:

| File | Contents |
| --- | --- |
| `01_ui_ast.log` | UIASTAgent prompt and raw response per call |
| `02_semantic_critic.log` | SemanticCriticAgent prompt and raw response per call |

## Docker

```bash
docker build -t autotestgenx .

docker run --rm \
  -v $(pwd)/outputs:/app/outputs \
  -v $(pwd)/dataset:/app/dataset \
  autotestgenx \
  --generate \
  --input dataset/functional_descriptions/my-spec.md \
  --api-key "sk-..." \
  --model openai/gpt-4o
```

## Project layout

```text
autotestgenx/
  cli.py
  framework/
    agents/
    orchestrator/
  prompts/
dataset/
outputs/
baselines/
```

## Datasets and baselines

- `dataset/functional_descriptions/` - Input markdown specs
- `dataset/ground_truth_test_cases/` - Reference UI-AST outputs for evaluation
- `baselines/` - Single-prompt and few-shot reference implementations

## Concurrency tuning

`--max-concurrency` controls how many LLM calls can be in-flight simultaneously. The default of 10 is safe for most providers. Lower it if you hit rate limits; raise it for providers with higher quotas. A single module can make up to 6 LLM calls (3 generator and 3 critic), but the concurrency cap bounds total in-flight requests.
