# Decisions

## D1: Scope is Option D (evaluation reliability layer)
Why: avoids duplicating Ragas/DeepEval, matches research interest in
judge reliability and statistics. Alternatives rejected: general eval
runner (duplicate), RAG-only suite (Ragas covers it), agent eval
(too costly for 3.5 h/week).

## D2: Python 3.12
Why: safer library compatibility than 3.14.

## D3: LLM provider is the Gemini API free tier
Why: Rs 0 budget. Limits seen in AI Studio: Flash Lite models 15 RPM /
500 RPD; Gemma 4 models 30 RPM / 14.4K RPD. Pro models unavailable on
free tier. Model names will live in config, not hard-coded, because
free-tier availability changes.