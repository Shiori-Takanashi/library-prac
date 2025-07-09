from core.book import Book
from core.user import User

from typing import List


class liblary:
    def __init__(self):
        self.booksinfo: List[Book] = None
        self.usesrinfo: List[User] = None

    def manage_book(self, title: str, author: str, isbn: str):
        book = Book.add_book(title=title, author=author, isbn=isbn)
        for bookinfo in booksinfo:
            if bookinfo.isbn == isbn:
                bookinfo.total = bookinfo.total + 1
