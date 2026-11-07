# Project State

## Scope (decided)
Evaluation reliability layer for LLM apps: judge-vs-human agreement,
bias probes, confidence intervals, and regression testing with
statistical significance. Test subject: a small RAG QA app.

## Environment
Windows, Python 3.12.10, venv in .venv, pytest 9.2.0 installed.
Budget: Rs 0 (free tiers only).

## Current milestone
M1: data model and runner. Step 1 (dataset loader) complete.

## Done
- Repo, structure, pyproject.toml, dev dependencies installed.
- 10-question starter dataset: data/eval/qa_v0.csv (needs 100+ later).
- src/reliab/dataset.py: EvalItem dataclass, load_items() with
  empty-field validation.
- tests/test_dataset.py: 6 tests passing.

## Next
Runner: send each question to an LLM and store the answers.
First decision: which free LLM API to use.

## Known issues
- Dataset Q3, Q4, Q8, Q10 are vague or open-ended (to be tagged by type).