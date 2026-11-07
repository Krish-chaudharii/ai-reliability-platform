from dataclasses import dataclass

from reliab.dataset import EvalItem
from reliab.llm import ask_model

@dataclass(frozen=True)
class RunResult:
    item_id: int
    question: str
    reference: str
    answer: str
    model: str

def run_eval(items: list[EvalItem], model: str) -> list[RunResult]:
    results: list[RunResult] = []
    for item in items:
        answer = ask_model(item.question, model= model)
        results.append(
            RunResult(
                item_id=item.item_id,
                question=item.question,
                reference=item.reference,
                answer=answer.strip(),
                model=model,
            )
        )
    return results