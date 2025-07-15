# core/domain/user.py

from typing import List


class User:
    def __init__(self, user_id: str, name: str, history: List[str]) -> None:
        self.user_id = user_id
        self.name = name
        self.history = history  # 操作履歴（"借用: ..." や "返却: ..."）
        self.borrowed_books: List[str] = []  # 現在借りているISBNリスト

    def borrow_book(self, isbn: str) -> None:
        if isbn in self.borrowed_books:
            raise ValueError(f"ISBN {isbn} の本はすでに借りています。")
        self.borrowed_books.append(isbn)
        self.history.append(f"借用: {isbn}")

    def return_book(self, isbn: str) -> None:
        if isbn not in self.borrowed_books:
            raise ValueError(f"ISBN {isbn} の本は借りていません。")
        self.borrowed_books.remove(isbn)
        self.history.append(f"返却: {isbn}")

    def current_borrowed(self) -> List[str]:
        return self.borrowed_books.copy()

    def get_history(self) -> List[str]:
        return self.history.copy()
