from dataclasses import dataclass

@dataclass(frozen=True)
class EvalItem:
    item_id: int
    question: str
    reference: str