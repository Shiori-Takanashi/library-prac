from typing import List


class User:
    def __init__(self, user_id: str, name: str, history: List[str]):
        self.user_id = user_id
        self.name = name
        self.history = history
        self.borrowed_books: List[str] = []  # 現在借りている本のISBNリスト

    def borrow_book(self, isbn: str) -> None:
        """本を借りる"""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            self.history.append(f"借用: {isbn}")

    def return_book(self, isbn: str) -> None:
        """本を返す"""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            self.history.append(f"返却: {isbn}")
        else:
            raise ValueError(f"ISBN {isbn} の本は借りていません。")
