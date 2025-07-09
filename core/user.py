from typing import List


class User:
    def __init__(
        self, id: int, name: str, history: List[str], current_book: Book = None
    ):
        self.id = id
        self.name = name
        self.history = history
        self.current_book = current_book
