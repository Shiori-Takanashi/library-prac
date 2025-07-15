# core/infra/factory.py

from typing import Any, Callable, Dict, List, TypeVar

from core.domain.book import Book
from core.domain.user import User

T = TypeVar("T", Book, User)


def make_book_instance(entry: Dict[str, Any]) -> Book:
    return Book(
        title=entry["title"],
        author=entry["author"],
        isbn=entry["isbn"],
        total=int(entry["total"]),
    )


def make_user_instance(entry: Dict[str, Any]) -> User:
    return User(
        user_id=entry["id"],
        name=f"{entry['last_name']} {entry['first_name']}",
        history=entry.get("history", []),
    )


def register_entities(
    info: List[Dict[str, Any]],
    registry: Dict[str, T],
    factory: Callable[[Dict[str, Any]], T],
) -> None:
    """
    Book または User のリストを登録辞書に一括登録する。

    Parameters:
        info: JSON等から読み込んだ辞書のリスト
        registry: 登録先の辞書（isbnやuser_idをキーとする）
        factory: Book か User を生成する関数
    """
    for entry in info:
        instance = factory(entry)
        if isinstance(instance, Book):
            registry[instance.isbn] = instance
        elif isinstance(instance, User):
            registry[instance.user_id] = instance
