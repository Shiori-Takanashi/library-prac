# core/domain/book.py


class Book:
    def __init__(self, title: str, author: str, isbn: str, total: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total = total
        self.borrowed = 0  # 現在の貸出中数

    def is_available(self) -> bool:
        return self.borrowed < self.total

    def lend(self) -> None:
        if not self.is_available():
            raise ValueError(f"『{self.title}』は在庫がありません。")
        self.borrowed += 1

    def return_book(self) -> None:
        if self.borrowed == 0:
            raise ValueError(f"『{self.title}』は現在誰にも貸し出されていません。")
        self.borrowed -= 1

    def stock_status(self) -> str:
        return f"{self.title}（在庫: {self.total - self.borrowed} / {self.total}）"
