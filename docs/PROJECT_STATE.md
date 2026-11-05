# Project State

## Scope (decided)
Evaluation reliability layer for LLM apps: judge-vs-human agreement,
bias probes, confidence intervals, and regression testing with
statistical significance. Test subject: a small RAG QA app.

## Environment
Windows, Python 3.12.10, venv in .venv, pytest 9.2.0 installed.
Budget: Rs 0 (free tiers only).

## Current milestone
M1: data model and runner. Step 1: EvalItem dataclass + load_items().

## Done
- Repo, structure, pyproject.toml, dev dependencies installed.
- 10-question starter dataset: data/eval/qa_v0.csv (needs 100+ later).

## Next
Write src/reliab/dataset.py and tests/test_dataset.py.

## Known issues
- Dataset Q3, Q4, Q8, Q10 are vague or open-ended (to be tagged by type).