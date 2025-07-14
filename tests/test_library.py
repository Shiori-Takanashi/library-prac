from core.domain.book import Book
from core.domain.library import Library
from core.domain.user import User


def test_register_book_and_user(sample_book: Book, sample_user: User) -> None:
    lib = Library()
    lib.register_book(sample_book)
    lib.register_user(sample_user)

    assert lib.books["123"].title == "吾輩は猫である"
    assert lib.users["u1"].name == "山田 太郎"
