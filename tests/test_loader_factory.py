import json
from pathlib import Path
from typing import Any, Dict, List

from core.domain.book import Book
from core.domain.user import User
from core.infra.factory import make_book_instance, make_user_inctance, register_entities
from core.infra.loader import load_entities


def test_load_entities(tmp_path: Path) -> None:
    data = [{"foo": "bar"}]
    f = tmp_path / "data.json"
    f.write_text(json.dumps(data), "utf-8")

    result: List[dict] = load_entities(f)
    assert result == data


def test_make_book_and_register() -> None:
    entry = {"title": "A", "author": "B", "isbn": "123", "total": "2"}
    book = make_book_instance(entry)
    assert isinstance(book, Book)
    assert book.total == 2

    registry: dict[str, Book] = {}
    register_entities([entry], registry, make_book_instance)
    assert registry["123"].title == "A"


def test_make_user_and_register() -> None:
    entry: Dict[str, Any] = {
        "id": "u1",
        "last_name": "山田",
        "first_name": "太郎",
        "history": [],
    }
    user = make_user_inctance(entry)
    assert isinstance(user, User)
    assert user.name == "山田 太郎"

    registry: dict[str, User] = {}
    register_entities([entry], registry, make_user_inctance)
    assert registry["u1"].user_id == "u1"
