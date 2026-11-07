import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class EvalItem:
    item_id: int
    question: str
    reference: str

def load_items(path: Path) -> list[EvalItem]:
    items: list[EvalItem] = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for line_number, row in enumerate(reader, start=2):
            question = row["Question"].strip()
            reference = row["Answer"].strip()
            if not question or not reference:
                raise ValueError(
                    f"Row on line {line_number} has an empty question or answer"
                )
            item = EvalItem(
                item_id = int(row["S.no"]),
                question = question,
                reference = reference,
            )
            items.append(item)
    return items