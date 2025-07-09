import random


class Book:
    def __init__(self):
        self.title: str | None = None
        self.author: str | None = None
        self.isbn: str | None = None
        self.total: int = 0

    def add_book(self, title: str, author: str, isbn: str, count: int) -> None:
        # 型チェック
        if not isinstance(title, str):
            raise TypeError(f"title must be str, got {type(title).__name__}")
        if not isinstance(author, str):
            raise TypeError(f"author must be str, got {type(author).__name__}")
        if not isinstance(isbn, str):
            raise TypeError(f"isbn must be str, got {type(isbn).__name__}")
        if not isinstance(count, int):
            raise TypeError(f"count must be int, got {type(count).__name__}")
        if count < 0:
            raise ValueError("count must be non-negative")

        # 整形
        title = title.strip()
        author = author.strip()
        isbn = isbn.strip()

        # 初回登録 or 一致確認
        if self.title is None:
            self.title = title
            self.author = author
            self.isbn = isbn
        else:
            if self.title != title or self.author != author or self.isbn != isbn:
                raise ValueError("Book attributes do not match existing record")

        self.total += count

    @classmethod
    def generate_fake_isbn13(cls) -> str:
        """ISBN-13風のダミー文字列を生成"""
        prefix = random.choice(["978", "979"])
        group = f"{random.randint(0, 5):01}"
        publisher = f"{random.randint(100, 999):03}"
        item = f"{random.randint(10000, 99999):05}"
        dummy_check_digit = random.randint(0, 9)
        return f"{prefix}-{group}-{publisher}-{item}-{dummy_check_digit}"
