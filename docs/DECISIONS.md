# Decisions

## D1: Scope is Option D (evaluation reliability layer)
Why: avoids duplicating Ragas/DeepEval, matches research interest in
judge reliability and statistics. Alternatives rejected: general eval
runner (duplicate), RAG-only suite (Ragas covers it), agent eval
(too costly for 3.5 h/week).

## D2: Python 3.12
Why: safer library compatibility than 3.14.