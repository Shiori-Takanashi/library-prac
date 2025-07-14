import pytest

from core.domain.user import User


def test_borrow_and_return_history() -> None:
    user = User("u1", "山田 太郎", history=[])

    user.borrow_book("isbn1")
    assert "isbn1" in user.borrowed_books
    assert user.history[-1] == "借用: isbn1"

    # 二重登録されない
    user.borrow_book("isbn1")
    assert user.borrowed_books.count("isbn1") == 1

    # 返却
    user.return_book("isbn1")
    assert "isbn1" not in user.borrowed_books
    assert user.history[-1] == "返却: isbn1"

    # 借りていない本を返すと例外
    with pytest.raises(ValueError):
        user.return_book("isbn1")
