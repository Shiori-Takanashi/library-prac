# core/domain/library.py

from __future__ import annotations

from typing import Dict

from core.domain.book import Book
from core.domain.user import User


class Library:
    def __init__(self) -> None:
        self.books: Dict[str, Book] = {}  # isbn → Book
        self.users: Dict[str, User] = {}  # user_id → User

    def register_book(self, book: Book) -> None:
        self.books[book.isbn] = book

    def remove_book(self, isbn: str) -> None:
        if isbn not in self.books:
            raise ValueError(f"ISBN {isbn} の図書は存在しません。")
        del self.books[isbn]

    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user

    def remove_user(self, user_id: str) -> None:
        if user_id not in self.users:
            raise ValueError(f"ID {user_id} の利用者は存在しません。")
        del self.users[user_id]

    def lend_book(self, user_id: str, isbn: str) -> None:
        if user_id not in self.users:
            raise ValueError(f"ID {user_id} の利用者は存在しません。")
        if isbn not in self.books:
            raise ValueError(f"ISBN {isbn} の図書は存在しません。")
        book = self.books[isbn]
        user = self.users[user_id]
        book.lend()
        user.borrow_book(isbn)

    def return_book(self, user_id: str, isbn: str) -> None:
        if user_id not in self.users:
            raise ValueError(f"ID {user_id} の利用者は存在しません。")
        if isbn not in self.books:
            raise ValueError(f"ISBN {isbn} の図書は存在しません。")
        book = self.books[isbn]
        user = self.users[user_id]
        book.return_book()
        user.return_book(isbn)

    def list_books(self) -> Dict[str, Book]:
        return self.books

    def get_user_history(self, user_id: str) -> list[str]:
        if user_id not in self.users:
            raise ValueError(f"ID {user_id} の利用者は存在しません。")
        return self.users[user_id].history
