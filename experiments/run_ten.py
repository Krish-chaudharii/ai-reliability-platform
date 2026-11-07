from pathlib import Path

from reliab.dataset import load_items
from reliab.runner import run_eval

items = load_items(Path("data/eval/qa_v0.csv"))
results = run_eval(items, model="gemini-3.1-flash-lite")
for r in results:
    print(r.item_id, "|", r.reference, "|", r.answer)