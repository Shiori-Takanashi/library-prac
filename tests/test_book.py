import pytest

from core.domain.book import Book


def test_lend_and_return() -> None:
    book = Book("Test", "Author", "isbn1", 2)

    # 2 回まで貸出可
    book.lend()
    book.lend()
    assert book.borrowed == 2
    assert not book.is_available()

    # 3 回目は在庫切れ
    with pytest.raises(ValueError):
        book.lend()

    # 返却
    book.return_book()
    assert book.borrowed == 1
    book.return_book()
    assert book.borrowed == 0

    # 借りていないのに返却は例外
    with pytest.raises(ValueError):
        book.return_book()
