from reliab.dataset import EvalItem
import pytest
from dataclasses import FrozenInstanceError

def test_eval_item_stores_reference() -> None:
    item = EvalItem(1, "What's the capital of India?", "New Delhi")
    assert item.reference == "New Delhi"

def test_eval_item_is_frozen() -> None:
    item = EvalItem(2, "What's the Region around India's Capital called?", "NCR (National Capital region)")
    with pytest.raises(FrozenInstanceError):
        item.reference = "Indian NCR (National Capital region)"