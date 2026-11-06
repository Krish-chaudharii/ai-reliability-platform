from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from reliab.dataset import EvalItem, load_items

DATA_PATH = Path(__file__).parent.parent / "data" / "eval" / "qa_v0.csv"


def test_eval_item_stores_reference() -> None:
    item = EvalItem(1, "What's the capital of India?", "New Delhi")
    assert item.reference == "New Delhi"


def test_eval_item_is_frozen() -> None:
    item = EvalItem(2, "What's the Region around India's Capital called?", "NCR")
    with pytest.raises(FrozenInstanceError):
        item.reference = "Mumbai"


def test_load_items_returns_ten_items() -> None:
    items = load_items(DATA_PATH)
    assert len(items) == 10


def test_load_items_strips_whitespace() -> None:
    items = load_items(DATA_PATH)
    assert items[0].reference == "New Delhi"