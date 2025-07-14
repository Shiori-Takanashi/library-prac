from __future__ import annotations

from typing import Dict

from core.domain.book import Book
from core.domain.user import User


class Library:
    def __init__(self) -> None:
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}

    def register_book(self, book: Book) -> None:
        self.books[book.isbn] = book

    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user
