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
        for row in reader :
            item = EvalItem(
                item_id= int(row["S.no"]),
                question= row["Question"].strip(),
                reference= row["Answer"].strip(),
            )
            items.append(item)
    return items